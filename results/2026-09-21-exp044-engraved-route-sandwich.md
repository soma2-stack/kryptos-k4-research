# EXP-044 — engraved-geometry route inside two periodic masks

**Branch:** `claude/dreamy-archimedes-79k6u0` · **Date:** 2026-09-21
**Preregistration:** `docs/exp044-preregistration.md`, committed at `4d47440` **before** implementation.

## Result

**14,400 configurations decided exactly. 0 FEASIBLE.**

All four predeclared controls pass. Independently verified by
`audit/verify_exp044.py`, which imports nothing from the experiment.

## Why this family existed at all

Checkpoint AP's census was the first pass built from the **code and registered scopes**
rather than from inherited rankings, and it found exactly one candidate in the
productive bucket. The gap was specific:

- **EXP-033** tested the engraved-route corpus — but only behind a single **fixed**
  monoalphabetic map, i.e. a position-*invariant* mask.
- **EXP-036** paired a periodic mask with transpositions — but its corpus is **keyed
  columnar, widths 2–10**, which does not contain the engraved routes.
- **EXP-043** tested the two-mask sandwich — but only with **affine mod 97** `pi`.

So the engraved routes had never met a position-**varying** mask, let alone two. That
is a real hole, not a relabelling, and it was verified as a hole before any test ran:
**none of the 12 corpus permutations is affine**, so the family is provably disjoint
from EXP-043, and the identity is absent.

## Declared scope (frozen before testing)

| Axis | Value |
|---|---|
| `pi` | `engraved_routes()` x {forward, inverse}, deduplicated 14 → **12** |
| `p`, `q` | 1..10 each, all **100** ordered pairs |
| conventions | the **12** committed |
| **N** | **14,400** |

Two routes (`eng_rows_boustro`, `eng_rows_rl`) are involutions, which is why 14
route/orientation pairs collapse to 12 distinct permutations.

## Budget — predicted, then confirmed by the run

| Quantity | Preregistered | Measured |
|---|---|---|
| worst-case `d_eff` | 19 | **19** |
| `log26(N)` | 2.939 | **2.939** |
| budget | 21.939 | **21.939** (< 24, PASS) |
| expected accidental survivors | 0.0012 | **0.0012** |

`mu = 24 - d_eff` ranges from **5** at worst to **23** at best, so the family is
non-vacuous everywhere in the declared scope.

## Controls

| Control | Outcome |
|---|---|
| Positive — planted synthetic instance carrying the real cribs at the real positions | **PASS** (`eng_cols_boustro/A`, p=7, q=9, rank 15) |
| Out-of-family permutation must not be accepted | **PASS** (verified non-affine *and* non-engraved, infeasible) |
| Adversarial — corrupt a crib-constrained ciphertext position | **PASS** (position 73 flips feasibility) |
| Blind-region — corrupt a position outside every crib image | **PASS** (position 0 stays feasible) |

The blind-region control is the one that keeps the other three honest: it *measures*
crib reach instead of assuming it, and its passing is what makes the adversarial
control's failure meaningful rather than automatic.

## Independent verification

`audit/verify_exp044.py` re-derives everything from `data/k4.json` and `k4lib`:

- **Route A — 4,000 of 4,000 cycle certificates verified.** Each is a self-contained
  *proof*: an explicit even-length alternating cycle in the bipartite crib graph whose
  alternating edge-value sum is non-zero mod 26. Since that sum telescopes to zero for
  any assignment, a non-zero value is impossible — no solver is trusted.
- **Route B — brute-force forward simulation with no graph theory**: all 432
  configurations with `p+q <= 3` fully enumerated, plus a random sample of 24 at
  `p=q=2` (456,976 key pairs each). 0 feasible.
- **Route B can say yes**: a planted in-family instance *is* found, so the negative is
  not vacuous.
- Corpus reconstruction, disjointness from all 9,312 affine permutations, and the
  budget arithmetic, all reproduced independently.

## What this closes — and what it does not

**Closes:** the engraved-geometry route corpus inside two additive periodic masks at
`p, q <= 10`, across the 12 committed conventions.

**Does not close, and must not be written up as closing:**

- permutations outside the engraved corpus;
- `p` or `q` above 10;
- non-additive masks;
- three or more stages;
- arbitrary non-affine `pi` in a sandwich — only this independently declared corpus
  was tested.

## Motivation caveat, carried forward as preregistered

The corpus splits by how well the Kryptos record supports it:

- **row-based routes** (`eng_rows_*`) rest on Grade-A *textual* row order
  (`4/31/31/31`) — strong;
- **column-based routes** (`eng_cols_*`) require a column lattice that **Checkpoint AJ
  says is not physically established** — weaker.

Since the result is zero feasible, no survivor needed this caveat. It is recorded
because it would have governed the interpretation had the result gone the other way,
and preregistered caveats do not get quietly dropped when they turn out unneeded.
