# AI resume prompt

You are continuing a reproducible Kryptos K4 investigation. This repository is a research handoff, not a claim that K4 has been solved.

1. Read `README.md`, `data/k4.json`, `docs/research-state.md`, `docs/negative-results.md`, and `docs/next-steps.md` before proposing an attack.
2. Preserve the zero-based crib spans and use them as hard tests.
3. Start by rebuilding and verifying the inherited `TOKIO → 57973` corpus: its 942 canonical route cases, definitions, inputs, and hash. Do not extend the reported 935 incomplete double-route cases until that base is reproducible.
4. Do not rerun a broadly ruled-out family unless you state an exact, material difference.
5. Keep hypotheses separate from facts. An inherited result needs independent replication. A crib-fitting method is not a solution unless it gives a complete, externally specified transform of all 97 characters.
6. For every run, save code, input hashes, full parameter bounds, count of variants, and result. Log negative results.

If no original corpus is available, create a precise specification of the expected 942 cases and identify the missing source evidence rather than inventing an enumeration.
