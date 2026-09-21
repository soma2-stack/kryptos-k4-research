# Preregistration — EXP-032 and EXP-033

Committed **before** either experiment is implemented or executed. Branch
`claude/k4-post-j`, base `6134fcc41254a31cc3131753826e1409224e5ecc` (Codex Checkpoint J head).
K4 remains unsolved. No external verifier will be consulted. No alleged plaintext,
solution dump, or private K5 material is used.

## Exact inputs

| input | sha256 |
|---|---|
| `data/k4.json` | `e3b18a93c5fda5a8fc7a9249d25b1567c55cc2b5aef2843a65551b96b754ced8` |
| `data/physical.json` | `6afc22576403af373295bc4172446d0825f84730d5e5a2c6e888e377db7f9e73` |

Ciphertext (97 chars, pinned by `k4lib.data` to
`eea813570c7f1fd3b34674e47b5c3da8948026f5cefee612a0b38ffaa515ceab`):
`OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR`

Public cribs, zero-based half-open, exactly as committed and unchanged:

- `EASTNORTHEAST` at [21, 34) against `FLRVQQPRNGKSS`
- `BERLINCLOCK` at [63, 74) against `NYPVTTMZFPK`

24 constrained positions. No other plaintext is assumed anywhere.

## Verified geometry used by both experiments

NSA DOCID 4145037 places K4 on the cipher side as rows 25–28, K4 positions 1–4 at
row 25 columns 28–31 (immediately after K3's terminal `?`), then 5–35, 36–66, 67–97
as full 31-column rows 26–28. Checked against the repository ciphertext before
preregistering: the three quoted 31-character rows equal `K4[4:35]`, `K4[35:66]`,
`K4[66:97]` exactly; row 25 is 31 characters ending in `OBKR`; 32 + 27×31 = 869.

Zero-based column map used: `col(i) = 28+i` for i<4, `i−3` for 4≤i<35, `i−34` for
35≤i<66, `i−65` for i≥66.

**Audit finding recorded in advance, because it bounds what the correction can buy:**
no crib lies at positions 0–3, and for i ≥ 4 the corrected and the old isolated-`OBKR`
column maps are identical. Therefore the geometry correction **cannot** change the
outcome of any crib-constrained column- or position-indexed model. It matters only for
(a) models that use the characters physically *above* K4, (b) transpositions on K4's
ragged physical grid, (c) predictions about positions 0–3. Both experiments below are
scoped accordingly, and EXP-032 will verify this equivalence programmatically rather
than assert it.

---

# EXP-032 — key as an arbitrary function of engraving column

## Model

`k[i] = f(col(i))`, with `f : {1..31} → Z26` **any** function, and
`C[i] = encrypt_conv(P[i], k[i])` for one of the 12 committed shift conventions.
Position-preserving, monographic.

## Motivation

Sanborn performed the physical encoding, and the engraving column is now a grade-A
documented property of every K4 character. A key that advances with the column and
resets at each engraved row is the natural "physical" reading of a repeating key, and
`f` arbitrary makes this a strict superset of every periodic or line-reset key already
eliminated in EXP-006 — including all key alphabets, since an arbitrary `f` absorbs any
relabelling of key letters.

## Overlap with existing experiments

EXP-006 eliminated periodic and line-reset keystreams at specific periods with fixed
alphabets. EXP-032 is strictly more general in `f` but strictly narrower in indexing
(column only). It overlaps EXP-006 on the periodic subset and is new for every
non-periodic `f`.

## Free parameters, search size, dedup

Convention (12). `f` is not enumerated: 31 values over Z26 are decided exactly by
consistency, covering all 26^31 functions. Key alphabet is absorbed by `f` and is
therefore **not** a parameter. **12 cases.**

## Exact criterion

A case is FEASIBLE iff no two crib positions sharing a column force different key
values. The crib set has exactly two column collisions, computed before running:
column 29 = positions {32, 63}, column 30 = positions {33, 64}. So each case carries
exactly 2 independent constraints; chance survival per case is 26⁻² ≈ 1.5×10⁻³ and the
expected number of chance-feasible cases over all 12 is ≈ 0.018.

## Failure statement

If all 12 cases are infeasible: **no function of engraving column alone, under any of
the 12 conventions, can produce K4 from a plaintext containing the public cribs.** That
eliminates an infinite family from two constraints. It says nothing about functions of
(row, column), which the crib set cannot constrain at all — each crib position has a
unique (row, column) pair — and that vacuity will be reported rather than hidden.

## Controls

Planted positives: for each convention, synthesise a ciphertext from a random `f` and a
padded plaintext carrying the real crib letters at the real positions; the detector must
report FEASIBLE and recover an `f` consistent with the plant. Adversarial: corrupt one
crib letter of a planted case; the detector must report INFEASIBLE.

## Verifier

`audit/verify_exp032.py`, importing neither the experiment nor `k4lib`, recomputing the
column map, the collisions, and every verdict from the raw ciphertext string.

## Prohibited post-hoc expansions

No widening to `f(row, col)`, `f(col) + g(row)`, per-row alphabets, or any added
parameter in response to a negative. No relaxation of the exact consistency criterion
into a score.

---

# EXP-033 — arbitrary monoalphabetic substitution composed with a declared transposition family

## Model

`C[i] = S(P[σ(i)])`, where `σ` is a permutation of {0..96} drawn from the declared
family below and `S : A–Z → A–Z` is **any** function.

`S` is not enumerated. All 26^26 functions (every mixed, keyword and reciprocal
alphabet included) are decided exactly per `σ` by consistency of the induced partial
map, in the manner of EXP-030's contradiction test.

**Dedup rule stated in advance:** a monoalphabetic substitution commutes with a
transposition — `π(S(P))` and `S(π(P))` are the same map — so composition order is not
a parameter and will not be double-counted. Encipher/decipher orientation *is* a
parameter and is carried as `σ` versus `σ⁻¹`.

## Motivation

1. **Every experiment in this repository so far assumes the key depends on message
   position.** EXP-021's argument that K4 must be position-preserving rested on the
   K4/K5 equal-length correspondence, which `docs/codex-audit.md` finding 7 withdraws as
   overbroad. With that withdrawn, architectures that *move* the plaintext are reopened,
   and nothing in EXP-001…031 tests one except the affine-mod-97 family.
2. **Documentary:** Scheidt describes a fourth high-level process, different from the
   first three, masking ordinary English statistical access; K3 is already a route
   transposition Sanborn implemented himself, and he says he modified the systems he was
   taught. Substitution composed with a columnar/route transposition is the classical
   pencil-and-paper answer in that space.
3. **It closes a gap the audit flags.** K4's IoC (0.03608) disfavours this architecture
   at z ≈ −3.9 against an English-transposition null, but the audit correctly notes that
   a low IoC does not *prove* no English plaintext exists. This experiment replaces that
   statistic with an exact crib-based decision over a large declared family.

## Overlap with existing experiments

EXP-003 and EXP-016 cover the **affine mod 97** permutation family (9,312 permutations)
composed with *keystream* models. EXP-033 covers non-affine columnar and route
permutations composed with a *single arbitrary substitution*, decided exactly. Inherited
community work on 3×31 and 4×22 routes was rejected on plaintext readability, never on
an exact crib criterion. EXP-011 found transposition plus a *free per-position* alphabet
vacuous; that does not apply here, and the falsifiability is computed below rather than
assumed.

## Declared permutation family

- **F1 — keyed columnar transposition.** Widths w = 2…11, **all w! column orders**,
  write by rows into a w-wide grid with a ragged final row, read columns in key order.
  Variants: columns read top→bottom or bottom→top (2) × orientation `σ` or `σ⁻¹` (2).
  Σ w! for w=2…11 = 43,954,712, so **175,818,848 cases** before dedup.
- **F2 — unkeyed rectangle routes.** All widths w = 2…96: write by rows, read by columns
  L→R and R→L, boustrophedon by columns and by rows, four spiral starts × 2 directions,
  and two diagonal routes; each × orientation (2).
- **F3 — routes on K4's corrected ragged engraving grid** (row 25 columns 28–31, rows
  26–28 columns 1–31): column-major down, column-major boustrophedon, row-major
  reversed, and their orientations. **This subfamily is the independent reproduction and
  formalisation of the uncommitted supervisory scratch result**, and is labelled as such
  in the output so its verdict can be read separately.

Duplicate permutations across and within subfamilies are deduplicated by hashing the
permutation tuple; the identity and any permutation already covered by the affine family
of EXP-003/016 are labelled, not silently dropped.

## Exact criterion

For each `σ`, build the partial map `P[j] ↦ C[σ⁻¹(j)]` over the 24 crib positions.

- **FEASIBLE-BIJECTIVE** iff that map is a well-defined function *and* injective.
- **FEASIBLE-FUNCTION** iff it is a well-defined function, injectivity not required
  (admits collapsing / non-injective substitutions).

Both counts are reported separately. Nothing is scored; there is no threshold.

## Falsifiability, computed before running

The 24 crib positions carry 13 distinct plaintext letters with multiplicities
E³ T³ A² S² N² O² R² L² C² B H I K, so Σ(m−1) = 11 equality constraints plus
injectivity. Using K4's own ciphertext letter frequencies, the chance that a random
permutation is FEASIBLE-BIJECTIVE is ≈ 6.6×10⁻¹⁷. Over the full declared family
(≈1.8×10⁸ cases) the expected number of chance survivors is ≈ 1.2×10⁻⁸. **The family is
therefore not vacuous**, and a survivor would be a genuine hypothesis rather than noise.

## Failure statement

If zero permutations in the declared family are FEASIBLE-BIJECTIVE: **K4 is not any
monoalphabetic substitution composed with any transposition in the declared family.**
Scope is exactly that family and the public cribs. This is not a statement about keyed
columnar widths ≥ 12, double transposition, keyed routes outside the family, any
polyalphabetic composition, or fractionation.

## Controls

- **Planted positives:** for each subfamily, ≥ 40 cases total — random `σ` from that
  subfamily and a random bijection `S` — synthesised with independent arithmetic, must
  be detected FEASIBLE at the planted `σ` with a recovered `S` matching the plant on all
  constrained letters.
- **Adversarial negatives:** each planted case re-tested with one crib ciphertext letter
  corrupted (must become infeasible) and with a neighbouring non-planted `σ` (must be
  infeasible).
- **Non-injective control:** a plant using a deliberately collapsing `S` must be found
  under FEASIBLE-FUNCTION and rejected under FEASIBLE-BIJECTIVE.

## Verifier

`audit/verify_exp033.py`, importing neither the experiment nor `k4lib`. It rebuilds
permutations by **explicit grid simulation** rather than the closed-form column
arithmetic the experiment uses, re-decides a random sample plus every control and every
declared-feasible case, and checks family coverage counts and input/output hashes.

## Prohibited post-hoc expansions

If a near-miss appears (a map that is a function but not injective, or one failing a
single constraint) it is recorded and **not** tuned around: no widening of the family,
no relaxation to "all but one crib", no per-row or per-block substitutions, no keyword
scoring, no plaintext readability judgement. Any follow-up requires a new, separately
motivated preregistration.

## Stop condition

Neither experiment may be used to claim K4 solved. A claim requires a complete
deterministic 97-character procedure explaining all public constraints, which neither
experiment can produce even on a hit without further independent work.
