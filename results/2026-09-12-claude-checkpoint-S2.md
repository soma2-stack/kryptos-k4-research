# Checkpoint S2 — 1991 Scheidt interview re-evaluation

**Starting HEAD:** `051009db43c87b5982314d1741eba8925bf3bfcb` (branch `claude/k4-post-j`, clean tree).

**Scope:** documentary only. No experiment was designed, preregistered or run. No cryptanalytic
family was opened or closed. K4 remains unsolved.

Full analysis: `docs/external/checkpoint-S2-1991-scheidt-reevaluation.md`.

## 1. Source identity

ABC *World News Tonight* B-roll, 1991. John Martin interviewing Edward Scheidt. Transcript by
Elonka Dunin, January 2004, published at `thekryptosproject.com/media/transcripts/pdfs/1991c.pdf`.
Ingested into this repository as `docs/external/checkpoint-S-1991-abc-scheidt-broll-audit.md`.

This is the **second contemporaneous source**, and the first *from the cryptographer himself*,
speaking within roughly a year of dedication.

## 2. Evidence grades

| Element | Grade |
| --- | --- |
| Clear, fully audible answers | **B+** — contemporaneous, first-person, named interviewer, third-party transcript, no primary A/V inspected |
| The muffled `computer / addons / modular` fragment | **LOW** — quarantined, load-bearing on nothing |
| The 1999 *Washington Post* "historic basis" quotation | **provenance gap** — appears only inside the incoming audit note; no independent audit record exists in this repository |

## 3. Is "custom / modified" strengthened?

**Yes — upgraded to STRONGLY SUPPORTED** (from SUPPORTED INTERPRETATION).

It stops short of **DIRECTLY STATED**. Scheidt *declined* to say whether it was a common form of
encryption, and a refusal is not a denial. Separately, "unique to Jim's design" most naturally
reads as *tailored to Jim's artwork*, **not** *Jim designed the code*.

## 4. Is any architecture newly selected?

**No.** The transcript names no transform, no key schedule, no key source, no composition order and
no equations. Section B of the analysis tabulates ten candidate architectures and finds **no direct
evidence chain** for any of them.

## 5. "Either the keys or the method or something like that"

Read correctly this is a **disjunction**, not a conjunction. It is satisfied by a standard method
with an unknown key just as well as by a novel method. The trailing hedge "or something like that"
weakens it further.

Net: method discovery was **anticipated**, not established as **necessary**. The incoming audit's
stronger reading is narrowed here.

## 6. Significance of the "another month"

Ranked, but bounded. The ~4 months of examining appropriate codes plus ~1 further month covers the
**whole sculpture's cryptography**, not K4 specifically; "designing K4 specifically" is marked
**NOT ESTABLISHED**.

A weak inference runs the other way: ~5 months producing four sections sits more comfortably with
*adapting* known systems than with *inventing* a novel primitive.

## 7. Four-process / masking reconciliation

The four-process interpretation is **unchanged**.

A genuine **tension** is now recorded. The 1991 Scheidt account — contemporaneous, from the
cryptographer — has Scheidt hand Sanborn "this is how you do it", making Sanborn the **executor**.
Checkpoint S §D leaned on the 2005 Sanborn recollection making Sanborn the **modifier**. Both
readings remain COMPATIBLE and no experimental decision turns on it, but the 1991 reading very
slightly **raises** the prior on a nameable-but-adapted method — running against the expectation
that this source would push the other way.

## 8. EXP-040 gate decision

**NO EXP-040 IS JUSTIFIED.**

Gate condition 1 (documentary motivation) **strengthens**. Conditions 2 (a specific named transform
or schedule) and 3 (a finite, precommittable parameter space) **fail**, and fail for reasons this
source cannot in principle repair.

The strengthening is also self-defeating for the purpose of opening an experiment: better evidence
that the process was *tailored* **lowers** the prior that any nameable family matches it. No fake
finite family has been constructed to preserve the ability to keep testing.

## 9. The muffled computer / modular fragment

Quarantined in its own subsection (§F of the analysis) with:

- the exact surviving words — `different enough, innovative enough to capture the imagination`,
  `taking the standard`, `you've got that computer there`, `addons`, `modular`;
- an explicit prohibition list: no computer-based cipher, no modular arithmetic claim, no add-on
  layer, no stream cipher, no block cipher, no multiple sequential layers, no software-generated
  keystream;
- the deflating alternative reading that "you've got that computer there" is most plausibly
  **deictic** — a computer physically present during on-location B-roll — not a statement about
  the cipher;
- the upgrade condition: the **original ABC audio/video** with surrounding context.

It is load-bearing on nothing in this repository.

## 10. ONE next action

**Unchanged primary: pursue Request 2** — the unedited 2005 Zetter/Scheidt interview material.

**Newly added secondary:** the original/full 1991 ABC *World News Tonight* Scheidt interview
audio/video, sought specifically to recover the muffled/cut passage in context.

Do **not** start another speculative cryptanalytic family.
