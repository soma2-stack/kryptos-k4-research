# EXP-044 preregistration — engraved-geometry route inside two periodic masks

**Branch:** `claude/dreamy-archimedes-79k6u0`
**Written:** 2026-09-21, **before** any implementation or any K4 scoring.
**Supersedes nothing.** This is a new registered scope.

## 0. Why this family and not another

Checkpoint AP's census found exactly one candidate in the productive bucket
(**motivated AND discriminating**). The reasoning is entirely pre-test:

- The repository's `M2 . pi . M1` sandwich shape survives every prior negative, but
  EXP-043 tested only the **affine-mod-97** surrogate for `pi`. That surrogate was
  chosen because 97 is prime and therefore admits **no** rectangular route, which is
  K3's actual principle. Affine maps are not the only Kryptos-motivated permutations.
- K4's **textual row structure** (`4 / 31 / 31 / 31`) is Grade-A authenticated in
  `data/cipher_side_rows.json` and `docs/external/checkpoint-K-nsa-cipher-rows-1-24.md`.
  Routes over that *ragged* engraving grid are already formalised in the repository as
  `k4lib.transpositions.engraved_routes()` and were used by EXP-033 — but **only**
  composed with a single fixed monoalphabetic map.
- EXP-036 paired a periodic mask with transpositions, but its corpus is **keyed
  columnar widths 2–10**; it does **not** contain the engraved routes.

So the engraved-route corpus has never been tested against a **position-varying** mask,
let alone two. That is the gap.

## 1. Model (fixed now)

    X[j]        = P[j] + m1[j mod p]                    (mask M1, plaintext index)
    Y[pi(j)]    = X[j]                                  (transposition)
    C[pi(j)]    = conv( Y[pi(j)], m2[pi(j) mod q] )     (mask M2, ciphertext index)

which collapses, for the additive conventions, to

    C[pi(j)] = conv( P[j], ( m1[j mod p] + m2[pi(j) mod q] ) mod 26 )

`m1` and `m2` are **never enumerated**. Each configuration is decided *existentially*
over all `26^(p+q)` key pairs by weighted union-find with potentials over Z26 — the
same exact decision procedure EXP-043 used, reused deliberately so the verification
machinery transfers.

## 2. Declared corpus (frozen before testing)

| Axis | Values | Count |
|---|---|---|
| `pi` | `engraved_routes()` x {forward, inverse}, deduplicated | **12 distinct** |
| `p` | 1..10 | 10 |
| `q` | 1..10 | 10 |
| convention | the 12 committed (3 combiners x STD/KRY plaintext x STD/KRY ciphertext) | 12 |

**N = 12 x 100 x 12 = 14,400 configurations.**

`p, q <= 10` is not arbitrary: it is the largest square bound whose worst-case budget
still passes (see §3), and it spans the only two key lengths Kryptos itself exhibits,
PALIMPSEST (10) and ABSCISSA (8). Consistent with `KNOWN_STATE.md`, `(8,10)` is
included **only as an ordinary member of a declared sweep**, never as a derived rule —
no K1–K3 period rule exists, because K3 has no key length.

Two of the 14 route/orientation pairs are involutions (`eng_rows_boustro`,
`eng_rows_rl`), so the corpus deduplicates 14 -> 12. Verified before testing:
**no engraved permutation is affine**, so this corpus is **disjoint from EXP-043**;
and the identity is absent.

### Motivation grading, stated honestly in advance

- **Row-based routes** (`eng_rows_*`, 3 routes): motivated by Grade-A *textual* row
  order alone. Strong.
- **Column-based routes** (`eng_cols_*`, 4 routes): require a column lattice that
  Checkpoint AJ says is **not** physically established. Weaker. They are included so
  the sweep is complete, and any survivor among them must be reported with this caveat
  attached. A column-route survivor is **not** equivalent evidence to a row-route one.

## 3. Discrimination budget — computed before writing the experiment

Using Checkpoint AP's cycle-rank theorem, `d_eff` is the rank of the signed anchored
crib graph, computed exactly for all 1,200 (route, p, q) combinations:

- worst-case `d_eff` = **19** (at `p=q=10`, `eng_cols_down/B`)
- `log26(14,400)` = **2.939**
- **budget = 21.939 < 24 — PASS**
- expected accidental survivors at the worst case: `14,400 x 26^-5` = **0.0012**

`mu = 24 - d_eff` ranges from **5** (worst) to **23** (best). The family is
non-vacuous everywhere in the declared scope.

## 4. Predeclared outcome rule

- **0 feasible** -> a scoped negative. It closes the engraved-route sandwich at
  `p,q <= 10` and **nothing more**. It must not be written up as closing arbitrary
  sandwiches, arbitrary non-affine `pi`, or `p,q > 10`.
- **1 or more feasible** -> **not** a solution and **not** evidence by itself. Any
  survivor must be reported with its expected-accidental-survivor count, and the
  column-route caveat where it applies. A survivor is promoted only if it predicts
  ciphertext it was never allowed to see.

I commit to reporting the count either way, including if it embarrasses the hypothesis.

## 5. Controls (all must pass or the run is void)

1. **Positive:** plant a synthetic ciphertext built from a known
   `(route, p, q, m1, m2, convention)` that carries the *real* crib letters at the
   *real* crib positions; the solver must find that configuration feasible.
2. **Out-of-family permutation:** a random non-engraved permutation must not be
   silently accepted as in-family, and must be verified non-affine and non-engraved.
3. **Adversarial corruption:** corrupting one crib-constrained ciphertext character of
   the synthetic instance must flip the planted configuration to infeasible.
4. **Blind-region control:** corrupting a position **outside** every crib must **not**
   flip it — this measures crib reach rather than assuming it.

## 6. Independent verification (separate file, no imports from the experiment)

`audit/verify_exp044.py` must re-derive, without importing
`experiments/exp044_*`:

- the engraved-route corpus and its deduplication to 12, from `k4lib` directly;
- disjointness from the affine family (all 9,312);
- for a random sample of infeasible configurations, an explicit **cycle certificate**:
  a closed walk in the crib graph whose alternating key sum is non-zero mod 26,
  which *proves* infeasibility rather than trusting the solver's verdict;
- a brute-force **forward simulation** cross-check on the small-key cases
  (`p, q <= 3`, so `26^(p+q) <= 26^6`) using no graph theory at all;
- the budget arithmetic of §3.

## 7. What this experiment cannot do

It cannot address non-additive masks, `p` or `q` above 10, permutations outside the
engraved corpus, three or more stages, or any Layer-B question. A negative here says
nothing about those.
