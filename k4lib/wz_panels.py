"""Loading, validating and gating the Weltzeituhr panel reconstruction.

The panel matrix (data/weltzeituhr_panels.json) is deliberately separate from the
reading procedures (k4lib/weltzeituhr.py). Nothing may collapse the clock into a
running text until the per-sector reconstruction is real.

`build_clock` REFUSES to produce a structure while sectors are UNKNOWN. That is a
guard, not a formality: the failure mode this project must avoid is a future
session quietly filling UNKNOWN sectors with modern names and then reporting a
"historical" result. The guard makes that impossible without deliberately passing
`allow_incomplete=True`, which stamps the output as NOT historical.
"""

import json
import os

from .data import REPO_ROOT

PANELS_PATH = os.path.join(REPO_ROOT, "data", "weltzeituhr_panels.json")


class ReconstructionIncomplete(RuntimeError):
    """Raised when a historical clock is requested but the data is not there."""


def load_panels(path=PANELS_PATH):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def readiness(panels=None):
    """Per-sector readiness for the PRE-1997 reconstruction."""
    panels = panels or load_panels()
    rows = []
    for key, s in panels["sectors"].items():
        up, lo = s.get("pre1997_upper"), s.get("pre1997_lower")
        frag = s.get("pre1997_fragment")
        if up not in (None, "UNKNOWN") and lo not in (None, "UNKNOWN"):
            state = "COMPLETE"
        elif frag:
            state = "FRAGMENT"
        else:
            state = "UNKNOWN"
        rows.append((int(key), state, s.get("confidence", "UNKNOWN")))
    rows.sort()
    return rows


def summary(panels=None):
    rows = readiness(panels)
    counts = {}
    for _, state, _ in rows:
        counts[state] = counts.get(state, 0) + 1
    return counts, rows


def build_clock(panels=None, era="pre1997", allow_incomplete=False):
    """Convert the panel matrix into the structure k4lib.weltzeituhr consumes.

    Refuses unless every sector carries both bands for the requested era.
    """
    panels = panels or load_panels()
    ukey, lkey = f"{era}_upper", f"{era}_lower"
    sectors, missing = [], []
    for key in sorted(panels["sectors"], key=int):
        s = panels["sectors"][key]
        up, lo = s.get(ukey), s.get(lkey)
        if up in (None, "UNKNOWN") or lo in (None, "UNKNOWN"):
            missing.append(key)
            up = up if isinstance(up, list) else []
            lo = lo if isinstance(lo, list) else []
        sectors.append({"upper": list(up), "lower": list(lo)})
    if missing and not allow_incomplete:
        raise ReconstructionIncomplete(
            f"{len(missing)} of {len(sectors)} sectors lack a {era} band assignment: "
            f"{missing}. Supply them from evidence, or pass allow_incomplete=True "
            f"to build a structure explicitly marked NOT historical.")
    return {"sectors": sectors,
            "utc_offset": [int(k) for k in sorted(panels["sectors"], key=int)],
            "era": era,
            "complete": not missing,
            "missing_sectors": missing}


def ingest_modern_list(panels, per_sector, source, note=""):
    """Record a published MODERN per-sector list into the matrix.

    `per_sector` maps a UTC offset (int or str) to a list of names IN PUBLISHED
    ORDER. The published order is stored as `modern_names_unsplit`; it is NOT
    split into upper and lower bands, because table order is not evidence of
    physical placement.
    """
    for off, names in per_sector.items():
        key = str(int(off))
        if key not in panels["sectors"]:
            raise KeyError(f"sector {key} is outside the displayed range")
        s = panels["sectors"][key]
        s["modern_names_unsplit"] = list(names)
        s["sources"] = sorted(set(s.get("sources", []) + [source]))
        if note:
            s["modern_note"] = note
    return panels
