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
print(f"   faces verified by 1988-89 evidence   : {s['faces_identified']} (both from the Aug 1989 frame)")
print(f"   faces from older photos + stability  : 0 (stability UNTESTED)")
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
