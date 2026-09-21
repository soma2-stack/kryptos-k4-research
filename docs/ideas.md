> **HISTORICAL PLANNING FILE — 2026-09-21 NOTICE.** Many "not yet tested" and "still not started" statements below predate later checkpoints and EXP-040–043. Use `docs/current-status.md` and `autonomous/KNOWN_STATE.md` for current coverage; use this file only to understand how ideas evolved.

# Attack ideas

Rewritten 2026-09-12 after the second research session. Status keys follow
`CONTRIBUTING.md`: `negative`, `inconclusive`, `replicated`, `candidate`.

Two sessions of work have moved this repository from "many untested ideas" to a
much narrower position. The honest summary is below, then the ideas worth pursuing.

---

## Where the hypothesis space now stands

**Eliminated exhaustively or by proof** — see `docs/negative-results.md` for scopes:

monoalphabetic · pure transposition of any complexity · Playfair · reflector rotor
machines · Hill blocks 2–3 · all parameter-linear position keystreams (periodic,
progressive, polynomial) with resets at any boundary · all single- and two-tap
autokey, feedback and self-referential keystreams · affine-mod-97 transposition
with any period ≤ 12 key · two-chart models · periods {1–7, 9, 10, 14, 15, 17} for
*any* periodic polyalphabetic cipher whatsoever · Quagmire I · every cipher with an
output alphabet below 26 symbols (bifid, four-square, two-square, ADFGVX, …) ·
trifid at both decidable periods · running keys from K4 itself, the Kryptos
alphabet and the carved tableau.

**Ruled undecidable rather than negative** — these cannot be refuted by 24 crib
letters, so searching them produces fits and never evidence:

Quagmire III and any two-keyed-alphabet scheme · homophonic models with a free
selector · transposition combined with a free keyed alphabet · trifid at period ≥ 4.

**That leaves a narrow surviving space**, and the ideas below are ordered by what
can actually be done about it.

---

## 1 — Acquire constraint, not more search

**Status: the single most actionable item in this repository.**

24 crib letters supply 24 × log₂26 = **112.8 bits**. EXP-011 computes, for each
model class, the number of known plaintext letters that would make it decidable:

| Class | Letters needed | More than we have |
| --- | --- | --- |
| Vigenère family, fixed alphabet, period 26 | 27 | 3 |
| Quagmire I + period 8 | 28 | 4 |
| Quagmire I + period 12 | 32 | 8 |
| Affine transposition + Quagmire I period 8 | 31 | 7 |
| Quagmire III + period 8 | 47 | 23 |
| Homophonic, 2 charts + free selector | 59 | 35 |

**Between 3 and 35 more known plaintext letters would re-open every family this
repository currently cannot falsify.** One further released clue of the size of
NORTHEAST (9 letters) would make Quagmire I fully decidable. That is a better
return than any conceivable search, and it reframes what "progress" means here.

Concretely: if a candidate 97-character plaintext ever becomes available — from
the 2025 archive, from a leak, or from an independent solve — stop searching and
run `k4lib.recover.diagnose` on it. See idea 2.

## 2 — Method recovery from a candidate plaintext

**Status: implemented, `k4lib/recover.py`, validated by EXP-005.**

Reporting around the archive sale distinguishes the recovered *text* from the
*decryption method*. With all 97 plaintext letters the keystream is forced
everywhere, and a period, an affine rule, a linear recurrence or a running key
(keystream IoC near 0.066) is read straight off. A *near*-correct plaintext still
shows partial structure, so this is worth running on imperfect candidates too.

Do not invert it into evidence: a candidate showing no structure is not refuted,
and one showing structure is not confirmed until the rule extends to all 97
positions.

## 3 — Transposition with a pre-fixed alphabet and an aperiodic key

**Status: the largest surviving testable family. Not yet tested.**

EXP-011 shows that transposition *plus a free keyed alphabet* is vacuous, but
transposition plus a **fixed** alphabet is comfortably testable (10¹⁵·³ against a
10³⁴ budget). EXP-003 tested the complete affine-mod-97 family against periodic
keys only. What remains is that same complete permutation family against the
keystream classes that have since been built: progressive, polynomial, feedback,
relative-phase.

The cost is the product of two sweeps already written, so this is engineering
rather than invention. Do it with the alphabet fixed in advance and declare it
before running.

## 4 — The `+5` run: state the ceiling and stop

**Status: `inconclusive`, p ≈ 0.017, and provably unresolvable by crib algebra.**

Across 1,248 (alphabet, lag, delta) combinations the `DIAWINFBN` run is the only
run of length ≥ 4 in the ciphertext; family-wise expectation is 0.017. Real but
modest, about 2σ.

Its termination at position 63 — the first letter of `BERLINCLOCK` — was the lead
that opened this session. **EXP-010 removed its independent support**: across four
change-point statistics, two alphabets and a permutation null on the maximum over
68 boundaries, no boundary is significant, and position 63 ranks 65th, 47th, 31st
and 39th of 68. It is not special.

Worse, the run is *provably* beyond crib algebra. `C[i+4] − C[i] = 5` expands to
`(P[i+4] − P[i]) + (k[i+4] − k[i]) = 5`, and positions 55–62 lie outside both
cribs, so both readings — progressive key over flat plaintext, flat key over
patterned plaintext — fit equally and cannot be separated. Its only crib contact,
`C[63] = C[59] + 5`, is one equation in two unknowns.

**Recommendation: demote.** Do not build further experiments on position 63. The
run can only be explained by a mechanism proposed on independent grounds that
happens to predict it.

## 5 — Reusable tools this work produced

Four checks that cost nothing and should be run before any new proposal:

- **Bounded-source lemma** (EXP-001). The cribs force a key index of 24 or 25 under
  8 of the 12 conventions, so any key source bounded below 25 — a 24-hour clock, a
  23-lamp display, a 24-sector ring — is dead for those eight with no search.
- **Alphabet-free period elimination** (EXP-011). If a crib conflict pair is
  congruent mod p, period p is impossible for *every* alphabet at once. This
  retires p ∈ {1–7, 9, 10, 14, 15, 17} for all periodic polyalphabetic ciphers.
  **The shortest period K4 could possibly have is 8.**
- **Output-alphabet coverage** (EXP-012). All 26 letters occur in K4, so any cipher
  with a smaller output alphabet is impossible. One line, whole family gone.
- **Block-coverage rule** (EXP-012). Crib evidence does not survive block
  boundaries: a block cipher keeps only blocks lying wholly inside a crib, so 24
  letters can fall to 9 or 0 usable constraints. Count covered positions *before*
  searching any block-structured cipher.

## 6 — Audit before searching: the selector lesson

**Status: `replicated`, and it demotes three inherited leads.**

EXP-009 reduced the two-chart question to graph colouring. Plaintext `E` occurs at
positions 21, 30 and 64 and enciphers to `F`, `G` and `Y`; plaintext `T` at 24, 28
and 33 to `V`, `R` and `S`. **At least three encryption alphabets are forced**, so
every two-chart model is impossible in that direction.

In the decryption direction two charts do suffice — but exactly **16,384 of
16,777,216** selectors separate all ten conflicts, so an arbitrary bit-stream does
so with probability **1 in 1,024**. The inherited opposite-tableau-parity, K0 Morse
and Kryptos-rail observations are each worth about ten bits, and the handoff
records that multiple Morse phases were searched. A selector family with ~1,000
members is *expected* to contain a winner.

**All three leads are explained as a selection effect.** The general rule: before
reporting that a model "has no contradictions", count how many models would not.

## 7 — Machine-readable physical transcript

**Status: still not started; prerequisite for any physical-geometry work.**

Nothing here records the sculpture's line breaks, panel boundaries, tableau
orientation, or the punctuation and misspelling handling that
`data/mask_sources.json` is currently guessing at. Transcribe it from the NSA
primary reference in `sources.md`. **Do not reconstruct it from memory** — EXP-004's
K1–K3 rows are marked `inconclusive` rather than `negative` precisely because they
rest on unverified transcriptions.

## 8 — Ideas deliberately not pursued, and why

Recorded so they are not re-invented:

- **Bespoke non-classical constructions.** Always available, never falsifiable
  without more plaintext. They belong after idea 1, not before it.
- **Anything with a free per-position selector or a free keyed alphabet.** EXP-011
  shows these are above the evidence budget. A fit would be meaningless.
- **More route and grid transpositions applied alone.** Killed outright by the IoC
  argument in EXP-007, without enumeration.
- **`EASTNORTHEAST` / `BERLINCLOCK` as operational instructions.** Attractive —
  compass directions do read like a route, and Sanborn has said the plaintext needs
  field work — but it is a claim about what the message *says*, not about the
  cipher, and no version of it is testable with the plaintext we have.

## 9 — What would actually settle this

1. More known plaintext. Idea 1 quantifies exactly how much, and it is not much.
2. A mechanism proposed on external grounds — a primary-source fact about
   construction — narrow enough for 24 letters to confirm. Idea 7 is the route.
3. A candidate plaintext run through idea 2.

Enumerating more cipher families is none of these. The families that remain are
either eliminated or, more often, unfalsifiable with the evidence in hand — and
telling those two apart is most of what this repository now offers.
