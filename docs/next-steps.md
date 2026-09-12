# Next experiments

## 1 — Reconstruct the `TOKIO → 57973` corpus

Priority: **highest**. This is the narrowest inherited program with unfinished, finite work.

- Locate the prior July 2026 route definition and hash, if possible.
- Otherwise write a specification before code: source data, normalization, physical coordinate system, all 942 canonical routes, and expected hash.
- Implement deterministic enumeration and a crib gate using `data/k4.json`.
- Commit inputs, implementation, hash, and an explicit status table for every case.
- Only then continue the reported 935 broader double-route cases.

## 2 — Bounded `4 × 22` lookup experiments

Priority: medium. The conventional versions are already negative.

Test only small, pre-registered rule classes of the form:

`P = f(C, T[col], row, col)`

where `T = JAKUTSKPJOENGJANGTOKIO`. Constrain every degree of freedom, require all crib letters, and reserve at least one family of positions as a holdout to limit overfitting. Report the total search count, not just the best score.

## 3 — Convert selector anomalies into predictions

Priority: medium.

For each selector candidate (opposite-tableau parity, K0 Morse phase, Kryptos rails), define its bitstream from source data without seeing a candidate plaintext. Then ask whether it predicts a simple, independently constrained chart or route. Discard it if chart flexibility is doing all the work.

## 4 — Audit the source transcription and geometry

Priority: supporting work. Make a machine-readable physical transcript that preserves row/column alignment, tableau orientation, omissions, and the exact normalization used. This prevents future work from silently mixing a modern World Clock city list with a period-appropriate one.

## Required result record

For each experiment create a dated Markdown record with: hypothesis; input source and hash; code revision; full parameters; number of variants; crib result; output/hash; negative or positive conclusion; and the exact reason it differs from prior work.
