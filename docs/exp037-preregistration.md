# Preregistration — EXP-037: periodic Porta, alone and composed with a transposition

Committed **before** implementation or execution. Branch `claude/k4-post-j`.
K4 remains unsolved. No external verifier. No alleged plaintext or K5 material.

## 0. Why this family, and at what grade

**Structural / historical candidate only.** Porta is a genuine hand-operable classical
polyalphabetic cipher of the right era. **No Sanborn or Scheidt evidence says K4 uses
Porta**, and none is claimed; it ranks below anything with direct Kryptos documentary
support. It is here because the evidenced families are exhausted and because it survived
the equivalence audit in `docs/combiner-coverage-matrix.md`:

- of the 207 distinct mappings from 3 combiners × 4 evidenced component pairs × 26 keys,
  exactly **one** Porta row appears (row 0 = `variant_beaufort/P=STD/C=STD/k=13`); rows
  1–12 are not representable;
- but Porta **is** conjugate to a family of even shifts under *some* pair of mixed
  alphabets, since `{Porta_n ∘ Porta_0⁻¹}` is a Z₁₃ acting regularly on two orbits of 13,
  exactly like `{Shift_0, Shift_2, …, Shift_24}`. So this experiment tests **one specific,
  precommitted, historically documented alphabet pair**, not a new algebraic class. That is
  stated now so no result can be reported as "a new combiner works/fails".

Gronsfeld and Quagmire I–III were reduced and **rejected as duplicates** before this
preregistration; Quagmire IV was rejected as an unevidenced free alphabet.

## 1. Exact inputs

`data/k4.json`, sha256 `e3b18a93c5fda5a8fc7a9249d25b1567c55cc2b5aef2843a65551b96b754ced8`;
ciphertext pinned to `eea813570c7f1fd3b34674e47b5c3da8948026f5cefee612a0b38ffaa515ceab`.
Public cribs only: `EASTNORTHEAST` [21,34), `BERLINCLOCK` [63,74) — 24 positions.

## 2. Exact table definition, provenance and generation algorithm

Giovanni Battista della Porta's reciprocal table, in its standard modern tabulation: 13
alphabets, key letters taken in pairs `AB CD EF GH IJ KL MN OP QR ST UV WX YZ`.

Generation algorithm, over an ordering `O` (a 26-letter sequence), for row `n ∈ 0…12`:

```
a = O.index(plaintext letter)
b = 13 + ((a + n) mod 13)      if a < 13
b = (a - 13 - n) mod 13        if a >= 13
ciphertext letter = O[b]
```

Row 0 must reproduce the textbook `A↔N, B↔O, …, M↔Z`; row 1 must reproduce
`A↔O, …, L↔Z, M↔N`. Both are asserted in the experiment and re-derived independently in the
verifier. Every row must be **self-reciprocal** with **zero fixed points**; both
implementations check reciprocity explicitly.

Two declared orderings, both precommitted: `O = STD` and `O = KRY`
(`KRYPTOSABCDEFGHIJLMNQUVWXZ`). No other ordering may be added.

## 3. Exact model equations

Key `k[0..q-1]` gives a **row index in 0…12** at each position; it is **never enumerated**
and is decided existentially by consistency.

- **Direct (no transposition):** `C[i] = Porta_{k[i mod q]}(P[i])`.
- **Order A:** `C[σ(j)] = Porta_{k[j mod q]}(P[j])` — residue class `j mod q`, σ-independent.
- **Order B:** `C[i] = Porta_{k[i mod q]}(P[σ(i)])` — residue class `σ⁻¹(j) mod q`,
  σ-dependent.

## 4. Alphabet and key treatment — what is absorbed

| degree of freedom | absorbed? |
|---|---|
| component ordering `O` | **NO** — carried explicitly as STD or KRY, 2 declared values |
| Porta row index per position | **yes** — decided existentially in 0…12 |
| repeating key **word** (key letters → row via the AB/CD… pairing) | **yes** — the pairing is a fixed relabelling of row indices, and any word of length `q` is one point in `{0..12}^q` |
| indicator / starting offset of the key | **yes** — absorbed by the existential key |

## 5. The decisive structural fact, computed before execution

Porta sends **every** letter to the opposite half, so for a pair `(p, c)`:

- if `p` and `c` lie in the **same half**, **no** Porta row realises it — at any key;
- if they lie in **opposite halves**, **exactly one** row realises it.

Checked against the real cribs before writing this: **16 of the 24 crib pairs lie in the
same half**, under both the STD and the KRY half-definition.

**Therefore the direct, untransposed periodic Porta family is impossible for K4 at every
period, every key and both orderings, decided by inspecting 24 letter pairs with no search
at all.** The experiment records this as an exact zero-compute elimination rather than
dressing it up as a search.

## 6. Decidability of the transposition-composed family

For a permutation σ the half-parity condition applies to `(P[j], C[σ(j)])` and becomes a
filter on σ. From K4's own ciphertext half-counts (STD: 46 lower / 51 upper; KRY: 53 / 44),
the mean per-crib cross-half probability is **0.5021** (STD) and **0.4768** (KRY), so

`P(a random σ passes all 24) ≈ 6.61×10⁻⁸` (STD) and `≈ 1.91×10⁻⁸` (KRY).

Conditional on passing, each crib pair forces a **unique** row, so a residue class with `m`
constrained positions survives with probability `13^-(m-1)`. **The null is therefore
`(cross-half)^24 × 13^-c`, not `13^-c`** — derived from the declared table family as
required, not assumed.

Constraint counts `c` are the same as EXP-036's, since the residue partition depends only
on the crib positions: 22 at q = 2 down to 7 at q = 17, 18, 23.

Expected chance survivors over the order-A family (16,151,648 permutations × 22 periods ×
2 orderings) is bounded by `16.15e6 × 6.61e-8 × Σ_q 13^-c(q) × 2 ≈ 3×10⁻⁷`. The family is
therefore decidable with enormous margin, and the experiment is cheap precisely because the
half-parity filter removes essentially everything before the row test.

**Underconstrained periods:** none in 2–23 under this null. `q = 1` (monoalphabetic Porta)
is *added* to the declared range because it costs nothing and is the simplest case;
`q ≥ 24` is excluded in advance, as in EXP-036.

## 7. Declared scope

| | transposition family | periods | orderings | orders |
|---|---|---|---|---|
| direct | none | 1–23 | STD, KRY | n/a |
| composed | **exactly EXP-036's declared families, definitions unchanged**: T1 widths 2–10 (order A) and 2–8 (order B), all column orders, both read directions and both orientations; T2 rectangle routes all widths; T3 ragged engraving-grid routes | 1–23 | STD, KRY | A and B |

Reusing EXP-036's families unchanged means the two results are directly comparable and no
new permutation code enters the trusted path.

## 8. Deduplication

Composition order is not deduplicated (orders A and B are inequivalent — re-verified).
Permutations identical across declared families are deduplicated by hashing the permutation
tuple, as in EXP-033/036. Under order A, feasibility depends on σ only through the 24
ciphertext letters it selects; permutations agreeing there are the same case, materialised
for T2/T3 and reported as a count caveat for T1. Case counts are not counts of independent
tests.

## 9. Success criterion and failure statement

A case is **FEASIBLE** iff (i) every constrained pair is cross-half and (ii) no two
constrained positions in the same residue class force different Porta rows. Nothing is
scored.

**Failure statement.** If no case is feasible: *K4 is not a periodic Porta cipher over the
STD or KRYPTOS ordering at any period 1–23, alone or composed with any transposition from
the declared EXP-036 families, in either composition order.* It does not touch Porta over
other orderings, aperiodic Porta keys, Porta composed with transpositions outside those
families, or any other reciprocal-table system.

## 10. Controls

- **Planted positives spanning every table state**: at least one plant per Porta row 0–12,
  across both orderings, both composition orders, a range of periods including `q = 1`, and
  keys with **repeated row states**; each must be detected FEASIBLE at the planted
  (σ, q, ordering) with the row sequence recovered on every constrained residue class.
- **Reciprocity** asserted independently in both the experiment and the verifier.
- **Adversarial mutations that definitely intersect active constraints**: the corrupted
  position is drawn from a residue class holding at least two constrained positions;
  classes without one are reported "not counted", never counted as passes.
- **Wrong-table-family control**: a ciphertext planted with a *Vigenère* key must be
  rejected by the Porta detector, and a Porta-planted ciphertext must be rejected by a
  shift detector — otherwise the two families are not being told apart.
- **Period-discrimination control**: each plant must be rejected at some other declared
  period; the observed rate is reported.
- Constraint counts are computed over every constrained position **before** any verdict —
  the EXP-034 invariant — and the verifier asserts it.

## 11. Verifier architecture

`audit/verify_exp037.py`, importing neither the experiment nor `k4lib`, and **building the
13 Porta tables from the definition in §2 rather than importing the production generator**.
It re-derives the half-parity fact, re-checks reciprocity and zero fixed points, rebuilds
permutations by explicit grid simulation, re-decides every declared-feasible case plus an
exhaustive recheck of the small widths and a sample of the large ones, re-derives the null
probability, asserts verdict-independent constraint counts, and replants its own positives.

## 12. Prohibited post-hoc expansions

No further orderings, periods, widths or families after seeing results. No aperiodic,
progressive or reset row schedule. No relaxation of the cross-half requirement or of the
consistency criterion into a score. No reinterpretation of a Porta result as evidence about
shift families. A feasible case would be recorded as a hypothesis only and would require a
new preregistration before any follow-up.
