# Checkpoint AC — AA/AB reconciliation and exact Trifid residual closure

**Branch:** `claude/k4-post-j`. **Starting HEAD:** `0296fe416833d36ff6b78e9c4a7d18a336bc346b`.
**Audited:** Codex Checkpoint AB, `codex/k4-continuation` at `3d18d205d08b81a8402eb02310b03476c585a085`.
No Codex file copied or modified; no branch merged.

**EXP-040 decision: `NO EXP-040 JUSTIFIED`.**

Analysis: `docs/analysis/checkpoint-AC-aa-ab-reconciliation-trifid-closure.md`.
Primary: `audit/checkpoint_AC.py`. Independent verifier: `audit/checkpoint_AC_verify.py`
— **139 checks, all pass**, importing neither the solver nor `k4lib`.
Certificates: `results/checkpoint_AC/` (328 KB).

## 1. Do AA and AB conflict? No

They quantify over different things, and neither had seen the other — AB was developed from
Checkpoint Z in parallel with AA.

- **AA** assumes a position-varying outer mask whose parameters over the cribs are **free**,
  and a **free** inner map on blocks. Erasure: zero constraints.
- **AB** assumes **one fixed** injective outer map and a **structured** inner stage (Trifid
  coordinates). Equality partitions survive: 175 of 194 refuted.

Both correct; neither claim reaches the other's regime.

**But the expected reconciliation is incomplete.** The brief anticipated that bounding the
outer mask to a fixed bijection is what brings internal invariants back. It is necessary and
**not sufficient**. Pin the outer map to the *identity* and keep the inner map free on
digraphs: the 11 crib digraphs are distinct in both alignments and so are their 11 ciphertext
images, so a consistent injective inner map always exists — **zero constraints with the outer
map completely fixed**.

> **AC-Result 1.** Constraints return only when the outer stage is bounded **and** the inner
> stage is structured — that is, when one parameter set is shared across many positions.
> Trifid qualifies because a single cube serves all 97 positions; a free block map does not.
> The generator of constraints is parameter *sharing*, not stage bounding.

## 2. Codex's claims: reproduced

| Claim | Result |
| --- | --- |
| K4 uses all 26 letters | CONFIRMED |
| 25-symbol inner alphabet + fixed letterwise maps + transpositions cannot emit 26 symbols | CONFIRMED as stated (it is about *fixed* maps; a position-varying outer stage escapes it) |
| Equality-partition theorem under one fixed bijection | CONFIRMED, both directions needed |
| Coordinate-row-concatenation model implemented correctly | CONFIRMED by reimplementation |
| Shortened blocks / row resets / unknown positions / shared coordinates | SOUND; unknown positions are a relaxation, hence safe for UNSAT |
| One-sided propagation, UNRESOLVED ≠ SAT | CONFIRMED and correctly labelled throughout |
| **175 rejected of 194** | **REPRODUCED EXACTLY** — 88 of 97 continuous, 87 of 97 row-reset |
| **The 19 survivors** | **REPRODUCED EXACTLY** — continuous `5,7,10,13,14,16,23,28,29`; row-reset `4,7,11,14,19,20,22,23,26,28` |

One gap, not an error: AB never uses the fact that 26 distinct ciphertext letters force exactly
26 of the 27 cells to be occupied. That constraint does real work below.

## 3. Exact status of each of the 19

**15 SAT, 4 UNSAT, 0 solver-incomplete. Residual after exact CSP: 15.**

| UNSAT | route |
| --- | --- |
| p=13 continuous | exhaustive backtracking, 16 nodes |
| p=14 continuous | exhaustive backtracking, 44,677 nodes |
| p=28 continuous | exhaustive backtracking, 403 nodes |
| p=11 row-reset | **ternary pigeonhole, no search at all** |

SAT: continuous 5, 7, 10, 16, 23, 29; row-reset 4, 7, 14, 19, 20, 22, 23, 26, 28.

## 4. Strongest new invariants

**AC-Result 2 (T-determinacy).** Writing `T[l]` for the cell ciphertext letter `l` is read
from, a fixed injective readout gives `X[i] = T[C[i]]`; inverting the coordinate-row
concatenation then makes the entire plaintext coordinate array a function of `T` alone. **The
97 unknown plaintext letters contribute no independent freedom.** This is what turns each
configuration into a small finite CSP over 45–48 ternary classes.

**AC-Result 3 (axis multiplicity).** An injection onto 26 of 27 cells uses each value of each
axis exactly 9, 9, 8 times, so no class may force one value on more than nine letters in one
axis.

**AC-Result 4 (ternary pigeonhole).** Four or more ciphertext letters sharing a class in two
axes must be pairwise distinct in the third, which holds only three values. This refutes
`p=11` row-reset outright: ciphertext letters **F, I, S, V** share axes 1 and 2.

## 5. A defect the verifier caught

The first complete run gave 18 SAT / 1 UNSAT. The independent verifier rejected 17 of those 18:
the solver enforced crib **dis**equality only as a static class-level pre-check, missing two
different class triples that take the same values. Enforced incrementally during search, three
configurations flipped to UNSAT. This is exactly what the two-implementation standard is for.

## 6. Certificates

**SAT** — period, reset mode, the outer map on 26 letters, the 97 plaintext **cells**, crib
cells. Deliberately **no** letter labelling of the 73 unknown positions: any bijection from
unused cells to unused letters completes the model equally, so a labelling carries no
information and would amount to manufacturing a plaintext candidate. The verifier checks each
by running the cipher **forward** and demanding the output equal K4 character for character.
All 15 do.

**UNSAT** — never "the solver said so". The pigeonhole is re-derived by breadth-first closure
over an explicit adjacency list; the other three carry replayable refutation traces (48, 1,209
and 134,031 steps, gzipped with recorded sha256). The verifier replays every step against
constraints it builds itself, confirms each claimed conflict holds, confirms none is claimed
that does not, and confirms every explored node tried all three values with the root exhausted.

## 7. Does this change the EXP-040 decision? No

Gate conditions **1, 5 and 10 fail**. Condition 10 is decisive: the family was selected *after*
seeing which configurations survived. No documentary source establishes Trifid, a 3×3×3 cube,
any of these periods, origin zero, physical-row reset, or a fixed monoalphabetic readout.

**15 SAT is not evidence for Trifid** — it is what Checkpoint AA's falsifiability budget
predicts, with 45–48 free ternary classes against 24 crib letters. The informative fact is the
other one: that 179 of 194 are refutable at all, entirely because one cube is shared across 97
positions. The conditional residual is **narrowed, not closed**.

## 8. Scope correction required to Checkpoint AA

One, prospective and dated, appended to the AA document rather than rewritten into it.

AA §2 is headed *"Residual A resolved: the polygraphic inner stage is vacuous."* The heading is
broader than the result. AA's theorem, body and ranked-table row all correctly say **free**
inner stage behind a **free** mask; the heading does not, and AB exhibits a structured
polygraphic inner stage under a bounded outer map where 175 of 194 configurations are
refutable. No AA mathematics changes, and AA's falsifiability budget in fact predicts this
checkpoint's 15 SAT outcome.

## 9. Single most valuable missing fact

**A third public crib (Request 7)** — now with explicit arithmetic: 45–48 free ternary classes
against 24 constraints per configuration. Additional verified plaintext both raises the
constraint count and creates the repeated blocks that are currently absent.

Sharpened by AC-Result 1: evidence bounding the outer stage is necessary but not sufficient, so
the most valuable single documentary sentence would name **a structured inner stage** whose
parameters are shared across positions.

K4 remains unsolved.
