# Preregistration — EXP-040: propagating text-autokey with a short primer

**Branch:** `claude/dreamy-archimedes-79k6u0`. **Written before implementation.**
**Starting HEAD:** `653eeb8a7aad3662493b726490fa2ed76dde76c2`.

## 1. What this is, and why it is not EXP-008

EXP-008 tested data-dependent keystreams as **local affine taps**: `k[i] = a·S[i−L] + b`.
Its plaintext source is implemented as

```python
out["plain"] = lambda j: (idx[P[j]] if j in P else None)
```

so it returns a value **only when the lagged position is itself inside a crib**. It therefore
never propagates, never derives unknown plaintext, and never solves the autokey recursion.
It also capped the plaintext lag at 12 and skipped any system with fewer than 6 rows.

A **propagating** autokey is a different object. Given a primer of `m` letters, the recursion
determines **all 97 plaintext letters** from the ciphertext. The unknowns are the `m` primer
letters and nothing else. That is the parameter-sharing property Checkpoint AC identified as
the generator of constraints, and it is why this family is decidable where a local tap was not.

## 2. Exact model

Let `idxP` and `idxC` index the plaintext and ciphertext alphabets of a convention, and let the
combiner be one of `vigenere`, `beaufort`, `variant_beaufort` as defined in `k4lib/conventions`.

**Forward plaintext autokey**, primer length `m`, primer letters `x[0..m−1]`:

```
k[i] = x[i]            for i < m
k[i] = P[i − m]        for i >= m
C[i] = combine(P[i], k[i])
```

Inverting gives `P[i] = uncombine(C[i], k[i])`. Within residue chain `r = i mod m` this is a
first-order recursion whose solution is affine in the single unknown `x[r]`:

- vigenere:         `P[r+jm] = (alternating ciphertext sum) + (−1)^(j+1)·x[r]`
- beaufort:         `P[r+jm] = x[r] − (cumulative ciphertext sum)`
- variant beaufort: `P[r+jm] = (cumulative ciphertext sum) + x[r]`

**Exactly one unknown per chain.** Every crib position in a chain yields an exact value for that
chain's unknown; two crib positions in one chain that disagree are a contradiction.

**Declared variants, all frozen now:**

| axis | values |
| --- | --- |
| source | plaintext autokey; **ciphertext autokey** (a duplicate-check against EXP-008, not a novelty claim) |
| direction | forward (`k[i] = S[i−m]`); reverse (`k[i] = S[i+m]`, primer at the tail) |
| combiner | the 3 committed combiners |
| plaintext alphabet | STD, KRY |
| ciphertext alphabet | STD, KRY |
| key-index alphabet | the fed-back letter indexed in the **plaintext** alphabet, or in the **ciphertext** alphabet |
| primer length `m` | 1 … 24 |
| reset | none; plus **physical-row reset** at message indices 4, 35, 66 with a fresh primer per row, for `m` ∈ {1,2,3} only |

Case count: `2 sources × 2 directions × 12 conventions × 2 key-alphabets × 24 lengths = 2,304`,
plus `2 × 2 × 12 × 2 × 3 = 288` row-reset cases. **2,592 exact solves. No search.**

## 3. Constraint budget, computed before implementation

Unknowns are the primer letters; constraints are `24 − (chains occupied by crib positions)`.

```
m:      1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
constr:23 22 21 20 19 18 17 16 15 14 13 12 11 11  9  8  7  7  9 11 11  9  7  5
```

Row-reset variant: 21, 18 and 15 constraints for `m` = 1, 2, 3.

**Declared scope limit.** `m ≥ 25` gives 3, 1, 0, 0, 0 constraints at `m` = 25…29. Those are
**excluded from the survivor question** and will be reported as **UNDECIDABLE WITH PRESENT CRIB
GEOMETRY**, never as survivors. This is fixed now, not after seeing results.

## 4. Decision rule

A configuration is **FEASIBLE** only if every chain's crib equations are mutually consistent.
There is no scoring, no threshold and no language model anywhere in the decision.

A FEASIBLE configuration deterministically yields all 97 plaintext letters. It will be reported
as a **structural survivor only**. K4 is **not** claimed solved unless a single frozen procedure
reproduces all 97 ciphertext characters and an independent verifier confirms it.

## 5. Null expectation, stated before execution

Chance survival for a configuration with `c` independent constraints is `26^−c`. The weakest
admitted configuration has `c = 5` (`m = 24`), giving `26^−5 ≈ 8.4 × 10^−8`. Summing `26^−c`
over all 2,592 admitted configurations gives an expected accidental-survivor count below
`2 × 10^−5`. **Any survivor is therefore either real or an implementation error**, which is why
an independent verifier is mandatory.

## 6. Controls

1. **Positive control** — plant a known primer, generate a synthetic ciphertext through the
   forward recursion, and require the solver to recover exactly that primer and plaintext.
2. **Adversarial control** — corrupt one ciphertext character at a position that participates in
   a crib chain and require the affected configuration to flip to infeasible. A control that
   cannot flip the verdict is reported "not counted", never as a pass.
3. **Duplicate check** — ciphertext autokey must come back negative, consistent with EXP-008
   having already covered it as the `a=1, b=0` case of its affine tap.

## 7. Prohibited post-hoc moves

No widening of `m` beyond 24; no additional sources, alphabets, combiners or directions; no
sliding or extending the cribs; no language scoring of survivors; no relabelling a weak
configuration as a survivor; no reporting `m ≥ 25` as anything but undecidable.

## 8. Evidence motivation, stated before the result

Autokey is a **classical, hand-executable, historically grounded** construction, consistent with
the 1999 *Washington Post* record that the methods could have a historic basis. It needs **no
apparatus beyond the Vigenère tableau already carved on the sculpture and already used for
K1/K2** — a changed rule rather than a new machine, matching the documented picture of a system
*adapted* rather than a textbook cipher used unchanged. It is also structurally a different kind
of object from K1/K2's periodic key, which fits K4 being the harder fourth process.

This is a **filter-level** motivation and is honestly labelled as such. No source names autokey,
and the family is **not** claimed to be documentary-selected. It clears the gate on being
genuinely new, finite, exactly decidable, non-vacuous and independently verifiable — not on
documentary specificity.
