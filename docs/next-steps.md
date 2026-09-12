# Next experiments

Rewritten 2026-09-12 after Checkpoint C. Read `docs/evidence-grades.md` first: it
regrades every earlier conclusion and states what each argument does *not* cover.

## The situation in one paragraph

Three sessions have eliminated short-key and structured-key models at scale and
found nothing. EXP-019 explains why in one line of arithmetic: K4's 97 characters
carry ~310–359 bits of redundancy, so they can determine a key of at most 66–76
letters. What matters is key **entropy**, not length. A random 97-letter key is
information-theoretically ambiguous and *no* method recovers it. A structured long
key — a running key from text, or a keystream read off a physical object — has low
entropy and remains recoverable, **but only once the right source is guessed**. The
surviving hypotheses differ from one another almost solely in *which external
source supplied the key*, and 24 crib letters cannot tell them apart.

That reframes the work. The bottleneck is no longer ideas or compute. It is
external evidence.

---

## 1 — Acquire evidence, in this order

Priority: **highest**, and it dominates everything below.

1. **K5's ciphertext.** 97 characters in depth with K4 would very likely break both,
   *even against a one-time pad*: EXP-019 shows by simulation that `C1−C2 = P1−P2`,
   that shared words at shared positions are directly visible, and that dragging 24
   known letters of one message reads 24 letters of the other with no key knowledge.
   Sanborn releases it only once K4 is solved — a circular lock, but worth tracking.
2. **The K4 plaintext.** It exists. It was found in September 2025 and sealed for 50
   years. If it becomes available, stop searching and run
   `k4lib.recover.diagnose` (EXP-005 validates the harness).
3. **More crib letters.** EXP-011 quantifies: 3 to 35 more re-open every family now
   beyond reach. Re-run EXP-011 whenever the crib set changes.

## 2 — Close the two physical-data gaps

Priority: **high**. These are the only gaps a researcher can close without waiting
on a release, and both currently block the object-based branch.

- **Primary verification of the K4 physical layout.** `data/physical.json` records
  7 rows × 14 columns, 98 cells, one blank — at MEDIUM confidence, because it traces
  mainly to a site whose solution claim Sanborn disputes. Verify against the NSA
  transcript or a photograph. EXP-018's grids depend on it.
- **The 1989 Weltzeituhr city configuration.** Recorded as UNKNOWN. The clock carried
  ~80 city names in 1969 and ~148 today, and was restored in 1997 and 2015 with names
  updated. **A modern city list must not be substituted for the one Sanborn could
  have seen.** Without it, no city-name keystream from the World Clock can be tested
  honestly. Sources to try: GDR-era photographs, Erich John's design documentation,
  Berlin municipal archives.

## 3 — The residual opening the audit re-opened

Priority: medium. `docs/evidence-grades.md` found one family that Checkpoint B
closed wrongly: **a 25-symbol system followed by a second encoding layer** that
re-expands to 26 letters. The output-alphabet coverage argument only ever sees the
final layer, so it says nothing about a composite. Before searching it, count free
parameters — a two-layer composite may well land above the evidence budget, in which
case record it as undecidable rather than searching it.

## 4 — Declared gaps in completed sweeps

Priority: medium-low, but they are gaps, not negatives, and should be labelled as
such wherever they are cited.

- **EXP-016 order B** for the progressive and polynomial models: the coefficient
  matrix depends on the permutation and cannot be pre-factored. Untested.
- **Feedback and relative-phase models under transposition** (EXP-008 and EXP-015
  families crossed with the permutation family). Untested.

## 5 — Specify, do not reconstruct, the `TOKIO → 57973` corpus

Unchanged. Its route definitions and hash were never committed; reconstructing 942
cases from a count alone is inventing an enumeration.

## 6 — Do not pursue

- **Position 63 / segmentation.** Demoted in Checkpoint B; no independent support.
- **Parity, K0 Morse, Kryptos rail selectors.** A 1-in-1,024 selection effect.
- **The Mengenlehreuhr.** The wrong clock, now confirmed.
- **Compass-bearing routes.** Eliminated by EXP-018 within a specified model.
- **More generic cipher-family enumeration.** Bounded above by the unicity result:
  if the key is long, this cannot succeed however long it is run.
- **Berlin→Moscow as a cipher mechanism.** The bearing coincidence is real but
  deflates under jitter and sector width; keep it as an interpretation of what the
  plaintext *says*, not of how it was enciphered.

---

## Required result record

Unchanged, and exemplified by the three dated records in `results/`. Six additions
learned across the sessions:

- **State the null, and check trial independence.**
- **Plant a positive control.** Every experiment here carries one.
- **Report whether the search finished.** A node cap is heuristic failure, not
  elimination.
- **Count free parameters before searching.** `modlin.chance_solvable` gives the
  exact chance a model class admits any solution for random data — but note the
  audit's correction: the penalty applies to **free** parameters, not to
  dimensionality. A physically-determined mechanism has almost none and is
  *maximally* testable however large it looks.
- **Prefer an invariant to a search**, and then **state its model class**. The most
  productive results here are one-line arguments — but three of them were originally
  over-scoped, and the qualifier is part of the result.
- **Grade every conclusion.** PROVED IMPOSSIBLE / EXHAUSTIVELY ELIMINATED WITHIN A
  SPECIFIED MODEL / STRONGLY DISFAVORED / HEURISTIC NEGATIVE / UNTESTABLE WITH
  CURRENT DATA. "Negative" alone hides which one you mean.
