# Checkpoint S — Sanborn / Scheidt documentary synthesis

Purpose: decide whether the combined documentary record — the newly audited first-person
Sanborn manuscript (Box 6 Folder 9), the Box 16 Folder 2 press scrapbook, and the existing
Scheidt material — now selects a specific, bounded, falsifiable K4 architecture strongly
enough to justify EXP-040.

**Answer: it does not.** The reasoning is below, including the one candidate that came closest
and exactly which gate condition it fails.

**Contamination lock.** Folder 9 page 2 states the manuscript was intended to carry embedded K4
clues. Under the current protocol only **explicit factual statements** are admitted. No
acrostic, first/last-letter, numeric, capitalisation, chapter-title, word-count, place-name or
repeated-phrase mining was performed, and none may be performed without a deliberate,
separately recorded change to the protocol. An intentionally clue-bearing text must not be used
as an answer oracle.

---

## A. What does "modern / contemporary" actually support?

| tier | statement |
|---|---|
| **Directly stated** | Sanborn knew historical systems such as the Vigenère tableau, and *sought* Scheidt because he wanted contemporary cryptographic expertise capable of challenging contemporary and future codebreakers. (Folder 9 p.12, first-person) |
| **Directly stated** | K1–K3 were expected to be solved in weeks or months; **K4 was intended to take much longer**. (Folder 9 p.23, first-person) |
| **Strongly implied** | The harder Kryptos process is **custom-built for this project**, not an off-the-shelf named cipher. (Jan 1990 *Washington Post*: "a modern system created for the project by an expert cryptographer"; 1991 *Museum & Arts Washington*: "developed by … a former CIA employee") |
| **Compatible** | Any construction that suppresses ordinary English statistics and is implementable in a 1989–90 workflow. |
| **Merely possible** | Every named modern primitive. |

**Not inferred, and explicitly refused:** stream cipher, LFSR, rotor machine, matrix cipher,
autokey, feedback, fractionation, homophony, one-time pad. "Contemporary expertise" names a
*person's qualifications*, not an algorithm. No second source supports any of these.

### A new upper bound that the record does supply

Sanborn's intent was that K4 be solved — *later*, not never. That is a design constraint, and it
combines with an existing repository result:

> EXP-019's unicity analysis: 97 characters can determine at most roughly **66–76 letters of key
> entropy**. A cipher whose key entropy exceeds the message's capacity is not "harder", it is
> **permanently unsolvable**.

So "modern" must be read as *stronger than a textbook classical cipher but still recoverable in
principle*. Any future proposal whose key entropy exceeds that bound contradicts Sanborn's
stated design intent.

**Grade: INFERENCE** — combining a first-person statement of intent with a prior repository
result. Not a documentary statement, and it selects no mechanism. It is a **filter on future
proposals**, which is the only new cryptanalytic content this synthesis produces.

---

## B. Re-audit of Scheidt's "four processes"

Prior reading, unchanged: one high-level process per section; K1/K2 related; K3 another; K4 the
fourth and disguised; **not** four sequential layers stacked on K4.

Nothing in Folder 9 strengthens or weakens it — the manuscript never enumerates processes.

**One caution the new material does add.** The 1991 profile describes "three or four systems of
encoding progressing in complexity from International Morse at the building entrance". That
enumeration **includes the Morse plates**, which are not K1–K4. So the journalistic count and
Scheidt's four processes are **not** demonstrably the same enumeration, and the apparent
agreement on the number four may be coincidental. Corroboration for a *progressive multi-process
design* is real; a one-to-one mapping onto K1–K4 is not established.

The interpretation is therefore **retained unchanged**, with that caveat recorded rather than
allowed to accumulate as false confirmation.

---

## C. What "disguise / masking" requires

From the Scheidt record: all four sections are English; frequency and counting gave access to
the first three; that access was *disguised* in the fourth; the masking technique "may not be
known".

Necessary properties of any architecture consistent with those statements:

1. **Materially suppresses ordinary plaintext statistical structure** — enough that
   frequency/counting attacks that worked on K1–K3 do not work here.
2. **Realistically implementable in the 1989–90 workflow**, by Sanborn or by Scheidt on
   Sanborn's behalf.
3. **Compatible with Sanborn selecting and modifying** the process rather than executing an
   unchanged textbook procedure.
4. **Does not require unexplained modern digital machinery** absent independent evidence.
5. **Recoverable in principle** — key entropy within the §A bound.

These are **filters, not a specification.** They are satisfied by a large space of
constructions, and a requirements list that many architectures satisfy does not select one.

---

## D. Sanborn / Scheidt division of labour

| role | who | source |
|---|---|---|
| cryptographic education; candidate historical and contemporary systems; modification ideas | **Scheidt** | 2005 Scheidt interview |
| thematic and narrative content | **both** | 2005 interviews |
| **selection** of which system to use | **Sanborn** | 2005 Sanborn interview; Folder 9 recruitment rationale |
| **modification** of the systems taught | **Sanborn** | 2005 Sanborn interview |
| final implementation and physical/visual encoding | **Sanborn** | Folder 9 fabrication account |

New first-person support from Folder 9: Sanborn already knew Vigenère-class systems and
recruited Scheidt specifically for what he lacked. He was therefore a *selector and modifier*
operating with expert input, not a copyist of a textbook procedure.

> **Conclusion: searching for an unchanged textbook cipher is now materially less justified than
> searching for a Sanborn-modified construction.**
>
> **Grade: SUPPORTED INTERPRETATION** — four independent sources (2005 Scheidt interview, 2005
> Sanborn interview, Jan 1990 *Washington Post* "created for the project", 1991 profile
> "developed by"), plus first-person corroboration of the recruitment rationale. Not PROVED: no
> source states what was modified or how.

**This is the most important result of the synthesis**, and it cuts against the strategy this
repository has actually been executing. EXP-001 … EXP-039 each tested a **named or
parametrically declared** family. If the process was custom-built and then modified, the prior
probability that it coincides with any nameable family is low — which is a coherent explanation
for thirty-nine negatives, and a reason to expect diminishing returns from further catalogue
search rather than to pick the next catalogue entry.

---

## E. Hand-implementability ranking

Not a proof; a ranking criterion.

| tier | mechanisms |
|---|---|
| **Practical by hand** | tableau lookups; periodic and running keys; columnar and route transposition; small-grid fractionation; keyed alphabets |
| **Practical with a calculator or simple 1989 computer** | modular arithmetic over Z26; short recurrences; small matrix operations; digit-driven schedules |
| **Requires substantial custom software** | large-state generators; many-round constructions; anything needing bulk trial computation to *encipher* |
| **Unknown** | what computing Scheidt's firm had available — no evidence either way |

The fabrication account describes an artist's studio hand-cutting copper, which says nothing
directly about how the *cipher* was produced: Scheidt could have produced key material
elsewhere. The ranking is a tiebreaker, not a filter, and it is not used here to exclude
anything.

---

## F. Coverage map — documentary-supported classes

| class | documentary support | substantially tested? | what remains open | finite exact test definable? |
|---|---|---|---|---|
| Transposition / modified transposition | **Strong** (K3 precedent; Sanborn implemented one) | Yes — EXP-003, 016, 033, 036, 039 | keyed widths ≥12; ≥3 passes; keys outside the evidenced words | **Only with a precommitted key family, which the evidence no longer supplies** |
| Polyalphabetic masking | **Strong** (K1/K2 precedent) | Yes — EXP-001, 006, 015, 036 | aperiodic/irregular schedules | Not without a named schedule |
| Running key / external-source masking | **Moderate** (fits "masking"; no named source) | Yes for every source the repository can name — EXP-004, 014, 022, 023, 024, 029–031, 035 | **any unidentified source** | **No** — needs evidence naming a source |
| Stateful / self-evolving keys | Weak (structural only) | Order-2 affine closed — EXP-038 | higher order; nonlinear; reset | Yes, but extending order is the rescue pattern |
| Fractionation | Weak–moderate ("masking" fits) | Named classics closed — EXP-012, 013, and the Checkpoint-O audit | custom full-26 constructions | Only once written as equations |
| Homophonic / variable mapping | Weak | Partially — EXP-009, 011 | length-preserving variants | Not without a named table |
| Nulls / length-changing | **Weakened** — the published positional cribs constrain it hard (Checkpoint P) | Indirectly | architectures that still honour the numbered anchors | Only if the anchors are explained |
| Multi-stage compositions | **Moderate** ("custom", "modified") | Pairwise compositions tested — EXP-033, 036, 039 | compositions outside declared families | **No** — the space is unbounded without a key family |
| Physical-layout-dependent | **Weakened by the new fabrication evidence** | Parked | nothing newly testable | No |

No class is revived here merely because its general category remains logically open.

---

## G. Physical geometry — prospective correction

Current best evidence, superseding the waterjet reading **prospectively** (history is not
rewritten):

> The copper was painted black, **straight horizontal row lines were scribed**, individual
> **metal character stencils** were positioned on those lines, traced, drilled, jigsaw-cut and
> hand-filed. The robotic/high-pressure-waterjet route was **considered and rejected on cost**.

Consequences:

- **Horizontal row order remains meaningful** — rows are the one physically established
  structure.
- **Same-column vertical relations are weaker** than under the waterjet reading. Manual stencil
  placement on a scribed baseline fixes the *line*, not the *pitch*.
- Fixed pitch, a common vertical x-grid, 31 physical columns, identical row starts and uniform
  spacing are **all unestablished**.
- Exact x-coordinate hypotheses stay **parked**.
- **Do not use apparent vertical alignment in photographs as a primary key source** — and note
  Folder 9 p.27 records that Sanborn deliberately obscured encoded text in photographs, so
  publicity images are not neutral documentation of the cipher surface.

**Request 4 is substantially answered and should be demoted.** It existed to determine whether a
common lattice exists; Sanborn's own account now indicates it very likely does not. A measured
survey would refine spacing, not unlock an architecture.

---

## H. The EXP-040 gate

The closest candidate, and why it still fails — worked rather than asserted:

**Candidate: a key constant on each engraved row**, `k[i] = f(row(i))` with `f` arbitrary. This
is the model the new fabrication evidence most directly points at, since rows are the one
established physical structure, and EXP-032 tested `f(column)` but never `f(row)`.

Rejection power, computed **without evaluating any verdict**: the 24 crib positions fall 13 in
row 26, 3 in row 27, 8 in row 28, giving **21 equality constraints against 3 free values** —
chance survival `26⁻²¹` per convention. Decidable, and trivially cheap.

| gate condition | verdict |
|---|---|
| 1. documentary support stronger than "not yet tested" | **FAILS** — see below |
| 2. exact definition freezable before the verdict | passes |
| 3. bounded or existentially decidable | passes |
| 4. cribs give meaningful rejection power | passes overwhelmingly (21 constraints) |
| 5. not substantially duplicating EXP-001…039 | passes (EXP-032 tested columns, not rows) |
| 6. expected accidental survivors calculable in advance | passes |
| 7. a zero eliminates a **meaningful family** | **FAILS** |
| 8. not selected because a previous experiment failed | borderline |

**Why 1 and 7 fail.** A key taking **three distinct values across 97 positions** is the weakest
key structure available. It would leave K4's plaintext statistics essentially intact — flatly
contradicting requirement C.1, the masking evidence, and Sanborn's stated intent that K4 be
substantially harder than K1–K3. The same documentary record that motivates *row indexing*
therefore rules out the only row-indexed model that is finite. It would be selected purely
because it is cheap and untested, which is exactly what the gate forbids.

**No other candidate reaches the gate.** "Custom / modified" is precisely a statement that the
parameter space is unbounded, which fails conditions 2 and 3: one cannot freeze the exact
equations of "a modification". The masking requirements in §C are filters satisfied by a large
space. The unidentified-source running key fails condition 3 for want of a source.

### Decision

> **The combined Sanborn/Scheidt documentary record materially strengthens the custom/modified-process
> interpretation but does not currently identify a sufficiently specific, evidence-backed, finite
> K4 architecture for EXP-040.**

**No EXP-040 is created.** The gap is not filled with order-3 recursion, generic double
transposition, arbitrary grid routes, random 26-letter alphabets, arbitrary long keys, generic
modern stream ciphers, or another historical-cipher catalogue. An honest documentary frontier is
preferred over speculative compute.
