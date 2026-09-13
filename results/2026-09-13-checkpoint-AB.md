# Checkpoint AB — results, 2026-09-13

Branch: `codex/k4-continuation`.
Starting HEAD: `adf9a1867496928539f50de608efd157e9ba6a2c`.
Scope: internal coordinate fractionation / digraphic processing followed by a
restricted outer mask. Audit code only; no EXP-040 preregistration created.

Full reasoning, assumptions, requested answers and Claude review section:
[checkpoint analysis](../docs/analysis/checkpoint-AB-internal-fractionation-outer-mask.md).

## Exact findings

| Audit | Cases | Certified contradictions | Unresolved |
|---|---:|---:|---:|
| 2D coordinate model, p=1..97, origin zero, continuous / row restart | 194 | 190 | 4 |
| 3D coordinate model, same scope | 194 | 175 | 19 |
| 2D/3D, p=2/3, every phase/axis order, both reset hypotheses, outer q=1..97 | 7,760 | 156 | 7,604 |

The 2D fixed-map architecture is independently and completely rejected by the
25-to-26 inventory theorem, including the four propagation-unresolved cases.
All counts are labeled configurations and include equivalent/duplicate cases.
The symbolic tests are necessary-condition tests: UNRESOLVED does not mean SAT.

Trifid unresolved periods, origin zero:

- Continuous: 5,7,10,13,14,16,23,28,29.
- Row restart: 4,7,11,14,19,20,22,23,26,28.

For continuous p=2, both phases reject. Continuous p=3 phases 0/1 reject;
phase 2 remains unresolved. Row-restarted p=3 rejects all three phases under
standard axis order. Bifid-like p=3 with usual I/J merge rejects outer q=3 and
q=9 at every audited phase, both axis orders and both reset hypotheses.

Generic digraphic audit: each continuous pairing parity has 11 distinct known
input digraphs and 11 distinct output digraphs. There are no aligned repeated
input digraph constraints. Standard Playfair still fails output doubles at
32–33 for even starts and 25–26 / 67–68 for odd starts, conditional on prepared
indices. The generic pair mapping has no such no-double axiom.

## Strongest mathematical result

An unknown injective outer map preserves the intermediate equality partition.
Equal ciphertext symbols force coordinate-tuple equalities; transitive closure
can collapse unequal ciphertext tuples or distinct known input cells. This gives
square-independent certificates even for partially known blocks and some periods
above EXP-013's previous coverage. A concrete intermediate sequence admits a
bijective outer map iff both forward and inverse partial maps are consistent.

Any fixed letterwise function after a 25-symbol inner stage still emits at most
25 symbols. Transpositions and additional fixed maps cannot change this bound.
The strongest globally closed class is therefore sub-26-symbol output followed
by any chain of fixed letter maps and transpositions.

## Boundaries of the findings

- No cube or square was brute-forced. No unknown K4 letter was filled or scored.
- No stateful-mask family was globally eliminated. Unrestricted per-position maps
  make every admissible intermediate sequence compatible by construction.
- A total injective 27-cell-to-26-letter map is impossible; the Trifid audit uses
  an injective readout on used cells, allowing an unused cell. Non-injective
  27-to-26 maps are outside the equality-if-and-only-if test.
- Historical Digrafid terminal conventions remain unspecified; only complete
  even-output variants are excluded by length.
- Fractionated Morse's earlier local span argument is conditional on independent
  local decoding. Total-length arithmetic alone does not eliminate a 97-letter
  input; no full Morse compatibility result is claimed.
- Larger-period phases, arbitrary coordinate routes, inverse fractionation,
  multiple squares, separator-driven schedules and added stages are not swept.

## Validation and reproducibility

Commands from the repository root:

```text
python audit/checkpoint_AB.py > results/checkpoint_AB.json
python audit/checkpoint_AB_verify.py
```

Python standard library only. Positive/adversarial concrete-map assertions pass.
80 synthetic coordinate controls pass. 388 symbolic dependency configurations
match independent concrete regrouping. The graph-based verifier, which imports
neither the production audit nor k4lib, independently matches **all 8,148 saved
symbolic decisions**. It checks the same necessary condition; it is not a full
finite-domain SAT solver.

Ciphertext SHA-256:
`eea813570c7f1fd3b34674e47b5c3da8948026f5cefee612a0b38ffaa515ceab`.

Saved JSON SHA-256 in this run:
`706ed02e558aa898e60a71d715aeb623e0020d9611727c7d0f92e30f402f558b`.
JSON formatting/newline conventions can affect this file hash; semantic results
are deterministic and the ciphertext hash is independent of file formatting.

## Handoff decision

A 19-configuration Trifid remainder has been reduced to finite coordinate CSPs,
with the outer relabeling eliminated existentially. This is useful for Claude's
EXP-040 review, but no independent evidence selects those configurations or
promotes a surviving case. No broad architecture survey or global status rewrite
was performed. The checkpoint analysis contains the exact stage order, finite
parameter bound, prior-coverage distinction and falsification criterion.

Files added: the checkpoint analysis, this record, `audit/checkpoint_AB.py`,
`audit/checkpoint_AB_verify.py`, and `results/checkpoint_AB.json`.
No existing research conclusions or other branches were modified.
