# Checkpoint AL — intended-human-solver / low-description-length census

Date: 2026-09-13  
Branch: `codex/k4-continuation`  
Starting HEAD: `8fb9f3e94085e343f7fb90b17eb4e41e2ce7ed66`

## Decision

**NO EXP-040 JUSTIFIED. K4 remains UNSOLVED.**

This prospective audit ranks only the genuinely open parts of Checkpoint AE. It uses the public
K4 artifact, K1–K3 lessons, the 97-character ciphertext, and the 24 fixed crib positions as its
information base. Checkpoints AH–AK add or correct artifact measurements but select no cipher
operation, period, alignment, recurrence, permutation, or reset rule.

Scores are qualitative and comparative. Description complexity counts independent choices,
not implementation effort. Crib density asks whether shared parameters create actual consistency
conditions, not whether a model can reproduce 24 observations.

## Open-class census

| Genuinely open class | Description complexity | Human discoverability | Crib constraint density | Puzzle-selected parameters | Meaningful falsification possible | Arbitrariness assessment / action |
|---|---|---|---|---|---|---|
| B/G: declared standard periodic mask families at `p=24..26`, direct or with a predeclared transposition | LOW | HIGH for the general repeating-key idea; LOW for these periods | LOW: exactly 5 / 3 / 1 constraints | NO | PARTIAL | Smallest description, but periods are chosen only because shorter scopes failed. Retain as the best *conditional* candidate; do not test. |
| B/G: the same families at `p=27..29` | LOW | LOW | LOW: exactly 0 / 0 / 0 constraints | NO | NO | Practically vacuous under current crib geometry; eliminate from experiment consideration until another positional crib exists. |
| H: two short periodic masks separated by a fixed permutation | HIGH | MEDIUM for composing prior operations; LOW for the exact pipeline | MEDIUM once fixed: at least 7 cycle constraints at `(8,10)`, 15–19 at short periods | PARTIAL: K1/K2 expose periods 10/8 and K3 exposes transposition, but do not instruct inheritance, order, or `π` | YES, for one frozen tuple | Technically falsifiable but highly post-hoc unless the puzzle first selects both periods and a finite permutation family. |
| E: a specifically declared low-state deterministic recurrence outside EXP-038 | MEDIUM | MEDIUM | MEDIUM only after the recurrence and seed domain are frozen | NO | YES, for one frozen recurrence family | A short recurrence could be human-solvable, but no public feature selects one; the generic class becomes an arbitrary lookup. |
| J: structured fractionation/polygraphy with one shared grid/cube and fixed readout | HIGH | MEDIUM for the historical concept; LOW for the exact configuration | LOW: the known Trifid residuals retain 45–48 free ternary classes against 24 letters | NO | PARTIAL | The architecture can be finite, but family, grid, period, reset, and readout are not selected. The 15 conditionally-SAT configurations are compatibility results, not candidates. |
| M: length-changing or non-position-preserving encoding with deterministic alignment | HIGH | LOW | LOW/UNKNOWN until alignment is supplied | NO | PARTIAL | Open in principle, incomplete as a hypothesis. Eliminate from experiment consideration until the artifact supplies the position mapping. |

## Technically open but practically vacuous

Arbitrary position functions, recurrences, permutations, 26×26 combiners, source lookups without
crib-position repeats, free polygraphic maps, and free inner/outer masks are omitted from the
ranking. Their freedom scales with the observations or destroys position correspondence, so a
fit is not evidence and a failure of one arbitrary choice eliminates nothing. Likewise, the
unsupported `HILL` reading and the textual `4/31/31/31` convention supply no physical rule.

## Public lessons and their limit

K1–K3 make four solver habits legitimately discoverable: use the visible KRY alphabet, expect
reused periodic parameters, preserve exact text, and consider transposition as well as
substitution. Those lessons are already represented in prior tests. They do **not** uniquely say
“inherit 8 and 10,” “compose every earlier operation,” choose a permutation, or select a new
recurrence. AK's verified physical `?OBKR` row ending corrects layout but supplies no operation.

## Top three

1. **Declared periodic mask families at `p=24..26`.** Lowest description length and familiar to
   a human solver, with 5/3/1 real constraints, but no artifact-derived reason for those periods.
2. **Two short masks around a fixed permutation.** It has useful cycle constraints after every
   parameter is frozen, but K1/K2/K3 analogy does not select the inheritance rule or permutation.
3. **A specific low-state recurrence.** Potentially concise and falsifiable, but presently only
   a template: no public feature chooses its equation or seed domain.

The single best conditional candidate is **B/G at `p=24..26`**, solely because it adds the least
description beyond an already public solver model. It still fails the puzzle-selection gate.

## EXP-040 gate

No candidate simultaneously has a fixed rule, a puzzle-selected small parameter domain,
independent crib constraints, and a meaningful negative. Therefore no EXP-040 preregistration
or execution is warranted. Checkpoint AE is unchanged.

## Exactly one next action

Obtain **one independently authenticated positional plaintext letter at one of indices
1, 3, 91, 93, 95, or 96**. Any one supplies constraints at all three blind periods 27–29 and at
34 of the 39 periods 2–40, increasing information without choosing a mechanism post hoc.
