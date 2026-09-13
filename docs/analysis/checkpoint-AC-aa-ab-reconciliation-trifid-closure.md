# Checkpoint AC — AA/AB reconciliation and exact Trifid residual closure

**Branch:** `claude/k4-post-j`. **Starting HEAD:** `0296fe416833d36ff6b78e9c4a7d18a336bc346b`.
**Audited:** Codex Checkpoint AB at `codex/k4-continuation` commit `3d18d205d08b81a8402eb02310b03476c585a085`.
No Codex file was copied or modified and no branch was merged; AB was read out of its commit.

**Decision: `NO EXP-040 JUSTIFIED`.**

Primary code `audit/checkpoint_AC.py`; independent verifier `audit/checkpoint_AC_verify.py`
(139 checks, imports neither the solver nor `k4lib`); certificates in `results/checkpoint_AC/`.
No web search. No plaintext beyond the two admitted cribs was used or inferred.

---

## 1. Do AA and AB conflict? No — and the reason is sharper than expected

AB was developed from `adf9a18` (Checkpoint Z) in parallel with AA, not on top of it, so
neither had seen the other. They nevertheless agree, because they quantify over different
things.

| | Checkpoint AA | Checkpoint AB |
| --- | --- | --- |
| Outer stage | position-varying mask, parameters over the cribs **free** | **one fixed** injective map |
| Inner stage | a **free** map on blocks | Trifid coordinate fractionation — **structured** |
| Result | zero constraints; family vacuous | equality partition preserved; 175 of 194 refuted |

Both are correct. AA's erasure theorem is explicitly conditioned on the mask parameters over
the cribs being free; AB's equality-partition argument is explicitly conditioned on a single
fixed bijection. Neither claim reaches the other's regime.

### The expected reconciliation is incomplete

The brief anticipated: *AA holds for a free outer mask; AB shows that bounding the outer mask
to a fixed bijection brings internal equality invariants back.* The first half is right. The
second half is **not sufficient**, and this checkpoint demonstrates it.

Pin the outer map all the way down to the identity — the most bounded bijection there is — and
keep the inner stage a free map on digraphs. The 11 crib digraphs are all distinct in both
alignments, and their 11 ciphertext images are also all distinct, so the input-to-output
relation is a partial injection and a consistent injective inner map always exists. **Zero
constraints, with the outer map completely fixed.**

> **AC-Result 1.** Bounding the outer stage is necessary but not sufficient. Constraints
> return only when the outer stage is bounded **and** the inner stage is structured — that
> is, when a single inner parameter set is shared across many positions. Trifid qualifies
> because one 3x3x3 cube serves all 97 positions; a free block map does not.

This strengthens AA's corollary rather than contradicting it, and it identifies parameter
*sharing*, not stage bounding as such, as the thing that generates constraints.

### Scope correction to Checkpoint AA (prospective, not a rewrite)

AA §2 is headed *"Residual A resolved: the polygraphic inner stage is vacuous."* That heading
is broader than the result it reports. The body, the theorem and the ranked-table row all say
**free** inner stage behind a **free** mask, which is correct; the heading does not. AB
exhibits a structured polygraphic inner stage under a bounded outer map for which 175 of 194
configurations are refutable, so the unqualified reading is false. A dated correction has been
appended to the AA document. Nothing in AA's mathematics changes, and its falsifiability
budget in fact predicts this checkpoint's outcome (§5).

---

## 2. Verification of Codex's claims

Every item was re-derived here with an independent implementation.

| # | Claim | Result |
| --- | --- | --- |
| 1 | K4 uses all 26 letters | **CONFIRMED** — 26 distinct, exactly A–Z |
| 2 | A 25-symbol inner alphabet followed only by fixed letterwise maps and transpositions cannot emit 26 symbols | **CONFIRMED** as stated. A fixed letterwise function cannot enlarge an inventory and a transposition only permutes positions, so the image stays within 25 symbols while K4 needs 26. It is a statement about *fixed* maps: a position-varying outer stage escapes it, which is why AB restricts to a fixed bijection |
| 3 | Under one fixed outer bijection, `Xi = Xj` iff `Ci = Cj` on the acted-on symbols | **CONFIRMED**, and both directions are needed. Forward is injectivity; backward is well-definedness. AB uses both |
| 4 | The coordinate-row-concatenation model is implemented correctly | **CONFIRMED.** Reimplemented from the definition — within a block of length `L`, `stream[m] = v[a + (m mod L)][m div L]` and `X[a+j] = (stream[3j], stream[3j+1], stream[3j+2])` — and it reproduces AB's dependency structure |
| 5 | Handling of shortened final blocks, physical-row resets, unknown positions, shared coordinates for repeated known letters | **SOUND.** Terminal blocks are correctly truncated by `min(a+period, hi)`; resets use the authoritative row bounds `(0,4) (4,35) (35,66) (66,97)`; unknown positions get independent variables, which is a **relaxation** and therefore safe for UNSAT; repeated known letters correctly share coordinates |
| 6 | UNSAT propagation is one-sided; UNRESOLVED is not SAT | **CONFIRMED**, and AB labels this correctly throughout. The relaxation in item 5 makes UNRESOLVED strictly weaker than SAT, which is exactly why the present checkpoint was worth running |
| 7 | 175 rejected of 194 audited | **REPRODUCED EXACTLY** — 88 of 97 continuous, 87 of 97 row-reset |
| 8 | The 19 labelled survivors | **REPRODUCED EXACTLY.** Continuous `5,7,10,13,14,16,23,28,29`; row-reset `4,7,11,14,19,20,22,23,26,28` |

One gap, not an error: AB does not use the fact that the ciphertext's 26 distinct letters force
**exactly 26 of the 27 cells** to be occupied. That constraint does real work below.

---

## 3. The reduction that makes the 19 CSPs finite and small

Let `T[l]` be the cell that ciphertext letter `l` is read from. Under one fixed injective
readout the intermediate sequence is simply `X[i] = T[C[i]]`.

Now invert the coordinate-row concatenation. Within each block, knowing every `X` means
knowing every entry of the block's coordinate stream, and each stream entry *is* a plaintext
coordinate. So:

> **AC-Result 2 (T-determinacy).** The entire plaintext coordinate array is a function of `T`
> alone. The 97 unknown plaintext letters contribute no independent freedom whatsoever.

The search therefore runs over `T` only, and the constraints reduce to exactly four:

1. positions holding the same known plaintext letter share a cell;
2. positions holding distinct known plaintext letters take distinct cells (13 crib letters);
3. `T` is injective — 26 ciphertext letters into 26 of the 27 cells;
4. the plaintext occupies at most 26 cells, so a 26-letter alphabet assignment exists.

Constraint 1 is imposed statically by union-find, leaving **45–48 free classes** over
`{0,1,2}` per configuration. Two further invariants make exhaustion cheap:

> **AC-Result 3 (axis multiplicity).** An injection onto 26 of 27 cells uses each value of
> each axis exactly 9, 9 and 8 times. So no union-find class may force one value on more than
> nine letters in a single axis.

> **AC-Result 4 (ternary pigeonhole).** If four or more ciphertext letters are forced into the
> same class in two of the three axes, their cells already agree there, so injectivity needs
> them pairwise distinct in the one remaining axis — which holds only three values. Four
> cannot fit.

AC-Result 4 alone refutes `p=11` row-reset outright, with no search: ciphertext letters
**F, I, S and V** share their axis-1 and axis-2 classes.

---

## 4. Exact status of the 19 residual configurations

Every configuration is fully resolved; none is solver-incomplete.

| period | mode | status | route | nodes |
| --- | --- | --- | --- | --- |
| 5 | continuous | SAT | exhaustive backtracking | 106 |
| 7 | continuous | SAT | exhaustive backtracking | 110 |
| 10 | continuous | SAT | exhaustive backtracking | 203 |
| 13 | continuous | **UNSAT** | exhaustive backtracking | 16 |
| 14 | continuous | **UNSAT** | exhaustive backtracking | 44,677 |
| 16 | continuous | SAT | exhaustive backtracking | 74 |
| 23 | continuous | SAT | exhaustive backtracking | 56 |
| 28 | continuous | **UNSAT** | exhaustive backtracking | 403 |
| 29 | continuous | SAT | exhaustive backtracking | 592 |
| 4 | row-reset | SAT | exhaustive backtracking | 3,870 |
| 7 | row-reset | SAT | exhaustive backtracking | 3,464 |
| 11 | row-reset | **UNSAT** | **ternary pigeonhole, no search** | 0 |
| 14 | row-reset | SAT | exhaustive backtracking | 87 |
| 19 | row-reset | SAT | exhaustive backtracking | 1,961 |
| 20 | row-reset | SAT | exhaustive backtracking | 2,387 |
| 22 | row-reset | SAT | exhaustive backtracking | 9,576 |
| 23 | row-reset | SAT | exhaustive backtracking | 304 |
| 26 | row-reset | SAT | exhaustive backtracking | 195 |
| 28 | row-reset | SAT | exhaustive backtracking | 55 |

**15 SAT, 4 UNSAT, 0 incomplete.** Residual after exact CSP: **15 of the original 194**.

### A defect this process caught

The first complete run returned 18 SAT and 1 UNSAT. The independent verifier rejected 17 of
those 18: the solver enforced crib **dis**equality only as a static class-level pre-check,
which misses two *different* class triples that happen to take the same values. With the
constraint enforced incrementally during search, three configurations flipped to UNSAT. The
verifier existed precisely to catch this, and it did.

### Certificates

**SAT** certificates record the period, reset mode, the outer map on all 26 letters, the 97
plaintext **cells**, and the crib letters' cells. They deliberately do **not** record any letter
labelling of the 73 unknown positions: every bijection from the unused cells to the unused
letters completes the model equally well, so such a labelling carries no information and would
amount to manufacturing a plaintext candidate. The verifier checks each one by running the
cipher **forward** — building the coordinate rows, slicing them into triples, applying the
outer map — and demanding the result equal K4 character for character. All 15 do.

**UNSAT** certificates are deterministic and auditable, never "the solver said so":

- `p=11` row-reset carries the pigeonhole, re-derived by the verifier through breadth-first
  closure over an explicit adjacency list rather than the solver's union-find.
- The other three carry a **replayable refutation trace** (48, 1,209 and 134,031 steps, gzipped
  with a recorded sha256). The verifier replays each step against constraints it builds itself,
  confirms every claimed conflict actually holds, confirms no conflict is claimed that does not
  hold, and confirms every explored node tried all three coordinate values and that the root
  was exhausted. This is checkable in linear time and is stronger than re-running a search.

---

## 5. What 15 SAT means — and does not

**It is not evidence for Trifid.** It is what Checkpoint AA's falsifiability budget predicts.
Each configuration carries 45–48 free ternary classes against 24 crib letters, so compatibility
is the expected outcome and carries essentially no evidential weight. The informative result is
the opposite one: that 179 of 194 configurations are refutable *at all* is what the structure
of Trifid buys, and it is entirely due to one cube being shared across 97 positions.

The conditional fixed-bijection Trifid residual is therefore **narrowed, not closed**.

No historical source establishes Trifid, a 3x3x3 cube, any of these periods, origin zero,
physical-row reset, or a fixed monoalphabetic outer readout. A surviving configuration means
only: *this conditional architecture is compatible with the ciphertext and the two public
cribs.*

---

## 6. EXP-040 gate

The ten-part gate is applied to the strongest surviving candidate, the 15 SAT configurations.

| # | Condition | Result |
| --- | --- | --- |
| 1 | one specific architecture survives | fails — 15 survive, and nothing chooses among them |
| 2 | stage order defined | pass for a test |
| 3 | each stage mathematically defined | pass |
| 4 | finite alphabet conventions | pass |
| 5 | key/parameter sources finite **and justified** | **FAIL** — no source names Trifid, the cube, the periods, origin zero, or the readout |
| 6 | search size statable in advance | pass |
| 7 | both crib regions constrain the model | weak — 45–48 free classes against 24 letters |
| 8 | not already covered | pass |
| 9 | preregisterable criteria | pass |
| 10 | falsifies a meaningful family | **FAIL** — the family was selected *after* seeing which configurations survived |

Conditions 1, 5 and 10 fail. Condition 10 is the decisive one: promoting a SAT structural
survivor into a K4 hypothesis because it survived is exactly the post-hoc selection the
project's gate exists to prevent. No documentary evidence selected this family before the
result was seen.

> **`NO EXP-040 JUSTIFIED`.** No preregistration was written.

---

## 7. What would change this

Unchanged in substance, sharpened in form by AC-Result 1:

1. **A third public crib (Request 7).** With `T`-determinacy the arithmetic is now explicit:
   each configuration has 45–48 free ternary classes against 24 constraints. Additional verified
   plaintext both raises the constraint count and, by creating repeated blocks, activates
   structure that is currently absent.
2. **Evidence bounding the outer stage** — the unedited Zetter/Scheidt material, or the original
   `ScheidtNova.doc`. AC-Result 1 refines what this buys: bounding the outer stage is necessary
   but not sufficient, so the most valuable single sentence would name **a structured inner
   stage** whose parameters are shared across positions.

K4 remains unsolved.
