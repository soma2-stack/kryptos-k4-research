> **Read `docs/evidence-grades.md` first.** Several entries below were originally
> stated more universally than their arguments support. That document regrades every
> one against a five-level scale (PROVED IMPOSSIBLE / EXHAUSTIVELY ELIMINATED WITHIN
> A SPECIFIED MODEL / STRONGLY DISFAVORED / HEURISTIC NEGATIVE / UNTESTABLE WITH
> CURRENT DATA) and says what each argument does **not** cover. In particular the
> three-alphabet, period-elimination and conflict results hold only for
> **monographic, position-preserving** ciphers.

# Tested and ruled-out paths

The items below were reported in the inherited conversation. They are retained to prevent duplicate work; replicate a result if it becomes a premise for a new method.

| Family | Reported scope | Result / stop rule |
| --- | --- | --- |
| Basic feedback/self-masking ciphers | Plain/cipher feedback, lags 1–12, affine variants, short keys | No crib-consistent solution. |
| 2×2 Hill / affine matrices | Matrices and affine offsets | No single matrix fits all confirmed crib letters. |
| 97-position affine clock stepping | Affine index permutations + repeated additive keys through period 20 | No exact crib fit. |
| Binary / Baudot approaches | Standard letter binary and ITA2, short repeated XOR/additive keys | No exact crib fit. |
| 24-sector World Clock geometry | Four revolutions, orientation, offsets, parity/half-rings, simple combinations | Does not reproduce cribs. |
| Opposite tableau as numeric stream | Standard/Kryptos modular arithmetic, reversals, simple two-operation variants | No clean crib explanation. |
| Physical-alignment masks | Addition, subtraction, 5-bit XOR; cyclic alignment comparison | Real alignment did not rank unusually well. |
| OBKR seeded recurrence / ordinary keyed methods | Order-4 linear recurrence, direct keyed substitution/transposition | Best reported result 7/24 crib letters; stop. |
| Alphabet-panel XOR then transposition | A prior high IoC output | Frequency profile was non-English (many S/K/Q/Z; few E/O); transposition cannot repair letter frequencies. |
| 3×31 routes | Route and optimized-columnar searches | No coherent English. |
| World Clock tape as conventional key | Vigenère/Beaufort/Variant Beaufort and columnar/Myszkowski use | Dead as ordinary use. |
| `4×22` conventional routes | 336 natural routes, including tape-ordering and Myszkowski | Best reported 5–7/24 crib letters; noise. |
| Direct simple rules on the 4×22 data | Affine, interaction/quadratic, row-specific/tableau-style arithmetic | No exact 24/24 crib mechanism. |
| K0 selector + two simple transforms | Two Baudot/Vigenère/tableau transforms | Failed. |
| Two-chart direct formulas | Caesar, affine, Atbash, Kryptos rotations; rules using opposite letter | Failed. |

## Added 2026-09-12 — reproducible, with exact search counts

Every row below is regenerable with `./run_all.sh`; see `results/2026-09-12-exp001-005.md`
for full parameter bounds and `results/logs/` for raw output. Unlike the inherited rows,
these state the number of variants actually evaluated.

| Family | Reported scope | Result / stop rule |
| --- | --- | --- |
| Repeating key, period <= 48, no transposition | 12 conventions (3 combiners x 2 plaintext x 2 ciphertext alphabets), all 24 crib letters | No period is consistent under any convention. EXP-001. |
| Affine keystream `k[i] = a*i + b` | All 676 (a,b) x 12 conventions | Zero fits under every convention. EXP-001. |
| Mengenlehreuhr (Berlin-Uhr) lamp count as keystream | t0 x step x 3 readouts x 12 conventions x free offset = 161,740,800 | 0 exact hits; best 10/24, at the null level. EXP-002. Distinct from the Urania Weltzeituhr negative above. |
| Affine-mod-97 transposition + periodic key | 9,312 permutations (complete family) + 848 routes, x 12 conventions x periods 1-12 x 2 composition orders = 2,926,080 gate evaluations | 0 hits at >= 8 constraints (FP rate 2.3e-12). EXP-003. Gate is key periodicity, not language. |
| Running-key mask from K4 ciphertext / KRYPTOS alphabet | Every alignment x 2 directions x 2 key alphabets x 12 conventions | 0 exact hits; best 7/24 against a null expectation of 1.06 such alignments. EXP-004. |
| Key sources bounded below 25 | Analytic, no search | Excluded for 8 of 12 conventions: the cribs force a key index of 24 or 25. EXP-001. |

## Interpretation discipline

“Ruled out” means the stated family and scope, not every possible cipher that shares a label. Reopen one only with a precise difference in inputs, degrees of freedom, or evaluation gate.

## Inconclusive, not negative

| Family | Why it is not a negative |
| --- | --- |
| Running-key mask from K1/K2/K3 plaintexts | `data/mask_sources.json` holds unverified working transcriptions (K2 is 370 letters here against a commonly cited 372). EXP-004 scores fuzzily so a transcription slip cannot fake a negative, but the result must be re-run against a primary transcript. |

## Added 2026-09-12 (session 2) — exact eliminations

Regenerate with `./run_all.sh`; full parameters in `results/2026-09-12b-exp006-014.md`.
"Exhaustive" below means the whole space was solved or searched to completion, not sampled.

| Family | Reported scope | Result / stop rule |
| --- | --- | --- |
| Parameter-linear position keystreams | periodic p<=16, progressive L<=12, polynomial deg<=5, each with phase reset / index reset / additive offset at every boundary in [48,80], x12 conventions; 22,584 systems **solved exactly** | Zero fits. EXP-006. Covers 26^16 = 4.4e22 keys per period. |
| Periodic keys with an arbitrary break | relative phase between cribs (p<=22) + full 1..96 boundary sweep; 43,836 systems solved exactly | Zero fits. EXP-015. Covers nulls, drops, restarts and a sculpture-long carry-over. Period 22 is MARGINAL; 23+ is vacuous. |
| Autokey / feedback / self-referential keystreams | single-tap, two-tap, tap+drift, tap+reset; sources = ciphertext forward, reversed, decimated mod 97 (m=2,3,5,7,11), plaintext; lags 0..40; 259,800 systems solved exactly | Zero fits. EXP-008. 2 unknowns vs 24 equations = chance 26^-22. |
| Reflector rotor machines (Enigma family) | invariant, no search | Impossible: C[i] == P[i] at positions 32 and 73. EXP-007. **Contingent on exact crib alignment** - at several +-3 offsets there are no fixed points at all (EXP-017). |
| Playfair | invariant, both digraph alignments | Impossible: cannot emit a doubled letter, yet ST->SS, NO->QQ, IN->TT. EXP-007. **Contingent on exact crib alignment** - the violation does not occur at every +-3 offset (EXP-017). |
| Pure transposition, any complexity | invariant + 20,000 simulations | Impossible: transposition preserves IoC; K4 is 0.03608 vs 0.06558 +- 0.00763 for English unigram text, z = -3.87, 0/20,000 at or below. Kills every route, columnar, spiral and grid transposition applied alone without enumerating any. EXP-007. |
| Hill ciphers | linear and affine, blocks 2 and 3, both alphabets, every alignment, solved exactly | No solution. EXP-007. Block 4+ largely undecidable. |
| Two-chart / binary-selector models | graph colouring, exact | Impossible in the encryption direction: at least THREE alphabets are forced. E at 21/30/64 -> F/G/Y; T at 24/28/33 -> V/R/S. EXP-009. |
| Periods for ANY periodic polyalphabetic cipher | alphabet-free conflict argument | p in {1,2,3,4,5,6,7,9,10,14,15,17} impossible for every alphabet simultaneously. The shortest possible period for K4 is 8. EXP-011. |
| Quagmire I | pincer: Part 1 + parameter count | Closed. Periods 1-7 impossible; period 6+ vacuous. No period is both possible and testable. EXP-011. |
| Every cipher with an output alphabet < 26 | coverage, no search | All 26 letters occur in K4 (J at 40, 51, 81). Kills Playfair, bifid, two-square, four-square, letter-form Nihilist, straddling checkerboard, ADFGX, ADFGVX, Baconian and every I/J-merged scheme. EXP-012. |
| Trifid | periods 2 and 3, all alignments, exhaustive constraint propagation (657,192 nodes) | Zero solutions. EXP-013. Periods 4+ are undecidable, not negative. |
| Carved tableau as running key | 26x26 KRYPTOS square by row/column/diagonal/anti-diagonal, forward and reversed, every alignment, both key alphabets, 12 conventions; 259,584 alignments | 0 exact hits, best 7/24. EXP-014. Note the alignments are correlated by construction; the apparent excess at the top of the distribution is clustering, not signal. |
| Simple progressive keys | k[i+L] = k[i] + delta, all L <= 8, both cribs, 12 conventions, algebraic | No constant lag-L key difference exists. |
| Linear recurrences over Z26 | order <= 3, fitted on EASTNORTHEAST's 13 consecutive forced key values | No recurrence fits even the fitting crib, let alone predicts BERLINCLOCK. |

| Complete transposition family x keystream models | 10,160 permutations (9,312 affine mod 97, complete + 848 routes) x 12 conventions x 25 models (progressive L<=12, polynomial deg<=5, periodic 8<=p<=16); 4,145,280 gate evaluations | Zero fits. EXP-016. Alphabet fixed in advance, since transposition + a free keyed alphabet is vacuous. Order B untested for the progressive and polynomial models - see the record. |

| Compass-bearing routes on the physical and Weltzeituhr grids | 16 compass points as lattice steps x 6 pre-registered grids (14x7 and 7x14 physical layout, 24x5 and 4x25 Weltzeituhr width, 22x5 tape, 26x4 control) x every start cell x 2 composition orders x 12 fixed conventions x 25 keystream models; 20,160 permutations, 6,048,000 gate evaluations | Zero fits. EXP-018. Planted control recovered. This is the principal BERLINCLOCK test that EXP-002 did not perform, since EXP-002 tested the Mengenlehreuhr - the wrong clock. |

| Carved-line hand-encipherment family | key restarting at each carved line (resets FIXED by the object at 4/35/66, not fitted), p<=20; per-line additive offset; key advancing once per line; progressive key per line; OBKR as line 0 or as indicator; 12 conventions; 1,344 systems solved exactly | Zero fits. EXP-020. Planted control recovered. Column-key prediction k[32]=k[63] and k[33]=k[64] satisfied by 0 of 12 conventions. |
| Panel-to-panel physical overlay (reading one object through another) | invariant, no search | STRONGLY DISFAVORED: the ciphertext panel's engraved line lengths VARY (Sanborn kerned the lettering) while the tableau panel is a regular grid, so the two are not on the same lattice and no exact cell-to-cell alignment exists. |
| Unbounded ciphertext feedback | architectural argument from the public K4/K5 description, simulated | STRONGLY DISFAVORED: it is the only class that completely destroys a positional correspondence between two messages sharing words at the same positions. EXP-021. |
| Length-changing outer layers | K4 and K5 are both exactly 97 characters | PROVED IMPOSSIBLE for any outer layer that changes length. EXP-021. |
| Natural-language running key | prediction test: under the correct convention the 24 forced key letters should look like text | HEURISTIC NEGATIVE only. Best p=0.018 uncorrected, 0.428 after correcting 24 tests. At n=24 the test cannot reliably separate English from uniform, and a key read off PROPER NOUNS need not follow English frequencies. EXP-022. |

## Undecidable, not negative

These cannot be refuted by 24 crib letters. Searching them yields fits, never evidence.
See `results/2026-09-12b-exp006-014.md` EXP-011 for the parameter counts.

| Family | Expected chance fits |
| --- | --- |
| Quagmire III / any two-keyed-alphabet scheme, period 8 | 10^+30.6 |
| Homophonic, 2 decryption charts with a free selector | 10^+48.5 |
| Affine-mod-97 transposition + Quagmire I period 8 | 10^+7.9 |
| Quagmire I, period >= 6 | 10^+1.1 |
| Trifid, period >= 4 | block coverage collapses to 0-16 constrained positions |
| Arbitrary per-position substitution | 10^+103.3 |

## A note on "exhaustive" vs "not found"

EXP-013's first implementation processed blocks in text order, hit a 40,000,000-node
cap on three of five runs, and returned no solutions. That is heuristic failure and
must not be recorded as elimination. Re-ordering the search most-constrained-block-first
cut it to 657,192 nodes and made every run complete. Only then did the negative become
real. Always report whether a search finished.
