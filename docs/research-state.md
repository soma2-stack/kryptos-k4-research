# Research state

## Provenance and confidence

This is an editorial reconstruction of the referenced ChatGPT conversation, not a laboratory notebook or an independent replication. Each statement is marked by its status:

- **Public fact** — supported by a link in `sources.md`.
- **Inherited result** — reported by the prior researcher; preserve it, but independently reproduce it before relying on it.
- **Hypothesis** — a bounded, falsifiable idea, not evidence of a solution.

## High-priority inherited program: `TOKIO → 57973`

**Inherited result.** A substantial prior July 2026 handoff reportedly converged on the following chain:

`W positions → 20, 15, 11, 9, 15 → TOKIO → physical 57973`

That handoff reportedly defined 942 canonical route cases and found 935 broader double-route cases that did not reach complete language closure. The immediate task is **not** to expand the search. First recover or reconstruct:

- the exact definition of every route family;
- the source of `57973` and its physical interpretation;
- the canonical enumeration order and reported hash;
- the 7 completed/negative cases and the 935 unfinished cases;
- the plaintext scoring and crib gate.

Until those records are recovered, treat the counts as an inherited lead, not an independently verified result.

## `4 × 22` World Clock / TOKIO construction

**Hypothesis; many obvious variants tested negatively.** Removing `OBKR` and the five `W` characters from K4 produces 88 letters, i.e. a `4 × 22` array. The five pre-terminal W-run lengths were recorded as `20, 15, 11, 9, 15`, spelling `TOKIO` under A1Z26; the final run is 22.

The inherited analysis constructed the historically relevant UTC+9 city tape:

`JAKUTSKPJOENGJANGTOKIO` (22 normalized letters)

and proposed:

`OBKR` indicator → W counts identify TOKIO → 22 specifies the clock tape → 88-character body in a 4 × 22 array → tape controls a bespoke lookup.

The 22-length coincidence is interesting, but ordinary transpositions and simple keyed operations did not work. The only remaining version worth testing is a small, pre-declared lookup rule `P = f(C, clock letter, row, column)`, with strict parameter bounds and an out-of-sample rule.

## Other retained leads

### Physical tableau parity / two-chart model

**Inherited result.** On a reconstruction of physically opposed tableau letters, ordinary A=0 parity reportedly separated every one of ten known same-cipher/different-plain crib conflicts. A two-chart **homophonic** interpretation had no contradictions at the crib positions and produced 49 observed `(chart, ciphertext)` symbols of 52 possible.

This is a selector clue, not a chart construction. Simple Caesar, affine, Atbash, rotated Kryptos-alphabet, and direct numeric-mask versions failed. Do not use unconstrained language optimization to fill the charts.

### K0 Morse as binary selector

**Inherited result.** A reversed, phase-shifted dot/dash stream from the physically visible “T IS YOUR POSITION” reading reportedly satisfied the same ten A/B selector constraints. Obvious two-transform (Baudot/Vigenère/tableau) follow-ons failed, and multiple phases were searched, so the match is not dispositive.

### Kryptos alphabet rail alternation

**Inherited observation.** Split the Kryptos alphabet into alternating rails:

```text
rail 0: K Y T S B D F H J M Q V X
rail 1: R P O A C E G I L N U W Z
```

At known crib positions, repeated plaintext-letter occurrences were reported to map to opposite ciphertext rails in 7/7 transitions. The inherited work found no simple relationship to opposite-tableau parity, position parity, or 7×14/31-column geometry. This is an anomaly to test prospectively, not a cipher key.

### `DIAWINFBN` +5 run

**Inherited observation.** The substring `DIAWINFBN` exhibits five consecutive relations `C[i+4] = C[i] + 5 (mod 26)`. Its previously reported post-hoc adjusted significance was approximately 0.00156. No cryptanalytic consequence has yet been derived, so treat it as low-priority until a mechanism predicts it.
