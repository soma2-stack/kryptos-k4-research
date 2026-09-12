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
by_era = {"1988-89": 0, "1984": 0, "DISPUTED-DATE": 0, "MODERN": 0}
for fid in g.sector_faces():
    srcs = " ".join(g.faces[fid]["sources"])
    if "1989" in srcs or "1988" in srcs:
        by_era["1988-89"] += 1
    elif "1984" in srcs:
        by_era["1984"] += 1
    elif "Straube" in srcs:
        by_era["DISPUTED-DATE"] += 1
    else:
        by_era["MODERN"] += 1
print(f"   faces from 1988-89 evidence          : {by_era['1988-89']}")
print(f"   faces from 1984 evidence only        : {by_era['1984']}")
print(f"   faces from the DISPUTED-DATE frame   : {by_era['DISPUTED-DATE']}  <- includes CET")
print(f"   faces from MODERN evidence only      : {by_era['MODERN']} (rules only, never membership)")
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
UP = ["AMSTERDAM","BERLIN","BRUSSEL","BUDAPEST","MADRID","PARIS","PRAG","STOCKHOLM","WARSCHAU"]
LO = ["KOPENHAGEN","LONDON","WIEN","ROM","BELGRAD","TUNIS"]
u = sum(len(w) for w in UP); l = sum(len(w) for w in LO)
print("## Tier-1 status of the UTC+1 (Berlin / CET) face, in detail")
print(f"   UPPER band  : {len(UP)} names, ORDERED (alphabetical), {u} letters")
print( "                 LOCAL VISUAL EVIDENCE - my own reading of UPLOAD-1 reproduces the")
print( "                 external handoff's nine names and their order independently.")
print(f"   LOWER band  : {len(LO)} names, ORDERED, {l} letters   LOCAL VISUAL EVIDENCE")
print( "                 I read LONDON, which the external handoff missed, and resolved the")
print( "                 band the handoff called untranscribable. Order is NOT alphabetical:")
print( "                 north-to-south with one inversion (ROM before BELGRAD).")
print(f"   face total  : {u} + {l} = {u+l} letters")
print(f"   K4 length   : 97")
print()
print("   So the letter-count shortfall that dominated the last three checkpoints is")
print("   now ZERO on this face. That is a real advance in the reconstruction. It is")
print("   NOT a cryptanalytic result, and the 97 itself is not evidence:")
print("     - I did not predict 97 in advance.")
print("     - 24 faces x 3 natural quantities = ~72 values over a 4-137 range, so")
print("       about 0.54 exact hits at 97 are expected by chance. One hit is nothing.")
print("     - The count is fragile: without LONDON it is 91; an unseen seventh lower")
print("       line would push it past 97.")
print("   The only non-free element is WHICH face: the Berlin/CET face named by the")
print("   BERLINCLOCK crib, and the face already targeted before the count was taken.")
print("   GRADE: OBSERVATION, NOT EVIDENCE.")
print()
print("## Why Tier 1 is STILL not met: the face's date is unresolved")
print("   The completeness criterion has two parts, and only one is satisfied:")
print("     (a) complete contiguous physical tape of >= 97 letters   -> SATISFIED")
print("     (b) that tape attested for the 1988-89 target era        -> NOT SATISFIED")
print()
print("   The arithmetic gap that previously blocked (b) is CLOSED:")
print("     146 modern - 80 original (1969) - 20 added (1997) = 46, and the 1985 first")
print("     major maintenance (Tagesspiegel, 14 Apr 2019, Erich John profile) is the")
print("     third change boundary that quantity requires. With boundaries at 1969,")
print("     1985 and 1997, any frame datable to [1985, 1997) shows the target state.")
print("     Dating is therefore now a yes/no question, not an open growth curve.")
print()
print("   But UPLOAD-1 is internally contradictory on date:")
print("     for >= 1985 : KOPENHAGEN, WIEN, ROM present - all named 1985 additions")
print("     for < 1985  : WELT caption says mid-1970s; clothing/vehicles read 1970s;")
print("                   ATHEN, the fourth named 1985 addition, is NOT visible")
print("     for < 1997  : LENINGRAD and MOSKAU present (LOCAL VISUAL, caption-free)")
print("   Either the Tagesspiegel 1985 change set is wrong, or the WELT caption is.")
print("   The cheapest reconciliation is that 1985 RE-ENGRAVED names already on the")
print("   drum - which would vindicate the 1970s caption and, ironically, also argue")
print("   for stability. But that is a reconciliation, not evidence.")
print("   No further analysis of the pixels in hand can settle it.")
print()
print("   TIER 1 VERDICT: NOT MET. EXP-024 remains frozen and unrun, unmodified.")
print()
print("## Physical rules established this checkpoint (era-independent)")
print("   1. Half-hour zones are inscribed with a literal '+30' suffix: NEW DELHI +30,")
print("      COLOMBO +30, RANGUN +30, KABUL +30. LOCAL VISUAL, and independently")
print("      confirming the 2019 report of a '+ 30' inscription. Consequence: a tape")
print("      reading crossing those faces must choose whether to skip or transliterate")
print("      the digits - a free choice, hence a degree of freedom to be penalised.")
print("   2. Within a face, UPPER = northern places, LOWER = southern. LOCAL VISUAL on")
print("      four independent face pairs, and matching the account of the upper metal")
print("      ring as the northern-hemisphere structural ring. Consequence: band")
print("      assignment is PREDICTABLE from latitude, removing the 2^k half of the")
print("      per-face layout entropy. The k! within-band ordering remains.")
print("   3. Upper bands are alphabetical (9/9 on CET). Lower bands are NOT. So no")
print("      single ordering rule governs both bands, and any procedure assuming one is")
print("      wrong. The lower rule itself is UNRESOLVED from one face.")
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
print("## THE SINGLE HIGHEST-VALUE NEXT ITEM")
print("   The blocker is no longer transcription. It is DATING one image.")
print("   In priority order, any ONE of these unblocks Tier 1:")
print("   1. The akg-images / picture-alliance catalogue record for the Straube")
print("      photograph used by WELT (article 217168174, image 1920313707). The")
print("      agency's own caption metadata carries a shoot date or date range. This is")
print("      a single archive page lookup and it decides (b) outright.")
print("   2. ANY dated 1985-1996 photograph showing the CET/Berlin face legibly -")
print("      which would attest the target-era tape directly and make the Straube")
print("      frame's date irrelevant.")
print("   3. Primary documentation of the 1985 maintenance change set (a BVB/city")
print("      maintenance ledger, works order, or contemporary 1985 press report),")
print("      to establish whether 1985 ADDED or RE-ENGRAVED Athen/Kopenhagen/Wien/Rom.")
print()
print("   Item 1 is the cheapest by a wide margin and is web-only: this environment's")
print("   egress blocks all image and archive hosts (verified again this session:")
print("   i.pinimg.com -> connect_rejected). It must be retrieved externally.")
print("   I am NOT working around it by guessing the date.")
