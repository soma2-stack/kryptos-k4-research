# Preregistration — EXP-041: additive two-tap propagating plaintext feedback

**Branch:** `claude/dreamy-archimedes-79k6u0`. **Written before implementation.**
**Starting HEAD:** `8f80a84d06bb43c82ad4e527ffbd3c300992488a`.

## 1. Phase 1 — theory, computed before any experiment was proposed

Model: `k[i] = α·P[i−a] + β·P[i−b] + γ`, with `P[i] = uncombine(C[i], k[i])`.

Because the recursion is linear, every `P[i]` is **affine in the unknowns**, so each crib
position contributes one linear equation over Z26. The unknowns are the `b` warm-up key values
(plus one if `γ` is free) — and **`b` alone**, not `a`, sets the parameter count.

The dependency graph joins `i` to `i−a` and `i−b`, so it splits into `gcd(a,b)` components. Per
the EXP-040 crib-span insight, constraints arise where several crib positions land in the same
component; the exact accounting is done by rank rather than by counting cribs.

**Result:** for `1 ≤ a < b ≤ 19` **no pair is vacuous**. Chance of accidental solvability is
`≈ 26^(b−24)`, ranging from `7.4×10⁻³²` at `b = 2` to `3.2×10⁻⁹` at `b = 18`.

## 2. Phase 2 — reductions applied before scoping

| # | Reduction | Effect |
| --- | --- | --- |
| R1 | Substituting `P[j] = C[j] − k[j]` gives `k[i] + k[i−a] + k[i−b] = C[i−a] + C[i−b]` — a linear recurrence on the key **with a ciphertext driving term**. EXP-038 registered an **autonomous** affine recurrence with no driving term. | **Not a reduction.** Genuinely outside EXP-038. |
| R2 | Ciphertext two-tap `k[i] = C[i−a] + C[i−b]` has no unknowns beyond warm-up, and EXP-008 already swept `k[i] = a·C[i−L] + c·C[i−M] + b` for `L < M ≤ 25` with general coefficients. | **Duplicate of EXP-008. Excluded.** |
| R3 | `β = 0` or `a = b` collapses to one-tap, which is EXP-040. | Excluded by `a < b`. |
| R4 | Canonicalising each configuration up to unit scaling of the unknowns and RREF of the augmented system collapses **10,949 of 32,832** configurations (33.3%). Confirmed example: `(a=1, b=2, α=β=+1, vigenere)` is the **same test** as `(a=1, b=2, α=β=−1, variant beaufort)`. | **21,883 distinct tests** remain. |

## 3. Declared scope, frozen now

| axis | values |
| --- | --- |
| taps | `1 ≤ a < b ≤ 19` |
| coefficients | `(α,β) ∈ {(1,1), (1,−1), (−1,1), (−1,−1)}` — the additive family only |
| offset `γ` | `0`, or free |
| combiner | vigenere, beaufort, variant beaufort |
| plaintext / ciphertext alphabet | STD, KRY each |
| direction | forward `k[i] = α·P[i−a] + β·P[i−b]`; reverse `k[i] = α·P[i+a] + β·P[i+b]` |
| key-index alphabet | **plaintext alphabet only** |

**Enumerated: 32,832. Distinct after canonicalisation: 21,883.** Exact linear solves, no search.

**Excluded in advance, with reasons:**

- `b ≥ 20` — chance rises above `10⁻⁶`; reported as **WEAK / UNDECIDABLE**, never as survivors.
- **Row reset** — Checkpoint T found that physical row breaks do **not** select a reset, so it is
  not independently motivated here; it would also add `4b` unknowns and drive most of the space
  into vacuity.
- **Key-index alphabet ≠ plaintext alphabet** — re-indexing the fed-back letters makes the
  recursion non-linear, which leaves the "smallest structured case".
- **Mixed plaintext/ciphertext taps, nonlinear functions, lookup tables, ≥3 taps, irregular tap
  schedules, position-dependent functions, and feedback composed with transposition** — all out
  of scope.

## 4. Decision rule

A configuration is **FEASIBLE** iff its linear system is solvable over Z26, decided exactly by
CRT through GF(2) and GF(13). No scoring, no threshold, no language model.

Any FEASIBLE configuration must then **reconstruct all 97 plaintext letters and re-encrypt to
the exact K4 ciphertext** before it is reported as anything more than a linear-algebra survivor.

## 5. Null expectation, stated before execution

Per-configuration chance is `26^(effective rank − 24)`. Computed over the 21,883 distinct
configurations **before running**:

- worst single configuration: **2.188 × 10⁻⁶**
- **expected accidental survivors: 2.200 × 10⁻³**

This is ~100× looser than EXP-040's `2×10⁻⁵`, so a survivor is roughly a 1-in-450 event under
the null. **Any survivor will therefore be treated as presumptively accidental** until the full
reconstruction test and the independent verifier both confirm it.

## 6. Controls

1. **Positive.** Synthesise a two-tap additive feedback ciphertext whose plaintext carries the
   **real cribs at the real K4 positions**; the decision procedure must accept it and recover the
   warm-up values and full plaintext.
2. **Adversarial.** Corrupt a position the dependency graph says must create a contradiction; the
   test must reject.
3. **Blind-region.** Demonstrate at least one modification in an absorbed region that does **not**
   flip the verdict, confirming the EXP-040 crib-span theory rather than mistaking it for a bug.

## 7. Prohibited post-hoc moves

No widening of `a`, `b`, coefficients, alphabets, directions or `γ`; no nonlinear functions; no
third tap; no transposition; no reset; no language scoring; no reporting a `b ≥ 20` configuration
as a survivor; no re-running with a broadened scope after seeing results.

## 8. Scope of any negative, stated in advance

A negative would **not** eliminate: nonlinear two-input functions; multiplication or lookup-table
feedback; three or more taps; feedback composed with transposition; irregular tap schedules;
position-dependent functions; or state machines not expressible as this recurrence.
