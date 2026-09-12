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

A band read as `*_band_partial` (some lines legible, band ends not visible) is
loaded as inscriptions PLUS an explicit incompleteness marker in `unknown`, so a
partially read face can never count as complete.

Transcriptions are tagged LOCAL (this agent read the image) or EXTERNAL (text
handoff only); `stats()` reports the two separately.
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
    def add_face(self, fid, utc=None, upper=None, lower=None, unknown=None, source=None,
                 local=False):
        f = self.faces.setdefault(fid, {"utc": None, "upper": [], "lower": [],
                                        "unknown": [], "sources": [], "local": False})
        if utc:
            f["utc"] = utc
        for key, val in (("upper", upper), ("lower", lower), ("unknown", unknown)):
            if val:
                for n in val:
                    if n not in f[key]:
                        f[key].append(n)
        if source and source not in f["sources"]:
            f["sources"].append(source)
        if local:
            f["local"] = True
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

    PSEUDO = ("lower", "half-hour")

    def sector_faces(self):
        """Nodes that denote one physical face. Excludes pseudo-nodes that name a
        band or a group rather than a face, so circumference is never overstated."""
        return [f for f in self.faces
                if not any(tok in f.lower() for tok in self.PSEUDO)]

    def stats(self, total_faces=24):
        obs = sum(1 for e in self.edges.values() if e["kind"] == "OBSERVED")
        sect = self.sector_faces()
        complete = [f for f in sect if self.face_complete(f)]
        with_upper = [f for f in sect if self.faces[f]["upper"]]
        with_lower = [f for f in sect if self.faces[f]["lower"]]
        upper_complete = [f for f in sect
                          if self.faces[f]["upper"]
                          and not any("upper" in u for u in self.faces[f]["unknown"])]
        lower_complete = [f for f in sect
                          if self.faces[f]["lower"]
                          and not any("lower" in u for u in self.faces[f]["unknown"])]
        return {
            "faces_total": total_faces,
            "faces_identified": len(sect),
            "pseudo_nodes_excluded": len(self.faces) - len(sect),
            "faces_with_upper_transcribed": len(with_upper),
            "faces_with_lower_transcribed": len(with_lower),
            "faces_upper_band_complete": len(upper_complete),
            "faces_lower_band_complete": len(lower_complete),
            "faces_complete": len(complete),
            "faces_complete_local": sum(1 for f in complete if self.faces[f]["local"]),
            "faces_locally_transcribed": sum(1 for f in sect if self.faces[f]["local"]),
            "edges_observed": obs,
            "edges_transitive": len(self.transitive_edges()),
            "circumference_fraction": len(sect) / total_faces,
            "longest_chain": max((len(c) for c in self.chains()), default=0),
        }


def load_from_photos(path=PHOTOS_PATH):
    """Build the graph from the photographic evidence dataset."""
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    g = DrumGraph()
    aliases = {k: v for k, v in doc.get("face_aliases", {}).items() if not k.startswith("_")}

    def norm(label):
        """Collapse descriptive labels and hedged sector strings onto one node name."""
        if label in aliases:
            return aliases[label]
        if "(" in label:
            label = label.split("(")[0].strip()
        return label

    for ph in doc["photographs"]:
        pid = ph["id"]
        is_local = bool(ph.get("self_transcribed"))
        local = {}
        for vf in ph.get("visible_faces", []) + ph.get("local_visual_faces", []):
            utc = vf.get("utc_sector")
            if utc:
                utc = norm(utc)
            # sector label IS the node name, so the same face seen in two photographs merges
            fid = utc if utc and utc != "UNKNOWN" else f"{pid}:{vf['face_ref']}"
            local[vf["face_ref"]] = fid
            up = vf.get("upper_band")
            lo = vf.get("lower_band")
            unknown = list(vf.get("names") or []) if isinstance(vf.get("names"), list) else []
            if not isinstance(up, list) and isinstance(vf.get("upper_band_partial"), list):
                up = vf["upper_band_partial"]
                unknown.append("upper band incomplete (band ends not visible)")
            if not isinstance(lo, list) and isinstance(vf.get("lower_band_partial"), list):
                lo = vf["lower_band_partial"]
                unknown.append("lower band incomplete (band ends not visible)")
            if not isinstance(up, list):
                unknown.append("upper band not read")
            if not isinstance(lo, list):
                unknown.append("lower band not read")
            g.add_face(fid, utc=utc,
                       upper=up if isinstance(up, list) else None,
                       lower=lo if isinstance(lo, list) else None,
                       unknown=unknown or None,
                       source=pid, local=is_local)
        for ad in ph.get("adjacency_observed", []):
            if "left" in ad and "right" in ad:
                pairs = [(ad["left"], ad["right"])]
            else:
                seq = ad.get("upper_sequence") or ad.get("lower_sequence") or []
                pairs = list(zip(seq, seq[1:]))
            for l, r in pairs:
                a = norm(local.get(l, l))
                b = norm(local.get(r, r))
                if a == b:
                    continue
                g.add_face(a, source=pid, local=is_local)
                g.add_face(b, source=pid, local=is_local)
                g.add_edge(a, b, kind=ad.get("kind", "OBSERVED"), source=pid)
    return g, doc
