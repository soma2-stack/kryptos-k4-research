# Checkpoint AA — residual multi-stage architecture elimination

**Branch:** `claude/k4-post-j`. **Starting HEAD:** `adf9a1867496928539f50de608efd157e9ba6a2c`.

**EXP-040 decision: `NO EXP-040 JUSTIFIED`.**

Analysis: `docs/analysis/checkpoint-AA-residual-architecture-elimination.md`.
Verifier: `audit/verify_checkpoint_AA.py` — 24 checks pass, no project imports.
No web search was used; this checkpoint is repo- and mathematics-driven.

## Strongest surviving architecture

**The sandwich, `M2 ∘ π ∘ M1`** — an additive mask, a transposition, then a second additive
mask.

**Why it survives.** The two masks are indexed on opposite sides of a non-commuting
permutation, so they cannot be combined the way same-index shift stages can. It is the *only*
class in the whole residual map that survives purely because a non-commuting step separates
two masks.

**What prevents collapse.** Checkpoint W's rules W-R1…W-R4 collapse everything else: fixed
substitutions compose; fixed substitution commutes with transposition; transpositions compose
to one permutation; same-index additive masks compose to one mask (the K1/K2 periods 8 and 10
give an effective period dividing 40, already inside EXP-001's period ≤ 48 sweep). Only the
intervening `π` blocks the last of these.

**Closest previous experiment.** EXP-036 — periodic polyalphabetic composed with the declared
transposition families, periods 2–23, zero feasible. The sandwich differs by exactly one
additional mask on the far side of the permutation.

**Unresolved free parameters.** The permutation `π` (family and key); the two periods `p` and
`q`; the `p + q` key values; the alphabet convention; and the stage order — which Checkpoints
X and Y record Scheidt **declining** to fix.

**Both crib regions constrain it?** Yes, but weakly, and only through `π`. The constraint
structure is a bipartite linear system over Z26 giving `24 − (p + q − 1)` independent
constraints when connected. At the much-discussed K1/K2 pair (8, 10) that is **7** — and
disconnection of the bipartite graph lowers it further.

**Evidence strength.** Multi-stage is direct Scheidt. The specific sandwich shape is
inference, and the periods are **not evidenced at all**: Checkpoint V found no statement that
K4 reuses K1/K2 key lengths or methods, and `LAYER TWO` does not supply one.

**Testability.** Finite once `π`, `p`, `q` and an order are fixed — but fixing them is the
assumption, not the finding.

**Gate outcome.** Condition 5 (key sources finite **and justified**) fails outright.
Conditions 2, 7 and 10 are weak. **No EXP-040.**

## The main new result: the top-ranked residual is not under-motivated, it is vacuous

Checkpoint W ranked an inner polygraphic/fractionating stage hidden by an outer mask as the
highest-value residual. Checkpoint AA closes it.

**AA-Theorem 1 (erasure).** If the chain ends in a position-varying monographic mask whose
parameters over the cribs are free, and the inner stage is a free map on blocks, then the
architecture fits the cribs for *every* mask — provided no two observed plaintext blocks are
equal. Proof: invert the mask to get the intermediate text, then assign the inner map on
distinct arguments.

The hypothesis is checkable, and had never been checked. **For block sizes 2, 4 and 5, at
every alignment, every block lying wholly inside a crib is distinct.**

**AA-Result 1.** A free digraphic, 4-graphic or 5-graphic inner stage behind a free mask
imposes **zero** constraint. Verified by construction: 4,000 random outer masks, a consistent
inner map exists **4,000 times**. Adding the injectivity a real cipher requires admits 93.6%
against a birthday null of 92.2% — a coincidence detector, not a constraint. This covers the
brief's whole illustrative list (Playfair, Bifid at period 2, Hill 2×2) when the inner stage
is free. The family is **VACUOUS** and fails gate conditions 7 and 10 by construction.

**AA-Result 2.** Block size 3 is the sole exception: one repeated trigram per alignment,
`EAS` at 21/30 and `AST` at 22/31, both at distance 9. A periodic additive mask cancels only
when `p | 9`, forcing a ciphertext repeat that is absent (`FLR`≠`GKS`, `LRV`≠`KSS`).
**A free trigraphic inner stage under a periodic additive mask of period 1, 3 or 9 is exactly
REFUTED**; every other period is vacuous. Three periods is the *complete* extent of what the
current cribs can say about any hidden polygraphic stage.

**Corollary — the falsifiability budget.** An architecture is testable only if
`(free mask parameters over the cribs) + (free inner parameters exercised) < 24`. Every stage
spends from a fixed budget of 24. This is the countable form of Checkpoint T's finding that
constraint density, not compute, is binding.

**Scope correction, stronger than Checkpoint W's.** By AA-Theorem 1, every crib-based proof in
this repository *necessarily* describes the observable end-to-end map, and internal-stage
proofs are impossible in principle while the outer stage is free. The right move is never to
rescue a rejected cipher as an inner stage; it is to bound the outer stage first.

## Also closed this checkpoint

**Transposition + feedback/autokey mask** — closes as vacuous or duplicate. With an unknown
`π` the mask's lagged source is an unknown intermediate symbol at every crib position, which
is exactly the erasure hypothesis. With a known `π` it is a reparameterisation of EXP-034 and
EXP-038 over the EXP-036 permutation corpus, and Checkpoint T's order-1 functional
contradiction already shows the cribs are hostile to low-memory autonomous state.

## Ranked residual table

| Architecture | Evidence support | Already covered? | Collapses? | Crib-constrained? | Finite? | Action |
| --- | --- | --- | --- | --- | --- | --- |
| Free digraphic / 4- / 5-graphic inner + mask | class only | no | no | **NO — zero (AA-1)** | n/a | **CLOSE, vacuous** |
| Free trigraphic inner + periodic mask | class only | no | no | only `p ∈ {1,3,9}` | yes | **REFUTED there, vacuous elsewhere** |
| Mask → transposition → mask | multi-stage direct; periods unevidenced | no | no | yes, `24−(p+q−1)` | yes given `π,p,q` | **HOLD — fails gate 5** |
| Periodic mask + permutation outside EXP-036 | low–moderate | partly | no | yes | yes | HOLD — compounds speculation |
| Transposition + feedback / autokey | none | EXP-034/038 in effect | vacuous with unknown `π` | no | no | **CLOSE, vacuous/duplicate** |
| Non-shift / changing tableau + transposition | class only | named cases closed | no | only if periodised | no | Open, non-actionable |
| Custom stateful mask | licensed, unnamed | no | n/a | rule-dependent | no | **UNTESTABLE WITH CURRENT CRIBS** |
| External-source mask + stage | shape only | EXP-004/014/023/024/029–031/035 | no | no | no | Blocked on a named source |
| Homophonic / variable mapping + stage | weak | no | no | no | no | Underconstrained |

## The single missing fact that would most help

**A third public crib — Request 7.** The polygraphic residual is vacuous *precisely because
there are no repeated plaintext blocks*. Each verified letter raises the falsifiability budget
by one, and letters in positions 34–62 or 74–96 would very likely create block repeats,
converting AA-Result 1 from a closure into a real experiment.

Complementary, not alternative: **one sentence bounding the outer mask** — the unedited
Zetter/Scheidt material or the original `ScheidtNova.doc`. By AA-Theorem 1 that is the only
way *any* inner stage becomes testable. A third crib raises the budget; a bounded mask lowers
the cost.

K4 remains unsolved.
