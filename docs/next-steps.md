# Next experiments

Updated 2026-09-12. The inherited priorities are preserved below the new ones, with an
explicit note on why the ordering changed.

## Why the ordering changed

The inherited plan put reconstructing the `TOKIO → 57973` corpus first. That was the right
call for a repository with no code, because it was the narrowest finite piece of unfinished
work. It is now second, for one reason: the corpus cannot be reconstructed. Its route
definitions, enumeration order and hash were never committed anywhere in this repository,
and `resume-prompt.md` already anticipates this — *"if no original corpus is available,
create a precise specification and identify the missing source evidence rather than
inventing an enumeration."* Reconstructing 942 route cases from a count alone **is**
inventing an enumeration. The honest version of that task is a specification plus a
request for the missing evidence, which is item 3.

Meanwhile a lead that *is* actionable has appeared. See item 1.

---

## 1 — Segment boundary at position 63

Priority: **highest**. See `ideas.md` § 2.

The `DIAWINFBN` `+5` run terminates exactly on the first letter of the BERLINCLOCK crib.
Two cheap experiments follow directly and neither has been run:

- **Per-segment periodicity.** Re-run EXP-001's period probes within `[0,21)`, `[21,34)`,
  `[34,63)`, `[63,74)`, `[74,97)` instead of globally. A key that restarts mid-message is
  aperiodic globally but periodic within a segment — which would explain every negative in
  this repository at once.
- **Constant lag-4 key advance.** Under each convention, test whether the crib-forced keys
  satisfy `k[i+4] − k[i] = c` for a constant `c` across the crib spans.

Extend `experiments/exp001_crib_keystreams.py`; the probes already exist in `k4lib/analysis.py`.

## 2 — Progressive-key and Gromark-family generators

Priority: **high**. See `ideas.md` § 6.

Every negative recorded here assumes the key repeats or is a fixed external text. The
classical family that is neither — progressive keys, and lagged-Fibonacci generators over
a short numeric primer — defeats period tests by construction, was standard in the relevant
literature, is small enough to enumerate, and is the only family that gives item 1's `+5`
run a natural mechanism. Gate on all 24 crib letters. Report the total variant count.

## 3 — Specify, do not reconstruct, the `TOKIO → 57973` corpus

Priority: **high**, but as a specification-and-evidence task, not a search task.

- Write the specification before any code: source data, normalisation, physical coordinate
  system, the definition of every route family, enumeration order, and the expected hash.
- State precisely which source evidence is missing and where it would have to come from.
- Do **not** enumerate 942 cases chosen to hit the number 942. A count is not a definition.
- Only once real definitions are recovered: implement, hash, and publish a status table for
  every case before touching the 935 double-route cases.

## 4 — Audit the selector leads for degrees of freedom

Priority: **medium**, and it should precede any further work on them. See `ideas.md` § 7.

The two-chart homophonic model, the K0 Morse selector and the Kryptos rail alternation are
all the same kind of claim: a selector that produces no contradiction at the cribs. Absence
of contradiction is what any sufficiently flexible model produces. Count the consistent
selectors. If the count is astronomical the lead is vacuous and can be demoted to `negative`
on information-theoretic grounds, with no further cryptanalysis. If it is small the selector
becomes a real prediction. Either result is worth more than more searching.

## 5 — Bounded `4 × 22` lookup experiments

Priority: medium. Unchanged from the inherited plan, with one addition: apply the
bounded-source lemma (`ideas.md` § 9) as a pre-filter. Any lookup whose output is bounded
below 25 is already excluded for 8 of the 12 conventions, with no search.

Test only small, pre-registered rule classes of the form `P = f(C, T[col], row, col)` where
`T = JAKUTSKPJOENGJANGTOKIO`. Constrain every degree of freedom, require all crib letters,
reserve a holdout family of positions, and report the total search count, not just the best
score.

## 6 — Audit the source transcription and geometry

Priority: supporting work, now with a concrete consumer. See `ideas.md` § 10.

`data/mask_sources.json` currently carries **unverified** K1–K3 plaintexts, which is why
EXP-004's result for those sources is `inconclusive` rather than `negative`. A machine-readable
physical transcript preserving row/column alignment, panel boundaries, tableau orientation,
omissions and exact normalisation would close that gap and is a prerequisite for testing the
segmentation hypothesis against physical structure. Transcribe it from the NSA primary
reference in `sources.md`. Do not reconstruct it from memory.

## 7 — The carved tableau as a running key

Priority: medium. See `ideas.md` § 5.

EXP-004 consumed every long text in this repository except the one physically on the
sculpture: the tableau block itself, read by row, column and diagonal.
`k4lib/alphabets.vigenere_tableau` already generates it; the experiment is a small extension
of `experiments/exp004_running_key_mask.py`.

---

## Required result record

Unchanged, and now exemplified by `results/2026-09-12-exp001-005.md`. For each experiment
create a dated Markdown record with: hypothesis; input source and hash; code revision; full
parameters; number of variants; crib result; output/hash; negative or positive conclusion;
and the exact reason it differs from prior work.

Two additions learned from this round:

- **State the null.** A "best 7/24" means nothing without the expected best over the number
  of trials run. EXP-004 reports the exact binomial tail; do the same.
- **Self-test the apparatus.** A negative from code that cannot produce a positive is not a
  negative. `experiments/exp005_recovery_selftest.py` plants known constructions and checks
  they are recovered; extend it whenever you add a probe.
