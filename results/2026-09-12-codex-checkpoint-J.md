# Checkpoint J — three target-era faces frozen; multi-face test negative

Continued from Checkpoint I on codex/k4-continuation. K4 remains unsolved.
No EXP-029 or EXP-030 rerun. Main and Claude's branch remain untouched.

## Image identification and evidence

All three uploads were read separately at native resolution and cropped for closer
inspection with ordinary interpolation only, no generative enhancement or OCR
completion. The Picture Alliance collection page and linked preview images were
then fetched and visually matched: J01 is 16008401; J02 is 16008415. This establishes
image identity beyond the filename. Both publisher captions date them 4 Nov 1989.
J03 matches HanisauLand asset 153695.jpg; its Picture Alliance accession remains
UNKNOWN. Its publisher caption dates it to the same day and credits PA / akg.
A larger 4065x2575 publisher version of J03 was retrieved and inspected.

All original uploads and the larger source are preserved with SHA-256 hashes.
They lack embedded EXIF/IPTC identification in the uploads. The exact provenance,
per-image roles, ordered observations, uncertainty and conflicts are recorded in
[data/weltzeituhr_checkpoint_J.json](../data/weltzeituhr_checkpoint_J.json) and
[the image audit](../docs/checkpoint-J-image-audit.md).

**Retraction: ATHEN is present**, between SOFIA and NIKOSIA on UTC+2. The inherited
absence claim was a misreading; it cannot support a historical maintenance theory.
This does not establish when ATHEN was added. CET's original frozen 120-letter
transcription remains unchanged and is independently corroborated by these images.

New complete faces:

| Face | Upper letters | Lower letters | Total | Evidence |
|---|---:|---:|---:|---|
| UTC+0 | 48 | 33 | 81 | Both band ends visible; five lower names |
| UTC+1 | 62 | 58 | 120 | Matches the prior frozen CET face |
| UTC+2 | 33 | 38 | 71 | ATHEN resolved; lower ends visible |
| Combined arc | 143 | 129 | **272** | Physical adjacency visible in both close views |

Every line is preserved in visual order, not sorted or filled from modern data.
UTC+3's upper list is readable; its lower list is partial, with exact-spelling
UNKNOWNs and an ANTALYA/ANKARA conflict against the inherited reading. That conflict
is retained explicitly. UTC+3 is not used in any experiment.

## Registration before execution

Local freeze/preregistration commit: 342dd7a. Published preregistration: d8a55d3.
A checksum check caught truncation of two JPEG transfers during publication; commit
5cb7b78 repairs the uploaded bytes and verifies their exact blob hashes. **No search
ran until after this repair.** Preregistration, frozen transcription and parameters
were unchanged. The published and local evidence trees were compared before running.

Regression guards pin every accepted line, sector order, dates, completeness,
photograph hashes, unchanged CET and the unresolved UTC+3 exclusion.

## EXP-031 — exact declared model

Concatenate all three faces in visual left-to-right or reverse sector order (2),
reading each face's bands upper/lower or lower/upper uniformly (2). Read the resulting
272-letter tape forward or fully reversed (2). Admit every full 97-letter window
that crosses at least one face boundary, with no modulo wrapping and no unknown
sector. This yields **1,216 unique windows**, including the relevant two-face
subwindows. Both key alphabets and all 12 existing shift conventions give
**29,184 cases**. No single-face full-message window is rerun.

Success criterion, fixed before search: exact 24/24 public crib reproduction.
Positive controls: **384/384 passed**, all traversal-label endpoints, key alphabets
and conventions. Synthetic encryption uses independent arithmetic.

**Result: zero exact hits.** Histogram:

| Crib matches | Cases |
|---:|---:|
| 0 | 11,487 |
| 1 | 10,640 |
| 2 | 5,075 |
| 3 | 1,588 |
| 4 | 339 |
| 5 | 48 |
| 6 | 5 |
| 7 | 2 |

The maximum is recorded without significance claims or follow-up tuning.
All windows, aliases and scores are saved. A separate verifier, importing neither
the experiment nor k4lib, independently reconstructs **all 1,216 windows** and
recomputes **all 29,184 scores**, checking coverage and hashes: PASS.

Grade: **EXHAUSTIVELY ELIMINATED WITHIN THE DECLARED MODEL**, conditional on the
transcription and public crib inputs. No candidate mechanism, no plaintext
recovery, no external-verifier submission. Confidence decreases in this particular
multi-face direct running-key construction, not quantitatively in all clock ideas.

## Scope and next direction

Still open: whole-band-first constructions, alternating-band paths, position-varying
sector selection, dynamic clock-state keys, transposition, fractionation, arbitrary
key alphabets and unrelated K4 architectures. No full-drum inference is justified.
The images show broadly the same CET side, not a new 45–90 degree view.

The primary task is complete: these images did unlock a new multi-face experiment,
and it has been run and independently checked. No further photograph is required
for that experiment. The next highest-information analytical step is to specify
and count a structurally different band-routing or clock-state model before
scoring, comparing its constraints against the now-known arc. Do not keep adding
parameters to chase the two 7/24 cases. UTC+3 remains an evidence subtask, and no
unverified accession is invented as a supposedly guaranteed better viewpoint.

## Reproduce Checkpoint J only

```sh
python audit/verify_checkpoint_J.py
python experiments/exp031_multiface.py
python audit/verify_exp031.py
```

Frozen evidence: data/weltzeituhr_checkpoint_J.json.
Registration: docs/exp031-preregistration.md.
Results: results/exp031/{windows,scores,summary}.json.
No old search needs to run to reproduce this checkpoint.
