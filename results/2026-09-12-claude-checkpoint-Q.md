# Checkpoint Q — stateful recursive-key test

**K4 remains unsolved.** No plaintext candidate, no mechanism, no external submission.

## Repository status

| | |
|---|---|
| branch | `claude/k4-post-j` |
| starting HEAD | `a34f11d637d31b43e7c31d14cb20804dcd2e2c80` |
| preregistration commit | `827f06b` (+ input-hash correction `4a3ea10`, both **before** execution) |
| final HEAD | this checkpoint's commit |
| `main` / `codex/k4-continuation` / `claude/dreamy-archimedes-79k6u0` | untouched |

## 1. Families admitted and rejected

**Admitted, together, decided before execution** — so that a negative on F1 could not be
followed by "add `c`" as a rescue:

- **F1** `k[n] = a·k[n-1] + b·k[n-2] (mod 26)`, params `a,b,k[0],k[1] ∈ Z26`
- **F2** `k[n] = a·k[n-1] + b·k[n-2] + c (mod 26)`, params `a,b,c,k[0],k[1] ∈ Z26`

`k[0]`, `k[1]` are the key values at K4 positions 0 and 1 — message-aligned, no primer offset.
Key values range over the **full Z26**, which is exactly the gap Gromark's digit-restricted
rejection left open at Checkpoint O.

**Rejected before admission:** polynomial models of degree ≥ 2 are *unreachable* by an order-2
recurrence (the characteristic polynomial can only be `(x−1)^≤2`), so they were not counted as
part of this family at all.

## 2. Duplicate audit — computed, not assumed

Because Z26 is not a field, distinct parameter tuples generate identical streams. Counts are
reported at all three levels, and feasibility is decided on the **crib projection**:

| quantity | F1 | F2 |
|---|---:|---:|
| raw parameter tuples | 456,976 | 11,881,376 |
| unique 97-key streams | — | **7,585,006** (collapse 1.57×) |
| unique 24-position crib projections | **172,375** | **4,481,750** (collapse 2.65×) |

**Overlap with prior coverage:**

| overlap | criterion | count |
|---|---|---:|
| EXP-006 **progressive** (arithmetic progression) | exactly the `(a,b) = (2,25)` locus, i.e. characteristic polynomial `(x−1)²` | 17,576 unique streams (4,472 of them also periodic) |
| EXP-006 **polynomial** degree ≥ 2 | unreachable at order 2 | — |
| EXP-036 / EXP-006 **periodic** | **97-prefix exactly periodic with `p ≤ 23`** → tagged `ALREADY COVERED` | **1,701,518** unique streams |
| **genuinely new** | remainder | **5,883,488** |

The periodicity criterion is deliberately the *actual 97-value stream*, not eventual
periodicity of the state machine: a recurrence is only tagged as covered if it genuinely *is*
a period-`p ≤ 23` key over the message.

## 3. Expected survivors — exact, from the family's own image

Not `26^(params − constraints)`. For fixed `(a,b,c)` the recurrence is linear in the state,
`k[n] = A_n·k[0] + B_n·k[1] + c·D_n`, so the realised image is computable:

- distinct crib projections realisable by F2: **4,481,750** of `26²⁴ ≈ 9.107 × 10³³`
- `P(a uniform random 24-vector is realisable) = 4.921 × 10⁻²⁸`
- **expected survivors over the 12 convention targets = 5.906 × 10⁻²⁷**

Twenty-seven orders of magnitude below one, so a zero is a genuine elimination rather than an
expected outcome. No convention is underdetermined: 24 constraints against at most 5
parameters.

## 4. Result

The closed form was checked against direct iteration on 500 random tuples (0 mismatches),
which turns each `(a,b,c)` into an exact **24 × 2 linear system over Z26** in the initial
state — so the state is decided existentially rather than enumerated: **210,912 exact solves**
instead of 143 million trials, in 16 seconds.

| | |
|---|---:|
| `(a,b,c)` × convention systems solved exactly | **210,912** |
| **FEASIBLE on all 24 cribs** | **0** |
| feasible on crib block 1 alone (13 positions) | **0** |
| feasible on crib block 2 alone (11 positions) | **0** |

The per-block diagnostic is the informative part of the zero. Each block alone overdetermines
the 2-dimensional state, and a family that satisfied one block but not the other would look
quite different from one that satisfies neither. **Neither block is satisfiable on its own** —
the failure is not a near-miss that a small change would repair.

## 5. Controls

- **Planted positives 14/14**, each detected with the initial state recovered. Coverage
  exercised as preregistered: `a=0` (2), `a=1` (3), `b=0` (3), `b=1` (2), non-unit coefficients
  (8), even (7) and odd (11) coefficients, repeated initial values (5), `k[0]=0` (3),
  `k[1]=0` (3), nontrivial affine `c` (7), short orbit (5), long orbit (9).
- **Adversarial 14/14 flipped**, with **0 not counted** — each alteration targets a forced key
  value at a position that genuinely participates in the constraint set, and capability is
  checked by construction before the control is scored.

## 6. Independent verification

`audit/verify_exp038.py` imports neither the production recurrence generator nor `k4lib`. It
re-parses the frozen data, independently implements STD/KRY indexing and all three combiners,
and generates the recurrence by **direct iteration of the definition** rather than by the
closed form the experiment uses — so an error in that algebra cannot hide behind itself.

**16/16 checks pass**, and the exhaustive path was affordable, so no sampling certificate was
needed:

- **F1 re-decided exhaustively: 456,976 tuples × 12 conventions — zero feasible**
- **F2 re-decided exhaustively: 11,881,376 tuples × 12 conventions — zero feasible**
- forced key targets re-derived independently for all 12 conventions and found identical
- unique-stream count (7,585,006) and `p ≤ 23` count (1,701,518) reproduced exactly
- replanted recurrences recovered, so the verifier is not a rubber stamp

## 7. Exact model-limited conclusion

> **No full-Z26 second-order affine self-evolving keystream — under the 12 committed shift
> conventions, message-aligned, without reset or transposition — satisfies the 24 published
> K4 positional cribs.**

Explicitly **not**: "recursive keys are eliminated", "stateful systems are eliminated", "K4 is
not autoregressive", or "K4 must use an external source". Higher-order, nonlinear, reset,
externally seeded and other state machines remain open, and none of the prohibited post-hoc
variants (order 3, resets, reversed recurrence, other moduli, nonlinear terms, text feedback,
transposition, new alphabets) was tried.

## 8. Surviving architectures

| rank | architecture | grade | falsifiable now? |
|---|---|---|---|
| 1 | Long key from an **unidentified external source** | DOCUMENTARY-MOTIVATED | **No** — moves on evidence naming a source, not on search |
| 2 | **Double transposition** from a precommitted key family, or keyed columnar width ≥ 12 | STRUCTURALLY-MOTIVATED (K3 is a transposition Sanborn built himself; the keywords are published) | **Yes**, as a small precommitted family |
| 3 | Higher-order / nonlinear / reset state machines | SPECULATIVE-BUT-OPEN — and extending order 2 → 3 with no new motivation would be the rescue pattern this programme rejects | Decidable, but needs independent motivation first |
| 4 | Custom full-26 fractionation | SPECULATIVE-BUT-OPEN | Only once written as equations |
| 5 | Clock as state/index; semantic inner encoding | SPECULATIVE-BUT-OPEN | No mechanism stated |
| 6 | Physical panel-alignment models | parked | Blocked on Request 4 |

## 9. ONE next recommended action

> **Preregister and run monoalphabetic substitution composed with DOUBLE transposition, where
> both transposition keys come from a precommitted list of published Kryptos keywords.**

**Why this and not more recursion.** Order 2 → order 3 is the rescue pattern, and it has no
motivation beyond "the last one failed". Double transposition has real motivation: K3 *is* a
transposition Sanborn implemented himself, and `KRYPTOS`, `PALIMPSEST` and `ABSCISSA` are
published keywords demonstrably his — so the key family is precommitted from evidence rather
than invented.

**Why it is not duplicate.** EXP-033 covered any fixed `A–Z → A–Z` substitution composed with a
**single** transposition from its declared family; EXP-036 covered periodic shifts composed
with the same single transpositions. A composition of two columnar transpositions is a
permutation outside both declared families, even though it is inside EXP-033's *criterion*.

**Why it is falsifiable and cheap.** EXP-033's exact consistency test gives a chance-feasibility
of `6.6 × 10⁻¹⁷` per permutation, so a family stays decidable up to about 10¹⁴ permutations.
Full double columnar at widths ≤ 11 is ≈ 1.9 × 10¹⁵ — too big — which is exactly why the key
list must be **precommitted and small**: keyword-derived column orders at a declared width
range give thousands of permutations, not quadrillions. Compute the family size and the null
from the keyword list *before* implementing, and if the list has to be padded with unevidenced
words to make the search interesting, do not run it.

**What would eliminate it.** Zero feasible permutations across the precommitted family, with
planted positives spanning both transposition stages, adversarial controls that intersect
constrained positions, and a verifier that rebuilds both permutations by explicit grid
simulation. That would close the last structurally-motivated composition on the list.

**Setup a fresh session needs:** cribs `[21,34)` and `[63,74)` zero-based, public-source
verified; the exact-consistency pattern is in `experiments/exp033_subst_transposition.py`; the
columnar machinery is `k4lib/transpositions.py` (already self-tested and independently
re-derived by `audit/verify_exp033.py`); the constraint-count-before-verdict invariant is
mandatory; and `docs/combiner-coverage-matrix.md` holds the reduction rule that any candidate
must pass before it gets a number.
