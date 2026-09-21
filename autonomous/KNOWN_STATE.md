# Compact canonical K4 knowledge state

Updated 2026-09-14 from the repository's prospective checkpoints. This file is memory, not a
replacement for historical checkpoint documents. Read it before selecting work.

## Current status

K4 remains UNSOLVED. No complete plaintext, key, or deterministic 97-character method is
admitted. Do not run EXP-040 overnight.

## Canonical ciphertext and verified cribs

```text
OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR
```

Length is 97. Verified zero-based anchors are `[21,34) = EASTNORTHEAST` (ciphertext
`FLRVQQPRNGKSS`) and `[63,74) = BERLINCLOCK` (ciphertext `NYPVTTMZFPK`). There are 24 known
plaintext letters. Do not slide, extend, or infer additional plaintext.

## Canonical cryptanalytic frontier

Checkpoint AE remains canonical. Checkpoints AF–AL are prospective clarifications/audits and
did not justify EXP-040. Constraint density, shared parameters, and independently motivated
finite domains are required; compatibility is not evidence.

### Documented scoped negatives

- Pure transposition is impossible: crib multiplicity requires at least three E's while the
  ciphertext has two. This does not eliminate substitution-plus-transposition generally.
- EXP-020 / Checkpoint T: declared row-reset, row-structured traversal, and 12 shift/combiner
  conventions across periods 2–40 are negative. Physical row breaks do not choose reset.
- EXP-033: declared single transpositions composed with any fixed A–Z function are zero at the
  registered scope.
- EXP-036: declared periodic shift-family conventions, periods 2–23, with declared
  transpositions are zero at the registered scope; not a theorem about arbitrary 26x26 tables.
- EXP-037: preregistered standard Porta is negative. Quagmire I–III and Gronsfeld reduce to
  covered families; Quagmire IV needs an unsupported second alphabet.
- EXP-038: full-Z26 second-order affine self-evolving keystreams, message-aligned with no
  primer/warm-up, reset, reversed recurrence, plaintext/ciphertext feedback, or transposition, across
  12 committed shift conventions, are exhaustively negative; generic recurrence is not eliminated.
- EXP-039: ordered pairs from `{KRYPTOS, PALIMPSEST, ABSCISSA}` in standard no-padding double
  columnar transposition followed by a fixed monoalphabetic map are zero; double transposition
  generally is not eliminated.
- Standard Fractionated Morse, direct Gromark, Digrafid, and declared direct clock-source
  models were rejected at their documented scopes. Do not broaden those negatives silently.
- Free inner/outer masks, free polygraphic maps, arbitrary position functions, and arbitrary
  26x26 combiners are vacuous or underconstrained under the present crib geometry.
- EXP-040 (2026-09-21): propagating text-autokey is exhaustively negative at its registered
  scope — plaintext or ciphertext fed back, forward or reversed, primer 1–24 letters, 12
  committed conventions, both key-index alphabets, with and without physical-row reset at m<=3;
  2,592 exact decisions, 0 feasible, 3 controls pass, independently verified three ways. All
  keyword primers are subsumed (every primer value per chain was enumerated). This does NOT
  eliminate two-tap/mixed feedback, feedback through a non-identity function, feedback composed
  with a transposition, or primers longer than 24.
- Hidden trigraphic stages behind additive masks are refuted only for periods 1, 3, and 9 by
  the repeated crib trigrams; this is not a universal fractionation negative.

## Open frontier (Checkpoint AL)

Six practical classes were reviewed. The conditional top three are: (1) declared periodic
masks at p=24–26 (5/3/1 crib constraints), (2) two short masks around a fixed permutation
(about 7 constraints at the K1/K2 pair, more only when parameters are frozen), and (3) a
specifically declared low-state recurrence outside EXP-038. Structured fractionation and
deterministic non-position-preserving alignment remain open only as templates. Periods 27–29
receive zero current crib constraints. None has a puzzle-selected finite parameter set, so no
EXP-040 is justified.

**Autokey blind region (EXP-040, new).** In a propagating feedback model a ciphertext change
downstream of every crib position in its own chain is absorbed by the primer and is undetectable.
So a feedback family's power is bounded by crib **span**, not crib count: the tail beyond each
chain's last crib carries zero constraint. This is the feedback analogue of the period 27–29 blind
spot and should be quoted whenever a feedback model is proposed.

Useful authenticated missing-plaintext targets are indices 1, 3, 91, 93, 95, and 96. One
legitimate letter there would constrain the blind periods and materially increase information.

## Physical artifact state (AI–AK)

The ideal generated KRY tableau has 866 cells; the institutional CIA textual transcription has
867 characters. The only modeled textual difference is an extra terminal `L` on the N row; its
physical copper presence remains UNKNOWN. Checkpoint AI found no artifact-selected cipher rule.
Checkpoint AJ found that textual `4/31/31/31` is not a complete physical measurement, no fixed
column lattice or spacing key is established, and rows 26–28 endpoints remain unmeasured.
Checkpoint AK prospectively verifies from an artist-supplied WIRED image that physical row 25
ends `?OBKR`; `OBKR` is not a separate engraved row. Full physical row 26–28 geometry remains
unestablished. Do not infer routes, resets, or Hill from these facts.

## Public documentary state

ScheidtNova.doc is located only through public index metadata; its payload is not recovered and
its server-side status is unknown. The unedited 2005 Kim Zetter/WIRED Scheidt material is not
located. GBH Open Vault `V_3AC501960CC4454A8FD950703CBED5A9` resolves to AAPB
`cpb-aacip-15-1615gc34`, a 56:46 NOVA ScienceNow broadcast master, not a complete Scheidt
interview. The exact UGA/Peabody object remains a search-result lead only. PBS narration about
concealment before enciphering is editorial, not a Scheidt stage-order statement. Pending
outreach: GBH, Kim Zetter, TecSec/Ed Scheidt, and Elonka Dunin. Do not duplicate requests.

## Contamination boundary

Reject alleged full K4 plaintexts, leaked or claimed solutions, auction-secret material, private
K5 material, stolen/private documents, solution dumps, and sites primarily intended to reveal
claimed solutions. If encountered, stop reading, record only safe URL/domain and category in
`rejected-contamination.md`, and never quote plaintext.

## Operating rule

Every worker performs exactly one bounded, repository-novel investigation, records whether it is
NEW / CONFIRMATION / CONTRADICTION / ALREADY KNOWN / LOW VALUE / IDEA CANDIDATE / BLOCKED, and
does not promote a cryptanalytic claim without reviewer support. Historical files are immutable;
prospective corrections go in this memory and the ledgers.

