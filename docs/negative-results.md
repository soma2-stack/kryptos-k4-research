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
