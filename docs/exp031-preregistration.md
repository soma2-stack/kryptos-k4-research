# EXP-031 preregistration — three adjacent target-era faces

Frozen evidence: data/weltzeituhr_checkpoint_J.json. UTC+0 (81 letters), UTC+1
(120), UTC+2 (71), total 272. All lines and band ends are transcribed directly
from J02 and J03-source. UTC+3 is excluded. Original CET block is unchanged.
This document and the experiment implementation are committed before execution.
Only geometry/window counts, not crib scores, have been computed at registration.

## Hypothesis and motivation

A person copies successive adjacent faces, each upper then lower (or lower then
upper), to obtain a running key. This is the multi-face continuation of the
object-motivated per-sector reading in EXP-024. It uses newly complete neighbouring
faces, not an alternative spelling or parameter fit to EXP-029/030's maxima.
The hour numerals are not used to identify sectors or choose a starting point.

## Exact construction and parameters

- Evidence-determined face order: visual left-to-right UTC+0, UTC+1, UTC+2.
- Sector traversal: that order or its reverse (2). No claim about compass handedness.
- Within each face, top-to-bottom lines in the frozen order; band order upper/lower
  or lower/upper, the same choice for every face (2).
- Normalize uppercase A-Z, dropping spaces and blank lines; no spelling substitution.
- Read the resulting 272-letter string forward or entirely reversed (2).
- Start: every integer offset 0..175 in that oriented string, admitting only windows
  whose full 97 characters touch at least TWO physical faces. No modulo or seam
  wrap. No window enters an unknown band or face.
- Deduplicate identical complete 97-letter key windows before scoring. Retain all
  construction aliases. Count computed before scoring: **1,216 labelled windows,
  1,216 unique windows**.
- Key alphabet: STD or KRY (2); plaintext/cipher alphabet and combiner: existing
  all_conventions() (12). **29,184 total cases.** No other fitted parameters.
- The combined 3-face enumeration includes qualifying 2-face subwindows. There is
  no separate duplicated search over two-face tapes.

No single-face full-message window is tested; EXP-029 and EXP-030 are not rerun.
A cross-boundary full window whose crib positions happen to lie in one face is
still retained: the declared model concerns the complete 97-character message.

## Gate and controls

Success gate: exact simultaneous 24/24 public crib reproduction. A crib fit is only
a candidate mechanism, not a solution. No language scoring, tuning, additional
plaintext assumptions, significance assigned to maxima, or verifier submission.
Failure: zero exact hits after all 29,184 cases; scoped elimination conditional
on this transcription, not a verdict on the clock or all multi-face constructions.

Before the real scan, plant synthetic ciphertext with X filler and public cribs
using the first and last legal windows of each of the eight traversal labels,
both key alphabets and all 12 conventions: **384 controls**. Generate by independent
modular arithmetic; require the production scorer to recover 24/24 in every case.
Abort on any failed control or frozen-evidence guard.

Preserve every window and alias, all scores in a documented stable order, input and
output hashes, histogram, exact hits, and positive-control count. A separate
verifier must reconstruct all admitted windows without importing the experiment,
recompute every score with independent formulas, and confirm complete coverage.
No statistical claim is needed for a complete zero-hit elimination. Tests may be
correlated; 29,184 is a case count, not a count of independent hypotheses.

Excluded: whole-band-first around several sectors, alternating single-band sectors,
per-face variable band orders, nonconstant or numeric clock-state routing,
transposition/fractionation, unknown UTC+3 data, arbitrary key alphabets and a full
drum. A full-drum loop cannot be inferred from a three-face arc.
