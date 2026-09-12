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
print("## Why Tier 1 is STILL not met: the face is dated OUTSIDE the target window")
print("   The completeness criterion has two parts, and only one is satisfied:")
print("     (a) complete contiguous physical tape of >= 97 letters   -> SATISFIED")
print("     (b) that tape attested for the 1988-89 target era        -> NOT SATISFIED")
print()
print("   CORRECTION TO LAST SESSION. I reported the date of this face as DISPUTED")
print("   between mid-1970s and [1985,1997), and reported the name-count arithmetic as")
print("   CLOSED. Both statements are now withdrawn:")
print()
print("   1. The date contradiction is GONE, and not in my favour. It rested entirely")
print("      on reading the Tagesspiegel 'nachgraviert 1985' sentence as a claim of")
print("      FIRST addition. A separately published Straube frame explicitly captioned")
print("      1974 already shows KOPENHAGEN and WIEN in the CET lower band. So their")
print("      presence here never forced >= 1985. The frame reads consistently as")
print("      mid-1970s - and ATHEN's absence, which I logged as evidence AGAINST the")
print("      1985 account, is now evidence FOR the Athens-only part of it. Same")
print("      observation, opposite sign.")
print("      Consequence: the only reading that would have put my complete face inside")
print("      the target window is gone. The stability gap is ~14 years, not ~4.")
print()
print("   2. The 46-name gap is NOT closed. 146 - 80 - ~20 = ~46 identifies an")
print("      unexplained REMAINDER; it says nothing about when those names entered.")
print("      Attributing them all to 1985 was my inference, not the source's claim -")
print("      the source names four places, and at least two were already present in")
print("      1974. The growth curve is OPEN and dating is NOT a yes/no question over a")
print("      single interval. A frame's date alone does not certify the target state.")
print()
print("   What the 1974 frame DOES buy: independent corroboration of KOPENHAGEN and")
print("   WIEN in the CET lower band from a second, exactly-dated photograph. Recorded")
print("   as corroboration in the graph; it adds no ordering or membership data.")
print()
print("   The CET transcription itself is UNCHANGED and remains valid LOCAL VISUAL")
print("   evidence. What changed is the era it attests, and that is what blocks Tier 1.")
print()
print("   Stability cannot be assumed from the absence of known change: NOWOSIBIRSK")
print("   moved faces, so per-face membership is not monotonic, and a re-engraving")
print("   maintenance in 1985 demonstrably touched CET-lower lettering.")
print()
print("   TIER 1 VERDICT: NOT MET. EXP-024 remains frozen, unrun and unmodified.")
print("   The 97-letter coincidence is explicitly NOT accepted as justification.")
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
print("## THE MINIMUM NEXT EVIDENCE REQUIRED")
print("   The blocker is an IMAGE, not text metadata. Text can no longer settle it:")
print("   the akg catalogue record I asked for last session would now only confirm a")
print("   mid-1970s date I already accept, which does not reach 1988-89.")
print()
print("   What is needed: ONE archive-dated photograph, inside or bracketing the target")
print("   window, in which the CET/UTC+1 face is identifiable by contents (BERLIN,")
print("   PARIS, MADRID, WARSCHAU ...) and BOTH bands are legible line by line.")
print()
print("   Ranked from the dated Picture Alliance webseries (weltzeituhr-in-berlin-w194131):")
print()
print("   RANK 1 - DECISIVE.  IDs 16008401 and 16008415, dated 04.11.1989.")
print("     The only listed frames inside the target window; 4 Nov 1989 is five days")
print("     before the Wall opened and squarely in the K4 composition period. If either")
print("     shows the CET face with both bands legible, Tier 1 is settled outright -")
print("     either confirming my 97-letter transcription for 1989 or refuting it.")
print("     Both IDs are wanted, at maximum available resolution: which one faces CET")
print("     cannot be known in advance.")
print("     Failure mode: if both were shot from the Asian side, or the CET face is too")
print("     oblique to read, they do not settle it and RANK 2 applies.")
print()
print("   RANK 2 - CIRCUMSTANTIAL.  ID 7728036, dated 05.08.1991.")
print("     Post-target and pre-1997. With the 1974 frame it BRACKETS the target window.")
print("     But interpolation between two matching frames is valid only under MONOTONIC")
print("     growth, and NOWOSIBIRSK refutes monotonicity. Strong circumstantial")
print("     evidence, NOT attestation - it would not on its own unfreeze EXP-024.")
print()
print("   RANK 3 - NARROWS ONLY.  ID 15638904, dated 01.01.1982.")
print("     Would show whether the CET face changed between 1974 and 1982, i.e. whether")
print("     this face changes at all. Useful, not sufficient.")
print()
print("   RANK 4 - LOW VALUE.  IDs 102505875 / 102505844 / 102506000, dated 22.05.1973.")
print("     A second early-1970s point corroborating a state already in hand.")
print()
print("   REQUEST, stated exactly: picture-alliance image 16008401 and image 16008415")
print("   (04.11.1989), highest resolution available. That is the minimum, and I am")
print("   stopping here rather than inferring the 1988-89 CET face from the 1970s one.")
