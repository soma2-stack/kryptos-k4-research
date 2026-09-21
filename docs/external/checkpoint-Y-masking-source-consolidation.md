# Checkpoint Y — masking / stage-order source consolidation

**Branch:** `claude/k4-post-j`

**Starting HEAD:** `cbd4f15bbe5a9164c1fc526374053886d179ebac`

**Purpose:** consolidate the external source hunt for Ed Scheidt statements about K4 masking, multi-stage structure, and stage order, while preserving the Layer A / Layer B distinction and the contamination lock.

**Result up front:** **NO EXP-040 JUSTIFIED.** The expanded source set strengthens the functional definition of masking and confirms that the stage-order question was deliberately left unanswered, but still supplies no operation, key, order, alphabet, schedule, or finite family.

## 1. Durable evidence

### 2005 WIRED — strongest operational description available

Kim Zetter's published Scheidt interview is direct participant testimony, though explicitly edited for length and organization.

Durable points:

- Scheidt says Kryptos uses four processes, with two similar and two different.
- For K4, he says he **masked the English language** so frequency/counting no longer gives the solver the same access.
- He says the masking technique **may not be known**.
- He says the solver has to identify the technique before attacking the underlying puzzle.
- He also says he did not later verify Sanborn's final implementation and that further changes were possible.

This defines masking by **effect**, not by construction.

> Working definition: masking is an operation or property intended to suppress recognizable English-language statistical structure in K4.

It does **not** establish null insertion, vowel removal, phonetic spelling, homophonic substitution, fractionation, transposition, a long key, or any other specific mechanism.

## 2. 2015 workshop — stage count and explicit refusal on order

Checkpoint X already established the durable statement that Scheidt considers K4 **more than one stage** and links that to the masking discussion.

The expanded source review adds a useful provenance refinement: the stage-order question was not merely left garbled by circumstance. The workshop record has Scheidt being asked, in substance, whether masking occurs before encryption or after it, and he **defers rather than choosing either order**.

Therefore:

- K4 multi-stage: **SUPPORTED / direct Scheidt**.
- masking as part of the Layer-A story: **SUPPORTED**.
- masking before encryption: **UNKNOWN**.
- masking after encryption: **UNKNOWN**.
- masking as one clean separable stage: **PLAUSIBLE, not explicitly fixed**.

This supersedes any reading of NOVA or solver commentary that tries to force a forward order.

## 3. PBS/NOVA 2007 — useful but easy to misuse

The official NOVA transcript contains the direct Scheidt line that the first challenge is identifying the masking technique.

However, the broadcast's examples of concealment **before enciphering** — such as vowel removal or phonetic spelling — are supplied by the narrator / other participants, not by Scheidt as a K4 specification.

Therefore NOVA is evidence that pre-encryption concealment was a public explanatory model, but **not evidence that K4 uses that order or those operations**.

## 4. Steganography / concealment lead

A preserved report of a 2004-era Scheidt talk attributes to him the statement that he used **"a bit of stego"** when designing K4, followed by a later clarification that there was a piece relating to steganography but he did not state how or in what context.

Grade this **C** unless the original exchange / recording / message metadata is recovered.

Safe conclusion:

- some concealment/steganographic relationship is plausible and historically reported;
- it is **not** enough to define a steganographic transform, stage, carrier, extraction rule, or placement in the pipeline;
- it must not be converted into acrostics, hidden-text mining, null insertion, punctuation channels, or visual carriers without independent evidence.

## 5. Other sources

### 1991 ABC B-roll

Still supports procedure selection / teaching and the possibility of a tailored method. The muffled `standard / addons / modular / computer` fragment remains quarantined as too incomplete and context-conflicted to support a K4 mechanism.

### 1999 Washington Post

Direct Scheidt quotation that the methods had a **historic basis** remains an important architecture filter, not a cipher name.

### 2010 Crimson Shield

Reported direct wording that the algorithms created for Kryptos were more unique while their mathematical principles were familiar is compatible with a project-specific adaptation. It does not identify whether this refers specifically to K4, the masking technique, or all sections.

### 2013 ACA attendee account

Claims about a hidden identity / something "built into the process" remain **C-grade attendee paraphrase**. They may concern Layer B and are too weak to motivate Layer-A architecture.

## 6. What is now safe to say

The combined documentary constraints are:

1. K4 is more than one stage.
2. A masking / disguise technique removes the ordinary English statistical advantage.
3. The masking technique may not be a standard named system.
4. There may be a steganographic / concealment-related component, but provenance is weaker and context unspecified.
5. Scheidt explicitly does not reveal whether masking precedes or follows encryption.
6. Sanborn may have modified or added something after Scheidt's handoff.
7. The design was historically grounded and intended to remain solvable.

What remains unknown:

- transform;
- stage order;
- exact number of stages;
- key source;
- alphabet/tableau;
- period/schedule;
- reset/boundary rule;
- whether the final Sanborn implementation exactly matches Scheidt's intended procedure.

## 7. EXP-040 decision

**NO EXP-040 JUSTIFIED.** `More than one stage + masking + possible stego` is still a filter, not a bounded family.

The following remain unjustified without new evidence:

- pre-encryption concealment + classical cipher;
- classical cipher + post-encryption mask;
- substitution + transposition merely because those are classical categories;
- fractionation because it suppresses statistics;
- generic steganography;
- `mask -> transposition -> mask`;
- a specific K1/K2/K3 inheritance rule.

Running any of those now would manufacture the missing architecture.

## 8. Highest-value unresolved sources

Ranked:

1. **Kim Zetter's unedited 2005 Scheidt interview** — recording, full transcript, notes, email exchange, or cut questions.
2. **Full PBS/NOVA Scheidt B-roll interview / production transcript** — to determine whether Scheidt himself endorsed any pre-encryption concealment framing that the aired narration presents editorially.
3. **Original 1991 ABC B-roll tapes** — to recover the muffled passage in context.

No new Request-7 plaintext crib was found.

## 9. Contamination lock

No 2025 recovered plaintext, reconstructed plaintext, alleged solution, auction-secret material, private K5 material, or solution-bearing page is admitted here.
