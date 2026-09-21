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

Within one era, a PARTIAL reading of a band never degrades a COMPLETE reading of the
same band: if the partial's names are already in the complete list it is recorded as
corroboration from a second frame. A complete reading clears any incompleteness marker
an earlier partial left. Membership or order disagreements are CONFLICTS, recorded
rather than silently resolved. The first complete observation is preserved when
another complete observation disagrees. Conflicts block completeness.

Faces are keyed by (sector, era): the same sector photographed in two decades is two
nodes, because completeness is a per-era property and a later frame must never dilute
or complete an earlier transcription. Circumference counts DISTINCT SECTORS.

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
                 local=False, complete_bands=(), partial_bands=()):
        f = self.faces.setdefault(fid, {"utc": None, "upper": [], "lower": [],
                                        "unknown": [], "sources": [], "local": False,
                                        "complete_bands": [], "corroborated": [],
                                        "conflicts": []})
        if utc:
            f["utc"] = utc
        for band in complete_bands:
            val = list({"upper": upper, "lower": lower}[band] or [])
            if band in f["complete_bands"]:
                if val != f[band]:
                    f["conflicts"].append(
                        f"{source}: competing complete {band} order: {val}")
                continue  # preserve the first complete observation, even on conflict
            # a complete reading is AUTHORITATIVE: it REPLACES whatever partial readings
            # left behind, so the transcribed order is preserved exactly as read
            earlier = [n for n in f[band] if n not in val]
            if earlier:
                f["conflicts"].append(
                    f"{source}: complete {band} reading omits names an earlier partial reported: {earlier}")
            elif f[band] and [n for n in val if n in f[band]] != f[band]:
                f["conflicts"].append(f"{source}: complete {band} contradicts earlier partial order")
            elif f[band]:
                f["corroborated"].append(
                    f"earlier partial {band} reading is a subset of {source}'s complete reading")
            f[band] = val
            if band not in f["complete_bands"]:
                f["complete_bands"].append(band)
            f["unknown"] = [u for u in f["unknown"] if band not in u]
        for band in partial_bands:
            if band in f["complete_bands"]:
                # subset -> corroboration; anything else -> a conflict worth keeping
                new = [n for n in ({"upper": upper, "lower": lower}[band] or [])
                       if n not in f[band]]
                if new:
                    f["conflicts"].append(f"{source}: {band} names not in the complete reading: {new}")
                elif (observed := list({"upper": upper, "lower": lower}[band] or [])) != [
                        n for n in f[band] if n in observed]:
                    f["conflicts"].append(f"{source}: partial {band} contradicts complete order")
                elif source and source not in f["corroborated"]:
                    f["corroborated"].append(f"{source} corroborates {band}")
                continue
            marker = f"{band} band incomplete (band ends not visible)"
            if marker not in f["unknown"]:
                f["unknown"].append(marker)
        for key, val in (("upper", upper), ("lower", lower), ("unknown", unknown)):
            if key in complete_bands:
                continue          # already set authoritatively above
            if key in partial_bands and key in f["complete_bands"]:
                continue
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
        return (bool(f["upper"]) and bool(f["lower"]) and not f["unknown"]
                and not f["conflicts"]
                and all(b in f["complete_bands"] for b in ("upper", "lower")))

    PSEUDO = ("lower", "half-hour")

    @staticmethod
    def sector_of(fid):
        return fid.split(" @")[0]

    def sectors(self):
        """Distinct physical sectors identified, across all eras."""
        return sorted({self.sector_of(f) for f in self.sector_faces()})

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
                          and "upper" in self.faces[f]["complete_bands"]
                          and not self.faces[f]["conflicts"]
                          and not any("upper" in u for u in self.faces[f]["unknown"])]
        lower_complete = [f for f in sect
                          if self.faces[f]["lower"]
                          and "lower" in self.faces[f]["complete_bands"]
                          and not self.faces[f]["conflicts"]
                          and not any("lower" in u for u in self.faces[f]["unknown"])]
        return {
            "faces_total": total_faces,
            "sectors_identified": len(self.sectors()),
            "face_era_records": len(sect),
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
            "circumference_fraction": len(self.sectors()) / total_faces,
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
        era = ph.get("era", "unknown")
        is_local = bool(ph.get("self_transcribed"))
        local = {}
        for vf in ph.get("visible_faces", []) + ph.get("local_visual_faces", []):
            utc = vf.get("utc_sector")
            if utc:
                utc = norm(utc)
            fid = (f"{utc} @{era}" if utc and utc != "UNKNOWN"
                   else f"{pid}:{vf['face_ref']}")
            local[vf["face_ref"]] = fid
            up = vf.get("upper_band")
            lo = vf.get("lower_band")
            unknown = list(vf.get("names") or []) if isinstance(vf.get("names"), list) else []
            complete, partial = [], []
            for band, val in (("upper", up), ("lower", lo)):
                if isinstance(val, list):
                    complete.append(band)
                elif isinstance(vf.get(f"{band}_band_partial"), list):
                    partial.append(band)
                else:
                    unknown.append(f"{band} band not read")
            up = up if isinstance(up, list) else vf.get("upper_band_partial")
            lo = lo if isinstance(lo, list) else vf.get("lower_band_partial")
            g.add_face(fid, utc=utc,
                       upper=up if isinstance(up, list) else None,
                       lower=lo if isinstance(lo, list) else None,
                       unknown=unknown or None,
                       source=pid, local=is_local,
                       complete_bands=complete, partial_bands=partial)
        for ad in ph.get("adjacency_observed", []):
            if "left" in ad and "right" in ad:
                pairs = [(ad["left"], ad["right"])]
            else:
                seq = ad.get("upper_sequence") or ad.get("lower_sequence") or []
                pairs = list(zip(seq, seq[1:]))
            for l, r in pairs:
                a = local.get(l) or f"{norm(l)} @{era}"
                b = local.get(r) or f"{norm(r)} @{era}"
                if a == b:
                    continue
                g.add_face(a, source=pid, local=is_local)
                g.add_face(b, source=pid, local=is_local)
                g.add_edge(a, b, kind=ad.get("kind", "OBSERVED"), source=pid)
    return g, doc
