"""Physical adjacency graph for the Weltzeituhr drum.

Nodes are physical FACES, not time-zone labels. Edges are left/right adjacency
observed in a photograph. The distinction the data model must protect:

  * the city cylinder is STATIC, the hour ring ROTATES, so an hour numeral under a
    face does NOT identify that face. Sectors are identified from CITY CONTENTS and
    adjacency only.
  * an edge is OBSERVED when one photograph shows both faces adjacent; it is
    TRANSITIVE when assembled from overlapping observations. Both are kept, and
    never conflated.

Each face stores ordered `upper` and `lower` inscriptions plus `unknown` entries.
A face is COMPLETE only when both bands are ordered and nothing is unknown.
"""

import json
import os
from collections import defaultdict

from .data import REPO_ROOT

PHOTOS_PATH = os.path.join(REPO_ROOT, "data", "weltzeituhr_photos.json")


class DrumGraph:
    def __init__(self):
        self.faces = {}          # face_id -> dict(utc, upper, lower, unknown, sources)
        self.edges = {}          # (a,b) -> dict(kind, sources)

    # ---------------------------------------------------------------- building
    def add_face(self, fid, utc=None, upper=None, lower=None, unknown=None, source=None):
        f = self.faces.setdefault(fid, {"utc": None, "upper": [], "lower": [],
                                        "unknown": [], "sources": []})
        if utc:
            f["utc"] = utc
        for key, val in (("upper", upper), ("lower", lower), ("unknown", unknown)):
            if val:
                for n in val:
                    if n not in f[key]:
                        f[key].append(n)
        if source and source not in f["sources"]:
            f["sources"].append(source)
        return f

    def add_edge(self, a, b, kind="OBSERVED", source=None):
        e = self.edges.setdefault((a, b), {"kind": kind, "sources": []})
        if kind == "OBSERVED":
            e["kind"] = "OBSERVED"          # observed always beats transitive
        if source and source not in e["sources"]:
            e["sources"].append(source)
        return e

    # ---------------------------------------------------------------- analysis
    def chains(self):
        """Maximal left-to-right chains of faces linked by any edge."""
        nxt = {a: b for (a, b) in self.edges}
        prv = {b: a for (a, b) in self.edges}
        starts = [f for f in self.faces if f not in prv]
        out = []
        for s in starts:
            chain, cur, seen = [s], s, {s}
            while cur in nxt and nxt[cur] not in seen:
                cur = nxt[cur]
                chain.append(cur)
                seen.add(cur)
            out.append(chain)
        return out

    def transitive_edges(self):
        """Edges implied by chaining but not directly observed."""
        implied = []
        for chain in self.chains():
            for i in range(len(chain)):
                for j in range(i + 2, len(chain)):
                    if (chain[i], chain[j]) not in self.edges:
                        implied.append((chain[i], chain[j]))
        return implied

    def face_complete(self, fid):
        f = self.faces[fid]
        return bool(f["upper"]) and bool(f["lower"]) and not f["unknown"]

    def stats(self, total_faces=24):
        obs = sum(1 for e in self.edges.values() if e["kind"] == "OBSERVED")
        complete = [f for f in self.faces if self.face_complete(f)]
        with_upper = [f for f in self.faces if self.faces[f]["upper"]]
        with_lower = [f for f in self.faces if self.faces[f]["lower"]]
        return {
            "faces_total": total_faces,
            "faces_identified": len(self.faces),
            "faces_with_upper_transcribed": len(with_upper),
            "faces_with_lower_transcribed": len(with_lower),
            "faces_complete": len(complete),
            "edges_observed": obs,
            "edges_transitive": len(self.transitive_edges()),
            "circumference_fraction": len(self.faces) / total_faces,
            "longest_chain": max((len(c) for c in self.chains()), default=0),
        }


def load_from_photos(path=PHOTOS_PATH):
    """Build the graph from the photographic evidence dataset."""
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    g = DrumGraph()
    for ph in doc["photographs"]:
        pid = ph["id"]
        local = {}
        for vf in ph.get("visible_faces", []):
            utc = vf.get("utc_sector")
            fid = f"{utc} [{pid[:12]}]" if utc and utc != "UNKNOWN" else f"{pid}:{vf['face_ref']}"
            # a face seen in more than one photograph merges under its sector label
            if utc and utc != "UNKNOWN" and any(utc == f.get("utc") for f in g.faces.values()):
                fid = next(k for k, f in g.faces.items() if f.get("utc") == utc)
            local[vf["face_ref"]] = fid
            up = vf.get("upper_band")
            lo = vf.get("lower_band")
            names = vf.get("names")
            g.add_face(fid, utc=utc,
                       upper=up if isinstance(up, list) else None,
                       lower=lo if isinstance(lo, list) else None,
                       unknown=names if isinstance(names, list) else None,
                       source=pid)
        for ad in ph.get("adjacency_observed", []):
            a, b = local.get(ad["left"]), local.get(ad["right"])
            if a and b:
                g.add_edge(a, b, kind="OBSERVED", source=pid)
    return g, doc
