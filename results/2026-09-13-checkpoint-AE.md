# Checkpoint AE — K4 decidability census

**Branch:** `claude/k4-post-j`. **Starting HEAD:** `9ca31c47c0c35645bec2dbc531f3440b86dcd428`.

**No new cipher experiment. No EXP-040. K4 remains unsolved.**

Census: `docs/analysis/k4-decidability-census.md`.
Diagnostics: `audit/census_AE.py` — regenerates every figure and asserts 15 of them, all passing.
Only the two public cribs were used; no alleged, leaked or reconstructed K4 plaintext was
searched for, fetched, quoted or inferred.

## Organizing principle

Checkpoint AC's result is the axis of the whole census: **parameter sharing, not merely bounding
a stage, is what creates constraints.** A stage constrains only when one finite parameter set is
reused across positions so the crib letters collide on it.

## The two geometric facts that decide almost everything

The 24 letters are two contiguous runs, not 24 independent points. Within-run distances never
exceed 12; cross-crib distances lie in 30–52.

1. **The period blind spot.** A shared periodic schedule receives 22 constraints at p=2 falling
   to 1 at p=26, then **exactly zero at p = 27, 28, 29**, recovering to 1 at p=30. Those periods
   are **undecidable with the present crib geometry** — not survivors.
2. **The block-repeat drought.** No plaintext block repeats at size 2, 4 or 5 at any alignment.
   Size 3 has exactly one repeat per alignment (`EAS` 21/30, `AST` 22/31, both at distance 9).
   This is why the polygraphic classes are vacuous rather than merely hard.

## The eight questions

1. **Already closed:** fixed monographic maps (± a declared permutation); periodic schedules for
   p ≤ 23 **in the declared shift/combiner families** (the 12 committed conventions — *not*
   arbitrary 26×26 tables, which are class L and are vacuous under the present cribs; clarified
   prospectively at Checkpoint AF); bounded position-functions and bounded recurrences; source lookups at every declared
   scope; declared single and precommitted double transpositions; pure transposition (proved
   impossible); Porta, Quagmire I–III, Gronsfeld, standard Fractionated Morse, Digrafid, Gromark.
2. **Decidable now:** only regimes already exhausted. Nothing both open and decisive remains.
3. **Partially decidable:** two masks around a permutation (7 constraints at the tempting (8,10),
   15–19 at short periods); structured fractionation with a fixed readout (45–48 free classes
   against 24 letters); periodic schedules at p = 24–26 (5, 3, 1 constraints).
4. **Mathematically vacuous:** free inner map behind a free mask, and free polygraphic map behind
   a *bounded* outer map — both provably zero-constraint; an arbitrary 26×26 table at the common
   periods; arbitrary `f(i)`, arbitrary recurrence, arbitrary permutation; any new source without
   crib-position repeats.
5. **Require more plaintext:** periods 27–29 (a hard ceiling); the polygraphic classes, to escape
   vacuity; the two-mask and arbitrary-table classes, to gain real power.
6. **Require a documentary parameter first:** two-mask (a period or inheritance rule); structured
   fractionation (a named inner structure); arbitrary table (a specific family); length-changing
   encodings (an alignment rule); source lookup (a named source).
7. **Minimum additional evidence.** For periods 27–29: **one** verified letter, best placed at
   1, 3, 91, 93, 95 or 96. For the polygraphic classes: a **short contiguous run**, because only
   contiguity can create the block repeats they need.
8. **Eligible for EXP-040 now: none.**

## Request 7, made actionable

Computed structurally, from which distances a new position creates. Of the 73 unknown positions,
**48 unlock all three blind periods at once** and **70 of 73 unlock at least one**. The best
single positions are **1, 3, 91, 93, 95, 96** — each unlocks all three blind periods and adds
constraints at 34 of the 39 periods in 2–40. Exactly three positions — **20, 47, 74** — unlock
none, their distances to every crib position avoiding all multiples of 27, 28 and 29.

**A single scattered letter is worth a great deal to the periodic and mask classes. Only a
contiguous run changes the verdict for the polygraphic ones.**

## Strongest safeguard the census installs

The identity-outer demonstration. The 11 crib digraphs are all distinct at both alignments, and
so are their 11 ciphertext images, so a consistent injective inner map exists **even with the
outer map pinned to the identity**. A hidden inner stage is testable only if it *shares
parameters across positions* — never merely because the outer stage is bounded. This forecloses
the recurring "maybe cipher X is hidden underneath another stage" rescue.

## Correction to Checkpoints AA and AC

Both stated that disconnection of the two-mask bipartite graph *lowers* the constraint count.
**That is backwards.** For fixed edges and vertices, more components means more independent
cycles, so disconnection **raises** it. `24 − (p+q−1)` is a **lower bound**, attained in the
connected fully-occupied case, not an upper bound — measured minima over 400 random permutations
per pair match it exactly, with means slightly above.

The class is therefore marginally better constrained than those checkpoints said. **No
conclusion changes**, because it fails on evidence, not on power. Recorded prospectively; no
history rewritten.

## What was not done

The 15 conditionally-SAT Trifid configurations were **not** chased, optimised, language-scored or
relabelled, and no keywords were added. They remain compatibility results with 45–48 free ternary
classes against 24 crib letters, selected post hoc, and are not candidates. No cipher sweep,
historical family, order-3 recursion, arbitrary grid, random alphabet or generic double
transposition was run.

## ONE next action

**No architecture passes both documentary motivation and cryptanalytic decidability, so the next
action is evidence acquisition, not another cipher experiment.**

Pursue **Request 2 — the unedited 2005 Zetter/Scheidt interview material**, together with the
original `ScheidtNova.doc` or the corresponding GBH production transcript identified at
Checkpoint Z. The published WIRED interview is explicitly described as edited for length and
organization, and **this repository has not located the unedited material; it is not claimed to
be publicly available.**

The census sharpens what would make it decisive. A source saying the process was masked, custom
or complex selects nothing — the scorecard shows generic words are not cipher names. The single
sentence that would collapse this census into a finite experiment names either **a structured
stage whose parameters are shared across positions**, or **a period or key-length inheritance**.

K4 remains unsolved.
