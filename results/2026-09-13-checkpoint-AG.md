# Checkpoint AG result — evidence-to-census reconciliation

**Date:** 2026-09-13

**Starting HEAD:** `e8be9e7d45db994bad6c150dd5b8f1c75bfefdf7`

**Experiment:** none

## Result

**NO EXP-040 JUSTIFIED. K4 remains UNSOLVED.**

The complete admitted Sanborn/Scheidt documentary record was reconciled against Checkpoint AE.
No overlooked operational parameter was found. The record supplies strong class-level facts
(multi-stage, masking by effect, historical grounding, possible Sanborn modification) but no
named transform, stage order, period/key length, reset/alignment rule, tableau, recurrence, or
parameter-reuse rule.

Quantitative near-candidates remain exactly where AE placed them:

- class H with unsupported inherited periods 8/10: 18 mask values, 17 effective after gauge,
  and at least 7 crib constraints for a fixed intervening permutation;
- row-constant additive mask: 3 values and 21 constraints, but the documentary record establishes
  physical rows, not key constancy or reset;
- B/G at periods 24/25/26: 5/3/1 constraints; periods 27/28/29: zero;
- class L arbitrary 26×26 table at periods 8/10/13/26: zero repeated inputs and zero constraints;
- class J Trifid residual: 45–48 free ternary classes against 24 crib equations; the 15 SAT
  configurations remain conditionally compatible and are not candidates.

The canonical present-status section was corrected prospectively for the `ScheidtNova.doc`,
GBH/AAPB, UGA/Peabody, PBS attribution, unedited Zetter material, and pending-outreach states.
Historical checkpoint documents were not rewritten.

**One next action:** recover and authenticate the original `ScheidtNova.doc` binary and audit
its verbatim Scheidt answers for a reusable Layer-A parameter. Do not send duplicate outreach.

Full audit: `docs/analysis/checkpoint-AG-evidence-to-census-reconciliation.md`.
