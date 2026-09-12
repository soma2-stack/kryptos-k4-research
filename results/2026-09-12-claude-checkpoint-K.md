# Checkpoint K — position preservation abandoned; three exact eliminations

Branch `claude/k4-post-j`, from Codex Checkpoint J head
`6134fcc41254a31cc3131753826e1409224e5ecc`. `main`, `codex/k4-continuation` and
`claude/dreamy-archimedes-79k6u0` are untouched; no history merged or rewritten.
**K4 remains unsolved.** No plaintext candidate, no verifier submission, no claimed
mechanism.

## 1. What I audited

Read Checkpoints I and J, `docs/codex-audit.md`, EXP-029/030/031 and their verifiers, the
frozen Checkpoint-J data, and all five Perplexity handoffs. Codex's audit found two real
defects in my own earlier work and I accept both: **EXP-029 wrapped modulo 120 although
its text promised windows inside a known arc**, so its two 7/24 maxima are one stream
described twice and its Poisson figure was not calibrated for a duplicated dependent
family. The zero-hit negative stands on the non-wrapping subset; the significance reading
is withdrawn and the 7/24 alignments are not pursued. Finding 6 is also fair: my
Checkpoint-H dating rested on banner content and an in-commit freeze declaration, which
is evidence but not independently timestamped chronology.

I treated the Perplexity documents as external research and checked what could be checked
locally rather than promoting reporting into fact.

**Geometry, verified not accepted.** The NSA DOCID 4145037 row placement is confirmed
against the repository ciphertext: the three quoted 31-character rows equal `K4[4:35]`,
`K4[35:66]`, `K4[66:97]` exactly; row 25 is 31 characters ending `OBKR`;
32 + 27×31 = 869. The isolated-`OBKR` model is wrong and stays retired.

**But a correction to how much that buys — recorded before running anything, and
verified programmatically in EXP-032:** *no crib lies at K4 positions 0–3, and for i ≥ 4
the corrected and the old isolated-`OBKR` column maps are identical.* So the geometry
correction **cannot change the outcome of any crib-constrained position- or
column-indexed model**. It matters only for (a) models using the characters physically
*above* K4, (b) transpositions on the ragged engraving grid, (c) claims about positions
0–3. Anyone citing the correction as a reason to revisit the keystream results is
mistaken, and I nearly made that mistake myself.

Established corrections kept: CET is 120 letters and the 97 coincidence stays withdrawn;
ATHEN is present between SOFIA and NIKOSIA; upper=northern/lower=southern withdrawn;
membership does not give order; no modern-clock back-projection.

## 2. The model-selection decision

The decisive observation is structural: **every experiment in this repository through
EXP-031 assumes the key is a function of message position.** The justification for that —
EXP-021's K4/K5 correspondence argument — is exactly what `docs/codex-audit.md` finding 7
withdraws as overbroad. With it withdrawn, the whole class of architectures that *move*
the plaintext is reopened, and nothing had tested one except the affine-mod-97 family of
EXP-003/016.

So I attacked two directions that are genuinely different from EXP-001…031, and in both
I used the trick that makes Codex's EXP-030 strong: **do not enumerate the substitution
or the lookup — decide it exactly by consistency.** That removes the free parameter that
would otherwise make these families unfalsifiable.

Preregistrations were committed before implementation: `9c06a54` (EXP-032, EXP-033) and
the EXP-034 preregistration commit. Each states inputs and hashes, the model, parameter
ranges, dedup rules, the exact criterion, the failure statement, controls, the intended
verifier, and prohibited post-hoc expansions.

## 3. EXP-032 — key as an arbitrary function of engraving column

`k[i] = f(col(i))`, `f : {1..31} → Z26` **any** function, under the verified geometry.
`f` is never enumerated; all 26³¹ functions are decided by consistency, and an arbitrary
`f` absorbs every key alphabet, so key alphabet is not a parameter. **12 cases**, one per
committed convention, each carrying exactly **2** constraints — the crib set has exactly
two column collisions, column 29 = {32, 63} and column 30 = {33, 64}, fixed before any
verdict.

**Result: 12/12 contradictions, 0 feasible.** Controls 12/12 planted (with `f` recovered)
and 12/12 adversarial. Chance-feasible expectation over all 12 cases: 0.018.

Scope: eliminates an infinite family from two constraints, and is strictly more general
in `f` than EXP-006's periodic and line-reset results while strictly narrower in
indexing. Reported honestly alongside it: a key that is a function of **(row, column)**
is **vacuous** here — every crib position has a unique (row, column) pair, so the cribs
yield zero constraints. No such model is claimed eliminated.

## 4. EXP-033 — arbitrary monoalphabetic substitution ∘ declared transposition

`C[i] = S(P[σ(i)])`, `S : A–Z → A–Z` **any** function, `σ` from a declared family.
Dedup fixed in advance: a monoalphabetic substitution commutes with a transposition, so
composition order is not a parameter; orientation (`σ` vs `σ⁻¹`) is.

Declared family: **F1** keyed columnar transposition, widths 2–11, **all w! column
orders**, columns read top→bottom and bottom→top, both orientations — 175,818,848 cases.
**F2** unkeyed rectangle routes at every width 2–96 (columns, boustrophedon, diagonals,
eight spirals). **F3** routes on K4's corrected ragged engraving grid — *this is the
independent reproduction and formalisation of the uncommitted supervisory scratch
result*, implemented from the geometry rather than from the scratch description, and
labelled so its verdict reads separately.

Falsifiability computed **before** running, from K4's own letter frequencies: the 24 crib
positions carry 13 distinct plaintext letters, Σ(m−1) = 11 equality constraints plus
injectivity, so a random permutation is feasible with probability **6.6 × 10⁻¹⁷**. Over
the declared family the expected number of chance survivors is **1.2 × 10⁻⁸**. The family
is therefore not vacuous — EXP-011's "transposition plus a free alphabet is vacuous"
verdict applies to a free *per-position* alphabet, not to one fixed substitution.

**Result: 175,820,784 cases decided, 0 FEASIBLE-BIJECTIVE, 0 FEASIBLE-FUNCTION.**
1,936 distinct small permutations after deduplicating 548 duplicates.

Controls: 39/39 planted positives across F1/F2/F3 with the substitution recovered on
every constrained letter; 39/39 adversarial corruptions rejected; 39/39 adversarial
wrong-permutation cases rejected (the first draft of this control swapped random slots
and therefore tested nothing — it was rebuilt to swap two crib-constrained slots whose
ciphertext letters differ); a deliberately non-injective plant found under
FEASIBLE-FUNCTION and correctly rejected under FEASIBLE-BIJECTIVE.

Independent verification — `audit/verify_exp033.py`, importing neither the experiment nor
`k4lib`, rebuilding permutations by **explicit grid simulation** instead of the closed-form
column arithmetic: **15/15 checks pass**, including exhaustive re-decision of widths 2–7
(23,648 cases), a 4,000-case F1 sample, coverage equal to Σw!×4 for every width, the
chance figure recomputed, and replanted positives so a rubber-stamp verifier is excluded.

**What this buys beyond a statistic.** K4's IoC (0.03608) already disfavoured this whole
architecture at about z = −3.9, but the audit is right that a low IoC does not prove no
English plaintext exists. The cribs now settle it *inside this family* with no
distributional assumption at all.

**Scope.** Not eliminated: keyed columnar widths ≥ 12, keyed routes outside the family,
double transposition, any polyalphabetic composition, fractionation, or substitution with
nulls or length change. Case counts are not counts of independent tests.

## 5. EXP-034 — text-dependent keys as arbitrary functions

`k[i] = f(S[i − L])`, `f` any function, decided by consistency. EXP-008 had eliminated
this family only in **parameter-linear** form (`a·S[i−L] + b`, two-tap, drift); this is
the same generalisation EXP-030 applied to EXP-029. 8 declared sources (ciphertext
forward, reversed, five decimations, plaintext autokey) × lags 1–96 × 12 conventions =
**9,216 cases**.

A threshold was preregistered: cases with ≤ 3 usable constraints are **UNDECIDED** and
excluded from any elimination.

**Result: 2,676 decided, 0 feasible; 6,540 UNDECIDED for lack of constraint.** Decided
cases carry 4–12 constraints (72 cases at 12, chance survival 1.0 × 10⁻¹⁷). Controls
120/120 planted with `f` recovered, 114/114 adversarial.

**A bug I found and fixed in my own first implementation, which matters more than the
result.** The first draft returned on the *first* contradiction, so the constraint count
it reported depended on the verdict — contradicting cases reported tiny counts and were
misfiled as UNDECIDED. It claimed only 3 decidable cases out of 9,216. Direct computation
showed the real counts are 8–12, the early return was removed, and the verifier now
asserts specifically that the constraint count is independent of the verdict. A
verdict-dependent difficulty metric silently converts strong negatives into "we cannot
tell", and it is exactly the failure a separate verifier exists to catch.

`audit/verify_exp032_034.py` re-derives the conventions, geometry, sources and lags from
first principles and re-decides **all 9,216 cases** plus all 12 EXP-032 cases:
**15/15 checks pass**, every verdict and constraint count agreeing.

## 6. Surviving architectures, ranked

| rank | architecture | why it survives | falsifiable now? |
|---|---|---|---|
| 1 | Polyalphabetic with a long, high-entropy key from an **unidentified** source | K1/K2 precedent; the flat IoC demands flattening; unicity bounds recovery at ~66–76 letters of key entropy | **No** — progress needs evidence identifying the source, not more search |
| 2 | Substitution ∘ **keyed** transposition with a key from the published Kryptos keyword corpus, or width ≥ 12 | EXP-033 kills widths ≤ 11 exhaustively but cannot reach 12! and beyond | **Yes**, if the key family is motivated rather than exhaustive — small and cheap |
| 3 | Fractionation whose output alphabet is the full 26 (fractionate on one grid, recombine on another) | EXP-012's coverage argument kills 5×5 and 6×6-with-digits, not this | Partly — many parameters; needs a declared, narrow variant |
| 4 | Two-tap or position-modulated text-dependent keys | EXP-034 kills one tap at one lag with any `f` | Yes, but constraint counts will fall fast — check decidability first |
| 5 | Clock as **index/state** rather than key source | Never given a concrete mechanism | Not yet — needs a mechanism before it is an experiment |
| 6 | Semantic/encoded inner layer under a simple outer cipher | Scheidt distinguishes the cipher from the meaning | No — untestable without the codebook |

Rank 1 is where I would put the probability mass, and it is precisely the rank that
cannot be advanced by searching. That is the honest state of the problem.

## 7. Highest-information next step

**It is an evidence request, not a search** — and it is cheap, because the document is a
published PDF.

`docs/external-evidence-requests.md` Request 1: the **NSA cipher-side transcription of
rows 1–24** (DOCID 4145037, or the 4145036 slides). The corrected geometry places K4's
rows 26–28 directly beneath 24 rows of *known* ciphertext in the same 31 columns. That
makes one architecture testable that no amount of local work can reach: **a key drawn
from the characters physically above each K4 character** — (row − k, same column) for
k = 1…24, or a column-major reading of the panel above. It is parameter-free, finite
(~1,200 exact cases), falsifiable by the 24 public cribs, and motivated by the documented
division of labour in which Sanborn did the physical and visual encoding himself.

This repository holds **no verified K1–K3 ciphertext** — `data/mask_sources.json` has only
`verified: false` plaintexts. `www.nsa.gov` and `media.defense.gov` were re-tested this
session and both return `403` from the proxy. I will not reconstruct the cipher side from
memory: that is the failure mode that produced the retracted `LONDON` misreading at
Checkpoint H.

Second request, lower priority because it may not be retrievable: the unedited 2005
Zetter/Scheidt interview material. Third, carried forward: a target-era Weltzeituhr frame
from a different bearing — now the *least* urgent, since EXP-029/030/031 have accumulated
bounded negatives against direct clock-letter running keys.

## 8. Reproduce this checkpoint only

```sh
python experiments/exp032_column_key.py
python experiments/exp033_subst_transposition.py     # ~8 min, needs numpy
python experiments/exp034_text_dependent_keys.py
python audit/verify_exp033.py
python audit/verify_exp032_034.py
```

Do not rerun EXP-029, EXP-030 or EXP-031: their scoped conclusions stand and nothing here
depends on reproducing them. EXP-024 remains frozen and unmodified.
