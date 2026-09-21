# Checkpoint AH diagnostic protocol

Frozen before running the new diagnostic code, 2026-09-13. This is an artifact
statistics audit, not a cipher experiment or EXP-040 preregistration.

Inputs: data/k4.json and public data/cipher_side_rows.json only. No other text corpus.
Seed 20260913, NumPy PCG64, 10,000 draws per null, batch size 250.
Nulls: uniform iid A-Z length 97; random permutations of K4 (exact histogram/support).
The latter is the relevant null for order features. Fixed crib positions are never moved;
their ciphertext observations change with the simulated ciphertext.

Twelve prespecified statistics: support size; unordered single-letter collision pairs;
repeated bigram pairs; repeated trigram pairs; adjacent doubles; maximum standardized
lag coincidence over lags 1..48; maximum standardized residue coincidence over periods
2..48; largest adjacent-difference bin in STD and KRY alphabets; repeated translated
trigram pairs in STD and KRY (equal successive-difference pairs); row-composition Pearson
statistic for the fixed 4/31/31/31 split. Lag/period standardization uses q=1/26 as a
scale only: Monte Carlo, not a normal approximation, calibrates the maxima.

Report both tails using plus-one estimates, double the smaller tail, then Bonferroni
over 24 feature/null comparisons. Fixed histogram statistics in the permutation null
are marked invariant. No uncorrected selected lag/period is a discovery. The two tails
are included because both excess and deficit could look attractive after inspection.
This does not correct the entire historical search; it cannot make a new hypothesis
independent of previously seen K4 observations.

Power illustration: empirical K3 ciphertext frequencies (336 letters, transposition
preserves its plaintext inventory). Bootstrap 10,000 iid 97-letter samples and measure
collision-statistic rejection at the uniform 95th percentile. This is a single-profile
power illustration, not an English probability model or a cipher classifier.

Also enumerate deterministic raw observations: all repeated substrings of lengths 2..6,
all symbol distances, all 276 crib pairs, differences in all 12 existing conventions,
period collision counts 1..96, fixed row-residue groups, and repeat-block alignments 2..5.
No key, plaintext, recurrence, permutation or candidate family is searched. Deterministic
identities may refute a class without rarity controls; a statistical anomaly alone may not.
