# Checkpoint AP — the crib cycle-rank theorem, and a frontier census built from it

**Branch:** `claude/dreamy-archimedes-79k6u0` · **Date:** 2026-09-21
**Code:** `audit/frontier_census_AP.py` (self-contained; imports no experiment)

## Summary

The repository's organising criterion was

    log26(N) + d_eff < 24

with `d_eff` described as "the effective rank of parameter influence on the 24 crib
values". That is correct but it was an *instruction to go compute a rank*. This
checkpoint replaces it with a **combinatorial invariant that can be read off a graph
before any linear algebra is written**, proves the two agree, and shows the invariant
subsumes four separate results the repository had been carrying as independent facts.

## 1. The theorem

**Setting.** Call a family *crib-pairwise-affine* if each of the 24 crib positions
yields an equation over Z26

    sum_{v in S_i} eps_{i,v} * u_v = c_i ,   eps in {+1,-1},   |S_i| <= 2

in unknowns `u_1..u_n`. Every additive-mask architecture in this repository is of this
shape: one mask, two masks around a permutation, propagating feedback, and a free
monoalphabetic map all qualify.

**Construction.** Build a multigraph `H` on the unknowns that actually appear:

- `|S_i| = 2` contributes an **edge** `{u,v}` carrying the sign `sigma = -eps_u * eps_v`;
- `|S_i| = 1` **anchors** its vertex (pins it to a known value);
- `|S_i| = 0` is a free-standing constraint.

Call a component **balanced** if every cycle in it has sign product `+1`.

**Theorem.** Over GF(13),

    d_eff  =  sum over components K of   |K|      if K is anchored or unbalanced
                                         |K| - 1  otherwise

and the number of independent constraints the cribs impose is the **cycle rank**

    mu  =  24 - d_eff .

A family of `N` classes has expected accidental survivors `N * 26^(-mu)` and can
discriminate only if `log26(N) < mu`, which is the old criterion rearranged.

**Why balance.** An unbalanced cycle multiplies to `-1` on return, forcing
`2u = const`, which pins an *absolute* value rather than only a difference — exactly
what an anchor does. Balance is invisible mod 2, where `-1 = 1`, so the theorem is
stated over GF(13) and the mod-2 rank is reported separately rather than averaged
into it. This matters: Z26 is not a field and the CRT components genuinely differ.

## 2. Verification

`audit/frontier_census_AP.py` checks the invariant against exact rank over Z26
(`k4lib.modlin.rank_mod_p`) on:

- single periodic masks, `p = 2..29`;
- single masks with mixed Vigenere/Beaufort signs;
- a free monoalphabetic map behind a permutation;
- one-tap propagating feedback at seven lags;
- two-mask sandwiches at eight `(p,q)` pairs under identity and affine permutations;
- **4,000 randomly generated signed systems**, in which the unbalanced branch fires
  3,924 times.

**Result: agreement in every case, 0 mismatches.**

**Negative control.** The sign-blind formula `d_eff = |V| - c` — the "obvious" cycle
rank, ignoring balance — is wrong in **4,000 of 4,000** random cases. The balance
correction is load-bearing, not decoration.

## 3. What the theorem subsumes

Four results previously carried separately now fall out of one computation.

| Previously recorded as | Now a corollary |
|---|---|
| Cribs give **zero** constraints at periods 27, 28, 29 | all 24 cribs land in distinct slots, so the graph is a forest of anchored singletons: `mu = 0` |
| Periods 24 / 25 / 26 give exactly **5 / 3 / 1** | reproduced exactly by the invariant |
| Two-mask sandwich gives `24 - (p+q-1)` constraints | `mu = 24 - (|V| - c)`; the AE correction that *disconnection raises* the count is now derived, not patched |
| **Crib-span law** (feedback downstream of every crib is absorbed) | each chain is one anchored component, so `mu = 24 - (#chains meeting a crib)`: a crib alone in its chain contributes nothing |
| **AA-Theorem 1** (free mask over free inner map is vacuous) | distinct blocks give every edge a fresh vertex, so the graph is a forest and `mu = 0` |
| **AC-Result 1** (parameter *sharing*, not stage bounding, makes constraints) | `mu > 0` iff the graph contains a cycle — and a cycle exists only where parameters are reused |

## 4. The sharper statement worth quoting in future work

**Schedule Partition Corollary.** For any *deterministic* single-mask schedule of the
form `k_eff[i] = k[s(i)] + g(i)` with `s` and `g` known, the additive term `g` moves to
the right-hand side. Therefore **`d_eff` depends only on the partition `s` induces on
the 24 crib positions** — not on how irregular, progressive, or clever the rule is.

Measured consequences:

| schedule | crib blocks | `mu` | affordable `log26(N)` |
|---|---|---|---|
| periodic `p=13` | 13 | 11 | 11 |
| progressive `p=13` (+1 per cycle) | 13 | 11 | 11 |
| Fibonacci-indexed mod 13 | 9 | 15 | 15 |
| squares `i^2 mod 13` | 7 | 17 | 17 |
| triangular `i(i+1)/2 mod 13` | 7 | 17 | 17 |
| row-structured `4/31/31/31` | 3 | 21 | 21 |

**A progressive key is budget-identical to the plain periodic key it is built on.**
This eliminates, in one line, the entire "make the schedule irregular" direction as a
route to *more* discrimination: irregularity helps only insofar as it **collides** crib
positions into the same slot, and collision is the only thing that ever mattered.

## 5. Census verdicts

| Area | Class | Reason |
|---|---|---|
| 1. Non-affine `pi` in `M2.pi.M1` | **A — motivated + discriminating** | engraved-geometry routes over the Grade-A textual row structure; verified disjoint from EXP-043's affine corpus, absent from EXP-036's keyed-columnar corpus, and tested by EXP-033 only behind a fixed map. Budget **21.94 < 24**. → **EXP-044** |
| 2. Structured non-shift combiners | **C — unmotivated + discriminating** | the affine combiner `a*P + k` is finite (12 multipliers) and discriminates (budget 7.5–15.5), but **nothing in the Kryptos record selects a multiplicative combiner**. Do not run it merely because it is cheap. |
| 3. Multi-stage substitution / fractionation | **B — motivated + underdetermined** | the Trifid residual's budget is **47.6**, roughly double the 24 available. SAT there is what the budget predicts, not evidence. |
| 4. Deterministic irregular schedules | **D — discard as a distinct direction** | by §4 they are budget-identical to their slot partition; they are not a new family, only a relabelling of one. |
| 5. Impossibility theorem | delivered above | §1 and §4. |

## 6. Scope

The theorem covers families with at most two unknowns per crib equation and `±1`
coefficients. Families outside that shape (for example the affine combiner of Area 2,
whose coefficient on `a` is a known plaintext value rather than `±1`) still need direct
rank computation; `audit/frontier_census_AP.py` does this for them and reports it
separately rather than stretching the theorem past what was proved.
