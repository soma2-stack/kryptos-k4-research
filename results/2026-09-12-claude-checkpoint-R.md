# Checkpoint R — keyword double-transposition test

**K4 remains unsolved.** No plaintext candidate, no mechanism, no external submission.

## Repository status

| | |
|---|---|
| branch | `claude/k4-post-j` |
| starting HEAD | `f6c7ddd66e2318ff1a485298e3f4f87135f45332` |
| preregistration commit | **`d594660`** — committed before any crib verdict was computed |
| final HEAD | this checkpoint's commit |
| `main` / `codex/k4-continuation` / `claude/dreamy-archimedes-79k6u0` | untouched |

**Grade: STRUCTURALLY MOTIVATED, not documentary.** K3 shows Sanborn used transposition and
the three keywords are genuinely documented Kryptos words — but nothing says K4 uses double
columnar transposition, and nothing here claims otherwise.

## 1. Frozen convention and exact keyword rankings

Row-wise fill into `w = len(keyword)` columns, **no padding** (ragged, column lengths
`ceil((97−c)/w)`), rank columns by `(keyword letter, original column index)` with ties broken
left-to-right, read in increasing rank, both passes encryption-direction, length 97 throughout.

Hand-derived and asserted in code rather than trusting library sort behaviour; the verifier
rebuilds them with a selection sort instead of `sorted()`:

| keyword | w | read order | ranked letters |
|---|---:|---|---|
| `KRYPTOS` | 7 | `[0,5,3,1,6,4,2]` | K0 O5 P3 R1 S6 T4 Y2 |
| `PALIMPSEST` | 10 | `[1,7,3,2,4,0,5,6,8,9]` | A1 E7 I3 L2 M4 P0 **P5** S6 **S8** T9 |
| `ABSCISSA` | 8 | `[0,7,1,3,4,2,5,6]` | A0 **A7** B1 C3 I4 S2 **S5 S6** |

Repeated letters (`PALIMPSEST` P@0,5 and S@6,8; `ABSCISSA` A@0,7 and S@2,5,6) are resolved by
that single frozen rule. **No alternative tie convention was tried.**

## 2. The nine ordered pairs and the duplication audit

All 9 ordered pairs including same-key pairs, `π = T2 ∘ T1`, i.e. `π(j) = t2(t1(j))`.

| check | result |
|---|---|
| raw ordered pairs | 9 |
| **distinct composed permutations** | **9** — no pair collapses onto another |
| any composition equal to the identity | none |
| any composition equal to one of its own single passes | none |
| non-commuting keyword pairs | **all three** |
| **membership in the EXP-033 corpus** | **0 of 9 — all GENUINELY NEW** |

**The EXP-033 overlap was decided structurally, not by enumerating 175M permutations.** A
width-`w` columnar read is exactly a decomposition of the ciphertext-ordered source sequence
into consecutive arithmetic progressions of common difference ±`w`, with run lengths matching
that width's column profile and run starts forming a permutation of the columns — which
reconstructs the key deterministically or fails. That covers EXP-033 F1 (widths 2–11, every
column order, both read directions, both orientations); the 1,936-permutation F2/F3 corpus was
compared directly.

**The test was self-checked:** it correctly finds each of the three *single* passes inside
EXP-033 F1 at the right width. So the single passes are already covered and every composition
is not — which is precisely the gap this experiment was for.

## 3. Null — recomputed exactly for this family

The constraint structure is fixed by the cribs and is **identical for every permutation**, so
no keyword pair can weaken the test: 13 distinct plaintext letters (E×3, T×3, A×2, S×2, N×2,
O×2, R×2, L×2, C×2, B, H, I, K), giving `Σ(m−1) = 11` equality requirements plus 13 distinct
images for a bijection.

Computed by exact subset dynamic programming over K4's own letter multiset, drawing 24
**distinct** ciphertext positions without replacement:

| | exact probability | expected accidental survivors over 9 |
|---|---:|---:|
| FEASIBLE-FUNCTION | **9.8076 × 10⁻¹⁷** | 8.83 × 10⁻¹⁶ |
| FEASIBLE-BIJECTION | **5.5193 × 10⁻¹⁸** | 4.97 × 10⁻¹⁷ |

EXP-033's ≈6.6 × 10⁻¹⁷ came from a with-replacement independence approximation; the figures
above are exact and supersede that quote **for this experiment only**.

## 4. Result — NEGATIVE at the strongest level

Every one of the nine contradicts on the **function** criterion, which is the strongest
outcome available: not merely "no bijection exists", but *no fixed map of any kind* — not even
a collapsing one.

| first → second | verdict | witness |
|---|---|---|
| ABSCISSA → ABSCISSA | CONTRADICTION | plaintext `T` needs both `T` and `D` |
| ABSCISSA → KRYPTOS | CONTRADICTION | `T` needs both `R` and `T` |
| ABSCISSA → PALIMPSEST | CONTRADICTION | `T` needs both `B` and `O` |
| KRYPTOS → ABSCISSA | CONTRADICTION | `T` needs both `I` and `A` |
| KRYPTOS → KRYPTOS | CONTRADICTION | `T` needs both `S` and `M` |
| KRYPTOS → PALIMPSEST | CONTRADICTION | `T` needs both `R` and `S` |
| PALIMPSEST → ABSCISSA | CONTRADICTION | `T` needs both `G` and `T` |
| PALIMPSEST → KRYPTOS | CONTRADICTION | `T` needs both `F` and `T` |
| PALIMPSEST → PALIMPSEST | CONTRADICTION | `T` needs both `U` and `G` |

**FEASIBLE-FUNCTION: 0. FEASIBLE-BIJECTION: 0.**

Every witness happens to fire on plaintext `T` at plaintext position 28, simply because that
is the first repeated-letter conflict the scan reaches; each permutation sends it to a
different ciphertext position, so these are nine independent contradictions, not one.

## 5. Controls

- **Planted positives 9/9** — one per unique composed permutation, each detected with the
  substitution recovered. Coverage as preregistered: all three keywords as first pass (3 each)
  and as second pass (3 each), 3 same-key pairs, 6 different-width pairs, 8 involving a
  repeated-letter keyword.
- **Non-bijective plant**: returns **FEASIBLE-FUNCTION = True** and is **correctly rejected as
  a bijection** — so the two criteria are demonstrably distinguished.
- **Adversarial 9/9 flipped.** Each mutation targets a ciphertext symbol inside a
  **repeated-plaintext-letter group**, so every one is capable of breaking an equality
  constraint by construction. None was scored that could not affect the verdict.

## 6. Independent verification

`audit/verify_exp039.py` imports neither the experiment nor `k4lib`. It rebuilds the keyword
ranking with a **selection sort** rather than `sorted()`, and builds each columnar permutation
by **explicit grid simulation** — writing indices into a ragged grid and reading columns out —
instead of the index arithmetic the experiment uses.

**35/35 checks pass**, exhaustively over all nine pairs: read orders reproduced, no-padding
column lengths confirmed, all nine verdicts reproduced independently, both counts agreeing at
zero, replanted substitutions recovered under every pair, the non-bijective distinction
confirmed, and the adversarial mutation flipping all nine plants.

## 7. Exact model-limited conclusion

> **No standard no-padding double columnar transposition using an ordered pair drawn from
> {KRYPTOS, PALIMPSEST, ABSCISSA}, followed by any fixed monoalphabetic substitution,
> satisfies the 24 published K4 positional cribs under the preregistered columnar
> convention.**

Explicitly **not**: "double transposition is eliminated", "K4 does not use transposition",
"K4 cannot use these words in another role", or "arbitrary two-stage routes are eliminated".
The negative applies only to this tiny motivated keyword family. **No keyword was added, no
tie rule was varied, and nothing was optimised** after seeing the result.

## 8. Surviving architectures

| rank | architecture | grade | falsifiable now? |
|---|---|---|---|
| 1 | Long key from an **unidentified external source** | DOCUMENTARY-MOTIVATED | **No** — moves on evidence naming a source, not on search |
| 2 | Custom full-26 fractionation | SPECULATIVE-BUT-OPEN | Only once written as equations |
| 3 | Higher-order / nonlinear / reset state machines | SPECULATIVE-BUT-OPEN | Decidable, but extending EXP-038's order is the rescue pattern |
| 4 | Transposition families outside the declared ones — unkeyed routes at width ≥ 12, keyed columnar width ≥ 12, three or more passes | SPECULATIVE-BUT-OPEN | Only with a precommitted small key family, which the evidence no longer supplies |
| 5 | Clock as state/index; semantic inner encoding | SPECULATIVE-BUT-OPEN | No mechanism stated |
| 6 | Physical panel-alignment models | parked | Blocked on Request 4 |

**What this checkpoint costs the programme.** Rank 2 at Checkpoint Q was "double transposition
from a precommitted key family" — the last *structurally motivated* composition on the list.
It is now closed at the only key family the evidence actually supplies. Everything remaining
is either documentary-but-unfalsifiable (rank 1) or speculative. That is a real narrowing, and
it is worth stating plainly rather than reshuffling the list to keep a search available.

## 9. ONE recommended next action

> **Stop searching and pursue Request 4: the Jim Sanborn papers, Archives of American Art,
> Series 3, Box 6, Folder 10, `Pre-Production and Notes, 1990–1999`.**

**Why this rather than another family.** Six sessions of exact eliminations have converged on
a single shape: every architecture this repository can *name* from public evidence has been
tested and failed, and everything still open is either unfalsifiable without a named key
source (rank 1) or has no motivation beyond logical possibility (ranks 2–5). Choosing among
the speculative ranks would be picking a family because compute is available, which is exactly
what this programme has repeatedly refused to do.

**Why it is not duplicate work.** Request 4 has never been attempted — external access was
blocked in every session where it was raised, and it was correctly kept non-blocking while
falsifiable analysis remained. That analysis has now run out.

**What it could supply.** Pre-production notes and fabrication material could name a key
source, a keyword, a device, or a layout — the one input that would move rank 1 from
unfalsifiable to testable. It is also the only open request that could reopen the parked
physical models, since a punch layout or fabrication drawing would settle whether a common
horizontal lattice exists.

**What would close it.** If the folder contains no cryptographic material — only fabrication
correspondence — then the repository should record that the public evidence base is exhausted
for architecture selection, and future sessions should not manufacture families to keep
searching. That is a legitimate and informative outcome.

**Caveat to carry:** if the folder does contain solution-adjacent material, the contamination
protocol applies — take provenance, layout and keying information; do **not** ingest anything
that amounts to K4 plaintext.
