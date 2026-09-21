# Checkpoint AI — physical tableau / alphabet-panel verification

Date: 2026-09-13
Branch: `codex/k4-continuation`
Starting HEAD: `82b6ac77dd8cd744ca26846ad1a501d5847117be`

## Decision

**NO previously unmodeled artifact feature independently specifies a finite, non-vacuous
cryptographic rule. NO EXP-040 IS JUSTIFIED. K4 remains UNSOLVED.**

One exact textual anomaly is established: the CIA institutional transcription contains one
extra terminal `L` on the `N`-labeled tableau row. The admitted installed-sculpture photographs
do not independently resolve that terminal cell or its spacing. Even granting its physical
existence, the `L` supplies no unique cipher family, dimension, alphabet, alignment, padding,
matrix construction, stage placement, or mask. `HILL` is therefore **merely possible after an
additional alignment choice, not physically forced**.

## Method and frozen representations

`audit/checkpoint_AI.py` constructs the ideal tableau before comparison. It uses the canonical
project alphabet, unchanged:

`KRYPTOSABCDEFGHIJLMNQUVWXZ`

The ideal representation is:

- top and bottom header: ordinary `A-Z` followed by `A-D`, 30 characters each;
- 26 labeled body rows `A-Z`;
- each body row: its one-letter ordinary-alphabet row label, followed by the corresponding
  left rotation of the 26-letter KRY alphabet, followed by that rotation's first four symbols;
- 31 characters per body line;
- 28 lines total;
- **866 characters** (`2×30 + 26×31`).

The algorithm was not altered to fit the sculpture. The CIA's 28 `Panel 2 - Cipher ( Text
Version )` lines were then entered verbatim as the **TEXTUAL ARTIFACT TRANSCRIPTION**. No spaces,
letters, or row boundaries were normalized.

## Exact count and complete textual difference map

The CIA transcription contains **867 alphabetic characters**. The independently regenerated
legacy value 867 is therefore:

`866 ideal characters + 1 extra textual L = 867`.

The complete ideal-versus-CIA-text difference map has exactly one entry:

| Type | Line | Body row | Full-line column (0-based) | Body column (0-based) | Expected | CIA text | Confidence | Consequence |
|---|---:|---|---:|---:|---|---|---|---|
| extra terminal | 14 | N (body index 13) | 31 | 30 | no cell | L | VERIFIED textual transcription only | none uniquely specified |

All other 866 positions match. There are zero substitutions, zero deletions, and no other
textual insertions, row-length departures, header changes, or label changes. The adjacent CIA
line lengths are `M=31, N=32, O=31`; the extra symbol is outside the normal N-line boundary.

The full 28-row and cell-level record is `data/tableau_checkpoint_AI.json`. It preserves ideal,
CIA-text, and physical-photo fields separately.

## Physical-image verification and confidence

The evidence hierarchy and hashes are recorded in
`docs/external/checkpoint-AI-tableau-source-ledger.md`.

The strongest installed-original image inspected is the LOC Carol M. Highsmith master,
3384×4283. It verifies a curved copper screen with horizontal letter rows. Its viewpoint is
strongly oblique, the panel curves away, and the terminal area is foreshortened/partly occluded.
The CIA 980×1305 close view is also oblique and does not expose the complete terminal edge.

Consequently:

- independently verified physical tableau size: **UNKNOWN**;
- extra terminal `L` visibly present on the original: **UNKNOWN**;
- exact terminal spacing and appendage treatment: **UNKNOWN**;
- every cell-level photograph reading in the dataset: **UNKNOWN**, rather than inferred;
- photograph-supported geometry: horizontal row organization and curved surface;
- unsupported geometry: an orthogonal rectangular lattice, equal pitch, common vertical
  columns, or a fixed diagonal through the terminal `L`.

This is the strongest conclusion the public institutional pixels support. A textual
institutional transcription is not silently upgraded into a physical measurement.

## Alignment and the `HILL` claim

The physical evidence does not establish equal-width columns. Sanborn's fabrication account
instead establishes individually placed metal stencils on scribed horizontal baselines. That
process is consistent with locally orderly rows but does not force shared x-coordinates across
rows. Curvature and perspective make apparent vertical/diagonal alignments viewpoint-dependent.

The extra `L` proposition and the `HILL` interpretation therefore have different statuses:

| Proposition | Status |
|---|---|
| CIA textual transcription ends N row with an extra L | **VERIFIED** |
| Original installed copper visibly has that cell | **UNKNOWN from admitted images** |
| The L occupies an ordinary 32nd fixed-width cell | **UNKNOWN** |
| A physically justified vertical/diagonal relation spells HILL | **NOT ESTABLISHED** |
| HILL uniquely instructs a Hill cipher | **NOT ESTABLISHED** |

No diagonal, rectangle, route, offset, acrostic, or alternative alignment was scanned. Even if
a chosen projection can display `HILL`, its null would have to include that geometry choice.

## Models / maquettes

No admissible cell-addressable maquette evidence was available. The repository's later
KRYPTOS-keyed proof and Cyrillic tableau-style sheet are not original-artifact models and cannot
settle the N-row terminal. Whether a Sanborn model contains the L, has the same margins, or was
mechanically generated remains **UNKNOWN**.

## Cryptographic gate and prior coverage

The anomaly is intentional-looking only in the limited sense that the CIA text has one isolated
extra letter. That is insufficient to select a decoder.

A Hill interpretation would still leave at least the block dimension, alphabet, block
alignment, padding/tail rule, linear versus affine form, matrix or matrix-construction rule,
stage placement, and any outer/inner mask unspecified. There is therefore no honest finite
search-space or false-positive number to calculate: the architecture is not selected.

Prior scope matters as well:

- EXP-007 exactly rejected direct linear and affine Hill blocks of sizes 2 and 3 under STD/KRY
  indexing at every alignment. Block size 4 was only partly testable and several cases were
  explicitly vacuous/underdetermined.
- Checkpoints AA/AE show that a free Hill-like digraphic inner map behind a free outer mask is
  vacuous when the crib blocks do not repeat.
- EXP-014 already tested the mathematically generated 26×26 KRY tableau as a running stream in
  eight declared read orders and all alignments/conventions. It did not test the extra-L
  transcription, but the L supplies no reproducible stream-reading rule, so that omission is
  not a selected new family.

Thus a Hill run would either duplicate a closed direct scope or invent multiple unsupported
parameters. A negative would prove only the invented completion; a positive would be exposed to
unpriced selection and route/alignment multiplicity.

## Answer to the central question

The original sculpture is not yet measured precisely enough to verify every physical cell, but
the strongest official textual record is precise enough to isolate its sole departure from the
generated tableau: one extra N-row terminal `L`. **No verified departure supplies an unambiguous
cryptographic instruction.** Checkpoints AE and AH do not change. No EXP-040 preregistration is
created and no cipher experiment was run.

## Exactly one highest-information next action

Obtain **one orthographic, full-resolution photograph or measured shop transcription of the
original tableau's N-row terminal edge, with the M/N/O row endings and a scale in the same
frame**. This single acquisition would decide physical presence, ordinary-cell versus appendage
spacing, and local cross-row alignment without fitting any K4 crib or scanning routes.
