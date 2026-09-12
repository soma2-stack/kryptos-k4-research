# Preregistration — EXP-035: running key from the authoritative cipher-side text

Committed **before** implementation or execution, on branch `claude/k4-post-j`, base
`ef082c80308c2fcc1d75dc0f559eaf28209de6ff`. K4 remains unsolved. No external verifier.
No alleged plaintext, solution material, or K5 content.

## Exact inputs

| input | sha256 |
|---|---|
| `data/k4.json` | `e3b18a93c5fda5a8fc7a9249d25b1567c55cc2b5aef2843a65551b96b754ced8` |
| `data/cipher_side_rows.json` | recorded in the experiment output at run time |
| linear 28-row stream (869 chars) | `dde19b74d57e0d2b169466cdec2641eb8c87e30ce35b74f4c60c4a74ba413177` |

Rows 1–28 come from `data/cipher_side_rows.json`, which carries the CIA Panel 1 text
version with NSA corroboration (grade A for row text and order) and its verification
record. Public cribs only: `EASTNORTHEAST` [21,34), `BERLINCLOCK` [63,74) — 24 positions.

## Why the physical "same column above" model is NOT being run

The requested rows arrived, and they refute the claim that made that model attractive.
Rows 1–24 hold **29, 30, 31, 32 or 33** characters (distribution 1/5/11/6/1). With a
monospaced punch and a common physical row width, every row would hold the *same* number
of characters. Therefore either the physical row width varies by row, or the letter pitch
varies by row — and the second is what `data/physical.json → engraving_line_lengths`
already records at MEDIUM confidence: *"Sanborn kerned the lettering for aesthetics;
fixed-width spacing was avoided."* Between a 29-character and a 33-character row the pitch
would differ by 13.8%, so character centres in different rows would not sit above one
another except by coincidence.

So the new grade-A evidence does not merely leave horizontal alignment undetermined; it
**positively disfavours the existence of a common punch lattice**. Grade: STRONGLY
DISFAVOURED, not disproved — the copper screen is an S-curve and `panel_layout` is
recorded as CONFLICTING, so "row width" is not perfectly well defined without a
photograph.

Constructing three alignment lattices in order to test them anyway would be rescuing the
idea, not falsifying it. The physical route is therefore **parked**, and the evidence that
would settle it is Request 4 in `docs/external-evidence-requests.md`.

What *is* authoritative is **row content and reading order**. EXP-035 uses only that.

## Model

`k[i] = f(S[g(i)])` and `C[i] = encrypt_conv(P[i], k[i])`, with

- `S` a declared source stream built only from row content and reading order;
- `g` a declared index map;
- `f : Σ → Z26` **any** function, never enumerated. All functions are decided exactly by
  consistency: if two constrained positions draw the same source symbol but force
  different key values, no `f` exists. An arbitrary `f` absorbs every key alphabet, so
  **key alphabet is not a parameter**.

## Motivation

Checkpoint K ranked "a long, low-entropy key from an *unidentified* external source" as
the surviving architecture carrying most of the probability mass, and said explicitly that
it can only move when a source is **identified**. The fulfilled evidence request
identifies a candidate: 745 characters of cipher-side text standing immediately above K4
on the same object, public since 1990, engraved by Sanborn himself, and never before
available to this repository. That is the intended use of the new evidence.

## Overlap with existing experiments

EXP-004, EXP-014, EXP-022 and EXP-023 tested running keys from K4 itself, the Kryptos
alphabet, the carved tableau and Morse material, each with **fixed** arithmetic. EXP-035
is new in both respects: the source was unavailable, and `f` is arbitrary rather than a
fixed letter-to-number rule. EXP-034 covered text-dependent keys drawn from K4's own
ciphertext at a lag; EXP-035 draws from a *different* text.

## Declared source streams

| id | definition | length |
|---|---|---|
| `above` | rows 1–24 concatenated in reading order | 745 |
| `above_rev` | `above` reversed | 745 |
| `k12` | rows 1–14 | 435 |
| `k3` | rows 15–24 plus row 25 up to and including its `?` | 337 |
| `full28` | rows 1–28 in reading order | 869 |
| `full28_rev` | `full28` reversed | 869 |

`k12` carries the unresolved 432-vs-435 letter discrepancy recorded in
`data/cipher_side_rows.json`; any verdict touching `k12` must repeat that caveat.

## Declared question-mark rules

The four `?` characters are part of the engraved row text. All three handlings are
declared now, before any result:

- `retain` — `?` is a 27th source symbol, so `f` is defined on 27 symbols;
- `strip` — `?` characters are removed from the stream before indexing;
- `block` — a case is rejected outright if any constrained position draws a `?`.

## Declared index maps

- **G1 `linear`** — `g(i) = offset + i`, every offset for which the whole 97-character
  window lies inside `S`. **No modulo wrapping.** This is explicit because EXP-029's
  audited defect was exactly a promised-bounded window that silently wrapped.
- **G2 `rowlocal` (TEXTUAL, NOT GEOMETRIC)** — `g(i)` = the character at the same
  row-local index, `k` rows earlier, for `k = 1…24`, under three index conventions:
  `left` (index from the row start), `right` (index from the row end), `centred`
  (index shifted by `floor((len(row_above) − len(row_of_i)) / 2)`). Positions whose
  target row is too short are unconstrained and are counted as such.

  **G2 is declared as a text-order family, not a physical claim.** Its asymmetry is stated
  now: a negative across all three conventions eliminates the rule *as a text rule*
  regardless of which alignment is physically true, whereas a positive would be
  **uninterpretable** without the geometry evidence of Request 4 and would not be
  promoted, pursued, or reported as support for any physical model.

## Free parameters and size

6 streams × 3 `?` rules × 12 conventions × (offsets for G1, or 24 displacements × 3
conventions for G2). Offsets number 649 for `above`, 773 for `full28`, and so on. Total on
the order of 10⁵ cases, every one decided exactly. Duplicate streams arising from `strip`
on a `?`-free span are deduplicated by hashing the realised (stream, index map) pair.

## Exact criterion, and the EXP-034 invariant

A case is FEASIBLE iff no two constrained positions drawing the same source symbol force
different key values.

**The usable-constraint count must be computed over every constrained position before any
verdict is formed.** No early return on first contradiction may influence whether a case
counts as decidable. This is the invariant EXP-034 established after that exact bug, and
the verifier asserts it.

Cases with **≤ 3** usable constraints are **UNDECIDED** and are excluded from every
elimination claim. Threshold fixed now.

## Failure statement

If every sufficiently-constrained case contradicts: **no key that is an arbitrary function
of a single symbol of the authoritative cipher-side text, taken at a fixed linear offset
(G1) or at the same row-local index a fixed number of rows above (G2), can produce K4 from
a plaintext carrying the public cribs, under the 12 committed conventions.** This does not
touch two-symbol functions, position-modulated `f`, resets, non-shift combiners,
transposition-composed architectures, fractionation, or any physically-aligned model.

## Controls

- **Planted positives** for every stream, `?` rule and index map, with a random `f`
  including a deliberately non-injective one, synthesised with independent arithmetic; the
  detector must report FEASIBLE and recover `f` on every constrained symbol.
- **Adversarial negatives** must be *capable* of changing the verdict: the corrupted
  position is chosen from a source symbol that actually appears at two or more constrained
  positions. Cases with no such symbol are not counted, rather than counted as passes.
  This follows the EXP-033/034 lesson that a control which cannot affect the verdict is
  not a control.

## Verifier

`audit/verify_exp035.py`, importing neither the experiment nor `k4lib`. It rebuilds the
row strings from `data/cipher_side_rows.json`, re-derives the conventions from first
principles, reconstructs every stream and index map **independently**, re-decides every
case, asserts that constraint counts are verdict-independent, and replants its own
positives so that a rubber-stamp verifier is excluded.

## Prohibited post-hoc expansions

No second source symbol, no offset-dependent or row-dependent `f`, no relaxation of the
consistency criterion into a score, no lowering of the constraint threshold, no addition
of alignment conventions after seeing results, and no promotion of a G2 hit into a
physical claim.
