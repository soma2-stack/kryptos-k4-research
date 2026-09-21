# Checkpoint N — reproducibility repaired; Porta reduced, then eliminated

Branch `claude/k4-post-j`. Base for this checkpoint:
`e1a2ee2c80928332fae85a06587197f39e7650f8` (verified on pull). `main`,
`codex/k4-continuation` and `claude/dreamy-archimedes-79k6u0` untouched.
**K4 remains unsolved.** No plaintext candidate, no verifier submission, no claimed
mechanism.

## 1. EXP-036 reproducibility repair — and it was broader than reported

The finding is correct and the defect was real. Auditing it showed it was **not confined to
EXP-036**: `.gitignore` ignored `results/*` with exceptions only for EXP-030 and EXP-031, so
**EXP-032, EXP-033, EXP-034, EXP-035 and EXP-036 were all untracked**, and six verifier
scripts — including `verify_geometry_correction.py` — were unrunnable from a clean checkout.
Every one is fixed.

**Provenance established before committing, not assumed.** `results/exp036/summary.json`
shares an mtime with the final run log (the same process writes both at the end), and every
figure in it appears verbatim in that log: 4,313,878,272 total, 4,264,035,072 order A,
48,820,992 order B, 1,022,208 T2/T3, 4,091,520 undecided, 0 feasible, controls 72/72. It is
the original artifact, not reconstructed from the checkpoint prose.

**Two artifacts were bulk output and were repackaged losslessly.** EXP-034 and EXP-035 wrote
single summaries of 1.28 MB and 8.98 MB. Each was split into a small `summary.json` plus
`rows.jsonl.gz` (29 KB and 148 KB, following the EXP-030 `cases.jsonl.gz` precedent), the
original sha256 recorded inside the new summary, and **the round trip checked to reproduce
the original object exactly**. Nothing was recomputed. The two verifiers now load the rows
back from the gz and assert the row count; the two experiments write the same split layout
on future runs so a rerun reproduces the committed shape.

`.gitignore` gained narrow per-file exceptions in the established style. No candidate dumps.

### Clean-checkout verification

From a `git worktree` containing only committed files:

| verifier | result |
|---|---|
| `verify_exp036.py` | **17/17** |
| `verify_exp035.py` | **14/14** |
| `verify_exp033.py` | **15/15** |
| `verify_exp032_034.py` | **15/15** |
| `verify_geometry_correction.py` | **25/25** |
| | **86/86, zero FAIL lines** |

The clean verification **agrees with the earlier results**, so this is a reproducibility
repair and **no cryptanalytic conclusion changes**.

## 2. The "all 36 experiments share one combiner" claim — narrowed

Checkpoint M's sentence is **too broad and is withdrawn**. Checkpoint M is not rewritten;
`docs/combiner-coverage-matrix.md` supersedes it.

Machine audit: **22 of 36** experiments call `all_conventions()`; **14 do not**. EXP-033 in
particular decides *any* fixed `A–Z → A–Z` table; EXP-012/013 are fractionation and Trifid;
EXP-019's unicity bound survives any combiner at all.

**Corrected statement:** the shift-combiner assumption binds the **keystream and periodic
polyalphabetic** line of work, not the substitution, transposition, fractionation or
structural results.

## 3. Combiner coverage matrix

Full experiment-by-experiment table in `docs/combiner-coverage-matrix.md`, classifying each
by transformation class, whether it calls `all_conventions()`, whether its result is
conditional on STD/KRY component indexing, how its table is constrained, and whether a new
combiner would escape it. Three conclusions:

1. **A new combiner cannot rescue a monoalphabetic model** — EXP-033 already decided every
   fixed table, whatever its historical name.
2. **A new combiner cannot rescue a single-symbol-lookup keystream** — EXP-030/032/034/035
   decide any function `f` of one source symbol or index. What they do *not* absorb is the
   plaintext and ciphertext **component alphabets**.
3. **The live gap is periodic tables that are not shifts** — the EXP-003/EXP-036 line.

## 4. Quagmire — reduced, and rejected as duplicate

Comparing the **full 26-setting families as sets** (not individual mappings):

| | reduces to | verdict |
|---|---|---|
| Quagmire I (keyed plain, straight cipher) | `Convention(P=KRY, C=STD, vigenere)` | **duplicate** |
| Quagmire II (straight plain, keyed cipher) | `Convention(P=STD, C=KRY, vigenere)` | **duplicate** |
| Quagmire III (same keyed alphabet both sides) | `Convention(P=KRY, C=KRY, vigenere)` | **duplicate** |
| Quagmire IV (two *different* keyed alphabets) | needs a second keyword | **not covered, but unevidenced** — no primary source names one; free it is 26! and unfalsifiable |

The Quagmire indicator only relabels which key *value* is used at each position, and EXP-036
decides the key existentially over all of Z26^p, so any fixed key-letter relabelling is
already absorbed. Running Quagmire I–III would duplicate billions of cases. **Gronsfeld**
likewise reduces to a digit-restricted Vigenère key — a strict subset of an existential key.

*(A first version of this check used a dict keyed by mapping, which collapses mappings
shared by several conventions and returned an arbitrary representative; it reported a
spurious "False" even for plain Vigenère. Corrected to set-equality of whole families.)*

## 5. Porta — equivalence audit, including a correction to my own proof attempt

Of the **207 distinct mappings** from 3 combiners × 4 evidenced component pairs × 26 keys,
exactly **one** Porta row appears: row 0 = `variant_beaufort/P=STD/C=STD/k=13`. **Rows 1–12
are not representable.** Same result with Porta built on the KRYPTOS ordering.

**But the relabelling question does not go my way, and I record that rather than the
convenient version.** I expected cycle type to prove non-collapse. It does not: every
`Porta_n ∘ Porta_0⁻¹` has cycle type (13, 13), exactly like an even shift — and the set is
**closed under composition**, a Z₁₃ acting regularly on two orbits of 13, which is precisely
the structure of `{Shift_0, Shift_2, …, Shift_24}`. The two permutation groups are therefore
conjugate, so bijections φ, ψ with `ψ ∘ Porta_n ∘ φ = Shift_{2n'}` **do exist**.

> **Exact statement: Porta is a shift family under *some* pair of mixed alphabets — just not
> under any of the four evidenced STD/KRYPTOS pairs.** Testing it tests one precommitted,
> historically documented alphabet pair, not a new algebraic class.

**Documentary grade: structural / historical candidate only.** No Sanborn or Scheidt evidence
says K4 uses Porta, and none is claimed.

## 6. Porta decidability — derived from the table family, not assumed

Porta sends **every** letter to the opposite half. So for a pair `(p, c)`: same half → **no**
row realises it at any key; opposite halves → **exactly one** row. Verified: exactly 338 of
676 letter pairs are realisable, each by one row.

**16 of the 24 crib pairs lie in the same half**, under both orderings. A single such pair
kills the family.

For the composed family the parity condition becomes a filter on σ. From K4's own half
counts the mean cross-half probability is 0.5021 (STD) / 0.4768 (KRY), so
`P(a random σ passes all 24) ≈ 6.61×10⁻⁸` / `1.91×10⁻⁸`. **The null is
`(cross-half)²⁴ × 13⁻ᶜ`, not `13⁻ᶜ`** — as required, derived rather than assumed.

## 7. EXP-037 — preregistered before implementation, result NEGATIVE

| | |
|---|---|
| **DIRECT periodic Porta (no transposition)** | **IMPOSSIBLE at every period 1–23, every key, both orderings — decided by inspecting 24 letter pairs, with no search at all** |
| **COMPOSED cases decided** | **1,486,129,728** |
| permutations passing the cross-half filter | **0** (expected ≈ 1.07 under the null; Poisson P(0) ≈ 0.34, so unremarkable) |
| **FEASIBLE** | **0** |

**An honest note on what did the work.** The composed elimination came almost entirely from
the structural half-parity fact; the row-consistency machinery never fired on a real case.
The controls, not the sweep, are what demonstrate that machinery works.

**Controls:** 80/80 planted positives with the row schedule recovered, **exercising all
13/13 Porta rows** and including keys with repeated rows; 80/80 adversarial, every one
capable of flipping the verdict (zero uncounted); **74/74 period discrimination** with 6
degenerate plants excluded — a key taking one row across all constrained positions is
consistent at every period by construction, so counting those as failures would be a wrong
control, not a finding; **wrong-table-family both ways, 80/80 and 80/80** — a Vigenère plant
is rejected by the Porta detector and a Porta plant by a shift detector.

**Independent verification:** `audit/verify_exp037.py` imports neither the experiment nor
`k4lib`, uses no numpy, and **builds the 13 tables from the documented definition by a
deliberately different construction** (explicit half lists rather than index arithmetic).
**31/31 checks pass**, including independent reciprocity and zero-fixed-point checks, the
338/676 realisability count, re-derivation of the cross-half null from the ciphertext,
320,896 cases re-decided exhaustively for widths 2–6, 8,000 sampled at widths 7–10, and
replants exercising all 13 rows in both composition orders.

### Exact model-limited conclusion

**K4 is not a periodic Porta cipher over the STD or KRYPTOS ordering at any period 1–23,
alone or composed with any transposition from the declared EXP-036 families, in either
composition order.** Not touched: Porta over other orderings, aperiodic or reset row
schedules, transpositions outside those families, other reciprocal-table systems.

## 8. EXP-036's scope, preserved verbatim

Unchanged and deliberately narrow: *periodic polyalphabetic substitution of period 2–23 over
STD/KRY plaintext components and STD/KRY ciphertext components under Vigenère / Beaufort /
variant-Beaufort combiners, composed with the declared transposition families in the declared
widths and orders, gave zero feasible cases.* **This is not "periodic polyalphabetic ciphers
are eliminated." They are not.**

## 9. Surviving architectures, re-ranked

| rank | architecture | change | falsifiable now? |
|---|---|---|---|
| 1 | A specific named **full-26 fractionating** construction (fractionate on one grid, recombine on another) | **promoted** — EXP-012's coverage argument kills 5×5 and 6×6-with-digits but not this, and it is the classical answer to "mask English statistics" | Yes, once the construction is named before searching |
| 2 | **Double transposition**, or keyed columnar width ≥ 12 from a precommitted key family | unchanged | Yes, as a small precommitted family |
| 3 | Long key from a still-unidentified external source | unchanged | No — needs evidence naming a source |
| 4 | Aperiodic / progressive / reset key schedules over the EXP-033 transposition family | unchanged; compute constraint density first — resets destroy the residue collisions | Marginal |
| 5 | Quagmire IV, or any two-different-keyed-alphabet system | **new entry, but unevidenced**; free alphabets are unfalsifiable | Only with a precommitted second keyword |
| 6 | Physical panel-alignment models | parked | Blocked on Request 4 / AAA Box 6 Folder 10 |
| 7 | Clock-as-index, semantic inner layer | unchanged | No — no mechanism stated |
| — | **Named classical "new combiners"** (Gronsfeld, Quagmire I–III, Porta) | **closed this session**: reduced to duplicates or eliminated | — |

The combiner direction I promoted at Checkpoint M is now largely spent: the reduction rule
turned most candidates into duplicates, and the one genuine survivor died on a structural
parity fact in a single line of arithmetic.

## 10. Highest-information next step

**Name a specific full-26 fractionating construction, then decide it.** The requirement, from
EXP-012, is that the output alphabet must cover all 26 letters — K4 contains `J` at positions
40, 51 and 81 — which kills 5×5 schemes and 6×6-with-digits. A construction that fractionates
on one grid and **recombines on a different 26-cell reading** escapes that argument.

Discipline first, before any number is assigned: state the grid, the fractionation rule and
the recombination rule as equations; check by the reduction rule that it is not a relabelled
version of something already decided; then compute the crib constraint density and the null
*from the construction itself*, exactly as the Porta null was derived — not by analogy. If
the cribs cannot constrain it, it does not get an experiment.

## 11. External evidence

Unchanged: **Request 4 open** (AAA Series 3, Box 6 Folder 10, `Pre-Production and Notes,
1990–1999`, for a punch layout or fabrication drawing; secondarily the LOC Highsmith TIFF at
full resolution). Requests 1 and 5 fulfilled. Requests 2 and 3 carried forward, lower
priority. Nothing is blocked on any of them.

## 12. Reproduce this checkpoint only

```sh
python audit/verify_exp036.py          # now runnable from a clean checkout
python experiments/exp037_porta.py     # ~1 min, needs numpy
python audit/verify_exp037.py          # pure standard library, builds the tables itself
```
