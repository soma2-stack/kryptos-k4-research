# Preregistration — EXP-034: text-dependent keys as arbitrary functions

Committed **before** implementation or execution, on branch `claude/k4-post-j`.
K4 remains unsolved. No external verifier. No alleged plaintext or K5 material.

## Inputs

`data/k4.json`, sha256 `e3b18a93c5fda5a8fc7a9249d25b1567c55cc2b5aef2843a65551b96b754ced8`;
ciphertext pinned to `eea813570c7f1fd3b34674e47b5c3da8948026f5cefee612a0b38ffaa515ceab`.
Public cribs only: `EASTNORTHEAST` [21,34), `BERLINCLOCK` [63,74) — 24 positions.

## Model

`k[i] = f(S[i - L])`, `C[i] = encrypt_conv(P[i], k[i])`, where

- `S` is a declared source stream,
- `L` is an integer lag,
- `f : A-Z → Z26` is **any** function, never enumerated. All 26²⁶ functions are decided
  exactly by consistency: if two constrained positions draw the same source letter but
  force different key values, no `f` exists; otherwise a consistent partial map extends.
  An arbitrary `f` absorbs every key alphabet, so key alphabet is **not** a parameter.

## Motivation

EXP-008 eliminated text-dependent keystreams only in **parameter-linear** form
(`k = a·S[i−L] + b`, and two-tap and drift variants). EXP-030 then showed that replacing
a fixed linear rule by an arbitrary function is exactly decidable and still strongly
falsifiable. EXP-034 applies that same generalisation to text-dependent keys, which is
the family EXP-008 itself named as the natural survivor of EXP-006. Classic autokey and
ciphertext feedback are pencil-and-paper systems of the right era, and a feedback key
flattens monographic statistics, which is what Scheidt's "masking" language requires of
whatever K4's process is.

## Declared sources and parameters

| source | definition | note |
|---|---|---|
| `ct_fwd` | `S[j] = C[j]` | ciphertext autokey / feedback; known at every position |
| `ct_rev` | `S[j] = C[96-j]` | self-referential reversed key |
| `ct_dec_m` | `S[j] = C[(m·j) mod 97]`, m ∈ {2,3,5,7,11} | decimated self-key |
| `pt` | `S[j] = P[j]` | classic plaintext autokey; constrained only where a crib supplies `P[j]` |

Lags `L = 1…96`. Conventions: the 12 committed shift conventions. Positions with
`i − L < 0` are unconstrained and are excluded from that case's constraint set, and the
count of usable constraints is reported per case.

Total cases: 8 sources × 96 lags × 12 conventions = **9,216**.

## Exact criterion

A case is FEASIBLE iff no two constrained positions sharing a source letter force
different key values. Cases whose usable constraint count is **≤ 3** are reported as
**UNDECIDED — INSUFFICIENT CONSTRAINT**, not as feasible, and are excluded from any
elimination claim. This threshold is fixed now, before any result.

## Falsifiability

Constraint counts are computed from the data before verdicts are read, and both the
per-case counts and the implied chance-survival rate `26^-(constraints)` are reported.
A case is only counted toward the elimination if its own constraint count makes a chance
survival less likely than 10⁻⁴, i.e. at least 4 constraints.

## Failure statement

If every sufficiently-constrained case contradicts: **no key that is an arbitrary
function of one declared source letter at one fixed lag can produce K4 from a plaintext
carrying the public cribs, under the 12 committed conventions.** This does not touch
two-tap functions of two source letters, position-dependent `f`, resets, running keys
from external text, or any non-shift combiner.

## Controls

Planted positives for every source and a sample of lags and conventions, using a random
`f` (including a deliberately non-injective one), synthesised with independent
arithmetic; the detector must report FEASIBLE and recover `f` on every constrained
letter. Adversarial: one corrupted crib ciphertext letter per plant must flip the
verdict to infeasible whenever that position participates in a constraint.

## Verifier

`audit/verify_exp034.py`, importing neither the experiment nor `k4lib`, recomputing
sources, lags, constraint counts and every verdict from the raw JSON, and re-planting
its own positives so that a rubber-stamp verifier is excluded.

## Prohibited post-hoc expansions

No second tap, no per-segment `f`, no lag-dependent `f`, no relaxation of the
consistency criterion to a score, and no lowering of the constraint threshold in
response to a near-miss.
