"""EXP-025  Reconstruction readiness gate, and why the modern list cannot stand in.

This experiment does not test a cipher. It does three things that protect the
integrity of the Weltzeituhr programme:

  1. reports per-sector readiness of the pre-1997 reconstruction and shows the
     guard in `k4lib.wz_panels.build_clock` refusing to fabricate a historical
     clock from incomplete data;
  2. QUANTIFIES the cost of substituting the modern list for the historical one -
     converting "do not use the modern clock" from an instruction into a measured
     probability;
  3. states the power the preregistered EXP-024 will have once the data exists, so
     that a future hit can be judged against a number fixed in advance.
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load
from k4lib.wz_panels import load_panels, summary, build_clock, ReconstructionIncomplete

k4 = load()
panels = load_panels()

print("# EXP-025 reconstruction readiness gate")
print(f"ciphertext sha256 {k4.sha256}\n")

counts, rows = summary(panels)
print("## Per-sector readiness, PRE-1997 reconstruction")
print(f"   {counts}")
for off, state, conf in rows:
    if state != "UNKNOWN":
        print(f"   UTC{off:+d}  {state}  {conf}")
print()

print("## The guard")
try:
    build_clock(panels)
    print("   build_clock SUCCEEDED - this would be a bug given the data above")
except ReconstructionIncomplete as e:
    print("   build_clock REFUSED, as it must:")
    print(f"     {str(e)[:110]}...")
print("   A historical clock cannot be produced by accident. Filling UNKNOWN")
print("   sectors from modern names requires deliberately passing")
print("   allow_incomplete=True, which stamps the result NOT historical.\n")

cs = panels["change_set_1997"]
print("## 1997 change set recovered so far")
print(f"   additions documented : {len(cs['additions_documented'])} of "
      f"{cs['additions_total_reported']} reported "
      f"({cs['additions_still_unnamed']} still unnamed)")
for a in cs["additions_documented"]:
    print(f"     + {a['name']}  [{a['confidence']}]")
print(f"   renames documented   : {len(cs['renames_documented'])}")
for r in cs["renames_documented"]:
    print(f"     ~ {r['from']} -> {r['to']}")
print(f"   zone moves documented: {len(cs['zone_moves_documented'])} "
      f"({cs['zone_moves_documented'][0]['name']}; from/to UNKNOWN)")
print(f"   removals             : {cs['removals']}")
print()

print("## Why the modern list cannot be substituted - measured, not asserted")
TOTAL, ADDED = 146, 20
PRE = TOTAL - ADDED
print(f"   {ADDED} of {TOTAL} modern names were added in 1997, so {PRE} are pre-1997.")
print("   A 97-letter keystream window covers roughly 97/L names for mean name")
print("   length L. Probability that such a window contains NO post-1997 addition,")
print("   under a hypergeometric draw without replacement:\n")
print("   mean name length L   names per window   P(window free of 1997 additions)")
for L in (6, 7, 8, 9):
    k = max(1, round(97 / L))
    p = 1.0
    for j in range(k):
        p *= (PRE - j) / (TOTAL - j)
    print(f"        {L}                   {k:>2}                    {p:.3f}")
print()
print("   So roughly 85-90% of windows of the MODERN tape are contaminated by at")
print("   least one name that did not exist when Sanborn was working. Testing the")
print("   modern list as a proxy would be wrong most of the time, and a negative")
print("   from it would carry almost no information about the historical clock.")
print("   This is the quantitative justification for not taking the shortcut.\n")

print("## A complication Checkpoint E did not account for")
w = panels["post_1997_changes_warning"]
print(f"   {w['value']}")
print(f"   {w['implication']}")
print("   Reversing 1997 alone is therefore NOT sufficient; the 2015 change set is")
print("   also UNKNOWN and must be reversed too.\n")

print("## Power of the preregistered test, fixed in advance")
NAMES, LMEAN = TOTAL, 7
tape = NAMES * LMEAN
align = 22 * 2 * 2 * tape * 12
print(f"   tape length, approx        : {tape} letters ({NAMES} names x {LMEAN})")
print(f"   alignments EXP-024 will try : ~{align:,}")
print(f"   expected false 24/24 hits   : {align * 26.0**-24:.2e}")
print("   So a single exact hit, when the data exists, would be decisive. The")
print("   weakness is not power - it is that circular readings share substrings,")
print("   so the alignments are NOT independent and a naive correction misstates")
print("   the null. EXP-024's control recovered one planted key under THREE")
print("   procedure labels; that dependency must be reported, not corrected away.\n")

print("## Grade")
print("   Blocker 1 (modern per-sector list): NOT CLOSED IN THIS ENVIRONMENT.")
print("   Verified at three levels - WebFetch returns EGRESS_BLOCKED for every")
print("   external domain; curl reports 'connect_rejected (organization policy)'")
print("   while pypi.org returns HTTP 200, so it is a domain policy and not a")
print("   general network failure; and search summaries decline to enumerate,")
print("   correctly refusing rather than inventing a list.")
print("   Blockers 2-4: PARTIALLY CLOSED - 5 of 20 additions, 4 renames, 1 zone")
print("   move, 0 removals.")
print("   Blockers 5-6 (band assignment, orientation): UNCHANGED, UNKNOWN.")
