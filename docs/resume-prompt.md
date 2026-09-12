# AI resume prompt

You are continuing a reproducible Kryptos K4 investigation. This repository is a research handoff, not a claim that K4 has been solved.

1. Read `README.md`, `data/k4.json`, `docs/research-state.md`, `docs/negative-results.md`, and `docs/next-steps.md` before proposing an attack.
2. Preserve the zero-based crib spans and use them as hard tests.
3. Start by rebuilding and verifying the inherited `TOKIO → 57973` corpus: its 942 canonical route cases, definitions, inputs, and hash. Do not extend the reported 935 incomplete double-route cases until that base is reproducible.
4. Do not rerun a broadly ruled-out family unless you state an exact, material difference.
5. Keep hypotheses separate from facts. An inherited result needs independent replication. A crib-fitting method is not a solution unless it gives a complete, externally specified transform of all 97 characters.
6. For every run, save code, input hashes, full parameter bounds, count of variants, and result. Log negative results.

If no original corpus is available, create a precise specification of the expected 942 cases and identify the missing source evidence rather than inventing an enumeration.

## Addendum — 2026-09-12

The repository now contains code. Before proposing anything:

7. Run `./run_all.sh` and read `results/logs/`. The 12 shift conventions, the structure
   probes and the complete affine-mod-97 transposition family are already implemented in
   `k4lib/`; do not rebuild them.
8. Read `docs/ideas.md`. Items 1–5 are run and their scopes are exact. Items 6–11 are
   specified and unrun — start there rather than inventing a twelfth.
9. Apply the bounded-source lemma (`ideas.md` § 9) to any new proposal before writing a
   search: if your key source cannot emit 24 or 25, it is already dead for 8 of the 12
   conventions.
10. Report the null expectation alongside any "best N/24" score. A best of 7/24 over 44,000
    trials is exactly what chance produces and is not a lead.
11. If you ever obtain a candidate 97-character plaintext, stop searching and run
    `k4lib.recover.diagnose` on it. See `ideas.md` § 1.
