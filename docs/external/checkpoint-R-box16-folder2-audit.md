# Checkpoint R external audit — Series 9 Box 16 Folder 2

Date: 2026-09-12
Branch: `claude/k4-post-j`

## Scope and provenance

This note records a visual audit of the complete user-supplied ZIP for:

- Jim Sanborn papers
- Archives of American Art, Smithsonian Institution
- Series 9 — Scrapbooks
- Box 16, Folder 2 — `Kryptos Sculpture, circa 1975-1993`

The ZIP contained **106 JPEG images**.

User-supplied ZIP SHA-256:

`1e85b054128159a4003328f0f6664d4913ab36a7a44fb852e41b5ea43bd67026`

The image files themselves are not committed here. This note records research-safe findings and exact archive filenames for the most relevant pages.

## Bottom line

This scrapbook is **not a K4 solution source**, but it is materially more useful than Folder 10 for documentary history.

It contains:

1. contemporaneous 1990–1992 press descriptions of the Kryptos coding architecture;
2. workshop / fabrication photographs;
3. dedication-era photographs of the installed cipher panel;
4. one useful fabrication statement that the letter cutting was performed with a **computer-guided high-pressure water jet**.

It still does **not** provide:

- an orthographic cipher-panel survey;
- exact character x-coordinates;
- a proved common horizontal lattice across rows;
- a K4 key source;
- K4 plaintext;
- an exact K4 algorithm;
- a Sanborn/Scheidt note naming the fourth process.

Therefore the parked physical same-column model remains parked, and no new cryptanalytic experiment is justified solely from this folder.

## High-value documentary findings

### 1. Pre-installation reporting: Vigenere plus a custom modern system

Archive file:

`57-AAA-AAA_sanbojim_4129443.jpg`

SHA-256:

`1dcc81fce5f1d45f4b3ff6373335a3b3aef4118f52547b9ef8d08e3a7bec8253`

This scrapbook page preserves the January 1990 Washington Post reporting around the sculpture while it was still being fabricated.

The article says, in substance:

- someone knowing the Vigenere tableau could decipher roughly one half of the phrase;
- the other half would use a **modern system created for the project by an expert cryptographer** whose identity Sanborn would not disclose;
- the assistant physically cutting letters into the copper did not know what the phrase meant.

Research weight: **HIGH documentary value, but still newspaper reporting rather than a technical specification.**

This strongly supports treating the later / harder Kryptos process as custom or modified rather than assuming that it must carry the name of a standard classical cipher.

It does **not** establish the exact K4 mechanism.

### 2. 1991 profile: “three or four” systems progressing in complexity

Archive file:

`47-AAA-AAA_sanbojim_4129403.jpg`

SHA-256:

`5c68de68595da30397b5ed3e0699977638f3df49aa670300c4ff8928a2d66819`

`Museum & Arts Washington`, March/April 1991, Paul Clements, states that Sanborn's work uses **“three or four” systems of encoding**, progressing in complexity from International Morse at the building entrance to a substantially harder cipher **developed by and encoded for Sanborn by a former CIA employee**.

Research weight: **HIGH contemporaneous corroboration** of a progressive multi-process design and a custom final/harder process.

This is consistent with the later Scheidt documentary record that K1/K2 are similar and the remaining sections involve different high-level processes, but it does not by itself prove a one-to-one mapping of those early journalistic descriptions onto K1–K4.

### 3. Additional 1991 corroboration: Morse → Vigenere → secret modern code

Archive file:

`50-AAA-AAA_sanbojim_4129415.jpg`

SHA-256:

`4fe2041a32694a98e238d844433bfcc858a9d717bb742f172656b9cd26f89743`

A contemporaneous article headed `The CIA's Top-Secret Sculpture` describes:

- an opening Morse-code section;
- subsequent Vigenere-tableau material;
- a **secret modern code**;
- an anonymous retired CIA veteran as the person who devised the code, while not knowing the message itself.

This is corroborative rather than an independent technical definition.

### 4. AP / syndicated 1991 reporting: lower-right portion is a “whole different ball game”

Relevant archive files include:

- `41-AAA-AAA_sanbojim_4129379.jpg`
- `42-AAA-AAA_sanbojim_4129381.jpg`
- `44-AAA-AAA_sanbojim_4129389.jpg`
- `45-AAA-AAA_sanbojim_4129395.jpg`

These repeat a common AP account: Vigenere is described for part of the work, while material in the lower-right quadrant / remainder is described as a substantially different problem involving multiple codes and work by a retired CIA cryptographer.

Research weight: **CORROBORATIVE**, with caution because the syndicated wording simplifies the sculpture and varies across reprints.

Do not use the “half” / “quadrant” language as exact K1–K4 boundaries without independent evidence.

### 5. Low-confidence lead: “complex anagram” / second higher-level puzzle

Archive file:

`38-AAA-AAA_sanbojim_4129367.jpg`

SHA-256:

`5b4b9345b3883e124b4aaef85e40a3fa7f5c88492fbe54192a899d318f2a825b`

A 1992 `Midwest Engineer` item says that the coded message is a **complex anagram** presenting a second higher-level puzzle.

Research treatment:

- **LOW / C-GRADE lead only**;
- the claim is unattributed in the clipped item;
- it may be journalistic shorthand for transposition, the already-known K3 structure, or another misunderstanding;
- it is not sufficient motivation for an “anagram” experiment;
- corroborate from a stronger Sanborn/Scheidt source before assigning cryptanalytic weight.

No experiment should be started from this sentence alone.

## Fabrication evidence

### 6. Computer-guided high-pressure water-jet cutting

Archive file:

`63-AAA-AAA_sanbojim_4129471.jpg`

SHA-256:

`e9f4209479c19929e290646a291e9551092da5ab35173fde34ef94ed616dd4a7`

A 1992 Washington Post profile states that the letters in the bronze/copper plates were cut using a high-pressure **water jet guided by computer**.

This is the strongest fabrication-process evidence found in the scrapbook.

Consequence:

- the final letter-cutting process was at least reported as computer-guided rather than a simple hand-punched character process;
- this makes an underlying digital/layout file plausible;
- it does **not** prove fixed pitch, a common 31-column lattice, identical row starts, or any specific x-coordinate model.

Do not revive EXP-032-style physical-column assumptions from this alone.

### 7. Workshop photograph with person working on a copper plate

Archive file:

`38-AAA-AAA_sanbojim_4129367.jpg`

The lower-left photograph shows a person working directly over a copper plate in the studio, with paper / letter-layout material visible nearby.

The exact operation cannot be established from the photograph alone. It could involve preparation, tracing, finishing, cutting assistance, or another fabrication task.

Do **not** label this as proof of hand punching or manual letter placement.

### 8. Pre-installation alphabet/tableau plates

Archive file:

`55-AAA-AAA_sanbojim_4129435.jpg`

SHA-256:

`66c6976701effb3be3cadb6b123849b50082a3589faab4d0279b9e8e5fbc4f79`

The workshop photograph shows pre-installation Kryptos plate material bearing alphabet/tableau text beside sculptural components.

Useful for fabrication provenance; insufficient for K4 cipher-side row geometry.

### 9. Flat workbench plate photograph

Archive file:

`56-AAA-AAA_sanbojim_4129440.jpg`

SHA-256:

`19b3b9ad4ac38e80754d5e30b2c3b3a31d5fe0f453ec430fb721517db4f2cfaf`

The January 1990 Washington Post photograph shows a flat text-bearing plate on a workbench during fabrication.

The visible material appears to be alphabet/tableau-side text rather than a clean orthographic view of the final K4 ciphertext rows.

It therefore does not settle the parked common-lattice question.

### 10. Dedication-era installed ciphertext face

Archive file:

`54-AAA-AAA_sanbojim_4129431.jpg`

SHA-256:

`d8a66be57d0654ebbe1b0e775481d2f242e14241d01fe3d8b6655f48fe3c3494`

Several color photographs show the installed ciphertext face around the dedication period.

They are useful provenance and somewhat clearer than some public publicity photographs, but remain:

- oblique;
- curved;
- partly occluded in some frames;
- too low-resolution as scrapbook reproductions for a defensible x-coordinate survey.

Result: **still insufficient to establish or reject a common horizontal character lattice.**

## What this changes in the research interpretation

The scrapbook strengthens one documentary conclusion:

> **The hardest Kryptos process was contemporaneously described as a custom / modern cipher developed with a former or retired CIA cryptographer, within a progression of multiple coding systems.**

This supports the existing caution against endlessly testing standard named historical ciphers merely because they exist.

It does not supply the missing custom mechanism, key source, or deterministic K4 architecture.

The scrapbook also adds meaningful fabrication evidence:

> **The letter cutting was reported as computer-guided high-pressure water-jet work.**

That is useful, but still not enough to infer the digital layout coordinates.

## Contamination review

No page in this supplied Box 16 Folder 2 ZIP contained a complete K4 plaintext or a demonstrated K4 solution method.

The scrapbook contains ordinary public press references to sealed solutions / keywords and to the people entrusted with them. Those are historical metadata, not solution content.

No purported solution dump was used.

## Disposition

- Box 16 Folder 2: **INSPECTED**
- solution/plaintext discovered: **NO**
- exact K4 method discovered: **NO**
- named K4 key source discovered: **NO**
- useful contemporary architecture evidence: **YES**
- useful fabrication-process evidence: **YES**
- common physical lattice established: **NO**
- common physical lattice disproved: **NO**

## Recommended next documentary step

The public / low-contamination photographic lane has now been substantially exhausted without producing the missing layout or K4 mechanism.

The highest-information archival target is now:

**Series 3, Box 6, Folder 11 — `Codes Research, circa 1980s-circa 2002`.**

Because that folder is higher contamination risk, use staged triage:

1. inventory / thumbnails / page types first;
2. admit published historical cipher references, bibliographic notes, method-development notes, public key-source references, and non-plaintext process material;
3. quarantine pages that are clearly proposed solutions, solver correspondence, reconstructed plaintext, or complete answer material;
4. do not let a solution-looking page silently enter the experiment corpus.

If the objective remains only physical geometry rather than cryptographic architecture, the lower-risk alternate target is Box 6 Folder 8, `Sculpture, 1993-2009`, for later photographs / conservation / fabrication records.

K4 remains unsolved.
