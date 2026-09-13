# Checkpoint AD — AC verification strengthening

**Branch:** `claude/k4-post-j`. **Starting HEAD:** `4dac2b11ad385035f808ce8188e0cae0690a15f4`.

**Characterisation: Checkpoint AC verification strengthening; no cryptanalytic conclusion
changed.** No EXP number assigned. No new cryptanalytic family started. No Checkpoint AC
history rewritten.

## The gap that was repaired

Checkpoint AC certified three UNSAT configurations — `p=13`, `p=14` and `p=28` continuous — by
having `audit/checkpoint_AC_verify.py` replay the solver's refutation trace. The replay
genuinely confirmed that every recorded conflict was real under the verifier's own constraints.
Its **completeness** test did not carry the weight AC claimed for it.

It asked only whether values 0, 1 and 2 each appeared *somewhere* at each depth, and whether
depth 0 saw all three. That is not tree exhaustion. A trace could omit one child under one
particular prefix and still satisfy the test, because the missing value would be supplied by a
different prefix at the same depth. AC therefore overstated how strongly the independent
verifier established the exhaustion claim. It never implied the solver's verdicts were wrong.

## The repair

An **independent exhaustive DFS** now runs inside the verifier and is the primary UNSAT
verification. It searches over the classes and all seven constraint families that the verifier
already rebuilds from `data/k4.json`:

1. Trifid block segmentation; 2. coordinate dependencies; 3. equal-known-plaintext
constraints; 4. ciphertext-letter injectivity; 5. distinct known plaintext-letter cells;
6. the plaintext ≤26-cell constraint; 7. the axis multiplicity bound.

It does not import or call `audit/checkpoint_AC.py`, and it reads neither the solver's verdict
nor its conflict trace. The only thing it takes from the certificate is the portable
`search_order_hint`, used purely as a variable-order heuristic — variable order cannot change a
SAT/UNSAT answer, only how long the search takes. The DFS returns SAT the moment it completes an
assignment, so a solver error would surface as a failed check rather than be absorbed.

## Results

| configuration | independent DFS nodes | solver nodes | independent verdict |
| --- | ---: | ---: | --- |
| p=13 continuous | 16 | 16 | **UNSAT** |
| p=14 continuous | 44,677 | 44,677 | **UNSAT** |
| p=28 continuous | 403 | 403 | **UNSAT** |

All three independently reach complete UNSAT. The node counts match the solver exactly, which
is expected under a shared variable ordering and is an additional consistency signal rather
than a substitute for the independent search.

**`p=11` row-reset** keeps its direct pigeonhole certificate, re-derived by breadth-first
closure over an explicit adjacency list: ciphertext letters **F, I, S and V** are forced into
the same class on axes 1 and 2, so an injective readout needs four pairwise-distinct values on
the single remaining axis, which holds only three. No DFS required.

**15 SAT certificates** continue to pass their forward checks — the verifier builds the
coordinate rows, slices them into triples, applies the outer map, and reproduces all 97
characters of K4 exactly, for every one.

**Total: 142 checks, all passing**, up from 139. Verified from a **clean checkout**: the solver
regenerates every certificate and the verifier passes 142/142 against them.

## Trace artifacts

The gzipped refutation traces are **retained**, not deleted. Their role is downgraded to a
**supplementary reproducibility record**. Their completeness test was also strengthened while
they remain: rather than the old per-depth test, the replay now walks the trace as a tree and
requires that every internal node account for all three branches **under its own prefix**. The
distinct-prefix counts equal the node counts exactly (16, 44,677 and 403), so the traces are in
fact complete — but the independent DFS, not the trace, is now what establishes it.

## What did not change

Every accepted Checkpoint AC finding stands: the 175/194 AB reproduction, both 19-configuration
survivor lists, the 15 SAT certificates, the p=11 pigeonhole, T-determinacy, the axis
multiplicity invariant, the AA/AB reconciliation, and `NO EXP-040 JUSTIFIED`.

**15 SAT remains compatibility, not evidence for Trifid.** The SAT configurations were not
chased, optimised, language-scored or relabelled, and no keywords were added. They remain
underconstrained conditional compatibility results.

## ONE next direction

**A decidability census over the independently evidenced architecture classes, run before any
further family is chosen.**

The reason is the project's own record. Checkpoint AC states plainly that the Trifid family was
selected post hoc and fails the EXP-040 gate, so continuing it — including trying to eliminate
the 15 SAT cases — would compound the error rather than correct it. Meanwhile Checkpoint AA
showed the binding resource is constraint density, and Checkpoint AC supplied the exact tool for
measuring it: **AC-Result 2 (T-determinacy)** shows that when a structured inner stage shares
one parameter set across positions, the unknown plaintext contributes no independent freedom, so
whole classes collapse to small finite CSPs; **AC-Result 1** identifies parameter *sharing*, not
stage bounding, as what generates constraints at all.

Those two results make it possible to compute, for each candidate class, **whether the present
24 crib letters can decide it at all** — before committing to it. That converts the recurring
question "which family next?" into the answerable one "which families are even answerable?", and
it is the structural safeguard against another post-hoc selection. It is cheap, it is
methodological rather than a cipher guess, and it is the natural product of AC.

Running it is **not** part of this repair session.

The parallel documentary target is unchanged and unranked here: the original `ScheidtNova.doc`
or the unedited Zetter/Scheidt material. AC-Result 1 sharpens what would make it decisive — the
most valuable single sentence would name **a structured inner stage whose parameters are shared
across positions**, not merely bound the outer stage.

K4 remains unsolved.
