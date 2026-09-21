# EXP-041 — additive two-tap propagating plaintext feedback

**Branch:** `claude/dreamy-archimedes-79k6u0`. **Starting HEAD:** `8f80a84`.
**Preregistration:** `docs/exp041-preregistration.md`, committed at `181760d` **before** implementation.
**Code:** `experiments/exp041_two_tap_feedback.py`. **Verifier:** `audit/verify_exp041.py`.

## Result

**32,832 configurations enumerated, 21,883 distinct tests decided, 0 FEASIBLE.**

Exhaustively negative at the registered scope. Every configuration is settled by exact linear
algebra over Z26 through CRT — no search, no scoring, no language model.

## Phase 1 — theory, done before the experiment was proposed

`k[i] = α·P[i−a] + β·P[i−b] + γ`, with `P[i] = uncombine(C[i], k[i])`.

The recursion is linear, so every `P[i]` is **affine in the unknowns** and each crib position
contributes exactly one linear equation. The unknowns are the `b` warm-up key values (plus one if
`γ` is free), so **`b` alone sets the parameter count — `a` does not.** The dependency graph
splits into `gcd(a,b)` components.

**No `(a,b)` pair with `b ≤ 19` is vacuous.** Chance of accidental solvability is `≈ 26^(b−24)`:
`7.4×10⁻³²` at `b = 2`, rising to `3.2×10⁻⁹` at `b = 18`.

## Phase 2 — reductions, applied before scoping

- **Outside EXP-038.** Substituting `P = C − k` gives `k[i] + k[i−a] + k[i−b] = C[i−a] + C[i−b]`
  — a key recurrence **with a ciphertext driving term**. EXP-038 registered an **autonomous**
  affine recurrence with no driving term, so this is not a reduction.
- **Ciphertext two-tap is a duplicate.** `k[i] = C[i−a] + C[i−b]` has no unknowns beyond warm-up
  and EXP-008 already swept `k[i] = a·C[i−L] + c·C[i−M] + b` for `L < M ≤ 25`. **Excluded.**
- **One-tap excluded** by `a < b` (that is EXP-040).
- **Equivalence collapse.** Canonicalising up to unit scaling of the unknowns plus RREF of the
  augmented system collapses **10,949 of 32,832 configurations — exactly 33.3%**. A concrete
  confirmed instance: `(a=1, b=2, α=β=+1, vigenere)` is **the same test** as
  `(a=1, b=2, α=β=−1, variant beaufort)`. **21,883 genuinely distinct tests remain.**

## Controls — all three pass

1. **Positive.** A planted `a=3, b=7` two-tap ciphertext whose plaintext carries the **real cribs
   at the real K4 positions** was accepted with exactly **one** solution, and the full 97-letter
   plaintext was rebuilt identically. A true instance would have been detected.
2. **Adversarial.** Corrupting index 30, inside the crib span, **rejects**.
3. **Blind-region.** Corrupting index 96, beyond every crib, is **absorbed** — the verdict does
   not change. This confirms the EXP-040 crib-span theory in a second, independent family rather
   than mistaking it for a bug.

## Null, stated before execution

Worst single configuration `2.188×10⁻⁶`; **expected accidental survivors `2.200×10⁻³`**. That is
roughly 100× looser than EXP-040, so any survivor would have been presumptively accidental. None
occurred.

## Independent verification

`audit/verify_exp041.py` imports neither the experiment nor `k4lib`; all linear algebra in it is
written from scratch. **All checks pass.**

- **Route A — certificates of infeasibility.** The experiment asked a solver whether each system
  was solvable. The verifier instead demands a **witness**: a vector `w` with `w·M ≡ 0` and
  `w·rhs ≢ 0` modulo 2 or 13, which is a self-contained proof that no solution exists, checkable
  by plain arithmetic with no solver trusted. **All 32,832 configurations — full coverage, no
  sampling — carry a verified certificate.**
- **Route B — brute force, encrypt direction, no linear algebra at all.** For `b = 2` it
  enumerates every warm-up pair, runs the recursion forward, **re-encrypts**, and demands both
  that K4 comes back and that the cribs match. 32,448 pairs, zero feasible.
- **Route C — independent recomputation** of the enumerated count and of the unknown-count law
  (`n = b`, `+1` when `γ` is free) for every `b`.

## Scope of this negative, stated narrowly

Closed: **additive** two-tap propagating **plaintext** feedback, `1 ≤ a < b ≤ 19`, coefficients in
`{±1}²`, `γ` zero or free, three combiners, STD/KRY on both sides, forward and reverse.

`b ≥ 20` was excluded in advance as **WEAK / UNDECIDABLE** and is not reported as a survivor.

**This does NOT eliminate:** nonlinear two-input functions; multiplication or lookup-table
feedback; three or more taps; feedback composed with transposition; irregular tap schedules;
position-dependent functions; mixed plaintext/ciphertext taps; a key-index alphabet differing from
the plaintext alphabet (which makes the recursion non-linear); or state machines not expressible
as this recurrence.

K4 remains unsolved.
