# K4 decidability census — what the 24 verified crib letters can and cannot falsify

**Branch:** `claude/k4-post-j`. **Starting HEAD:** `9ca31c47c0c35645bec2dbc531f3440b86dcd428`.
**Companion result:** `results/2026-09-13-checkpoint-AE.md`.
**Diagnostics:** `audit/census_AE.py` regenerates every figure below and asserts 15 of them.

This is not a cipher hunt and names no new family. It answers one question: **which broad
Layer-A architecture classes can the present evidence actually falsify?** It exists as the
structural safeguard against another post-hoc family selection.

No experiment was run. No EXP number assigned. Only the two public cribs were used; no alleged,
leaked or reconstructed K4 plaintext was searched for, fetched, quoted or inferred.

---

## 0. Organizing principle

From Checkpoint AC:

> **Parameter sharing, not merely bounding a stage, is what creates constraints.**

A stage generates constraints only when one finite parameter set is *reused* across many
positions, so that the crib letters collide on it. Bounding a stage without sharing buys
nothing — the identity-outer demonstration in class I proves this outright.

Everything below is an application of that principle plus the actual crib geometry.

### The falsifiability budget (Checkpoint AA, made exact here)

A class is testable only if

`(free parameters exercised at the 24 crib positions) < 24`.

"Exercised" is the operative word: a parameter that no crib position touches costs nothing and
buys nothing.

---

## 1. The crib geometry, which decides almost everything

The 24 letters are **not** 24 independent random points. They are two contiguous runs:

```
head 0-20   [21 ................ 33]   gap 34-62   [63 ...... 73]   tail 74-96
             EASTNORTHEAST                          BERLINCLOCK
             13 letters                             11 letters
```

| feature | value |
| --- | --- |
| distinct plaintext letters | 13 — repeats `A`×2 `C`×2 `E`×3 `L`×2 `N`×2 `O`×2 `R`×2 `S`×2 `T`×3 |
| distinct ciphertext letters at crib positions | 14 — repeats `F K N Q R S T V`×2, `P`×3 |
| maximum within-run distance | **12** |
| cross-crib distances | **30 to 52** |
| repeated plaintext digraphs | **none**, at either alignment |
| repeated plaintext 4- and 5-grams | **none**, at any alignment |
| repeated plaintext trigrams | exactly two: `EAS` at 21/30, `AST` at 22/31, both at distance **9** |
| physical row boundaries crossed | one — `BERLINCLOCK` splits `BER | LINCLOCK` at index 66 |

Two consequences dominate the census.

**The period blind spot.** A shared periodic schedule receives constraints only where a period
divides some distance between crib positions. Within-run distances never exceed 12 and
cross-crib distances lie in [30, 52], so:

```
p:  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
c: 22 21 20 19 18 17 16 15 14 13 12 11 11  9  8  7  7  9 11 11  9  7
p: 24 25 26 | 27 28 29 | 30 31 32 33 34 35 36 37 38 39 40
c:  5  3  1 |  0  0  0 |  1  2  3  4  5  6  7  8  9 10 11
```

**Periods 27, 28 and 29 receive exactly zero constraints, and 24–26 receive 5, 3 and 1.**

**The block-repeat drought.** Every polygraphic lever requires two identical plaintext blocks.
There are none at block size 2, 4 or 5, at any alignment. Size 3 has exactly one per alignment.
This single fact is why most inner-stage classes below are vacuous rather than merely hard.

---

## 2. Reduction rules — reject duplicate "new" families before coding them

Apply these before counting anything. Each is established elsewhere in the repository.

| # | Rule | Consequence |
| --- | --- | --- |
| R1 | `S2 ∘ S1` = one fixed substitution | any number of fixed monographic stages is one stage |
| R2 | fixed substitution commutes with transposition | `S → T` and `T → S` are the same architecture |
| R3 | `T3 ∘ T2 ∘ T1` = one permutation | "double/triple transposition" is not a new algebraic type |
| R4 | same-index additive masks compose | effective period divides `lcm`; the K1/K2 pair 8 and 10 gives 40, inside EXP-001's ≤48 sweep |
| R5 | Quagmire I–III ≡ existing STD/KRY shift families; Gronsfeld ⊂ periodic Vigenère | not new combiners |
| R6 | **Erasure** (AA-Theorem 1): free outer mask over a free inner block map fits every ciphertext | no inner stage is testable behind a free mask |
| R7 | **Identity-outer** (AC-Result 1): even a *fixed* outer map leaves a free block map untestable when observed blocks and their images are all distinct | bounding the outer stage is necessary, not sufficient |
| R8 | **T-determinacy** (AC-Result 2): under a fixed injective readout, inverting a coordinate fractionation makes the whole plaintext coordinate array a function of the readout | unknown plaintext adds no freedom in that class |
| R9 | An unbounded state machine is a free lookup | arbitrary `R` in a recurrence is vacuous by R6 |

---

## 3. The census

### A. Fixed monographic map — `C[i] = S(P[i])`, optionally composed with one declared permutation

Shared parameters: ≤26 table entries, of which 13 are exercised. Crib constraints: repeated
plaintext letters force equal images; repeated ciphertext letters force equal preimages. Both
fail immediately — 8 of 9 repeated plaintext letters take different ciphertext letters.

**Status: ALREADY CLOSED** (direct form by crib contradiction; composed with the declared
transposition families by EXP-033 at 175,820,784 cases; with the nine precommitted
double-columnar permutations by EXP-039). Pure transposition alone is separately **PROVED
IMPOSSIBLE** by Checkpoint T's letter-multiset argument. Do not rerun.

### B. Periodic schedule — `C[i] = F(P[i], k[i mod p])`

> **Scope clarification added 2026-09-13 at Checkpoint AF (prospective; nothing below is
> rewritten).** The notation `F(P[i], k[i mod p])` is generic, but the **ALREADY CLOSED** verdict
> for `p ≤ 23` is **not** a theorem about every arbitrary periodic combiner. It applies to the
> **declared shift/combiner families actually tested** — the 12 committed conventions (Vigenère,
> Beaufort, variant Beaufort × plaintext alphabet ∈ {STD, KRY} × ciphertext alphabet ∈ {STD, KRY}),
> as swept by EXP-001 directly and by EXP-036 composed with the declared transposition families,
> plus the combiner-coverage reductions (Quagmire I–III, Gronsfeld) and EXP-037 for standard Porta.
>
> An **arbitrary fixed 26×26 table** used as `F` is a different object and is censused separately
> as **class L**, where it is *vacuous* under the present cribs at key periods 8, 10, 13 and 26 —
> it receives **zero** constraints there, because no `(plaintext, key)` input pair repeats.
>
> So: a short period does **not** by itself close an arbitrary combiner. Read the `p ≤ 23` row as
> "the evidenced shift families are exhausted at those periods", never as "no periodic combiner of
> period ≤ 23 can exist". Class L governs the arbitrary-table case, and it is blocked by lack of
> constraint rather than by prior search.

Shared: `p` key values. Exercised: the occupied residue classes. Constraints: the table in §1.

This class must be split honestly:

- **p = 2…23:** 7 to 22 constraints. **ALREADY CLOSED** — EXP-001 direct through period 48,
  EXP-036 composed with the declared transposition families (4.3×10⁹ cases).
- **p = 24, 25, 26:** 5, 3, 1 constraints. **PARTIALLY DECIDABLE** and degrading fast.
- **p = 27, 28, 29:** **zero** constraints. **UNDECIDABLE WITH PRESENT CRIB GEOMETRY.**

The last group are **not survivors.** No result at those periods could distinguish a true model
from a false one; any "fit" there is vacuous. This is an information ceiling, not a gap in
effort, and EXP-036 was right to cap at 23.

### C. Position-function keystreams — `k[i] = f(i)`

Split by whether `f` is shared:

- **Bounded shared parameterisation** (affine `a·i+b`, row-local indexing, row resets,
  boustrophedon, row-number offsets): **ALREADY CLOSED** — EXP-001 for all 676 affine pairs,
  EXP-006/015/020 for resets, Checkpoint T for eleven row-structured models × 12 conventions ×
  periods 2–40.
- **Arbitrary `f(i)`:** one free parameter per observed position — 24 free against 24
  constraints. **VACUOUS WITH 24 CRIBS**, by R6.

### D. Source-symbol lookup — `k[i] = f(S[g(i)])` with one shared table

Constraints arise **only from repeated source symbols**: two crib positions reading the same
source symbol force equal key values. The count is therefore `24 − (distinct source symbols at
crib positions)`.

With K4's own ciphertext as source under identity `g`: 14 distinct symbols, so **10** equality
constraints. A source presenting 24 *distinct* symbols at the crib positions yields **zero** and
is vacuous — which is precisely why external tape sources with long non-repeating stretches were
uninformative.

**Status: ALREADY CLOSED at the declared scopes** — EXP-030 (tape lookup), EXP-032 (arbitrary
function of engraving column), EXP-034 (arbitrary function of one lagged source symbol),
EXP-035 (panel running key, 43,824 cases). **VACUOUS** for any newly proposed source whose crib
positions do not repeat. Checkpoint U additionally demoted every nameable artistic source to
Layer B, so this class is also **UNSUPPORTED** documentarily.

### E. Stateful recursive key schedules — `state[i+1] = R(state[i])`, `k[i] = h(state[i])`

Census of the generic class, not an extension of it:

| sub-case | shared DOF | verdict |
| --- | --- | --- |
| bounded `R` with small seed and parameter entropy | seed + parameters, both shared | **DECIDABLE** — and the specific full-Z26 second-order affine family is **ALREADY CLOSED** by EXP-038 (210,912 exact solves, independently exhaustive) |
| order-1 map `k[i+1] = f(k[i])` over Z26 | 26 table entries | **ALREADY CLOSED** — Checkpoint T found no consistent order-1 map under any of the 12 conventions |
| arbitrary `R` | unbounded | **VACUOUS** by R9 — an unbounded state machine is a free lookup |

The frontier is marked, not moved. No order-3 recursion is proposed: it adds seed and parameter
entropy without adding constraints, and Checkpoint T already showed the cribs are actively
hostile to low-memory autonomous state.

### F. Fixed transposition + fixed substitution

By R2 the order is immaterial and by R3 any chain collapses to one permutation.

- **Declared single-transposition families:** **ALREADY CLOSED** (EXP-033).
- **Precommitted keyword-pair double transposition:** **ALREADY CLOSED** (EXP-039, nine ordered
  pairs from `{KRYPTOS, PALIMPSEST, ABSCISSA}`).
- **Arbitrary unknown permutation:** a permutation consumes essentially all positional
  information — the crib letters no longer sit at known ciphertext positions — so the model is
  **VACUOUS WITH 24 CRIBS** unless `π` comes from a precommitted finite family.

No new transposition search is warranted.

### G. Periodic mask composed with transposition

Same constraint table as B, since a declared `π` preserves the count. **ALREADY CLOSED** for
periods 2–23 (EXP-036). Degrades to **PARTIALLY DECIDABLE** at 24–26 and
**UNDECIDABLE WITH PRESENT CRIB GEOMETRY** at 27–29, exactly as in B.

### H. Two masks separated by a permutation — `M2 ∘ π ∘ M1`

The one class surviving purely because a non-commuting step separates two masks (R4 does not
apply). Each crib position `j` gives

`a[j mod p] + b[π(j) mod q] = C[π(j)] − P[j]`,

a bipartite system whose solvability conditions are its independent cycles,
`edges − vertices touched + components`.

Measured over 400 random permutations per pair:

| p, q | free | `24 − (p+q−1)` | measured min | measured mean |
| --- | ---: | ---: | ---: | ---: |
| 3, 3 | 6 | 19 | 19 | 19.00 |
| 5, 5 | 10 | 15 | 15 | 15.01 |
| 7, 7 | 14 | 11 | 11 | 11.10 |
| **8, 10** | 18 | **7** | **7** | 7.60 |
| 10, 10 | 20 | 5 | 5 | 5.74 |
| 12, 12 | 24 | 1 | 1 | 2.85 |
| 13, 13 | 26 | −1 | 0 | 1.83 |

> **Correction to Checkpoints AA and AC.** Both stated that disconnection of the bipartite graph
> *lowers* the constraint count. That is backwards. For fixed edges and vertices, more components
> means more independent cycles, so disconnection **raises** it. `24 − (p+q−1)` is a **lower
> bound** attained in the connected, fully-occupied case, not an upper bound. The class is
> therefore slightly better constrained than those checkpoints claimed. This is recorded
> prospectively; no conclusion changes, because the class fails on evidence, not on power.

**Status: PARTIALLY DECIDABLE (decidable for short periods) but REQUIRES NEW DOCUMENTARY
PARAMETER.** Checkpoint V found no statement that K4 inherits K1/K2 key lengths or methods, and
`LAYER TWO` does not supply one. **Do not search (8, 10) merely because it survives** — choosing
it would convert "earlier sections contain clues" into an exact Layer-A inheritance rule no
source states.

### I. Free polygraphic inner map + bounded outer map

**VACUOUS WITH 24 CRIBS**, and provably so.

The 11 crib digraphs are all distinct at both alignments, and so are their 11 ciphertext images.
So the input-to-output relation is already a partial injection and a consistent injective inner
map exists **even when the outer map is pinned to the identity** — the most bounded bijection
there is. Checkpoint AC verified this by construction. The same holds at block sizes 4 and 5,
where no blocks repeat either.

This row is the strongest safeguard in the census: it forecloses the endless "maybe cipher X is
hidden underneath another stage" rescue. A hidden inner stage is only ever testable if it
*shares parameters across positions* (class J), never merely because the outer stage is bounded.

The single exception is block size 3, whose one repeated trigram per alignment lies at distance
9 — refuting a periodic additive outer mask of period 1, 3 or 9 and nothing else.

### J. Structured polygraphic / fractionating stage + fixed readout

The contrasting case, and the reason class I is about freedom rather than about polygraphy.

What makes such a class decidable is exactly four things: **a shared finite parameter set**
(one grid or cube serving all positions), **repeated use** of it, **a fixed readout**, and
**enough equality/disequality interaction** to bite. Trifid on a 3×3×3 cube has all four, which
is why 179 of 194 configurations are refutable — 175 by Codex AB's propagation, 4 more by
Checkpoint AC's exact CSP.

**This does not generalize to "all fractionation."** It generalizes only to the architectural
recipe above. A fractionator whose grid is re-keyed per block, or whose readout is
position-varying, loses the sharing and falls back to class I or K.

The 15 remaining Trifid configurations are **CONDITIONALLY SAT / UNDERCONSTRAINED** — compatible
with the ciphertext and both cribs, with 45–48 free ternary classes against 24 crib letters, so
compatibility is the expected outcome and carries essentially no evidential weight. They are
**not candidates**, must not be chased, optimised, language-scored or relabelled, and the family
was selected post hoc.

### K. Position-varying outer mask + inner stage

**VACUOUS / ZERO CONSTRAINTS**, by AA-Theorem 1 directly. If the mask parameters at the crib
positions are free and the inner map is free over the exercised blocks, invert the mask to
obtain the intermediate text and assign the inner map on distinct arguments: every ciphertext
fits, for every mask. Verified over 4,000 random masks at 100% consistency, with the injectivity
filter matching its birthday null (93.6% against 92.2%).

Together with I, this closes the two largest rescue routes in the residual space.

### L. Arbitrary fixed 26×26 combiner — `C[i] = T[P[i]][k[i]]`

676 free cells. Constraints require **repeated `(plaintext, key)` input pairs**, and the crib
geometry supplies almost none:

| key period | 2 | 3 | 5 | 8 | 10 | 13 | 17 | 26 | free |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| repeated input pairs | 4 | 6 | 2 | **0** | **0** | **0** | 1 | **0** | 0 |

At periods 8, 10, 13 and 26 — and for any free keystream — an arbitrary table receives **zero**
constraints. **VACUOUS WITH 24 CRIBS.** Do not enumerate one. A non-shift table becomes
meaningful only if some independent evidence names a *specific* finite table family, which none
does; the named candidates are already closed (R5, plus EXP-037 for standard Porta, direct and
composed, and Quagmire IV needing an unevidenced second alphabet).

### M. Length-changing or non-position-preserving inner encoding

Not rejected — but incomplete as stated. The public clues give **exact numbered plaintext
anchors**, so any such architecture must itself supply a deterministic mapping between
ciphertext positions and plaintext positions. Without one, the cribs cannot even be applied and
no constraint exists to test.

**Status: REQUIRES EXTRA ALIGNMENT/STATE RULE** unless the architecture provides it. Standard
Fractionated Morse is separately and structurally closed by Morse-length arithmetic against the
positional crib semantics (Checkpoint O/P); **that result must not be generalized** to the wider
class, and the Digrafid closure rests specifically on the primality of 97.

---

## 4. Scorecard

Ranked by expected information gain if tested next, not by interest.

| class | shared DOF | active crib constraints | decisive invariant | status | more plaintext helps? | documentary parameter helps? | documentary grade |
| --- | --- | ---: | --- | --- | --- | --- | --- |
| H two masks around `π` | `p+q` | 7 at (8,10); 15–19 at short periods | bipartite cycle count | **PARTIALLY DECIDABLE**, blocked on evidence | yes, strongly | **decisive** — a stated period or inheritance | UNSUPPORTED |
| J structured fractionation + fixed readout | grid/cube + readout | 45–48 free vs 24 | T-determinacy + injective readout | **PARTIALLY DECIDABLE**; 15 conditionally SAT | yes, strongly | decisive | UNSUPPORTED (post hoc) |
| B/G periodic schedule, p 24–26 | `p` | 5 / 3 / 1 | residue collisions | **PARTIALLY DECIDABLE**, degrading | yes | modest | STRUCTURALLY CONSISTENT |
| B/G periodic schedule, p 27–29 | `p` | **0** | residue collisions | **UNDECIDABLE WITH PRESENT CRIB GEOMETRY** | **yes — required** | modest | STRUCTURALLY CONSISTENT |
| M length-changing inner encoding | alignment rule | undefined until rule given | position correspondence | **REQUIRES EXTRA ALIGNMENT RULE** | only after the rule | **required first** | UNSUPPORTED |
| L arbitrary 26×26 table | 676 cells | 0–6 | repeated `(P,k)` inputs | **VACUOUS WITH 24 CRIBS** | only marginally | required | UNSUPPORTED |
| D source lookup, new source | table | 0 if source unique at cribs | repeated source symbols | **VACUOUS / ALREADY CLOSED** at declared scopes | yes | required | UNSUPPORTED (Layer B — Checkpoint U) |
| E arbitrary `R` | unbounded | 0 | R9 | **VACUOUS** | no | required | UNSUPPORTED |
| C arbitrary `f(i)` | 24 free | 0 net | R6 | **VACUOUS** | no — scales with the cribs | required | UNSUPPORTED |
| F arbitrary permutation | `97!` | 0 net | positional information destroyed | **VACUOUS** | yes | required | UNSUPPORTED |
| I free polygraphic behind bounded outer | free | **0** | all blocks distinct | **VACUOUS** — provably | **yes — the direct lever** | not sufficient alone | UNSUPPORTED |
| K free inner behind free mask | free | **0** | AA-Theorem 1 | **VACUOUS** — provably | no | not sufficient alone | UNSUPPORTED |
| A fixed monographic (±`π`) | ≤26 | 13–24 | repeated letters | **ALREADY CLOSED** | n/a | n/a | CONTRADICTED |
| B/G periodic **declared shift families**, p ≤ 23 | `p` | 7–22 | residue collisions | **ALREADY CLOSED** (12 committed conventions; *not* arbitrary tables — see class L) | n/a | n/a | STRUCTURALLY CONSISTENT |
| C bounded `f(i)`; E bounded `R`; F declared families | small | high | various | **ALREADY CLOSED** | n/a | n/a | mixed |

Documentary grades follow Checkpoints S, U, V, X, Y and Z. Scheidt/Sanborn evidence supports a
**custom/adapted, harder fourth process** involving masking, and — per the 1999 *Washington
Post* — one with a **historic basis**. It names **no** transform: not Trifid, not recursive
keys, not double transposition, not Porta, not a period, not a key source, not a stage order.
Generic words like *modern*, *mask*, *custom*, *adapted* and *complex* are not cipher names and
no family is inferred from them.

---

## 5. Request 7 — exactly how much one more verified letter buys

Treating additional public plaintext as an external blocker, and using **only** the structural
question of which distances a new position creates. No alleged 2025 plaintext was used.

- **Would a single letter help? Yes, and dramatically.** Of the 73 unknown positions, **48
  unlock all three blind periods** 27, 28 and 29 at once, and **70 of 73** unlock at least one.
- **Which positions maximise gain?** The head and tail extremes: **1, 3, 91, 93, 95 and 96**
  each unlock all three blind periods *and* add constraints at 34 of the 39 periods in 2–40.
  Positions in the gap (for example 53) also unlock all three. This is intuitive: distance from
  the existing runs is what creates new divisibility.
- **Which positions are worthless for the blind spot?** Exactly three — **20, 47 and 74** —
  whose distances to every crib position avoid all multiples of 27, 28 and 29. They still add
  constraints at other periods.
- **VACUOUS → DECIDABLE for the polygraphic classes (I, J) needs more than one letter.** Those
  classes are vacuous because **no plaintext block repeats**. One isolated letter creates no new
  full block. The requirement is structural rather than numerical: enough contiguous plaintext
  that two blocks of the same size and alignment coincide. A short contiguous crib is therefore
  needed, not a scattered letter — and because a repeat cannot be guaranteed in advance, the
  honest statement is that a new run *makes repeats possible*, where at present they are
  impossible at sizes 2, 4 and 5.
- **For classes B, G, H and L, single scattered letters are efficient**, since each new position
  adds residue collisions and repeated-input pairs directly.

**Summary: for periodic and mask classes, one well-placed letter is worth a great deal; for
polygraphic classes, only a contiguous run changes the verdict.**

---

## 6. Critical gate

For every still-open class: *is there a finite, precommittable parameter family supported
independently of the observed K4 crib behaviour?*

| class | finite precommittable family? | independently supported? | outcome |
| --- | --- | --- | --- |
| H two masks around `π` | yes, once `p`, `q`, `π` are fixed | **no** — no source states a period or K1/K2 inheritance | no experiment |
| J structured fractionation | yes, once cube, period, reset, readout are fixed | **no** — selected post hoc after seeing survivors | no experiment |
| B/G at p 24–29 | yes | the *class* is structurally consistent, the *periods* are not independently selected | more plaintext, not more compute |
| L, M, D-new, E-arbitrary, C-arbitrary, F-arbitrary, I, K | mostly no | no | no experiment |

**No class answers yes to both.** Where the answer is yes-but-underpowered, the census
prescribes **more plaintext, not more compute**.

> **No architecture is honestly eligible for EXP-040.**

---

## 7. Answers to the eight census questions

1. **Already closed:** A in full; B/G for periods ≤ 23; C and E in their bounded shared forms;
   D at every declared source scope; F for the declared single-transposition families and the
   nine precommitted double-columnar permutations; pure transposition (proved impossible);
   standard Porta, Quagmire I–III, Gronsfeld, standard Fractionated Morse, Digrafid, Gromark.
2. **Decidable now:** only the short-period regimes already exhausted. Nothing both open and
   decisive remains.
3. **Partially decidable:** H (7 constraints at the tempting (8,10), 15–19 at short periods);
   J (45–48 free against 24); B/G at periods 24–26.
4. **Mathematically vacuous:** I and K (provably, zero constraints); L at the common periods;
   arbitrary `f(i)`, arbitrary `R`, arbitrary `π`; any new source lacking crib-position repeats.
5. **Require more plaintext:** B/G at 27–29 (a hard ceiling, not an effort gap); I and J to
   escape vacuity; H and L to gain real power.
6. **Require a documentary parameter first:** H (a period or an inheritance rule), J (a named
   inner structure), L (a specific table family), M (an alignment rule), D (a named source).
7. **Minimum additional evidence to unlock the best undecidable class.** For B/G at 27–29:
   **one** verified letter, best placed at 1, 3, 91, 93, 95 or 96. For I and J: a **short
   contiguous run**, since only contiguity can create the block repeats those classes need.
8. **Eligible for EXP-040 now: none.**

---

## 8. One next action

**No architecture passes both documentary motivation and cryptanalytic decidability, so the
correct next action is evidence acquisition, not another cipher experiment.**

Pursue **Request 2 — the unedited 2005 Zetter/Scheidt interview material**, and the original
`ScheidtNova.doc` or the corresponding GBH production transcript identified at Checkpoint Z.

The published WIRED interview is explicitly described as edited for length and organization, and
**this repository has not located the unedited material; it is not claimed to be publicly
available.**

The census sharpens what would make it decisive. It is not enough for a source to say the
process was masked, custom or complex — the scorecard shows such words select nothing. The
single sentence that would collapse this census into a finite experiment is one that names
**a structured stage whose parameters are shared across positions** (class J's recipe), or a
**period or key-length inheritance** (class H's missing parameter).

Request 7 — additional verified public plaintext — remains the parallel blocker, now with
precise targeting: **one letter at 1, 3, 91, 93, 95 or 96** for the periodic classes, a **short
contiguous run** for the polygraphic ones.

K4 remains unsolved.
