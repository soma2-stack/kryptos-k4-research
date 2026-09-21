# Checkpoint W — residual multi-stage architecture map

**Starting HEAD:** `f1484c071d17e0d06262693b1456c5a777627d25`

**Verdict:** `NO EXP-040 JUSTIFIED`.

Full analysis: `docs/analysis/checkpoint-W-multistage-residual-map.md`.

## Why this checkpoint was needed

Checkpoint V upgraded the documentary evidence: Ed Scheidt directly described K4 as **more than one stage**, with a **masking technique** involved. That is genuine Layer-A evidence, so the project needed a dedicated audit of what multi-stage hand ciphers EXP-001…039 actually leave open.

## Main result: stage count is not the same as architectural novelty

Most naive multi-stage combinations collapse algebraically:

- fixed substitution + fixed substitution → one fixed substitution;
- any number of pure transpositions → one net permutation;
- fixed substitution commutes with a pure transposition;
- same-index additive/Vigenère-like masks combine into one effective shift schedule;
- Quagmire I–III and Gronsfeld reduce to already-covered shift families; standard Porta is closed by EXP-037.

Therefore the direct Scheidt statement does **not** reopen every classical cipher in stacked form.

The genuine residual must contain at least one non-collapsing component: a polygraphic/fractionating stage, masks on both sides of a transposition, a state-varying non-shift table, a stateful/external-source stage, or a custom full-26 fractionator.

## Ranked residuals

1. **Polygraphic/fractionating inner stage + outer position-varying mask.** This is the strongest structural residual. EXP-012’s own scope already says a 25-symbol inner system followed by a second layer that re-expands to 26 letters is not eliminated. Checkpoint V’s multi-stage evidence makes that opening more relevant, but no source names the inner transform or the outer mask, so it remains unbounded.
2. **Mask → transposition → mask.** A genuinely new normal form because the two masks are indexed on opposite sides of a non-commuting permutation. A period-8/period-10 subcase is mathematically attractive, but using the K1/K2 key lengths as K4 inheritance is not directly supported by any source.
3. **Periodic mask + net permutation outside EXP-036.** Technically open for some wider/double-transposition net permutations. The nine EXP-039 double-columnar permutations plus a periodic mask would be finite, but the double-columnar keyword choice is only structurally motivated, not documentary.
4. **Transposition + feedback/autokey/stateful mask.** Not globally covered, but no public evidence names feedback or recurrence and Checkpoint T is already hostile to low-memory autonomous state.
5. **Periodic/state-varying non-shift tables + transposition.** The class remains open, but the obvious named cases are duplicate/closed and a free table is underdetermined.
6. **Custom full-26 fractionation**, **external-source composites**, and **homophonic/variable mapping composites** remain logically open but are not bounded by current evidence.

## Important scope correction

A stand-alone impossibility does not always eliminate an **inner** stage hidden by a later mask. Examples:

- Playfair’s final-output invariants do not prove Playfair could never occur internally before a mask;
- EXP-012’s 25-symbol-output proof applies to the observed final output inventory, not to a 25-symbol inner layer followed by a 26-letter outer encoding;
- direct Hill/reflector/fractionation negatives do not automatically propagate through an unknown non-commuting outer stage.

This is **not** evidence for those named ciphers. It only fixes the scope of prior eliminations under the newly stronger multi-stage evidence.

## EXP-040 gate

The three nearest finite-looking candidates all fail the evidence gate:

- named inner fractionator + outer periodic mask: no source selects the fractionator;
- periods 8 and 10 around a transposition: no source says K4 inherits those K1/K2 periods/methods;
- nine EXP-039 double-columnar permutations + periodic mask: exact and finite, but compounds two structurally motivated choices without documentary support.

So the project still lacks a justified EXP-040.

## Next action

The highest-value documentary input remains the unedited Zetter/Scheidt material, because one sentence identifying the **base stage**, **mask stage**, or **stage order** could turn this residual map into a bounded experiment.

The highest-value cryptanalytic input remains Request 7: one additional public position-specific K4 plaintext letter, especially in positions `34–62` or `74–96`.

K4 remains unsolved.
