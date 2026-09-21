# Checkpoint V — K1–K3 clue inheritance research

**Branch:** `claude/k4-post-j`

**Starting HEAD:** `1d9d9ef687adae21ba71d23a66969f464871a379`

**Task:** determine what public evidence actually supports about the often-repeated claim that K1–K3 contain clues to K4, while separating Layer A (cryptographic transformation) from Layer B (post-decryption meaning/riddle).

**Result up front:** **No direct, bounded K1–K3 → K4 inheritance rule was found. No new Request-7 crib was found. No EXP-040 is justified from this evidence alone.**

The pass did produce two durable refinements:

1. `LAYER TWO` is not merely an accidental correction with no clue status: in WIRED 2006, Sanborn directly says the incorrect K2 ending meant solvers were **“missing a clue.”** The clue’s target remains ambiguous; the source does not say it is a K4 encryption instruction.
2. The 2015 Scheidt workshop is direct Layer-A evidence that K4 is **more than one stage**, with a masking technique involved. That strengthens multi-stage Layer-A motivation, but does not identify the stages, order, key, or a reuse rule from K1–K3.

---

## 1. Contamination and method

This research used only public interviews, contemporaneous reporting, and a public workshop transcript. Search results exposed 2025 solution/plaintext material; it was excluded and not used.

No alleged K4 plaintext, solution reconstruction, private K5 material, auction-secret material, or quarantined archive content is admitted.

Source ledger: `docs/external/checkpoint-V-source-ledger.md`.

---

## 2. What is actually established about “K1–K3 contain clues to K4”

### 2.1 The claim is real in contemporary reporting, but the direct quotation is still missing

WIRED reported in 2006 that Sanborn had said clues to the 97-letter last section were contained in the already deciphered parts. WIRED repeated substantially the same claim in 2010 and 2014.

However, in the accessible articles this is **reporter narration**, not a located verbatim Sanborn sentence. That distinction matters.

The evidence therefore supports:

> **SUPPORTED:** contemporary reporters close to Sanborn repeatedly understood him to mean that solved material in K1–K3 contains clues relevant to K4.

It does **not** yet support:

> **NOT ESTABLISHED:** Sanborn explicitly said those clues reveal K4’s encryption algorithm, tell the solver to combine the first three ciphers, reuse earlier keys, or reuse earlier plaintext as a key.

The unedited 2005/2006 interview material remains the best route to resolve that ambiguity.

---

## 3. K1 audit

### Public facts relevant here

K1 plaintext contains the well-known light/shadow wording and the misspelling `IQLUSION`. K1 uses the published KRYPTOS/PALIMPSEST Vigenère-family construction.

WIRED 2009 says the K1 misspelling **may** be a clue to K4, but that sentence is reporter narration. The same article quotes Sanborn saying several misspellings are intentional.

### Classification

| Candidate | Evidence | Layer classification |
| --- | --- | --- |
| light / shadow / absence-of-light wording | no direct source found saying this tells how to decrypt K4 | **NOT ACTUALLY SUPPORTED as Layer A** |
| `IQLUSION` | intentional-misspelling context exists; “may be a clue to K4” is reporter inference | **AMBIGUOUS / weak** |
| reuse K1 Vigenère-family method | no direct Sanborn/Scheidt inheritance statement found; broad descendants already heavily tested | **NOT SUPPORTED as inheritance** |
| reuse PALIMPSEST | no direct inheritance statement found | **NOT SUPPORTED** |

### Cryptanalytic coverage

Obvious K1-style shift/polyalphabetic reuse and many compositions with transposition are already represented in EXP-001/003/006/015/036/037 and related coverage. A new run is not justified by the documentary record.

---

## 4. K2 audit

K2 is the strongest clue-bearing section in this pass because of the 2006 correction.

### 4.1 `LAYER TWO`

Sanborn intentionally omitted an `X` separator for aesthetic balance, expecting the resulting decryption around the omission to become unusable. By chance, solvers obtained the plausible phrase `ID BY ROWS` instead.

When Sanborn later compared the physical text to his intended plaintext, he corrected the passage to `X LAYER TWO`.

The important documentary point is his direct 2006 WIRED statement that solvers had been **“missing a clue.”**

That establishes:

- `LAYER TWO` was something Sanborn wanted solvers to have;
- Sanborn himself called its absence the loss of **a clue**.

It does **not** establish:

- that `LAYER TWO` names a second cryptographic stage of K4;
- that “layer” means physical overlay;
- that K4 uses two alphabets, two ciphers, two panels, or two passes;
- that the clue points specifically to Layer A rather than the sculpture/riddle structure.

Therefore the current classification is **AMBIGUOUS**, not Layer A.

### 4.2 Coordinates / magnetic field / transmission / “buried out there somewhere”

These are plaintext-content features. Existing 2005 material already supports a distinction between deciphering the text and interpreting what that text refers to.

No direct source located in this pass says the coordinates, magnetic field, or burial wording are inputs to K4 encryption.

Classification: **Layer B unless new evidence says otherwise.**

### 4.3 K2 cipher and key reuse

No located direct Sanborn/Scheidt statement says K4 reuses `ABSCISSA`, the K1/K2 mixed alphabets, or the K2 Vigenère-family mechanism.

Classification: **NOT SUPPORTED as inheritance.**

---

## 5. K3 audit

K3 uses a transposition method and paraphrases Howard Carter’s opening of Tutankhamun’s tomb, ending with the question about seeing anything.

No direct source located in this pass says:

- K3’s transposition is reused inside K4;
- the Carter passage is a literal K4 key source;
- the discovery/excavation theme specifies a K4 transform;
- K3’s final question or punctuation gives a bounded K4 operation.

The thematic “uncovering/discovery” content is naturally compatible with Layer B, but even that is interpretation rather than a direct K4 inheritance statement.

Classification: **Layer B / ambiguous thematic relevance; no supported Layer-A inheritance rule.**

Cryptanalytic note: transposition combined with substitution/polyalphabetic families has already received substantial exact coverage in EXP-033/036/039. Pure transposition of K4 is now independently proved impossible by Checkpoint T.

---

## 6. The anomaly / misspelling audit

| Anomaly | Documentary status | K4 significance |
| --- | --- | --- |
| `IQLUSION` in K1 | Sanborn is reported/quoted as saying multiple misspellings are intentional; accessible source does not isolate a direct K4 instruction from this spelling | **Speculative / ambiguous** |
| `UNDERGRUUND` in K2 | part of the known anomalous plaintext; no direct K4 inheritance statement located here | **Speculative / ambiguous** |
| omitted `X` before `LAYER TWO` | **admitted construction error caused by an intentional aesthetic deletion**; Sanborn expected gibberish, not `ID BY ROWS` | the correction restores a clue, but clue target is **ambiguous** |
| `ID BY ROWS` | accidental meaningful-looking decryption caused by the omission, not intended plaintext | **Do not use as a K4 clue** |
| `LAYER TWO` | intended plaintext; Sanborn explicitly says solvers had been missing a clue | **Real clue, but Layer A vs Layer B unresolved** |

This table is important because it prevents the project from treating every anomaly as intentional cryptographic machinery.

---

## 7. New direct Layer-A evidence from Scheidt (2015)

The public transcript of the 24 October 2015 Kryptos workshop records a direct question asking whether K4 is one-stage like K1–K3.

Scheidt answers that he would consider K4 **more than one stage**, then immediately refers to the masking technique that prevents ordinary English statistics from being available to the solver.

This is stronger than simply inferring multiple layers from “riddle within a riddle.” It is **direct Layer-A evidence** from the cryptographer who supplied the process.

The same workshop also contains broader remarks about substitution, transposition, mixing/matching principles, and building layers. But those remarks are examples/general cryptographic discussion; they do not freeze a specific K4 pipeline.

### What this changes

**Strengthened:**

- K4 should not be modeled as a single untouched classical operation unless that operation itself naturally contains multiple stages in Scheidt’s sense.
- The “masking” operation is part of Layer A, not merely Layer B semantics.
- Multi-stage composition remains documentary-motivated even after Checkpoint U correctly demoted “riddle within a riddle” as evidence for cipher stacking.

**Not established:**

- two stages exactly;
- which stage is first;
- substitution + transposition specifically;
- fractionation + substitution;
- a reused K1/K2 method plus one extra mask;
- K3 transposition + another stage;
- any named family;
- any key or parameter source.

Therefore this evidence is important but **insufficient to define EXP-040**.

---

## 8. Layer A / Layer B classification summary

| Candidate clue/inheritance | Classification | Reason |
| --- | --- | --- |
| K1 light/shadow wording | **NOT ACTUALLY SUPPORTED as Layer A** | no direct inheritance statement found |
| `IQLUSION` | **AMBIGUOUS** | intentional anomaly; K4-link wording is reporter-level |
| K2 coordinates / buried language | **Layer B** | plaintext semantics / location theme |
| `LAYER TWO` | **AMBIGUOUS, genuine clue** | Sanborn directly calls the missing material a clue, but target is unspecified |
| K2 Vigenère-family method / ABSCISSA | **NOT SUPPORTED as inheritance** | no direct reuse statement found |
| K3 Carter/discovery content | **Layer B / ambiguous theme** | no method inheritance statement |
| K3 transposition | **NOT SUPPORTED as inheritance** | no direct reuse statement found |
| “first three contain clues to K4” | **AMBIGUOUS as to layer** | repeated reporter attribution, direct quote not located |
| Scheidt 2015 “more than one stage” | **Layer A** | direct process statement |
| Scheidt masking technique | **Layer A** | direct process statement, also supported in 2005 |

---

## 9. Comparison against EXP-001…039

The evidence does **not** justify rerunning old families.

Already-covered obvious interpretations include:

- K1/K2-style periodic shift/polyalphabetic mechanisms;
- reuse of published KRYPTOS/PALIMPSEST/ABSCISSA material in the tested scopes;
- K3-like transposition families;
- substitution/transposition compositions;
- standard Porta and several related shift-family constructions;
- double columnar transposition using the committed keyword corpus;
- row-boundary reset variants;
- artistic referents as direct keystream sources.

The 2015 multi-stage statement tells us the surviving architecture is likely composed, but the space of possible composed hand ciphers remains unbounded without one more structural fact.

That is a **model-selection problem**, not a compute shortage.

---

## 10. Request 7 result

**No new public, position-specific K4 plaintext letter was found outside:**

- `EASTNORTHEAST`
- `BERLINCLOCK`

Request 7 remains open.

---

## 11. Unresolved questions

1. What exact Sanborn wording lies behind WIRED’s repeated 2006/2010/2014 statement that K1–K3 contain clues to K4?
2. When Sanborn called `LAYER TWO` a clue, did he mean:
   - a clue to K4’s encryption mechanism;
   - a clue to the post-decryption riddle;
   - the sculpture’s physical/semantic layering;
   - something else?
3. In Scheidt’s “more than one stage” description, is “masking” a separate stage composed with a known classical system, or an internal feature of one broader process?
4. Did Sanborn modify Scheidt’s supplied multi-stage process after the handoff, and if so, where in the sequence?

These are exactly the kinds of questions the unedited Zetter/Scheidt material could answer.

---

## 12. Recommended next cryptanalytic interpretation task

Do **not** create EXP-040 yet.

The next reasoning task should take the now-stronger Layer-A statement:

> K4 is **more than one stage**, with a masking technique involved,

and audit EXP-001…039 specifically for **which two-stage / multi-stage hand-executable architecture classes remain genuinely uncovered**.

The purpose is not to search them immediately. The purpose is to produce a residual matrix:

- documentary support;
- stage count/order assumptions;
- whether the mask is pre- or post-encryption;
- exact existing experiment coverage;
- whether the 24 crib letters can falsify the class;
- whether any family is bounded enough to become EXP-040.

A valid outcome remains **NO EXP-040 JUSTIFIED**.

The external evidence priority remains:

1. unedited 2005 Zetter/Scheidt interview material;
2. original/full 1991 ABC Scheidt footage;
3. any direct Sanborn source behind the “first three sections contain clues to K4” reporter wording;
4. any additional public position-specific K4 plaintext disclosure satisfying Request 7.

K4 remains unsolved.
