# Checkpoint U — 2025 Sanborn public-clue audit

**Starting HEAD:** `a5cb0deb1014a86bcbde1e4dae710a87909aa50c` (branch `claude/k4-post-j`, clean tree).

**Verdict: `NO EXP-040 JUSTIFIED`.**

Full audit: `docs/external/checkpoint-U-2025-sanborn-public-clues.md`.

## Provenance ceiling — binding on everything below

**No primary source could be fetched.** Every relevant domain — `elonka.com`,
`scientificamerican.com`, `washingtonpost.com`, `wired.com`, `npr.org`, `smithsonianmag.com`,
`apnews.com`, Wikipedia, ACM — is blocked by this environment's egress policy; direct `curl`
returns `403` at the proxy. The audit rests on **search-result summaries** of reputable
reporting, cross-checked by independent queries.

Maximum grade awarded is **C+/B−**, below the 1991 ABC transcript and the 1999 *Washington
Post* article. One outlet described K4 as "79 encrypted letters" — it is 97 — so numeric
detail in this reporting is not trustworthy. **Re-run with primary access before any of this
becomes load-bearing.**

Contamination held: searches repeatedly surfaced 2025 plaintext, reconstruction and solution
pages. **None was opened**, and later searches blocked those domains explicitly.

## Main finding: yes, we have been conflating the two layers

**Layer A** is the map from 97 plaintext letters to the 97 K4 ciphertext letters.
**Layer B** is whatever the recovered plaintext then instructs the solver to do.

Sanborn documents the split himself. The 2005 Zetter interview is explicitly sequential —
"you have to **decipher the piece** *and then* **go to the agency and find that place**" —
and the 2025 quotation "K4 has not been solved. K4 has been **discovered** and it **points
in the direction of K5**" makes the same division from the other side. A text can only
*point* if pointing is a property of its content. **Layer A is unsolved while Layer B is
already in three people's hands**, which is the sharpest possible proof the layers separate.

Sorting the ten audited items: **eight are Layer B or neither. Exactly two touch Layer A,
and both concern K5, which is not published.**

Decisively, `BERLINCLOCK` is a **plaintext word**. The November 2025 clarification that it
means the Weltzeituhr rather than the Mengenlehreuhr says what a decrypted word *denotes*.
It is not, and never was, a statement that clock geometry is a keystream source.

## Consequence for prior experiments

EXP-002 (Mengenlehreuhr keystream), EXP-018 (compass-bearing routes), EXP-023 (Morse
keystream), EXP-024 / EXP-029 / EXP-031 (Weltzeituhr tape and running key) and EXP-035
(panel running key) all converted an artistic referent into a Layer A key source.

- **Their negative results stand unchanged.** They were correct.
- **Their motivation is demoted** from DOCUMENTARY-MOTIVATED to **SPECULATIVE**. The record
  was never saying "use the clock as a key"; it was saying "the plaintext mentions a clock."
- **Do not revive this class.** Converting Weltzeituhr, Mengenlehreuhr, Morse, compass
  bearings, Egypt or the Wall into a keystream now fails gate condition 1 outright.

It also deflates "riddle within a riddle": under the two-layer model the nesting is most
naturally **Layer B nesting** (plaintext → riddle → K5), not nested cipher stages. That
removes it from the evidence base for multi-stage composition. Scheidt's 1991/1999 Layer A
statements are untouched, as is Checkpoint S's four-process reading of K1→K4.

## The one unverifiable item in the brief

The brief attributes to WIRED, August 2025, that K4's plaintext does **not** require
physical access to CIA grounds. **I could not source this, and the best-attested WIRED
statement — the 2005 Zetter interview — says the reverse.** Three readings survive, none
established: the brief conflates 2005 with 2025; a genuine 2025 reversal (plausible, since
K5 is to stand in a *public space*); or a 2025 piece this environment's search missed.
**Recorded UNVERIFIED and used nowhere.** The §4 conclusion does not depend on it.

## Chronology problem — preserved, not resolved

Sanborn is reported to say both events shaped the plaintext he was "writing in **1988**";
Egypt was late 1986 (consistent) but the Wall fell **9 November 1989** (after). He is
separately quoted saying he was "designing the project when the Berlin Wall fell." The
sculpture is dated 1988 by cost and commission and was dedicated 3 November 1990, so writing
plainly spanned 1988–1990.

**Most probable: loose dating.** Not established; reporting error and unresolved
misrecollection both survive. **Prohibited:** treating 1986, 1988 or 1989, or any arithmetic
on them, as a key length, offset, period, seed or index.

## The five questions

1. **New position-specific plaintext constraint satisfying Request 7?** **No.** The
   Weltzeituhr clarification changes a meaning, not a position; `[63,74)` is unmoved. The
   thematic clues yield no letter anywhere, and inferring plaintext from them is prohibited.
2. **Any clue identifying or bounding the encryption method?** **No, not usably.** Only
   K5's "similar but not identical" is method-adjacent, and it is self-referential to an
   unknown system.
3. **Does "the plaintext is an instruction" change the masking / riddle readings?** **Yes** —
   it relocates the nesting from cipher stages to riddle stages.
4. **Does it demote experiments using artistic referents as keystreams?** **Yes — their
   motivation, not their results.**
5. **Is a new bounded experiment justified?** **No.**

## K5: the only Layer A content, and it is a closed loop

Reported: K5 is **97 characters**, uses a system **"similar but not identical"** to K4, and
**shares coded words at shared positions**, reportedly including `BERLINCLOCK`. If verified
that would be exactly the cross-text constraint Checkpoint T identified as the binding
shortage — but K5's release is conditioned on K4 being cryptographically solved, so it is a
**closed loop, not a lead**. It is also the weakest-sourced item in the audit.

## ONE next action

**Obtain primary-source access to the 2025 open letters** (August and November, via Elonka
Dunin's Kryptos page and the 1 Nov 2025 *Washington Post*), and settle the claimed WIRED
August 2025 piece. Until then no 2025 clue may be load-bearing.

Priority order is otherwise unchanged, with one promotion: **Request 7** (additional
verified K4 plaintext) remains highest-value; **Request 2** (unedited 2005 Zetter/Scheidt
material) **rises**, because this audit shows the 2005 interview is the clearest articulation
of the Layer A / Layer B split on record and the repository holds only the edited version.

Do not start another speculative cryptanalytic family.

K4 remains unsolved.
