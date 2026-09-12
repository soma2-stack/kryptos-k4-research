> **Checkpoint I supersedes stale interpretations below.** Read
> [the audit](codex-audit.md) and [current result](../results/2026-09-12-codex-checkpoint-I.md)
> first. Preserve the frozen 120-letter tape. Do not rerun historical large searches.

# AI resume prompt

You are continuing a reproducible Kryptos K4 investigation. This repository is a research handoff, not a claim that K4 has been solved.

1. Read `README.md`, `data/k4.json`, `docs/research-state.md`, `docs/negative-results.md`, and `docs/next-steps.md` before proposing an attack.
2. Preserve the zero-based crib spans and use them as hard tests.
3. Start by rebuilding and verifying the inherited `TOKIO → 57973` corpus: its 942 canonical route cases, definitions, inputs, and hash. Do not extend the reported 935 incomplete double-route cases until that base is reproducible.
4. Do not rerun a broadly ruled-out family unless you state an exact, material difference.
5. Keep hypotheses separate from facts. An inherited result needs independent replication. A crib-fitting method is not a solution unless it gives a complete, externally specified transform of all 97 characters.
6. For every run, save code, input hashes, full parameter bounds, count of variants, and result. Log negative results.

If no original corpus is available, create a precise specification of the expected 942 cases and identify the missing source evidence rather than inventing an enumeration.

## Addendum — 2026-09-12

The repository now contains code. Before proposing anything:

7. Run `./run_all.sh` and read `results/logs/`. The 12 shift conventions, the structure
   probes and the complete affine-mod-97 transposition family are already implemented in
   `k4lib/`; do not rebuild them.
8. Read `docs/ideas.md`. Items 1–5 are run and their scopes are exact. Items 6–11 are
   specified and unrun — start there rather than inventing a twelfth.
9. Apply the bounded-source lemma (`ideas.md` § 9) to any new proposal before writing a
   search: if your key source cannot emit 24 or 25, it is already dead for 8 of the 12
   conventions.
10. Report the null expectation alongside any "best N/24" score. A best of 7/24 over 44,000
    trials is exactly what chance produces and is not a lead.
11. If you ever obtain a candidate 97-character plaintext, stop searching and run
    `k4lib.recover.diagnose` on it. See `ideas.md` § 1.

## Addendum — 2026-09-12 (session 2)

Fifteen experiments now exist. Before proposing anything:

12. Read `docs/ideas.md` first. It separates what is **eliminated** from what is
    **undecidable with 24 crib letters**. Proposing something from the second list is
    the most common way to waste effort here.
13. Run the four free checks in `ideas.md` § 5 against your idea before writing code:
    the bounded-source lemma, alphabet-free period elimination, output-alphabet
    coverage, and the block-coverage rule. Each costs nothing and several retire whole
    families.
14. Compute `modlin.chance_solvable` for your model before searching it. If it is near
    1, the model has more freedom than the cribs constrain and any fit is meaningless.
15. The shortest period K4 could possibly have is **8**; at least **three** encryption
    alphabets are forced; **all 26 letters** occur in the ciphertext.
16. Do not build on position 63. It was pursued hard in session 2 and demoted.
17. If your search hits an iteration or node cap, report it as inconclusive. Only a
    completed search is an elimination.

## Addendum — 2026-09-12 (Checkpoint C)

18. **Read `docs/evidence-grades.md` before anything else.** Several earlier
    conclusions were over-scoped. The three-alphabet bound, the period elimination
    and the conflict census hold only for **monographic, position-preserving**
    ciphers; the output-alphabet argument sees only the final layer; the IoC
    argument is statistical; the bit-budget frontier is a heuristic.
19. `BERLINCLOCK` is the **Weltzeituhr**, not the Mengenlehreuhr (Sanborn,
    Nov 2025). EXP-002 tested the wrong clock. EXP-018 is the real test: negative.
20. Before proposing any new cipher search, read EXP-019. K4 can determine a key of
    at most ~66–76 letters. If the key is long and random, nothing works; if it is
    long and structured, only knowing its **source** helps. Searching short-key
    families further is bounded above by this.
21. The bit-budget penalty applies to **free** parameters, not dimensionality. A
    mechanism read off a physical object has almost no free parameters and is
    *maximally* testable — this is the one direction the frontier argument
    encourages rather than blocks.
22. Two closable data gaps block the object branch: primary verification of the
    7×14 K4 layout, and the **1989** Weltzeituhr city configuration. Do not
    substitute a modern city list for the historical one.

## Addendum — 2026-09-12 (Checkpoint D)

23. **Read `docs/contamination-log.md` first.** This is a blind experiment. The only
    plaintext admitted as a constraint is `EASTNORTHEAST` and `BERLINCLOCK`. Never
    seek, fetch or ingest a purported K4 plaintext; never use a site whose purpose
    is publishing one. Log every incident, including near-misses, when it happens.
24. The verified K4 geometry is **OBKR + three lines of 31** (boundaries 4, 35, 66),
    not 7×14. The 7×14 layout came from an excluded source.
25. The engraved line lengths **vary** (Sanborn kerned them), so the ciphertext panel
    and the tableau panel are not on a common lattice. Panel-overlay mechanisms are
    strongly disfavoured.
26. The Weltzeituhr's city-name cylinder is **static**; an hour ring rotates inside.
27. Before proposing anything, read the convergence in `docs/next-steps.md`: the
    surviving architecture is a keystream read off an external object, position by
    position. The blocker is the **1988–89 Weltzeituhr city list**, which is not
    public. Do not substitute a modern list — 20 names were added in 1997 alone.
28. If K5 is released, run the EXP-021 memory-depth diagnostic before anything else.
29. Do not submit to the external verifier without all six conditions in
    `docs/next-steps.md`.

## Addendum — 2026-09-12 (Checkpoint E)

30. The Weltzeituhr object model is `data/weltzeituhr.json`, with confidence grades
    and six explicit blocking items. The city-name cylinder is **static**; a
    rotating hour ring sits between an **upper** and a **lower** band of names;
    letters are **stamped**. Do not re-introduce the "rotating drum" error.
31. `EXP-024` is built, preregistered and validated on a synthetic clock — but NOT
    RUN. It needs the per-sector name list. Fill the six blocking items and it runs
    unchanged. Do not invent names to make it run.
32. The modern list is published at `weltzeituhr-berlin.de`; this environment blocks
    `WebFetch` for all external domains. Retrieving it is a browser task, not a
    research task.
33. Circular clock readings share substrings — the planted control was recovered
    under three procedure labels. Those alignments are NOT independent.
34. The Morse material as a running-key tape is a HEURISTIC NEGATIVE (EXP-023,
    below chance). Its non-tape uses are untested.
35. Both keystream-statistics probes (English prose, place names) fail correction.
    Do not rescue the city-tape hypothesis with arbitrary transformations.

## Addendum — 2026-09-12 (Checkpoint F)

36. `data/weltzeituhr_panels.json` is the panel evidence matrix — one entry per
    displayed sector. Do NOT collapse the clock into a running text before this
    layer is real. Published table order is stored as `modern_names_unsplit` and is
    **not** evidence of physical upper/lower band placement.
37. `k4lib/wz_panels.build_clock()` REFUSES to build a historical clock while any
    sector is UNKNOWN. Do not defeat the guard. `allow_incomplete=True` stamps the
    output NOT historical and must never be used for a reported result.
38. Substituting the modern list is measurably wrong: only **8–19%** of its
    97-letter windows are free of post-1997 names (EXP-025).
39. There are now **seven** blockers, not six — the **2015 restoration** change set
    was missed by Checkpoint E.
40. Recovered pre-1997 fragment: the UTC+1 panel carried *… Bern, Bratislava,
    Belgrad …* — adjacency sourced from Dec 1997 reporting, **band unknown**.
41. Highest-value single document: the **Senatsbauverwaltung ↔ Auswärtiges Amt
    Sprachendienst** 1997 correspondence on the spellings. It would close blockers
    2, 3 and 4 together.
42. In this environment only package registries are reachable. `curl https://pypi.org/`
    returns 200; everything else is `connect_rejected (organization policy)`.
    Retrieving the city list is a browser task, not a research task.
43. EXP-024 is unaltered and unrun. Do not tune its 22 preregistered procedures
    after the data arrives.

## Addendum — 2026-09-12 (Checkpoint G)

44. Blocker 1 is CLOSED. The official 146-place modern list lives in
    `data/weltzeituhr_modern_official.json`, validated, marked MODERN. Never copy a
    value from it into a `pre1997_*` field without documented evidence of reversal.
45. **Table order is NOT physical order — demonstrated**, not merely cautioned: the
    sourced adjacency Bern–Preßburg–Belgrad has Rom, Tunis and Kinshasa interposed
    in the table. Parenthetical forms ("Bratislava (Pressburg)", "Vilnius (Wilna)")
    are a website convention, not engraved text.
46. The 24 faces are CONFIRMED: exactly 24 whole-hour zones, UTC−10…+13. The five
    half-hour places cannot own a face; their physical placement is an open question.
47. 2015 was **monument protection**, not a restoration. Checkpoint F's blocker 7 is
    retired. Apia's 2011 change is a date-line label matter on the same face.
48. **THE PRIORITY IS REVERSED (EXP-026).** Even a perfect 1989 name list leaves
    ~10^125 physical arrangements, so a name list can NEVER unblock EXP-024. The
    dominant blocker is dated, legible pre-1990 photographs giving band and order.
    Do not spend further effort on the name list believing it will unblock the test.
49. Classification lives in `data/weltzeituhr_classification.json`: 12/146 (8.2%)
    determined. Classify only from evidence — geopolitical intuition is not evidence.
50. EXP-024 remains frozen, unmodified and unrun.

## Addendum — 2026-09-12 (Checkpoint H)

51. The threshold to run EXP-024 is **ONE FACE**, not the drum. A 97-letter window
    fits inside UTC+1 (137 letters), UTC+3 (126) or UTC+2 (108). TIER 1 = one
    contiguous arc of COMPLETE faces >= 97 letters, run restricted and reported as
    such. TIER 2 = all 24 faces. Currently 0 complete faces.
52. Highest-value acquisition: a legible pre-1997 photograph of the **UTC+1 face**,
    both bands, names in order. UTC+1/+2/+3 hold 45.6% of remaining layout entropy.
53. This agent cannot fetch ANY image host (HTTP 000) but CAN read images uploaded
    as session files. Ask for uploads; do not accept transcriptions blindly.
54. `data/weltzeituhr_photos.json` + `k4lib/wz_graph.py` hold the evidence and the
    adjacency graph. Edges are OBSERVED or TRANSITIVE and must never be conflated.
55. **Geometry rule, non-negotiable:** the cylinder is STATIC, the hour ring ROTATES.
    An hour numeral beneath a face NEVER identifies that face. Assign sectors from
    city contents and adjacency only.
56. Bundesarchiv accessions read `183-YYYY-MMDD-frame` (modern) or
    `183-<LETTER>MMDD-frame` (ADN, letter = year). Seven undated Weltzeituhr
    candidates are listed in `docs/checkpoint-H-archive-targets.md`.
57. Stability 1969-1997 is UNTESTED. Proving it would unlock the whole 1970s-80s
    photo pool. Never assume it.
58. EXP-024 remains frozen, unmodified and unrun.

## Addendum — 2026-09-12 (Checkpoint H continued)

59. External evidence is in `docs/external/checkpoint-H-web-photo-handoff.md`. Every
    reading from it is an EXTERNAL-AGENT TRANSCRIPTION, never this agent's own visual
    verification. Do not promote any of it to ground truth without a second source or
    a locally readable image.
60. Layout now: **7 of 24 faces, 29.2%, 6-face chain, 5 observed edges — but 0
    COMPLETE faces and 0 lower bands.** Tier-1 NOT met.
61. **Ordering may be rule-determined**: upper bands read alphabetical (UTC+1 1970s
    upper, P=2.8e-6; all five 1984/1989 multi-name groups too), lower bands read
    north-to-south by latitude. The discriminator against transcriber bias is that
    the same agent rendered the modern lower band NON-alphabetically. SUPPORTED, NOT
    PROVEN. If true, ORDER follows from MEMBERSHIP.
62. **The arithmetic does not close: 80 + 20 != 146**, ~46 names unexplained. So the
    clock may still have been growing before 1997, and a mid-1970s photo is NOT
    evidence for 1989. STABILITY is now the pivotal question.
63. **New blocker**: Soviet-era zone membership differs from modern (ALMA-ATA with
    TASCHKENT on one face in 1984). Reversal must undo post-Soviet time-zone changes.
64. Do NOT report the "9 letters short" figure as near-completion. Tier-1 needs a
    COMPLETE face; a partly-read band gives a tape with unknown gaps and is unusable.
65. Best stability test available: fully transcribe the UTC+10 face in both a 1984
    and a 1988-89 frame. CHABAROWSK is already attested in both.
66. EXP-024 remains frozen, unmodified and unrun.

## Addendum — 2026-09-12 (Checkpoint H, local visual — session 10)

Read `results/2026-09-12h3-checkpoint-H-local-visual.md` first, then
`data/weltzeituhr_photos.json` (fields `local_visual_session`, `findings`,
`date_problem`, `face_aliases`).

State you are resuming into:

- **15/24 faces identified (62.5%), 7-face chain, 11 observed edges, 1 complete face.**
- The **CET/UTC+1 face is fully transcribed at 97 letters** from my own visual reading.
  Treat the 97 as OBSERVATION, NOT EVIDENCE — it is not a reason to run EXP-024.
- **Tier 1 NOT met.** The tape exists; its **date** does not. EXP-024 remains frozen,
  unrun and unmodified.
- The four source images were conversation attachments with no path or hash. You cannot
  re-verify my readings. They are recorded as this agent's testimony, not as files.
- Established physical rules, era-independent and safe to build on: upper band =
  northern places, lower = southern; half-hour faces inscribed `+30`; upper bands
  alphabetical, lower bands not.
- Established negative: **membership is not stable** — NOWOSIBIRSK changed faces between
  1984 and the modern drum. Do not reverse the modern list assuming fixed faces.
- The blocker is a single external lookup: the **akg-images / picture-alliance catalogue
  record** for the Straube photograph (WELT article 217168174, image 1920313707). Its
  shoot date decides Tier 1. Egress to archive and image hosts is closed here.

Do not date the image by inference to get past this. If it stays unresolved, say so.

## Addendum — 2026-09-12 (Checkpoint H, 1974 correction — session 11)

Read `results/2026-09-12h4-checkpoint-H-1974-correction.md` first. It retracts two claims
from the session-10 record, which now carries a supersession notice.

- The complete CET face (97 letters) **stands unchanged** as LOCAL VISUAL evidence. Do not
  re-transcribe it without new image evidence.
- Its date is **mid-1970s**, not disputed. `nachgraviert 1985` is not a first-addition
  claim: a 1974 Straube frame already shows KOPENHAGEN and WIEN. The stability gap to
  1988–89 is **~14 years**.
- The 46-name arithmetic gap is **an unexplained remainder, not "closed"**. Do not date it
  to 1985.
- **Tier 1 NOT met. EXP-024 frozen, unrun, unmodified.** The 97-letter coincidence is not
  justification — it is OBSERVATION, NOT EVIDENCE, on a frame ~14 years pre-target.
- Do not argue stability from absence of known change: membership is non-monotonic
  (NOWOSIBIRSK moved faces), and 1985 demonstrably touched CET-lower lettering.
- Graph rules to preserve: faces keyed by **(sector, era)**; a complete band reading is
  authoritative and a partial one corroborates or conflicts, never degrades.
- **The blocker is an image.** Needed: picture-alliance `16008401` and `16008415`
  (04.11.1989), max resolution, CET face with both bands legible. Fallbacks: `7728036`
  (1991, circumstantial), `15638904` (1982, narrows only).

If it is still not supplied, say so and stop. Do not infer the 1988–89 CET face.

## Addendum — 2026-09-12 (Checkpoint H, Tier 1 met — session 12)

Read `results/2026-09-12h5-checkpoint-H-tier1-met-and-negative.md` first.

- **Tier 1 is MET** on the CET/UTC+1 face from a 4 Nov 1989 frame: 120 letters, frozen in
  `data/weltzeituhr_photos.json → tier1_frozen_reconstruction`. That block is FROZEN — change
  it only on new image evidence, never in response to a test result.
- **EXP-029 ran the permitted restricted test and it is NEGATIVE**: 11,520 alignments,
  0 exact matches, best 7/24 (chance mean 0.92), positive control passed on the real tape.
  EXP-024 itself remains unmodified and not re-run.
- **The 97-letter coincidence is WITHDRAWN** — my own transcription error (LONDON belongs to
  the UTC+0 upper band). Do not resurrect it. EXP-028 asserts it cannot creep back.
- Also withdrawn: "upper = northern / lower = southern", and the hope that order follows from
  membership. Each face's order must be read off a photograph.
- Two alignments hit 7/24 (`STD dir+1 variant_beaufort/P=KRY/C=KRY`, offsets 78 and 16),
  Poisson p ≈ 0.03 on a post-hoc maximum. **Do not pursue them and do not consult the
  external verifier.**
- What is still open: multi-face readings (most of EXP-024's space), non-running-key uses of
  the object. Blocked on the UTC+0 and UTC+2 bands.
- Ask: a target-era close frame from a different bearing — picture-alliance `16008401` /
  `16008415` (whichever was not uploaded), or HanisauLand `153695.jpg`.

K4 remains unsolved. The first mechanism this programme could finally test came back negative.
