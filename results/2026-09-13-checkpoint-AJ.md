# Checkpoint AJ result — physical K4 ciphertext-layout audit

**Result: NO EXP-040 JUSTIFIED. K4 remains UNSOLVED.**

- Canonical linear K4 remains the fixed 97-character string.
- The CIA published textual placement is exactly `OBKR` plus three 31-character rows, but
  `OBKR` is the terminal four characters of panel row 25, not an isolated engraved row.
- The LOC master directly shows adjacent physical rows beginning `ECDM`, `UOX`, `TWT`, and
  `VTT`; no separate row exists between ECDM and UOX.
- The row-25 terminal `?OBKR` and the complete right endpoints are not adequately visible.
  Exact physical K4 row count and exact physical row lengths therefore remain **UNKNOWN**.
- `4/31/31/31` is verified as institutional textual placement, not as a complete metric survey.
- No fixed column lattice, shared margins, systematic stagger, pitch distribution, or significant
  spacing anomaly is established.
- No 96-gap scan, route search, diagonal search, overlay, column read, or spacing-key test was
  performed.
- EASTNORTHEAST maps to panel row 26 columns 17–29. BERLINCLOCK maps to row 27 columns
  28–30 and row 28 columns 0–7, crossing the published break as `NYP | VTTMZFPK`. No physical
  spacing feature at either crib is measurable.
- Visible K4 baselines and stencil forms do not establish a difference from adjacent K1–K3
  engraving; quantitative control is unavailable.
- Row-reset and ordinal-column interpretations are already covered by EXP-020, EXP-032,
  Checkpoint T, and AH. A visible line break does not select reset behavior.
- No physical feature supplies a new finite cryptographic parameter. AE/AH/AI do not change.
- Exactly one next action: obtain one orthographic, scaled image or shop drawing showing both
  endpoints of physical rows 25–28 and adjacent control rows.

Reproduce the representation audit:

```text
python audit/checkpoint_AJ.py
python audit/checkpoint_AJ_verify.py
```

Expected verifier output:

```text
PASS: canonical/textual mapping exact; physical unknowns preserved; no route, spacing key, or cipher experiment introduced
```
