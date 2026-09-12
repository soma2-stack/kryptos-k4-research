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

## 1 — Retrieve the modern Weltzeituhr city list, then run EXP-024

Priority: **highest**, and it is now a *minutes-long task for a human with a
browser*. `weltzeituhr-berlin.de` publishes a places-by-time-zone page. This
session could not retrieve it: `WebFetch` is blocked by the network egress proxy
for every external domain, and search summaries decline to enumerate lists. That is
an environment limit, not a gap in the historical record.

With that list in hand, `EXP-024` runs unchanged — 22 preregistered reading
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
