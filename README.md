# Kryptos K4 research handoff

This repository preserves an ongoing, **unsolved** investigation into the 97-character
K4 cryptogram on Jim Sanborn's *Kryptos* sculpture. It is a reproducible handoff for a
human, ChatGPT, or another research agent — not a claimed solution.

## Current position

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
user. Extended 2026-09-12 with an executable toolchain, twenty-five experiments, an exact
Z₂₆ solver, the testability frontier, robustness and evidence-grade audits, the
Weltzeituhr and compass-bearing tests, the unicity bound, the verified carved line
geometry, and the K4/K5 memory-depth diagnostic. **K4 remains unsolved, and no candidate
mechanism is claimed.**
