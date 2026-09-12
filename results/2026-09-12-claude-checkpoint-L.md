# Checkpoint L — the panel above K4 is not its key, and a frontier appears

Branch `claude/k4-post-j`. Base for this checkpoint:
`ef082c80308c2fcc1d75dc0f559eaf28209de6ff` (the fulfilled evidence request).
Work committed at `afee4ac` and this checkpoint's commit. `main`,
`codex/k4-continuation` and `claude/dreamy-archimedes-79k6u0` untouched; no history
merged or rewritten. **K4 remains unsolved.** No plaintext candidate, no verifier
submission, no claimed mechanism.

## 1. Geometry correction — ACCEPTED, and verified rather than taken on trust

The supplied row strings were re-counted here before use. Every one matches the handoff's
own length table; rows 1–24 hold **29–33** characters (distribution 29:1, 30:5, 31:11,
32:6, 33:1); rows 1–24 = 745, rows 25–28 = 124, total 869; four `?`. So
**`32 + 27×31 = 869` gives the correct total but is a false description of the row
structure**, and I retract it going forward. Checkpoint K is not rewritten; this is the
supersession record. The same false claim in
`docs/external/perplexity-k4-geometry-correction-2026-09-12.md` is superseded too.

Three **independent corroborations** of the transcription passed, none of them assumed:

- rows 15–25 up to and including the terminal `?` hold 337 characters, i.e. exactly
  **336 K3 letters**, the standard K3 ciphertext length;
- row 25 after its `?` is exactly `OBKR`, and rows 26–28 equal `K4[4:35]`, `K4[35:66]`,
  `K4[66:97]` from `data/k4.json`, so K4 = 4 + 93 = 97;
- row 1 and row 15 are the canonical K1 and K3 ciphertext openings.

The rows are preserved with provenance and this verification record in
`data/cipher_side_rows.json`; the 869-character linear stream hashes to
`dde19b74d57e0d2b169466cdec2641eb8c87e30ce35b74f4c60c4a74ba413177`.

### A discrepancy of my own finding, left unresolved

Rows 1–14 supply **432 letters plus 3 question marks**. The commonly cited section
lengths K1 = 63 and K2 = 372 sum to **435 letters** — three more, for the same span.
Candidate explanations (the cited counts including separators or counting differently; the
CIA text version omitting three characters; K2 not ending at the row-14/15 boundary, which
row 15's canonical K3 opening disfavours) are recorded without choosing between them.
**Status: UNRESOLVED.** It cannot affect any model using only rows 15–28 or K4 itself; it
does bear on anything keyed to rows 1–14, so every such verdict below repeats the caveat.
Evidence Request 5 names what would settle it.

## 2. Does the correction change EXP-032, EXP-033 or EXP-034? — No, and this was tested

`audit/verify_geometry_correction.py` decides this per experiment by enumerating the
geometric quantities each one actually consumes, rather than by accepting an expectation:
**25/25 checks pass.**

- **EXP-032 — unchanged.** Its geometry table names only rows 25–28; it embeds no row
  1–24 string; row 25 columns 28–31 hold `OBKR` in the authoritative transcription; and no
  crib lies in row 25, so no crib column depends on the `OBKR` indent. 12/12
  contradictions stand.
- **EXP-033 — unchanged, F3 included.** F1 and F2 are abstract rectangles over K4's 97
  letters with no panel geometry at all. **F3 was checked cell by cell:** its engraved grid
  references exactly rows 25–28, covers all 97 K4 positions and nothing else, puts
  positions 0–3 at columns 28–31 matching `OBKR`, puts rows 26–28 at columns 1–31 matching
  the authoritative row strings, and **never uses a column beyond 31 or a row below 25**.
  So F3 did *not* depend on a uniform full-panel 31-column assumption, and its elimination
  stands. 175,820,784 cases, zero feasible.
- **EXP-034 — unchanged.** Verified by parsing the module rather than by string-matching:
  it imports no geometry module, opens no panel data file, and defines no row or column
  map. Its sources are K4's own ciphertext and the crib plaintext. 2,676 decided, zero
  feasible.

One thing *did* need fixing: **EXP-032's own printed cross-check asserted the false
`32 + 27*31 == 869`.** That line is corrected in place to the real row-length table; the
experiment's 12/12 contradiction result is unchanged. I am not weakening any unaffected
negative, and I am not leaving a false assertion in code that passes.

## 3. Physical vertical alignment — NOT recoverable, and now positively disfavoured

Searched the repository for offsets, drawings, templates, surveys or orthographic imagery.
What exists: `data/physical.json → panel_layout` is `CONFLICTING REPORTS / LOW`;
`k4_grid` is `DISALLOWED-SOURCE / UNVERIFIED`; and — decisively —
`engraving_line_lengths` records at MEDIUM confidence *"vary, not a uniform grid … Sanborn
kerned the lettering for aesthetics; fixed-width spacing was avoided."* No orthographic
photograph, fabrication drawing, punch template or survey is in the repository, and
outbound web access is refused.

The new evidence does more than leave the question open. **With a monospaced punch and a
common physical row width, every row would hold the same number of characters.** Rows 1–24
hold 29–33. Therefore either the physical row width varies by row, or the letter pitch
varies by row — and between a 29- and a 33-character row the pitch would differ by
**13.8%**, so character centres in different rows would not sit above one another except
by coincidence. That is the kerning the repository already recorded, now corroborated by a
grade-A source.

**Grade: STRONGLY DISFAVOURED, not disproved** — the copper screen is an S-curve and the
panel layout itself is recorded as conflicting, so "row width" is not perfectly defined
without an image.

**So the physical `row − k, same column` architecture is PARKED.** I did not build three
alignment lattices to test it: given that the evidence now argues against any common
lattice, preregistering lattices would be rescuing the idea rather than falsifying it.
Checkpoint K's description of that model as "parameter-free" is withdrawn.

Evidence **Request 4** states the one cheap observation that would settle it: *is the right
edge of the engraved cipher text ragged or flush?* Ragged means constant pitch and
row-local index **is** a physical column; flush means variable pitch and no lattice. A
typeset transcription cannot answer it; it needs an image or a drawing.

## 4. New preregistration — EXP-035, committed before implementation

`docs/exp035-preregistration.md`, committed at `afee4ac` ahead of any code. It uses only
what the new source is authoritative for — **row content and reading order** — and states
in advance why the physical model is absent, the exact streams, the three question-mark
rules, both index maps, the no-wrapping requirement, the constraint threshold, the control
design, the verifier, and the prohibited expansions.

Model: `k[i] = f(S[g(i)])`, `f : Σ → Z26` **any** function, never enumerated — every
function decided exactly by consistency, so key alphabet is not a parameter.

Motivation: Checkpoint K ranked "a long key from an *unidentified* external source" first
and said it could only move when a source was **identified**. The fulfilled request
identifies the most physically obvious candidate in existence: **745 characters engraved
directly above K4 on the same object**, public since 1990, cut by Sanborn himself.

One sub-family, **G2 (same row-local index, k rows above)**, is declared explicitly as a
**text-order** family and not a physical claim, with its asymmetry fixed in advance: a
negative across all three index conventions kills the rule *as a text rule* whichever
alignment is physically true, while a positive would be **uninterpretable** without
Request 4 and would not be promoted.

## 5. EXP-035 result — NEGATIVE

| | |
|---|---|
| cases decided | **43,824** (G1 linear 42,096; G2 row-local 1,728) |
| duplicate windows deduplicated | 80,952 |
| CONTRADICTION | **41,412** |
| BLOCKED by a `?` under the `block` rule | 2,412 |
| UNDECIDED for lack of constraint | **0** |
| **FEASIBLE** | **0** |

Constraint counts run **4 to 16** per case — every single case cleared the preregistered
decidability threshold, which is why nothing is undecided. 4,188 cases carry 12
constraints (chance survival 1.0 × 10⁻¹⁷) and 24 carry 16 (2.3 × 10⁻²³).

Streams that are *spans* of a longer stream contribute no separate cases: every `k12`
window is an `above` window, and `k3` and the rows-1–24 part of `full28` likewise, so they
are deduplicated by realised symbol tuple rather than re-tested. Their windows are
covered — under the stream that first supplied them.

**Controls.** G1: 36/36 planted positives detected with `f` recovered on every constrained
symbol, 36/36 adversarial corruptions flipped the verdict. G2: 15/15 and 15/15. Every
adversarial control was *capable* of changing the verdict by construction — the corrupted
position is drawn from a source symbol occurring at two or more constrained positions, and
cases with no such symbol are reported as "not counted" rather than counted as passes.
Zero were not counted. This follows the EXP-033/034 lesson directly.

**Independent verification.** `audit/verify_exp035.py` imports neither the experiment nor
`k4lib`; it rebuilds the rows, the 12 conventions, all six streams and both index maps
from first principles and re-decides **all 43,824 cases**: **14/14 checks pass**, every
verdict, constraint count and constrained-position count agreeing. It additionally asserts
that **no G1 window wraps** (EXP-029's audited defect), that deduplication is sound, that
constraint counts are **verdict-independent** (the EXP-034 invariant, tested not assumed),
and it replants its own positives so a rubber-stamp verifier is excluded.

### Exact model-limited elimination

**No key that is an arbitrary function of a single symbol of the authoritative
cipher-side text — taken at a fixed linear offset with no wrapping, or at the same
row-local index a fixed number of rows above — can produce K4 from a plaintext carrying
the public cribs, under the 12 committed shift conventions.** Because `f` was decided
rather than enumerated, this covers every key alphabet and every non-injective symbol map
at once.

Not touched: functions of two or more source symbols, position-modulated `f`, mid-message
resets, non-shift combiners, transposition-composed or fractionating architectures, and
every physically-aligned model. Verdicts touching `k12` inherit the unresolved
432-vs-435 discrepancy.

**This is a real loss for the leading hypothesis, not a neutral result.** The one
architecture carrying most of the probability mass could only advance by identifying a key
source; the new evidence identified the best candidate there is, and it fails.

## 6. A frontier I had not stated, and it reframes the whole negative corpus

Four experiments now eliminate the *same shape* of model — `k[i] = f(one symbol of a named
source at a fixed index)` — against every source this repository can name: the frozen CET
clock tape (EXP-030), the multi-face clock arc (EXP-031), K4's own ciphertext at any lag
(EXP-034), and the engraved panel text at any offset (EXP-035). That pattern says either
the source is still unidentified, or **the architecture is not a single-symbol lookup at
all.**

And there is an assumption underneath all of it that I have never stated plainly:
**every experiment in this repository uses the same 12 conventions, which are shift
families over exactly two indexing alphabets, STD and KRYPTOS.** The "arbitrary `f`" trick
absorbs the *key* alphabet completely — but not the plaintext and ciphertext alphabets. So
the entire negative corpus is conditional on indexing by STD or KRY.

That matters because K1 and K2 demonstrably use **keyed mixed alphabets** derived from
keywords. A shift in a mixed alphabet is not a shift in STD.

The frontier, stated honestly: admit *arbitrary* mixed alphabets on both sides together
with an arbitrary `f`, and the model becomes `C[i] = T(P[i], S[g(i)])` for a nearly
arbitrary 26×26 table — **unfalsifiable**, exactly the wall EXP-011 mapped. The family is
only testable if the alphabets come from a **precommitted small motivated set**.

## 7. Surviving architectures, re-ranked

| rank | architecture | change since Checkpoint K | falsifiable now? |
|---|---|---|---|
| 1 | Keystream families **re-tested under keyword-derived mixed alphabets** | **NEW, promoted to first.** Tests whether the whole negative corpus is an artefact of STD/KRY indexing. Motivated directly by K1/K2's keyed alphabets | **Yes**, if the keyword list is precommitted from published K1–K3 keywords only |
| 2 | Long key from a still-unidentified external source | **Demoted.** Its best identified candidate just failed | No — needs evidence naming a source |
| 3 | Full-26 fractionating construction (fractionate on one grid, recombine on another) | unchanged; EXP-012's coverage argument does not reach it | Only after a specific construction is named |
| 4 | Substitution ∘ keyed transposition, width ≥ 12, key from the published keyword corpus | unchanged | Yes, as a small precommitted key family |
| 5 | Two-symbol or position-modulated text-dependent keys | unchanged; compute constraint density first | Marginal — counts will fall |
| 6 | Physical panel alignment models | **parked**, and now disfavoured | Blocked on Request 4 |
| 7 | Clock-as-index / semantic inner layer | unchanged | No — no mechanism stated |

## 8. Highest-information next action

**Re-test the exact-consistency families under a precommitted set of keyword-derived mixed
alphabets** (rank 1). It is cheap, it is motivated by the only two sections whose method is
known, and its information content is unusual: a negative would show the repository's
large negative corpus is robust to the indexing assumption, while a positive would
identify the assumption as the flaw in four sessions of work. Either outcome is worth
more than another source hunt.

Discipline it requires, fixed before implementation: the alphabet list must be derived
only from **published** K1/K2/K3 keywords and the Kryptos alphabet — no alphabet may be
added after seeing a result — and the decidability of each family must be computed before
execution so we do not manufacture undecided cases.

## 9. External evidence requests

- **Request 4 (new, decisive for the parked model):** one straight-on photograph, drawing,
  punch template or survey of the cipher side showing whether the right edge is ragged or
  flush, whether row left edges share an x, and whether pitch is constant.
- **Request 5 (new, minor):** a primary character count of K1 and K2 *ciphertext*, to
  settle the 432-vs-435 discrepancy.
- **Request 1: fulfilled**, with the correction accepted above.
- Requests 2 and 3 (unedited 2005 Zetter/Scheidt material; a target-era Weltzeituhr frame
  from a different bearing) carried forward unchanged and still lower priority.

## 10. Reproduce this checkpoint only

```sh
python audit/verify_geometry_correction.py
python experiments/exp032_column_key.py
python experiments/exp035_panel_running_key.py
python audit/verify_exp035.py
```

EXP-024 remains frozen. EXP-029, EXP-030, EXP-031 and EXP-033 were not rerun, and nothing
here depends on reproducing them.
