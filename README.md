# Kryptos K4 research handoff

This repository preserves an ongoing, **unsolved** investigation into the 97-character K4
cryptogram on Jim Sanborn's *Kryptos* sculpture. It is a reproducible handoff for a human,
ChatGPT, or another research agent—not a claimed solution.

## Current position

The highest-value lead is new as of 2026-09-12: the `DIAWINFBN` `+5` run at lag 4 terminates
**exactly on position 63, the first letter of the `BERLINCLOCK` crib**. That is consistent
with a segment boundary at 63 or with a progressive key, and it would explain why every
global periodicity test in this repository fails. See [ideas](docs/ideas.md) § 2 and
[next steps](docs/next-steps.md) § 1.

The inherited `TOKIO → 57973` route program is now a *specification* task rather than a
search task: its route definitions and hash were never committed, and reconstructing 942
cases from a count alone would be inventing an enumeration. See
[next steps](docs/next-steps.md) § 3.

## Reproducing

```sh
./run_all.sh          # regenerates every experiment log into results/logs/
```

Python 3.11, standard library only. No network, no RNG, no external corpus.
Ciphertext SHA-256 `eea813570c7f1fd3b34674e47b5c3da8948026f5cefee612a0b38ffaa515ceab`.

## Layout

| Path | Contents |
| --- | --- |
| `data/k4.json` | The 97-character ciphertext and confirmed crib spans. Single source of truth. |
| `data/mask_sources.json` | Candidate running-key texts, each flagged `verified` or not. |
| `k4lib/` | Alphabets, the 12 shift conventions, structure probes, transposition families, the Berlin-Uhr model, and the method-recovery harness. |
| `experiments/` | One pre-registered experiment per file, each stating its hypothesis, parameter bounds and gate in its docstring. |
| `results/` | Dated result records and raw logs. |

## Where to start

1. [research state](docs/research-state.md) — inherited leads, and the short list of facts
   that are actually verified by code here.
2. [new ideas](docs/ideas.md) — eleven ranked attacks, five already run, six specified.
3. [negative results](docs/negative-results.md) — what is closed, and at what exact scope.
4. [next steps](docs/next-steps.md) — the ordered work queue.
5. [resume prompt](docs/resume-prompt.md) — complete instructions for picking this up cold.

## Discipline

Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding a result. In short: state the
hypothesis before the search, bound every parameter, report the **total variant count** and
the **null expectation** rather than only the best score, and never let a flexible model
absorb the cribs and call it a fit. A negative from apparatus that cannot produce a positive
is not a negative — `experiments/exp005_recovery_selftest.py` exists to keep that honest.

## Status

Prepared from the referenced ChatGPT conversation on 2026-09-11 and published to this
repository by the user. Extended 2026-09-12 with the first executable toolchain, five
experiments, and the position-63 observation. **K4 remains unsolved.**
