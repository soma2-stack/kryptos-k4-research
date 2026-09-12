# Canonical current status — read this first

This file is a navigation aid for future research sessions. It does **not** replace or rewrite historical checkpoints. Older files such as `docs/next-steps.md` and the opening banners in `README.md` / `docs/research-state.md` contain historical snapshots and can be stale at the top.

**Current research checkpoint:** Checkpoint Q (`results/2026-09-12-claude-checkpoint-Q.md`).

**Current branch state when this handoff was refreshed:** `claude/k4-post-j` at `d69102d828f79599a8ade42a997396539d33760b`.

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
- EXP-032 through EXP-038 artifacts are committed and reproducible from clean checkout.
- EXP-036 remains only a scoped negative for the declared periodic shift-family + transposition space; it does not eliminate all periodic polyalphabetic ciphers.
- EXP-037 eliminates the declared standard Porta family at its exact scope.
- Quagmire I–III and Gronsfeld reduce to already-covered families; Quagmire IV requires an unsupported second alphabet.
- Standard CM Bifid reduces to EXP-012; standard Fractionated Morse is closed as above; named classical fractionation is substantially narrowed, not globally eliminated.
- Direct Gromark was rejected structurally before primer search because legal key digits 0–9 cannot realise enough public crib pairs under the evidenced component-alphabet treatments.
- **EXP-038 (Checkpoint Q) closed the full-Z26 second-order affine recursive-key family**: F1 and F2 were preregistered together; 11,881,376 raw F2 tuples collapse to 7,585,006 unique 97-key streams and 4,481,750 distinct crib projections; 1,701,518 streams are already covered by period ≤23; 5,883,488 streams are genuinely new. The preregistered null expected about `5.91e-27` survivors across the 12 convention targets. Result: **zero feasible**, with neither crib block satisfiable on its own. Independent direct-iteration verification was exhaustive. Read this narrowly — it is *not* an elimination of recursive or stateful keys in general.
- Direct World Clock city-letter models have multiple bounded negatives; do not rescue them by adding post-hoc parameters.
- The physical same-column-above-K4 model is parked because a common horizontal lattice is not established.

## Do not rerun

Do not rerun EXP-029 through EXP-038 merely for reassurance. Their exact scope, controls, and verifier status are already recorded.

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

**Monoalphabetic substitution composed with DOUBLE transposition, both keys drawn from a precommitted list of published Kryptos keywords** (`KRYPTOS`, `PALIMPSEST`, `ABSCISSA`).

Motivated rather than speculative: K3 is a transposition Sanborn implemented himself and those keywords are demonstrably his. Not duplicate: EXP-033 and EXP-036 each composed their substitution with a **single** transposition from a declared family, and a product of two columnar transpositions can lie outside both. Decidable: use EXP-033's exact consistency test for an arbitrary fixed monoalphabetic substitution after composing the two permutations. Keep the family small and precommitted; do not pad it with unevidenced words merely to enlarge the search.

Important algebraic simplification: a fixed monoalphabetic substitution commutes with a pure transposition, so `S ∘ T2 ∘ T1` and `T2 ∘ T1 ∘ S` are the same model up to writing the same permutation in the opposite convention. Do not count substitution/transposition order as a separate free parameter.

Before assigning a new experiment number, freeze the exact columnar-transposition convention, repeated-letter tie rule, padding/no-padding rule, orientation, and whether each pass is encryption-direction or inverse-direction. Deduplicate identical composed permutations. Then compute the exact family size and chance survival before running.

Do **not** extend EXP-038 from order 2 to order 3 without independent motivation — that is the rescue pattern this programme rejects. See Checkpoint Q §9 for the full setup.

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
