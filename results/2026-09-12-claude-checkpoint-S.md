# Checkpoint S — Sanborn/Scheidt documentary synthesis

**K4 remains unsolved.** No experiment was run this session, and **no EXP-040 was created**.
That is the reported result, not a shortfall.

## Repository status

| | |
|---|---|
| branch | `claude/k4-post-j` |
| starting HEAD | `ed9452bec45431bb1e11f04eb341ce1c17eea838` |
| final HEAD | this checkpoint's commit |
| `main` / `codex/k4-continuation` / `claude/dreamy-archimedes-79k6u0` | untouched |

Full working: `docs/external/checkpoint-S-sanborn-scheidt-synthesis.md`.

## 1. Documentary statements newly relied upon, with grades

All from the Box 6 Folder 9 first-person Sanborn manuscript unless noted.

| # | statement | grade |
|---|---|---|
| 1 | The robotic / high-pressure-waterjet cutting route was **considered and rejected on cost** | **A** — first-person, specific |
| 2 | Letters were laid out manually: copper painted black, **straight horizontal row lines scribed**, **metal stencils** positioned on those lines, traced, drilled, jigsaw-cut, hand-filed | **A** — first-person, specific |
| 3 | Sanborn knew Vigenère-class systems and **sought Scheidt for contemporary expertise** able to challenge contemporary and future codebreakers | **A** for the recruitment rationale; **not** a mechanism |
| 4 | K1–K3 expected solved in weeks/months; **K4 intended to take much longer** | **A** for design intent |
| 5 | At the 1990 dedication Sanborn gave DCI Webster **some plaintext and a partial key** | **A** for custody; content not disclosed |
| 6 | The manuscript **intentionally contains embedded K4 clues** | **A** — and this is why it is locked, not mined |
| 7 | Sanborn **deliberately obscured** encoded text in photographs | **A** |
| 8 | (Jan 1990 *Washington Post*) the harder half uses "a **modern system created for the project** by an expert cryptographer" | **B** — contemporaneous press |
| 9 | (1991 *Museum & Arts Washington*) "three or four systems" progressing in complexity from Morse at the entrance | **B** — and see §4 |

**Contamination lock honoured.** Because the manuscript announces embedded clues, only explicit
factual statements were admitted. No acrostic, first/last-letter, numeric, capitalisation,
chapter-title, word-count, place-name or repeated-phrase mining was performed. An intentionally
clue-bearing text is not an answer oracle, and turning it into one would require a deliberate,
separately recorded protocol change.

## 2. Fabrication correction

The waterjet reading is **superseded prospectively** (history not rewritten). Manual stencil
placement on scribed horizontal baselines:

- **row order remains meaningful** — rows are the one physically established structure;
- **same-column vertical relations are weaker** than under the waterjet reading: a scribed
  baseline fixes the *line*, not the *pitch*;
- fixed pitch, a common x-grid, 31 physical columns, identical row starts and uniform spacing
  are **all unestablished**; exact x-coordinate hypotheses stay **parked**;
- apparent vertical alignment in photographs must not be used as a primary key source — and
  Sanborn says he deliberately obscured encoded text in photographs, so publicity images are
  not neutral documentation.

**Consequence for the standing evidence requests: Request 4 is substantially answered and is
demoted.** It existed to determine whether a common lattice exists; Sanborn's own account
indicates it very likely does not. A measured survey would now refine spacing, not unlock an
architecture.

## 3. Sanborn / Scheidt roles

Scheidt supplied education, candidate systems and modification ideas. Sanborn **selected**,
**modified** and **implemented**. Folder 9 adds first-person support: he already knew
Vigenère-class systems and recruited Scheidt precisely for what he lacked.

> **Searching for an unchanged textbook cipher is now materially less justified than searching
> for a Sanborn-modified construction. Grade: SUPPORTED INTERPRETATION** — four independent
> sources, plus first-person corroboration of the recruitment rationale. Not PROVED: no source
> says what was modified or how.

**This cuts against the strategy the repository has actually been executing.** EXP-001 … EXP-039
each tested a *named or parametrically declared* family. If the process was custom-built and
then modified, the prior probability that it coincides with any nameable family is low — a
coherent explanation for thirty-nine negatives, and a reason to expect **diminishing returns
from further catalogue search**, not a reason to pick the next catalogue entry.

## 4. "Four processes" — interpretation retained, with a new caution

Unchanged: one high-level process per section; K1/K2 related; K3 another; K4 the fourth and
disguised; **not** four layers stacked on K4. The manuscript never enumerates processes, so it
neither strengthens nor weakens this.

**New caution.** The 1991 "three or four systems" count **includes the Morse plates at the
building entrance**, which are not K1–K4. That enumeration and Scheidt's four processes are
therefore **not demonstrably the same list**, and the apparent agreement on "four" may be
coincidental. Corroboration for a *progressive multi-process design* is genuine; a one-to-one
mapping onto K1–K4 is not established. Recorded so it does not accumulate as false confirmation.

## 5. "Disguise / masking" — what it requires

Any consistent architecture must: (1) materially suppress ordinary plaintext statistics;
(2) be realistically implementable in the 1989–90 workflow; (3) be compatible with Sanborn
selecting and modifying rather than copying; (4) not require unexplained digital machinery;
(5) remain recoverable in principle.

**These are filters, not a specification.** A requirements list satisfied by a large space of
constructions does not select one.

### One genuinely new constraint the record does yield

Sanborn intended K4 to be solved — *later*, not never. Combined with EXP-019's unicity result
(97 characters can determine at most ~66–76 letters of key entropy), a cipher whose key entropy
exceeds the message's capacity is not "harder" but **permanently unsolvable**, contradicting
that intent.

> **Filter for all future proposals: key entropy must lie within the unicity bound.**
> Grade: INFERENCE (stated intent + an existing repository result). It selects no mechanism.

## 6. Surviving classes and prior coverage

| class | support | tested? | still open | finite test definable? |
|---|---|---|---|---|
| Transposition / modified | **Strong** | EXP-003/016/033/036/039 | widths ≥12, ≥3 passes, other keys | only with a precommitted key family — **evidence no longer supplies one** |
| Polyalphabetic masking | **Strong** | EXP-001/006/015/036 | aperiodic schedules | not without a named schedule |
| Running key, external source | Moderate | every nameable source: EXP-004/014/022/023/024/029–031/035 | **any unidentified source** | **No** — needs a named source |
| Stateful / self-evolving | Weak (structural) | order-2 affine closed, EXP-038 | higher order, nonlinear | yes, but that is the rescue pattern |
| Fractionation | Weak–moderate | named classics closed, EXP-012/013 + Checkpoint O | custom full-26 | only once written as equations |
| Homophonic / variable mapping | Weak | partially, EXP-009/011 | length-preserving variants | not without a named table |
| Nulls / length-changing | **Weakened** by the verified positional cribs | indirectly | must still honour the numbered anchors | only if the anchors are explained |
| Multi-stage compositions | Moderate | EXP-033/036/039 | outside declared families | **No** — unbounded without a key family |
| Physical-layout-dependent | **Weakened** by §2 | parked | nothing newly testable | No |

## 7. EXP-040 gate decision — NO EXPERIMENT

The closest candidate was worked rather than dismissed: **a key constant on each engraved row**,
`k[i] = f(row(i))` with `f` arbitrary — the model the new fabrication evidence points at most
directly, and one EXP-032 never covered (it tested `f(column)`).

Rejection power, computed **without evaluating any verdict**: the 24 cribs fall 13 / 3 / 8 across
rows 26 / 27 / 28, giving **21 equality constraints against 3 free values**, chance survival
`26⁻²¹` per convention. Decidable and trivially cheap — it passes gate conditions 2, 3, 4, 5, 6.

**It fails conditions 1 and 7.** A key taking **three distinct values across 97 positions** is
the weakest key structure available; it would leave K4's statistics essentially intact, flatly
contradicting the masking evidence and Sanborn's stated intent that K4 be substantially harder
than K1–K3. The same record that motivates row indexing rules out the only finite row-indexed
model. It would be selected purely because it is cheap and untested — exactly what the gate
forbids.

Nothing else reaches the gate: "custom / modified" *is* a statement that the parameter space is
unbounded, which fails conditions 2 and 3, since one cannot freeze the equations of "a
modification".

> **The combined Sanborn/Scheidt documentary record materially strengthens the
> custom/modified-process interpretation but does not currently identify a sufficiently
> specific, evidence-backed, finite K4 architecture for EXP-040.**

The gap is **not** filled with order-3 recursion, generic double transposition, arbitrary grid
routes, random 26-letter alphabets, arbitrary long keys, generic modern stream ciphers, or
another historical-cipher catalogue.

## 8. ONE next action

> **Pursue Request 2: the unedited 2005 Kim Zetter / Edward Scheidt interview material** — raw
> audio or full transcript, interviewer notes, questions cut from the published piece, drafts and
> fact-check correspondence.

**Why this rather than another experiment.** This synthesis locates the bottleneck precisely: the
blocker is no longer *testing* architectures but *identifying* one. Every architecture nameable
from public evidence has been tested and failed, and §3 explains why that pattern was to be
expected. The one filter this session produced (key entropy within the unicity bound) narrows
proposals but names none.

**Why Scheidt specifically.** He is the only living source who has publicly described the
fourth process, and the published article is **self-described as a partial transcript edited for
length and organisation** — so material almost certainly exists that was not printed. Nothing
else in the record has a comparable chance of naming a mechanism.

**Why not the alternatives.** Request 4 is demoted by §2 — Sanborn's own account has largely
answered the fabrication question, and a survey would refine spacing rather than unlock an
architecture. The Webster partial-key custody trail (Folder 9 p.20–21) is tempting but its
content is unknown, it may not survive, and *partial plaintext* would engage the contamination
protocol directly. Unlocking the manuscript's embedded clues would require deliberately
abandoning the contamination lock, which should not be done casually and is not recommended here.

**What would close it.** If the unedited material contains no further technical detail — only
the same high-level "four processes / masking" language — then the documentary route to naming
the process is exhausted, and the repository should record that plainly rather than manufacture
families to keep searching. That is a legitimate and informative outcome.
