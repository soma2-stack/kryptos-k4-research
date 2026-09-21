# Preregistration — EXP-036: K3-type transposition composed with a K1/K2-type periodic polyalphabetic

Committed **before** implementation or execution. Branch `claude/k4-post-j`, base
`806ee4d78e8bc1669074e5056f1e55bcced5f273`. K4 remains unsolved. No external verifier.
No alleged plaintext, purported solution, or K5 material.

## 0. Two corrections that precede this experiment

Both are verified here against repository data, not accepted on assertion.

**Request 5 — my error, not a transcription defect.** K1 = rows 1–2 = 63 characters, all
alphabetic. K2 = rows 3–14 = 372 *physical* characters = 369 letters + 3 `?`. So rows 1–14
hold 435 characters = 432 letters + 3 `?`, and `63 + 372 = 435` is a count of *physical
characters*. Checkpoint L compared 432 **letters** against 435 **characters** as though
they were the same unit. **There is no transcription discrepancy on this basis. Request 5
is FULFILLED** and is no longer carried as open. Kept separate: the historical NSA
DOCID 4050989 convention (K2 as 373, three sections 773, total 870, 97 unresolved) and
Sanborn's reported deletion of an `X` from the end of a K2 line for aesthetic balance.
Those bear on an *intended pre-aesthetic* source, which is a **separately preregistered
source variant** if ever tested. EXP-035 tested the **physical engraved** 869-character
source and keeps that interpretation unchanged.

**The Checkpoint-L "alphabet frontier" does not survive audit.** I claimed the negative
corpus omitted the K1/K2 mixed alphabet. That is wrong. `k4lib/alphabets.py` defines
`KRY = KRYPTOSABCDEFGHIJLMNQUVWXZ`; rebuilding the KRYPTOS keyword-mixed sequence
independently from the keyword gives exactly that string, and
`k4lib/conventions.py::all_conventions()` already enumerates all four
plaintext×ciphertext combinations of {STD, KRY} across three combiners. NSA DOCID 4050988
gives, for **both** K1 and K2, plain component *and* cipher component as keyword-mixed
sequences based on KRYPTOS. **So the historically demonstrated K1/K2 component alphabet is
already present in every experiment that uses `all_conventions()`.**

`PALIMPSEST` and `ABSCISSA` are identified by the primary source as **repeating keys**, not
as component-alphabet keywords. Building mixed alphabets from them would be a new
speculative architecture with no documentary support as component alphabets. Candidate A
(additional keyword-derived component alphabets) is therefore **rejected for now**: it
would add free parameters with no evidence behind them, and a negative would eliminate
nothing anyone has reason to believe. Note also the frontier: arbitrary mixed alphabets on
both sides plus an arbitrary key make the model an arbitrary 26×26 table, which is
unfalsifiable.

## 1. Exact inputs

| input | sha256 |
|---|---|
| `data/k4.json` | `e3b18a93c5fda5a8fc7a9249d25b1567c55cc2b5aef2843a65551b96b754ced8` |
| ciphertext (pinned by `k4lib.data`) | `eea813570c7f1fd3b34674e47b5c3da8948026f5cefee612a0b38ffaa515ceab` |

Public cribs only, zero-based half-open, unchanged: `EASTNORTHEAST` [21,34) against
`FLRVQQPRNGKSS`; `BERLINCLOCK` [63,74) against `NYPVTTMZFPK`. 24 constrained positions.

## 2. Exact model equations

Let `σ` be a permutation of {0..96} from the declared transposition family, `p` a period,
and `k[0..p-1]` key indices in Z26. Both composition orders are tested, because they place
the key on different indices and are genuinely inequivalent (this is EXP-003's original
observation, re-verified: order B is *not* order A under inversion).

- **Order A — substitute at the plaintext index, then transpose.**
  `C[σ(j)] = encrypt_conv(P[j], k[j mod p])`.
  The constraining ciphertext letter for crib position `j` is `C[σ(j)]`, and the residue
  class is `j mod p`, which is **independent of σ**.
- **Order B — transpose, then substitute at the ciphertext index.**
  `C[i] = encrypt_conv(P[σ(i)], k[i mod p])`.
  For crib position `j` the constraining ciphertext letter is `C[σ⁻¹(j)]` and the residue
  class is `σ⁻¹(j) mod p`, which **does depend on σ**.

`k` is **never enumerated**. For each case the key is decided existentially: the case is
feasible iff every pair of constrained positions in the same residue class forces the same
key index. A consistent assignment then extends to a full key. This is the EXP-030/033/035
decision formulation, applied to a periodic key.

## 3. Which degrees of freedom are absorbed — stated explicitly, as required

| degree of freedom | absorbed? |
|---|---|
| 1. plaintext component alphabet | **NOT absorbed** — carried as STD or KRY by the 12 conventions |
| 2. ciphertext component alphabet | **NOT absorbed** — carried as STD or KRY by the 12 conventions |
| 3. numerical / index key | **absorbed** — decided existentially as `p` free values in Z26 |
| 4. source letters used to derive the key | **not applicable** — this model has no external key source |
| 5. repeating key word | **absorbed** — any word of length `p` is one point in Z26^p, so `PALIMPSEST` (p=10) and `ABSCISSA` (p=8) are covered as special cases and need no separate speculative test |
| 6. tableau row labels | **absorbed** — relabelling rows permutes which key value is selected, which an arbitrary key value already ranges over |

## 4. Motivation

This is the hybrid the section sequence actually points at, and the gap between two
existing experiments:

- K1 and K2 are periodic polyalphabetic substitutions over KRYPTOS-mixed components, with
  repeating keys of length **10** and **8**. K3 is a route/columnar transposition Sanborn
  implemented himself. Scheidt describes a fourth, different, better-masking process.
- **EXP-003** tested exactly this gate — transposition plus a short periodic key, both
  composition orders — but only over the affine-mod-97 family (9,312 permutations) and
  small route families.
- **EXP-033** expanded the transposition frontier enormously (all keyed columnar widths
  2–11 with every column order, rectangle routes at every width, ragged engraving-grid
  routes) but composed it with **one fixed monoalphabetic substitution**.

The intersection — the large transposition family composed with a short periodic
polyalphabetic layer — is untested. A period range of **2–23** brackets both known Kryptos
key lengths with margin.

## 5. Declared transposition families

Reused unchanged from `k4lib/transpositions.py`, which is already self-tested against
reference implementations and independently re-derived by `audit/verify_exp033.py`:

- **T1 — keyed columnar**, widths `w`, all `w!` column orders, columns read top→bottom or
  bottom→top, orientation `σ` or `σ⁻¹`: 4·Σ w! cases.
- **T2 — unkeyed rectangle routes**, all widths 2–96, thirteen named routes, both
  orientations.
- **T3 — routes on K4's corrected ragged engraving grid** (row 25 columns 28–31, rows
  26–28 columns 1–31), both orientations.

## 6. Declared scope, and the compute asymmetry stated in advance

| | transposition family | periods | conventions | cases |
|---|---|---|---|---|
| **Order A** | T1 widths **2–10** (16,151,648) + T2 + T3 | 2–23 | 12 | ≈ 4.26 × 10⁹ |
| **Order B** | T1 widths **2–8** (184,928) + T2 + T3 | 2–23 | 12 | ≈ 4.88 × 10⁷ |

Order A's residue partition is σ-independent, so all 22 periods share one pass over the
family. Order B's grouping is σ-dependent and costs roughly `p` reductions per case per
period, which is why its family is narrower. **This asymmetry is declared now, with its
reason, and is not a result-dependent choice.** Widths 11+ for order A and 9+ for order B
are outside scope and will be reported as such, not as eliminated.

## 7. Decidability table, computed before execution

Because both crib runs are contiguous, occupied residue classes saturate quickly and the
constraint count stays high across the whole declared period range. Constraints
= 24 − |{j mod p : j a crib position}| for order A:

| p | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| constraints | 22 | 21 | 20 | 19 | 18 | 17 | 16 | 15 | 14 | 13 | 12 | 11 | 11 | 9 | 8 | 7 | 7 | 9 | 11 | 11 | 9 | 7 | 5 |

Chance survival is `26^-c`, from `1.25×10⁻¹⁰` at the weakest declared period (p = 17, 18,
23: 7 constraints) to `7.4×10⁻³²` at p = 2.

**Preregistered decidability rule.** A (period, family, order) combination is admitted to
the elimination only if `N · 26^-c < 0.01`, where `N` is that family's case count and `c`
the constraint count. Combinations failing this are reported **UNDECIDABLE-BY-SIZE** and
excluded. Under this rule the whole declared range p = 2–23 is admissible for both orders;
**p = 24 is excluded in advance** (5 constraints, expected chance survivors 1.36 at
N = 16.15 M), which is precisely why the range stops at 23.

For order B the constraint count varies per case. It is computed **per case, over every
constrained position, before any verdict is formed** — the EXP-034 invariant — and cases
falling below 7 constraints are reported UNDECIDED rather than counted.

## 8. Equivalence and deduplication

- Composition order is **not** deduplicated: orders A and B are inequivalent, verified by
  construction rather than assumed.
- Under order A, feasibility depends on σ only through the 24-letter word
  `(C[σ(j)])_{j∈crib}`, so permutations agreeing on the crib positions are the same case.
  This is materialised and deduplicated for T2 and T3; for T1 at 16 M cases it is reported
  as a count caveat rather than materialised, and **case counts are not counts of
  independent tests**.
- Identical permutations arising in more than one declared family are deduplicated by
  hashing the permutation tuple, as in EXP-033.

## 9. Exact success criterion and failure statement

A case is **FEASIBLE** iff no two constrained positions in the same residue class force
different key indices. Nothing is scored; there is no threshold and no language model.

**Failure statement.** If no admissible case is feasible: *K4 is not any transposition from
the declared families composed with a periodic polyalphabetic substitution of period 2–23
over STD/KRYPTOS plaintext and ciphertext components under the three committed combiners,
in either composition order.* Scope is exactly that, conditional on the public cribs. It
does not touch keyed columnar widths above the declared limits, aperiodic or
progressive keys, period ≥ 24, non-shift combiners, component alphabets outside
{STD, KRY}, double transposition, fractionation, or any physically-aligned model.

## 10. Controls

- **Planted positives**, at least 60, spanning both orders, every declared family, a range
  of periods and all 12 conventions: a random σ, a random key in Z26^p (including a key
  with repeated values), and a plaintext carrying the real crib letters, synthesised with
  independent arithmetic. The detector must report FEASIBLE at the planted (σ, p,
  convention) **and** recover a key agreeing with the plant on every constrained residue
  class.
- **Adversarial negatives that actually intersect constraints.** For each plant, one
  ciphertext letter is corrupted at a position whose residue class contains **at least two**
  constrained positions, so the corruption is *capable* of flipping the verdict. Cases with
  no such class are reported "not counted" and never counted as passes. This follows the
  EXP-033/034/035 lesson.
- **Period-discrimination control:** a case planted at period `p` must be found infeasible
  at some other admissible period, otherwise the period parameter is not doing work; the
  observed discrimination rate is reported rather than asserted.

## 11. Independent verifier

`audit/verify_exp036.py`, importing neither the experiment nor `k4lib`. It rebuilds the 12
conventions from first principles, rebuilds permutations by **explicit grid simulation**
(not the closed-form column arithmetic the experiment uses), recomputes the decidability
table, re-decides every declared-feasible case plus an exhaustive recheck of the small
widths and a pseudorandom sample of the large ones, asserts that constraint counts are
**verdict-independent**, asserts that no admissible combination violates the
`N·26^-c < 0.01` rule, and replants its own positives so a rubber-stamp verifier is
excluded.

## 12. Prohibited post-hoc expansions

No widening of widths, periods, conventions or families in response to a result. No
progressive, drifting or reset key. No per-block or position-modulated key. No relaxation
of the consistency criterion into a score or an "all but one crib" rule. No lowering of the
decidability threshold. No promotion of a near-miss without a new, separately motivated
preregistration. If a feasible case appears it is recorded as a hypothesis only: it fixes
at most `p` key values and says nothing about the other 73 plaintext positions.
