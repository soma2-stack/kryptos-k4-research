# Checkpoint P — public crib provenance verified

Small checkpoint. **No cryptanalytic experiment was run.** Its whole content is: audit the
external crib-provenance evidence, accept it, and propagate exactly what it licenses —
nothing wider.

**K4 remains unsolved.**

## Repository status

| | |
|---|---|
| branch | `claude/k4-post-j` |
| starting HEAD | `3979fa4824d0ab5aa709baf631eff2c26238da49` |
| working tree at start | **clean** — the interrupted session left nothing uncommitted, so no local work was lost or discarded |
| final HEAD | this checkpoint's commit |
| `main` / `codex/k4-continuation` / `claude/dreamy-archimedes-79k6u0` | untouched |

## 1. Audit of the evidence note — ACCEPTED

Every positional claim was re-derived against the committed ciphertext before acceptance:

| clue | one-based | repo zero-based | ciphertext in repo | matches source? |
|---|---|---|---|---|
| `EAST` | 22–25 | part of [21,34) | `FLRV` | ✓ |
| `NORTHEAST` | 26–34 | part of [21,34) | `QQPRNGKSS` | ✓ |
| `BERLIN` | 64–69 | part of [63,74) | `NYPVTT` | ✓ |
| `CLOCK` | 70–74 | part of [63,74) | `MZFPK` | ✓ |
| `BERLINCLOCK` | 64–74 | [63,74) | `NYPVTTMZFPK` | ✓ |

The one-based → zero-based conversions are correct, K4 is 97 characters, and the committed
cribs are byte-identical to what they were. **No crib text or index changed.**

## 2. Evidence grades — kept distinct, not flattened

| clue | grade | basis |
|---|---|---|
| `BERLIN` | **A/B** | contemporaneous NYT, explicitly position-specific ("the 64th through 69th characters … when deciphered") |
| `CLOCK` | **A/B** | same NYT report: five letters at 70–74, "they spell 'clock'", so 64–74 is BERLIN CLOCK |
| `NORTHEAST` | **A/B** positions + **A** authorship | Jan 2020 NYT places it at 26–34; Sanborn confirms the word directly on NPR (the audio does not carry the numbers) |
| `EAST` | **B+** | Sanborn released the layout privately; NYT reporter John Schwartz publicly confirmed the four letters go immediately before NORTHEAST, so 22–25 follows from NORTHEAST's placement |

`EAST` is one inferential step weaker than the other three, and this repository says so rather
than pretending the four releases have identical provenance. The combined span
`22–34 = EASTNORTHEAST` remains sufficient for use.

## 3. What the verification licenses

**The cribs are local plaintext/ciphertext positional anchors**, not statements that the words
occur somewhere in the plaintext. A proposed architecture cannot evade the 24 constraints by
decoding the clue words at other positions.

### 3a. Standard Fractionated Morse — upgraded, narrowly

Checkpoint O's rejection was conditional on the repository's inherited crib model. **That
condition is now externally supported**, so the conclusion becomes:

> **Standard Fractionated Morse is structurally incompatible with the published K4 positional
> crib semantics.**

Because `BERLIN` sits at 64–69, six ciphertext letters must account for it: 18 ternary symbols
against a minimum of 21. `CLOCK` at 70–74 is five letters, 15 symbols, against a minimum of 22.
No keyed alphabet repairs this — a keyword permutes which triple maps to which letter and
changes no length.

**Explicitly NOT generalised** to all Morse-derived systems, all length-changing systems, all
fractionation, or every non-position-preserving cipher. A more elaborate architecture may
still exist; it must *explain the numbered anchors* rather than slide the clue words.

### 3b. A second consequence, checked rather than assumed

`docs/evidence-grades.md` had downgraded the **reflector-machine and Playfair** eliminations
from PROVED IMPOSSIBLE to STRONGLY DISFAVORED, because EXP-017 showed they do not survive
every ±3 crib offset and the positions were unverified. Those offsets are now excluded by
evidence — but `EAST` is the weakest link, so I checked whether either elimination leans on it:

- **Reflector machines:** both violating positions (plaintext letter equal to its ciphertext
  letter) are one-based **33 and 74** — inside the *directly numbered* NORTHEAST and CLOCK
  spans. It does not touch the `EAST` span at all.
- **Playfair:** **7 of the 10** conflicting position-pairs lie entirely inside the directly
  numbered spans; only 3 touch 22–25.

Both eliminations therefore stand on grade-A/B positions alone and are **restored to PROVED
IMPOSSIBLE within the monographic, position-preserving class**.

## 4. Stale language removed

Current-state documents no longer describe the crib positions as inherited or unverified:
`docs/fractionation-frontier-audit.md`, `docs/evidence-grades.md`, `docs/research-state.md`,
and `data/k4.json`'s provenance note (updated in the evidence commit). **Historical checkpoint
text was not rewritten** — Checkpoint O keeps its body verbatim and carries only a
supersession banner pointing here.

Untouched deliberately: `docs/negative-results.md`'s caveat about `data/mask_sources.json`, and
`results/2026-09-12-exp001-005.md`'s note about K1–K3 rows. Those concern *ciphertext
transcriptions* of other sections, which this evidence does not address.

## 5. Evidence requests

- **Crib positions — FULFILLED** (Request 6 in `docs/external-evidence-requests.md`).
- **Request 4 — OPEN**, and the only open request that matters: Jim Sanborn papers, Archives
  of American Art, **Series 3, Box 6, Folder 10, `Pre-Production and Notes, 1990–1999`** —
  cipher-panel line geometry, fabrication layout, character spacing, row alignment, punch/type
  template, and pre-production cryptographic notes *provided they are non-solution-contaminating*.
  Nothing is blocked on it.

---

## ONE recommended next direction for a fresh session

> **Preregister and run an exact-consistency test of *stateful recursive key* schedules — keys
> whose state evolves from prior key values — over a small, precommitted family of recurrences,
> with the key decided existentially rather than enumerated.**

**Why this and not something else.** The Gromark audit at Checkpoint O established that this
class sits *outside* every existing coverage: EXP-006 covers keys that are functions of
*position* (periodic, progressive, polynomial, reset/offset); EXP-008 and EXP-034 cover keys
derived from *plaintext or ciphertext* symbols; EXP-036 covers *periodic* keys at periods 2–23.
A key that evolves from its own prior values is none of those. Only the **digit-restricted**
instance died at Checkpoint O, and it died on an alphabet gate (11–16 of 24 crib pairs need a
shift outside 0–9), not on the recurrence itself.

**Why it is not duplicate work.** Ranked #2 on the surviving list and demonstrably uncovered by
EXP-001…037. The reduction rule from `docs/combiner-coverage-matrix.md` must still be applied
to each candidate recurrence before it is admitted — a recurrence whose orbit is eventually
periodic with period ≤ 23 is *already* covered by EXP-036 and must be excluded from the family
rather than re-tested.

**Why it is falsifiable.** With the key existentially decided, a recurrence with a small state
space is finite: the whole keystream is a deterministic function of the seed, so the 24 crib
positions impose 24 constraints on a seed space of known size. Compute, before implementing,
the seed-space size, the number of distinct projections onto the 24 crib positions, and the
expected chance survivors — exactly as the Porta null was derived from its own table family,
not by analogy. **If the constraint count cannot beat the seed space, do not run it.**

**What evidence supports it.** Structural, not documentary — and it should be labelled
**STRUCTURALLY-MOTIVATED**, not documentary. Scheidt describes a fourth process that masks
ordinary English better than the first three; a self-evolving key flattens statistics in the
way that requires, and it is hand-operable in the K1–K3 idiom. There is no Sanborn or Scheidt
statement naming such a system.

**What would eliminate it.** Zero feasible seeds across the precommitted recurrence family,
with planted-positive and adversarial controls that intersect active constraints, and an
independent verifier that reimplements the recurrence rather than importing it. That would
close the last structurally-motivated class on the list and leave only speculative ones —
which is itself worth knowing.

**Setup a fresh session needs** (so nothing has to be reconstructed): cribs are
`EASTNORTHEAST` [21,34) and `BERLINCLOCK` [63,74), zero-based, now public-source verified;
`k4lib.conventions.all_conventions()` supplies the 12 committed conventions and already
includes the evidenced KRYPTOS-mixed component alphabet on both sides; the existential-decision
pattern is in `experiments/exp036_transposition_periodic.py`; the verifier pattern — no `k4lib`
import, independent reimplementation — is in `audit/verify_exp037.py`; the
constraint-count-before-verdict invariant is mandatory and asserted by the verifiers.
