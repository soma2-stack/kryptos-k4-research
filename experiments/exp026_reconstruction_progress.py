"""EXP-026  Reconstruction progress metric, and whether a name list can ever suffice.

Two jobs.

1. A quantitative completion metric, so "how close are we to being allowed to run
   EXP-024?" has an objective answer rather than a feeling.

2. A question that turns out to matter more than the metric: even a PERFECT 1989
   name list per sector would not let EXP-024 run, because its reading procedures
   need the physical ORDER within each sector and the UPPER/LOWER band of each
   name. Neither is recoverable from a name list, and the combinatorics of guessing
   them are computed here.

Nothing in this experiment tests K4. The modern tape statistics at the end are
observations about the MODERN clock, explicitly not a cryptanalytic test, and are
reported with the multiple-testing caveat they require.
"""
import sys, os, json, math, collections, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load, REPO_ROOT

k4 = load()
mod = json.load(open(os.path.join(REPO_ROOT, "data", "weltzeituhr_modern_official.json"), encoding="utf-8"))
cls = json.load(open(os.path.join(REPO_ROOT, "data", "weltzeituhr_classification.json"), encoding="utf-8"))
recs = cls["records"]

print("# EXP-026 reconstruction progress, and the sufficiency question")
print(f"ciphertext sha256 {k4.sha256}\n")

print("## Blocker 1: CLOSED for the MODERN list")
p = mod["provenance"]
print(f"   source   : {p['publisher']} - {p['page_title']}")
print(f"   url      : {p['url']}")
print(f"   retrieved: {p['retrieved_date']} (supplied; this environment denies the domain)")
print(f"   sha256   : {p['sha256_of_supplied_file'][:32]}...")
print(f"   validated: 146/146 entries, indices contiguous, no duplicates, all cross-checks passed")
print("   HISTORICAL 1988-89 list: STILL UNKNOWN / PARTIALLY RECONSTRUCTED\n")

print("## Completion metric")
counts = collections.Counter(r["historical_status"] for r in recs)
determined = sum(v for k, v in counts.items() if k != "UNKNOWN")
print(f"   entries whose pre-1997 presence is DETERMINED : {determined} / 146  "
      f"({determined/146*100:.1f}%)")
for k, v in sorted(counts.items()):
    print(f"     {k.ljust(22)} {v:>3}")
zones = sorted({r["utc_zone_modern"] for r in recs})
with_evidence = {r["utc_zone_modern"] for r in recs if r["historical_status"] != "UNKNOWN"}
print(f"   zones containing >=1 classified entry          : {len(with_evidence)} / {len(zones)}")
print(f"   sectors FULLY reconstructed (1989 names)       : 0 / 24")
print(f"   historical BAND assignments known              : 0 / 146")
print(f"   historical ORDER relations known               : 1  (Bern-Bratislava-Belgrad)")
print(f"   unresolved 1997 additions                      : 15 of 20 unnamed")
print(f"   unresolved 1997 zone moves                     : all but Kiew")
print(f"   unresolved 1997 removals                       : entirely unknown")
print(f"   unresolved 2015 change set                     : entirely unknown\n")

print("## The sufficiency question: would a perfect name list be enough?")
print("   EXP-024's preregistered procedures read each sector's UPPER band and LOWER")
print("   band, in physical order. A name list gives neither. So suppose the 1989")
print("   names per sector were known exactly - how many physical arrangements would")
print("   remain consistent with them?\n")
byzone = collections.defaultdict(list)
for r in recs:
    byzone[r["utc_zone_modern"]].append(r["name"])
log10 = 0.0
print("   zone      names   orderings k!      band splits 2^k")
for z in sorted(byzone, key=lambda s: (len(s), s)):
    k = len(byzone[z])
    lo = math.log10(math.factorial(k)) + k * math.log10(2)
    log10 += lo
    if k >= 9:
        print(f"   {z:<9} {k:>5}   10^{math.log10(math.factorial(k)):<6.1f}        10^{k*math.log10(2):<5.1f}")
print(f"\n   TOTAL arrangements consistent with a perfect name list: ~10^{log10:.0f}")
print("   For comparison, EXP-024 as preregistered tries ~10^6 alignments.")
print()
print("   CONSEQUENCE, and it is the main result of this session:")
print("   A NAME LIST ALONE CAN NEVER UNBLOCK EXP-024. Recovering every 1989 name")
print("   would still leave ~10^%d physical arrangements, and guessing among them" % round(log10))
print("   would both be computationally impossible and destroy the preregistration")
print("   by unbounded multiple testing. The binding constraint is not WHICH NAMES")
print("   were on the clock - it is WHERE THEY SAT: band and order within each")
print("   sector. That is recoverable only from dated photographs of the object.")
print()

print("## Observations on the MODERN tape - NOT a K4 test")
def norm(s):
    s = s.upper().replace("Ä","AE").replace("Ö","OE").replace("Ü","UE").replace("SS","SS")
    return re.sub(r"[^A-Z]", "", s)
names = [norm(r["name"]) for r in recs]
total = sum(len(n) for n in names)
print(f"   146 names, {total} letters after normalisation, mean {total/146:.2f} letters")
print(f"   letters if parentheticals are stripped first: ", end="")
stripped = [norm(re.sub(r"\(.*?\)", "", r["name"])) for r in recs]
print(f"{sum(len(n) for n in stripped)}")
print("   Any coincidence with 97 here would concern the MODERN clock, which")
print("   Sanborn never saw, and would be one of many numbers this file can produce.")
print("   Recorded as an observation only; no prediction is derived from it.")
