# Checkpoint AI result — physical tableau / alphabet-panel verification

**Result: NO EXP-040 JUSTIFIED. K4 remains UNSOLVED.**

- Ideal tableau: 28 rows, **866** characters.
- CIA textual artifact transcription: 28 rows, **867** alphabetic characters.
- Complete textual difference map: exactly one extra terminal `L`, on line 14 / N-labeled
  body row 13, full-line column 31 (all zero-based). All other 866 positions match; no
  substitutions or omissions.
- Independently verified physical count: **UNKNOWN**. The LOC installed-original master and CIA
  close image are oblique and do not provide a complete orthographic cell survey.
- Extra-L physical presence and spacing: **UNKNOWN from admitted photographs**. Its presence in
  the CIA text is verified and kept separate.
- Geometry: horizontal rows and a curved copper surface are visible; uniform pitch, a common
  vertical lattice, and a fixed diagonal are not established.
- `HILL`: **not physically forced** and not an experiment selector. It leaves dimension,
  alphabet, alignment, padding, matrix construction, stage placement, and masking free.
- Models/maquettes: no admissible cell-addressable evidence was available; their agreement with
  the terminal L remains unknown.
- Prior coverage: direct Hill 2×2 and 3×3 scopes were closed by EXP-007; hidden free digraphic
  stages are vacuous at AA/AE; the generated tableau stream was tested by EXP-014. No prior
  result was rewritten.
- Checkpoints AE/AH: unchanged.
- Exactly one next action: acquire one orthographic, scaled image or shop transcription showing
  the original M/N/O tableau row endings.

Reproduce:

```text
python audit/checkpoint_AI.py
python audit/checkpoint_AI_verify.py
```

Verifier output:

```text
PASS: 28 rows, 866 ideal chars, 867 CIA-text chars, one textual-only terminal L; no photo cell inferred
```
