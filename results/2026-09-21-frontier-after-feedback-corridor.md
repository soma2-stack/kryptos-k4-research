# Frontier after the feedback corridor — and a discrimination theorem

**Branch:** `claude/dreamy-archimedes-79k6u0`. Written immediately after EXP-042 returned negative.

The simple feedback corridor is **provisionally exhausted** (EXP-040, EXP-041, EXP-042). This
document does the required frontier comparison A–E and, under E, states the theorem that now
organises the whole search.

---

## E first: the discrimination budget

Three experiments in a row produced the same shape of answer, so the regularity is worth stating
exactly rather than rediscovering.

> **Discrimination budget.** Let a model class map a parameter vector to the plaintext
> deterministically given the ciphertext, and let
>
> **`d_eff` = the rank, over Z26, of the map (parameters → the 24 crib plaintext values)**.
>
> Then a single class is consistent with the cribs for a fraction `26^(d_eff − 24)` of possible
> crib assignments, and a family of `N` such classes has expected accidental survivors
> `N · 26^(d_eff − 24)`. The family can discriminate only if
>
> **`log₂₆(N) + d_eff < 24`.**

Two points make this more than bookkeeping.

**`d_eff` is not the nominal parameter count.** Only parameters a crib position actually reaches
enter the rank. That *is* the crib-span law: a warm-up value whose chain contains no crib, or a
ciphertext tap that only shifts a known constant, contributes nothing. Using the nominal count
instead mislabels EXP-040 and EXP-042 as undecidable when both were in fact decisive — a mistake
this analysis made once and corrected.

**It reproduces every measured result in the repository.**

| family | log₂₆ N | `d_eff` | sum | verdict | measured |
| --- | ---: | ---: | ---: | --- | --- |
| EXP-040 one-tap autokey, worst `m = 24` | 2.41 | 19 | **21.4** | discriminating | 0 feasible, decisive |
| EXP-041 two-tap plaintext, worst `b = 19` + γ | 3.07 | 20 | **23.1** | marginal | 0 feasible |
| EXP-042 mixed two-tap, worst `a = 24` + γ | 3.56 | 20 | **23.6** | marginal | 0 feasible |
| Periodic mask `p = 24` | 0.76 | 19 | **19.8** | discriminating | 5 crib constraints |
| Periodic mask `p = 26` | 0.76 | 23 | **23.8** | marginal | 1 constraint |
| Periodic mask `p = 27` | 0.76 | 24 | **24.8** | **cannot discriminate** | 0 constraints |
| `M2 ∘ π ∘ M1` at (8,10), one declared `π` | 0.98 | 17 | **18.0** | discriminating | ~7 constraints |
| `M2 ∘ π ∘ M1` at (8,10), EXP-036-scale `π` corpus | 6.81 | 17 | **23.8** | marginal | — |
| AC structured Trifid, per configuration | 1.62 | 46 | **47.6** | **cannot discriminate** | 15 conditionally SAT |
| Shared 26-entry feedback table | 1.41 | 26 | **27.4** | **cannot discriminate** | — |
| Shared 26×26 feedback table | 1.41 | 676 | **677** | **cannot discriminate** | — |
| Free polygraphic inner map behind any mask | 0 | ~600 | **~600** | **cannot discriminate** | AA: vacuous |

The period 27–29 blind spot, the AA erasure theorem, the AC parameter-sharing principle and the
crib-span law are all the same inequality seen from different sides.

**Use it as the first screen on any future proposal.** Compute `d_eff` and `N` before writing code.

---

## A. `M2 ∘ π ∘ M1` — two masks around a fixed permutation

**Can K1–K3 or the physical/documentary record select `π`, the mask periods, or an inheritance
rule?** No, and the repository has now looked three separate ways.

- Checkpoint V found **no statement** that K4 reuses K1/K2 key lengths or methods; `LAYER TWO`
  does not supply one.
- Checkpoints AI–AK found **no artifact-selected** route, reset or permutation; physical row
  geometry for rows 26–28 remains unmeasured, and Checkpoint T showed row breaks do **not** select
  a reset.
- Checkpoints X, Y and Z established that Scheidt **declined** to fix stage order, and that the
  `ScheidtNova.doc` payload remains unrecovered.

The budget says this class *would* be decisive with a **single declared `π`** (sum 18.0), and only
marginal against an EXP-036-scale corpus (23.8). **So the blocker is precisely and only parameter
selection — not compute, and not constraint density.** That is worth stating sharply: this is the
one remaining class where a single sentence of evidence would convert a blocked family into a
decisive experiment.

**Status: blocked on evidence, highest value if evidence arrives.**

## B. Periods 24–26

**Is there any independently motivated reason for specifically 24, 25 or 26 that does not arise
from crib fitting?** Searching the repository's evidence record: **no.**

- 26 is the alphabet size — a numerological coincidence, not a documented key length.
- 24 and 25 have no documentary, physical or K1–K3 basis whatsoever.
- The K1/K2 key lengths that *are* evidenced are 10 and 8, not 24–26.

Any selection of 24, 25 or 26 would be chosen *because those are the periods the cribs happen to
leave partly open* — which is crib fitting, the exact failure mode the gate exists to prevent.

**Status: remains blocked.** And note the budget: even `p = 26` sits at 23.8, i.e. marginal at
best, so this would be a weak experiment even if a motivation appeared.

## C. Structured fractionation

Only admissible if the readout, tableau and period can be **independently selected**. They cannot:
Checkpoint AC's Trifid family was explicitly selected post hoc, and its per-configuration budget
is 47.6 — far beyond discrimination. Free polygraphic maps are not reopened (AA proved them
vacuous even behind a fixed outer map).

**Status: closed unless an external source names a specific readout and period.**

## D. Deterministic alignment / permutation not already covered

EXP-033 (declared single transpositions × any fixed A–Z map), EXP-036 (declared transpositions ×
periodic shift families) and EXP-039 (precommitted double columnar) span the declared corpus. A
genuinely new entrant would need a **source-selected** alignment — and the physical audits
AI–AK found none, with rows 26–28 endpoints still unmeasured.

**Status: no new entrant available.**

---

## Which of the two situations are we in?

The brief asks whether (1) a small, historically plausible, finitely testable architecture is still
hiding, or (2) the 24 authenticated letters are fundamentally insufficient to discriminate the
surviving classes.

**The evidence now points substantially toward (2), and the theorem says why.** Every surviving
class falls into exactly one of two buckets:

- **`log₂₆(N) + d_eff ≥ 24`** — cannot be discriminated by 24 letters *no matter how much compute
  is applied*. This covers structured fractionation, all shared-table feedback, free polygraphic
  maps, and periodic masks at `p ≥ 27`.
- **`log₂₆(N) + d_eff < 24` but no evidence selects the parameters** — `M2 ∘ π ∘ M1`, periods
  24–26, and any transposition family outside the declared corpus.

**Nothing currently sits in the productive third bucket** — decisive *and* motivated — which is
where EXP-040, EXP-041 and EXP-042 sat, and which is now empty.

This is not a proof of (2). A class with small `d_eff` and genuine motivation could still be
found; the theorem bounds what 24 letters can do, but it cannot enumerate every conceivable
architecture. What it does establish is that **further progress requires new information, not new
search** — and it quantifies exactly how much: each additional authenticated plaintext letter
raises the right-hand side of the inequality by one, which is worth a factor of 26 in
discriminating power.

## One next action

**Request 7 — a single additional authenticated plaintext letter**, targeted at indices
**1, 3, 91, 93, 95 or 96**, remains the highest-information move available, and the theorem now
prices it exactly: one letter buys a factor of 26, and moves `p = 27` from "cannot discriminate"
to testable while giving `M2 ∘ π ∘ M1` room against a realistic `π` corpus.

Failing that, **Request 2** — the unedited Zetter/Scheidt material or the `ScheidtNova.doc`
payload — is the only route that can populate the empty third bucket, because class A is blocked
**solely** on parameter selection.

No further cipher family should be enumerated until one of those two arrives.

K4 remains unsolved.
