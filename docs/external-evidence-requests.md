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
