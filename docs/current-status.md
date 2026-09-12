# Canonical current status — read this first

This file is a navigation aid for future research sessions. It does **not** replace or rewrite historical checkpoints. Older files such as `docs/next-steps.md` and the opening banners in `README.md` / `docs/research-state.md` contain historical snapshots and can be stale at the top.

**Current research checkpoint:** Checkpoint P (`results/2026-09-12-claude-checkpoint-P.md`).

**Parent branch state when this handoff was created:** `claude/k4-post-j` at `81d928dce9569d5afc8b1fc061f2e279856e8063`.

**K4 remains unsolved.**

## Public crib constraints — verified

Use these as local plaintext/ciphertext positional anchors:

- zero-based `[21,34)` = `EASTNORTHEAST`, ciphertext `FLRVQQPRNGKSS`
- zero-based `[63,74)` = `BERLINCLOCK`, ciphertext `NYPVTTMZFPK`

Evidence grades are intentionally distinct:

- `BERLIN` one-based 64–69: strong contemporaneous position-specific reporting
- `CLOCK` one-based 70–74: strong contemporaneous position-specific reporting
- `NORTHEAST` one-based 26–34: strong position-specific reporting plus direct Sanborn confirmation of the word
- `EAST` one-based 22–25: B+, inferred from reporter-confirmed placement immediately before NORTHEAST

See `docs/external/checkpoint-O-public-crib-primary-verification.md` and Checkpoint P.

## Current consequences

- Standard Fractionated Morse is structurally incompatible with the **published K4 positional crib semantics**. Do not generalise this to all Morse-derived systems, all fractionation, or every non-position-preserving cipher.
- Reflector-machine and Playfair eliminations are restored to **PROVED IMPOSSIBLE within the monographic, position-preserving class**, because their rejecting witnesses lie in directly numbered public spans.
- EXP-032 through EXP-037 artifacts are committed and the verifier suite was repaired for clean-checkout reproducibility.
- EXP-036 remains only a scoped negative for the declared periodic shift-family + transposition space; it does not eliminate all periodic polyalphabetic ciphers.
- EXP-037 eliminates the declared standard Porta family at its exact scope.
- Quagmire I–III and Gronsfeld reduce to already-covered families; Quagmire IV requires an unsupported second alphabet.
- Standard CM Bifid reduces to EXP-012; standard Fractionated Morse is closed as above; named classical fractionation is substantially narrowed, not globally eliminated.
- Direct Gromark was rejected structurally before primer search because legal key digits 0–9 cannot realise enough public crib pairs under the evidenced component-alphabet treatments. No EXP-038 exists.
- Direct World Clock city-letter models have multiple bounded negatives; do not rescue them by adding post-hoc parameters.
- The physical same-column-above-K4 model is parked because a common horizontal lattice is not established.

## Do not rerun

Do not rerun EXP-029 through EXP-037 merely for reassurance. Their exact scope, controls, and verifier status are already recorded.

In particular, do not restart old claims that were retracted:

- CET = 97 letters
- ATHEN absent from UTC+2
- upper band = north / lower band = south
- membership implies physical order
- EXP-029 significance from the wrapped/duplicate implementation
- isolated physical `OBKR` row
- uniform 31-character rows across the cipher panel
- the Checkpoint-L mixed-alphabet frontier
- the Checkpoint-M claim that all experiments share the same three shift combiners

## One recommended next cryptanalytic direction

**Stateful recursive key schedules**, with state evolving from prior key values, over a **small precommitted recurrence family**.

Before assigning a new EXP number:

1. Define each recurrence algebraically.
2. Prove it is not already covered by EXP-006, EXP-008, EXP-034, or EXP-036.
3. Exclude any recurrence whose relevant orbit is eventually periodic with period ≤ 23 if that makes it a subset of EXP-036.
4. Compute the seed-space size and the number of distinct projections onto the 24 verified crib positions **before implementation**.
5. Derive the expected chance-survivor count from the declared family itself.
6. If the crib constraints do not beat the seed space, do not run the family.
7. Prefer existential consistency over brute-force key enumeration where possible.
8. Require planted-positive and adversarial controls that actually intersect active constraints.
9. Require an independent verifier that reimplements the recurrence rather than importing production code.
10. Keep the conclusion model-limited.

This direction is **STRUCTURALLY-MOTIVATED, not documentary**. There is no Sanborn/Scheidt statement naming such a system.

## External evidence

Fulfilled:

- official cipher-side rows 1–24 / Request 1
- K1/K2 physical-character count issue / Request 5
- public crib positions / Request 6

Still open but nonblocking:

- Request 4: Jim Sanborn papers, Archives of American Art, Series 3, Box 6, Folder 10, `Pre-Production and Notes, 1990–1999`, for actual cipher-panel fabrication geometry / row alignment / punch-layout evidence

Lower-priority historical evidence requests remain documented in `docs/external-evidence-requests.md`.

## Contamination protocol

Do not access or use alleged full K4 plaintext, purported solution dumps, leaked solution material, private K5 plaintext, or private K5 ciphertext.

Allowed material remains public K4 ciphertext, public Sanborn clues, public documentary sources, and the repository's existing uncontaminated experiment corpus.

Do not claim K4 solved unless there is one complete deterministic 97-character decryption procedure with fixed parameters that explains all public constraints and reproduces independently.
