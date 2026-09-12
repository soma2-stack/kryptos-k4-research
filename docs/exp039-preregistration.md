# Preregistration — EXP-039: fixed monoalphabetic substitution ∘ double columnar transposition, Kryptos-keyword keys only

Committed **before** any K4 crib verdict is computed. Branch `claude/k4-post-j`, base
`f6c7ddd66e2318ff1a485298e3f4f87135f45332`. K4 remains unsolved. No external verifier. No
alleged plaintext, purported solution, or K5 material.

The permutation audit and null below were computed **without evaluating a single crib
verdict**, so the information-gain gate is decided before the experiment can see its answer.

## 1. Exact inputs

| input | sha256 |
|---|---|
| `data/k4.json` | `d710d758e92abc7c4ac87da189baef936ee97c18ba1636c2ee0021ebe673f4e5` |

Ciphertext pinned by `k4lib.data` to
`eea813570c7f1fd3b34674e47b5c3da8948026f5cefee612a0b38ffaa515ceab`.

Public cribs, public-source verified at Checkpoint P, **not to be slid**:
`EASTNORTHEAST` at zero-based `[21,34)`, `BERLINCLOCK` at `[63,74)` — 24 plaintext positions.

## 2. Grade

**STRUCTURALLY MOTIVATED, not documentary.** K3 demonstrates Sanborn used transposition, and
`KRYPTOS`, `PALIMPSEST` and `ABSCISSA` are genuinely documented Kryptos words. **There is no
evidence that K4 uses double columnar transposition**, and none is claimed.

## 3. Keyword list — frozen, closed

`KRYPTOS` (w=7), `PALIMPSEST` (w=10), `ABSCISSA` (w=8). **No other word may be added after
seeing results.** All 9 ordered pairs, same-key pairs included, because excluding them would
itself be an unsupported assumption. Order matters and is not deduplicated a priori.

## 4. Frozen columnar convention

1. Write the 97 symbols **row-wise** into `w = len(keyword)` columns.
2. **No padding**; the final row is ragged and column lengths are `ceil((97-c)/w)`.
3. Rank columns by the **alphabetical order of the keyword letters**.
4. **Repeated-letter tie rule:** sort by `(keyword_letter, original_column_index)` — ties broken
   left-to-right by original column position. This is frozen now, before any feasibility is
   evaluated. **Only this one rule is tested**; no alternative tie convention will be tried
   afterwards.
5. Read columns in **increasing rank order**.
6. The second pass acts on the resulting 97-symbol stream with its own keyword, same rule.
7. Both passes are **encryption-direction** columnar transpositions.
8. Length is exactly 97 throughout.

Hand-derived rankings, asserted in code rather than trusting library sort behaviour:

| keyword | w | read order (column indices) | ranked letters |
|---|---:|---|---|
| `KRYPTOS` | 7 | `[0,5,3,1,6,4,2]` | K0 O5 P3 R1 S6 T4 Y2 |
| `PALIMPSEST` | 10 | `[1,7,3,2,4,0,5,6,8,9]` | A1 E7 I3 L2 M4 P0 P5 S6 S8 T9 |
| `ABSCISSA` | 8 | `[0,7,1,3,4,2,5,6]` | A0 A7 B1 C3 I4 S2 S5 S6 |

Repeated letters handled: `PALIMPSEST` has P@0,5 and S@6,8; `ABSCISSA` has A@0,7 and S@2,5,6.

## 5. Model, and the algebraic simplification

A fixed monoalphabetic substitution acts letterwise and therefore **commutes** with a pure
position permutation. So `S ∘ T2 ∘ T1` and `T2 ∘ T1 ∘ S` are **not** separate families and the
case count is **not** doubled for substitution order. The model is

> `C[π(j)] = S(P[j])`  with  `π = T2 ∘ T1`, i.e. `π(j) = t2(t1(j))`

for one composed positional permutation `π` and one fixed substitution `S : A–Z → A–Z`.

**The cribs are fixed at their published PLAINTEXT positions.** The permutation is applied
first, and the substitution constraint is formed at ciphertext position `π(j)` — *not* at
position `j`. Requiring `P[i] ↔ C[i]` after transposition would be wrong, and is exactly why
this family differs from the position-preserving substitution families.

`S` is **never enumerated**: all 26²⁶ functions are decided exactly by consistency, as in
EXP-033. If no arbitrary function exists, no bijection exists either.

## 6. Duplication audit — completed before this preregistration

| check | result |
|---|---|
| raw ordered pairs | 9 |
| distinct composed permutations | **9** — no ordered pair collapses onto another |
| any composition equal to the identity | none |
| any composition equal to one of its own single passes | none |
| non-commuting keyword pairs | all three: (KRYPTOS,PALIMPSEST), (KRYPTOS,ABSCISSA), (PALIMPSEST,ABSCISSA) |
| **membership in the EXP-033 corpus** | **0 of 9 found — all GENUINELY NEW** |

The EXP-033 overlap was decided **structurally**, not by enumerating 175M permutations: a
width-`w` columnar read is exactly a decomposition of the ciphertext-ordered source sequence
into consecutive runs that are arithmetic progressions of common difference ±`w`, with run
lengths matching that width's column profile and run starts forming a permutation of the
columns. That reconstructs the key deterministically or fails. The test covers EXP-033 F1
(widths 2–11, every column order, both read directions, both orientations) and was
**self-checked**: it correctly finds each of the three *single* passes inside F1, at the right
width. The small F2/F3 corpora (1,936 permutations) were compared directly.

So each single pass is already inside EXP-033, and **every one of the nine compositions is
outside it**.

## 7. Null — recomputed exactly for this family

The constraint structure is fixed by the cribs and is **identical for every permutation** (the
plaintext groups do not depend on `π`), so no keyword pair can weaken the test:

- 13 distinct plaintext letters: E×3, T×3, A×2, S×2, N×2, O×2, R×2, L×2, C×2, B, H, I, K
- `Σ(m−1) = 11` equality requirements, plus 13 distinct images for a bijection

Under the null of a random position permutation — 24 **distinct** ciphertext positions drawn
without replacement — computed exactly by subset dynamic programming over K4's own letter
multiset (not by the independence approximation EXP-033 used):

| | exact probability | expected accidental survivors over 9 |
|---|---:|---:|
| FEASIBLE-FUNCTION | **9.8076 × 10⁻¹⁷** | 8.83 × 10⁻¹⁶ |
| FEASIBLE-BIJECTION | **5.5193 × 10⁻¹⁸** | 4.97 × 10⁻¹⁷ |

EXP-033 quoted ≈6.6 × 10⁻¹⁷ for its own family under a with-replacement approximation; the
figures above supersede that quote **for this experiment only**.

**Gate: PASSED**, by roughly fifteen orders of magnitude.

## 8. Success criterion and failure statement

Reported **separately**:

- **FEASIBLE-FUNCTION** — the induced map plaintext letter → ciphertext letter is well defined.
- **FEASIBLE-BIJECTION** — additionally injective.

A contradiction at the **function** level is the strongest outcome. Nothing is scored: **no
language scoring, no hill climbing, no annealing, no substitution optimisation.** The cribs
decide the model exactly.

**Failure statement.** If every genuinely new composed permutation is contradictory:

> No standard no-padding double columnar transposition using an ordered pair drawn from
> {KRYPTOS, PALIMPSEST, ABSCISSA}, followed by any fixed monoalphabetic substitution,
> satisfies the 24 published K4 positional cribs under the preregistered columnar convention.

It will **not** be reported as "double transposition is eliminated", "K4 does not use
transposition", "K4 cannot use these words in another role", or "arbitrary two-stage routes are
eliminated". The negative applies only to this tiny motivated keyword family.

## 9. Controls

**Positive**, one per unique keyword-pair permutation (all 9): choose a fixed substitution,
build a plaintext carrying the public crib letters at the real crib positions, apply T1 then
T2, apply the substitution, and require the experiment to report FEASIBLE with the mapping
recovered. Coverage required: all 3 keywords as first pass; all 3 as second pass; same-key
pairs; different-width pairs; both repeated-letter keywords.

**Non-bijective control:** at least one planted map that is deliberately collapsing must return
**FEASIBLE-FUNCTION but NOT FEASIBLE-BIJECTION**.

**Adversarial:** mutate a ciphertext symbol that participates in a **repeated-plaintext-letter**
consistency constraint, and require a previously feasible plant to become contradictory. Every
adversarial control must be capable of flipping the verdict by construction; mutations at
positions irrelevant to the constrained mapping are **not counted**.

## 10. Independent verifier

`audit/verify_exp039.py`, importing neither the EXP-039 implementation nor `k4lib`. It
independently implements keyword ranking, the repeated-letter tie rule, ragged no-padding
column lengths, the one-pass columnar permutation, composition of two passes, all nine ordered
pairs, deduplication, the 24 crib constraints, and both feasibility criteria. With nine pairs,
verification is **exhaustive**.

## 11. Prohibited post-hoc expansions

After seeing the result, do **not** add: BERLIN, CLOCK, EAST, NORTHEAST, BERLINCLOCK,
EASTNORTHEAST, CIA, SANBORN, SCHEIDT, arbitrary dictionary words, reversed keywords, alternate
tie-breaking, padding symbols, a different fill direction, alternating passes, width 12+,
arbitrary column permutations, a third transposition, or periodic substitution. Any of these
requires fresh independent motivation and a new preregistration.

## 12. If a pair survives

No optimisation follows. Each survivor will be independently reproduced; its forced
substitution mapping derived and reported; stated as a full bijection or only a partial map;
the number of **unconstrained** substitution letters counted; only the fixed-constraint-determined
positions decrypted, with **no language filling** of the remainder; and the survival compared
against the preregistered chance above. A crib-consistent pair is a **candidate architecture,
not a solution**, and the keyword list will not be expanded because something nearly fits.
