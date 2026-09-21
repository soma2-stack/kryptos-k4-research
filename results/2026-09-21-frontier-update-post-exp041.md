# Frontier update after EXP-040 and EXP-041

**Branch:** `claude/dreamy-archimedes-79k6u0`. Written immediately after EXP-041 returned negative.

## What the two experiments changed

EXP-040 and EXP-041 close the **propagating text-feedback** corridor at its structured core:
one-tap (any lag, plaintext or ciphertext, forward or reversed, primer 1–24) and additive
two-tap plaintext feedback (`b ≤ 19`, coefficients in `{±1}²`, `γ` free or zero).

They also produced a reusable **screening law**, now confirmed in two independent families:

> **The crib-span law.** A feedback model's power is bounded by where several known plaintext
> positions fall inside the *same dependency component*, not by the total crib count. Anything
> downstream of every crib in its component is absorbed by the warm-up and is undetectable.

This is the feedback analogue of the period 27–29 blind spot, and it is now a cheap pre-test:
compute the dependency components, check how many cribs share one, and reject the family before
coding if the answer is "at most one".

## Ranking the remaining finite, falsifiable architectures

Ranked by constraint density first, then evidence support, finite parameter count, and ability to
predict beyond the 24 cribs. Everything genuinely distinct from EXP-033 … EXP-041.

| rank | architecture | shared parameters | constraint density | evidence | predicts beyond cribs? | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **Nonlinear two-input feedback** `k[i] = f(P[i−a], P[i−b])` with `f` a shared 26×26 table | 676 table cells | **very low** — 24 equations against 676 cells, and the consumed input pairs rarely repeat | none names it | yes if it survived | **VACUOUS** — the table memorises the cribs |
| 2 | **Small-table feedback** `k[i] = f(P[i−a])` with `f` a shared 26-entry table | 26 + primer | borderline — 26 unknowns vs 24 equations | none | yes | **UNDERDETERMINED** — fails the non-vacuity gate by parameter count alone |
| 3 | **Three-or-more-tap additive feedback** | `b` warm-up values | good for small `b` — same law as EXP-041 | none | yes | **OPEN and testable**, but strictly weaker motivation than EXP-041 had; adds taps without adding evidence |
| 4 | **Mixed plaintext/ciphertext taps** `k[i] = P[i−a] + C[i−b]` | `a` warm-up values | good — still linear and propagating | none | yes | **OPEN and testable**; the cheapest genuinely untested feedback variant |
| 5 | **Feedback composed with a declared transposition** | warm-up + permutation choice | unknown until `π` is fixed; positional alignment is destroyed for unknown `π` | none | yes | open only for **declared finite** `π` families |
| 6 | **Two masks around a permutation**, `M2 ∘ π ∘ M1` | `p + q` | `24 − (p+q−1)` as a **lower** bound; only ~7 at the K1/K2 pair | multi-stage is direct Scheidt; the **periods are not evidenced** | weakly | **blocked on parameter selection**, unchanged |
| 7 | **Periodic masks at p = 24–26** | `p` | 5 / 3 / 1 | none selects the period | barely | **blocked**; p = 27–29 remain at **zero** |

## Assessment

**Nothing in the list clears the gate that EXP-040 and EXP-041 cleared.** Ranks 1 and 2 fail
non-vacuity on parameter count alone — a 676-cell or even 26-cell shared table simply memorises
24 equations, which is the failure mode the repository's census already names. Ranks 3 and 4 are
testable but are *weaker* propositions than the ones just closed: they add structure without
adding evidence, which is precisely the "accumulate experiment numbers" trap the brief warns
against. Ranks 5–7 are unchanged and still blocked on parameter selection rather than compute.

The honest summary is that the **structured, evidence-neutral core of the feedback corridor is now
closed**, and what remains inside it is either vacuous or a strictly less motivated variant of
what has just been eliminated.

## What this means for the two-outcome test the brief sets

The brief asks us to keep going until either a deterministic candidate survives and predicts new
structure, or we prove the 24 letters cannot discriminate the remaining families. EXP-040 and
EXP-041 are real progress toward the **second** outcome: combined with the AE census and the
crib-span law, the pattern is that every family with enough shared structure to be testable has
been tested, and every untested family is untestable *because* its parameters outnumber the
constraints.

That is not yet a proof. It is a strong and now twice-confirmed regularity.

## One next action

**Mixed plaintext/ciphertext two-tap feedback** (rank 4) is the single highest-information
remaining move inside this corridor: it is linear, propagating, exactly decidable by the same
machinery, has the same favourable constraint density as EXP-041, and is the only feedback
variant left whose parameter count stays below the crib budget without invoking a shared table.

It should be attempted **only** with the crib-span law applied first as a screen, and with the
same honesty that its documentary motivation is filter-level rather than specific — the same
standing that EXP-040 and EXP-041 were granted, and no more.

K4 remains unsolved.
