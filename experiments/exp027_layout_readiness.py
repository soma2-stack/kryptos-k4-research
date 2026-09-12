"""EXP-027  Layout readiness: what must be known before EXP-024 may legitimately run.

Checkpoint G showed the binding constraint is WHERE names sat, not which names.
This experiment turns that into an operational threshold, and measures progress
against it.

The key refinement: the threshold is NOT "reconstruct the whole drum". A running-key
test needs a contiguous 97-letter window. So a CONTIGUOUS ARC of fully reconstructed
faces whose letters total >= 97 already permits a restricted, honest run of EXP-024 -
covering exactly those alignments whose window falls inside the known arc, with the
restriction reported. That is a principled restriction of the preregistered space,
not a modification of it, and it is far more achievable than the full circumference.
"""
import sys, os, json, math, collections, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load, REPO_ROOT
from k4lib.wz_graph import load_from_photos

k4 = load()
g, photos = load_from_photos()
mod = json.load(open(os.path.join(REPO_ROOT, "data", "weltzeituhr_modern_official.json"), encoding="utf-8"))
byzone = collections.defaultdict(list)
for p in mod["places"]:
    byzone[p["utc_zone"]].append(p["name"])


def norm(s):
    s = s.upper().replace("Ä", "AE").replace("Ö", "OE").replace("Ü", "UE")
    return re.sub(r"[^A-Z]", "", s)


print("# EXP-027 layout readiness")
print(f"ciphertext sha256 {k4.sha256}\n")

print("## Photographic evidence catalogued")
for ph in photos["photographs"]:
    st = "self-transcribed" if ph.get("self_transcribed") else "NOT self-transcribed"
    print(f"   {ph['id']:<38} {str(ph['date']):<11} {st}")
    print(f"      date confidence: {ph['date_confidence']}")
print()
print(f"   {photos['environment_limitation'][:78]}...")
print()

s = g.stats()
print("## Layout reconstruction metric")
print(f"   faces total                          : {s['faces_total']}")
print(f"   faces identified                     : {s['faces_identified']}")
print(f"   faces with UPPER band transcribed    : {s['faces_with_upper_transcribed']}")
print(f"   faces with LOWER band transcribed    : {s['faces_with_lower_transcribed']}")
print(f"   faces COMPLETE (both bands, ordered) : {s['faces_complete']}")
print(f"   adjacency edges OBSERVED             : {s['edges_observed']}")
print(f"   adjacency edges TRANSITIVE           : {s['edges_transitive']}")
print(f"   circumference fraction identified    : {s['circumference_fraction']*100:.1f}%")
print(f"   longest contiguous chain             : {s['longest_chain']} faces")
by_era = {"1988-89": 0, "1984": 0, "mid-1970s": 0}
for fid, f in g.faces.items():
    srcs = " ".join(f["sources"])
    if "1989" in srcs:
        by_era["1988-89"] += 1
    elif "1984" in srcs:
        by_era["1984"] += 1
    elif "1970" in srcs:
        by_era["mid-1970s"] += 1
print(f"   faces from 1988-89 evidence          : {by_era['1988-89']}")
print(f"   faces from 1984 evidence only        : {by_era['1984']}")
print(f"   faces from mid-1970s evidence only   : {by_era['mid-1970s']}")
print(f"   faces usable for 1989 via stability  : 0 (stability UNPROVEN - see below)")
print()

print("## Letters per face, and what a 97-letter window needs")
lens = {}
for z, names in byzone.items():
    if ":" in z:
        continue
    lens[z] = sum(len(norm(n)) for n in names)
order = [f"UTC{'+' if i >= 0 else ''}{i}" if i != 0 else "UTC±0" for i in range(-10, 14)]
order = [z for z in order if z in lens]
print(f"   total letters across 24 faces: {sum(lens.values())}")
big = sorted(lens.items(), key=lambda kv: -kv[1])[:6]
print("   largest faces: " + ", ".join(f"{z}={n}" for z, n in big))
print()
print("   Minimal contiguous ARCS reaching 97 letters (sliding around the drum):")
best = []
n = len(order)
for start in range(n):
    tot, arc = 0, []
    for k in range(n):
        z = order[(start + k) % n]
        arc.append(z)
        tot += lens[z]
        if tot >= 97:
            best.append((len(arc), tot, list(arc)))
            break
best.sort()
seen = set()
for L, tot, arc in best:
    key = tuple(sorted(arc))
    if key in seen:
        continue
    seen.add(key)
    if L <= 3:
        print(f"      {L} faces, {tot} letters: {' - '.join(arc)}")
minfaces = best[0][0] if best else None
print(f"\n   MINIMUM faces needed for one 97-letter window: {minfaces}")
print()

print("## The threshold, stated explicitly")
print("   TIER 1 - RESTRICTED RUN PERMITTED:")
print(f"     one contiguous arc of COMPLETE faces (both bands, order known) totalling")
print(f"     >= 97 letters. Currently {s['faces_complete']} faces are complete, so: NOT MET.")
print("     A restricted run must report what fraction of the preregistered alignment")
print("     space it covers, and may not be presented as the full EXP-024.")
print("   TIER 2 - FULL PREREGISTERED RUN PERMITTED:")
print("     all 24 faces complete, plus the 1997 reversal applied. Currently: NOT MET.")
print()
print("   Neither tier is met. EXP-024 remains frozen and unrun.\n")

# ---------------------------------------------------------------- UTC+1 status
UP70 = ["AMSTERDAM","BERLIN","BRUSSEL","BUDAPEST","MADRID","PARIS","PRAG","STOCKHOLM","WARSCHAU"]
LOWSUB = ["KOPENHAGEN","WIEN","BELGRAD","TUNIS"]
u = sum(len(w) for w in UP70); l = sum(len(w) for w in LOWSUB)
print("## Tier-1 status of the UTC+1 face, in detail")
print(f"   UPPER band  : {len(UP70)} names, ORDERED, {u} letters   [EXTERNAL-AGENT, mid-1970s]")
print(f"   LOWER band  : INCOMPLETE. {len(LOWSUB)} readable names ({l} letters), full")
print( "                 membership and order UNKNOWN; the source states the lower")
print( "                 band is not sharp enough for a responsible transcription.")
print(f"   attested letters so far : {u+l}")
print(f"   Tier-1 requirement      : 97 letters IN A COMPLETE FACE")
print(f"   naive shortfall         : {97-(u+l)} letters")
print()
print("   BUT THE NAIVE SHORTFALL IS MISLEADING, and this matters:")
print("   Tier-1 requires a COMPLETE face, not 97 attested letters. A partially read")
print("   band yields a tape with UNKNOWN GAPS at unknown positions, which cannot be")
print("   used as a keystream at all. The modern lower band holds 9 names; the")
print("   historical one holds an unknown number of which 4 are legible. Until the")
print("   full membership AND order of the historical lower band are known, the face")
print("   is not complete and Tier-1 is NOT met - however close the letter count gets.")
print()
print("## The date problem - the most serious issue in the new evidence")
print("   1969 original: 80 names. Added in 1997: ~20. Implied total: ~100.")
print(f"   Actual modern total: 146. UNEXPLAINED: 46 names.")
print("   So ~46 names entered at some time OTHER than 1997. If any entered between")
print("   1969 and 1997, the clock was still growing during the target period, and a")
print("   MID-1970s photograph is not evidence for 1989 without demonstrated")
print("   stability. Source 3's nine-name UTC+1 upper band may be an earlier, smaller")
print("   state of that face. Casablanca - the one modern-upper name absent from it -")
print("   is consistent with a later addition, though it could simply be obscured.")
print()
print("## Stability, first data point")
print("   The UTC+10 face carries CHABAROWSK in BOTH the April 1984 and the August")
print("   1989 frames. No contradiction - but a single name shows only that this name")
print("   did not move, not that the face is unchanged. Stability remains UNPROVEN,")
print("   and it is now the pivotal question, because it decides whether pre-1989")
print("   photographs may be used for the 1989 state at all.")
print()
print("## Where further photographs are worth most")
ent = []
for z, names in byzone.items():
    if ":" in z:
        continue
    k = len(names)
    ent.append((math.log10(math.factorial(k)) + k * math.log10(2), z, k))
ent.sort(reverse=True)
tot = sum(e[0] for e in ent)
print("   face      names   share of remaining layout entropy")
for lg, z, k in ent[:6]:
    print(f"   {z:<9} {k:>5}    {lg/tot*100:>5.1f}%")
print(f"\n   UTC+1, +2 and +3 together carry "
      f"{sum(e[0] for e in ent if e[1] in ('UTC+1','UTC+2','UTC+3'))/tot*100:.1f}% of the total.")
print("   The Aug 1989 frame in hand shows UTC+10 and UTC+11 - between them "
      f"{sum(e[0] for e in ent if e[1] in ('UTC+10','UTC+11'))/tot*100:.1f}% of the entropy.")
print("   So the single highest-value acquisition is a legible pre-1997 photograph of")
print("   the EUROPEAN side of the drum, not more Pacific frames.")
