# Checkpoint H (session 12) — Tier 1 met, the 97 retracted, and an honest negative

Three 4 Nov 1989 images were uploaded. One of them is the first photograph this programme
has ever had in which a complete face of the drum is legible. It settles Tier 1, and it
refutes my own session-10 transcription.

## The images

| upload | what it is | use |
|---|---|---|
| UPLOAD-5 | B/W elevated frame of the 4 Nov 1989 demonstration, ~600px, clock left of centre | same frame as UPLOAD-6, downscaled; panel text not readable |
| **UPLOAD-6** | **the same frame at ~2000px; the drum is large and the city panels are readable line by line** | **the evidence** |
| UPLOAD-7 | vertical frame with the Interhotel tower, clock small and distant | event/context only, no panel text |

**Dating does not rest on caption metadata.** The frame carries hand-painted banners reading
`NEUES FORUM`, `SDP`, and `Kreml…Moskau / Reformen allein Werk so Politbüro und ZK … och so?`.
That is the autumn-1989 East German demonstration wave, and the 4 November Alexanderplatz
rally is the one event of this scale. The date is corroborated from image content.

One provenance gap: the handoff names three candidate same-day frames (`16008401`,
`16008415`, HanisauLand `153695`) and explicitly declines to assert they are the same image.
**I cannot tell which of the three I was given.** That does not affect the date; it does mean
the accession is unresolved and a later worker cannot re-pull "the" image by ID.

## My reading of the CET / UTC+1 face, 4 Nov 1989

```
UPPER  AMSTERDAM BERLIN BRUSSEL BUDAPEST MADRID PARIS PRAG STOCKHOLM WARSCHAU      62
       9 names, alphabetical                                          confidence HIGH
LOWER  KOPENHAGEN WIEN BERN BELGRAD ROM TUNIS BRAZZAVILLE KINSHASA LUANDA          58
       9 names, strictly latitude-descending                   confidence MEDIUM-HIGH
                                                                        TOTAL     120
```

The upper band is an **exact 9/9 match** — names *and* order — to my independent reading of
the 1970s frame. The lower band I grade MEDIUM-HIGH rather than HIGH because I misread this
very band once already; it is not lower because the nine names come out in **strictly
descending latitude** (55.7, 48.2, 46.9, 44.8, 41.9, 36.8, −4.3, −4.4, −8.8), which a
misreading does not produce.

## RETRACTION — the 97 was my own transcription error

Session 10 reported this face as 62 + 35 = **97 letters, exactly K4's length**. That is
wrong, and the higher-resolution target-era frame shows exactly how:

- **LONDON is in the UPPER band of the neighbouring UTC+0 face** (REYKJAVIK DUBLIN LONDON
  LISSABON ALGIER MADEIRA BISSAU). I imported it across a sector boundary from a
  foreshortened, partly occluded view — precisely the error that view invites.
- **BERN** was missed entirely.
- **BRAZZAVILLE, KINSHASA, LUANDA** were missed — all genuinely UTC+1.
- The "one inversion (ROM before BELGRAD)" was an artefact of the misreading. The real band
  is strictly latitude-ordered, a check my new reading passes and the old one failed.

**The real face carries 120 letters. The 97 is withdrawn entirely.**

It was graded OBSERVATION, NOT EVIDENCE and explicitly refused as grounds to run EXP-024.
That refusal is the only reason this is a corrected error rather than a wasted programme —
had I unfrozen the test on a number that came from my own misreading, everything after it
would have been noise.

## Two further retractions the 1989 frame forces

1. **"Upper = northern, lower = southern" is not the drum's organising principle.**
   KOPENHAGEN (55.7 °N) is in the CET *lower* band while MADRID (40.4 °N) is *upper*, and the
   lower band mixes northern European with sub-Saharan African places. The rule holds on the
   Asian faces I observed but does not generalise. **The 2^k layout-entropy reduction claimed
   in session 10 is withdrawn.** Downgraded CONFIRMED → LOCAL REGULARITY.
2. **Order does not follow from membership.** CET upper is alphabetical; UTC+0 upper is
   strictly latitude-descending (64.1 → 11.9) and *not* alphabetical; CET lower is
   latitude-descending; UTC+0 lower (CASABLANCA CONAKRY DAKAR BAMAKO ACCRA) is neither. The
   hope that a single ordering rule would let order follow from a place list — the thing that
   made reconstruction look tractable — is **withdrawn**. Each face's order must be read off
   a photograph.

Also: **ATHEN is still absent from the UTC+2 face in November 1989** — a third strike against
reading the 1985 maintenance as an Athens addition.

**LENINGRAD is now attested in the target era itself** (with MURMANSK and KIEW on the same
face), so the Soviet-era-toponym point no longer rests on 1984 and a 1970s frame.

## Stability, 1970s → 1989

No contradiction on anything still trustworthy: upper band 9/9 exact. Five of the nine 1989
lower names are legible in the 1970s frame; BERN, BRAZZAVILLE, KINSHASA and LUANDA are
unresolved there — neither confirmed nor excluded. SUPPORTED, and now **secondary**: direct
target-era attestation supersedes any stability argument.

## TIER 1: MET

- (a) complete contiguous tape ≥ 97 letters — **satisfied** (120).
- (b) attested for the 1988–89 target era — **satisfied** (4 Nov 1989, content-corroborated).

Procedure followed in the order required: the reconstruction was **frozen** in
`data/weltzeituhr_photos.json → tier1_frozen_reconstruction` *before* any test ran, with its
confidence grades and a stated risk; **EXP-024 was left unmodified and not re-run**; then and
only then the restricted run permitted by the Tier-1 rule was executed as **EXP-029**.
EXP-028 pins the frozen tape against the graph — 21/21 invariants hold.

## EXP-029 — the restricted preregistered test

EXP-029 imports EXP-024's components unchanged: the same `procedures()`, both key alphabets
(STD, KRY), both directions, **every** offset, all twelve shift conventions, and the same
preregistered criterion — all 24 known crib letters reproduced simultaneously.

**What "restricted" costs, stated plainly.** With one face the 22 procedures collapse: the
two utc-order readings need a multi-sector clock, direction and start sector are meaningless
for a single sector, whole-band-first equals band-order, and the alternating readings
degenerate to one band. **20 applicable procedures → 4 distinct tapes → 2 usable** (the
62- and 58-letter single-band tapes cannot carry a 97-window). This is a small fraction of
EXP-024's space and is not EXP-024.

**Positive control on the real tape** (not a synthetic one): a keystream planted at offset
41, STD, direction +1, `vigenere/P=STD/C=STD` was recovered exactly once. The scan detects a
genuine Weltzeituhr-derived keystream when one is present.

**Result — NEGATIVE.**

| | |
|---|---|
| tapes tested | 2 (both 120 letters) |
| alignments scanned | **11,520** |
| exact 24/24 matches | **0** |
| best achieved | 7/24 |
| mean | 0.910/24 (chance 0.923) |

Distribution: 0/24 × 4,668 · 1/24 × 4,186 · 2/24 × 1,870 · 3/24 × 646 · 4/24 × 134 ·
5/24 × 14 · 7/24 × 2.

Is the best alignment notable? Tested rather than asserted: ≥6/24 observed 2 vs 2.76
expected; ≥7/24 observed 2 vs 0.28 expected, Poisson p ≈ 0.032. A ~2σ blip on a maximum I
picked out after looking, across twelve conventions that are not independent — and nowhere
near the 24/24 criterion. Both are `STD dir+1 variant_beaufort/P=KRY/C=KRY`, offsets 78 and
16. **Recorded, not pursued.** Chasing it is exactly how this programme would fool itself.

Expected spurious exact hits over 11,520 alignments: ~1.3 × 10⁻³⁰. A single 24/24 would have
been meaningful. There are none.

## What this eliminates, and what it does not

**Eliminated — exhaustively, within the stated model:** the single-face running-key reading of
the Berlin/CET face, for these two tapes across the full alignment space above.

**Not eliminated:**

- readings spanning **several faces** — most of EXP-024's space, and blocked because the
  neighbouring faces' bands are only partially read;
- any **non-running-key** use of the object (indicator, coordinate, digit source);
- readings under a **different transcription** of the lower band, since mine is MEDIUM-HIGH;
- **the Weltzeituhr hypothesis itself.** This is one honest negative, not a verdict on the
  object.

No external verifier was consulted, and none will be on the basis of a 7/24 blip.

## Next evidence required

The neighbours are incomplete, which is what blocks the multi-face readings:

| face | state |
|---|---|
| UTC+0 | upper COMPLETE (7 names); lower PARTIAL — CASABLANCA CONAKRY DAKAR BAMAKO ACCRA, band ends unseen |
| UTC+2 | upper PARTIAL — one line between SOFIA and NIKOSIA is **UNKNOWN**; lower PARTIAL, ends unseen |
| UTC+3 | both PARTIAL and oblique; lower line order uncertain |

**The ask: one more target-era close frame from a different bearing** — roughly 45–90° around
the drum, so UTC+0 and UTC+2 present frontally rather than obliquely. Same-day frames are
ideal because they remove the stability question entirely.

1. **picture-alliance `16008401` and `16008415` (04.11.1989)** — whichever of the two was *not*
   the frame already uploaded, at maximum resolution.
2. **HanisauLand / bpb `153695.jpg` (04.11.1989)** — which the handoff declines to identify with
   either PA id, so it may be the third distinct same-day frame.

Success criterion: the UTC+0 and/or UTC+2 face frontal, both bands legible line by line, both
band ends visible.

K4 remains unsolved. No deterministic mechanism is claimed, and the one mechanism this
checkpoint could finally test came back negative.
