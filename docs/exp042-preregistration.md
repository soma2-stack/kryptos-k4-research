# Preregistration — EXP-042: mixed plaintext/ciphertext two-tap propagating feedback

**Branch:** `claude/dreamy-archimedes-79k6u0`. **Written before implementation.**
**Starting HEAD:** `763336f007ee9cabfbb4feeda9dd8097c9034eab`.

## 1. Phase 1 — the exact recurrence, derived before anything was proposed

`k[i] = α·P[i−a] + β·C[i−b] + γ`, with `C[i] = combine(P[i], k[i])`.

Substituting the encryption relation (shown for vigenere; the other two combiners give the same
shape with sign changes):

```
k[i] = α·(C[i−a] − k[i−a]) + β·C[i−b] + γ
k[i] + α·k[i−a] = α·C[i−a] + β·C[i−b] + γ
```

> **The structural fact that governs everything below.** The ciphertext is fully known, so
> `β·C[i−b]` is a **known driving term**. It contributes **nothing** to the recursive structure.
> The recurrence is **first order in `k`, with lag `a` — the plaintext tap alone.**

Consequences, all verified computationally before this file was written:

- **Unknowns = `a`**, not `b` and not `gcd(a,b)`. Confirmed for every tested `(a,b)`.
- The dependency graph decomposes into **chains mod `a`**, exactly as in EXP-040.
- **The constraint budget is therefore identical to EXP-040's table**: `24 − (chains occupied by
  crib positions)`, running 23 down to 5 across `a` = 1…24. The C tap adds **zero** constraints.

## 2. Phase 1 — reduction tests, proven not assumed

| # | Question | Answer |
| --- | --- | --- |
| R1 | Are the two orientations `α·P[i−a] + β·C[i−b]` and `α·C[i−a] + β·P[i−b]` distinct? | **No.** With the lags exchanged the two produce **byte-identical linear systems in 126 of 126** tested cases. They are the same family reparameterised. **Only one orientation is enumerated.** |
| R2 | Does `β = 0` reduce to EXP-040? | **Yes, exactly** — with `β = 0` the C lag becomes irrelevant (`b = 3` and `b = 11` give identical systems). **`β ≠ 0` is required.** |
| R3 | Does it reduce to EXP-041? | **No.** EXP-041 is second order in the plaintext recursion; this is first order in `k` with a known driving term. |
| R4 | Does it reduce to EXP-008? | **No.** EXP-008's two-tap family used only known ciphertext and does not propagate; here the plaintext tap propagates. |
| R5 | Does it reduce to EXP-038? | **No.** EXP-038 registered an autonomous affine recurrence with no driving term. |

**Verdict: genuinely new, subject to `β ≠ 0` and a single orientation.**

## 3. Phase 2 — crib-span screen

The crib-span law is applied before implementation. Components are the chains mod `a`; a chain
constrains its unknown only when it contains **two or more** crib positions. Positions downstream
of every crib in a chain are **blind** and absorbed by the warm-up.

Budget by `a` (chains occupied / independent constraints):

```
a:      1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
constr:23 22 21 20 19 18 17 16 15 14 13 12 11 11  9  8  7  7  9 11 11  9  7  5
```

**No `a` in 1…24 is vacuous**, so no lag pair is excluded on that ground.

The two crib intervals `[21,34)` and `[63,74)` couple through a chain exactly when their positions
share a residue mod `a` — the same coupling that drove EXP-040. The C tap never creates a new
coupling, because it is a known offset.

## 4. Phase 3 — information value, computed in advance

- **Raw configurations: 110,592** = `a`(24) × `b`(24) × `α`(2) × `β`(2) × `γ`(2) × combiner(3) ×
  plaintext alphabet(2) × ciphertext alphabet(2) × direction(2), single orientation.
- **Worst single-configuration chance: 8.417 × 10⁻⁸.**
- **Expected accidental survivors over the whole range: 3.970 × 10⁻⁴.**

For comparison: EXP-040 expected `2.0 × 10⁻⁵`, EXP-041 expected `2.2 × 10⁻³`. This sits between
them, so **no cap on `a` is required** and the family is not elevated merely because it computes.

**Honest caveat, recorded before the result.** The C tap multiplies the hypothesis count roughly
24-fold while adding **no** constraints, so a survivor here would be **less surprising** than one
in EXP-040 at the same constraint density. And the documentary motivation is **weaker** than
EXP-040's: autokey is a classical hand method with a historic basis, whereas mixing a plaintext
tap with a ciphertext tap is a synthetic construction that **no source names**. This family clears
the seven technical gate conditions; it does not gain documentary standing by doing so.

## 5. Declared scope, frozen now

| axis | values |
| --- | --- |
| plaintext-tap lag `a` | 1 … 24 |
| ciphertext-tap lag `b` | 1 … 24 (`b = 0` excluded: it makes encryption self-referential) |
| `α` | `{1, −1}` |
| `β` | `{1, −1}` — **`β = 0` excluded**, it is EXP-040 |
| `γ` | `0`, or free |
| combiner | vigenere, beaufort, variant beaufort |
| plaintext / ciphertext alphabet | STD, KRY each |
| direction | forward, reverse |
| orientation | **one only** — the swap is proven identical (R1) |

**Excluded in advance:** nonlinear or lookup-table feedback; three or more taps; transposition;
row reset; a key-index alphabet differing from the plaintext alphabet; any `β` outside `{±1}`.

## 6. Decision rule

**FEASIBLE** iff the linear system is solvable over Z26, decided exactly by CRT through GF(2) and
GF(13). No scoring, no threshold, no language model. Any FEASIBLE configuration must then rebuild
all 97 plaintext letters and match every crib before being reported as more than a linear survivor.

## 7. Controls

1. **Positive.** A synthetic mixed-feedback instance whose plaintext carries the **real cribs at
   the real K4 positions**; the procedure must accept it and recover the warm-up state where
   uniqueness is theoretically expected.
2. **Contradiction.** Corrupt a position inside a constrained chain; the system must become
   infeasible.
3. **Blind-region.** Modify a position the theory predicts is absorbed; the solver must correctly
   **remain feasible**. This is expected behaviour, not a defect.

## 8. Verification

Infeasibility **certificates**: a vector `w` with `w·M ≡ 0` and `w·rhs ≢ 0` mod 2 or 13, checkable
by plain arithmetic without trusting any solver. A second route must not import the experiment.

## 9. Stop condition, agreed in advance

If EXP-042 is negative, the simple feedback corridor is declared **provisionally exhausted**. There
will be **no** escalation to three taps, four taps, arbitrary nonlinear `f`, 26×26 feedback tables,
or arbitrary state machines — those add flexibility without new evidence. Work returns to the
wider architecture frontier.

## 10. Scope of any negative

A negative would not eliminate nonlinear mixed feedback, more than two taps, mixed feedback
composed with transposition, irregular tap schedules, position-dependent coefficients, or state
machines not expressible as this recurrence.
