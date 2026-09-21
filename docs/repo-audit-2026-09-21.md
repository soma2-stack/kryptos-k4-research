# Whole-repository audit — 2026-09-21

**Repository:** `soma2-stack/kryptos-k4-research`  
**Audited branch:** `claude/dreamy-archimedes-79k6u0`  
**Audited HEAD:** `133d566733b16e46221ace5490295f2c2499deb7`  
**Tree:** `478143b6fe06ff171924c352a966a771368a284e`

## Scope and verification boundary

This was a whole-tree static/content audit of the committed branch through GitHub: repository
structure, canonical handoffs, machine-readable data, experiment/result/preregistration/verifier
coverage, provenance/contamination records, operational scripts, and stale/superseded claims.

The active execution container could not resolve github.com, so this audit did **not** perform a
fresh clean-clone rerun of the Python experiments. Findings labelled reproducibility gaps therefore
refer to committed artifacts/code and documentation, not a new execution verdict.

Tree inventory at audit time:

- 371 Git tree entries
- 344 tracked blobs/files
- 27 directories
- 43 experiment scripts (EXP-001 through EXP-043)
- 35 audit files
- 120 result files
- no zero-byte tracked files
- one exact duplicate-blob pair: `audit/exp005_baseline.txt` and
  `results/logs/exp005_recovery_selftest.txt`

K4 remains UNSOLVED.

---

## Executive verdict

The repository has a **strong research core but a weak current navigation layer**.

The strongest modern work (roughly EXP-030 through EXP-043) is substantially better documented
than the early repository: preregistrations, compact result artifacts, controls, scoped claims and
independent verifier scripts are generally present. The contamination discipline and prospective
correction practice are also unusually careful.

The main risk is not that the latest negative experiments are obviously broken. It is that a new
researcher can enter through README / next-steps / resume-prompt / autonomous files and be sent
back into claims that later checkpoints explicitly superseded.

Several machine-readable or operational files also lag the current state, so this is not merely
cosmetic documentation debt.

---

## Findings

### A1 — HIGH: the front-door handoff files are stale and mutually inconsistent

The following files still present old states as current:

- `README.md`: “Current position” is Checkpoint S.
- `docs/research-state.md`: opens with “Current: Checkpoint J.”
- `docs/next-steps.md`: opens with “Current: Checkpoint J” and still uses the withdrawn
  EXP-021 position-preservation/external-object-keystream convergence as an active premise.
- `docs/resume-prompt.md`: opens with Checkpoint J, tells a new agent to read the stale files,
  directs work toward old inherited tasks, and instructs `./run_all.sh`.
- `docs/ideas.md`: contains multiple “not yet tested” / “still not started” statements that
  later checkpoints have closed or superseded.

This is operationally dangerous because these are exactly the files a fresh agent is likely to
read first.

**Recommended correction:** put one authoritative “CURRENT STATE” banner at the top of each,
pointing to `docs/current-status.md` and `autonomous/KNOWN_STATE.md`, and label the body below
as historical unless rewritten.

### A2 — HIGH: autonomous scout state/instructions predate EXP-040–043

`AUTONOMOUS_SCOUT.md` still says:

- Checkpoint AE remains canonical;
- no EXP-040 is justified;
- do not launch EXP-040;
- the AL residual classes are the current frontier.

`autonomous/state.json` is frozen at iteration 13 / 2026-09-14 and predates EXP-040–043,
Checkpoint AM and the AN/AO provenance correction.

`autonomous/open-questions.md` still asks AL-era questions as the current queue.

The PowerShell supervisor is hard-wired to `luna/k4-autonomous-scout` and refuses Claude
branches, which prevents accidental pushes from the Claude branch; nevertheless the content is
unsafe as a current research handoff.

**Recommended correction:** either archive the Luna automation explicitly as historical/frozen,
or update its readme/state contract and keep branch-specific automation separate from the current
Claude handoff.

### A3 — HIGH: machine-readable cipher-side metadata revives a resolved discrepancy

`data/cipher_side_rows.json` still contains
`verification.open_discrepancy.status = "UNRESOLVED"` for the old 432-vs-435 issue.

Later Checkpoint L / Request 5 correctly resolved this as a units mistake:

- rows 1–14 = 435 physical characters;
- 432 are letters;
- 3 are `?`;
- there is no discrepancy on that basis.

Because `data/cipher_side_rows.json` is treated as authoritative machine-readable data, this
stale field can cause code or agents to reopen a closed issue.

**Recommended correction:** prospectively replace the “open discrepancy” object with a
`resolved_correction` record pointing to Checkpoint L / Request 5, while retaining the historical
text elsewhere.

### A4 — HIGH: EXP-043's K3-derived-family motivation is not independently reproducible yet

The EXP-043 negative over its **declared affine-mod-97 family** is well recorded:

- 15,197,184 configurations;
- zero feasible;
- controls pass;
- summary artifact committed;
- independent verifier performs cycle-certificate and forward-simulation checks.

However the stronger derivation claim used to motivate that family is not independently rebuilt by
the committed verifier.

The result/write-up claims that K3's exact permutation was recovered from 12 equivalent rectangle
descriptions, with:

- one unique permutation of 336 positions;
- first differences only 191 and 192;
- cycle type 168 + 168;
- order 168.

But `experiments/exp043_k3_derived_sandwich.py` starts from the asserted near-constant-stride
property; it does not contain the K3 route-recovery procedure. `audit/verify_exp043.py` verifies
that K3 plaintext/ciphertext have matching multisets and then verifies the affine K4 corpus
arithmetic, but it does not independently reproduce those K3 permutation properties.

Therefore:

- **the affine-family negative stands as a reproducible scoped negative from committed artifacts;**
- the stronger statement “K1–K3 are exhausted as a source of π / this is the unique faithful
  K3-derived family” currently has a verification gap.

**Recommended correction:** add a small independent verifier that reconstructs the K3 permutation
from committed K3 plaintext/ciphertext data and asserts the 12 descriptions, permutation equality,
191/192 differences, cycle type and order before treating the derivation as fully independently
verified.

### A5 — HIGH/MEDIUM: EXP-043's plaintext-side provenance is weaker than its wording suggests

`data/mask_sources.json` explicitly marks `K1_plaintext`, `K2_plaintext` and `K3_plaintext`
as `verified: false`, with notes saying they are working/widely published transcriptions not yet
checked against a primary source.

EXP-043 says K1–K3 mechanics were “re-derived from repository data,” and the K3 route derivation
depends on the exact K3 plaintext.

The cipher-side rows are Grade-A/provenance-tracked; the plaintext side is not represented at the
same provenance level in the machine-readable data.

**Recommended correction:** primary-source-verify and freeze exact K1–K3 plaintext strings (or
explicitly downgrade the EXP-043 derivation language until that is done). Do not silently flip the
existing `verified` flags without a source record.

### A6 — MEDIUM: EXP-043 preregistration contains a disclosed counting deviation and an under-explained null

The preregistration states `p,q >= 2, p+q <= 19` but calls this 57 pairs. The implementation
correctly treats M1/M2 as distinct roles and uses 136 ordered pairs. The final result discloses the
correction.

This appears to be bookkeeping rather than hidden post-hoc model expansion because the roles were
already ordered in the mathematical model, but it is still a preregistration deviation and should
remain visible.

The result also quotes expected accidental survivors around `2.3e-3`. A naive bound using the
reported final `N=15,197,184` and worst `d_eff=18` gives a much looser ~0.049 upper bound.
A separate rank-distribution calculation can produce a value in the few-`1e-3` range, so the
smaller null is plausible; the problem is that the committed result does not show that
rank-distribution calculation explicitly.

**Recommended correction:** commit the exact null calculation/rank histogram used for EXP-043.

### A7 — MEDIUM: EXP-029 remains a reproducibility artifact hole

EXP-029 has committed source code and is discussed extensively as a completed scoped negative, but
the tree still lacks:

- `results/logs/exp029_weltzeituhr_restricted.txt`;
- `results/exp029/summary.json`;
- a dedicated independent verifier.

This is especially relevant because `docs/codex-audit.md` already found material defects in the
original EXP-029 presentation:

- modulo-120 wrapping contradicted the stated non-wrapping intent;
- duplicated labelled streams;
- the two 7/24 maxima were the same alignment under rotation;
- the Poisson significance interpretation was not calibrated;
- a control wrapped;
- the raw log was not committed.

The codex audit preserves a narrower zero-hit conclusion for the non-wrapping subset, but the
underlying artifact gap still exists.

**Recommended correction:** either reproduce EXP-029 cleanly into a compact versioned summary +
verifier, or explicitly demote the original result to “historical scoped negative, repaired only
by later audit” and stop presenting it as equivalent in reproducibility to EXP-030+.

### A8 — MEDIUM: `run_all.sh` is no longer a safe onboarding command

`run_all.sh` blindly executes every `experiments/exp*.py` and overwrites
`results/logs/<name>.txt`.

Older docs still instruct fresh researchers to run it.

That made sense when the suite was small. The current tree contains expensive modern exhaustive
experiments and scripts that write their own summary artifacts. A blanket full rerun is not an
appropriate smoke test and can overwrite historical logs.

**Recommended correction:** split into:
- a fast deterministic smoke/integrity suite;
- targeted verifier suite;
- explicitly opt-in full regeneration commands per checkpoint.

### A9 — MEDIUM: dependency/environment reproducibility is not pinned

No `requirements.txt`, `pyproject.toml`, lockfile, or equivalent environment manifest is
present in the tree, and no `.github/workflows` CI directory is present.

Later checkpoint documentation explicitly notes that some experiments require NumPy. Python version
and dependency versions are therefore implicit.

**Recommended correction:** add a minimal pinned/reasonably bounded Python environment manifest and
a CI/smoke workflow for data integrity + cheap verifier checks. Large experiments should remain
manual/opt-in.

### A10 — MEDIUM: `docs/sources.md` is no longer a useful source-of-truth index

`docs/sources.md` contains only a handful of sources, while the actual repository now contains a
large, nuanced evidence/provenance corpus under `docs/external/`.

This mismatch makes it easy for new agents or external research tools to rediscover evidence or
miss supersession/provenance grades.

**Recommended correction:** make `docs/sources.md` an index into the current source ledger, with
claim, date, source, grade, checkpoint, and supersession status. Do not duplicate all narrative
content.

### A11 — MEDIUM/LOW: `docs/external-evidence-requests.md` is historical, not a current queue

The file begins with Request 1 as blocked/highest priority, then later records Request 1 as
fulfilled. Other requests are similarly appended and later demoted/resolved.

The history is valuable; the filename and opening presentation make it easy to treat obsolete
requests as current.

**Recommended correction:** add a status table at the very top: OPEN / FULFILLED / DEMOTED /
BLOCKED / SUPERSEDED, with links to the later resolution sections.

### A12 — MEDIUM/LOW: canonical files still contain residual historical present tense

`autonomous/KNOWN_STATE.md` says it is updated through EXP-043, yet still states
“Checkpoint AE remains canonical” and labels a section “Open frontier (Checkpoint AL).”

`docs/current-status.md` has a correct 2026-09-21 prospective update at the top, but lower
historical material still contains present-tense statements such as “No EXP-040 exists” and
“Strongest surviving architecture: M2.pi.M1.”

These are understandable preserved historical statements, but they are not always visibly scoped
as historical at the exact point of reading.

**Recommended correction:** add local “HISTORICAL — superseded by top update” markers rather than
rewriting old checkpoint reasoning.

### A13 — LOW: process/governance docs lag the modern research standard

`CONTRIBUTING.md` requires provenance, normalization, code, bounds, trial count and outputs, but
does not encode the stronger standards the repository later adopted:

- preregistration before implementation;
- non-vacuity / positive controls;
- adversarial controls;
- explicit falsifiability/discrimination budget;
- independent verifier for strong eliminations;
- prospective correction rather than historical rewriting;
- contamination-specific source handling.

The repo practices a stronger standard than its contributor contract advertises.

**Recommended correction:** update CONTRIBUTING to match the actual current standard.

### A14 — LOW: one exact duplicate tracked artifact

`audit/exp005_baseline.txt` and `results/logs/exp005_recovery_selftest.txt` are byte-identical.

Harmless, but the repository generally prefers one canonical artifact plus references.

---

## What is strong and should be preserved

### Modern experiment discipline

EXP-030 through EXP-043 generally have much stronger artifact discipline than the first half of the
repository. EXP-030–043 all have committed summary JSON; EXP-030–043 have verifier coverage either
dedicated or shared, with EXP-032/034 sharing `verify_exp032_034.py`. Preregistration is present
for this modern series, with EXP-032/033 intentionally sharing one preregistration.

EXP-040–043 in particular preserve narrow scope and report zero feasible configurations without
claiming K4 solved.

### Canonical K4 input

`data/k4.json` is cleanly structured:
- 97-character ciphertext;
- zero-based half-open spans;
- exact two public crib runs;
- KRYPTOS mixed alphabet;
- explicit primary-verification pointer;
- no full plaintext.

`k4lib/data.py` pins ciphertext SHA-256 and checks length, alphabet, crib spans/segments,
disjointness and KRY alphabet permutation.

### Contamination discipline

The contamination logs are candid about accidental exposure risks and source failures.
Disallowed solution-oriented sources are quarantined rather than mined. Checkpoint AO correctly
demotes the recent “Stego” material after provenance failed to meet the stronger evidence
threshold.

### Prospective correction culture

The project usually does not rewrite history to hide mistakes. Later checkpoints record
corrections and preserve older reasoning. That is a major strength; the required fix is better
indexing/supersession signage, not erasing the history.

---

## Current trustworthy handoff after this audit

For a new researcher, the safest order is currently:

1. `docs/current-status.md` — read the 2026-09-21 prospective block first.
2. `autonomous/KNOWN_STATE.md` — but treat its AE/AL headings as historical until cleaned.
3. `data/k4.json`.
4. EXP-040–043 result/preregistration/verifier files when working on those exact classes.
5. Checkpoint AM and AO for the latest documentary provenance corrections.
6. Historical files only when the current state points to them.

Do **not** currently use `docs/resume-prompt.md`, `docs/next-steps.md`,
`docs/research-state.md`, or `AUTONOMOUS_SCOUT.md` as an unqualified current instruction set.

---

## Priority repair order

1. Fix the current entrypoints / stale autonomous state so future agents cannot regress.
2. Correct the stale `data/cipher_side_rows.json` resolved-discrepancy metadata.
3. Make EXP-043's K3 permutation derivation independently reproducible and pin K1–K3 plaintext
   provenance.
4. Repair/demote EXP-029's artifact trail.
5. Replace `run_all.sh` onboarding with smoke + targeted verifier commands.
6. Add dependency manifest / lightweight CI.
7. Build one current source/evidence index and one current evidence-request status table.

None of these repairs supplies a K4 solution. They improve the reliability of the research
program and prevent future agents from reintroducing already-corrected premises.


---

## Repair pass completed — 2026-09-21

The user authorized a prospective repair pass after this audit. The following audit findings were
addressed on `claude/dreamy-archimedes-79k6u0` without rewriting historical checkpoint records:

- **A1:** current-state guards added to README, research-state, next-steps, resume-prompt and ideas.
- **A2:** Luna scout contract, state snapshot and AL-era open-question queue explicitly frozen as
  historical on the Claude branch; KNOWN_STATE advanced prospectively through EXP-043.
- **A3:** `data/cipher_side_rows.json` now records the 432-vs-435 issue as RESOLVED and removes
  the stale `open_discrepancy` object.
- **A4:** added `audit/verify_exp043_k3_derivation.py`, which independently reconstructs K3 from
  an explicit 8x42 -> 24x14 double-rotation route and verifies the 191/192 differences, 168+168
  cycle type, order 168 and a frozen permutation hash. The historical uncommitted “12 route
  descriptions” count is no longer load-bearing.
- **A5:** provenance was **not falsely upgraded**. The new verifier deliberately preserves and
  reports `K3_plaintext verified=false`; current EXP-043 wording now separates reproducible
  derivation from primary-source provenance.
- **A6:** EXP-043 current wording now points to the corrected verification scope. The exact
  rank-distribution/null calculation remains a documentation improvement rather than a blocking
  validity issue.
- **A7:** EXP-029 now has a dedicated prospective reproducibility-status note and is explicitly
  classified as a historical scoped negative repaired by later audit, not equivalent to EXP-030+.
- **A8:** `run_all.sh` is explicit opt-in only; `smoke.py` and `run_smoke.sh` are the safe
  onboarding commands.
- **A9:** added `requirements.txt` and `.github/workflows/smoke.yml`.
- **A10:** added `docs/source-index-current.md`; legacy `docs/sources.md` points to it.
- **A11:** added a current OPEN/FULFILLED/DEMOTED status table to
  `docs/external-evidence-requests.md`.
- **A12:** residual stale present-tense frontier statements in current-status were narrowed or
  explicitly marked historical.
- **A13:** CONTRIBUTING now codifies preregistration, discrimination accounting, controls,
  independent verification, contamination discipline and prospective corrections.
- **A14:** the duplicate EXP-005 baseline artifact was left in place because it is harmless and
  may serve historical auditability; no research conclusion depends on deduplicating it.

A CI run was not observable through the available GitHub status interface at repair time, so this
appendix does not claim that GitHub Actions executed successfully. The smoke workflow and scripts
are committed for execution in a normal clone/Actions environment.
