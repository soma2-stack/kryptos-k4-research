# Research state

## Provenance and confidence

This is an editorial reconstruction of the referenced ChatGPT conversation, not a laboratory notebook or an independent replication. Each statement is marked by its status:

- **Public fact** — supported by a link in `sources.md`.
- **Inherited result** — reported by the prior researcher; preserve it, but independently reproduce it before relying on it.
- **Hypothesis** — a bounded, falsifiable idea, not evidence of a solution.

## Independently verified facts (2026-09-12)

These are the only statements in this document backed by code in this repository.
Regenerate with `./run_all.sh`.

- `data/k4.json` is internally consistent: 97 characters, both crib spans match their
  recorded ciphertext segments, the Kryptos alphabet is a permutation of A-Z.
  Ciphertext SHA-256 `eea813570c7f1fd3b34674e47b5c3da8948026f5cefee612a0b38ffaa515ceab`.
- **The "ten conflicts" claim replicates, and its definition is now pinned.** Nine
  ciphertext letters appear at crib positions against differing plaintext letters,
  forming exactly **10** conflicting position-pairs (and 12 pairs in the reverse
  direction). No monoalphabetic layer can exist. See EXP-001.
- K4's index of coincidence is **0.03608** (random ~0.0385, English ~0.0667).
- **New.** The `DIAWINFBN` `+5` run at lag 4 occupies positions 55-63 and terminates
  **exactly on position 63, the first letter of the BERLINCLOCK crib**. The full set of
  lag-4 `+5` positions is {22, 29, 55, 56, 57, 58, 59}. It is the ONLY run of length
  >= 4 across 1,248 (alphabet, lag, delta) combinations, family-wise p ~ 0.017.
  **Session 2 demoted this lead**: EXP-010 found no independent statistical support for
  a boundary at 63, and the run is provably unresolvable by crib algebra. See
  `ideas.md` § 4.
- The tooling is self-validating: EXP-005 plants four known constructions and recovers
  all four, so the negatives recorded here are not artefacts of broken code.

### Added 2026-09-12 (session 2)

- **At least THREE encryption alphabets are forced.** Plaintext `E` occurs at positions
  21, 30, 64 and enciphers to `F`, `G`, `Y`; plaintext `T` at 24, 28, 33 to `V`, `R`, `S`.
  Every two-chart model is impossible in the encryption direction. EXP-009.
- **The shortest period K4 could possibly have is 8.** Periods {1-7, 9, 10, 14, 15, 17}
  are impossible for *any* periodic polyalphabetic cipher, whatever its alphabets,
  because a crib conflict pair is congruent mod p. EXP-011.
- **All 26 letters occur in K4** (J at positions 40, 51, 81), so no cipher with a
  smaller output alphabet can have produced it. EXP-012.
- **K4 cannot be an anagram of English**: IoC 0.03608 against 0.06558 +- 0.00763 for
  97 letters of English unigram text, z = -3.87. Pure transposition is dead. EXP-007.
- **24 crib letters = 112.8 bits.** Model classes with more parameter entropy than that
  cannot be refuted at all; several inherited leads sit above the line. EXP-011.
- **Robustness to a crib off-by-one (EXP-017).** Sliding each crib independently by
  -3..+3 (49 alignments): the three-alphabet lower bound holds at *every* alignment,
  as does the impossibility of periods {1-7, 9}. The IoC and output-alphabet arguments
  use no crib positions at all. But the **Playfair and reflector-machine eliminations
  are contingent on the exact alignment** and would need rechecking if the crib
  positions moved. Verify `data/k4.json` against a primary transcript.

### Added 2026-09-12 (session 3) — external evidence and the unicity bound

- **`BERLINCLOCK` is the Weltzeituhr**, Alexanderplatz, not the Mengenlehreuhr
  (Sanborn, 12 November 2025). EXP-002 therefore tested the wrong clock; EXP-018 is
  the principal `BERLINCLOCK` test and is negative.
- **The K4 plaintext exists and is not public.** Found September 2025 in Sanborn's
  Smithsonian donation; the finders declined to publish and the material is sealed
  for 50 years. Sanborn: "They did not solve K4 and they certainly did not find the
  key." The *method* is unknown to everyone, including the plaintext's finders.
- **K5 exists**: 97 characters, "similar but not identical" system, shares coded
  words with K4 **in the same positions** — released only once K4 is solved.
- **Unicity bound (EXP-019).** K4's 97 characters carry ~310–359 bits of redundancy
  and can therefore determine a key of at most **66–76 letters**. What matters is
  key *entropy*, not length: a random 97-letter key (456 bits) makes K4
  **information-theoretically ambiguous**, while a structured long key — a running
  key from text, or a keystream read off a physical object (~30 bits) — stays
  recoverable *if the source is known*. This single fact explains the whole pattern
  of results across three sessions.
- **Depth would break it.** Simulated against a true one-time pad, two messages
  sharing a keystream give `C1−C2 = P1−P2` exactly; shared words at shared positions
  are directly visible; and crib-dragging 24 known letters of one message recovers
  24 letters of the other with no key knowledge. That is the stated K4/K5 relation.

### Added 2026-09-12 (session 4) — verified geometry and the surviving architecture

- **K4's carved line structure is OBKR + three lines of 31** (boundaries at absolute
  positions 4, 35, 66). Self-verified: the lines concatenate exactly to the canonical
  ciphertext. This REPLACES the 7×14 layout, which came from a source now on the
  contamination exclusion list (`docs/contamination-log.md`).
- `EASTNORTHEAST` lies wholly inside line 1; `BERLINCLOCK` **straddles** the
  line-2/line-3 boundary at position 66.
- **The engraved line lengths vary** — Sanborn kerned the lettering — so the
  ciphertext panel is not on a regular lattice while the tableau panel is. Any
  panel-to-panel overlay mechanism is STRONGLY DISFAVORED.
- **Weltzeituhr mechanics corrected**: the 24-sided city-name cylinder is STATIC;
  an hour ring rotates inside it. The earlier note describing the drum as rotating
  was wrong.
- **A new diagnostic (EXP-021).** The pattern of breakage at the edges of a span
  shared by two messages measures a cipher's memory depth and direction directly:
  no breaks → position-indexed; k leading breaks → backward memory k; k trailing
  breaks → forward mixing k; all broken → unbounded feedback; scattered →
  transposition. This is the first measurement to make if K5 is ever released.
- **The surviving architecture.** Three independent lines converge on a keystream
  **read off an external object, position by position**: EXP-019 (long but
  low-entropy, externally sourced), EXP-021 (position-indexed, no net transposition,
  no unbounded feedback), and the exhaustive elimination of every short or
  structured position-indexed key.

### Added 2026-09-12 (session 5) — the authentic Weltzeituhr, as far as it goes

- **Structure corrected and established.** The 24-sided city-name cylinder is
  **static**; a **rotating hour ring** carries the hours through the zones (Trabant
  gearbox). The cylinder is in **three parts**: city names on the **upper** disk,
  hour ring in the **middle**, city names on the **lower** disk. Letters are
  **stamped** from punches. An orrery above turns once per minute; a compass-rose
  mosaic sits at the base. Earlier notes describing the drum as rotating were wrong.
- **Hans-Joachim Kunsch** executed the 1969 construction on site and led the Oct–Dec
  1997 restoration — one person spanning both states of the object. His restoration
  records are the single highest-value missing document.
- **1997 changes, partial**: Leningrad→Sankt Petersburg, Alma Ata→Almaty,
  Bratislava→Pressburg; ~20 politically-omitted cities added (only Tel Aviv, Cape
  Town, Seoul, Jerusalem named); some zone moves (only Kyiv named).
- **Totals conflict irreconcilably**: 80 (1969) / 146 / 148.
- **The 1988–89 per-sector name list is UNKNOWN** and was not guessed. See
  `docs/checkpoint-E-research-log.md`.
- **The Weltzeituhr test is built, preregistered and validated but NOT RUN**
  (EXP-024): 22 reading procedures fixed while the data is unavailable, validated
  end-to-end on a synthetic clock with a planted keystream.
- **Sanborn's Morse material tested as a key tape and failed** (EXP-023): 13,680
  alignments, best 5/24, below chance.

## High-priority inherited program: `TOKIO → 57973`

**Inherited result.** A substantial prior July 2026 handoff reportedly converged on the following chain:

`W positions → 20, 15, 11, 9, 15 → TOKIO → physical 57973`

That handoff reportedly defined 942 canonical route cases and found 935 broader double-route cases that did not reach complete language closure. The immediate task is **not** to expand the search. First recover or reconstruct:

- the exact definition of every route family;
- the source of `57973` and its physical interpretation;
- the canonical enumeration order and reported hash;
- the 7 completed/negative cases and the 935 unfinished cases;
- the plaintext scoring and crib gate.

Until those records are recovered, treat the counts as an inherited lead, not an independently verified result.

## `4 × 22` World Clock / TOKIO construction

**Hypothesis; many obvious variants tested negatively.** Removing `OBKR` and the five `W` characters from K4 produces 88 letters, i.e. a `4 × 22` array. The five pre-terminal W-run lengths were recorded as `20, 15, 11, 9, 15`, spelling `TOKIO` under A1Z26; the final run is 22.

The inherited analysis constructed the historically relevant UTC+9 city tape:

`JAKUTSKPJOENGJANGTOKIO` (22 normalized letters)

and proposed:

`OBKR` indicator → W counts identify TOKIO → 22 specifies the clock tape → 88-character body in a 4 × 22 array → tape controls a bespoke lookup.

The 22-length coincidence is interesting, but ordinary transpositions and simple keyed operations did not work. The only remaining version worth testing is a small, pre-declared lookup rule `P = f(C, clock letter, row, column)`, with strict parameter bounds and an out-of-sample rule.

## Other retained leads

### Physical tableau parity / two-chart model

**Inherited result — now EXPLAINED as a selection effect, and demoted.** On a
reconstruction of physically opposed tableau letters, ordinary A=0 parity reportedly
separated every one of ten known same-cipher/different-plain crib conflicts. A two-chart
homophonic interpretation had no contradictions at the crib positions.

EXP-009 computes what that is worth. Exactly **16,384 of the 16,777,216** possible binary
selectors separate all ten conflicts, so an arbitrary bit-stream does so with probability
**1 in 1,024** — the observation carries about ten bits. A selector family with ~1,000
members is expected to contain a winner, and this document already records that multiple
Morse phases were searched. Moreover, in the *encryption* direction two charts are
impossible outright (at least three alphabets are forced), so the two-chart framing is
not merely uninformative but unavailable. **Do not spend further effort here.**

This is a selector clue, not a chart construction. Simple Caesar, affine, Atbash, rotated Kryptos-alphabet, and direct numeric-mask versions failed. Do not use unconstrained language optimization to fill the charts.

### K0 Morse as binary selector

**Inherited result — demoted for the same reason as the parity lead above; see EXP-009.**
A reversed, phase-shifted dot/dash stream from the physically visible “T IS YOUR POSITION” reading reportedly satisfied the same ten A/B selector constraints. Obvious two-transform (Baudot/Vigenère/tableau) follow-ons failed, and multiple phases were searched, so the match is not dispositive.

### Kryptos alphabet rail alternation

**Inherited observation.** Split the Kryptos alphabet into alternating rails:

```text
rail 0: K Y T S B D F H J M Q V X
rail 1: R P O A C E G I L N U W Z
```

At known crib positions, repeated plaintext-letter occurrences were reported to map to
opposite ciphertext rails in 7/7 transitions. **Demoted:** this is the same class of claim
as the parity and Morse selectors, and EXP-009 shows such a claim is worth about ten bits. The inherited work found no simple relationship to opposite-tableau parity, position parity, or 7×14/31-column geometry. This is an anomaly to test prospectively, not a cipher key.

### `DIAWINFBN` +5 run

**Inherited observation.** The substring `DIAWINFBN` exhibits five consecutive relations `C[i+4] = C[i] + 5 (mod 26)`. Its previously reported post-hoc adjusted significance was approximately 0.00156. The run was localised (positions 55-63, ending on the first letter of the BERLINCLOCK
crib) and then tested hard. Its significance is **p ~ 0.017** family-wise across 1,248
(alphabet, lag, delta) combinations — real but about 2 sigma. **EXP-010 removed its
independent support**: across four change-point statistics, two alphabets and a permutation
null on the maximum over 68 boundaries, no boundary is significant and position 63 ranks
65th, 47th, 31st and 39th of 68. It is not special.

The run is also *provably* beyond crib algebra: positions 55-62 lie outside both cribs, so
"progressive key over flat plaintext" and "flat key over patterned plaintext" fit equally
and cannot be separated. **Demoted back to an unexplained anomaly.** See `ideas.md` § 4.
