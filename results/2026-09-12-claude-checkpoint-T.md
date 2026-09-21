# Checkpoint T — constraint-first architecture search

**Starting HEAD:** `8d9c9e4867e52a7d19afaafa0645b7b1865b3168` (branch `claude/k4-post-j`, clean tree).

**Verdict: `NO EXP-040 JUSTIFIED`.**

Full analysis: `docs/analysis/checkpoint-T-constraint-first-architecture-search.md`.
Independent verifier: `audit/verify_checkpoint_T.py` — 16/16 checks pass, imports no
project code, rebuilds K4 from `data/cipher_side_rows.json`.

## What was done

A constraint-first pass: structural requirements were derived from the 24 verified
plaintext/ciphertext pairs, the authoritative row structure and the admitted documentary
record, *before* any architecture was named. No named cipher was selected merely because it
was untested, and no experiment was manufactured to keep testing.

## Three durable findings

**T-1 — Pure transposition of K4 is PROVED IMPOSSIBLE.** *(new)*
The cribs place `E` at positions 21, 30 and 64, so the plaintext holds at least three `E`s;
the ciphertext holds exactly two. A permutation preserves the letter multiset, so the two
cannot be reconciled. This is a deterministic contradiction requiring no search, no null and
no language model. It **upgrades** EXP-007's index-of-coincidence result, graded
*STRONGLY DISFAVORED, not proved*, to **PROVED IMPOSSIBLE** — the grade Playfair and the
reflector machines already hold. Scope: transposition of the K4 message alone; it does not
reach substitution-then-transposition, nor a transposition spanning K1–K4 jointly.

**T-2 — The crib set has a structural blind spot at periods 27, 28 and 29.** *(new)*
Constraint counts run 22, 21, 20 … 5, 3, 1 for periods 2…26 and then hit **zero** at 27–29
before recovering. The cribs are contiguous runs of 13 and 11; within-crib differences never
exceed 12 and cross-crib differences lie in [30, 52], which 27, 28 and 29 fail to divide.
Any "consistent period" reported there is **vacuous** and must never be counted as a
survivor. This is an information-theoretic ceiling, not a gap in effort — EXP-036 capped at
period 23 under a minimum-constraint rule and was right to do so.

**T-3 — Constraint density, not compute, is the binding resource.**
Across eleven row-structured models × 12 conventions × periods 2–40, survivors appeared
*only* where the constraint count collapsed, and in exactly the numbers chance predicts:
12 survivors at periods 27–29 (0 constraints), and 12 survivors for the row-offset model at
n=26 against a null expectation of exactly 12.0. Nothing survived anywhere the data can
speak.

## Row-reset audit (Part 3)

Only real row boundaries were used — message indices 4, 35, 66. Eleven models were swept:
every-row reset, single resets at 35 and at 66, both, boustrophedon traversal in two phases,
row-number additive offsets in message and row-local indexing. **All negative.**

The family is meaningfully rejectable because `BERLINCLOCK` straddles the row 27/28 boundary
(`BER | LINCLOCK`) while `EASTNORTHEAST` reaches row-local indices 28 and 29. Row-local
indexing therefore forces `k(32) = k(63)` and `k(33) = k(64)`; all 12 conventions fail both.

**This is a replication, not a discovery.** EXP-020 preregistered exactly this prediction,
computed the same 26⁻² null and reported 0 of 12. It was reached here from an independent
starting point. EXP-020's geometry also survives the geometry correction intact — the
withdrawn "uniform 31 columns" claim concerned rows 1–24, not the K4 split.

**EXP-038's row-reset variant is rejected, not tested.** Re-seeding at row boundaries adds
6 free Z26 values while removing the cross-row constraints that gave EXP-038 its force;
row 27 would contribute 3 constrained positions against 2 fresh seeds. Technically untested,
but without evidence or power.

## Method change inside K4 (Part 4)

Scheidt's statement concerns K1→K4, not K4's interior. The complete list of independently
established internal boundaries is **{4, 35, 66}**, and all three are already covered — one
searched reset (EXP-006, EXP-015), three fixed resets (EXP-020), and single resets at 35 and
66 here. Arbitrary split positions are excluded by the brief and by gate conditions 1 and 3.

## "Historic basis" filter (Part 5)

Used as a filter, never as a cipher name. It rejects software keystreams, machine-dependent
constructions, keys beyond the EXP-019 unicity bound of ~66–76 letters, and hand-unreliable
high-order recurrences. It is **not constructive**: the classical hand-cipher catalogue it
points at is precisely the catalogue EXP-001…039 has already exhausted.

## Gate outcome (Part 6)

Ten candidates were assessed against all eight conditions. Every one fails at least one —
most commonly condition 5 (already covered) or conditions 3 and 4 (unbounded, or no
constraint power). Nothing passes. No EXP-040 was created.

## What information is still missing

1. **A third verified crib, or any verified plaintext letter in positions 34–62 or 74–96.**
   Now the single highest-value input in the project — it would close the 27–29 blind spot
   and restore power to long-period, per-row and reset-at-boundary models. It **outranks
   further cryptanalysis**.
2. The unedited 2005 Zetter/Scheidt interview material (Request 2) — primary documentary
   target, unchanged.
3. The original/full 1991 ABC Scheidt interview audio/video — secondary.

The frontier is no longer a missing experiment. It is a **missing constraint**.

## ONE next action

**Open a new external evidence request for additional verified K4 plaintext** — any
publicly attributable Sanborn statement or contemporaneous report fixing a plaintext letter
outside the two known cribs — and keep Request 2 as the primary documentary target.

Do not start another speculative cryptanalytic family.

K4 remains unsolved.
