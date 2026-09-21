# Checkpoint S2 — re-evaluation of Checkpoint S against the 1991 ABC Scheidt interview

Narrow question: does the 1991 Scheidt language change the EXP-040 gate or identify a specific,
bounded, evidence-backed K4 architecture?

**Answer: no.** It strengthens one class-level conclusion, narrows two readings that the
incoming audit stated slightly too strongly, surfaces a genuine tension with Checkpoint S §D,
and exposes one provenance gap. It specifies no transform.

## Source identity and grade

ABC *World News Tonight* B-roll, 1991; John Martin interviewing Ed Scheidt across two tapes;
transcript prepared by Elonka Dunin, January 2004; public PDF at
`thekryptosproject.com/media/transcripts/pdfs/1991c.pdf`.

**Grade B+** for the clear answers — contemporaneous interview, but a third-party transcript
rather than the original master. **LOW / context-incomplete** for the muffled passage (§F).

---

## A. Is "custom / adapted" strengthened?

**Yes. Grade: STRONGLY SUPPORTED** (up from SUPPORTED INTERPRETATION at Checkpoint S).

Contributing statements: roughly four months examining what kinds of codes would be
appropriate; tutorials given because the cryptography had to fit Sanborn's objectives and
constraints; Scheidt confirms he helped design how the information would be encrypted; a
further month after the code was chosen; then "this is how you do it".

This is now the second **contemporaneous** source (with the January 1990 *Washington Post*
"a modern system created for the project") rather than a retrospective recollection, and it is
from the cryptographer himself. That is a real upgrade.

**It stops well short of DIRECTLY STATED.** Scheidt never says the method was modified,
non-standard, or newly invented — and when asked directly whether it was a common form of
encryption, he **declined to answer**. A refusal is not a denial.

### A caution the phrase "unique to Jim's design" actually requires

Read in context, Scheidt has just explained that the cryptography had to match Sanborn's
intended objective and theme. "The code was unique to Jim's design" therefore reads most
naturally as *the code was tailored to Jim's artwork* — **not** as *Jim designed the code*.

That distinction matters, because Checkpoint S §D leaned on Sanborn as the **modifier**.

---

## B. Does it select a specific architecture? — No, for every candidate

| candidate | direct evidence chain from the 1991 source? |
|---|---|
| modified transposition | none — no mechanism named |
| modified polyalphabetic masking | none |
| running key | none — no source named |
| keyed tableau, irregular schedule | none |
| fractionation | none |
| homophonic mapping | none |
| multi-stage composition | none — "a code" is discussed in the singular |
| stateful keystream | none |
| computer-assisted construction | **only** the muffled fragment, which is prohibited as motivation (§F) |
| something already in the corpus | not excluded, and not indicated either |

"Unique" and "innovative" describe intent and fit, not a transform. Nothing here supplies
equations, a schedule, a key source, or a composition.

---

## C. "Either the keys or the method or something like that" — narrowed

The incoming audit reads this as *strong evidence that model identification was intentionally
part of the puzzle*. **That is slightly stronger than the sentence licenses**, and the
correction matters because this line is the one most likely to be over-cited later.

- **Directly supported:** Scheidt contemplated that a solver might need to discover the method
  as well as, or instead of, the keys. Method discovery was **within his expectation**.
- **Not supported:** that method discovery is *required*. The sentence is a **disjunction** —
  "either the keys **or** the method" — which is also satisfied by a standard method with an
  unknown key, where key recovery alone suffices. The trailing hedge "or something like that"
  weakens it further.
- **Speculation, excluded:** that the method is therefore nonstandard, or that the key is
  insufficient without algorithm knowledge.

**Net: SUPPORTED that method discovery was anticipated; NOT SUPPORTED that it is necessary.**
This is not a licence for arbitrary custom algorithms.

---

## D. The extra month — ranked, and one thing it does not establish

Scheidt: after they decided what code they wanted, he spent about another month on it, then
gave Sanborn "this is how you do it."

| reading | grade |
|---|---|
| implementation, documentation, preparing key material, and teaching the procedure | **most economical; fully compatible** |
| substantial modification of a known method | compatible, no better supported than the above |
| custom key-schedule development | compatible, no better supported |
| custom masking-layer design | compatible, no better supported |
| designing K4 **specifically** | **NOT ESTABLISHED** |

**The timeline covers the sculpture's cryptography as a whole, not K4.** Four months of
selection plus one month of work spans all four sections, so attributing that month to K4 is
unsupported. Any future argument that leans on "a month was spent on K4" is using evidence that
does not exist.

**A soft inference worth recording:** roughly five months, part-time, for a professional to
select and prepare the cryptography for four sections is a *modest* budget. It sits more
comfortably with adapting and combining known systems than with inventing and validating a
novel primitive. **Grade: INFERENCE, weak.** Not used to select anything.

---

## E. Reconciliation with the 2005 material — and a tension worth recording

**Four processes: unchanged.** The 1991 interview never enumerates processes and speaks of "a
code" for the work as a whole. It neither supports nor undermines one-process-per-section, and
the interpretation is retained exactly as at Checkpoint S.

**Masking: mildly strengthened at class level.** "Tailored to Jim's design" fits Scheidt's later
description of a disguised fourth process better than it fits an off-the-shelf cipher — but it
still names no masking technique.

### The tension

Checkpoint S §D concluded that **Sanborn selected and modified**, leaning on the 2005 Sanborn
interview. The 1991 Scheidt account points the other way: **Scheidt** examined the options,
**Scheidt** spent the extra month, and **Scheidt** then handed Sanborn a procedure — "this is
how you do it." On that account Sanborn is the **executor**.

Both can be true in sequence (Scheidt delivers, Sanborn adapts), and neither source rules the
other out. But the 1991 source is **contemporaneous and from the cryptographer**, while the
2005 Sanborn statement is a recollection fifteen years later from the non-specialist.

**Consequence, and it runs against the obvious expectation:** if a professional delivered a
finished procedure, the result is more likely to be a *coherent, professionally-chosen method,
possibly adapted*, than an idiosyncratic artist's modification. That very slightly **raises**
the prior on a nameable-but-adapted method and correspondingly softens Checkpoint S's claim
that searching nameable families is poorly justified.

**It does not reverse that claim** — thirty-nine negatives stand, and "adapted" still breaks
name-matching. Recorded as a tension, not resolved. Grade: **both readings COMPATIBLE**; no
change to any experimental decision.

### Provenance gap found

The incoming audit cites a **1999 *Washington Post*** quotation in which Scheidt says he could
use methods with a **historic basis** without compromising then-current government cryptography,
and that the puzzle was meant eventually to be decipherable.

That quotation appears **nowhere else in this repository** and has **no audit note of its own**.
If it holds it is important — it would bound "modern" from above and point at adapted-classical
rather than a modern primitive, materially constraining §A. **It must not be relied on until it
has its own provenance record.** Logged as a documentary to-do.

---

## F. The muffled "computer / addons / modular" fragment — quarantined

**Exact surviving words, as transcribed:**

- "different enough, innovative enough to capture the imagination"
- "taking the standard"
- "you've got that computer there"
- "addons"
- "modular"

**Why the context is insufficient:** the transcript describes the audio as very muffled and the
clip as cut before and after, so the referent of every fragment is unrecoverable. The transcript
is also a third-party transcription of B-roll, not a master. "Taking the standard" has no object.
"Addons" and "modular" have no subject. And "you've got that computer there" is most plausibly a
**deictic remark about a computer physically present in the room during the 1991 interview** —
B-roll is shot on location — rather than a statement about how the cipher was built. That
alternative reading alone is enough to disqualify it as evidence.

**Prohibited claims** — none of these may be inferred from the fragment: computer-based cipher;
modular arithmetic; an add-on or extra layer; stream cipher; block cipher; multiple sequential
layers; software-generated keystream; or any specific K4 architecture. It may **not** be used as
experiment motivation.

**What it does do, minimally:** it weakens any *categorical* assertion that the design must have
been entirely pencil-and-paper. That is a removal of a constraint, not the addition of one.

**What would upgrade it:** the original ABC audio or video for these two tapes, with enough
surrounding context to recover the subject and object of each fragment. Nothing less. A cleaner
re-transcription of the same muffled audio would not suffice.

---

## G. EXP-040 gate — reapplied

The distinction the gate is designed to catch applies exactly here: **condition 1 strengthens
while conditions 2 and 3 remain impossible.**

| condition | status after the 1991 source |
|---|---|
| 1. documentary support stronger than "not yet tested" | **strengthened** for the *class* "custom/adapted procedure" |
| 2. exact mathematical definition freezable before the verdict | **fails** — no transform, schedule, key source or equations are named |
| 3. bounded or existentially decidable parameter space | **fails** — "tailored to Jim's design" is a statement that the space is unbounded |
| 4. meaningful crib rejection power | n/a — nothing to test |
| 5. not duplicating EXP-001…039 | n/a |
| 6. precomputed accidental-survivor expectation | n/a |
| 7. a zero eliminates a meaningful family | n/a |
| 8. not selected because prior experiments failed | n/a |

There is a self-defeating quality worth naming: the **stronger** the evidence that the method
was tailored and deliberately withheld, the **lower** the prospect that any nameable family
matches it. This source increases confidence in the class while reducing the chance of a bounded
test — so it cannot, even in principle, be the thing that unlocks EXP-040.

> **The 1991 Scheidt interview materially strengthens the conclusion that the Kryptos method was
> custom/adapted to Sanborn's design and that method discovery was anticipated as part of the
> puzzle, but it still does not specify a bounded transform or parameter family. No EXP-040 is
> justified.**

No fake finite family was constructed to keep testing.
