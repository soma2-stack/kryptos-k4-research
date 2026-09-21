# EXP-029 reproducibility status — prospective correction, 2026-09-21

EXP-029 is **not** to be presented as having the same artifact/verification status as EXP-030+.

## Historical result

The original restricted Weltzeituhr run reported 11,520 labelled alignments, zero exact 24/24
matches, best 7/24, and a positive control.

## Later audit defects

`docs/codex-audit.md` found that the original implementation/report:

1. used modulo-120 wrapping despite the stated intent to remain inside the known arc;
2. therefore duplicated labelled streams (the two reported 7/24 maxima were one stream under a
   rotation);
3. quoted a Poisson significance interpretation that was not calibrated for the duplicated,
   dependent family;
4. used a control whose offset wrapped;
5. did not commit the original EXP-029 raw log.

Those defects do **not** justify treating the old best-score/significance narrative as evidence.

## Durable scope

The later audit preserves only the narrower statement that the zero-hit result covers the
non-wrapping subset represented by the run. The broader Weltzeituhr hypothesis is not eliminated,
and direct clock-referent Layer-A motivation was later demoted independently.

## Reproducibility classification

- source code: present;
- original raw log: **missing**;
- compact `results/exp029/summary.json`: **missing**;
- dedicated independent verifier: **missing**;
- later corrective audit: present.

Therefore classify EXP-029 as:

> **HISTORICAL SCOPED NEGATIVE, PROSPECTIVELY REPAIRED BY AUDIT — not a modern independently
> reproducible checkpoint artifact.**

Do not regenerate it casually to manufacture a new historical log. If a future researcher needs
EXP-029 as a premise, first preregister a clean non-wrapping reproduction and commit its summary and
independent verifier as a new prospective repair.

K4 remains unsolved.
