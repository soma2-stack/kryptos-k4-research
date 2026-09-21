# EXP-040 — propagating text-autokey with a short primer

**Branch:** `claude/dreamy-archimedes-79k6u0`. **Starting HEAD:** `653eeb8a7aad3662493b726490fa2ed76dde76c2`.
**Preregistration:** `docs/exp040-preregistration.md`, committed at `5ac21b6` **before** implementation.
**Code:** `experiments/exp040_propagating_autokey.py`. **Verifier:** `audit/verify_exp040.py`.

## Result

**2,592 configurations decided exactly. 0 FEASIBLE. 2,592 INFEASIBLE.**

Exhaustively negative at the registered scope, with no search: every configuration is settled by
an exact consistency decision, not by scoring.

## Why this was a legitimate EXP-040 rather than a rerun

EXP-008 tested data-dependent keys as **local affine taps** `k[i] = a·S[i−L] + b`. Its plaintext
source is `lambda j: (idx[P[j]] if j in P else None)` — it returns a value **only when the lagged
position is itself inside a crib**, so it never propagates, never derives unknown plaintext, and
never solves the recursion. It also capped the plaintext lag at 12 and skipped any system with
fewer than six rows.

A propagating autokey is a different object: a primer of `m` letters determines **all 97
plaintext letters** from the ciphertext, so the unknowns are the `m` primer letters and nothing
else. That is exactly the parameter-sharing property Checkpoint AC identified as the generator of
constraints, which is why this family is decidable where a local tap was not.

Against the ten-part gate: genuinely new; finitely defined (2,592 cases, zero search); falsifiable
by present evidence (23 down to 5 constraints for `m` = 1…24); not vacuous (proved empirically
below); motivated before the result; and small enough to verify three separate ways.

## Scope, exactly

| axis | values |
| --- | --- |
| source | plaintext autokey; ciphertext autokey (duplicate-check against EXP-008, not a novelty claim) |
| direction | forward `k[i] = S[i−m]`; reverse `k[i] = S[i+m]` with the primer at the tail |
| combiner | vigenere, beaufort, variant beaufort |
| plaintext / ciphertext alphabet | STD, KRY each |
| key-index alphabet | fed-back letter indexed in the plaintext alphabet, or in the ciphertext alphabet |
| primer length `m` | 1 … 24 |
| reset | none; plus physical-row reset at 4, 35, 66 with a fresh primer per row, for `m` ≤ 3 |

**`m` ≥ 25 was excluded in advance** and is reported as **UNDECIDABLE WITH PRESENT CRIB
GEOMETRY** (3, 1, 0, 0, 0 constraints at `m` = 25…29), never as survivors.

**All keyword primers are subsumed.** The decision enumerates every primer value per chain, which
is exactly all 26^m primers, so `KRYPTOS`, `PALIMPSEST`, `ABSCISSA` and every other keyword seed
is already covered. No follow-up keyword sweep is warranted.

## Controls — all three pass

1. **Positive.** A planted primer is recovered exactly from a synthetic autokey ciphertext.
2. **Adversarial.** A corruption that **straddles** two crib positions in one chain flips the
   verdict to infeasible.
3. **Non-vacuity — the decisive one.** An autokey message whose plaintext carries the **real
   cribs at the real positions** was planted and run through the actual decision procedure. It
   came back **FEASIBLE**, with a **unique** primer per chain and the **full 97-letter plaintext
   reconstructed identically**, on 17 constraints. **A true autokey K4 would have been detected**,
   so this negative is informative rather than empty.

## New structural fact: the autokey blind region

The first adversarial control failed, and the reason is a general property worth recording rather
than a bug.

> **A ciphertext change lying downstream of every crib position in its own chain is absorbed by
> the primer.** It is indistinguishable from a different primer value, so it cannot be detected.

Verified directly: corrupting index 91 leaves the verdict unchanged, while corrupting index 41 —
which straddles crib positions 31 and 66 in the same chain — flips it.

**Consequence.** A propagating autokey constrains only the span from each chain's seed through its
last crib position. The tail beyond the last crib carries **zero** constraint. This is the autokey
analogue of the period 27–29 blind spot and should be quoted whenever a feedback model is
proposed: a feedback family's power is bounded by crib **span**, not crib count.

## Independent verification

`audit/verify_exp040.py` imports neither the experiment nor `k4lib` and uses three different
methods. **All checks pass.**

- **Route A — encrypt direction.** The experiment decrypted; the verifier enumerates whole
  primers, builds a candidate plaintext, **re-encrypts** it with the forward rule, and demands K4
  come back. 438,672 whole primers over `m` = 1…3 across all conventions and key alphabets.
- **Route B — backward solve.** Instead of trying 26 primer values it inverts the recursion from
  the first pinned crib position back to the seed, then runs forward to test the rest. All
  `m` = 1…24.
- **Route C — structure.** Chains partition all 97 positions exactly for every
  `m`/direction/reset; the constraint budget is recomputed from scratch.

## What is now closed, stated narrowly

Propagating text-autokey — plaintext or ciphertext fed back, forward or reversed, with a primer of
1 to 24 letters, under the 12 committed conventions and both key-index alphabets, with or without
a physical-row reset at `m` ≤ 3 — is **exhaustively negative**.

This does **not** eliminate: two-tap or mixed feedback; feedback through a non-identity function;
feedback composed with a transposition; primers longer than 24; or any feedback family whose key
depends on more than one prior symbol. Those remain open, and the blind-region result above bounds
how testable any of them can be.

K4 remains unsolved.
