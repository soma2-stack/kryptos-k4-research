# Canonical current status — read this first

This is the compact handoff for future sessions. It does **not** replace historical checkpoints.

**Current cryptanalytic checkpoint:** Checkpoint R (`results/2026-09-12-claude-checkpoint-R.md`).

**Documentary work completed after R:** Box 6 Folders 8, 9, 10 and 11, plus Series 9 Box 16 Folder 2, have all been inspected.

**K4 remains unsolved.**

## Verified K4 anchors

Use the published positional cribs exactly as:

- zero-based `[21,34)` = `EASTNORTHEAST`, ciphertext `FLRVQQPRNGKSS`
- zero-based `[63,74)` = `BERLINCLOCK`, ciphertext `NYPVTTMZFPK`

See `docs/external/checkpoint-O-public-crib-primary-verification.md`.

## Cryptanalytic state

Do **not** rerun EXP-029 through EXP-039 merely for reassurance.

Important current scoped negatives include:

- EXP-033: declared single-transposition families composed with **any fixed A-Z→A-Z function** — zero feasible at its exact scope.
- EXP-036: declared periodic shift-family, periods 2–23, composed with the declared transposition families — zero feasible at its exact scope.
- EXP-037: preregistered standard Porta family — zero feasible.
- EXP-038 / Checkpoint Q: full-Z26 second-order affine self-evolving keystreams, message-aligned, 12 committed shift conventions — zero feasible; independently exhaustive. This does **not** eliminate recursive/stateful systems generally.
- EXP-039 / Checkpoint R: standard no-padding double columnar transposition using ordered pairs from `{KRYPTOS, PALIMPSEST, ABSCISSA}`, followed by any fixed monoalphabetic map — `0 FEASIBLE-FUNCTION`, `0 FEASIBLE-BIJECTION`. This does **not** eliminate double transposition generally.
- Standard Fractionated Morse is structurally incompatible with the published positional crib semantics.
- Direct Gromark was rejected structurally before primer search because legal digits 0–9 cannot realise enough crib pairs under evidenced alphabet treatments.
- Quagmire I–III and Gronsfeld reduce to already-covered families; Quagmire IV needs an unsupported second alphabet.
- Direct World Clock letter-source models have multiple bounded negatives. Do not rescue them post hoc.

Retracted claims that must **not** be revived:

- CET = 97 letters
- ATHEN absent from UTC+2
- upper band = north / lower band = south
- membership implies physical order
- EXP-029 significance from the wrapped/duplicate implementation
- isolated physical `OBKR` row
- uniform 31-character cipher-panel rows
- Checkpoint-L mixed-alphabet frontier
- Checkpoint-M claim that all experiments share the same three shift combiners

## Documentary results after Checkpoint R

### Box 6 Folder 10 — `Pre-Production and Notes, 1990-1999`

Inspected completely from the user-supplied image batch.

**Negative** for cipher-panel x-coordinate / common-lattice evidence, punch/type layout, K4 key source, exact K4 algorithm, or a note naming the fourth process.

Do not re-audit it. See `docs/external/checkpoint-R-folder10-content-audit.md`.

### Series 9 Box 16 Folder 2 — `Kryptos Sculpture, circa 1975-1993`

Inspected completely from a 106-image user-supplied ZIP.

Useful findings:

- 1990–1991 reporting repeatedly describes progression from Morse / Vigenere material to a harder **custom / modern process developed with a former or retired CIA cryptographer**;
- a March/April 1991 profile says Sanborn used “three or four” systems progressing in complexity;
- a 1992 Washington Post profile reports computer-guided high-pressure-waterjet letter cutting.

The waterjet fabrication claim is now **superseded as the current working account** by the stronger first-person Sanborn manuscript in Box 6 Folder 9: Sanborn says waterjet automation was considered but rejected on cost and the actual letters were hand-cut from traced metal stencils. Keep the 1992 statement only as conflicting secondary reporting.

A 1992 clipping calling the message a “complex anagram” is **low-confidence only** and is not experiment-grade evidence.

See `docs/external/checkpoint-R-box16-folder2-audit.md` and the Folder 9 supersession below.

### Box 6 Folder 11 — `Codes Research, circa 1980s-circa 2002`

Inspected completely from a 37-image user-supplied ZIP under staged contamination-safe triage.

**No complete alleged K4 plaintext or purported K4 solution was found in the supplied batch.**

The folder is broad and largely concerns Sanborn's wider code / intelligence / multilingual research rather than the original K4 construction. It includes a 1994 `FUMEE` layout, a Cyrillic tableau-style sheet, a later KRYPTOS-keyed alphabet proof, explicitly dated 2002 `Russian Decoding Chart` Morse/binary material, multilingual intelligence-text material, and Soviet/Russian archival documents.

These later practices are chronologically/evidentially insufficient to infer K4's 1989–1990 custom mechanism. Do **not** launch K4 experiments from them alone.

See `docs/external/checkpoint-R-folder11-codes-research-audit.md`.

### Box 6 Folder 8 — `Sculpture, 1993-2009`

Inspected from a 49-image user-supplied ZIP under contamination-safe triage.

The folder is dominated by later public Kryptos web printouts, 1999 newspaper coverage, public K1–K3 solver history, and solver correspondence / worksheets. It contains **no usable orthographic or restoration geometry** for the ciphertext face and no new K4 key source or exact mechanism.

Important contamination boundary:

- archive page `29-AAA-AAA_sanbojim_4128992.jpg` explicitly begins a proposed **message four / K4 solution** packet;
- pages 29–49 are therefore treated conservatively as **solution-adjacent / quarantined** for cryptanalytic use;
- no claimed K4 plaintext, key or method from that packet is admitted into this research programme.

See `docs/external/checkpoint-R-folder8-sculpture-audit.md`.

### Box 6 Folder 9 — `Book, undated`

Inspected completely from a 30-image user-supplied ZIP.

This is an unpublished / draft first-person manuscript / proposal headed **`KRYPTOS: From The Source`**. Page 2 says the text would be written by Jim Sanborn.

This is the strongest archive source so far for **fabrication and design-intent history**, while still not disclosing K4's exact algorithm or plaintext.

High-value explicit statements:

- Sanborn considered automated high-pressure-waterjet cutting but says the estimated cost was prohibitive;
- the actual letters were then **cut by hand with jigsaws**;
- copper sheets were painted black and **horizontal straight lines were scribed for rows of letters**;
- each character was individually located, a **metal stencil** was placed on the long row line, and the letter was traced, drilled, cut and hand-filed;
- K3 and K4 were ultimately cut by one remaining assistant over roughly two months, according to Sanborn, with virtually no errors;
- Sanborn says he recruited **Edward Scheidt** because historical systems such as Vigenere were not enough for his goal of challenging contemporary and future code-breakers;
- Sanborn says he expected the first three Kryptos sections to be solved in weeks or months while **K4 was intended to take much longer**;
- Sanborn says some plaintext and a partial code key were given to DCI William Webster for custody at the private dedication;
- Sanborn says official photography deliberately obscured some encoded text to delay decryption.

Important contamination boundary: page 2 says the proposed book would contain **significant K4 clues embedded in its text**. Under the current protocol, do **not** mine prose, anecdotes, numbers, place names, chapter titles or wording for hidden clues. Only explicit factual construction / history statements are admitted.

See `docs/external/checkpoint-R-folder9-book-audit.md`.

## Physical geometry status

The strongest current fabrication evidence is now Sanborn's first-person Folder 9 account:

- letters were manually laid out along scribed **horizontal row guides**;
- individual metal stencils were traced;
- letters were hand-cut / hand-filed;
- the contemplated automated waterjet route was rejected.

This establishes row baselines but still does **not** establish:

- exact cipher-panel character x-coordinates;
- fixed character pitch;
- a common horizontal x-lattice across rows;
- identical row starts;
- 31 physical columns.

The earlier computer-guided-waterjet inference should no longer be used to argue that a digital fixed-coordinate source layout probably existed. The common-column-above-K4 model remains parked and is now **less supported**, not more.

## One recommended next action

**Do not start another speculative cipher family and do not mine the Folder 9 manuscript for hidden clues under the current contamination rules.**

The strongest accessible archive lanes have now been inspected:

- Folder 10: negative for method / geometry;
- Box 16 Folder 2: useful contemporaneous context, no exact method;
- Folder 11: broad later code research, no K4 mechanism;
- Folder 8: no geometry and contains a quarantined proposed-K4-solution packet;
- Folder 9: strong first-person fabrication / design-intent evidence, but explicitly warns that the proposed manuscript would embed K4 clues.

At this point the accessible archive evidence base is **substantially exhausted for evidence-driven selection of a new cipher family**.

The next research session should first synthesize the new first-person Folder 9 evidence against the existing Scheidt documentary record and decide whether it changes the rank of any *already-defined, falsifiable* architecture. If it does not, record that no evidence-backed EXP-040 is currently justified rather than manufacturing one.

Do **not** use Box 6 Folders 13–19 (`Attempts at Deciphering Codes`, `Cracked Codes and Charts`) for cryptanalytic idea generation under the current protocol.

## Contamination protocol

Do not access or use alleged complete K4 plaintext, purported solution dumps, leaked solution material, private K5 plaintext, or private K5 ciphertext.

Public construction photographs, public documentary sources, production records, historical-cipher references and explicit process provenance are safe. Clearly solution-looking pages must be quarantined before they influence cryptanalysis.

For Folder 9 specifically, explicit first-person factual statements may be used, but the announced **embedded K4 clues** must not be mined unless the user intentionally changes the contamination protocol.

Do not claim K4 solved unless there is one fixed deterministic 97-character decryption procedure that reproduces independently and satisfies all published constraints.
