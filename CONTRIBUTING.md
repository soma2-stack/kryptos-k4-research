# Contributing a result

K4 remains unsolved. Preserve historical records and make corrections prospectively.

A strong new cryptanalytic result must include:

1. **Provenance and normalization** for every input. Distinguish primary/public evidence,
   repository-declared working transcriptions, hypotheses and contaminated/excluded material.
2. **Preregistration before implementation** for a new experiment family: exact equations,
   parameter bounds, composition order, alphabets, indexing, deduplication, stop rule and what a
   negative would actually prove.
3. **Discrimination/falsifiability accounting before execution.** Show that the available crib
   constraints can reject the declared family. Do not search a family whose freedom merely
   memorizes the observations.
4. **Reproducible code and artifacts:** input hashes where practical, total cases, compact
   machine-readable summary, and a regeneration command. Do not commit giant candidate dumps.
5. **Controls:** at minimum a planted positive/non-vacuity control for a search/solver, plus an
   adversarial control capable of changing the verdict. Report controls that cannot flip the
   verdict as "not counted", not passes.
6. **Independent verification** for a strong elimination whenever practical. The verifier should
   avoid importing the production experiment and should use a meaningfully different method.
7. **Scope discipline.** State the exact model eliminated and important nearby classes not
   eliminated. Compatibility, a best score, or a crib fit is not a solution.
8. **Contamination discipline.** Follow `docs/contamination-log.md`. Do not ingest alleged full
   K4 plaintexts, claimed/leaked solutions, auction-secret material, private K5 data, stolen/private
   documents or solution-dump sites.
9. **Prospective correction.** If a prior result is wrong or overstated, preserve the historical
   file and add a clear later correction/current-state pointer instead of silently rewriting the
   research history.

Labels remain `negative`, `inconclusive`, `replicated`, or `candidate`. Use `candidate`
only when the mechanism was specified without fitting unreleased plaintext and exactly reproduces
all admitted constraints. A complete K4 claim additionally requires one fixed deterministic
97-character procedure that independently reproduces the full ciphertext/plaintext relation.

For onboarding and CI use `python smoke.py`. Full `EXP-001..EXP-043` regeneration is
intentionally opt-in via `K4_FULL_REGEN=1 ./run_all.sh`.
