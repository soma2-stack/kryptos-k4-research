# New attack ideas

Ranked by expected value. Each entry states the mechanism, why it is not already
covered by `negative-results.md`, and the cheapest experiment that would kill it.
Ideas 1–5 have been implemented and run; 6–11 are specified but not yet run.

Status keys follow `CONTRIBUTING.md`: `negative`, `inconclusive`, `replicated`, `candidate`.

---

## 1 — Invert the problem: recover the *method* from a candidate plaintext

**Status: implemented, `k4lib/recover.py`, validated by EXP-005.**

Reporting around the November 2025 archive sale distinguishes the recovered *text*
from the *decryption method*: knowing what K4 says would not reveal how it was
enciphered. That inverts this repository's whole framing. Every experiment here
searches a mechanism space and scores the plaintext it produces. If a candidate
plaintext ever becomes available — from the archive, from a leak, or from an
independent solve — the correct move is the opposite: fix the plaintext, let it
force the keystream at all 97 positions, and read the structure straight off.

Twenty-four known letters cannot distinguish mechanisms. Ninety-seven can: a
period is visible immediately, an affine rule is a two-point fit, a running key
shows up as a keystream IoC near 0.066, a linear recurrence is a small solve.

`diagnose(plaintext, ciphertext)` does all of this in one call, under all 12
conventions. It should be the first thing anyone runs on any candidate plaintext,
including a wrong one — a *near*-correct plaintext will still show partial structure.

**Do not** invert this into evidence: a candidate plaintext that produces no
keystream structure is not thereby refuted, and one that does is not thereby
confirmed until the rule extends to all 97 positions.

---

## 2 — The `DIAWINFBN` +5 run marks a segment boundary at position 63

**Status: new observation, `inconclusive`, highest-value untested lead.**

The inherited notes record that `DIAWINFBN` shows five consecutive relations
`C[i+4] = C[i] + 5 (mod 26)` and that no mechanism explains it. Locating it
precisely changes its character:

```
positions with C[i+4] = C[i] + 5 :  22, 29, 55, 56, 57, 58, 59
the consecutive run i = 55..59 covers ciphertext positions 55 through 63
position 63 is the first letter of the BERLINCLOCK crib
```

The run does not merely sit near the crib. It **ends exactly on its first letter**.

Two readings, both testable:

1. **Segmentation.** K4 is not one homogeneous system but a concatenation of
   segments, with a break at 63. A regime change at 63 would explain both why the
   run stops there and why every global periodicity test in EXP-001 and EXP-003
   fails: a key that restarts mid-message is aperiodic when measured globally.
   *Test:* re-run EXP-001's period probes **per segment**, splitting at 63 (and at
   21, 34, 74) rather than across the whole text. A period that is invisible
   globally but consistent within `[34,63)` or `[63,97)` would be decisive. This is
   cheap and has not been done.

2. **Progressive key.** Under a Vigenère, `C[i+4] − C[i] = 5` with plaintext
   `P[i+4] − P[i] = d` forces `k[i+4] − k[i] = 5 − d`. A key that advances by a
   constant every four characters is exactly a progressive-key cipher (idea 6).
   The run would then be the key's arithmetic showing through a stretch where the
   plaintext happened to be locally flat. *Test:* under each convention, check
   whether the crib-forced keys satisfy `k[i+4] − k[i] = c` for any constant `c`
   across the crib spans.

The anomaly's reported significance (~0.00156, post-hoc adjusted) was never the
interesting part. Its **endpoint** is.

---

## 3 — Mengenlehreuhr lamp count as keystream

**Status: `negative` at full scope — EXP-002, 161,740,800 parameter sets.**

The `BERLINCLOCK` crib names the Berlin-Uhr. The recorded negative for "24-sector
World Clock geometry" concerns the *Urania Weltzeituhr*, a different clock, and
"World Clock tape as conventional key" uses a city tape as a Vigenère keyword.
Neither touches the lamp count, so this needed running. It is now closed for a
fixed-step readout with a free additive offset.

**Still open:** the 23-lamp *bit vector* as a bitstream (5-bit groups → letters),
and a non-uniform time step — e.g. one driven by the ciphertext itself.

---

## 4 — Complete transposition families, gated on key structure not language

**Status: `negative` for period ≤ 12 — EXP-003, 9,312 permutations, exhaustive.**

97 is prime, so `i → a·i + b (mod 97)` is a bijection for every `a ≠ 0`. The family
is *complete* at 96 × 97 = 9,312 permutations — every decimation and rotation of the
text, closed under inversion and composition. No sampling, no route-design taste
required.

The recorded negatives for 3×31 routes, 4×22 routes and optimised columnar searches
all gated on **plaintext readability**, which needs a language model and rewards
overfitting. Gating on **key periodicity at the cribs** needs neither and has a
false-positive rate of 26⁻ⁿ that can be stated exactly.

**Still open, and the obvious extension:** the same 9,312 permutations against a
*running* key (idea 5) or a progressive key (idea 6) instead of a periodic one.

---

## 5 — Running-key "mask" from the sculpture's own text

**Status: `negative` for verified sources, `inconclusive` for K1–K3 — EXP-004.**

Sanborn has described a masking technique. Every periodicity test here fails, and a
key as long as the message is precisely the construction that defeats periodicity
tests while leaving the cipher elementary. The long texts available to the sculptor
are the sculpture's own. Because both cribs must satisfy one alignment, a mask of
length *L* offers only *L* alignments — a tiny space for a 24-letter test.

K4's own ciphertext and the KRYPTOS alphabet are closed. K1–K3 plaintexts are
`inconclusive` only because `data/mask_sources.json` holds working transcriptions
marked `verified: false`; re-run once a primary transcript is committed.

**Still open and untested:** the **carved tableau itself** as the running key. The
sculpture's tableau is a large keyed block of letters, readable by row, by column,
by diagonal. It is the one long text physically present on the object that this
experiment has not consumed. `k4lib/alphabets.vigenere_tableau` already generates it.

---

## 6 — Progressive-key and lagged-generator ciphers (Gromark family)

**Status: specified, not run. Highest-priority unrun idea.**

Every negative in this repository shares a shape: they assume the key either repeats
(period ≤ 48) or is a fixed external text. The classical family that is neither is the
**progressive key** — the key advances by a rule each block — and its ACA-era relative
the **Gromark**, whose keystream comes from a lagged-Fibonacci recurrence over a short
numeric primer. These were standard in the cryptographic literature Ed Scheidt would
have drawn on, they defeat Kasiski and period tests by construction, and they are
*small*: a 5-digit primer is 100,000 keystreams.

This is also the only family that gives idea 2's `+5` run a natural mechanism.

**Experiment.** Enumerate lagged-Fibonacci keystreams over Z₁₀ and Z₂₆ for primer
lengths 2–6, all lag pairs, both additive and subtractive, × 12 conventions, gated on
all 24 crib letters. Well under 10⁹ and fully pre-registerable. `k4lib/recover.py`
already fits linear recurrences of order 1–2; extend to the generator direction.

---

## 7 — Audit the two-chart homophonic lead for degrees of freedom

**Status: specified, not run. Cheap, and it either kills or promotes an inherited lead.**

`research-state.md` reports that a two-chart homophonic interpretation had *no
contradictions* at the crib positions. Absence of contradiction is not evidence — it is
what a model with enough freedom always produces, and `data-conventions.md` warns about
exactly this. What was never computed is the **number of consistent selectors**.

**Experiment.** Build the constraint graph over crib positions implied by the 10
conflicting position-pairs, then count the 2-colourings consistent with them. If the
count is astronomical, the two-chart model is absorbing the constraints rather than
explaining them, and the lead should be demoted to `negative` on information-theoretic
grounds without any further cryptanalysis. If the count is small, the selector is nearly
determined by the cribs alone and becomes a strong, independently checkable prediction.

Either outcome is worth more than more searching. This should be run before any further
work on the parity / K0-Morse / rail selector leads, all three of which are the same
kind of claim.

---

## 8 — Per-segment statistics instead of whole-text statistics

**Status: specified, not run.**

K4's index of coincidence is **0.03608** (random ≈ 0.0385, English ≈ 0.0667). It sits
*below* random, which is itself mildly notable for a 97-character sample and consistent
with a long or non-repeating key. Every statistic in this repository has been computed
over the whole 97 characters. If idea 2 is right and the text is segmented, whole-text
statistics are averaging over regimes and destroying the signal. Recompute IoC, letter
frequency and lag-autocorrelation **within** `[0,21)`, `[21,34)`, `[34,63)`, `[63,74)`,
`[74,97)`.

---

## 9 — The bounded-source lemma as a standing filter

**Status: implemented as a reusable check — EXP-001.**

Eight of the 12 conventions require a key index of 24 or 25 somewhere in the cribs.
Any proposed key source whose values are bounded below 25 — a 24-hour clock, a 23-lamp
display, a 24-sector ring, a 0–23 counter, a 5-bit code with reserved values — is
therefore **falsified outright for those eight conventions, with no search at all**.

Run this check first on every future proposal. It costs nothing and it retired
two-thirds of the search space in EXP-002 before a single parameter was enumerated.

---

## 10 — Machine-readable physical transcript

**Status: not started; prerequisite for ideas 2, 8 and any physical-geometry work.**

`next-steps.md` item 4 remains correct and remains undone. Nothing in this repository
records the sculpture's line breaks, panel boundaries, tableau orientation or the
question-mark/misspelling handling that `data/mask_sources.json` is currently guessing
at. A segmentation hypothesis (idea 2) cannot be tested against physical structure
until that structure exists as data. **Do not** invent it — transcribe it from the NSA
primary reference in `sources.md`.

---

## 11 — What would actually settle this

Worth stating plainly, because this repository can drift into search for its own sake.
None of the searches above can succeed if the mechanism depends on information not
present in the ciphertext — and Sanborn has said the plaintext still requires field
work after decryption. The realistic paths to a solve are:

1. A candidate plaintext from the archive, run through idea 1. Cheap, decisive, and the
   apparatus for it now exists.
2. A correct guess at the *shape* of the mechanism — segmented, progressive, or
   running-key — narrow enough that 24 crib letters can confirm it. Ideas 2 and 6.
3. A primary-source fact about construction that removes a degree of freedom. Idea 10.

Enumerating more route families is none of these.
