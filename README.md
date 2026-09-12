> **Checkpoint J:** [image audit](docs/checkpoint-J-image-audit.md) and
> [results](results/2026-09-12-codex-checkpoint-J.md). Three target-era faces
> (UTC+0/+1/+2), 272 letters frozen. ATHEN absence retracted. EXP-031: 29,184
> new multi-face cases, zero exact hits; 384 controls pass; independently verified.
> K4 remains unsolved. Older statuses below are historical.

> **Current audit (Checkpoint I):** see [Codex audit](docs/codex-audit.md) and
> [verified continuation](results/2026-09-12-codex-checkpoint-I.md). Historical
> entries below include superseded interpretations; the audit takes precedence.
> EXP-030: 172,800 constant-step CET tape cases, any fixed letter-to-number lookup,
> zero feasible mappings; 120 controls and independent certificates pass. K4 unsolved.

# Kryptos K4 research handoff

This repository preserves an ongoing, **unsolved** investigation into the 97-character
K4 cryptogram on Jim Sanborn's *Kryptos* sculpture. It is a reproducible handoff for a
human, ChatGPT, or another research agent — not a claimed solution.

## Current position

> **Checkpoint R (2026-09-12, `claude/k4-post-j`).** **EXP-039** closed the last
> structurally-motivated composition: a fixed monoalphabetic substitution after **double**
> columnar transposition, both keys from the precommitted list `{KRYPTOS, PALIMPSEST,
> ABSCISSA}`. All 9 ordered pairs give **distinct** composed permutations, none is the
> identity or a single pass, all three pairs fail to commute, and all 9 were shown
> **structurally** to lie outside EXP-033's corpus — by a run-decomposition test self-checked
> against the single passes it correctly finds. Exact null recomputed for this family
> (9.81×10⁻¹⁷ function, 5.52×10⁻¹⁸ bijection → 8.83×10⁻¹⁶ expected survivors). Result:
> **0 FEASIBLE-FUNCTION, 0 FEASIBLE-BIJECTION** — contradiction at the strongest level, no
> fixed map of any kind. Controls 9/9 planted, 9/9 adversarial (each mutating a repeated-letter
> group), plus a non-bijective plant correctly separating the two criteria; verified
> independently 35/35 with a selection sort and explicit grid simulation. Read narrowly: this
> is **not** "double transposition is eliminated". See
> [Checkpoint R](results/2026-09-12-claude-checkpoint-R.md).

> **Checkpoint Q (2026-09-12, `claude/k4-post-j`).** **EXP-038** closed the stateful
> recursive-key gap at its second-order affine scope: `k[n] = a·k[n-1] + b·k[n-2] (+ c) mod 26`
> over the **full Z26**, message-aligned, all 12 committed conventions. The state was decided
> **existentially** — the closed form makes each `(a,b,c)` a 24×2 exact linear system, so
> 210,912 solves replaced 143 million trials. **Zero feasible**, and *neither crib block is
> satisfiable on its own*, so it is not a near-miss. The null was computed from the family's
> own realised image (4,481,750 distinct crib projections of 26²⁴ → 5.9×10⁻²⁷ expected
> survivors), and the duplicate audit is quantitative: 11.9M tuples collapse to 7,585,006
> streams, of which 1,701,518 have a 97-prefix periodic with `p ≤ 23` and are tagged ALREADY
> COVERED. Verified **exhaustively and independently** — both 26⁴ and 26⁵ re-decided by direct
> iteration without importing `k4lib`, 16/16. Read narrowly: this is **not** "recursive keys
> are eliminated". See [Checkpoint Q](results/2026-09-12-claude-checkpoint-Q.md).

> **Checkpoint P (2026-09-12, `claude/k4-post-j`).** The public crib positions are now
> **externally verified** rather than inherited convention: contemporaneous NYT reporting
> fixes `BERLIN` at one-based 64–69, `CLOCK` at 70–74 and `NORTHEAST` at 26–34, and `EAST` is
> reporter-confirmed as the four letters immediately before `NORTHEAST` (grade B+, one step
> weaker, and recorded as such). Audited against the repository: every span reproduces the
> committed ciphertext and **no crib text or index changed**. Two consequences, both kept
> narrow: standard Fractionated Morse is now **structurally incompatible with the published
> positional crib semantics** (BERLIN needs 21 ternary symbols where six ciphertext letters
> supply 18) — *not* generalised to all Morse or all fractionation; and the alignment
> contingency on the **reflector-machine and Playfair** eliminations is **lifted**, checked by
> confirming their witnesses sit in the directly numbered spans (reflector at 33 and 74; 7 of
> Playfair's 10 pairs). No experiment was run. See
> [Checkpoint P](results/2026-09-12-claude-checkpoint-P.md).

> **Checkpoint O (2026-09-12, `claude/k4-post-j`).** Conservative session: symbolic audit
> only, **no new experiment run** — both candidate families were closed by exact structural
> observations costing seconds. **CM Bifid** reduces to EXP-012 (two 5×5 squares cannot emit
> the `J` K4 carries). **Digrafid** is closed by the primality of 97: a block system emitting
> `c > 1` per block gives length `c·m`, and no `c` in 2…96 divides 97. **Fractionated Morse**
> got real work, because EXP-023 left Morse-as-structure open: `n` ciphertext letters supply
> `3n` ternary symbols, and `BERLIN` needs 21 vs 18, `BERLINCLOCK` 44 vs 33, `NORTHEAST` 28
> vs 27 — while a 97-letter plaintext would need a mean of 2.01 Morse marks against an
> alphabet mean of 3.15. (`EASTNORTHEAST` fits *exactly* at 39 = 13×3; recorded, not
> pursued.) **Gromark** was rejected before any primer search — its key values are digits
> 0–9 and 11–16 of the 24 crib pairs demand a shift outside that set under every evidenced
> alphabet pair, so **EXP-038 was not assigned**. Named classical fractionators are now
> substantially exhausted; this is *not* "K4 is not fractionated". Next action: **verify the
> primary wording of the public clues** and pin the 24 crib constraints to a cited source —
> every experiment here consumes them as given. See
> [Checkpoint O](results/2026-09-12-claude-checkpoint-O.md).

> **Checkpoint M (2026-09-12, `claude/k4-post-j`).** Two of my own Checkpoint-L claims are
> **retracted**. (1) The "432 vs 435" discrepancy was my unit error: K1 = 63 characters,
> K2 = 372 *physical* characters = 369 letters + 3 `?`, so rows 1–14 = 435 characters = 432
> letters + 3 `?`. **Request 5 fulfilled, no discrepancy.** (2) The "alphabet frontier" was
> wrong: rebuilding the KRYPTOS keyword-mixed sequence from the keyword gives exactly
> `k4lib`'s `KRY`, all four STD/KRY plaintext×ciphertext combinations were already
> enumerated, and NSA gives KRYPTOS-mixed as both components for K1 *and* K2 — so the
> evidenced alphabet was covered all along. `PALIMPSEST`/`ABSCISSA` are repeating **keys**,
> not component keywords, so alphabets built from them are speculative; that candidate is
> **rejected**.
> Instead **EXP-036** closed the real gap — the hybrid the section sequence points at:
> K1/K2's **periodic polyalphabetic** over K3's **transposition**, sitting between EXP-003
> (this gate, 9,312 permutations) and EXP-033 (175 M permutations, one fixed monoalphabetic
> map). Decidability was computed *before* naming it: contiguous crib runs keep 7–22
> constraints across periods 2–23, and p = 24 was excluded in advance by the preregistered
> `N·26⁻ᶜ < 0.01` rule. The key is decided existentially, so every repeating key word of
> those lengths — `PALIMPSEST` and `ABSCISSA` included — is covered without adding
> parameters. **4,313,878,272 cases, zero feasible**, both composition orders; controls
> 72/72 planted, 72/72 adversarial (all capable of flipping the verdict), 72/72 period
> discrimination; independently verified 17/17 with 1.84 M cases re-decided by explicit
> grid simulation. Next: **vary the combiner** — the one structural assumption every
> experiment here still shares. See
> [Checkpoint M](results/2026-09-12-claude-checkpoint-M.md).

> **Checkpoint L (2026-09-12, `claude/k4-post-j`).** Checkpoint K's evidence request was
> fulfilled — the authoritative CIA/NSA cipher-side rows 1–24 — and it **corrected the
> geometry**: rows 1–24 hold **29–33** characters, not a uniform 31, so `32 + 27×31 = 869`
> gives the right total but is a false description and is retracted. Verified here, with
> three independent corroborations (336 K3 letters, `OBKR` + K4 = 97, canonical K1/K3
> openings) and one new unresolved discrepancy of my own finding (rows 1–14 give 432
> letters against the commonly cited 435).
> **No earlier result changes:** `audit/verify_geometry_correction.py` tests this per
> experiment, 25/25 — EXP-032 uses rows 25–28 only, EXP-033's F3 was checked cell by cell
> and never assumed a uniform panel, EXP-034 is purely textual. EXP-032's own printed
> assertion of the false arithmetic is corrected in place.
> **The physical "same column above" model is PARKED, not tested with a manufactured
> lattice:** with a monospaced punch and a common row width every row would hold the same
> count, so 29–33 means the pitch varies by up to 13.8% between rows and no common lattice
> exists. Checkpoint K's "parameter-free" description of it is withdrawn.
> Instead **EXP-035** used what the source *is* authoritative for — row content and order —
> and tested a running key drawn from the 745 characters engraved directly above K4, with
> an arbitrary letter-to-key function decided exactly: **43,824 cases, 41,412
> contradictions, zero feasible, zero undecided**, constraint counts 4–16, all controls
> capable of flipping the verdict, independently verified 14/14. That is a real loss for
> the architecture Checkpoint K ranked first. It also exposed a frontier: every experiment
> here assumes **shift** combiners over just two indexing alphabets, so the next step is to
> re-test under a precommitted set of keyword-derived mixed alphabets. See
> [Checkpoint L](results/2026-09-12-claude-checkpoint-L.md).

> **Checkpoint K (2026-09-12, `claude/k4-post-j`).** Continued from Codex Checkpoint J.
> The decisive audit finding is that **every experiment through EXP-031 assumes the key is
> a function of message position**, and the argument for that (EXP-021's K4/K5
> correspondence) is withdrawn by `docs/codex-audit.md` finding 7 — so architectures that
> *move* the plaintext were reopened. Three preregistered exact experiments, all negative,
> all independently verified:
> **EXP-032** key as an arbitrary function of engraving column — 12/12 contradictions;
> **EXP-033** arbitrary monoalphabetic substitution composed with a declared transposition
> family (keyed columnar widths 2–11 with **all** column orders, rectangle routes at every
> width, and routes on K4's real ragged engraving grid) — **175,820,784 cases, zero
> feasible**, against a computed chance-survival of 6.6×10⁻¹⁷ per permutation;
> **EXP-034** text-dependent keys as arbitrary functions of one source letter at one lag —
> 2,676 decided, zero feasible, 6,540 honestly reported UNDECIDED for lack of constraint.
> In none of these was the substitution or lookup enumerated: it is decided exactly by
> consistency, which is what keeps the families falsifiable.
> Also recorded: the corrected `OBKR` geometry **cannot** change any crib-constrained
> position- or column-indexed result, because no crib lies at K4 positions 0–3 and the
> corrected and old column maps agree for every i ≥ 4. The highest-information next step is
> an **evidence request**, not a search — the NSA cipher-side transcription of rows 1–24,
> which would make a key drawn from the characters physically above K4 testable. See
> [Checkpoint K](results/2026-09-12-claude-checkpoint-K.md) and
> [external evidence requests](docs/external-evidence-requests.md).

> **Checkpoint H, Tier 1 met (2026-09-12).** A 4 Nov 1989 press photograph — dated from its
> own `NEUES FORUM` / `SDP` banners, not from caption metadata — shows the **complete CET /
> UTC+1 face**, both bands and order: upper 9 names/62 letters (alphabetical), lower 9
> names/58 letters (strictly latitude-descending), **120 letters** in the target era.
> **Tier 1 is MET.** It also **refutes my own session-10 reading**: LONDON is on the
> neighbouring UTC+0 face, BERN and BRAZZAVILLE/KINSHASA/LUANDA were missed, and the
> **97-letter coincidence is withdrawn entirely** — it was a transcription error. Because it
> had been graded OBSERVATION, NOT EVIDENCE and refused as grounds to run the test, nothing
> was built on it. Reconstruction frozen first, EXP-024 left unmodified, then the permitted
> restricted run executed as **EXP-029: 11,520 alignments, 0 exact matches, best 7/24 against
> a chance mean of 0.92, positive control passed on the real tape — NEGATIVE.** The
> single-face running-key reading of the Berlin face is eliminated; multi-face readings are
> not, and are blocked on the neighbours' bands. Also withdrawn: the "upper = northern /
> lower = southern" rule and the hope that order follows from membership. See
> [Checkpoint H Tier 1](results/2026-09-12h5-checkpoint-H-tier1-met-and-negative.md).

> **Checkpoint H, 1974 correction (2026-09-12).** New external evidence — a Straube
> photograph explicitly dated **1974** already showing KOPENHAGEN and WIEN — forces two
> retractions of the previous checkpoint. The Tagesspiegel `nachgraviert 1985` wording may
> **not** be read as first addition, so the complete CET face's date is no longer disputed
> between the 1970s and [1985, 1997): it reads consistently as **mid-1970s**, which puts it
> **outside** the target window and makes the stability gap ~14 years instead of ~4. And the
> 46-name arithmetic gap is **not** "closed" — `146 − 80 − ~20 = ~46` is an unexplained
> remainder, not a dating. The CET transcription stands unchanged (97 letters, local visual);
> only the era it attests has changed. **Tier 1 NOT met; EXP-024 frozen, unrun, unmodified**,
> and the 97-letter coincidence is explicitly refused as justification. The blocker is now an
> **image, not text metadata**: picture-alliance **16008401** and **16008415**, dated
> **04.11.1989**, at maximum resolution. See
> [Checkpoint H 1974 correction](results/2026-09-12h4-checkpoint-H-1974-correction.md).

> **Checkpoint H, local visual (2026-09-12).** First session with actual photographs:
> four images read directly, lifting the reconstruction to **15 of 24 faces (62.5%)**,
> a **7-face contiguous chain**, **11 observed adjacency edges**, and the **first
> COMPLETE face** — the Berlin/CET face, upper 9 names (alphabetical, 62 letters) plus
> lower 6 names (north-to-south, 35 letters) = **97 letters**, K4's length. That 97 is
> graded **OBSERVATION, NOT EVIDENCE** (not predicted in advance; ~0.54 such hits
> expected by chance; fragile to one name). **Tier 1 is still NOT met** for one reason:
> that face's **date is unresolved** between a mid-1970s caption and a [1985, 1997)
> reading. **EXP-024 stays frozen, unrun and unmodified.** Also established: band
> assignment is northern-over-southern (removing the 2^k layout entropy), half-hour
> faces carry a literal `+30`, upper and lower bands do **not** share one ordering rule,
> and **a place changed faces between 1984 and today** — so backward reversal from the
> modern list cannot assume stable membership. The single highest-value next item is
> **dating one image**: the akg-images/picture-alliance catalogue record for the Straube
> photograph. See
> [Checkpoint H local visual](results/2026-09-12h3-checkpoint-H-local-visual.md).

> **Checkpoint H continued (2026-09-12).** External photographic evidence lifted the
> reconstruction to **7 of 24 faces (29.2%)** with a **6-face contiguous chain** —
> but **0 complete faces and 0 lower bands**, so Tier-1 is still NOT met and EXP-024
> stays frozen. Two findings matter most: within-band order may be **rule-determined**
> (upper bands alphabetical, lower bands north-to-south), and **the name arithmetic
> does not close** — 80 (1969) + 20 (1997) ≠ 146, leaving ~46 names unexplained, so a
> mid-1970s photograph is not evidence for 1989 without proven stability. See
> [Checkpoint H continued](results/2026-09-12h2-checkpoint-H-continued.md).


> **Checkpoint H (2026-09-12).** The reconstruction bar is now **one face**, not the
> whole drum: a 97-letter window fits inside a single large sector
> (UTC+1 = 137 letters, UTC+3 = 126, UTC+2 = 108). A legible pre-1997 photograph of
> the **UTC+1 face** — Berlin's own sector — would on its own permit a restricted run
> of the frozen EXP-024. See [Checkpoint H](results/2026-09-12h-checkpoint-H.md) and
> [archive targets](docs/checkpoint-H-archive-targets.md).
>
> This agent **cannot view any photograph** (all image hosts return HTTP 000), but
> **can read and transcribe images uploaded as files**. Current layout graph: 2 of 24
> faces identified, 1 observed adjacency edge, **0 complete faces**, 0 lower bands.


> **Checkpoint F (2026-09-12).** The modern city list is published but **denied by
> this environment's egress policy** — proven at three levels (`curl` returns
> `connect_rejected (organization policy)` while `pypi.org` returns HTTP 200).
> Contemporary December 1997 reporting closed part of the gap instead: five of ~20
> additions, four renames, one zone move, and the **first genuine pre-1997 panel
> fragment** — the UTC+1 panel carried *… Bern, Bratislava, Belgrad …*
>
> A seventh blocker surfaced: the clock was **also restored in 2015**, so reversing
> 1997 alone is not enough. And substituting the modern list is now measurably wrong:
> only **8–19%** of its 97-letter windows are free of post-1997 names.
>
> `wz_panels.build_clock()` refuses to fabricate a historical clock from incomplete
> data. EXP-024 remains **unaltered and unrun**. See
> [Checkpoint F](results/2026-09-12f-checkpoint-F.md).


> **Checkpoint E (2026-09-12).** The 1988–89 Weltzeituhr could **not** be
> reconstructed, and the hypothesis was not rescued. What changed: the object model
> is now correct — the city-name cylinder is **static**, with a rotating hour ring
> between an **upper** and a **lower** band of names, letters **stamped** from
> punches. The Weltzeituhr test is **built, preregistered and validated** on a
> synthetic clock, and blocked only on the name list
> ([EXP-024](results/2026-09-12e-checkpoint-E.md)).
>
> Sanborn's own Morse material — which he named in 2025 — was tested as a key tape
> and failed: 13,680 alignments, best 5/24, **below chance**.
>
> The immediate blocker is retrievability, not history: the modern per-sector list
> **is published**, but `WebFetch` is blocked here for every external domain. A
> human with a browser could supply it in minutes and run EXP-024 unchanged.


> **Checkpoint D (2026-09-12).** Four sessions converge on one architecture:
> **a keystream read off an external object, position by position.** The
> `BERLINCLOCK` crib names such an object. The bottleneck is now one specific piece
> of missing public data — the 1988–89 Weltzeituhr city configuration. See
> [the Checkpoint D record](results/2026-09-12d-checkpoint-D.md).
>
> Verified this session: K4's carved line structure is **OBKR + three lines of 31**
> (boundaries at 4, 35, 66), self-verified because the lines concatenate exactly to
> the canonical ciphertext. This *replaces* the 7×14 layout, which came from a
> source now on the [contamination exclusion list](docs/contamination-log.md).
> `EASTNORTHEAST` lies wholly inside line 1; `BERLINCLOCK` straddles the boundary
> at 66.
>
> New diagnostic: the pattern of breakage at the edges of a span shared by two
> messages measures a cipher's **memory depth and direction** directly. If K5 is
> ever released, that is the first measurement to make — before any key is guessed.


> **Checkpoint C (2026-09-12).** Sanborn confirmed in November 2025 that
> `BERLINCLOCK` is the **Weltzeituhr** at Alexanderplatz, not the Mengenlehreuhr.
> The principal World-Clock test has now been run and is negative. More importantly,
> a unicity calculation explains three sessions of failure at once, and identifies
> the bottleneck as external evidence rather than ideas. See
> [the Checkpoint C record](results/2026-09-12c-checkpoint-C.md) and
> [evidence grades](docs/evidence-grades.md).
>
> **K4's 97 characters can determine a key of at most ~66–76 letters.** What matters
> is key *entropy*, not length: a random 97-letter key is information-theoretically
> ambiguous and no method recovers it, while a structured long key — a running key
> from text, or a keystream read off a physical object — stays recoverable *only
> once its source is known*. The surviving hypotheses differ almost solely in which
> external source supplied the key, and 24 crib letters cannot tell them apart.
>
> The K4 **plaintext exists** — found September 2025 in Sanborn's Smithsonian
> donation, unpublished, sealed 50 years. Sanborn: *"They did not solve K4 and they
> certainly did not find the key."* **K5** exists too: 97 characters, shares coded
> words with K4 in the same positions — released only once K4 is solved. Simulation
> shows two messages in depth break each other even against a one-time pad.


Two sessions of work have moved this from "many untested ideas" to a narrow, documented
position. The most useful result is not an elimination:

> **24 crib letters supply 112.8 bits of constraint. Many remaining cipher families have
> more parameter entropy than that — they are not unsolved, they are unfalsifiable with
> the evidence in hand.** Between 3 and 35 more known plaintext letters would re-open
> every one of them.

Telling *eliminated* apart from *undecidable* is what this repository now offers.
See [ideas](docs/ideas.md) § 1 and the testability frontier in `EXP-011`.

Three one-line arguments did more than any search:

- **At least three encryption alphabets are forced.** Plaintext `E` occurs at positions
  21, 30, 64 and enciphers to `F`, `G`, `Y`. Every two-chart model is dead.
- **All 26 letters occur in K4**, so no cipher with a smaller output alphabet — bifid,
  Playfair, four-square, ADFGVX — can have produced it.
- **K4's IoC is 0.03608** against 0.0656 ± 0.0076 for English, so it cannot be an anagram
  of English: every route, columnar, spiral and grid transposition applied alone is dead
  without enumerating any of them.

These results were stress-tested: sliding each crib independently by −3..+3
(EXP-017), the three-alphabet bound and the impossibility of periods {1–7, 9} hold at
every one of 49 alignments, while the Playfair and reflector eliminations turn out to
be **contingent on the exact crib alignment** and are flagged as such.

The `DIAWINFBN` `+5` lead that opened the second session was **demoted**: it is the only
run of its kind in the ciphertext (family-wise p ≈ 0.017), but position 63 shows no
independent statistical support, and the run is provably unresolvable by crib algebra.

## Reproducing

```sh
./run_all.sh          # regenerates every experiment log into results/logs/
```

Python 3.11, standard library only. No network, no external corpus; RNG appears only in
permutation nulls and planted controls, always seeded.
Ciphertext SHA-256 `eea813570c7f1fd3b34674e47b5c3da8948026f5cefee612a0b38ffaa515ceab`.

## Layout

| Path | Contents |
| --- | --- |
| `data/k4.json` | The 97-character ciphertext and confirmed crib spans. Single source of truth. |
| `data/mask_sources.json` | Candidate running-key texts, each flagged `verified` or not. |
| `k4lib/` | Alphabets, the 12 shift conventions, structure probes, transposition families, the Berlin-Uhr model, parameter-linear keystream models, an exact Z₂₆ linear solver, and the method-recovery harness. |
| `experiments/` | One pre-registered experiment per file, each stating its hypothesis, parameter bounds, gate and positive control in its docstring. |
| `results/` | Dated result records and raw logs. |

## Method rules this work adopted

Earned the hard way; read before adding an experiment.

1. **Prefer an invariant to a search.** A search says "not found"; an invariant says
   "cannot exist", costs nothing, and retires a whole class.
2. **Count degrees of freedom first.** `modlin.chance_solvable` gives the exact chance a
   model class admits *any* solution for random data. Near 1 means the search is theatre.
3. **State the null, and check trial independence.** A "best 7/24" is meaningless without
   the expected best over the trials run.
4. **Plant a positive control.** A negative from code that cannot produce a positive is
   not a negative.
5. **Report whether the search finished.** Hitting a node cap is heuristic failure, not
   elimination.

## Where to start

0. [contamination log](docs/contamination-log.md) — **read first.** The blind-experiment
   rule, the standing source-exclusion list, and every logged incident.
0b. [evidence grades](docs/evidence-grades.md) — Regrades every
   conclusion and states what each argument does not cover.
1. [research state](docs/research-state.md) — inherited leads, and the facts actually
   verified by code here.
2. [new ideas](docs/ideas.md) — the surviving hypothesis space, ranked, with what is
   eliminated, what is undecidable, and what is worth doing.
3. [negative results](docs/negative-results.md) — what is closed, at what exact scope,
   and separately what is undecidable rather than negative.
4. [next steps](docs/next-steps.md) — the ordered work queue.
5. [resume prompt](docs/resume-prompt.md) — instructions for picking this up cold.

## Status

Prepared from the referenced ChatGPT conversation on 2026-09-11 and published by the
user. Extended 2026-09-12 with an executable toolchain, twenty-seven experiments, an exact
Z₂₆ solver, the testability frontier, robustness and evidence-grade audits, the
Weltzeituhr and compass-bearing tests, the unicity bound, the verified carved line
geometry, and the K4/K5 memory-depth diagnostic. **K4 remains unsolved, and no candidate
mechanism is claimed.**
