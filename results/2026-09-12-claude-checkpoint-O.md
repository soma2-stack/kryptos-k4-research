# Checkpoint O — named fractionation audit and next exact frontier

> **SUPERSEDED IN PART — see [Checkpoint P](2026-09-12-claude-checkpoint-P.md).** Checkpoint O
> made two statements conditional on the crib positions being unverified: §1C's rejection of
> standard Fractionated Morse, and §7's recommended next action. Both are now resolved —
> the positions are public-source verified, so the Fractionated-Morse rejection is
> unconditional against the *published* positional semantics, and §7's action is **fulfilled**.
> The body below is left exactly as written.

## Repository status

| | |
|---|---|
| branch | `claude/k4-post-j` |
| starting HEAD | `a6d6e48ecac953a4032a6384777bcb8fb5ef25fd` (verified on pull) |
| final HEAD | this checkpoint's commit |
| `main` | **untouched** |
| `codex/k4-continuation` | **untouched** |
| `claude/dreamy-archimedes-79k6u0` | **untouched** |
| working tree at start | clean |
| new experiments run | **none** — see §3 |

**K4 remains unsolved.** No plaintext candidate, no complete mechanism, no external
submission. Every Checkpoint-N conclusion is preserved unchanged; nothing was rerun for
reassurance.

This session was operated in conservative mode: symbolic reasoning and tiny scripts only,
no multi-billion-case search, and the budget reserved for a complete handoff.

---

## 1. Fractionation audit

Full working in `docs/fractionation-frontier-audit.md`. Every figure was recomputed here
from letter data rather than copied from the brief.

### A. Conjugated Matrix Bifid — reduced, not run

Standard CM Bifid uses **two 5×5 squares over a 25-letter alphabet** with one letter merged,
so its emitted inventory is 25 symbols. K4 contains **`J` at three positions**. That is
EXP-012's coverage argument applied unchanged.

> **REDUCED TO EXP-012.** No Bifid search. A 6×6 variant was **not** silently substituted —
> it carries 10 extra non-letter cells, is a different model, and EXP-012 already grades it
> strongly disfavoured on the same grounds.

### B. Digrafid — closed by the primality of 97

I do **not** have an authoritative offline definition of Digrafid's exact block ratio and did
not assert one from memory. It turns out not to matter:

> A block system consuming `b > 1` and emitting `c > 1` symbols per block produces a
> ciphertext of length `c · m`. **97 is prime**, so `c · m = 97` forces `c = 1` or `c = 97`.
> No ratio in `2 … 96` can emit exactly 97 symbols.

> **STRUCTURALLY INCOMPATIBLE with a 97-character ciphertext for any block ratio c > 1.**
> No padding or truncation convention was invented. The 27th filler symbol is *not* the
> rejection — length is the stronger argument. If a documented standard convention for an
> incomplete final block exists, this should be revisited against that citation.

### C. Fractionated Morse — the one that deserved real work

Given priority because Kryptos physically carries Morse material and **EXP-023 tested that
material only as a running-key letter tape**, explicitly leaving structural dot/dash/separator
use open. A real gap, not a catalogue entry.

`n` ciphertext letters cover exactly `3n` ternary symbols; a `k`-letter plaintext segment
needs at minimum `marks + (k − 1)` symbols:

| segment | letters | marks | min. seps | min. stream | 3n supply | verdict |
|---|---:|---:|---:|---:|---:|---|
| `BERLIN` | 6 | 16 | 5 | **21** | 18 | impossible, short by 3 |
| `CLOCK` | 5 | 18 | 4 | **22** | 15 | impossible, short by 7 |
| `BERLINCLOCK` | 11 | 34 | 10 | **44** | 33 | impossible, short by 11 |
| `NORTHEAST` | 9 | 20 | 8 | **28** | 27 | impossible, short by 1 |
| `EAST` | 4 | 7 | 3 | 10 | 12 | fits |
| `EASTNORTHEAST` | 13 | 27 | 12 | **39** | **39** | **fits exactly** |

**Global argument, independent of crib positions:** 97 ciphertext letters = 291 ternary
symbols, so for an `n`-letter plaintext `Σ marks = 292 − n`. At `n = 97` that demands a mean
of **2.01** Morse marks per letter against an unweighted alphabet mean of **3.15**. Standard
Fractionated Morse is neither length- nor position-preserving.

**Semantic check, stated honestly rather than forced.** The repository's crib model is
`P[i] ↔ C[i]`, and `data/k4.json` itself records the crib positions as inherited-canonical,
not primary-verified; I cannot check the primary wording offline. So:

- **If** the clues mean cipher positions 63–73 decrypt to `BERLINCLOCK` at plaintext
  positions 63–73, standard Fractionated Morse is **structurally rejected**, and no keyed
  alphabet repairs it — a keyword permutes which triple maps to which letter and changes no
  length.
- **If** they do not establish local position preservation, a Fractionated-Morse reading must
  restate all 24 crib constraints in *stream offsets*: define how ciphertext position 63
  indexes into a variable-length ternary stream, what "plaintext position 63" means when
  letters occupy 1–4 symbols plus separators, and how the disclosed segments are recovered.
  That is a different programme. **No crib was slid to a new position.**

> **STANDARD Fractionated Morse: structurally rejected under the repository's
> position-preserving crib model. No keyword search was run** — not `KRYPTOS`, `PALIMPSEST`,
> `ABSCISSA`, `BERLINCLOCK`, nor dictionary keys, because an alphabet key cannot repair a
> length contradiction.

`EASTNORTHEAST` fitting *exactly* at 39 = 13 × 3 is a genuine coincidence. **Recorded and not
pursued**: it needs zero word separators and zero end padding, and `BERLINCLOCK` in the same
message fails by 11, so no one message satisfies both.

### Relation to existing experiments

- **EXP-012** — CM Bifid reduces to it exactly; unchanged and not rerun.
- **EXP-013** — Trifid remains eliminated only at its decidable periods (2 and 3); periods ≥ 4
  stay undecidable for lack of crib coverage. Nothing here changes that.
- **EXP-023** — its open "Morse as structure" gap is now closed **only for standard
  Fractionated Morse**. EXP-023's own tape result remains a HEURISTIC NEGATIVE resting on
  community transcriptions; nothing here upgrades it.

### What fractionation remains genuinely open

> **The obvious named classical fractionation candidates are substantially exhausted under
> the public evidence.**

This is **not** "K4 is not fractionated." A custom fractionator that emits all 26 letters,
preserves length and preserves position could still exist — but it is then a **speculative
architecture with no name, no documentary support and free parameters**, and it does not
automatically inherit budget. Before a number is assigned it must be written as equations,
checked for duplication against EXP-012/013/033, and have its crib constraint density and
null derived from the construction itself.

---

## 2. Gromark audit

**Exact standard definition used:** Gronsfeld with a mixed alphabet and a running key — a
five-digit primer expanded by chained addition `d[i+5] = (d[i] + d[i+1]) mod 10`, the
resulting digits driving the substitution. Key values are therefore **restricted to 0–9**.

**Coverage question, settled before any search.** Gromark's state evolves from *previous key
digits*, which is outside EXP-036 (arbitrary but **periodic** keys, periods 2–23 — a chained
recurrence is not short-periodic), outside EXP-006 (position-functions: periodic,
progressive, polynomial, reset/offset), and outside EXP-008/EXP-034 (keys derived from
*plaintext or ciphertext* source symbols, not from prior key state). **Gromark is genuinely
outside existing coverage** — which is why it got the gate rather than a dismissal.

**The gate made it moot.** Every crib pair must need a shift inside `{0…9}`:

| plain / cipher | shifts 0–9 | shifts 1–10 |
|---|---:|---:|
| STD / STD | **15 of 24 rejected** | 14 rejected |
| STD / KRY | 15 rejected | 16 rejected |
| KRY / STD | 14 rejected | 15 rejected |
| KRY / KRY | **11 rejected** (best case) | 12 rejected |

Example rejections under STD/STD: position 22 `A→L` needs 11; position 23 `S→R` needs 25;
position 27 `R→P` needs 24.

> **The direct position-preserving Gromark family is structurally impossible under every
> evidenced component-alphabet pair. The 100,000-primer search was NOT run.**

**EXP-038 was not assigned** — correctly, since the gate rejects before the primer space is
reached.

**What I deliberately did not do.** I did not derive an ACA columnar-transposition Gromark
alphabet from `KRYPTOS`. First, I have no authoritative offline source for that exact
construction and will not invent a "standard" from memory. Second, it would not be evidence:
a random mixed alphabet passes the 24-crib digit gate with probability
`(10/26)²⁴ ≈ 1.1 × 10⁻¹⁰`, which across 26! alphabets still leaves on the order of **10¹⁶
alphabets passing by chance**. Hunting for an alphabet that admits the cribs is **fitting,
not testing**, and no primary source names a Gromark alphabet for Kryptos at all.

Not attempted and reserved for a future session only with independent motivation:
transposition-composed Gromark, reversed recurrence, alternate modulus, primer offset,
resets, longer secret state, additional keywords.

---

## 3. EXP-038 — not run, by design

No experiment number was assigned this session. Both candidate families were closed by exact
structural observations costing seconds, which is the stated preference order: structural
reasoning before search. Spending the remaining budget on a 100,000-primer sweep of a family
already rejected at 11–16 of 24 crib positions would have been activity, not information.

---

## 4. Current architecture ranking

| rank | architecture | grade | falsifiable now? |
|---|---|---|---|
| 1 | **Unidentified high-entropy or aperiodic key** — a long key from a source not yet named | **DOCUMENTARY-MOTIVATED** (K1/K2 precedent; Scheidt's "different, better-masking" fourth process; K4's flat IoC demands flattening) | **No** — moves only on evidence naming a source, not on search |
| 2 | **Stateful / recursive key systems** whose state evolves from prior key values | **STRUCTURALLY-MOTIVATED** — the Gromark audit showed this class sits outside EXP-006/008/034/036; only the *digit-restricted* instance died | Yes, if a specific recurrence with an evidenced alphabet is named |
| 3 | **Narrowly motivated double transposition**, or keyed columnar width ≥ 12 from a precommitted key family | **STRUCTURALLY-MOTIVATED** (K3 is a transposition Sanborn built himself) | Yes, as a small precommitted family |
| 4 | **Custom full-26 fractionation** | **SPECULATIVE-BUT-OPEN** — named classics now exhausted | Only after the construction is written as equations |
| 5 | **Clock as state/index** rather than letter source | **SPECULATIVE-BUT-OPEN** | No — still no stated mechanism |
| 6 | **Semantic / inner encoding** under a simpler outer cipher | **SPECULATIVE-BUT-OPEN** | No — untestable without the codebook |
| 7 | **Physical mechanisms** needing fabrication evidence | parked | Blocked on Request 4 |

Logical possibility is not evidence, and ranks 4–7 are labelled accordingly.

---

## 5. Model coverage summary

**Strongly narrowed (each at its exact declared scope, not beyond):**

- ordinary short-period shift polyalphabetic — EXP-006, EXP-036
- declared transposition + periodic shift substitution — EXP-036 (4.31 × 10⁹ cases)
- fixed monoalphabetic substitution + declared transposition — EXP-033 (1.76 × 10⁸ cases,
  every fixed `A–Z → A–Z` map)
- direct World Clock letter tapes — EXP-024/029/030/031
- single-symbol source-lookup key families — EXP-030/032/034/035
- standard Porta, direct and transposition-composed — EXP-037
- standard Trifid at its decidable periods — EXP-013
- sub-26-symbol output alphabets — EXP-012
- **named classical fractionators audited here** — CM Bifid, Digrafid, Fractionated Morse
- **standard direct Gromark** — audited here

**Still open:**

- unidentified high-entropy or aperiodic key
- stateful recursive key systems not previously covered
- narrowly motivated double transposition
- custom fractionation
- clock as state/index rather than letter source
- semantic / inner encoding
- physical mechanisms requiring unavailable fabrication evidence

---

## 6. External evidence

**Request 4 remains OPEN and was not pursued** (external access is blocked; spending budget
on it was explicitly ruled out):

> Jim Sanborn papers, Archives of American Art, **Series 3, Box 6, Folder 10 —
> `Pre-Production and Notes, 1990–1999`**. Wanted: cipher-panel line geometry, fabrication
> layout, character spacing, row alignment, punch/type template, and pre-production
> cryptographic notes **provided they are non-solution-contaminating**.

Requests 1 and 5 fulfilled; 2 and 3 carried forward at lower priority. Nothing is blocked on
any of them.

A second, cheaper evidence item is now worth naming: **the primary wording of the public
`BERLIN`/`CLOCK` clues**, sufficient to establish whether they assert *local positional*
correspondence. `data/k4.json` flags the crib positions as inherited-canonical rather than
primary-verified, and §1C shows that this one question decides whether a whole class of
non-position-preserving ciphers is rejected or merely unformulated.

---

## 7. ONE next action

> **Verify the primary wording of the public K4 clues, and pin the 24 crib constraints to a
> cited primary source.**

- **Not duplicate work.** Every one of EXP-001…037 consumes the crib positions as given.
  They have never been checked against a primary transcript; the repository's own data file
  asks for exactly this and has been asking since the beginning.
- **Falsifiable.** The clue wording either does or does not assert that ciphertext positions
  63–73 decrypt to `BERLINCLOCK` at plaintext positions 63–73. Both answers are decisive.
- **Evidence supporting it.** Sanborn's clue releases are public and quotable; this is a
  documentary lookup, not a search.
- **What would eliminate it / what turns on the answer.** If local positional correspondence
  is confirmed, the position-preserving crib model is vindicated and §1C's rejection of
  standard Fractionated Morse becomes final — and, more valuable, every future
  non-position-preserving candidate can be rejected by the same one-line argument. If it is
  *not* confirmed, then a whole class of length- or position-changing ciphers reopens, the
  24 constraints must be reformulated in stream offsets, and several scoped negatives narrow
  in a way this repository would need to state explicitly.

It is the cheapest item on the board and it sits underneath every result in the repository —
which is precisely why it outranks starting another cipher family.
