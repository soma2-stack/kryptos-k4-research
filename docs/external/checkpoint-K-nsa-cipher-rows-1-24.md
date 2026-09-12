# External evidence handoff: NSA/CIA cipher-side rows 1–24

Purpose: fulfill Checkpoint K's evidence request for the authoritative cipher-side transcription above K4, while preserving a critical geometry caveat discovered during acquisition.

No alleged K4 plaintext, purported solution, or private K5 material is included.

## Sources

Primary text transcription: CIA legacy page, **"Kryptos" Sculpture**, Panel 1 — Encoded Text (Text Version):
https://www.cia.gov/legacy/headquarters/kryptos-sculpture

NSA corroborating visual/transcription source: **DOCID 4145036, The CIA KRYPTOS Sculpture**, cipher-side slide/page showing the 28 engraved rows. A public mirror of the released NSA packet is available at:
https://documents.theblackvault.com/documents/controversies/CIAKryptosSculpturePresentation.pdf

Related NSA summary: **DOCID 4145037, The CIA Kryptos Sculpture: A Summary of Previous Work and New Revelations in Working Toward Its Complete Solution**:
https://www.nsa.gov/portals/75/documents/news-features/declassified-documents/cia-kryptos-sculpture/KRYPTOS_Summary.pdf

Source grade: A for the CIA text transcription and NSA institutional row transcription. The documents are not a measured fabrication survey.

## Exact rows 1–24

The following strings are transcribed exactly from the CIA Panel 1 text version and visually cross-checked against the NSA cipher-side slide where useful:

```text
01  EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJ
02  YQTQUXQBQVYUVLLTREVJYQTMKYRDMFD
03  VFPJUDEEHZWETZYVGWHKKQETGFQJNCE
04  GGWHKK?DQMCPFQZDQMMIAGPFXHQRLG
05  TIMVMZJANQLVKQEDAGDVFRPJUNGEUNA
06  QZGZLECGYUXUEENJTBJLBQCRTBJDFHRR
07  YIZETKZEMVDUFKSJHKFWHKUWQLSZFTI
08  HHDDDUVH?DWKBFUFPWNTDFIYCUQZERE
09  EVLDKFEZMOQQJLTTUGSYQPFEUNLAVIDX
10  FLGGTEZ?FKZBSFDQVGOGIPUFXHHDRKF
11  FHQNTGPUAECNUVPDJMQCLQUMUNEDFQ
12  ELZZVRRGKFFVOEEXBDMVPNFQXEZLGRE
13  DNQFMPNZGLFLPMRJQYALMGNUVPDXVKP
14  DQUMEBEDMHDAFMJGZNUPLGEWJLLAETG
15  ENDYAHROHNLSRHEOCPTEOIBIDYSHNAIA
16  CHTNREYULDSLLSLLNOHSNOSMRWXMNE
17  TPRNGATIHNRARPESLNNELEBLPIIACAE
18  WMTWNDITEENRAHCTENEUDRETNHAEOE
19  TFOLSEDTIWENHAEIOYTEYQHEENCTAYCR
20  EIFTBRSPAMHHEWENATAMATEGYEERLB
21  TEEFOASFIOTUETUAEOTOARMAEERTNRTI
22  BSEDDNIAAHTTMSTEWPIEROAGRIEWFEB
23  AECTDDHILCEIHSITEGOEAOSDDRYDLORIT
24  RKLMLEHAGTDHARDPNEOHMGFMFEUHE
```

For context, row 25 is:

```text
25  ECDMRIPFEIMEHNLSSTTRTVDOHW?OBKR
```

Rows 26–28 are the three 31-character K4 rows already present in the repository.

## Critical correction: rows 1–24 are not uniformly 31 characters wide

Counting the authoritative CIA strings gives these row lengths:

```text
01 32
02 31
03 31
04 30
05 31
06 32
07 31
08 31
09 32
10 31
11 30
12 31
13 31
14 31
15 32
16 30
17 31
18 30
19 32
20 30
21 32
22 31
23 33
24 29
25 31
26 31
27 31
28 31
```

Rows 1–24 therefore range from **29 to 33 characters**, not a uniform 31. Rows 1–24 contain 745 characters; rows 25–28 contain 124; total = **869**.

Therefore the inherited external claim:

> first physical row has 32 characters and the remaining 27 rows have 31, so 32 + 27×31 = 869

is false as a description of the actual row lengths. The total 869 happens to be correct, but it is obtained from the varying row lengths above, not from `32 + 27×31`.

This supersedes that row-width statement in `docs/external/perplexity-k4-geometry-correction-2026-09-12.md` and the same arithmetic repeated in Checkpoint K's commit message. Do not rewrite historical commits; cite this correction going forward.

## Consequence for the proposed "physically above" experiment

The requested rows are now available, but the evidence does **not** yet make a `row-k, same column` key source parameter-free.

Why:

1. Rows above K4 have unequal character counts.
2. CIA's text version supplies row strings, not surveyed horizontal coordinates.
3. NSA's typeset transcription is strong evidence for row membership and order, but prior audit already correctly noted that it does not establish millimetre-level x/y coordinates, exact inter-character spacing, or vertical character-centre alignment.
4. A rule such as "same column" therefore requires an independently justified alignment convention (for example, a documented fabrication grid, exact indentation offsets, orthographic measurement, or a preregistered finite set of alignment conventions). It must not silently assume all upper rows occupy the same 31 columns.

The official CIA rendered encoded-text image also displays the variable-length lines, but it is a presentation rendering rather than a fabrication drawing; it should not be promoted into surveyed geometry without evidence.

## Safe next use

The 24 row strings can now be treated as authoritative textual evidence for any model that depends only on row content/order.

Before testing a physical `same-column-above` architecture, obtain or define evidence for horizontal alignment/offsets. If a small finite family of alignment conventions is justified independently, preregister all of them before scoring and preserve each as a separate physical assumption.

K4 remains unsolved.