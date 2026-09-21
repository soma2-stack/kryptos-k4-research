# EXP-042 — mixed plaintext/ciphertext two-tap propagating feedback

**Branch:** `claude/dreamy-archimedes-79k6u0`. **Starting HEAD:** `763336f`.
**Preregistration:** `docs/exp042-preregistration.md`, committed at `1fe7673` **before** implementation.
**Code:** `experiments/exp042_mixed_feedback.py`. **Verifier:** `audit/verify_exp042.py`.

## Result

**110,592 raw configurations, 68,972 distinct tests, 0 FEASIBLE.** Exhaustively negative at the
registered scope, decided by exact linear algebra over Z26 — no search, no scoring.

## Phase 1 — the screen that shaped everything

`k[i] = α·P[i−a] + β·C[i−b] + γ`. Substituting the encryption relation gives

```
k[i] + α·k[i−a] = α·C[i−a] + β·C[i−b] + γ
```

> **The ciphertext is fully known, so `β·C[i−b]` is a known driving term. It contributes nothing
> to the recursive structure.** The recurrence is **first order in `k` with lag `a`** — the
> plaintext tap alone.

Verified consequences: unknowns = `a` (not `b`, not `gcd(a,b)`); components are chains mod `a`;
**the constraint budget is identical to EXP-040's**, and the ciphertext tap adds **zero**
constraints.

## Phase 1 — reductions proven, not assumed

The brief asked for proof rather than assumption on the orientation question. Both directions
were built independently and compared:

- **The two orientations are the same family.** `α·P[i−a] + β·C[i−b]` with lags exchanged is
  **byte-identical** to `α·C[i−a] + β·P[i−b]` in **126/126** cases in the experiment and
  **336/336** in the independently written verifier. Only one orientation is enumerated.
- **`β = 0` is exactly EXP-040** — with `β = 0` the ciphertext lag becomes irrelevant (`b = 3`
  and `b = 11` give identical systems). `β ≠ 0` is required.
- Not EXP-041 (that is second order), not EXP-008 (that does not propagate), not EXP-038 (that is
  autonomous).

## Phase 3 — information value, computed in advance

Worst single-configuration chance `8.417 × 10⁻⁸`; **expected accidental survivors
`3.970 × 10⁻⁴`** — between EXP-040 (`2.0 × 10⁻⁵`) and EXP-041 (`2.2 × 10⁻³`), so no cap on `a`
was needed.

**Caveat recorded before the result, and it still stands:** the ciphertext tap multiplies the
hypothesis count ~24-fold while adding no constraints, so a survivor here would have been **less
surprising** than one in EXP-040. And the documentary motivation is **weaker**: autokey is a
classical hand method with a historic basis, whereas mixing a plaintext and a ciphertext tap is a
synthetic construction **no source names**. Clearing the technical gate gave this family no
documentary standing.

## Controls — all three pass

1. **Positive.** A planted `a=5, b=3` instance whose plaintext carries the **real cribs at the
   real positions** was accepted with exactly **one** solution and the full 97-letter plaintext
   rebuilt identically.
2. **Contradiction.** Corrupting index 26, inside a constrained chain, **rejects**.
3. **Blind-region.** Corrupting index 95, downstream of every crib in its chain, is **absorbed** —
   the expected behaviour under the crib-span law, now confirmed in a **third** feedback family.

## Independent verification

`audit/verify_exp042.py` imports neither the experiment nor `k4lib`. **All checks pass.**

- **Route A — certificates of infeasibility, full coverage.** Every one of the **110,592**
  configurations yields a witness `w` with `w·M ≡ 0` and `w·rhs ≢ 0` mod 2 or 13 — a
  self-contained proof checkable by plain arithmetic, with no solver trusted.
- **Route B — brute force, encrypt direction, no linear algebra.** 404,352 warm-ups for `a = 1`
  and `a = 2`, run forward and **re-encrypted**, demanding K4 return and the cribs match.
- **Route C — structural claims re-derived**: the unknown count is the plaintext-tap lag
  independent of the ciphertext lag; the orientation swap is identical; `β = 0` is EXP-040.

## Scope of this negative, stated narrowly

Closed: mixed **additive** two-tap propagating feedback, `a, b ∈ 1…24`, `α, β ∈ {±1}` with
`β ≠ 0`, `γ` zero or free, three combiners, STD/KRY on both sides, forward and reverse, one
orientation (the other proven identical).

**Does not eliminate:** nonlinear mixed feedback; more than two taps; mixed feedback composed with
transposition; irregular tap schedules; position-dependent coefficients; `β` outside `{±1}`; a
key-index alphabet differing from the plaintext alphabet; or state machines not expressible as
this recurrence.

## Stop condition invoked

Per the preregistration, the **simple feedback corridor is now declared provisionally exhausted**.
There is no escalation to three taps, four taps, arbitrary nonlinear `f`, 26×26 feedback tables or
arbitrary state machines — those add flexibility without new evidence. Work returns to the wider
architecture frontier, in `results/2026-09-21-frontier-after-feedback-corridor.md`.

K4 remains unsolved.
