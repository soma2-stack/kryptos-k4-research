> **Checkpoint I supersedes stale interpretations below.** Read
> [the audit](codex-audit.md) and [current result](../results/2026-09-12-codex-checkpoint-I.md)
> first. Preserve the frozen 120-letter tape. Do not rerun historical large searches.

# Next experiments

Rewritten 2026-09-12 after Checkpoint D. Read in this order:
`docs/contamination-log.md` → `docs/evidence-grades.md` → this file.

## The situation in one paragraph

Four sessions have eliminated short-key and structured-key models at scale. Three
independent lines now converge on a single architecture:

- **EXP-019 (unicity):** K4's 97 characters can determine a key of at most ~66–76
  letters. What matters is key *entropy*, not length. A long **random** key is
  information-theoretically unrecoverable; a long **structured** key — read off text,
  a chart, or an object — is recoverable *only once its source is known*.
- **EXP-021 (K5 architecture):** position-indexed, no net transposition, no unbounded
  feedback — placing K4 in the monographic, position-preserving class where this
  repository's structural results are proofs rather than heuristics.
- **EXP-006/008/015/016/018/020:** every short or structured position-indexed key,
  including the hand-executable line-by-line family, is eliminated.

What survives is a **keystream read off an external object, position by position**.
The `BERLINCLOCK` crib names such an object. The bottleneck is no longer ideas,
compute, or cipher families — it is one specific piece of missing public data.

---

## 0 — Status after Checkpoint H, Tier 1 met (session 12)

**Tier 1 is MET and the test has been run. It came back negative.**

A 4 Nov 1989 frame shows the complete CET/UTC+1 face — upper `AMSTERDAM BERLIN BRUSSEL
BUDAPEST MADRID PARIS PRAG STOCKHOLM WARSCHAU` (62), lower `KOPENHAGEN WIEN BERN BELGRAD ROM
TUNIS BRAZZAVILLE KINSHASA LUANDA` (58) = **120 letters**, target era, date corroborated by
the image's own `NEUES FORUM`/`SDP` banners. Frozen in
`data/weltzeituhr_photos.json → tier1_frozen_reconstruction` before testing; EXP-024 left
unmodified; restricted run executed as **EXP-029**.

**EXP-029: 11,520 alignments, 0 exact 24/24 matches, best 7/24, chance mean 0.92, positive
control passed on the real tape.** Eliminated exhaustively within the model: the single-face
running-key reading of the Berlin face. Not eliminated: multi-face readings (most of
EXP-024's space), non-running-key uses of the object, or the Weltzeituhr hypothesis itself.

**Three retractions of my own session-10 claims:**

1. **The 97 is withdrawn.** It was a transcription error — LONDON belongs to the neighbouring
   UTC+0 *upper* band, and BERN/BRAZZAVILLE/KINSHASA/LUANDA were missed. The face carries 120
   letters. It had been graded OBSERVATION, NOT EVIDENCE and refused as grounds to run the
   test, so nothing downstream was built on it.
2. **"Upper = northern, lower = southern" does not generalise** — KOPENHAGEN (55.7 °N) is
   lower while MADRID (40.4 °N) is upper. The 2^k layout-entropy reduction is withdrawn.
3. **Order does not follow from membership** — CET upper is alphabetical, UTC+0 upper is
   latitude-descending, UTC+0 lower is neither. Each face's order must be read off a photo.

Still standing: half-hour faces inscribed `+30`; membership non-monotonic (NOWOSIBIRSK moved
faces); LENINGRAD/MURMANSK/KIEW now attested in the target era itself.

**NEXT EVIDENCE — one target-era close frame from a different bearing** (≈45–90° around), so
UTC+0 and UTC+2 present frontally. Those two faces are what block the multi-face readings:
UTC+0's lower band ends are unseen, and UTC+2 has an UNKNOWN upper line between SOFIA and
NIKOSIA.

> Ask: **picture-alliance `16008401` / `16008415` (04.11.1989)** — whichever was *not* the
> frame uploaded — and **HanisauLand `153695.jpg` (04.11.1989)**, which may be a third
> distinct same-day frame. Success criterion: UTC+0 and/or UTC+2 frontal, both bands legible
> line by line, band ends visible.

## 0a — Earlier status after Checkpoint H, 1974 correction (session 11)

Metric: **15 of 24 sectors identified (62.5%)**, 20 face-era records, a **7-face contiguous
chain**, **14 observed adjacency edges**, **1 complete face** (CET @1970s, local visual,
97 letters — transcription unchanged).

**Tier 1 is NOT met, and moved further away.** Two retractions:

1. **The CET frame's date is no longer disputed — it reads mid-1970s.** A Straube frame
   explicitly dated **1974** already shows KOPENHAGEN and WIEN, so `nachgraviert 1985`
   cannot mean first addition and their presence never forced ≥ 1985. The reading that
   would have put my complete face in the target window is gone; the stability gap is
   **~14 years**, not ~4. ATHEN's absence flips sign — it now *supports* the Athens-only
   part of the 1985 account (Athens is UTC+2, not CET).
2. **The 46-name gap is NOT closed.** `146 − 80 − ~20 = ~46` is an unexplained remainder,
   not a dating. Attributing it all to 1985 was my inference. The growth curve is **open**,
   and a frame's date alone does not certify the target state.

Unchanged and still load-bearing: upper = northern / lower = southern (kills the 2^k layout
entropy); half-hour faces inscribed `+30`; upper bands alphabetical, lower bands not;
**membership is non-monotonic** (NOWOSIBIRSK moved faces), so no bracketing or
absence-of-known-change argument substitutes for attestation.

**THE BLOCKER IS AN IMAGE, NOT TEXT METADATA.** The akg catalogue-record request from
session 10 is **withdrawn** — it would only confirm a mid-1970s date already accepted.

> **Exact request: picture-alliance image `16008401` and image `16008415`, dated
> 04.11.1989, at maximum available resolution.** Both, because which one faces CET cannot
> be known in advance. Success criterion: the CET face identifiable by contents (BERLIN,
> PARIS, MADRID, WARSCHAU …) with **both bands legible line by line**. That either confirms
> the 97-letter transcription for 1989 or refutes it.

Fallbacks in order: `7728036` (05.08.1991, brackets the window — circumstantial only, since
interpolation needs monotonicity); `15638904` (01.01.1982, narrows whether this face changes
at all); the 22.05.1973 IDs (low value).

## 0a — Earlier status after Checkpoint H, local visual (session 10)

First session with actual pixels: four photographs pasted into the conversation and
read by this agent directly. Metric now **15 of 24 faces identified (62.5%), a 7-face
contiguous chain, 11 observed adjacency edges, 1 COMPLETE face**.

**The CET/UTC+1 face is fully transcribed** — upper 9 names/62 letters (alphabetical),
lower 6 names/35 letters (north-to-south, one inversion) — **97 letters total**. Graded
OBSERVATION, NOT EVIDENCE: not predicted in advance, ~0.54 such hits expected by chance
across 72 natural face quantities, and fragile to one name either way.

**Tier 1 is NOT met**, and for a single reason: the face's **date is unresolved**.
Tier 1 needs (a) a complete 97-letter tape — satisfied — and (b) that tape attested for
1988–89 — not satisfied. EXP-024 stays frozen, unrun, unmodified.

What changed since session 9:

1. **The arithmetic gap CLOSED.** 146 − 80 − 20 = 46, and the 1985 first major
   maintenance is the third change boundary that quantity requires. With boundaries at
   1969/1985/1997, any frame datable to **[1985, 1997)** shows the target state. Dating
   is now a yes/no question.
2. **But the one complete face is internally contradictory on date.** KOPENHAGEN, WIEN
   and ROM present (claimed 1985 additions) vs. a mid-1970s caption, 1970s clothing, and
   ATHEN — the fourth claimed 1985 addition — absent. LENINGRAD/MOSKAU fix it pre-1997.
   Either the 1985 change set or the caption is wrong; a 1985 *re-engraving* of existing
   names reconciles both.
3. **Stability: demonstrated NEGATIVE.** NOWOSIBIRSK changed faces between 1984 and the
   modern drum. Backward reversal cannot assume a place keeps its face. Within the
   target window, stability remains UNTESTED.
4. **Band assignment is no longer free.** Upper = northern, lower = southern within each
   sector, on four independent face pairs. This removes the 2^k half of per-face layout
   entropy; the k! within-band ordering remains.
5. **Half-hour faces carry a literal `+30`.** Read directly. Any tape reading crossing
   them must skip or transliterate digits — a free choice, so a penalised degree of
   freedom.
6. **Ordering is not one rule.** Upper alphabetical (9/9), lower not. Procedures assuming
   a single rule for both bands are wrong.
7. **Five target-era spellings differ from the modern list** (SWERDLOWSK, ASCHCHABAD,
   ALMA-ATA, LENINGRAD, PHOENGJANG), so the target-era letter multiset differs.

**THE SINGLE HIGHEST-VALUE NEXT ITEM — dating one image.** In cost order:

1. the **akg-images / picture-alliance catalogue record** for the Straube photograph used
   by WELT (article 217168174, image 1920313707) — its caption metadata carries a shoot
   date; one archive page decides (b);
2. any **dated 1985–1996 photograph of the CET/Berlin face**, legible;
3. **primary documentation of the 1985 maintenance change set**, to settle whether 1985
   added or re-engraved Athen/Kopenhagen/Wien/Rom.

Web-only, and this environment's egress to archive and image hosts is closed (re-tested:
`i.pinimg.com` → `connect_rejected`). Not being worked around by guessing.

## 0a — Earlier status after Checkpoint H continued (session 9)

Reconstruction advanced: **7 of 24 faces identified (29.2%), a 6-face contiguous
chain, 5 observed adjacency edges**. But **0 faces are COMPLETE and 0 lower bands
are transcribed**, so Tier-1 is NOT met.

Three findings changed the picture:

1. **Within-band order may be rule-determined.** Upper bands read alphabetical
   (UTC+1 1970s upper is strictly alphabetical, P=2.8e-6; all five multi-name groups
   in 1984/1989 are too). Lower bands read geographic, north-to-south. If order is
   rule-determined, order follows from MEMBERSHIP — a much weaker acquisition
   requirement. **SUPPORTED, NOT PROVEN.**
2. **The arithmetic does not close: 80 (1969) + 20 (1997) ≠ 146.** ~46 names entered
   at some other time. If any entered before 1997, the clock was still growing during
   the target period, and **a mid-1970s photograph is not evidence for 1989**.
   Stability is now the pivotal question.
3. **New blocker — Soviet-era zone membership.** The 1984 frame groups ALMA-ATA with
   TASCHKENT, correct for Soviet time zones but split in modern ones. Reversal must
   undo post-Soviet time-zone reorganisation too.

**Next acquisition target (narrowed):** a legible **1988–89** photograph of the
**UTC+1 lower band** — enough to identify which names are present. Secondarily, any
single face fully transcribed in **both** an early-1980s and a 1988–89 frame, which
would test stability directly (UTC+10 is the best candidate — CHABAROWSK is already
attested in both years).

**Cheapest unblock:** upload any candidate image as a **session file**. This agent
cannot fetch images but can read and transcribe uploaded ones directly.

## 0b — Earlier status after Checkpoint H: the bar is ONE FACE

EXP-027 establishes the operational threshold, and it is far lower than Checkpoint G
implied. A running-key test needs one contiguous 97-letter window, and single faces
already exceed that: **UTC+1 = 137 letters, UTC+3 = 126, UTC+2 = 108**.

> **Minimum faces needed for a 97-letter window: 1.**

**TIER 1 (restricted run permitted):** one contiguous arc of COMPLETE faces — both
bands, order known — totalling >= 97 letters. A restricted run must report the
fraction of the preregistered alignment space it covers. Currently 0 complete faces:
NOT MET.
**TIER 2 (full preregistered run):** all 24 faces complete plus the 1997 reversal.
NOT MET.

**The single highest-value acquisition** is a legible pre-1997 photograph of the
**UTC+1 face** — Berlin's own sector, 19 names, 137 letters, and the side a visitor is
most likely to photograph. UTC+1/+2/+3 carry 45.6% of all remaining layout entropy;
the Aug 1989 frame in hand (UTC+10/+11) carries 3.7%.

**Upload images as files.** This agent cannot fetch any image host, but CAN read and
transcribe uploaded image files directly — turning assertion into evidence.

See `docs/checkpoint-H-archive-targets.md` for the accession list and the decoded
Bundesarchiv accession structure.

## 0b — Earlier status after Checkpoint G: the priority has REVERSED

Blocker 1 is closed — the official 146-place modern list is stored and validated.
But EXP-026 establishes that **a name list can never unblock EXP-024**: even a
perfect 1989 list leaves ~10^125 physical arrangements, because the preregistered
procedures read upper/lower bands *in physical order*.

**So the dominant blocker is no longer the 1997 name changes. It is dated, legible
pre-1990 photographs of the drum**, at resolution sufficient to read the upper and
lower bands of individual sectors plus enough neighbouring faces to fix order.
Candidate holders: DDR-Bildarchiv, picture-alliance (1969–1982 material), Getty
(~231 tagged images), Bundesarchiv, DDR Museum. This is a human visual-transcription
task; images are not readable through this toolchain.

The 146-name endpoint makes that task much easier: a photograph no longer has to be
read cold, only matched against a known candidate set for its zone.

Blocker 7 (a "2015 restoration") is **retired** — July 2015 was monument protection.

## 0b — Earlier status after Checkpoint F

Blockers 2–4 are partially closed from contemporary December 1997 reporting: five of
~20 additions (Jerusalem, Tel Aviv, Cape Town, Oslo, Seoul), four renames (adding
Aschchabad→Aschgabat), one zone move (Kiew). The first genuine pre-1997 panel
fragment is established: the UTC+1 panel carried **… Bern, Bratislava, Belgrad …**
— adjacency sourced, band unknown.

A **seventh blocker** was found: the clock was also restored in **2015**, so
reversing 1997 alone is insufficient.

`k4lib/wz_panels.build_clock()` now **refuses** to build a historical clock while any
sector is UNKNOWN. Do not defeat that guard.

## 1 — Retrieve the modern Weltzeituhr city list, then run EXP-024

Priority: **highest**, and it is now a *minutes-long task for a human with a
browser*. `weltzeituhr-berlin.de` publishes a places-by-time-zone page. This
session could not retrieve it: `WebFetch` is blocked by the network egress proxy
for every external domain, and search summaries decline to enumerate lists. That is
an environment limit, not a gap in the historical record.

Ingest it with `k4lib.wz_panels.ingest_modern_list`, which stores the published
order as `modern_names_unsplit` and does NOT infer physical band placement from
table order. Then reverse 2015, then 1997.

With the historical list in hand, `EXP-024` runs unchanged — 22 preregistered reading
procedures, 2 alphabets, 2 directions, every offset, 12 conventions, ~480,000
alignments, validated end-to-end on a synthetic clock with a planted keystream.
Fill the six blocking items in `data/weltzeituhr.json`.

**Caution recorded in advance:** circular readings of the same clock share
substrings, so those alignments are NOT independent — the planted control was
recovered under three procedure labels, not one. Do not apply a naive binomial
correction.

Then, for the 1988–89 state:

A city-name tape read off the World Clock is ~900–1000 letters, ordered by the
object, hand-readable by an artist, needs no mathematics, and applies position by
position to a 97-character message. It satisfies every constraint established here:
long, low-entropy, externally sourced, position-indexed, named by a confirmed clue.
**It cannot be tested because the historical list is not public.**

Searched already, in English and German — see `docs/checkpoint-E-research-log.md`
for the full trail. Where to look next:

- GDR-era photographs of the drum at readable resolution (picture agencies, DDR
  Museum, Bundesarchiv);
- Erich John's design documentation or interviews;
- Berlin municipal / Stadtmuseum archives;
- **The Senatsbauverwaltung ↔ Auswärtiges Amt Sprachendienst correspondence (1997)** —
  the Senate building administration stated publicly in December 1997 that the
  spellings were coordinated with the Foreign Office language service in Bonn and the
  Senatskanzlei. One correspondence file would enumerate every 1997 name and spelling,
  closing blockers 2, 3 and 4 at once. **Highest-value single document.**
- **The 2015 restoration record** — blocker 7, entirely unknown.
- **The 1997 restoration records under Hans-Joachim Kunsch** — he executed the 1969
  construction on site *and* led the restoration, so his records would specify every
  change at once. Three renames (Leningrad→Sankt Petersburg, Alma Ata→Almaty,
  Bratislava→Pressburg) and four of ~20 additions (Tel Aviv, Cape Town, Seoul,
  Jerusalem) are already in hand.
- **The cylinder's orientation relative to north** — without it no bearing-based
  reading of `EASTNORTHEAST` can be evaluated at all. Note that with 24 faces every
  15°, any bearing lies within 7.5° of a face centre, so only an exact documented
  alignment carries information.

**Do not substitute a modern city list.** Twenty names were added in 1997 alone, and
the published counts (80 / 126 / 146 / 148) are mutually inconsistent.

## 2 — Verify the carved geometry photographically

Priority: **high**. `data/physical.json` grades the 4/31/31/31 line structure
MEDIUM-HIGH as transcription, MEDIUM as engraving, because reporting says the
engraved line lengths vary. Confirm from institutional photographs:

- exact characters per engraved line for the K4 section;
- which half of the screen carries the ciphertext (sources currently conflict —
  graded LOW and unusable);
- whether the tableau and ciphertext panels share any lattice at all.

## 3 — Hold the K5 diagnostic ready

Priority: standing. If K5's ciphertext is released, the **first** measurement is not
a cipher search. Line K4 and K5 up, find the agreeing positions, and read the memory
depth and direction off the edges of each shared run (EXP-021). That fixes the
architecture before any key is guessed. Depth would then very likely break both
messages even against a one-time pad (EXP-019).

## 4 — Residual openings, honestly labelled

- **A 25-symbol system followed by a second encoding layer.** Re-opened by the
  Checkpoint C audit; the output-alphabet argument sees only the final layer. Count
  free parameters before searching — a composite may land above the evidence budget,
  in which case record it as undecidable rather than searching it.
- **EXP-016 order B** for progressive/polynomial models: untested, not negative.
- **Feedback and relative-phase models under transposition:** untested.
- **Keystreams read off a chart, tableau, or numeric structure** rather than prose:
  untouched by EXP-022, which tested natural-language and place-name statistics only.
- **The Morse material used as anything other than a letter tape** — its dot/dash
  structure, for instance. EXP-023 tested only the tape reading.

## 5 — Do not pursue

- Position 63 / segmentation (demoted, Checkpoint B).
- Parity, K0 Morse, Kryptos rail selectors (1-in-1,024 selection effect).
- The Mengenlehreuhr (wrong clock, confirmed).
- The Morse material as a direct running-key tape (EXP-023, below chance).
- Compass-bearing routes (EXP-018) and the carved-line family (EXP-020).
- Panel-to-panel physical overlay — the two panels are not on the same lattice.
- Generic cipher-family enumeration — bounded above by the unicity result.
- **Any site publishing a claimed complete K4 plaintext.** See the exclusion list.

---

## Standing rules

- **Grade every conclusion**: PROVED IMPOSSIBLE / EXHAUSTIVELY ELIMINATED WITHIN
  SPECIFIED MODEL / STRONGLY DISFAVORED / HEURISTIC NEGATIVE / SUPPORTED
  INTERPRETATION / PROMISING HYPOTHESIS / UNTESTABLE WITH CURRENT PUBLIC DATA.
  "Negative" alone hides which one you mean, and "killed" or "proved" are only for
  the grades that warrant them.
- **State the model class** with every invariant. Three Checkpoint B results were
  over-scoped until the audit attached "monographic and position-preserving".
- **Plant a positive control** in every experiment.
- **Report whether the search finished.** A node cap is heuristic failure.
- **Count free parameters, not dimensions.** A physically-determined mechanism has
  almost no free parameters and is *maximally* testable however large it looks.
- **State the null and check trial independence.**
- **Protect the blind experiment.** Log every contamination incident at the time it
  happens, including near-misses.
- **Do not submit to the external verifier** without a complete 97-character
  plaintext, a deterministic method, parameters derived independently of that
  plaintext, exact crib reproduction, coherent non-crib text, and at least one
  prediction not used in construction.
