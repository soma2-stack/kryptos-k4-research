"""EXP-028  Graph invariants: regression guards on the reconstruction dataset.

Adding the 1974 Straube frame silently destroyed the one complete face, because a second
photograph of the same sector merged in and its PARTIAL lower-band reading re-marked the
band incomplete. A first fix then silently REORDERED the lower band. Both were data-model
bugs that would have propagated into every downstream readiness claim, so they are pinned
here as assertions rather than trusted to review.

Run this after any change to data/weltzeituhr_photos.json or k4lib/wz_graph.py.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from k4lib.wz_graph import load_from_photos

g, doc = load_from_photos()
checks = []


def check(name, cond, detail=""):
    checks.append((name, bool(cond), detail))


CET = "UTC+1 @1970s"
f = g.faces.get(CET)
check("the CET 1970s face exists", f is not None)

UPPER = ["AMSTERDAM", "BERLIN", "BRUSSEL", "BUDAPEST", "MADRID", "PARIS", "PRAG",
         "STOCKHOLM", "WARSCHAU"]
LOWER = ["KOPENHAGEN", "LONDON", "WIEN", "ROM", "BELGRAD", "TUNIS"]

check("CET upper band verbatim, in transcribed order", f["upper"] == UPPER, str(f["upper"]))
check("CET lower band verbatim, in transcribed order", f["lower"] == LOWER, str(f["lower"]))
check("CET face carries no unknowns", f["unknown"] == [], str(f["unknown"]))
check("CET face is COMPLETE", g.face_complete(CET))
check("CET letter total is 97",
      sum(len(n.replace(" ", "")) for n in f["upper"] + f["lower"]) == 97)
check("the 1974 frame is recorded as corroboration, not as new data",
      any("subset" in c for c in f["corroborated"]), str(f["corroborated"]))
check("no unresolved conflicts on the CET face", f["conflicts"] == [], str(f["conflicts"]))

# era separation
check("faces are keyed by (sector, era), never merged across eras",
      all(" @" in k or ":" in k for k in g.faces))
check("a sector seen in two eras yields two records, not one",
      len(g.sector_faces()) > len(g.sectors()))
check("circumference counts distinct sectors, not face-era records",
      g.stats()["circumference_fraction"] == len(g.sectors()) / 24)

# no target-era completeness may be claimed
tgt = [k for k in g.sector_faces() if k.endswith("@1988-89") and g.face_complete(k)]
check("NO complete face is claimed for the 1988-89 target era", not tgt, str(tgt))

# every face-era record traces to a photograph with an era
ids = {p["id"] for p in doc["photographs"]}
check("every photograph declares an era", all("era" in p for p in doc["photographs"]))
check("every face traces to a catalogued photograph",
      all(any(s in ids for s in v["sources"]) for v in g.faces.values()))

print("# EXP-028 graph invariants\n")
bad = 0
for name, ok, detail in checks:
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        bad += 1
        print(f"          got: {detail}")
print(f"\n   {len(checks) - bad}/{len(checks)} invariants hold")
if bad:
    print("\n   REGRESSION. Do not report readiness metrics until these pass.")
sys.exit(1 if bad else 0)
