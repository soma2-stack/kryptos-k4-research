# Checkpoint R external audit — Box 6 Folder 9 `Book, undated`

Date: 2026-09-12
Branch: `claude/k4-post-j`

## Scope and provenance

This note records a contamination-safe visual audit of the complete user-supplied ZIP for:

- Jim Sanborn papers
- Archives of American Art, Smithsonian Institution
- Series 3 — Commission Files
- "Kryptos" CIA Headquarters
- Box 6, Folder 9 — `Book, undated`

The ZIP contained **30 JPEG images**.

User-supplied ZIP SHA-256:

`34b82d101f80f9ca41794f0a6fcb721ce29ab57f2190d97f1c1818b81f5ab27c`

The images themselves are not committed here. This note records only research-safe findings and exact archive filenames for the most important pages.

## Bottom line

This is the most important documentary find in the archive work so far.

The folder is an unpublished / draft book proposal-manuscript headed **`KRYPTOS: From The Source`**. Page 2 explicitly says the text would be written by **Jim Sanborn**, and the surviving pages are written in the first person as Sanborn's account.

It still does **not** disclose:

- K4 plaintext;
- the exact K4 key;
- the exact K4 algorithm;
- a named K4 key source;
- a complete physical x-coordinate layout of the ciphertext panel.

But it supplies strong first-person evidence about:

1. how the copper letters were actually fabricated;
2. why Edward Scheidt was brought into the project;
3. Sanborn's intended relative difficulty of K1–K3 versus K4;
4. his deliberate effort to obscure encoded text in official photographs;
5. the custody of partial plaintext / key material after dedication.

The most important correction is fabrication: **Sanborn's own draft says the proposed robot / high-pressure-waterjet method was rejected as too expensive and the actual Kryptos lettering was cut by hand with jigsaws from individually traced metal stencils on scribed horizontal row lines.** This supersedes the weaker 1992 newspaper statement previously recorded as saying the final lettering was computer-guided water-jet cut.

## Contamination rule for this folder

Page 2 states that the proposed book would contain **significant clues to K4 embedded in its text**.

Therefore this audit deliberately does **not** mine suggestive wording, anecdotes, place names, numbers, chapter titles, or prose patterns for hidden K4 clues.

Admitted evidence is restricted to explicit factual statements about fabrication, collaboration, publication history, custody, and Sanborn's stated design intent.

No latent-clue search, acrostic search, numerical clue extraction, or speculative keyword harvesting was performed.

## High-value pages

### 1. Page 2 — authorship and explicit clue warning

Archive file:

`2-AAA-AAA_sanbojim_4129058.jpg`

SHA-256:

`31443e670ef9d43c025c1bc15eeb9f72764c154e3625989d0c24c4f0ef65b592`

The page is headed `KRYPTOS: From The Source` and describes the proposed book as a first-hand account. It explicitly says the text would be written by Jim Sanborn.

It also says the author intended to embed significant K4 clues in the book text.

Research treatment:

- first-person / authorial documentary material is high-value provenance;
- do **not** mine the draft for hidden clues under the current contamination protocol;
- use only explicit construction/history statements unless the protocol is intentionally changed later.

### 2. Pages 10–11 — direct fabrication account; waterjet story corrected

Archive files:

- `10-AAA-AAA_sanbojim_4129085.jpg`
- `11-AAA-AAA_sanbojim_4129088.jpg`

SHA-256:

- page 10: `81cd563251efc3d7b30a95f43464539292d02c36d71ced8cc425f7178f123eee`
- page 11: `4252b4fc4420243f6322c8d18d15d268ff52e6ae20e9717b095c6b950b0df270`

Sanborn's account says:

- Revere Copper Products supplied the copper plates;
- the copper was roughly 3/8 inch thick;
- a robot / high-pressure-waterjet process was considered;
- the estimated cost of the automated cutting route was prohibitive;
- the team therefore **began cutting the letters by hand**;
- the Vigenere-tableau plates were cut first;
- the copper sheets were painted black;
- **horizontal straight lines were scribed for the rows of letters**;
- each character was placed by checking its proper location, placing a **metal stencil** on the long row line, and tracing it with a scribe;
- each character was then drilled, cut with jigsaw blades and hand-filed to the scribed outline;
- when work reached encoded plates K1–K4, staffing had fallen sharply;
- one assistant ultimately cut K3 and K4 by himself over about two months, according to Sanborn, with virtually no errors.

### Geometry consequence

This is the strongest fabrication evidence currently available.

It establishes:

- straight horizontal row guides / baselines;
- individual stencil placement;
- hand tracing and hand cutting;
- no demonstrated computer-generated final x-coordinate layout.

It does **not** establish:

- fixed character pitch;
- a common vertical x-grid across rows;
- 31 physical columns;
- identical row starts;
- uniform character spacing.

The previous idea that a computer-guided waterjet implies a digital fixed-layout source is therefore **superseded / weakened** by this direct first-person account. A common lattice remains unproved and should stay parked.

### 3. Page 12 — why Edward Scheidt was recruited

Archive file:

`12-AAA-AAA_sanbojim_4129091.jpg`

SHA-256:

`efbf431d0f6e9e56c76f8f288a4237d63792071798e8df6d7d4e2f8688e4a26e`

Sanborn says he knew historical systems such as the Vigenere tableau but wanted contemporary expertise capable of challenging contemporary and future code-breakers. He then introduces Edward Scheidt, who had retired from the Agency and started a cryptographic-security company.

Research consequence:

- strong first-person support that Scheidt's role was specifically sought to provide a **modern / stronger** cryptographic dimension beyond Sanborn's historical-cipher knowledge;
- consistent with the contemporaneous press material already collected;
- still not a specification of K4's mechanism.

Do not infer a named modern cipher from this statement.

### 4. Page 23 — direct statement of intended K4 difficulty

Archive file:

`23-AAA-AAA_sanbojim_4129133.jpg`

SHA-256:

`edbb1d4cf8707a357bb7dc6fd5a9b6fb6d13b686808baef57ccff77f9e48e02c`

Sanborn states that when he designed the code he expected the first three sections to be solved in weeks or months, while **K4 was intended to take much longer**.

This is strong first-person confirmation that K4 was deliberately differentiated in difficulty from K1–K3.

It does not say what transformation makes K4 harder.

### 5. Pages 20–21 — partial plaintext / partial key custody

Archive files:

- `20-AAA-AAA_sanbojim_4129122.jpg`
- `21-AAA-AAA_sanbojim_4129125.jpg`

SHA-256:

- page 20: `a0b50d6278188366f4529541311547430f5968a1160d98550658125c7bab5a5d`
- page 21: `c98f0adb603f9f86e94057daf131fbb841f39acc3c65b01982a25cb73e8c0c2`

Sanborn says that at the private dedication in November 1990 he passed **some plaintext and a partial code key** to Director of Central Intelligence William Webster for personal custody.

Research treatment:

- metadata about custody only;
- no plaintext or key content appears on these pages;
- do not infer which Kryptos section(s) the partial key covered without separate evidence.

### 6. Page 27 — deliberate photographic obscuration

Archive file:

`27-AAA-AAA_sanbojim_4129149.jpg`

SHA-256:

`e19b934e3b88880c6f6d2d87a1533bc98b6d20f87d802445a4dc34c12a98e389`

Sanborn says that when photographing the installed work he wanted some encoded text obscured in order to delay decryption, while CIA photography restrictions also controlled angles / exposure for security reasons.

Research consequence:

- archival/publicity photographs were not necessarily intended as neutral documentation of the ciphertext surface;
- this further weakens attempts to infer precise panel geometry solely from oblique publicity photographs;
- a true shop drawing / measured survey would still be needed for an exact physical-coordinate model.

## Other pages

The remainder of the 30-image folder consists of draft chapters / proposal material about:

- the CIA site and sculpture elements;
- quarrying / petrified wood / landscaping;
- Sanborn's background and artistic themes;
- later CIA / historical-intelligence anecdotes;
- K1–K3 solver history;
- later Sanborn projects and multilingual / secrecy themes.

Some of these anecdotes may have been intended to carry embedded K4 clues, per page 2. They were **not** used as cryptanalytic evidence in this audit.

## Correction to earlier scrapbook evidence

The Series 9 Box 16 Folder 2 audit recorded a 1992 Washington Post statement that Kryptos lettering was cut by a computer-guided high-pressure water jet.

The new Box 6 Folder 9 first-person Sanborn account is more specific and directly addresses the fabrication decision. It says waterjet automation was considered but rejected because of cost, after which the team hand-cut the letters with jigsaws from traced metal stencils.

Current hierarchy:

1. **Sanborn first-person draft account:** actual lettering hand-cut after waterjet was rejected — preferred evidence.
2. **1992 newspaper description:** waterjet-guided cutting — retained historically as conflicting secondary reporting, but no longer used as the current fabrication model.

Do not silently delete the earlier report; treat this note as its documentary supersession.

## Cryptanalytic consequence

No new K4 cipher family is justified by Folder 9.

The folder strengthens three higher-level conclusions:

1. K4 was deliberately intended to be substantially harder than K1–K3.
2. Scheidt was recruited specifically because Sanborn wanted contemporary cryptographic expertise beyond historical Vigenere-type systems.
3. The physical ciphertext rows were laid out manually along scribed horizontal row guides using metal stencils; exact vertical / fixed-column alignment remains unproved and is now **less** supported than under the earlier waterjet interpretation.

Because the manuscript explicitly announces embedded K4 clues, using its prose as a source of secret keywords / numbers would require a deliberate change to the contamination protocol. Under the current programme, do not do that.

K4 remains unsolved.
