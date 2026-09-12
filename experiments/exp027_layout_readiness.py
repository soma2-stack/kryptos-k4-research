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
print(f"   SECTORS identified (distinct faces)  : {s['sectors_identified']}")
print(f"   face-era records (sector x era)      : {s['face_era_records']}")
print(f"   faces with UPPER band transcribed    : {s['faces_with_upper_transcribed']}")
print(f"   faces with LOWER band transcribed    : {s['faces_with_lower_transcribed']}")
print(f"   faces with UPPER band COMPLETE       : {s['faces_upper_band_complete']}")
print(f"   faces with LOWER band COMPLETE       : {s['faces_lower_band_complete']}")
print(f"   faces COMPLETE (both bands, ordered) : {s['faces_complete']}")
print(f"   ... of those, LOCAL VISUAL evidence  : {s['faces_complete_local']}")
print(f"   faces locally transcribed by me      : {s['faces_locally_transcribed']}")
print(f"   pseudo-nodes excluded from the count : {s['pseudo_nodes_excluded']} (band/group labels, not faces)")
print(f"   adjacency edges OBSERVED             : {s['edges_observed']}")
print(f"   adjacency edges TRANSITIVE           : {s['edges_transitive']}")
print(f"   circumference fraction identified    : {s['circumference_fraction']*100:.1f}%")
print(f"   longest contiguous chain             : {s['longest_chain']} faces")
import collections as _c
by_era = _c.Counter(f.split(" @")[-1] for f in g.sector_faces())
for era in ("1988-89", "1984", "1970s", "modern"):
    label = {"1988-89": "faces from 1988-89 evidence",
             "1984": "faces from 1984 evidence",
             "1970s": "faces from 1970s evidence (incl. CET)",
             "modern": "faces from MODERN evidence (rules only)"}[era]
    print(f"   {label:<37}: {by_era.get(era, 0)}")
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
import json as _json
FR = _json.load(open(os.path.join(REPO_ROOT, "data", "weltzeituhr_photos.json"),
                     encoding="utf-8"))["tier1_frozen_reconstruction"]
print("## Tier-1 status of the UTC+1 (Berlin / CET) face")
print(f"   UPPER : {len(FR['upper'])} names, ORDERED (alphabetical), {FR['letters']['upper']} letters"
      f"   [{FR['confidence']['upper']}]")
print(f"   LOWER : {len(FR['lower'])} names, ORDERED (strictly latitude-descending),"
      f" {FR['letters']['lower']} letters   [{FR['confidence']['lower']}]")
print(f"   TOTAL : {FR['letters']['total']} letters, from a TARGET-ERA photograph (4 Nov 1989)")
print()
print("   TIER 1 IS MET, for the first time in this programme:")
print("     (a) complete contiguous tape >= 97 letters   -> SATISFIED (120)")
print("     (b) attested for the 1988-89 target era      -> SATISFIED (4 Nov 1989, and the")
print("         date is corroborated by image content - NEUES FORUM and SDP banners - not")
print("         by caption metadata alone)")
print()
print("   The restricted run permitted by this rule was executed as EXP-029. EXP-024 itself")
print("   is unmodified and was not re-run. Result: NEGATIVE, best alignment 7/24 cribs")
print("   against a chance mean of 0.92, criterion 24/24, 11,520 alignments, positive")
print("   control passed on the real tape.")
print()
print("## RETRACTION: the 97-letter reading was my own transcription error")
print("   Session 10 reported this face as 62 + 35 = 97 letters, exactly K4's length, from a")
print("   1970s colour frame. The target-era photograph at much higher resolution refutes it:")
print("     - LONDON is in the UPPER band of the NEIGHBOURING UTC+0 face, not in CET lower;")
print("       I imported it across a sector boundary from a foreshortened view.")
print("     - BERN was missed entirely.")
print("     - BRAZZAVILLE, KINSHASA and LUANDA were missed - all genuinely UTC+1.")
print("     - the 'one inversion (ROM before BELGRAD)' was an artefact; the real band is")
print("       strictly latitude-ordered, which is now a check my reading passes.")
print("   The real face carries 120 letters. THE 97 IS WITHDRAWN ENTIRELY.")
print("   It was graded OBSERVATION, NOT EVIDENCE and explicitly refused as grounds to run")
print("   EXP-024, so nothing downstream was built on it. That refusal is the only reason")
print("   this is a corrected error and not a wasted programme.")
print()
print("## Stability of this face, 1970s -> 1989")
print("   No contradiction on anything still trustworthy: the upper band matches 9/9 exactly,")
print("   names and order. Five of the nine 1989 lower names are legible in the 1970s frame;")
print("   BERN, BRAZZAVILLE, KINSHASA and LUANDA are unresolved there - neither confirmed nor")
print("   excluded. SUPPORTED, and now secondary: direct target-era attestation supersedes it.")
print()
print("## Physical rules established this checkpoint (era-independent)")
print("   1. Half-hour zones are inscribed with a literal '+30' suffix: NEW DELHI +30,")
print("      COLOMBO +30, RANGUN +30, KABUL +30. LOCAL VISUAL, and independently")
print("      confirming the 2019 report of a '+ 30' inscription. Consequence: a tape")
print("      reading crossing those faces must choose whether to skip or transliterate")
print("      the digits - a free choice, hence a degree of freedom to be penalised.")
print("   2. RETRACTED: 'upper = northern, lower = southern'. The target-era CET face")
print("      has KOPENHAGEN (55.7 N) in the LOWER band while MADRID (40.4 N) is UPPER,")
print("      and the lower band mixes northern European with sub-Saharan African places.")
print("      The rule holds on the Asian faces observed but is not the drum's organising")
print("      principle. The 2^k layout-entropy reduction claimed last session is")
print("      WITHDRAWN. Downgraded CONFIRMED -> LOCAL REGULARITY.")
print("   3. RETRACTED: 'upper alphabetical, lower not' as a global rule. In the 1989")
print("      frame CET upper is alphabetical, but UTC+0 upper is strictly")
print("      latitude-descending (64.1 to 11.9) and not alphabetical; CET lower is")
print("      latitude-descending; UTC+0 lower is neither. ORDER DOES NOT FOLLOW FROM")
print("      MEMBERSHIP. The hope that it might - which made reconstruction look")
print("      tractable - is withdrawn: each face's order must be read from a photograph.")
print()
print("## Stability: now a demonstrated NEGATIVE")
print("   NOWOSIBIRSK sits with KRASNOJARSK in the April 1984 frame and with")
print("   OMSK/ALMATY/TASCHKENT in the modern frame. A place CHANGED faces. LOCAL")
print("   VISUAL at both ends. Consequence: backward reversal from the modern list")
print("   cannot assume a place keeps its face, so membership must be read per era.")
print("   This is the strongest single argument against reconstructing 1988-89 from")
print("   the modern list plus a change log.")
print("   Within the target window stability is UNTESTED, not established: I hold no")
print("   two frames of the SAME face in two different target-era years.")
print()
print("## Target-era toponyms that differ from the modern list")
print("   SWERDLOWSK (mod. Jekaterinburg), ASCHCHABAD, ALMA-ATA (mod. ALMATY),")
print("   LENINGRAD, PHOENGJANG (mod. PJOENGJANG). LOCAL VISUAL.")
print("   LENINGRAD is now confirmed IN THE TARGET ERA (4 Nov 1989 frame), alongside")
print("   MURMANSK and KIEW on the same face - so this is no longer an inference from")
print("   1984 and a 1970s frame.")
print("   At least five target-era names differ, so the target-era LETTER MULTISET")
print("   differs from the modern one. The Soviet-zone blocker is real and reaches")
print("   individual spellings, not just zone boundaries.")
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
print("   So more Pacific frames are near-worthless now. CET is fully read; UTC+2 and")
print("   +3 are only partially read and still carry 27% of the entropy between them.")
print()
print("## THE MINIMUM NEXT EVIDENCE REQUIRED")
print("   The single-face test is done and negative. What remains untested in EXP-024 is")
print("   the MULTI-FACE readings, which are most of its space. Those need a contiguous")
print("   arc of COMPLETE faces, and the CET face's neighbours are not complete:")
print("     UTC+0  upper COMPLETE (REYKJAVIK DUBLIN LONDON LISSABON ALGIER MADEIRA BISSAU)")
print("            lower PARTIAL - CASABLANCA CONAKRY DAKAR BAMAKO ACCRA, band ends unseen")
print("     UTC+2  upper PARTIAL - one line between SOFIA and NIKOSIA is UNKNOWN")
print("            lower PARTIAL - BEIRUT DAMASKUS KAIRO KHARTUM LUSAKA MAPUTO, ends unseen")
print("     UTC+3  both PARTIAL and oblique; the lower block's line order is not certain")
print()
print("   So the ask is ONE more target-era close frame of the drum from a DIFFERENT")
print("   BEARING - roughly 45-90 degrees around, so that UTC+0 and UTC+2 present")
print("   frontally instead of obliquely. Same-day frames are ideal because they remove")
print("   the stability question entirely.")
print()
print("   Exactly which images, given that I cannot tell which of the three candidates I")
print("   was just given:")
print("     1. picture-alliance 16008401 and 16008415 (04.11.1989) - whichever of the two")
print("        was NOT the frame already uploaded, at maximum resolution.")
print("     2. HanisauLand / bpb 153695.jpg (04.11.1989), which the handoff explicitly")
print("        declines to identify with either PA id - so it may be the third distinct")
print("        same-day frame.")
print("   Success criterion: the UTC+0 and/or UTC+2 face frontal, with BOTH bands legible")
print("   line by line and both band ends visible.")
print()
print("   Also worth resolving, cheaply: the accession of the frame I have. Three")
print("   candidate ids, and I cannot tell them apart, so a later worker cannot re-pull")
print("   'the' image. That is a provenance gap, not a blocker.")
print()
print("   ATHEN is still not visible on the UTC+2 face in NOVEMBER 1989. That is a")
print("   third strike against the Athens-added-1985 reading and is worth noting")
print("   whenever the 1985 maintenance is cited again.")
