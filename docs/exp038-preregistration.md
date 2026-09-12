# Preregistration — EXP-038: second-order affine stateful recursive key schedules

Committed **before** the real K4 search is implemented or executed. Branch
`claude/k4-post-j`, base `a34f11d637d31b43e7c31d14cb20804dcd2e2c80`.
K4 remains unsolved. No external verifier. No alleged plaintext, purported solution, or K5
material.

The family-structure figures below were computed **without touching the real target
vectors** — only the recurrence family's own algebra — precisely so that the gate is decided
before the experiment can see its answer.

## 1. Exact inputs

| input | sha256 |
|---|---|
| `data/k4.json` | `d710d758e92abc7c4ac87da189baef936ee97c18ba1636c2ee0021ebe673f4e5` |

*(Correction, committed before execution: the first draft of this file carried the
pre-Checkpoint-P hash `e3b18a93…`. `data/k4.json` changed when its crib-provenance note
was updated by the public-verification commit; the ciphertext, crib text and crib indices
are byte-identical. The hash above is the current file.)*

Ciphertext pinned by `k4lib.data` to
`eea813570c7f1fd3b34674e47b5c3da8948026f5cefee612a0b38ffaa515ceab`.

**Public crib constraints, public-source verified (Checkpoint P), not to be slid:**
`EASTNORTHEAST` at zero-based `[21,34)`, `BERLINCLOCK` at `[63,74)` — 24 positions:
`21…33` and `63…73`.

## 2. Exact recurrence equations, modulus and alignment

All arithmetic **mod 26**. Key values range over the **full Z26**, not a digit subset — that
is the specific gap Gromark's rejection left open.

- **F1 — homogeneous order 2:** `k[n] = a·k[n-1] + b·k[n-2] (mod 26)`,
  parameters `a, b, k[0], k[1] ∈ Z26`. Raw space `26⁴ = 456,976`.
- **F2 — affine order 2:** `k[n] = a·k[n-1] + b·k[n-2] + c (mod 26)`,
  parameters `a, b, c, k[0], k[1] ∈ Z26`. Raw space `26⁵ = 11,881,376`.

**Inclusion decision, fixed now: EXP-038 contains F1 and F2 together.** F1 is the `c = 0`
slice of F2 and is reported as a labelled subfamily. This is decided in advance precisely so
that a negative on F1 cannot be followed by "add `c`" as a rescue step. The gate in §5 shows
F2 is still overwhelmingly constrained, so including it costs nothing in falsifiability.

**Initial-state alignment, frozen:** `k[0]` is the key value at **K4 position 0** and `k[1]`
the key value at **K4 position 1**, zero-based, message-aligned. There is no primer offset, no
warm-up, and no separate seeding phase.

## 3. Component conventions

The 12 committed conventions from `k4lib.conventions.all_conventions()`: three combiners
(Vigenère, Beaufort, variant Beaufort) × plaintext indexing alphabet ∈ {STD, KRY} ×
ciphertext indexing alphabet ∈ {STD, KRY}. **No new alphabets. No table families.** The 12
forced-key target vectors are distinct, so no convention collapses into another.

## 4. Duplication audit — computed, not assumed

**Not covered by prior work.** EXP-006 makes the key a function of *position*; EXP-008 and
EXP-034 derive it from *plaintext or ciphertext* symbols; EXP-036 covers *periodic* schedules.
A key evolving from its own prior values is none of these. Gromark's direct form died on an
alphabet gate (legal digits 0–9 cannot realise enough crib pairs), not on the recurrence.

**Overlaps that exist and are excluded from the new-family count:**

| overlap | locus | size |
|---|---|---|
| EXP-006 **progressive** (arithmetic progression `k0 + n·d`) | exactly the characteristic polynomial `(x−1)² = x² − 2x + 1`, i.e. `(a,b) = (2,25)` | 17,576 unique streams |
| EXP-006 **polynomial** of degree ≥ 2 | **not reachable**: order 2 admits only `(x−1)^≤2`, so degree ≤ 1 | — |
| EXP-036 / EXP-006 **periodic** | any parameter tuple whose **97-prefix** is exactly periodic with some `p ≤ 23` | **1,701,518 unique streams** |

Measured family structure:

| quantity | F1 | F2 |
|---|---:|---:|
| raw parameter tuples | 456,976 | 11,881,376 |
| unique 97-key streams | — | **7,585,006** (collapse 1.57×) |
| unique 24-position crib projections | **172,375** | **4,481,750** (collapse 2.65×) |
| streams tagged `ALREADY COVERED` (97-prefix periodic, `p ≤ 23`) | — | 1,701,518 |
| **genuinely new streams** | — | **5,883,488** |

The `ALREADY COVERED` criterion is exactness of the **97-prefix**, per the rule that a
recurrence must not be discarded merely because its infinite state machine is eventually
periodic. A stream is tagged only if it *is* a period-`p ≤ 23` key over the message.

Because Z26 is not a field, distinct tuples collide: 11.9M tuples give 7.59M streams and only
4.48M distinct crib projections. **Feasibility is decided on the projection**, and counts are
reported at all three levels rather than treating tuples as independent tests.

## 5. Decidability gate — exact, from the family itself

For fixed `(a,b,c)` the recurrence is linear in the state:
`k[n] = A_n(a,b)·k[0] + B_n(a,b)·k[1] + c·D_n(a,b) (mod 26)`, verified against direct
iteration on 300 random tuples with zero mismatches. So the 24 crib constraints are a
**24 × 2 linear system over Z26** in `(k[0], k[1])` for each `(a,b,c)` — solved exactly, not
searched.

The null is **not** `26^(params − constraints)`. It is computed from the realised image:

- distinct crib projections realisable by F2: **4,481,750**
- `|Z26^24| = 26²⁴ ≈ 9.107 × 10³³`
- `P(a uniform random 24-vector is realisable) = 4.921 × 10⁻²⁸`
- **expected survivors over the 12 convention targets = 5.906 × 10⁻²⁷**

**No convention is underdetermined:** 24 constraints against at most 5 parameters, and each
crib block alone overdetermines the 2-dimensional state (block 1 has 13 positions, block 2
has 11, against 2 unknowns for fixed `(a,b,c)`). Per-block feasibility is therefore also
reported as a diagnostic — a family feasible on one block but not the other is more
informative than a bare zero.

**Gate: PASSED.** The expected survivor count is 27 orders of magnitude below one, so a zero
result is a genuine elimination rather than an expected outcome.

## 6. Success criterion and failure statement

A case is **FEASIBLE** iff the recurrence reproduces **all 24** forced key values exactly.
Nothing is scored; there is no language model and no threshold.

**Failure statement.** If zero parameter tuples are feasible: *no full-Z26 second-order affine
self-evolving keystream, under the 12 committed shift conventions, message-aligned and without
reset or transposition, satisfies the 24 published K4 positional cribs.*

**Interpretation is limited to exactly that.** It will **not** be reported as "recursive keys
are eliminated", "stateful systems are eliminated", "K4 is not autoregressive", or "K4 must use
an external source". Higher-order, nonlinear, reset, externally seeded and other state machines
remain open.

## 7. Controls

**Planted positives** must exercise, at minimum: `a = 0`; `b = 0`; `a = 1`; `b = 1`;
non-unit coefficients; even coefficients; odd coefficients; repeated initial values;
`k[0] = 0`; `k[1] = 0`; nontrivial affine `c`; a recurrence with a short orbit; a recurrence
with a long orbit. Each plant synthesises a ciphertext through the same convention and must be
detected FEASIBLE at the planted tuple with the state recovered.

**Controls that cannot affect the constrained positions are not counted.**

**Adversarial controls:** for each plant, alter a forced key value at a crib position that
genuinely participates in the constraint set, and require the verdict to flip. Every
adversarial control must be capable of changing the verdict *by construction* — the lesson
from EXP-034/035.

## 8. Independent verifier

`audit/verify_exp038.py` must:

- **not** import the production recurrence generator and **not** import `k4lib`;
- contain or independently load the ciphertext and crib definitions;
- independently implement STD and KRY indexing and all three combiners;
- independently generate the recurrence **by direct iteration**, not by the closed form the
  experiment uses for its linear solve — so an error in that algebra cannot hide;
- exhaustively re-decide **F1** (456,976 tuples × 12 conventions);
- re-decide **F2** exhaustively if affordable, otherwise by a deterministic strided
  certificate plus independent recheck of every feasible hit and every control, with the
  reason stated;
- check the duplicate accounting and the period-overlap accounting.

## 9. Prohibited post-hoc variants

No order-3 recurrence, resets, a boundary at `BERLINCLOCK`, reversed recurrence, modulus 25,
27 or 10, multiplicative or other nonlinear terms, ciphertext feedback, plaintext feedback,
transposition, or new alphabets. Any of these requires a separate, independently motivated
preregistration. **EXP-038 answers one clean question.**

## 10. If there is a hit

A crib fit is **not** a solution. Every hit will be: reproduced independently; expanded to the
full 97-value keystream; used to decrypt all 97 characters; reported with the complete
plaintext shown; assessed for coherence in the **unconstrained** positions; counted against the
preregistered null; and left with its parameters **unmodified**. No parameter optimisation
follows a hit. Only a deterministic, coherent 97-character decryption under these frozen
parameters would become a serious candidate, and even then nothing is submitted anywhere.
