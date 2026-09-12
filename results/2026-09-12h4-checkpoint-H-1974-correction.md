# Checkpoint H (session 11) — the 1974 frame, and two retractions

An external handoff (`docs/external/checkpoint-H-1974-evidence-correction.md`) supplies a
Straube photograph explicitly captioned **1974** in which the CET lower band already
carries **KOPENHAGEN** and **WIEN**. Incorporating it forces two retractions of my own
last-session conclusions, and it moves the Tier-1 position backwards rather than forwards.

## Retraction 1 — the date contradiction is gone, and not in my favour

Last session I recorded the CET frame's date as **DISPUTED** between a mid-1970s caption
and a [1985, 1997) reading, and treated that as a live chance of target-era attestation.
That disputation rested entirely on reading the Tagesspiegel sentence

> *Schon bei der ersten großen Wartung 1985 wurde aus gegebenem Anlass Athen nachgraviert,
> aber auch Kopenhagen, Wien und Rom.*

as a claim of **first** engraving. `Nachgraviert` also means *re-engraved / renewed*, and
the 1974 frame settles which reading is right for at least two of the four names. So
KOPENHAGEN/WIEN/ROM on my frame never forced ≥ 1985.

The frame therefore reads **consistently as mid-1970s** — and one observation flips sign:
**ATHEN's absence**, which I logged as evidence *against* the 1985 account, is now evidence
*for* the Athens-only part of it. Athens is on UTC+2, not CET, and nothing contradicts its
being a genuine 1985 addition; `aus gegebenem Anlass` fits an occasion peculiar to Athens.

**Net effect on Tier 1: worse.** The only reading that would have placed my one complete
face inside the target window is gone. The stability gap I have to close is now about
**fourteen years** (≈1974 → 1988–89), not about four.

One structural note, recorded as hypothesis only: setting Athen aside, the named places —
KOPENHAGEN, WIEN, ROM — are exactly three of the six names I read in the **CET lower band**.
If 1985 was a re-engraving of worn lettering, that is where it happened, and re-engraving
preserves text. That would be a weak argument *for* that band's stability across 1985. It is
three of six names on one face out of twenty-four, noticed after the fact, so it is not
offered as evidence.

## Retraction 2 — the 46-name gap is not "closed"

Last session I wrote that `146 − 80 − 20 = 46` is "exactly the quantity the 1985 event has
to account for", and concluded that with boundaries at 1969/1985/1997 any frame in
[1985, 1997) shows the target state, making dating "a yes/no question".

That was my inference, not the source's claim. The arithmetic identifies an **unexplained
remainder**; it says nothing about *when* those names entered, and they may well have
entered at several different times. The 1974 evidence now positively argues for multiple
entry times, since two of the four places named for 1985 were already present eleven years
earlier.

**Corrected statement:** 146 modern places; ~80 at installation in 1969; ~20 at the 1997
restoration; therefore **~46 entered at one or more unknown times in between. The growth
curve is open.** A frame's date does not by itself certify the target state.

## What the 1974 frame does buy

Independent corroboration of **KOPENHAGEN** and **WIEN** in the CET lower band from a
second, exactly-dated photograph. The graph records it as corroboration rather than as new
data: it contributes no ordering and no membership beyond two names already read.

**The CET transcription is unchanged** and remains valid LOCAL VISUAL evidence:

```
UPPER  AMSTERDAM BERLIN BRUSSEL BUDAPEST MADRID PARIS PRAG STOCKHOLM WARSCHAU   62
LOWER  KOPENHAGEN LONDON WIEN ROM BELGRAD TUNIS                                  35
                                                                          TOTAL  97
```

What changed is the **era** it attests, and that is what blocks Tier 1.

## Data-model fixes this forced

Adding the 1974 frame initially *destroyed* the complete CET face in the graph: a second
photograph of the same sector merged in and its partial lower-band reading re-marked the
band incomplete. Two rules now prevent that, and both are substantive rather than cosmetic:

1. **Faces are keyed by (sector, era).** Completeness and membership are per-era
   properties; a frame from another decade must never dilute or complete a face
   transcribed in a different one. Circumference is counted over **distinct sectors** so
   the same sector seen twice is not double-counted.
2. **A complete reading is authoritative; a partial reading never degrades it.** Within an
   era, a partial whose names are a subset of a complete reading is recorded as
   *corroboration*; a partial naming something the complete list lacks is recorded as a
   *conflict* rather than silently resolved. Complete readings replace partial residue, so
   transcribed order is preserved exactly as read (this was verified by assertion — the
   first implementation reordered the lower band).

## Metric (EXP-027, regenerated)

| quantity | value |
|---|---|
| sectors identified | **15 / 24 (62.5%)** |
| face-era records (sector × era) | 20 |
| upper bands complete / lower bands complete | 3 / 1 |
| faces COMPLETE | **1** — CET @1970s, local visual |
| adjacency edges OBSERVED / TRANSITIVE | 14 / 24 |
| longest contiguous chain | **7 faces** (UTC−2W … UTC+4, 1970s) |
| faces from 1988–89 evidence | 2 |
| faces from 1970s evidence | 7 (includes CET) |
| faces usable for 1989 via stability | **0** |

## TIER 1: NOT MET, and EXP-024 stays frozen

- (a) complete contiguous ≥ 97-letter tape — **satisfied** (CET, 97 letters).
- (b) that tape attested for 1988–89 — **not satisfied**, and now further from satisfied
  than it appeared last session.

**EXP-024 is unmodified, unrun and frozen.** The 97-letter coincidence is explicitly not
accepted as justification for running it; it remains OBSERVATION, NOT EVIDENCE, and it is
now a count on a frame ~14 years before the target period, which weakens any inference
from it.

Stability may not be assumed from the absence of known change. **NOWOSIBIRSK moved faces**
between 1984 and the modern drum, so per-face membership is not monotonic, and the 1985
maintenance demonstrably touched CET-lower lettering.

## The blocker is an image, not text metadata

Last session I asked for the akg-images catalogue record for the Straube frame. **That
request is withdrawn as no longer decisive:** it would now only confirm a mid-1970s date I
already accept, which does not reach 1988–89.

What is needed is one archive-dated photograph, inside or bracketing the target window, in
which the CET/UTC+1 face is identifiable by contents (BERLIN, PARIS, MADRID, WARSCHAU …)
and **both bands are legible line by line**. Ranked from the dated Picture Alliance
webseries `weltzeituhr-in-berlin-w194131`:

| rank | IDs | date | what it settles |
|---|---|---|---|
| **1 — decisive** | **16008401**, **16008415** | **04.11.1989** | The only listed frames inside the target window; five days before the Wall opened, squarely in the K4 composition period. Either confirms my 97-letter transcription for 1989 or refutes it. |
| 2 — circumstantial | 7728036 | 05.08.1991 | Post-target, pre-1997; brackets the window with the 1974 frame. Interpolation needs monotonic growth, which NOWOSIBIRSK refutes — would not on its own unfreeze EXP-024. |
| 3 — narrows only | 15638904 | 01.01.1982 | Whether the CET face changed 1974 → 1982, i.e. whether it changes at all. |
| 4 — low value | 102505875, 102505844, 102506000 | 22.05.1973 | A second early-1970s point on a state already in hand. |

**The exact request: picture-alliance image `16008401` and image `16008415` (04.11.1989),
at the highest resolution available.** Both, because which of the two faces CET cannot be
known in advance. If both were shot from the Asian side or the CET face is too oblique,
they do not settle it and rank 2 applies.

I am stopping at that request rather than inferring the 1988–89 CET face from the 1970s
one. K4 remains unsolved, and no complete deterministic mechanism is claimed.
