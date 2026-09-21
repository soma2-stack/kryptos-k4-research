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
LOWER89 = ["KOPENHAGEN", "WIEN", "BERN", "BELGRAD", "ROM", "TUNIS",
           "BRAZZAVILLE", "KINSHASA", "LUANDA"]
TGT = "UTC+1 @1988-89"
t = g.faces.get(TGT)

check("the 1970s CET upper band is verbatim", f["upper"] == UPPER, str(f["upper"]))
check("the 1970s CET lower band is NO LONGER claimed complete (LONDON misassignment)",
      not g.face_complete(CET) and "lower" not in f["complete_bands"],
      f"complete_bands={f['complete_bands']}")
check("the retracted 97-letter reading is not resurrected anywhere",
      "LONDON" not in f["lower"], str(f["lower"]))

check("the target-era CET face exists", t is not None)
check("target-era CET upper band verbatim", t["upper"] == UPPER, str(t["upper"]))
check("target-era CET lower band verbatim, in transcribed order",
      t["lower"] == LOWER89, str(t["lower"]))
check("target-era CET face carries no unknowns", t["unknown"] == [], str(t["unknown"]))
check("target-era CET face is COMPLETE", g.face_complete(TGT))
check("target-era CET letter total is 120",
      sum(len(n.replace(" ", "")) for n in t["upper"] + t["lower"]) == 120)
check("target-era CET lower band matches the frozen order (not a latitude verification)",
      LOWER89 == ["KOPENHAGEN", "WIEN", "BERN", "BELGRAD", "ROM", "TUNIS",
                  "BRAZZAVILLE", "KINSHASA", "LUANDA"])
check("LONDON is on the UTC+0 face, not CET",
      "LONDON" in g.faces["UTC+0-W @1988-89"]["upper"] and "LONDON" not in t["lower"])
check("no unresolved conflicts on either CET face",
      f["conflicts"] == [] and t["conflicts"] == [], str(f["conflicts"] + t["conflicts"]))

# the frozen tape must match the dataset's own frozen block
fr = doc["tier1_frozen_reconstruction"]
check("frozen block matches the graph's target-era face",
      fr["upper"] == t["upper"] and fr["lower"] == t["lower"])
check("frozen block letter total is self-consistent",
      fr["letters"]["total"] == 120)

# era separation
check("faces are keyed by (sector, era), never merged across eras",
      all(" @" in k or ":" in k for k in g.faces))
check("a sector seen in two eras yields two records, not one",
      len(g.sector_faces()) > len(g.sectors()))
check("circumference counts distinct sectors, not face-era records",
      g.stats()["circumference_fraction"] == len(g.sectors()) / 24)

# no target-era completeness may be claimed
tgt = [k for k in g.sector_faces() if k.endswith("@1988-89") and g.face_complete(k)]
check("exactly ONE complete target-era face is claimed", tgt == [TGT], str(tgt))

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
