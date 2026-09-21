# Checkpoint X — 2015 Scheidt workshop stage-order audit

**Branch:** `claude/k4-post-j`

**Purpose:** determine whether the 24 October 2015 Ed Scheidt workshop resolves the forward order or role of K4's masking stage strongly enough to justify EXP-040.

**Result up front:** **NO EXP-040 JUSTIFIED.** The workshop strengthens that K4 is multi-stage and that masking is part of Layer A, but it does **not** establish whether masking occurs before or after the other cryptographic stage(s). The explicit stage-order question near the end of the workshop received no clear answer in the surviving public transcript.

## 1. Source and access discipline

Primary recording cited in the literature:

- Klaus Schmeh, `2015-10-25-Kryptos Workshop`
- YouTube ID: `25YFYKKKkDo`
- HistoCrypt 2021 cites the recording directly at approximately 45:04.

Public transcript:

- Richard Bean transcription, published by Klaus Schmeh / Cipherbrain as `Kryptos workshop transcript`.

Cross-check sources used:

- HistoCrypt 2021, *Cryptodiagnosis of Kryptos K4* proceedings paper, which independently cites Scheidt's 2015 statement that K4 is "more than one stage" and points to the workshop recording.
- WIRED 2005 direct Scheidt interview on the masking technique.
- PBS/NOVA 2007 transcript for how concealment was publicly explained at the time.

### Tooling limitation

The current research environment could identify and source the original video, but could not stream or directly inspect the audio track. Therefore **no claim below is presented as a new audio correction**. Exact wording is taken only from the public transcript where the transcript is clear, and ambiguous portions remain ambiguous.

This checkpoint therefore answers a narrower but still useful question: **does the available workshop record itself justify fixing a stage order?**

It does not.

## 2. Relevant workshop chronology

### ~7:09 — masking suppresses the solver's initial English-language tools

Scheidt explains that ordinary cryptanalytic approaches use letter periodicity/frequency and says that with "a mask of some type" the solver no longer has that as the initial tool. He then discusses the mathematics associated with cryptography, including substitution and transposition, and says those still tend to carry the weight of the language.

### What this supports

- The mask is intended to suppress ordinary language statistics.
- Scheidt conceptually distinguishes the masking effect from familiar substitution/transposition principles.
- The solver may need to deal with the mask before ordinary language-statistical attacks become useful.

### What this does **not** support

It does **not** fix forward encipherment order. "First step" language in this passage is spoken from a solver/analysis perspective and cannot safely be converted into:

`plaintext -> mask -> cipher`

or

`plaintext -> cipher -> mask`.

Either forward order could produce a reverse-solving process in which the mask must be handled first.

## 3. ~39:06–40:33 — Scheidt did not verify final K4 implementation

Scheidt says he worked backwards to plaintext on the earlier sections but intentionally stayed away from K4. He describes the possibility that Jim added "some things" or "another step" after being shown the tools, and says the project ultimately belonged to Jim.

### Durable implication

Even if Scheidt's own intended procedure were reconstructed exactly, **the final sculpture may contain a Sanborn-added modification or step that Scheidt did not verify**.

This is consistent with the 2005 WIRED interview, where Scheidt says he does not know what Jim ultimately did and that further masking was possible.

### Cryptanalytic consequence

This weakens any attempt to interpret Scheidt's generic examples as a complete frozen K4 recipe. His statements are best treated as constraints on the design class, not a full specification.

## 4. ~42:31–46:40 — design goals, hand execution, and period discussion

Scheidt discusses designing a secret that could have different levels of difficulty, avoiding unfair mechanisms such as obscure/extinct-language dependence, and balancing long-term difficulty with practical execution. The conversation explicitly distinguishes **executing** the system from **breaking** it and asks how much could be pencil-and-paper versus computer-assisted.

The discussion then turns to the meaning of a "period," sentence boundaries, and special characters.

### Durable implication

- Hand/pencil-and-paper executability remains a serious design prior.
- The procedure had to be teachable/recreatable, not a one-time unknowable construction.
- Period and symbol-handling were live conceptual issues in the design discussion.

### What is not justified

No period value, reset rule, sentence segmentation, or computer-dependent state machine is supplied. This passage cannot justify reopening periods 27–29, adding sentence resets, or inventing punctuation-state rules.

## 5. ~47:06–47:35 — the strongest direct Layer-A statement

Question: whether K1, K2 and K3 are one-stage encryption and whether that is also true of K4.

Scheidt's answer, in the public transcript, is clear enough on the durable point:

> he would consider K4 **more than one stage**.

He immediately refers to the previously public masking technique that makes English unavailable.

### What is established

- K4 is not best modeled as a single untouched one-stage procedure.
- Masking belongs to the cryptographic Layer-A story rather than only to the post-decryption riddle.
- Multi-stage architectures deserve higher prior weight than single-stage named ciphers.

### What is not established

- exactly two stages;
- whether the mask is a separate stage versus an internal substep of a broader process;
- stage order;
- whether one stage is substitution, transposition, fractionation, autokey, running key, etc.;
- whether any K1/K2/K3 method is literally inherited.

## 6. ~48:16–51:48 — plaintext clues do not automatically reveal the process

Participants discuss Sanborn releasing more plaintext words and the concern that more plaintext alone may still not reveal how to reverse the process.

Scheidt defers on the analytical consequence. He also says, to the best of his memory, that Sanborn selected among systems he had been shown and wanted to put his own artistic touch on the work.

At ~51:48 the transcript marks a phrase involving something like "polygram" / "polynomial" as unclear.

### Decision

The unclear phrase is **not admitted as evidence**. Without the audio it would be irresponsible to turn it into a polynomial, polygraphic, or algebraic hypothesis.

## 7. ~53:45 onward — explicit masking-order question

The transcript records an explicit question equivalent to:

> masking first then encryption, or the other way around?

The transcript's status is:

> **no clear answer**.

This is the exact question Checkpoint W needed answered.

### Consequence

The workshop does **not** resolve the forward order of the masking stage.

The order remains an open structural branch:

1. **pre-encryption concealment/masking**
2. **post-encryption masking/superencipherment**
3. a broader process in which "masking" is not cleanly separable into one external stage

None can be promoted above the others from the 2015 workshop alone.

## 8. Cross-check against WIRED 2005

Scheidt's 2005 interview says:

- the first three sections expose English statistics more readily;
- K4 disguises that;
- the masking technique may not be known;
- the solver needs to solve the technique before going for the puzzle;
- Scheidt did not later verify what Sanborn actually did.

This reinforces the 2015 interpretation but still does **not** fix forward stage order. "Solve the technique first" describes attack priority, not necessarily encipherment chronology.

## 9. Cross-check against NOVA 2007

The NOVA transcript publicly explains concealment as something that **could** happen before encryption. Jim Gillogly is quoted saying it could involve obfuscating the language before starting to encrypt, and the narrator gives examples such as removing vowels or using phonetic spelling.

Important provenance distinction:

- this is useful evidence for what "concealment" was understood to mean publicly;
- it is **not** a direct Scheidt statement that K4 specifically uses pre-encryption concealment;
- NOVA's explanation cannot be used to freeze K4 stage order.

Therefore the project's stage-order variable remains unresolved.

## 10. Implications for Checkpoint W

Checkpoint W identified several residual multi-stage shapes. This audit changes their ranking only slightly.

### Strengthened

- **Some genuinely multi-stage Layer-A architecture is strongly supported.**
- A model in which masking is simply ignored is now weaker than one that explicitly accounts for it.
- A future experiment should state which stage is being interpreted as the mask and why.

### Not strengthened enough for EXP-040

- `mask -> transposition -> mask`
- pre-encryption concealment + classical cipher
- base cipher + additive/superencipherment mask
- fractionation + outer mask
- transposition + autokey/feedback

All remain underdefined because the workshop gives no exact mask definition and no stage order.

## 11. EXP-040 gate

### Candidate A — pre-encryption concealment + known classical stage

Fails evidence/definition gate. The public record does not define what concealment operation is used.

### Candidate B — known classical stage + post-encryption mask

Fails the same gate. No exact post-mask family is named.

### Candidate C — test both orders over a large generic mask family

Rejected. This would convert an unresolved historical ambiguity into a large free-parameter search and would be post-hoc architecture fitting.

### Candidate D — infer a polynomial/polygraphic stage from the ~51:48 unclear phrase

Rejected. The transcript explicitly marks the wording uncertain, and the audio has not been independently resolved.

### Decision

**NO EXP-040 JUSTIFIED.**

The workshop supplies a strong structural fact — multi-stage + masking — but still withholds the one fact needed to make a finite experiment honest: **what the masking operation is, or how it is ordered relative to the other stage(s).**

## 12. Best next evidence

Ranked:

1. **Direct audio review of approximately 51:30–55:30 from the original workshop recording**, specifically the unclear `polygram/polynomial` phrase and the masking-order question.
2. Unedited Zetter/Scheidt 2005 material.
3. Original 1991 ABC Scheidt audio/video around the muffled "taking the standard" passage.

If the workshop audio yields a clear answer on either the mask definition or its stage order, Checkpoint W can be revisited immediately for a bounded EXP-040 candidate.

## 13. Contamination note

During web discovery, search results surfaced modern pages claiming or reproducing K4 plaintext/solution material. Those pages were not opened or used as evidence. This checkpoint uses only the public workshop record, historical interviews, and already admitted public clues.
