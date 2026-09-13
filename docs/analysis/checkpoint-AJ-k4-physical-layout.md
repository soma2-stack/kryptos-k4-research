# Checkpoint AJ — physical K4 ciphertext-layout audit

Date: 2026-09-13

Branch: `codex/k4-continuation`

Starting HEAD: `3ddbd7aba4a3af2c0d87c98ac587fb9d0266edbb`

## Decision

**The physical K4 engraving does not reveal a previously unmodeled, reproducible parameter that
turns an open Checkpoint-AE class into a finite, non-vacuous family. NO EXP-040 IS JUSTIFIED.
K4 remains UNSOLVED.**

The strongest new measurement is representational, not cryptanalytic: the LOC master directly
shows adjacent physical rows beginning `ECDM`, `UOX`, `TWT`, and `VTT`. It rules out `OBKR` as
an isolated engraved row. But the terminal end of the `ECDM` row is not adequately visible, and
the photograph does not support exact physical counts, pitch measurements, or a fixed column
lattice.

## Three representations kept separate

### 1. Canonical linear K4

The canonical 97-character string in `data/k4.json` remains unchanged.

### 2. Published textual layout

The CIA institutional text places K4 as:

```text
panel row 25, cols 27-30   OBKR
panel row 26, cols 0-30    UOXOGHULBSOLIFBBWFLRVQQPRNGKSSO
panel row 27, cols 0-30    TWTQSJQSSEKZZWATJKLUDIAWINFBNYP
panel row 28, cols 0-30    VTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR
```

The segment lengths are exactly `4/31/31/31`, concatenate to the canonical K4, and are
independently regenerated in `data/k4_physical_layout_checkpoint_AJ.json`. This is a verified
**textual placement**. It is not a metric claim about equal physical widths or columns.

### 3. Physical engraving

The LOC image identifies four adjacent physical row starts:

```text
ECDM...
UOX...
TWT...
VTT...
```

There is visibly no additional row between `ECDM…` and `UOX…`; `OBKR` is therefore not a
separate physical row. The image does not resolve the far terminal `?OBKR`, so it does not by
itself prove exactly where K3 ends and K4 begins within row 25.

Accordingly:

- physically identified starts of K4-only rows: the three beginning UOX/TWT/VTT;
- exact physical number of rows occupied by K4: **UNKNOWN from pixels alone** because the
  row-25 terminal boundary is not visible;
- exact physical row lengths: **UNKNOWN**;
- `4/31/31/31`: **institutional textual convention/placement, not yet a complete physical
  measurement**.

This prospective wording supersedes any current use of “verified geometry” to mean measured
character centers. It does not rewrite historical Checkpoint T, whose computations use the
institutional row indexing explicitly.

## Horizontal geometry

No defensible coordinate dataset could be extracted. The strongest image has all three limiting
conditions at once: curvature, oblique perspective, and incomplete endpoints. There are no
surveyed control points or scale. A single planar homography was rejected as physically invalid,
and no local rectification was attempted because the required row terminals remain outside or
foreshortened.

Therefore the following are all **UNKNOWN**:

- row left/right artifact x-positions and total widths;
- full character-center sequences;
- mean pitch and pitch variance;
- absolute or normalized inter-character gaps;
- terminal isolation and indentation;
- statistically significant tight/loose pairs.

No 96-gap scan was conducted. Thus there is no multiple-comparison problem to correct and no
spacing anomaly to report. “No anomaly established” is not “uniform spacing established.”

## Vertical geometry

Horizontal baselines are visible and independently supported by Sanborn's fabrication account.
A common vertical lattice is not. The curved surface and perspective cause apparent x-alignments
to change across the frame; individual stencils were placed by hand along scribed row guides.

No proposed column can be assigned a residual error relative to pitch or glyph width because
neither pitch nor artifact-plane x-coordinates are measured. The defensible classification is:

- shared horizontal row organization: **VERIFIED**;
- shared left or right margin: **UNKNOWN**;
- regular rectangular lattice: **NOT ESTABLISHED**;
- stagger/centering/systematic offset: **UNKNOWN**;
- local visual alignment: present in places but cryptographically non-selective.

No vertical read, diagonal, overlay, route, spiral, acrostic, or column extraction was tested.

## Spacing and character-form audit

No objectively measurable K4 spacing outlier survives the source limitations. The GSA full-view
preview is too small; the CIA close view does not expose K4 row endpoints; the LOC master lacks
the terminal geometry and calibration required for pitch statistics. No anomaly can therefore
be claimed across two independent images.

The visible letters are cut-through stencil forms. Bridges and small cutting variations are
structurally expected for metal integrity and hand filing. No reversed glyph, distinct K4-only
stencil, restored/damaged K4 letter, or intentional marking was verified. Damage/restoration
status at K4 is **UNKNOWN**.

Against the best empirical control—the adjacent K1–K3 rows in the same LOC photograph—K4's
visible baselines and glyph construction appear continuous with surrounding practice. The view
does not permit a calibrated distributional comparison, so the strict conclusion is **no
verified physical difference from normal engraving practice**, not proof of identity.

## Crib locations on the artifact

Indices remain fixed. In the published textual mapping:

| Crib | K4 interval | Ciphertext | Panel placement | Boundary fact |
|---|---|---|---|---|
| EASTNORTHEAST | `[21,34)` | `FLRVQQPRNGKSS` | row 26, columns 17-29 | wholly within one textual/physical row; neither begins nor ends at its boundary |
| BERLINCLOCK | `[63,74)` | `NYPVTTMZFPK` | row 27 columns 28-30, then row 28 columns 0-7 | crosses the published row 27→28 break as `NYP | VTTMZFPK` |

The source images do not supply reliable gap measurements at those columns. No crib letter can
be said to coincide with unusual spacing. The two spans occupy different portions of the curved
screen, and no exact geometric relation between them is measured.

## Line breaks as parameters and prior coverage

Physical rows make row-aware hypotheses discoverable, but they do not choose what a cipher does
at a row boundary. Reset, continuation, row-local key phase, row-constant key, transposition
width, and route are different operations all compatible with the same visual break.

The obvious finite interpretations are already addressed:

| Interpretation | Shared parameters / crib constraints | Prior result | AJ consequence |
|---|---|---|---|
| reset a declared periodic shift family at published K4 row boundaries | varies by declared period; exact equality conflicts derived in EXP-020/T | negative across registered row/reset variants and 12 conventions | do not reopen |
| arbitrary key by ordinal row-column slot | 31 possible values; 22 exercised by cribs; 2 independent equality constraints | EXP-032/T: all 12 conventions fail | already tested; low constraint density |
| one additive value per crib-bearing physical row | 3 exercised values; 21 equalities | AH: finite but physically unsupported constancy | line breaks do not select constancy |
| arbitrary row-and-column dependence | 24 distinct crib arguments; 0 constraints | AH/AE: vacuous | no experiment |
| row-width transposition | route/order/alignment remain free | broad declared transposition scopes tested elsewhere; physical width not measured | no artifact-selected permutation |

Thus the row break is evidence that a reset **could** be defined, not evidence that one was.

## Cipher gate

| Question | Result |
|---|---|
| Objectively verified feature? | Three K4 row starts, adjacent preceding ECDM row, horizontal row organization, curved cut-through copper |
| Intentional-looking beyond fabrication? | No; these are the ordinary layout and fabrication method |
| Unique/tightly bounded operation? | No |
| Exact new parameter recovered? | None |
| Alternatives remaining? | reset/continue/phase/route/spacing interpretations remain unconstrained |
| Already-tested obvious family? | Yes: EXP-020, EXP-032, Checkpoint T, AH |
| New independent crib constraints? | None beyond the existing 24-letter row geometry |
| Meaning of a negative? | Only the arbitrarily selected use of layout, not a sculpture-specified family |

No physical feature passes the AE/AH experiment gate. Checkpoints AE, AH, and AI remain
unchanged. No EXP-040 preregistration was created and no cipher experiment was run.

## Exactly one highest-information next action

Acquire **one orthographic, scaled, full-resolution image or measured shop drawing that shows
both endpoints of physical rows 25–28 in the same coordinate system**. It must resolve
row 25's terminal `?OBKR`, the starts and ends of rows 26–28, and include enough surrounding
rows for an empirical kerning control. This single artifact would decide physical row counts,
margins, pitch/gap distributions, and column-lattice claims without selecting a cipher.
