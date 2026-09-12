# Result record — 2026-09-12 (session 3) — Checkpoint C

Branch `claude/dreamy-archimedes-79k6u0`. Ciphertext SHA-256
`eea813570c7f1fd3b34674e47b5c3da8948026f5cefee612a0b38ffaa515ceab`.
Regenerate with `./run_all.sh`. Python 3.11, standard library only.

This session began with an audit of Checkpoint B, incorporated Sanborn's confirmed
November 2025 clues, and tested the physical/World-Clock direction they point at.

---

## 0 — Audit of Checkpoint B (`docs/evidence-grades.md`)

Several Checkpoint B claims were stated more universally than their arguments
support. Full regrade against a five-level scale is in `docs/evidence-grades.md`.
The corrections that matter:

**The scoping error.** The three-alphabet bound, the alphabet-free period
elimination and the conflict census all assume the cipher is **monographic and
position-preserving** — that P[i] is enciphered to C[i] one letter at a time.
Outside that class they say nothing: under a transposition the "conflicting"
letters were never enciphered together, and under fractionation a ciphertext
letter is not a function of one plaintext letter at all. I previously wrote "at
least three encryption alphabets are forced" without the qualifier. It is now
attached everywhere.

**"All 26 letters occur" was too broad.** Split by grade:
- PROVED IMPOSSIBLE: any cipher whose *final output alphabet* has < 26 symbols.
- STRONGLY DISFAVORED, not proved: 6×6 (36-cell) fractionation — all 97 outputs
  would have to miss the 10 non-letter cells, P ≈ 2.0 × 10⁻¹⁴.
- STRONGLY DISFAVORED: 2×13 rectangular Polybius, P(all outputs valid) ≈ 10⁻⁷⁹.
- **NOT ELIMINATED, wrongly closed before:** a 25-symbol system followed by a
  *second encoding layer* that re-expands to 26 letters. The coverage argument
  only ever sees the final layer. This is a genuine residual opening.

**The IoC argument is statistical, not logical** — correctly conditional on the
plaintext being English. The audit makes it *stronger* than I credited: since a
transposition preserves IoC exactly, a pure transposition needs a plaintext with
IoC ≈ 0.036, which is **flatter than uniform random (0.0385)** — anti-clustered,
not merely non-English. Grade: STRONGLY DISFAVORED, with an extreme alternative.

**The 112.8-bit frontier is a heuristic, not a proof.** Parameter entropy alone
does not establish unfalsifiability; the counting argument assumes the model
behaves *generically*. The correct statement:

> The penalty applies to **free** parameters, not to dimensionality.

This licenses the whole direction of this session. A mechanism **determined by a
physical object** — a clock face, a compass rose, a tableau, a projection — may
have thousands of entries, but none of them is fitted. Such a model has close to
zero free parameters and is therefore *maximally* testable, however large it looks.

**EXP-002 tested the wrong object.** Sanborn confirmed in November 2025 that
`BERLINCLOCK` means the **Weltzeituhr**, not the Mengenlehreuhr. EXP-002 remains a
valid elimination of the Set-Theory-Clock lamp count and is *not* the principal
`BERLINCLOCK` test. That test had not been run.

---

## 1 — External evidence gathered (verified, not assumed)

Checked against reporting rather than taken on trust. Recorded with confidence
levels in `data/physical.json`.

| Fact | Confidence |
| --- | --- |
| `BERLINCLOCK` = Weltzeituhr, Alexanderplatz (announced 12 Nov 2025) | HIGH |
| Weltzeituhr: 24-sided rotating cylinder, one face per time zone, Erich John, opened 30 Sep 1969 | HIGH |
| It stands on a **compass-rose mosaic**; Kryptos's courtyard also has a compass rose | HIGH |
| Original 1969 configuration carried **80** city names; ~148 today | MEDIUM (single-source) |
| Cities grouped in **four** longitudinal bands | LOW–MEDIUM — whether these are physical rows is *not* established |
| K4's physical layout is 7 rows × 14 columns, 98 cells, one blank | MEDIUM — traces mainly to a site whose solution claim Sanborn disputes; corroborated only indirectly by the inherited handoff's mention of "7×14 geometry". **Needs primary verification.** |
| Per-segment city list as it stood in 1988–89 | **UNKNOWN** — not available; the clock was restored in 1997 and 2015 with names updated. Modern lists must not be substituted. |

**Status of the plaintext and of K5** — decisive for what follows:
- The K4 **plaintext was found** in September 2025 by Jarett Kobek and Richard
  Byrne, as taped-together scraps in Sanborn's Smithsonian donation. They declined
  to publish it; the Smithsonian sealed the material for 50 years.
- Sanborn: *"They did not solve K4 and they certainly did not find the key."*
  **The method is unknown to everyone, including the people holding the plaintext.**
- **K5** exists, is 97 characters, uses a "similar but not identical" system, and
  shares coded words with K4 **in the same positions** — but its ciphertext is
  released only *once K4 is solved*. A deliberate circular lock.

---

## 2 — EXP-018: compass-bearing routes · EXHAUSTIVELY ELIMINATED WITHIN MODEL

**Hypothesis, pre-registered.** Both confirmed cribs name the same kind of object.
`EASTNORTHEAST` is a compass bearing; `BERLINCLOCK` is an object standing on a
compass rose, and Kryptos has a compass rose of its own. If the cribs are
operational rather than decorative, the operation they jointly name is *read a grid
of letters along a bearing* — "delivering a message" in its most literal
cryptographic form, and executable by hand with a straightedge on copper.

**Not a repeat of EXP-003/016.** Those swept row/column/boustrophedon routes. A
bearing route is a lattice step taken repeatedly on a torus; ENE is two columns
east for one row north, which no row-or-column route produces.

**Scope.** Grids pre-registered from the evidence, not swept: 14×7 and 7×14 (the
reported physical layout), 24×5 and 4×25 (Weltzeituhr width), 22×5 (inherited
world-clock tape), 26×4 (alphabet control). All 16 compass points as integer
lattice steps, every start cell, both composition orders, 12 fixed conventions,
25 keystream models (periodic 8–16, progressive L ≤ 12, polynomial degree ≤ 5).

**20,160 permutations, 6,048,000 gate evaluations. Zero fits.** Planted
`progressive(L=5, δ=7)` under the ENE route on 14×7 recovered by the same code
path. False-fit expectation 2.9 × 10⁻⁵.

**Structural observation recorded rather than papered over:** the Weltzeituhr's
natural grid is 24 segments × 4 city bands = **96 cells, and K4 is 97 characters —
exactly one too many.** Grids too small to hold 97 had their height raised, keeping
the clue-motivated width.

---

## 3 — The two clues do connect, but geographically, not cryptographically

`EASTNORTHEAST` is bearing 67.5°. The great-circle initial bearing from Berlin
(Alexanderplatz) to **Moscow is 67.48°** — the exact centre of the ENE compass
point. Berlin → Moscow, East, a message crossing the Wall: it fits Sanborn's
"delivering a message", the 1989 Alexanderplatz demonstrations, and K2's precedent
of ending in real coordinates.

**Deflated honestly, and it does not survive as a mechanism:**
- the bearing moves over 65.9°–69.0° under ±0.2° jitter in either city's
  coordinates, so the 0.02° agreement is illusory precision;
- a compass point names a **22.5° sector**, not a line, and that sector also
  contains Vilnius, Kazan, Nizhny Novgorod, Minsk and Novosibirsk — six of forty
  cities tested against an expected 2.5, so ENE-of-Berlin does **not** single out
  Moscow;
- the city list was mine and the bearing was chosen after seeing the clue.

**Grade: suggestive interpretation of what the plaintext *means*, with no
cryptanalytic content.** It supports reading the cribs as message content —
navigational instructions — rather than as cipher instructions.

---

## 4 — EXP-019: unicity, and why the pattern of failure has one explanation

The most consequential result of the session, and it is arithmetic, not search.

A ciphertext can only determine a key whose entropy is below the redundancy it
carries. With n = 97 and English redundancy D ≈ 3.2–3.7 bits/letter, K4 carries
about **310–359 bits**, so it can uniquely determine a key of at most **66–76
letters**.

**The nuance that matters** — what counts is key *entropy*, not key *length*:

| Key | Entropy | Verdict |
| --- | --- | --- |
| Random 97-letter key (true one-time pad) | 456 bits | **AMBIGUOUS — unbreakable from ciphertext alone** |
| 97-letter running key from English text | 116 bits | in principle recoverable |
| Keystream read off a physical object | ~30 bits | in principle recoverable |
| Keyword of length 12 / 22 | 56 / 103 bits | in principle recoverable |

So the correct conclusion is narrower than "long keys are hopeless":

- a long **random** key makes K4 information-theoretically ambiguous, and *no*
  method recovers it — not cleverness, not compute;
- a long **structured** key — a running key from natural text, or a keystream read
  off a physical object — has low entropy and **is** recoverable in principle, but
  only once the right source is guessed.

**This explains the entire pattern of three sessions' results.** Short and
structured keys have been eliminated at scale; what remains are candidates that
differ from one another only in *which external source supplied the key*. The 24
crib letters constrain the mechanism — which is why they kill structured models so
efficiently — but they place essentially no constraint on a long key: under an
aperiodic key the other 73 positions admit ~10²⁶ plausible English completions.

**Depth, validated by simulation.** If two messages share a keystream the key
cancels exactly: `C1[i] − C2[i] = P1[i] − P2[i]`. In simulation against a *true
one-time pad*: the identity holds at all 97 positions; positions where the
ciphertexts agree are exactly the positions where the plaintexts agree, so shared
words at shared positions are **directly visible with no cryptanalysis**; and
crib-dragging a known 24-letter span of one message recovered the corresponding 24
letters of the other exactly, using no key knowledge at all.

That is precisely the relationship Sanborn has described between K4 and K5.

---

## Checkpoint C — what was achieved

- **(B) A major World-Clock/sculpture hypothesis exhaustively eliminated within a
  specified model**: compass-bearing routes over the physical and Weltzeituhr
  grids, 6.05M gate evaluations, planted control, zero fits.
- **(C) A new independently supported structural constraint**: the unicity bound.
  K4 can determine at most a ~66–76 letter key; a random 97-letter key is provably
  ambiguous; structured long keys remain recoverable only given their source.
- **(D) Two clues connected through one idea**: `EASTNORTHEAST` and `BERLINCLOCK`
  both name a compass rose. Tested as a cipher mechanism and eliminated; retained
  as an interpretation of the plaintext's meaning, honestly deflated.
- **(E) The dominant bottleneck is now identified precisely and quantitatively.**
  Not "we need more ideas". The surviving hypotheses differ only in which external
  source supplied a low-entropy long key, and the cribs cannot distinguish them.
  Ranked by information per unit effort:
  1. **K5's ciphertext** — 97 characters in depth would very likely break both,
     even against a one-time pad. Withheld until K4 is solved.
  2. **The K4 plaintext** — exists, found, sealed 50 years. `recover.diagnose`
     reads the method off it directly (EXP-005 validates the harness).
  3. **More crib letters** — EXP-011: 3 to 35 more re-open every family now beyond
     reach.
  4. **The 1989 Weltzeituhr city configuration** and **primary verification of the
     7×14 layout** — the two concrete physical-data gaps blocking the object-based
     branch.
  5. *Further searching of short-key models* — bounded above by the unicity result.

**K4 remains unsolved. No candidate mechanism is claimed.**
