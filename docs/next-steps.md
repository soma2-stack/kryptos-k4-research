# Next experiments

Rewritten 2026-09-12 after the second research session. The ordering changed
substantially because two sessions of elimination changed what is worth doing.

## What changed, and why the list is shorter

Session 1 built the toolchain and closed the obvious families. Session 2 set out to
pursue the position-63 lead and instead **demoted it** while closing far more:
parameter-linear keystreams, feedback keystreams, five cipher classes by invariant,
two-chart models, fractionation, and Quagmire I.

The most important result is not an elimination at all. **24 crib letters supply
112.8 bits, and many remaining families have more parameter entropy than that.**
They are not unsolved — they are *unfalsifiable with the evidence in hand*.
Distinguishing those two is now the main thing this repository offers, and it makes
"try another cipher" a much less valuable move than it looks.

---

## 1 — Treat acquiring constraint as the primary objective

Priority: **highest**. See `ideas.md` § 1 and EXP-011.

Between **3 and 35** more known plaintext letters would re-open every family
currently beyond reach. One further released clue the size of NORTHEAST would make
Quagmire I decidable outright. Concretely:

- Track any further Sanborn clue or archive disclosure; each one changes what is
  testable, and EXP-011 already computes by how much.
- If a candidate 97-character plaintext appears from any source, **stop searching**
  and run `k4lib.recover.diagnose` on it (`ideas.md` § 2). The harness exists and is
  validated.
- Re-run EXP-011 whenever the crib set changes. It is cheap and it re-plans the work.

## 2 — Transposition with a pre-fixed alphabet: finish the remaining corner

Priority: **high**, and **mostly done** — EXP-016 closed the main cross product:
10,160 permutations × 12 conventions × 25 keystream models, 4,145,280 gate
evaluations, zero fits.

Two declared gaps remain, both small and both worth closing:

- **Order B for the progressive and polynomial models.** The key indexed on the
  ciphertext side makes the coefficient matrix depend on the permutation, so it
  cannot be pre-factored the way EXP-016 does. It is untested, *not* negative.
  Either accept the cost of a per-permutation solve, or derive an O(24) check the
  way the periodic case has one.
- **Feedback and relative-phase models under transposition.** EXP-016 covered
  progressive, polynomial and periodic. The EXP-008 and EXP-015 model families have
  not been crossed with the permutation family.

Keep the alphabet fixed and declared in advance: EXP-011 shows transposition plus a
*free* keyed alphabet is vacuous (10⁺⁷·⁹ expected chance fits) while transposition
plus a fixed alphabet is comfortably testable (10⁻¹⁸·⁷).

## 3 — Machine-readable physical transcript

Priority: **high**, and EXP-017 raised it: the Playfair and reflector-machine
eliminations are contingent on the crib positions being exactly right, so verifying
them against a primary transcript now has a concrete payoff rather than being tidiness., and it is the only route to genuinely new evidence that does not
depend on someone else releasing it. See `ideas.md` § 7.

Nothing here records the sculpture's line breaks, panel boundaries, tableau
orientation, or the punctuation and misspelling handling that
`data/mask_sources.json` currently guesses at. EXP-004's K1–K3 rows remain
`inconclusive` rather than `negative` solely because of this. Transcribe from the
NSA primary reference in `sources.md`; do not reconstruct from memory.

## 4 — Specify, do not reconstruct, the `TOKIO → 57973` corpus

Priority: medium, unchanged from session 1, and still a specification task.

Its route definitions and hash were never committed. Reconstructing 942 cases from a
count alone is inventing an enumeration, which `resume-prompt.md` explicitly warns
against. Write the specification, state exactly which source evidence is missing, and
stop there until it is found.

## 5 — Bounded `4 × 22` lookup experiments

Priority: medium, and now strongly pre-filtered.

Before writing any search, apply the four free checks in `ideas.md` § 5. In
particular the bounded-source lemma kills any lookup whose output is bounded below
25 for 8 of the 12 conventions, and the block-coverage rule shows how quickly 24 crib
letters collapse to nothing once a cipher has block structure.

## 6 — Do not pursue

Recorded so effort is not re-spent:

- **Position 63 / segmentation.** Demoted. `ideas.md` § 4 gives the ceiling argument.
- **The parity, K0 Morse and Kryptos rail selectors.** Explained as a 1-in-1,024
  selection effect by EXP-009.
- **More route or grid transpositions applied alone.** Killed by the IoC invariant.
- **Any model with a free per-position selector or a free keyed alphabet.** Above the
  evidence budget; a fit would be meaningless.

---

## Required result record

Unchanged, and exemplified by `results/2026-09-12-exp001-005.md` and
`results/2026-09-12b-exp006-014.md`. Hypothesis; input source and hash; code revision;
full parameters; number of variants; crib result; output/hash; conclusion; and the
exact reason it differs from prior work.

Five additions learned across the two sessions:

- **State the null.** "Best 7/24" means nothing without the expected best over the
  number of trials run — and check whether those trials were independent. EXP-014's
  apparent excess is correlation between tableau alignments, not signal.
- **Self-test the apparatus.** A negative from code that cannot produce a positive is
  not a negative. Every experiment here carries a planted positive control.
- **Report whether the search finished.** EXP-013's first run hit a node cap and found
  nothing; that is heuristic failure, not elimination. Re-ordering the search cut it
  60-fold and made the negative real.
- **Count degrees of freedom before searching.** `modlin.chance_solvable` gives the
  exact probability that a model class admits *any* solution for random data. If that
  is near 1, the class is vacuous and the search is theatre.
- **Prefer an invariant to a search.** A search reports "not found". An invariant
  reports "cannot exist", costs nothing, and retires an entire class at once. The most
  productive results in this repository — three alphabets forced, all 26 letters
  present, IoC versus transposition — are all one-line arguments.
