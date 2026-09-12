# External web audit after Checkpoint L: Requests 4/5 and alphabet-frontier correction

External supervisory research handoff. This is documentary evidence and model-selection guidance, not a Claude experiment. No alleged K4 plaintext, purported solution, or private K5 material is included.

## 1. Request 5 is resolved: the 432-vs-435 issue is a counting-category mismatch, not evidence corruption

Primary CIA transcription:

- CIA, `"Kryptos" Sculpture`, Panel 1 Encoded Text (text version):
  https://www.cia.gov/legacy/headquarters/kryptos-sculpture

Primary NSA corroboration:

- NSA DOCID 4145037, *The CIA Kryptos Sculpture: A Summary of Previous Work and New Revelations in Working Toward Its Complete Solution*:
  https://www.nsa.gov/portals/75/documents/news-features/declassified-documents/cia-kryptos-sculpture/KRYPTOS_Summary.pdf
- NSA DOCID 4050989, chronological history of NSA Kryptos work:
  https://www.nsa.gov/portals/75/documents/news-features/declassified-documents/cia-kryptos-sculpture/doc_2.pdf
- NSA DOCID 4050988, K1/K2 solution details:
  https://www.nsa.gov/portals/75/documents/news-features/declassified-documents/cia-kryptos-sculpture/doc_1.pdf

The section boundary is explicit in NSA 4145037: the first two sculpture lines consist of **63 characters** and are K1.

Using the authoritative CIA row strings already preserved in `data/cipher_side_rows.json`:

- K1 = rows 1-2 = **63 alphabetic characters**.
- K2 = rows 3-14 = **372 physical ciphertext characters total**.
- Those 372 K2 characters consist of **369 alphabetic letters + 3 question marks**.
- Therefore rows 1-14 contain **435 physical characters = 432 alphabetic letters + 3 question marks**.

So the Checkpoint-L statement that `432 letters + 3 ?` conflicts with `K1 63 + K2 372 = 435 letters` compares different units. `63 + 372 = 435` is a count of physical ciphertext characters, while `432` is alphabetic letters only. There is no discrepancy in the current CIA transcription on that basis.

### Historical 870-vs-869 wrinkle

NSA DOCID 4050989 records an early working convention in which the second section is described as 373 characters, the first three solved sections total 773, and the complete cipher totals 870 with 97 unresolved. That is a separate historical counting issue and should not be conflated with the physical current transcription of 869 characters.

WIRED's 2006 direct report from Sanborn explains a relevant one-character anomaly: Sanborn said he intentionally deleted an `X` from the end of a K2 line for aesthetic balance, later realizing it changed the decryption. Source:

https://www.wired.com/2006/04/typo-confounds-kryptos-sleuths/

WIRED 2013 repeats the same account while discussing the NSA work:

https://www.wired.com/2013/07/nsa-cracked-kryptos-before-cia/

Safe interpretation:

- **Physical/current K2 source:** 372 characters = 369 letters + 3 `?`.
- **Intended/corrected cryptographic text may involve the omitted X**; if a future experiment needs the intended pre-aesthetic K2 stream rather than the engraved physical stream, that must be a separately preregistered source variant, not silently inserted.
- EXP-035, which explicitly tests the engraved panel as source text, should remain grounded in the physical 869-character transcription unless its model is deliberately changed.

Request 5 can therefore be marked **FULFILLED / NO CURRENT TRANSCRIPTION DISCREPANCY**.

## 2. Request 4 remains unresolved, but the web evidence reinforces parking the physical-lattice model

Useful primary/near-primary image sources found:

### CIA official Kryptos page

https://www.cia.gov/legacy/headquarters/kryptos-sculpture

CIA provides:

- an official text rendering of Panel 1,
- an official physical close-up/upward photograph of the copper screen,
- a full-view sculpture photograph.

The text rendering visibly left-aligns variable-length rows, but it is a presentation rendering, not a fabrication survey, so it must **not** be used as proof of actual horizontal punch coordinates.

The physical close-up is strongly oblique and does not expose the complete cipher-side right edge well enough to determine flush-vs-ragged row endings.

### Library of Congress, Carol M. Highsmith Archive

Record:

https://www.loc.gov/pictures/item/2011631531/

Title: *Art made of "code" named Kryptos sits on the grounds of the C.I.A. Headquarters in Virginia*

Creator: Carol M. Highsmith

Reproduction numbers:

- `LC-DIG-highsm-13337`
- `LC-HS503-2081`

The LOC record exposes high-resolution public derivatives up to an 83 MB TIFF and has no known restrictions on publication. This is a strong image-acquisition target, but the cataloged view is not established here as sufficiently orthographic to settle row-edge geometry without inspecting the full-resolution image.

### Smithsonian Archives of American Art -- Jim Sanborn papers

Series 3, Commission Files:

https://www.aaa.si.edu/collections/jim-sanborn-papers-22298/series-3

The finding aid explicitly says the commission files include **designs and sketches, some photographs, correspondence, notes, type-work quotes, and project concepts**. The Kryptos material is in Box 6, including:

- Box 6 Folder 8: `"Kryptos" CIA Headquarters -- Sculpture, 1993-2009`
- Box 6 Folder 10: `Pre-Production and Notes, 1990-1999`
- Box 6 Folder 11: `Codes Research, circa 1980s-circa 2002`

The archive allows reproduction requests, but these folders have no public downloads at present. If physical row offsets become important again, **Box 6 Folder 10 (Pre-Production and Notes)** is currently the highest-value exact archival target because a punch layout/template or fabrication drawing would settle the issue much more cleanly than angled photographs.

### Documentary clue against a rigid lattice

Sanborn told WIRED in 2006 that he removed an `X` from the end of a K2 line **for aesthetic reasons, to keep the sculpture visually balanced**. That is direct evidence that the final engraved line lengths were artistically adjusted rather than being treated as inviolable cryptographic blocks.

This does not prove variable pitch or prove there is no common x-grid, but it strengthens Checkpoint L's decision to **park rather than rescue** the fixed-lattice / same-column-above model until physical construction evidence exists.

Request 4 remains **OPEN**.

## 3. Important model-selection correction: the historically demonstrated KRYPTOS mixed alphabet is already in the repo's 12 conventions

Checkpoint L proposes promoting a robustness test under a precommitted set of keyword-derived mixed alphabets because the negative corpus is conditional on alphabet indexing.

Before doing that, note what the current code already tests.

`k4lib/alphabets.py` defines:

- `STD = ABCDEFGHIJKLMNOPQRSTUVWXYZ`
- `KRY = KRYPTOSABCDEFGHIJLMNQUVWXZ`

`k4lib/conventions.py::all_conventions()` already enumerates all 12 combinations:

- 3 combiners: Vigenere, Beaufort, Variant Beaufort
- plaintext indexing alphabet in `{STD, KRY}`
- ciphertext indexing alphabet in `{STD, KRY}`

So all four P/C indexing combinations involving the **KRYPTOS keyword-mixed alphabet** are already part of every experiment using `all_conventions()`.

That matters because NSA DOCID 4050988 states for both K1 and K2:

- **Plain component: Keyword mixed sequence based on KRYPTOS**
- **Cipher component: Keyword mixed sequence based on KRYPTOS**

For K1 the repeating key is `PALIMPSEST`; for K2 it is `ABSCISSA`.

Therefore the historically demonstrated K1/K2 mixed component alphabet is **already covered** by the current convention set.

### Do not misclassify PALIMPSEST and ABSCISSA

In the NSA K1/K2 descriptions, `PALIMPSEST` and `ABSCISSA` are repeating keys, not the keyword used to construct the plain/cipher component alphabets.

Constructing new mixed indexing alphabets from `PALIMPSEST` or `ABSCISSA` would be a new speculative architecture. It may be testable, but it is **not** a robustness check of a known omitted K1/K2 alphabet convention and should not be promoted as such.

Before EXP-036, explicitly audit whether the proposed additional alphabets have documentary support as component alphabets rather than merely being known words/keys.

## 4. Better next question than automatically expanding mixed alphabets

The real uncovered structural gap now appears narrower:

1. Current one-symbol exact-consistency negatives already include the historically evidenced `KRY` mixed alphabet on the plaintext and ciphertext sides.
2. EXP-003 tested **transposition + short periodic key**, a highly motivated K1/K2-plus-K3 hybrid, but only over the old small affine/route permutation families.
3. EXP-033 enormously expanded the transposition family (including all keyed columnar widths 2-11) but only for one fixed monoalphabetic substitution, not a short periodic polyalphabetic layer.

That leaves a genuine intersection gap:

> **the much larger EXP-033 transposition family composed with a tightly constrained short-period polyalphabetic process.**

This is not a recommendation to brute-force `175M × every key` naively. Before execution, determine whether crib consistency can symbolically prune or decide the family without enumerating all key values, and compute expected constraint density by period.

Historically motivated small variants include:

- an unknown short periodic key of declared period range, decided by equality constraints rather than enumerated key letters;
- or, more narrowly, the exact known repeating-key structures `PALIMPSEST` / `ABSCISSA` only if the experiment is explicitly framed as testing reuse of known prior-section keying patterns.

This direction is materially different from EXP-033 and extends the original motivation of EXP-003 rather than adding unsupported alphabet permutations.

## 5. Recommended gate before the next run

Before naming EXP-036, compare these two candidate directions:

A. **Additional keyword-derived component alphabets**
- Only proceed for alphabets with documentary evidence or a clearly labelled finite speculative set.
- Do not claim K1/K2 precedent for PALIMPSEST-/ABSCISSA-mixed component alphabets; the NSA record says their component alphabet is KRYPTOS-mixed.

B. **Expanded transposition + short-period polyalphabetic family**
- Directly motivated by K1/K2 substitution plus K3 transposition.
- EXP-003 tested the concept but over a much smaller permutation family.
- EXP-033 supplies a much stronger transposition frontier.
- First derive a symbolic/constraint-based solver and a decidability table by period; do not blindly multiply 175,820,784 cases by a large key space.

Select the one with greater falsifiability and information gain after that audit.

K4 remains unsolved.
