# Checkpoint AK — prospective correction: physical row 25 endpoint

Date: 2026-09-13
Branch: `codex/k4-continuation`
Starting HEAD: `99acecd79dd95de382e8da0054e7c7f81118bd24`

## Decision

**A new public photograph prospectively corrects one factual uncertainty recorded in Checkpoint AJ. It does not change the cryptanalytic verdict. NO EXP-040 IS JUSTIFIED. K4 remains UNSOLVED.**

Checkpoint AJ correctly established that `OBKR` is not a separate engraved row, but left the far endpoint of physical panel row 25 unresolved from the then-admitted pixels. A later public source closes that one measurement gap.

## Newly verified physical fact

WIRED's 7 March 2025 article *AI Thinks It Cracked Kryptos. The Artist Behind It Says No Chance* publishes an artist-supplied photograph of the installed Kryptos sculpture. The publicly downloadable image is 2400 × 1867 pixels and is credited `Courtesy of the Artist`.

In that physical photograph, the terminal portion of the relevant ciphertext row is visibly readable as:

```text
...DOHW?OBKR
```

The `R` is the final visible character on that physical text line, and the following ciphertext row begins below it. Therefore the following propositions are now supported by direct public physical-image evidence:

1. physical panel row 25 ends in `?OBKR`;
2. `OBKR` follows the question mark on the same engraved/cut row;
3. `OBKR` is not a separate physical engraved row.

This is a prospective correction to AJ's narrower statement that the row-25 terminal endpoint was still unknown from pixels. **AJ is preserved unchanged as a historical checkpoint.**

## Source provenance

- Publication: WIRED
- Article date: 2025-03-07
- Article: `https://www.wired.com/story/plaintext-kryptos-code-artificial-intelligence/`
- Asset identifier: `67c9dd0622006643b146663d`
- Retrieved filename reported by the acquisition audit: `Plaintext-Kryptos-Solved-AI-Business.jpg`
- Displayed credit: `Courtesy of the Artist`
- Public image dimensions: 2400 × 1867
- SHA-256 reported for the retrieved JPEG: `b337a2c0c37e6e5d17fb8914dcc7bd4d3e08bae400073f4550ce340c9c363fe9`

The publication credit establishes an artist-supplied provenance chain, but the photographer is not identified. This source is sufficient for the short high-contrast endpoint reading; it is not treated as a surveyed orthographic measurement.

## What remains unknown

The frame is oblique, the copper is curved, and substantial parts of the lower rows are obstructed or insufficiently exposed. It does **not** establish:

- exact full engraved lengths of physical rows 26–28;
- whether rows 26–28 each contain exactly 31 physical characters;
- common left/right margins across rows 25–28;
- uniform character pitch;
- exact cross-row column correspondence;
- whether the textual `4/31/31/31` segmentation represents intentionally measured physical geometry.

Accordingly, the new observation does not recover a cryptographic parameter.

## Cryptanalytic consequence

None beyond closing the artifact-measurement uncertainty above.

The same visible row ending remains compatible with many mutually incompatible mechanisms: continuation, reset, row-local phase, transposition, or no cryptographic use of the line break at all. It therefore does not select a finite family, add a new shared parameter, or create a new crib constraint beyond those already represented in Checkpoints T, AH, and AJ.

Checkpoints AE, AH, and AI remain unchanged. AJ's cryptanalytic conclusion also remains unchanged.

**NO EXP-040 preregistration is created and no cipher experiment is run.**

## Exactly one highest-information next action

Request the original pre-publication source for WIRED asset `67c9dd0622006643b146663d`, including any larger uncropped file or companion artist-supplied frames from the same set, specifically asking for a frame that exposes both endpoints of physical rows 25–28. Such a source could settle the remaining row-length, margin, pitch, and column-lattice questions without introducing a cipher hypothesis.
