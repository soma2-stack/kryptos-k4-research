# Checkpoint T — constraint-first architecture-discovery pass

**Starting HEAD:** `8d9c9e4867e52a7d19afaafa0645b7b1865b3168`, branch `claude/k4-post-j`.
**Method:** derive structural requirements from the data first; only then ask whether any
bounded architecture is motivated well enough to become EXP-040.
**Verification:** every exact claim below is re-checked by `audit/verify_checkpoint_T.py`,
which imports no project code and rebuilds K4 from `data/cipher_side_rows.json`.

**Result up front: `NO EXP-040 JUSTIFIED`.** Three durable findings were produced anyway;
two are new, one is an independent replication of EXP-020.

---

## 0. Inputs actually used

Nothing outside the admitted set was consulted. No alleged plaintext, no solution
material, no Folder 8 pages, no clue mining from the Folder 9 manuscript.

The physical row split was **re-derived, not assumed**:

```
row 25, last 4 chars   OBKR                              message idx [0,4)
row 26   (31 chars)    UOXOGHULBSOLIFBBWFLRVQQPRNGKSSO   message idx [4,35)
row 27   (31 chars)    TWTQSJQSSEKZZWATJKLUDIAWINFBNYP   message idx [35,66)
row 28   (31 chars)    VTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR   message idx [66,97)
```

Concatenation reproduces the pinned ciphertext exactly. This split is **unaffected by the
withdrawn "uniform 31-column" claim**, which concerned rows 1–24 of the whole sculpture;
rows 25–28 genuinely are 31 characters and the K4 segmentation is internally verified.

Crib geometry, which drives everything below:

- `EASTNORTHEAST` (21–33) lies **wholly inside row 26**, at row-local indices 17–29.
- `BERLINCLOCK` (63–73) **straddles the row 27/28 boundary**, splitting as `BER | LINCLOCK`.
  Positions 63–65 are row-local 28–30; positions 66–73 are row-local 0–7.

---

## PART 1 — architecture-independent constraint extraction

### 1.1 Exact facts (no model assumed, no null needed)

| # | Fact |
| --- | --- |
| F1 | No fixed substitution `P→C` is consistent: 8 of 9 repeated plaintext letters take different ciphertext letters. |
| F2 | No fixed substitution `C→P` is consistent: 9 ciphertext letters carry two different plaintext letters. |
| F3 | Exactly two positions are self-mapping: `S→S` at 32, `K→K` at 73. |
| F4 | The only plaintext letter with a constant image is `R→P`, at 27 and 65 (distance 38). |
| F5 | **Pure transposition of the K4 message is impossible.** See §7.1 — this is new. |
| F6 | No convention shows a constant first or second difference of the derived key in either crib run. |
| F7 | No order-1 keystream map `k(i+1) = f(k(i))` over Z26 is consistent, under any of the 12 conventions. |
| F8 | The derived key takes 12–16 distinct values across the 24 positions, depending on convention. Any generator must be able to emit that many values. |

### 1.2 Pattern observations, each killed by its own null

**F4, the `R→P` repeat.** Tempting as a repeated-state signature. Under the null of
independent uniform ciphertext letters, the probability that *at least one* of the nine
repeated-plaintext groups (sizes 2,2,3,2,2,2,2,2,3) is constant is **0.242**, with expected
count 0.272. One constant group is unremarkable. **Not evidence.** Discovered post hoc.

**Message-aligned "periodic fits" at periods 27, 28, 29.** All 12 conventions appear
consistent there. This is entirely an artifact — see §7.2. **Not evidence.**

**Row-number additive offset, `k_i = base[i mod n] + c·row`, at n = 26.** Twelve
(convention, `c`) combinations survive. Null: 12 conventions × 26 values of `c` × 26⁻¹
(period 26 supplies exactly one equality constraint) = **12.0 expected**. Observed 12.
An exact match to chance. **Not evidence.**

### 1.3 Hostility to small-memory deterministic models

F7 is the sharpest statement available: a keystream generator whose next value is a
function of its current value alone cannot produce the crib key streams, in any admitted
convention. EXP-038 already extended this exhaustively to second-order affine recurrences.
The 24 pairs are therefore **actively hostile** to low-memory autonomous keystreams, and
any surviving stateful model must draw on something beyond its own recent key history —
plaintext, ciphertext, position, or an external tape.

---

## PART 2 — coverage map: what EXP-001…039 actually left open

| Structural class | Status | Defining scope |
| --- | --- | --- |
| Monoalphabetic substitution | **PROVED IMPOSSIBLE** | F1/F2, cribs alone |
| Playfair, reflector machines | **PROVED IMPOSSIBLE** | EXP-007, crib positions verified at Checkpoint P |
| Pure transposition (K4 alone) | **PROVED IMPOSSIBLE** | §7.1 — *upgraded this checkpoint from STRONGLY DISFAVORED* |
| Periodic shift key, period ≤ 48, no transposition | **TESTED NEGATIVE** | EXP-001, 12 conventions |
| Affine keystream `a·i+b` | **TESTED NEGATIVE** | EXP-001, all 676, 12 conventions |
| Transposition ∘ periodic polyalphabetic | **TESTED NEGATIVE** | EXP-036, periods 2–23, 4.3×10⁹ cases |
| Any fixed A–Z map ∘ declared transposition | **TESTED NEGATIVE** | EXP-033, 1.76×10⁸ cases |
| Substitution ∘ double columnar (Kryptos keywords) | **TESTED NEGATIVE** | EXP-039, 9 ordered pairs |
| Porta, direct and composed | **PROVED IMPOSSIBLE / TESTED NEGATIVE** | EXP-037; half-parity kills the direct form |
| Second-order affine recursive keystream | **TESTED NEGATIVE** | EXP-038, message-aligned, no reset |
| Text-dependent key from one lagged symbol | **TESTED NEGATIVE** | EXP-034 |
| Panel running key | **TESTED NEGATIVE** | EXP-035, 43,824 cases |
| Key restart at physical row boundaries | **TESTED NEGATIVE** | EXP-020 (correct geometry); replicated §3 |
| Single key reset at one searched boundary | **TESTED NEGATIVE** | EXP-006, EXP-015 |
| Standard Fractionated Morse, Digrafid, CM Bifid, Gromark | **PROVED IMPOSSIBLE / reduced** | Checkpoint O |
| Quagmire I–III, Gronsfeld | duplicates | Checkpoint N |
| Periodic key of period 27–29 | **UNTESTABLE WITH CURRENT DATA** | zero constraints — §7.2 |
| Per-row *independent* keys (a different key each row) | **UNTESTABLE WITH CURRENT DATA** | no forced equality exists |
| Fractionation with period ≥ 4 | **UNTESTABLE WITH CURRENT DATA** | EXP-013 |
| Cross-section transposition spanning K1–K4 | **UNTESTED, EVIDENCE-POOR** | no documentary support; §7.1 does not reach it |
| Higher-order / nonlinear / externally seeded state | **UNTESTED, EVIDENCE-POOR** | unbounded without a named source |

### 2.1 Assumptions shared by earlier experiments — audited

| Shared assumption | Genuinely untested? |
| --- | --- |
| message-aligned indexing | **No** — EXP-020 tests row-local and line-reset indexing directly |
| no state reset | **No** — EXP-006/015 (one searched reset), EXP-020 (three fixed resets) |
| one continuous key stream | **No** — same as above |
| no physical-row reset | **No** — EXP-020, on the correct geometry |
| no row-dependent initialisation | **No** — EXP-020 tests a per-line additive offset; §3 M8/M10/M11 extend it |
| no position-dependent alphabet change | **Yes, but unbounded** — no evidence names a switching rule |
| no method boundary inside K4 | **Partly** — see Part 4; only three boundaries are admissible and all are covered |
| encryption direction fixed globally | **Partly** — boustrophedon traversal tested in §3 (M6/M7), negative |
| fixed substitution map | **No** — EXP-034 covers text-dependent keys |
| fixed permutation | **No** — EXP-033/036/039 sweep permutation families |
| one stage vs composed stages | **No** — EXP-033/036/039 are all two-stage |

**Conclusion of Part 2:** the "silently shared assumptions" list is largely already broken
by existing experiments. The two assumptions that remain genuinely open — a
position-dependent alphabet switch, and higher-order externally seeded state — are open
precisely because **no evidence bounds them**, which is a gate-3 failure, not an opportunity.

---

## PART 3 — physical row / visual-structure reset audit

Only actual row boundaries were used: message indices **4, 35, 66**. No invented columns,
no x-coordinates, no assumed lattice.

Eleven row-structured key-indexing models were swept against all 12 conventions and all
periods 2–40. `min-constraints` is the weakest equality-constraint count over the period
range, and is reported so that a vacuous "fit" cannot be mistaken for a survivor.

| Model | min-constraints | Survivors |
| --- | --- | --- |
| M1 message-aligned, no reset (baseline) | 0 | 12, **all at periods 27–29, all vacuous** |
| M2 reset at every row boundary | 2 | **none** |
| M3 single reset at row 27/28 (i=66) | 3 | **none** |
| M4 single reset at row 26/27 (i=35) | 6 | **none** |
| M5 resets at 35 and 66 | 3 | **none** |
| M6 boustrophedon, odd rows reversed | 3 | **none** |
| M7 boustrophedon, even rows reversed | 3 | **none** |
| M8 row-local index + row number | 1 | **none** |
| M9 row-local + 31·(row−25) | 0 | vacuous only |
| M10 `base[i mod n] + c·row` | — | 12 at n=26, **exactly the null expectation of 12.0** |
| M11 `base[local mod n] + c·row` | — | **none**, any n ∈ 2…31, any c |

### 3.1 The five questions, answered

1. **Documentary/physical motivation?** Genuine but weak. Sanborn cut the panel line by
   line from stencils, and restarting a key per line is the cheapest hand procedure. This
   motivated EXP-020 and it motivates M2–M11.
2. **Exact enough to preregister?** Yes — the reset positions come from the object.
3. **Bounded?** Yes.
4. **Do the 24 crib letters reject it meaningfully?** **Yes, and this is the crux.** Because
   `BERLINCLOCK` straddles the row 27/28 boundary and `EASTNORTHEAST` reaches row-local
   indices 28 and 29, row-local indexing forces exactly two equalities:
   `k(32) = k(63)` and `k(33) = k(64)`. All 12 conventions fail both.
5. **Already covered?** **Yes.** EXP-020 states this prediction in advance, computes the same
   26⁻² null, and reports 0 of 12. My sweep is an **independent replication reached from a
   different starting point**, not a new result. M3–M7 and M10/M11 extend the shape of the
   family; all are negative.

### 3.2 Does EXP-038's "message-aligned / no reset" scope leave a row-reset version open?

**Technically yes, substantively no.** EXP-038 covers second-order affine recurrences
without reset. A row-reset variant would re-seed the recurrence at indices 4, 35, 66.

It fails the gate on **power**, not on plausibility. Re-seeding partitions the 24 crib
letters into groups of 13 (row 26), 3 (row 27) and 8 (row 28). Each group then needs its
own seed pair, adding 6 free Z26 values while removing the cross-row constraints that gave
EXP-038 its force. Row 27 contributes 3 constrained positions against 2 fresh seed
values — essentially free by construction. Per the user's own instruction, a family that is
only *technically untested* but lacks both evidence and power is **rejected, not tested**.

---

## PART 4 — method-change possibility inside K4

Scheidt described changing methodology as the sculpture progressed. That is evidence about
**K1→K4**, not about internal structure within K4.

An internal split is admissible only if an independently established boundary motivates it.
The complete list of such boundaries is **{4, 35, 66}** — the physical row edges. There is
no `?` character in K4, no punctuation, no established vertical lattice, and no documentary
statement of an internal division. Sweeping arbitrary splits 1–96 is explicitly excluded.

All three admissible boundaries are already covered, at three levels of generality:

- one reset at a searched boundary — EXP-006, EXP-015;
- three fixed resets — EXP-020;
- single resets at 35 and at 66 individually, plus the pair — §3 M3/M4/M5.

Every one is negative. **No bounded internal-method-change hypothesis survives that is not
already tested.** The unbounded version — an arbitrary change of rule at an unmotivated
position — fails gate conditions 1 and 3.

---

## PART 5 — the "historic basis" filter

The 1999 *Washington Post* statement (now independently sourced, `docs/external/checkpoint-S2-1999-washington-post-scheidt-provenance.md`) is used as a **filter, not a cipher name**.

Properties a 1989–90 hand-teachable, historically grounded, adapted system should have:

- finite letter alphabet, no bit-level operations;
- low state, executable with pencil, paper and printed tableaux;
- deterministic and exactly reproducible;
- no secret hardware, no software keystream;
- **teachable to a non-cryptographer in a short handover** — 1991 Scheidt: he spent about a
  further month, then gave Sanborn "this is how you do it";
- executable by hand across a construction process spanning months;
- hard because the *method and key* are unknown, not because of computational cost.

### What this filter rejects

- generic modern stream and block ciphers, and any software-generated keystream;
- any construction requiring machine assistance to execute;
- keys exceeding the EXP-019 unicity bound of roughly 66–76 letters — Sanborn intended
  eventual solution, so a key larger than the message can carry contradicts stated intent;
- high-order nonlinear recurrences that a hand operator could not run reliably for 97
  characters without error.

### What it does not do

It does not name a cipher, and it must not be read as one. Crucially it is **not**
constructive: it eliminates candidates but selects none, and the classical hand-cipher
catalogue it points at is precisely the catalogue EXP-001…039 has already exhausted.

---

## PART 6 — search for a real EXP-040

Every candidate surfaced by Parts 1–5, against the eight gate conditions:

| Candidate | Fails on |
| --- | --- |
| Row-reset periodic key | 5 — covered by EXP-020; also replicated negative here |
| Row-reset second-order recurrence | 4 and 6 — row 27 offers 3 constraints against 2 fresh seeds |
| Boustrophedon traversal | 5 — tested negative in §3, and 1 is weak |
| Internal method change at 4 / 35 / 66 | 5 — covered by EXP-006/015/020 |
| Internal change elsewhere | 1 and 3 — no boundary is independently established |
| Position-dependent alphabet switch | 2 and 3 — no rule, unbounded |
| Higher-order / externally seeded state | 3 and 6 — unbounded without a named source |
| Cross-section K1–K4 transposition | 1 — no documentary support whatsoever |
| Period 27–29 periodic key | 4 — **zero** constraints; unfalsifiable with current data |
| Per-row independent keys | 4 — no forced equality exists at all |

**No candidate passes all eight. `NO EXP-040 JUSTIFIED`.** No experiment was manufactured.

---

## PART 7 — new structural findings

### 7.1 Pure transposition of K4 is PROVED IMPOSSIBLE *(new)*

A transposition permutes characters and therefore preserves the letter multiset exactly.

- The two verified cribs place `E` at message positions **21, 30 and 64** — the plaintext
  contains **at least three** `E`s.
- The K4 ciphertext contains **exactly two** `E`s.

Contradiction. No search, no statistics, no language model.

This **upgrades** the existing grade. EXP-007 eliminated pure transposition via an
index-of-coincidence argument graded *STRONGLY DISFAVORED, not proved* — conditional on the
plaintext being ordinary English. The multiset argument is unconditional and belongs at
**PROVED IMPOSSIBLE**, alongside Playfair and the reflector machines.

- **Null model:** none required; this is a deterministic contradiction.
- **Post hoc?** The observation is post hoc, but its validity does not depend on selection —
  it is a proof, not a test statistic.
- **Scope:** transposition of the **K4 message alone**, with no substitution layer. It does
  **not** reach substitution-then-transposition (EXP-033/036/039 cover that), nor a
  transposition spanning K1–K4 jointly, where the multiset argument has no purchase.

### 7.2 The crib set has a structural blind spot at periods 27–29 *(new)*

Equality constraints available to any message-aligned periodic model, by period:

```
n:      2   3   4  ...  23  24  25  26  27  28  29  30  31  32
count: 22  21  20  ...   7   5   3   1   0   0   0   1   2   3
```

The two cribs are contiguous runs of 13 and 11 characters, separated by a gap. Within-crib
differences never exceed 12; cross-crib differences lie in [30, 52]. A period therefore
generates a collision only if it divides some difference in that set. **Periods 27, 28 and
29 divide none of them**, so they impose *no constraint whatsoever*.

Consequences:

1. Any report of a "consistent period" at 27–29 — including the 12 conventions found in §3
   M1 — is **vacuous** and must never be counted as a survivor.
2. This is an **information-theoretic ceiling, not a gap in effort**. EXP-036 capped its
   sweep at period 23 under a minimum-constraint rule and was therefore right to stop; the
   blind spot is not a defect in any prior experiment.
3. It is unreachable with current data. Closing it requires **a third crib, or any verified
   plaintext letter in the gap 34–62 or the tail 74–96** — placed so that some new
   difference is divisible by 27, 28 or 29.

### 7.3 Constraint density is the binding resource, not compute

Across every model in §3, survivors appear **only** where the constraint count collapses,
and in exactly the numbers chance predicts (M1 at 27–29 with 0 constraints; M10 at n=26 with
1 constraint and 12.0 expected survivors, 12 observed). Nothing survives anywhere the data
can actually speak.

The practical consequence for future work: **a candidate architecture is worth running only
if its constraint count stays high across its whole parameter range.** M4 (single reset at
i=35, minimum 6 constraints throughout) is the strongest-powered row model available;
it is negative.

---

## What information is still missing

Ranked by how much each would unlock:

1. **A third verified crib, or any verified plaintext letter in positions 34–62 or 74–96.**
   This is now the single highest-value input in the entire project. It would close the
   27–29 blind spot, restore power to long-period and per-row models, and give
   reset-at-boundary recurrences real force. It outranks further cryptanalysis.
2. **The unedited 2005 Zetter/Scheidt interview material** (Request 2) — still the primary
   documentary target, unchanged.
3. **The original/full 1991 ABC Scheidt interview audio/video** (secondary) — to recover the
   muffled passage in context.

Absent one of these, the frontier is not a missing experiment. It is a **missing constraint**.

K4 remains unsolved.
