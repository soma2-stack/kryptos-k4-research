# Checkpoint AI source ledger — physical tableau / alphabet panel

Date: 2026-09-13
Scope: public artifact measurement only; no solution sites, alleged plaintext, private K5
material, auction-secret material, or cipher-family search.

## Evidence hierarchy used

1. **CIA institutional textual artifact transcription.** CIA, `"Kryptos" Sculpture`,
   `Panel 2 - Cipher ( Text Version )`:
   <https://www.cia.gov/legacy/headquarters/kryptos-sculpture>. Retrieved 2026-09-13.
   The 28 displayed row strings are preserved verbatim in
   `data/tableau_checkpoint_AI.json`. Grade: **A- for what the CIA web page prints**;
   it is not itself a measured survey of the copper.
2. **Library of Congress institutional photograph of the installed original.** Carol M.
   Highsmith Archive, `LC-DIG-highsm-13337` / `LC-HS503-2081`, *Art made of "code"
   named Kryptos sits on the grounds of the C.I.A. Headquarters in Virginia*:
   <https://www.loc.gov/pictures/item/2011631531/>. The LOC record dates the underlying
   transparency only to `[between 1980 and 2006]`, says the digital image represents the
   original film transparency, and reports no known publication restriction. The inspected
   3384×4283 master derivative was
   <https://cdn.loc.gov/master/pnp/highsm/13300/13337u.tif>, SHA-256
   `302fb88dee8db7f484a85d9d7f9bbd39f69de37cbf7bb25ae5a2e35bf8b8cf52`.
   Grade: **A- provenance / MEDIUM geometric utility**.
3. **CIA institutional close photograph.** The 980×1305 CIA image at
   <https://www.cia.gov/static/bc5188e5768e6c394ec8dff5f1083da0/1949f/kryptos_sculpture_lg.jpg>,
   SHA-256
   `31013cb7c25557174afb228879c654c81b192867661b7c0f477cb31d9c02420a`.
   Grade: **A- provenance / LOW tableau-cell utility**: it is a close, strongly oblique
   detail and does not expose the complete tableau terminal edge.
4. **Repository fabrication evidence.** `docs/external/checkpoint-R-folder9-book-audit.md`
   records Sanborn's first-person draft account: horizontal row guides were scribed, then
   metal stencils were individually positioned, traced, drilled, jigsaw-cut, and hand-filed.
   This establishes horizontal baselines but not equal pitch or a shared column lattice.
   The same source says publicity photography sometimes intentionally obscured encoded text.

## What the photographs can and cannot verify

The LOC master visibly establishes that this is a curved copper screen organized into
horizontal letter rows. The view is oblique, the panel curves away from the camera, the seam
occludes/foreshortens terminal areas, and no scale or orthographic control is present. The CIA
close view is even less suitable for cell addressing. Neither image supports a defensible
row-by-row, column-by-column transcription of the full tableau.

Accordingly, every `photograph_visible_symbol` in the machine-readable cell map is `null` and
every cell confidence is `UNKNOWN`. This does **not** say that no letters are visible. It says
that no visible glyph was promoted to a uniquely indexed tableau cell without a justified
rectification. In particular, the official text's extra terminal `L` is not copied into the
physical field.

## Models and maquettes

No admissible, cell-addressable model or maquette image was found in the repository or the
narrow institutional-source check. Folder 11's later KRYPTOS-keyed alphabet proof and Cyrillic
tableau-style sheet are separate later works; Checkpoint R already prohibits back-projecting
them into the 1989–1990 artifact. Model/maquette agreement on the extra `L`, margins, and row
length therefore remains **UNKNOWN**.

## Source cautions

- The CIA page also says the whole screen has exactly 1,735 alphabetic letters. That global
  statement is not used to back-solve the tableau count: counting categories elsewhere include
  question marks and known engraved/intended-text discrepancies.
- The same page's phrase `matrix coding systems` concerns its overview of K1–K3 and does not
  name Hill, specify a matrix, or state a K4 process.
- The CIA's PNG labelled `Kryptos Cypher` is a graphic rendering of the same text version, not
  an independent photograph of the installed copper.
