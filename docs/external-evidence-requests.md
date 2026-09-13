# External evidence requests (web-blocked in this environment)

This environment's egress refuses the hosts below; re-tested this session:
`www.nsa.gov` and `media.defense.gov` both return `CONNECT tunnel failed, response 403`.
Nothing here is guessed, reconstructed from memory, or substituted. Each request names
the source, what exactly is needed, and why the analysis is blocked without it.

---

## REQUEST 1 — the official 869-character cipher-side transcription (rows 1–28)

**Highest-value request. It unblocks a preregistered experiment that cannot otherwise be
run at all, and it is a grade-A primary source.**

| field | value |
|---|---|
| Source | National Security Agency, declassified Kryptos file |
| Title | *The CIA Kryptos Sculpture: A Summary of Previous Work and New Revelations in Working Toward Its Complete Solution* |
| DOCID | 4145037 (OIA/FOIA 65414), released 16 September 2014 |
| URL | `https://www.nsa.gov/portals/75/documents/news-features/declassified-documents/cia-kryptos-sculpture/KRYPTOS_Summary.pdf` |
| Also acceptable | DOCID 4145036, *The CIA KRYPTOS Sculpture* slides, `https://media.defense.gov/2021/Jul/12/2002760451/-1/-1/0/KRYPTOS_SLIDES.PDF` — its transcription slides carry the same material |
| Pages | printed p.4 Fig. 2, and pp. 13–16 Figs. 14–18 |

### Exactly what is needed

The **ciphertext** of the cipher side as typeset by NSA, row by row, rows 1 through 28 —
that is, the 869 characters comprising the K1, K2 and K3 ciphertext and the four
question marks, in engraved row order, with each row's exact character count. Row 25 is
already published in a source we hold (`ECDMRIPFEIMEHNLSSTTRTVDOHW?OBKR`); rows 1–24 are
the missing part.

Not needed and explicitly not wanted: any plaintext, any solution, any commentary
claiming to solve K4, and anything concerning K5.

### Why it matters

The corrected geometry (already verified here against the repository ciphertext: the
three quoted 31-character rows equal `K4[4:35]`, `K4[35:66]`, `K4[66:97]`; row 25 is 31
characters ending in `OBKR`; 32 + 27×31 = 869) places K4's rows 26–28 directly beneath 24
rows of *known* ciphertext, in the same 31 columns. That makes a specific, parameter-free
architecture testable for the first time: **a key drawn from the characters physically
above each K4 character** — the letter at (row − k, same column) for k = 1…24, or a
column-major reading of the panel above. It is finite (24 × 12 conventions × 2 alphabets
× a few readings ≈ 1,200 exact cases, zero free parameters), it is falsifiable by the 24
public cribs, and it is motivated by the division of labour the documentary record
describes — Sanborn did the physical and visual encoding himself.

Without rows 1–24 the key material does not exist in this repository. `data/mask_sources.json`
holds only *plaintexts* for K1/K2, flagged `verified: false`. Reconstructing the cipher
side from memory is exactly the failure mode that produced the retracted `LONDON`
misreading at Checkpoint H, so it will not be attempted.

### Status

Blocked. This subtask only. EXP-032 and EXP-033 were designed and executed without it.

---

## REQUEST 2 — the unedited 2005 Zetter/Scheidt interview material

| field | value |
|---|---|
| Source | Kim Zetter / WIRED (Condé Nast) |
| Published pieces | `https://www.wired.com/2005/01/inside-info-on-kryptos-codes/` and `https://www.wired.com/2005/01/questions-for-kryptos-creator/`, both self-described as partial transcripts edited for length and organisation |
| Needed | raw audio or full transcript, interviewer notes, questions cut from the published piece, drafts and fact-check correspondence |

**Exactly what is needed:** Scheidt's unedited words on (a) what distinguishes the fourth
process from the first three, (b) what "masking" meant operationally, (c) whether any
named system or family was discussed for K4, and (d) what Sanborn changed.

**Why it matters:** the published text supports only "four high-level processes, K1/K2
similar, K3/K4 different, K4 masks ordinary English access better". Every attempt to read
a primitive out of it — fractionation, Bifid, double transposition, autokey, Polybius,
matrix work — is unsupported, and this repository's model selection is currently choosing
among families on structural grounds alone.

**Status:** not established public. Lower priority than Request 1 precisely because it may
not exist in retrievable form, whereas Request 1 is a published PDF.

---

## REQUEST 3 — a target-era Weltzeituhr frame from a different bearing (carried forward)

Unchanged from Checkpoint J and still open: a 1985–1996 close frame rotated roughly
45–90° from the CET side, so UTC+3's lower band can be resolved and its
`ANTALYA`/`ANKARA` conflict settled. Candidate leads and the reasoning are in
`docs/codex-image-request.md`. This is now the *least* urgent of the three: EXP-029,
EXP-030 and EXP-031 have accumulated bounded negatives against direct clock-letter
running keys, so more of the same arc buys less than either request above.

---

## REQUEST 1 — FULFILLED (2026-09-12), with a correction

Rows 1–24 were supplied in `docs/external/checkpoint-K-nsa-cipher-rows-1-24.md` and are
now preserved and verified in `data/cipher_side_rows.json`. Three independent
corroborations passed: rows 15–25 give exactly 336 K3 letters; row 25 after its `?` is
exactly `OBKR` and rows 26–28 equal `K4[4:35]`, `K4[35:66]`, `K4[66:97]`; row 1 and row 15
are the canonical K1 and K3 ciphertext openings.

**The correction is accepted:** rows 1–24 hold 29–33 characters, not a uniform 31. The
`32 + 27×31 = 869` sentence I repeated in Checkpoint K gives the right total but is a false
description of the row structure, and is retracted going forward.

---

## REQUEST 4 — one straight-on photograph of the cipher side (NEW, and decisive)

**What is needed is very small: whether the right-hand edge of the engraved cipher text is
ragged or flush.**

| field | value |
|---|---|
| Source | any orthographic / straight-on high-resolution photograph of the Kryptos cipher-side copper screen; or a fabrication drawing, punch template, shop drawing, or measured survey |
| Candidate holders | CIA Fine Arts Commission / CIA Museum installation records; Jim Sanborn's own studio material; the sculpture fabricator's shop drawings; NSA DOCID 4145036's original photographic plates rather than its typeset transcription |
| Exactly what is needed | (a) is the right edge of rows 1–24 ragged or flush; (b) do the left edges of all rows start at a common x; (c) is the inter-character pitch constant within a row and across rows |

### Why it matters, precisely

Rows 1–24 hold 29–33 characters. With a monospaced punch and a common row width every row
would hold the same count. So either row width varies (ragged right edge → constant pitch,
in which case row-local index **is** a physical column) or the pitch varies by row (flush
right edge → no common lattice, and "the character physically above" is undefined by
index). A single straight-on photograph distinguishes these, and the two hypotheses differ
by 13.8% in pitch between the shortest and longest rows, which is visible rather than
metrological.

Until then the physical "characters above K4" architecture is **underdetermined, and
currently disfavoured** by `data/physical.json → engraving_line_lengths` ("Sanborn kerned
the lettering for aesthetics; fixed-width spacing was avoided", MEDIUM). It is parked, not
tested with a manufactured lattice.

**A typeset transcription cannot answer this.** It must be an image or a drawing that
preserves real indentation.

---

## REQUEST 5 — FULFILLED (2026-09-12). No discrepancy; the error was mine

Resolved by `docs/external/checkpoint-L-web-audit-requests-4-5.md` and verified here
against `data/cipher_side_rows.json`:

| span | physical characters | letters | `?` |
|---|---|---|---|
| K1 = rows 1–2 | 63 | 63 | 0 |
| K2 = rows 3–14 | 372 | 369 | 3 |
| rows 1–14 | **435** | **432** | 3 |

`63 + 372 = 435` counts **physical ciphertext characters**. Checkpoint L compared 432
**letters** against it as though the units matched. **There is no transcription
discrepancy on this basis**, and it is no longer carried as open.

Kept separate, and not mixed into the physical source: NSA DOCID 4050989's early working
convention (K2 as 373, three solved sections 773, total 870, 97 unresolved), and Sanborn's
report to WIRED (2006) that he deleted an `X` from the end of a K2 line for aesthetic
balance. Those bear on an **intended pre-aesthetic cryptographic source**, which is a
distinct thing from the **physical engraved source**. If the restored-`X` stream is ever
tested it must be a separately preregistered source variant; it will not be inserted
silently. EXP-035 tested the physical engraved 869-character source and keeps that
interpretation and its result unchanged.

### The original wording of this request, for the record

`data/cipher_side_rows.json` records an unresolved discrepancy: rows 1–14 supply **432
letters plus 3 question marks**, while the commonly cited section lengths K1 = 63 and
K2 = 372 sum to **435 letters**. Needed: a character-by-character count of the K1 and K2
*ciphertext* from the same CIA/NSA primary source, or NSA DOCID 4145036's cipher-side
slide at legible resolution. It does not affect any result that uses only rows 15–28 or K4
itself, but it bears on any model keyed to rows 1–14.

---

## REQUEST 4 — still OPEN; exact archival target now identified

The external audit found official CIA photographs, a Library of Congress Carol M.
Highsmith record (`LC-DIG-highsm-13337` / `LC-HS503-2081`, high-resolution derivatives up
to an 83 MB TIFF, no known publication restrictions), and the Smithsonian Jim Sanborn
papers — but **no public image proven orthographic enough** to establish a common
character-centre lattice. The CIA text rendering left-aligns variable-length rows, but it
is a presentation rendering and must not be promoted into surveyed geometry; the CIA
physical close-up is too oblique to show the cipher-side right edge.

**Highest-value exact target if this becomes important again:**

| field | value |
|---|---|
| Collection | Jim Sanborn papers, Archives of American Art, Smithsonian Institution |
| Series | Series 3 — Commission Files |
| Location | **Box 6, Folder 10 — `Pre-Production and Notes, 1990–1999`** |
| Also relevant | Box 6 Folder 8 (`"Kryptos" CIA Headquarters — Sculpture, 1993–2009`); Box 6 Folder 11 (`Codes Research, circa 1980s–circa 2002`) |
| Finding aid | `https://www.aaa.si.edu/collections/jim-sanborn-papers-22298/series-3` |
| Exactly what is needed | a punch layout, fabrication drawing, type-work template, or measured line-layout sheet showing row start positions and character pitch |
| Secondary | the LOC Highsmith TIFF at full resolution, inspected for whether the cipher-side right edge is ragged or flush |

A drawing or template would settle this far more cleanly than any angled photograph.

**Also new, and pointing the same way:** Sanborn told WIRED in 2006 that he removed an `X`
from the end of a K2 line *for aesthetic balance*. That is direct evidence the final
engraved line lengths were artistically adjusted rather than treated as inviolable
cryptographic blocks — which strengthens the Checkpoint-L decision to **park rather than
rescue** the fixed-lattice, same-column-above model.

**Do not block cryptanalysis on this.** The physical architecture stays PARKED, and work
continues on families that need no horizontal coordinate.

---

## REQUEST 6 — FULFILLED (2026-09-12): public crib positions verified

Checkpoint O's single highest-priority action was to pin the 24 crib constraints to a cited
public source rather than to inherited convention. **Done**, in
`docs/external/checkpoint-O-public-crib-primary-verification.md`, and audited against the
repository here: every cited span reproduces the committed ciphertext exactly, and no crib
text or index changed.

| clue | one-based span | repo zero-based | ciphertext | evidence grade |
|---|---|---|---|---|
| `BERLIN` | 64–69 | part of [63,74) | `NYPVTT` | **A/B** — contemporaneous NYT, position-specific |
| `CLOCK` | 70–74 | part of [63,74) | `MZFPK` | **A/B** — same NYT report, position-specific |
| `NORTHEAST` | 26–34 | part of [21,34) | `QQPRNGKSS` | **A/B** NYT positions + **A** Sanborn NPR authorship |
| `EAST` | 22–25 | part of [21,34) | `FLRV` | **B+** — reporter-confirmed private release; position inferred as "immediately before NORTHEAST" |

The four releases do **not** share identical provenance and the repository does not pretend
they do. The combined span is nonetheless sufficient for repository use, and the two
eliminations that were alignment-contingent were re-checked against the *directly numbered*
spans only (see `docs/evidence-grades.md`).

**Request 4 (fabrication geometry, AAA Series 3 Box 6 Folder 10) remains the only open
request that matters, and nothing is blocked on it.**

---

## REQUEST 7 — OPEN, HIGHEST PRIORITY (added Checkpoint T): additional verified K4 plaintext

**What is wanted:** any publicly attributable, position-specific statement fixing one or more
K4 plaintext letters **outside** the two known cribs — that is, in zero-based positions
`0–20`, `34–62` or `74–96`. Acceptable forms: a Sanborn public statement or interview, a
contemporaneous report quoting one, or a museum/press release with the same standing as the
`BERLIN`/`CLOCK`/`NORTHEAST`/`EAST` releases already admitted under Request 6.

**Explicitly excluded:** alleged full plaintexts, claimed solutions, solution dumps, leaked
material, private K5 material and the quarantined Folder 8 pages. A candidate letter is
admissible only with public, citable provenance, graded like every other source.

**Why this now outranks further cryptanalysis.** Checkpoint T established that the binding
resource is constraint density, not compute:

- The two cribs are contiguous runs of 13 and 11 characters. Within-crib position
  differences never exceed 12; cross-crib differences lie in `[30, 52]`.
- Consequently **periods 27, 28 and 29 receive exactly zero equality constraints**, and
  periods 24–26 receive only 5, 3 and 1. Any model in that window is unfalsifiable with
  current data, and any "fit" reported there is vacuous.
- Per-row independent keys, and long-period or reset-at-boundary recurrences, lose their
  power for the same reason.

A single additional verified letter placed in the gap `34–62` or the tail `74–96` would
create new position differences, several of which are divisible by 27, 28 or 29, and would
restore falsifiability to a family of models that is currently untestable rather than
untested.

See `docs/analysis/checkpoint-T-constraint-first-architecture-search.md` §7.2.
