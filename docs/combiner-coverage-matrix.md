# Combiner coverage matrix — EXP-001 … EXP-036

Built to answer a narrow question and stop a broad one being restated: *which surviving
architectures actually depend on the three shift combiners, and which structured non-shift
mappings have genuinely never been tested?*

## The Checkpoint-M overstatement, narrowed

Checkpoint M said the next frontier is the combiner because "all 36 experiments share
Vigenère / Beaufort / variant Beaufort." **That is too broad and is withdrawn.** Checkpoint M
is not rewritten; this file supersedes that sentence.

Machine audit: **22 of 36** experiments call `all_conventions()`. **14 do not**, and several
of those test mappings far outside the shift families — most obviously **EXP-033**, whose
`S : A–Z → A–Z` is *any* fixed function decided by consistency, and **EXP-012/013**, which
are fractionation and Trifid.

**Corrected statement:** the shift-combiner assumption binds the *keystream and periodic
polyalphabetic* line of work — 22 experiments — and does not bind the substitution,
transposition, fractionation or structural results.

## Matrix

`conv?` = calls `all_conventions()`. `STD/KRY?` = the result is conditional on those
component alphabets. Table = how the plaintext→ciphertext mapping is constrained.

| EXP | transformation class | conv? | STD/KRY? | table | escaped by a new combiner? |
|---|---|---|---|---|---|
| 001 | forced keystream at cribs | yes | yes | periodic/arbitrary per position | yes |
| 002 | external-source keystream | yes | yes | source-dependent | yes |
| 003 | transposition + periodic polyalphabetic | yes | yes | periodic | **yes** |
| 004 | running-key substitution | yes | yes | source-dependent | yes |
| 005 | toolchain validation | yes | n/a | n/a | n/a |
| 006 | parameter-linear keystreams, with resets | yes | yes | position-function | yes |
| 007 | structural invariants, no search | no | no | class-level | mostly no |
| 008 | feedback / autokey substitution | yes | yes | source-dependent | yes |
| 009 | alphabet-count bound from cribs | no | no | information-theoretic | no |
| 010 | change-point statistics | no | no | none | no |
| 011 | testability frontier | no | no | none | no |
| 012 | **fractionation, coverage argument** | **no** | **no** | grid/coordinate | **no — not a shift experiment** |
| 013 | **Trifid, exhaustive at decidable periods** | **no** | **no** | coordinate | **no** |
| 014 | carved-tableau running key | yes | yes | source-dependent | yes |
| 015 | relative-phase keystreams | yes | yes | periodic | yes |
| 016 | affine transposition × all keystreams | yes | yes | periodic/linear | yes |
| 017 | crib-alignment robustness | no | no | meta | n/a |
| 018 | bearing routes × keystreams | yes | yes | periodic | yes |
| 019 | unicity / key-entropy bound | no | no | information-theoretic | **no — bound survives any combiner** |
| 020 | carved line geometry × keystreams | yes | yes | periodic | yes |
| 021 | K4/K5 architecture argument | no | no | structural | no |
| 022 | is the forced keystream text-like | yes | yes | source-dependent | yes |
| 023 | Morse material as keystream | yes | yes | source-dependent | yes |
| 024 | Weltzeituhr test (frozen) | yes | yes | source-dependent | yes |
| 025–028 | reconstruction gates, metrics, invariants | no | no | none | n/a |
| 029 | restricted Weltzeituhr running key | yes | yes | source-dependent | yes |
| 030 | fixed lookup on the CET tape, **any** `f` | yes | yes | arbitrary `f` of a source symbol | yes |
| 031 | multi-face arc running key | yes | yes | source-dependent | yes |
| 032 | key = any `f` of engraving column | yes | yes | arbitrary `f` of an index | yes |
| 033 | **any monoalphabetic `S` ∘ transposition** | **no** | **no** | **arbitrary fixed bijection/function** | **no — already covers every fixed table** |
| 034 | text-dependent key, any `f` | yes | yes | arbitrary `f` of a source symbol | yes |
| 035 | panel running key, any `f` | yes | yes | arbitrary `f` of a source symbol | yes |
| 036 | transposition + periodic polyalphabetic | yes | yes | periodic shift | **yes** |

### What the matrix shows

1. **A new combiner cannot rescue a monoalphabetic model.** EXP-033 already decided *every*
   fixed `A–Z → A–Z` table, so any "new" cipher whose table is fixed for the whole message
   is covered there, whatever its historical name.
2. **A new combiner cannot rescue a single-symbol-lookup keystream.** EXP-030/032/034/035
   decide *any* function `f` of one source symbol or index. What they do **not** absorb is
   the plaintext and ciphertext **component alphabets**.
3. **The live gap is periodic/state-varying tables that are not shifts** — exactly the
   EXP-003/EXP-036 line, where the mapping changes with position and is assumed to be one of
   three shift forms.

## Reduction rule applied to candidate "new" ciphers

Before any such family gets an experiment number it must be reduced to an equation and
tested for duplication. Results so far:

| candidate | reduction | verdict |
|---|---|---|
| **Gronsfeld** | Vigenère with the key restricted to digits 0–9 | **duplicate** — EXP-036 decides the key existentially over all of Z26^p, so a digit-restricted key is a strict subset |
| **Quagmire I** | keyed plaintext component, straight cipher component, periodic shift | **duplicate** — the full 26-setting family is *set-equal* to `Convention(P=KRY, C=STD, vigenere)` (verified) |
| **Quagmire II** | straight plaintext, keyed cipher component | **duplicate** — set-equal to `Convention(P=STD, C=KRY, vigenere)` |
| **Quagmire III** | same keyed alphabet both sides | **duplicate** — set-equal to `Convention(P=KRY, C=KRY, vigenere)` |
| **Quagmire IV** | two *different* keyed alphabets | **not covered**, but the second keyword is an unevidenced free parameter; no primary source names one. Unfalsifiable if left free |
| **Bellaso / reciprocal tableaux** | reciprocal table families | reduce case by case; the Porta result below is the worked example |
| **Porta** | 13 reciprocal half-swapping tables | **not a duplicate under the evidenced alphabets** — see below |

The Quagmire "indicator that shifts the alphabet setting" only relabels which key *value* is
used at each position, and EXP-036 decides the key existentially over all of Z26^p, so any
fixed key-letter relabelling is already absorbed. Re-running Quagmire I–III would duplicate
billions of cases.

## Porta — equivalence result, stated exactly

Standard Porta: 13 self-reciprocal tables, key letters in pairs AB, CD, … YZ; row `n` maps
lower-half index `a < 13` to `13 + ((a + n) mod 13)` and is its own inverse. Verified: all 13
rows are reciprocal, and every row has **zero fixed points** — every letter is sent to the
opposite half.

**Result 1 — not representable under the evidenced alphabets.** Enumerating all
3 combiners × 4 evidenced component pairs × 26 key values gives **207 distinct mappings**.
Of Porta's 13 rows, exactly **one** (row 0) appears among them — it is
`variant_beaufort / P=STD / C=STD / k=13`, the plain A↔N swap. **Rows 1–12 are not
representable by any of the 207.** The same holds with Porta built on the KRYPTOS ordering
(row 0 = `variant_beaufort / P=KRY / C=KRY / k=13`).

**Result 2 — but it IS conjugate to shifts under *some* relabelling, and my first proof
attempt was wrong.** I expected the cycle-type invariant to settle this. It does not:
every `Porta_n ∘ Porta_0⁻¹` has cycle type (13, 13), the same as an even shift. Worse for
that argument, `{Porta_n ∘ Porta_0⁻¹}` is *closed under composition* — a Z₁₃ acting
regularly on two orbits of 13 — which is exactly the structure of the even-shift subgroup
`{Shift_0, Shift_2, …, Shift_24}`. The two permutation groups are therefore conjugate, so
bijections φ, ψ **do** exist with `ψ ∘ Porta_n ∘ φ = Shift_{2n'}`.

So the honest statement is not "Porta is a new combiner". It is:

> **Porta is a shift family under a particular pair of mixed alphabets — just not under any
> of the four evidenced STD/KRYPTOS pairs.** Testing it is testing that specific,
> precommitted, historically documented alphabet pair, not a new algebraic class.

This is the frontier restated precisely: admitting *arbitrary* component alphabets collapses
everything and is unfalsifiable; a *named historical* table family is a legitimate finite
precommitment.

## Documentary grade for Porta

**Structural / historical candidate only.** Porta is a real, hand-operable classical
polyalphabetic cipher of the right era and working style. **There is no Sanborn or Scheidt
evidence that K4 uses Porta**, and none is claimed. It ranks below anything with direct
Kryptos documentary support; it is being considered because the evidenced families are
exhausted, not because the record points at it.
