# Canonical current status — read this first

This is the compact handoff for future sessions. It does **not** replace historical checkpoints.

## Prospective canonical update — 2026-09-21

**K4 remains UNSOLVED.** The authenticated plaintext constraint set is unchanged at 24 letters:
zero-based `[21,34) = EASTNORTHEAST` and `[63,74) = BERLINCLOCK`.

Since the historical AE–AL frontier was written, four bounded experiments have run on the Claude
continuation branch and are now part of the canonical prospective state:

- **EXP-040:** registered propagating one-tap text-autokey / feedback families — exhaustively negative.
- **EXP-041:** registered additive two-tap plaintext feedback — exhaustively negative with full
  infeasibility-certificate coverage.
- **EXP-042:** registered mixed plaintext/ciphertext two-tap feedback — exhaustively negative;
  the simple feedback corridor is provisionally exhausted at the tested scopes.
- **EXP-043:** K1–K3-derived `M2 . pi . M1` search using the faithful prime-length affine-mod-97
  surrogate for K3's recovered transposition principle — 15,197,184 configurations, zero feasible,
  independently verified.

The organising discrimination theorem is now:

`log26(N) + d_eff < 24`

with `d_eff` the effective rank of parameter influence on the 24 authenticated crib values.
Every surviving class is presently either underdetermined by the 24 letters or discriminating but
lacks an independently selected parameter. The productive bucket — **motivated and discriminating** —
is currently empty. New authenticated information is higher-value than another unconstrained family.

**Checkpoint AM:** the reported 2015 workshop exchange “Would you consider it periodic?” / “Yeah.”
remains **UNRESOLVED** and is **not** admitted as evidence. The primary audio was unreachable from the
Claude environment, so no audio was assessed and speaker/referent/polarity remain unauthenticated.
Authenticated workshop evidence remains only: K4 is **more than one stage**, and masking is part of
Layer A. No period, period value, reset rule, or schedule is licensed.

Generic modern K4 clue searches now risk surfacing solution-dump contamination. Prefer named
primary-source domains and preserve the existing contamination firewall.

**Checkpoint AN / AO:** the Wilson-attributed Scheidt phrase “a piece relating to Stego” is now a
**C-grade provenance-limited lead, not an authenticated K4 constraint**. The original communication,
metadata, underlying 2004 talk record, and independent contemporary corroboration were not recovered.
It may guide provenance work, but it selects no carrier, method, stage order, period, key length,
alphabet, reset, recurrence, or alignment and does not justify EXP-044.

**Historical cryptanalytic baseline:** Checkpoint AE
(`results/2026-09-13-checkpoint-AE.md`), the **K4 decidability census**
(`docs/analysis/k4-decidability-census.md`): a per-class account of what the 24 verified crib
letters could falsify at that checkpoint. Its gate logic remains binding, but later prospectively
registered EXP-040 through EXP-043 have now executed at their documented scopes. Read the census
before proposing any family - it exists to prevent another post-hoc selection, and it carries
the reduction rules that reject duplicate "new" families before any code is written.

Headline findings: the crib letters are two contiguous runs, so a shared periodic schedule gets
**zero** constraints at periods 27-29 and only 5/3/1 at 24-26; **no plaintext block repeats** at
size 2, 4 or 5 at any alignment, which is why free polygraphic inner stages are vacuous even
behind a bounded outer map; an arbitrary 26x26 table receives **zero** constraints at key
periods 8, 10, 13 and 26. Request 7 is now targeted: **48 of 73 unknown positions unlock all
three blind periods**, the best single positions being **1, 3, 91, 93, 95, 96**, while exactly
**20, 47 and 74** unlock none. One scattered letter helps the periodic and mask classes a great
deal; only a **contiguous run** can rescue the polygraphic ones.

**Correction to AA and AC recorded at AE:** disconnection of the two-mask bipartite graph
*raises* the constraint count, not lowers it, so `24 - (p+q-1)` is a **lower** bound. No
conclusion changes.

## Evidence-acquisition status (prospectively reconciled at Checkpoint AG)

**Historical note:** at the AG reconciliation stage, AE remained the cryptanalytic checkpoint and
no EXP-040 was then justified. See the 2026-09-21 prospective update above for the later state.

Request 2 is split into two distinct states, and both must be reported separately:

1. **`ScheidtNova.doc` - LOCATED via public index metadata; actual payload NOT RECOVERED.** The
   filename, 2005 filming date, PBS B-roll description, ~140K size and 2009-02-13 posting date
   are established from the public index. The live payload is inaccessible and its underlying
   server-side status is unknown. **Do not canonize any one HTTP failure mechanism.** No wording
   may be quoted, paraphrased or inferred from it - not from the filename, not from index
   metadata, and not from search-engine snippets.
2. **Unedited 2005 Kim Zetter / WIRED Scheidt material - NOT LOCATED.** The published WIRED
   interview states it was edited for length and organization; the unedited version has not been
   found and is **not** claimed to be publicly available.

The GBH Open Vault identifier `V_3AC501960CC4454A8FD950703CBED5A9` resolves to AAPB record
`cpb-aacip-15-1615gc34`: the 56:46 Digital Betacam **Green Label Master** of NOVA ScienceNow
episode 3411. This is the broadcast master, not evidence of a complete Scheidt interview,
B-roll transcript, logging transcript, outtakes or production notes. The proposed UGA / Peabody
`Nova scienceNOW [No. 3411, 2007-07-24]` object is **not independently verified** and remains a
search-result lead only, not a confirmed catalog holding.

The PBS explanation that concealment can occur before enciphering is narrator/editorial language,
not a Scheidt statement fixing K4 stage order. Requests are already pending with **GBH, Kim
Zetter, TecSec / Ed Scheidt, and Elonka Dunin**. Do not send duplicate outreach.

## Scope clarification (Checkpoint AF) - do not over-read the periodic negative

Checkpoint AE writes class B as `C[i] = F(P[i], k[i mod p])`. That notation is generic, but the
**ALREADY CLOSED** verdict at `p <= 23` covers only the **declared shift/combiner families** - the
12 committed conventions swept by EXP-001 and EXP-036, plus the Quagmire/Gronsfeld reductions and
EXP-037 for standard Porta. It is **not** a theorem eliminating every arbitrary periodic combiner.

An arbitrary fixed 26x26 table is **class L**, and under the present cribs it is *vacuous* at key
periods 8, 10, 13 and 26, receiving **zero** constraints because no `(plaintext, key)` input pair
repeats there. A short period therefore does not by itself close an arbitrary combiner: class L is
blocked by lack of constraint, not by prior search.

## Documentary reconciliation (Checkpoint AG)

Checkpoint AG (`docs/analysis/checkpoint-AG-evidence-to-census-reconciliation.md`) audited 18
relevant documentary statements against every affected AE census class. **No overlooked
operational parameter was found.** Multi-stage, masking, historic basis, custom/adapted design,
and possible Sanborn changes remain class-level filters; none supplies a transform, stage order,
period/key length, reset/alignment rule, tableau, recurrence, or parameter-sharing rule.
**No previous cryptanalytic conclusion changed and no EXP-040 is justified.**

**Previous cryptanalytic checkpoint:** Checkpoint AC
(`results/2026-09-13-checkpoint-AC.md`) — independent audit of Codex Checkpoint AB plus exact
CSP closure of its Trifid residual: **`NO EXP-040 JUSTIFIED`**. Codex's 175-of-194 rejection
count and both 19-configuration remainder lists reproduced exactly. Of the 19, **15 SAT,
4 UNSAT, 0 incomplete**; the conditional fixed-bijection Trifid residual is **narrowed, not
closed**, and a SAT result is **not evidence for Trifid** — it is what the falsifiability
budget predicts from 45-48 free ternary classes against 24 crib letters.

**Verification status (Checkpoint AD, `results/2026-09-13-checkpoint-AD.md`).** AC's four UNSAT
results now carry **independent exhaustive verification**. The three search-based cases are
re-decided by the verifier's own DFS over independently rebuilt classes and constraints
(16 / 44,677 / 403 nodes), not by replaying the solver's trace; `p=11`
row-reset keeps its directly re-derived pigeonhole. The refutation traces are retained as a
supplementary record only. 142 checks pass, including from a clean checkout. No cryptanalytic
conclusion changed.

**AC-Result 1 — refines the AA corollary.** Bounding the outer stage is **necessary but not
sufficient**. With the outer map pinned to the identity, a free inner map on digraphs still
imposes zero constraints, because the 11 crib digraphs and their 11 ciphertext images are each
all distinct. Constraints return only when the outer stage is bounded **and** the inner stage
is structured — one parameter set shared across many positions. **Parameter sharing, not stage
bounding, is what generates constraints.**

**AC-Result 2 (T-determinacy).** Under a fixed injective readout, inverting a coordinate-row
fractionation makes the entire plaintext coordinate array a function of the readout alone: the
unknown plaintext letters contribute no independent freedom. This is the reduction that makes
such families finite and small.

**Previous cryptanalytic checkpoint:** Checkpoint AA
(`results/2026-09-13-checkpoint-AA.md`), the residual multi-stage architecture elimination:
**`NO EXP-040 JUSTIFIED`**. It builds on Checkpoint T's constraint-first pass
(`results/2026-09-12-claude-checkpoint-T.md`) and Checkpoint W's residual map.

## The falsifiability budget (Checkpoint AA) — apply this before proposing any architecture

**AA-Theorem 1 (erasure).** If the chain ends in a position-varying monographic mask whose
parameters over the cribs are free, and the inner stage is a free map on blocks, the
architecture fits the cribs for *every* mask, provided no two observed plaintext blocks are
equal. Invert the mask to get the intermediate text, then assign the inner map on distinct
arguments.

**Corollary.** An architecture is testable only if
`(free mask parameters over the cribs) + (free inner parameters exercised) < 24`.
Every stage added to a chain spends from a fixed budget of 24. This is the countable form of
Checkpoint T's finding that constraint density, not compute, is the binding resource.

**Consequence for scope.** Every crib-based proof in this repository *necessarily* describes
the observable end-to-end map. Internal-stage proofs are impossible in principle while the
outer stage is free. Do **not** propose rescuing a rejected cipher as a hidden inner stage;
bound the outer stage first.

**Closed at Checkpoint AA as VACUOUS (zero constraints, not merely untested):**

- a free digraphic, 4-graphic or 5-graphic inner stage behind a free mask - every block lying
  wholly inside a crib is distinct at every alignment, so *no* result could falsify it. This
  covers Playfair, Bifid at period 2 and Hill 2x2 as hidden inner stages.
- transposition composed with a feedback/autokey mask - with unknown `pi` the lagged source is
  an unknown intermediate symbol at every crib position; with known `pi` it reparameterises
  EXP-034/EXP-038 over the EXP-036 permutation corpus.

**Exactly REFUTED at Checkpoint AA:** a free trigraphic inner stage under a periodic additive
mask of period 1, 3 or 9. The repeated trigrams `EAS` (21/30) and `AST` (22/31) sit at distance
9, so such a mask would force a ciphertext repeat that is absent. Three periods is the complete
extent of what the current cribs can say about any hidden polygraphic stage.

**Strongest surviving architecture:** the sandwich `M2 . pi . M1`, the only class that survives
purely because a non-commuting permutation separates two masks. Its bipartite constraint system
yields `24 - (p + q - 1)` independent constraints - only **7** at the K1/K2 pair (8, 10). It
fails EXP-040 gate condition 5: no source states any period, key, or inheritance from K1/K2.

**Current documentary checkpoint:** Checkpoint U (`results/2026-09-12-claude-checkpoint-U.md`),
the 2025 Sanborn public-clue audit: also **`NO EXP-040 JUSTIFIED`**.

## The two-layer model (Checkpoint U) — apply this before proposing anything

- **Layer A** is the map from 97 plaintext letters to the 97 K4 ciphertext letters. It is the
  only layer this repository can test, and the only one whose failure keeps K4 unsolved
  cryptographically.
- **Layer B** is whatever the recovered plaintext then instructs the solver to do.

Sanborn documents the split himself: the 2005 Zetter interview is sequential — decipher the
piece *and then* go and find the place — and the 2025 statement that K4 "has been discovered
and it points in the direction of K5" makes the same division. Layer A is unsolved while
Layer B is already in three people's hands.

**`BERLINCLOCK` is a plaintext word.** The November 2025 clarification that it means the
Weltzeituhr rather than the Mengenlehreuhr is Layer B semantics. It is **not** a statement
that clock geometry is a keystream source, and it never was.

**Therefore:** Weltzeituhr, Mengenlehreuhr, Morse material, compass/bearing language, Egypt
and the Berlin Wall are **Layer B referents**. Their use as Layer A keystream, mask or route
sources is demoted from DOCUMENTARY-MOTIVATED to **SPECULATIVE**. The negatives of EXP-002,
EXP-018, EXP-023, EXP-024, EXP-029, EXP-031 and EXP-035 all stand unchanged; what changes is
that this class must **not be revived** — it now fails gate condition 1 outright.

"riddle within a riddle" most naturally describes **Layer B nesting**, not nested cipher
stages, and should no longer be cited as support for multi-stage composition. Scheidt's
1991/1999 Layer A statements and Checkpoint S's four-process reading of K1-K4 are untouched.

**Provenance caution:** every 2025 clue is graded no higher than **C+/B-**, because no
primary source was reachable from this environment. Do not make any 2025 clue load-bearing
until it is verified against the original letters and reporting.

**Documentary work completed after R:** Box 6 Folders 8, 9, 10 and 11, plus Series 9 Box 16 Folder 2, have all been inspected. Checkpoint S2 (`results/2026-09-12-claude-checkpoint-S2.md`) re-evaluated the 1991 ABC Scheidt interview: "custom / adapted" is now STRONGLY SUPPORTED, but no architecture is named and **no EXP-040 is justified**.

**K4 remains unsolved.**

## Verified K4 anchors

Use the published positional cribs exactly as:

- zero-based `[21,34)` = `EASTNORTHEAST`, ciphertext `FLRVQQPRNGKSS`
- zero-based `[63,74)` = `BERLINCLOCK`, ciphertext `NYPVTTMZFPK`

See `docs/external/checkpoint-O-public-crib-primary-verification.md`.

## Cryptanalytic state

Do **not** rerun EXP-029 through EXP-039 merely for reassurance.

Important current scoped negatives include:

- **Pure transposition of K4 is PROVED IMPOSSIBLE** (Checkpoint T). The cribs require at
  least three `E`s in the plaintext; the ciphertext has exactly two, and a permutation
  preserves the letter multiset. This upgrades EXP-007's statistical argument. It does
  **not** reach substitution-then-transposition, nor a transposition spanning K1-K4.
- **The cribs impose ZERO constraints on message-aligned periods 27, 28 and 29**, and only
  5 / 3 / 1 on periods 24 / 25 / 26 (Checkpoint T). A "consistent period" reported in that
  window is **vacuous and must never be counted as a survivor**. This is an
  information-theoretic ceiling, not a gap in effort.
- Physical row-boundary key resets are negative: EXP-020 on the correct geometry, replicated
  and extended at Checkpoint T across eleven row-structured models (every-row reset, single
  resets at 35 and 66, boustrophedon traversal, row-number offsets) x 12 conventions x
  periods 2-40. Do not reopen the row-reset family without new plaintext.
- EXP-033: declared single-transposition families composed with **any fixed A-Z→A-Z function** — zero feasible at its exact scope.
- EXP-036: declared periodic shift-family, periods 2–23, composed with the declared transposition families — zero feasible at its exact scope.
- EXP-037: preregistered standard Porta family — zero feasible.
- EXP-038 / Checkpoint Q: full-Z26 second-order affine self-evolving keystreams, message-aligned, 12 committed shift conventions — zero feasible; independently exhaustive. This does **not** eliminate recursive/stateful systems generally.
- EXP-039 / Checkpoint R: standard no-padding double columnar transposition using ordered pairs from `{KRYPTOS, PALIMPSEST, ABSCISSA}`, followed by any fixed monoalphabetic map — `0 FEASIBLE-FUNCTION`, `0 FEASIBLE-BIJECTION`. This does **not** eliminate double transposition generally.
- Standard Fractionated Morse is structurally incompatible with the published positional crib semantics.
- Direct Gromark was rejected structurally before primer search because legal digits 0–9 cannot realise enough crib pairs under evidenced alphabet treatments.
- Quagmire I–III and Gronsfeld reduce to already-covered families; Quagmire IV needs an unsupported second alphabet.
- Direct World Clock letter-source models have multiple bounded negatives. Do not rescue them post hoc.

Also **prohibited**: treating 1986, 1988 or 1989 - or any arithmetic on them - as a key
length, offset, period, seed or index. The 2025 clue's "writing the plaintext in 1988"
against a Wall that fell in 1989 is an unresolved dating problem, most probably loose dating,
and is **not** a cryptographic clue (Checkpoint U).

Retracted claims that must **not** be revived:

- CET = 97 letters
- ATHEN absent from UTC+2
- upper band = north / lower band = south
- membership implies physical order
- EXP-029 significance from the wrapped/duplicate implementation
- isolated physical `OBKR` row
- uniform 31-character cipher-panel rows
- Checkpoint-L mixed-alphabet frontier
- Checkpoint-M claim that all experiments share the same three shift combiners

## Documentary results after Checkpoint R

### Box 6 Folder 10 — `Pre-Production and Notes, 1990-1999`

Inspected completely from the user-supplied image batch.

**Negative** for cipher-panel x-coordinate / common-lattice evidence, punch/type layout, K4 key source, exact K4 algorithm, or a note naming the fourth process.

Do not re-audit it. See `docs/external/checkpoint-R-folder10-content-audit.md`.

### Series 9 Box 16 Folder 2 — `Kryptos Sculpture, circa 1975-1993`

Inspected completely from a 106-image user-supplied ZIP.

Useful findings:

- 1990–1991 reporting repeatedly describes progression from Morse / Vigenere material to a harder **custom / modern process developed with a former or retired CIA cryptographer**;
- a March/April 1991 profile says Sanborn used “three or four” systems progressing in complexity;
- a 1992 Washington Post profile reports computer-guided high-pressure-waterjet letter cutting.

The waterjet fabrication claim is now **superseded as the current working account** by the stronger first-person Sanborn manuscript in Box 6 Folder 9: Sanborn says waterjet automation was considered but rejected on cost and the actual letters were hand-cut from traced metal stencils. Keep the 1992 statement only as conflicting secondary reporting.

A 1992 clipping calling the message a “complex anagram” is **low-confidence only** and is not experiment-grade evidence.

See `docs/external/checkpoint-R-box16-folder2-audit.md` and the Folder 9 supersession below.

### Box 6 Folder 11 — `Codes Research, circa 1980s-circa 2002`

Inspected completely from a 37-image user-supplied ZIP under staged contamination-safe triage.

**No complete alleged K4 plaintext or purported K4 solution was found in the supplied batch.**

The folder is broad and largely concerns Sanborn's wider code / intelligence / multilingual research rather than the original K4 construction. It includes a 1994 `FUMEE` layout, a Cyrillic tableau-style sheet, a later KRYPTOS-keyed alphabet proof, explicitly dated 2002 `Russian Decoding Chart` Morse/binary material, multilingual intelligence-text material, and Soviet/Russian archival documents.

These later practices are chronologically/evidentially insufficient to infer K4's 1989–1990 custom mechanism. Do **not** launch K4 experiments from them alone.

See `docs/external/checkpoint-R-folder11-codes-research-audit.md`.

### Box 6 Folder 8 — `Sculpture, 1993-2009`

Inspected from a 49-image user-supplied ZIP under contamination-safe triage.

The folder is dominated by later public Kryptos web printouts, 1999 newspaper coverage, public K1–K3 solver history, and solver correspondence / worksheets. It contains **no usable orthographic or restoration geometry** for the ciphertext face and no new K4 key source or exact mechanism.

Important contamination boundary:

- archive page `29-AAA-AAA_sanbojim_4128992.jpg` explicitly begins a proposed **message four / K4 solution** packet;
- pages 29–49 are therefore treated conservatively as **solution-adjacent / quarantined** for cryptanalytic use;
- no claimed K4 plaintext, key or method from that packet is admitted into this research programme.

See `docs/external/checkpoint-R-folder8-sculpture-audit.md`.

### Box 6 Folder 9 — `Book, undated`

Inspected completely from a 30-image user-supplied ZIP.

This is an unpublished / draft first-person manuscript / proposal headed **`KRYPTOS: From The Source`**. Page 2 says the text would be written by Jim Sanborn.

This is the strongest archive source so far for **fabrication and design-intent history**, while still not disclosing K4's exact algorithm or plaintext.

High-value explicit statements:

- Sanborn considered automated high-pressure-waterjet cutting but says the estimated cost was prohibitive;
- the actual letters were then **cut by hand with jigsaws**;
- copper sheets were painted black and **horizontal straight lines were scribed for rows of letters**;
- each character was individually located, a **metal stencil** was placed on the long row line, and the letter was traced, drilled, cut and hand-filed;
- K3 and K4 were ultimately cut by one remaining assistant over roughly two months, according to Sanborn, with virtually no errors;
- Sanborn says he recruited **Edward Scheidt** because historical systems such as Vigenere were not enough for his goal of challenging contemporary and future code-breakers;
- Sanborn says he expected the first three Kryptos sections to be solved in weeks or months while **K4 was intended to take much longer**;
- Sanborn says some plaintext and a partial code key were given to DCI William Webster for custody at the private dedication;
- Sanborn says official photography deliberately obscured some encoded text to delay decryption.

Important contamination boundary: page 2 says the proposed book would contain **significant K4 clues embedded in its text**. Under the current protocol, do **not** mine prose, anecdotes, numbers, place names, chapter titles or wording for hidden clues. Only explicit factual construction / history statements are admitted.

See `docs/external/checkpoint-R-folder9-book-audit.md`.

## Physical geometry status

**Superseded prospectively at Checkpoint S by first-person fabrication evidence (Box 6 Folder 9).**
History is not rewritten; earlier waterjet-based reasoning stands as a record and is no longer
the current model.

Sanborn's own draft says the robotic / high-pressure-waterjet route was **considered and rejected
on cost**, after which the copper was painted black, **straight horizontal row lines were
scribed**, and individual **metal character stencils** were placed on those lines, traced,
drilled, jigsaw-cut and hand-filed.

Therefore:

- **horizontal row order remains meaningful** — rows are the one physically established structure;
- **same-column vertical relations are weaker** than previously assumed: a scribed baseline fixes
  the line, not the pitch;
- fixed pitch, a common vertical x-grid, 31 physical columns, identical row starts and uniform
  spacing are **all unestablished**;
- exact x-coordinate hypotheses remain **parked**;
- **do not use apparent vertical alignment in photographs as a primary key source** — Sanborn
  also states he deliberately obscured encoded text in photographs, so publicity images are not
  neutral documentation of the cipher surface.

**Request 4 is demoted.** It existed to settle whether a common lattice exists; the first-person
account indicates it very likely does not, so a measured survey would refine spacing rather than
unlock an architecture.

## One recommended next action

**Pursue Request 7 (new, Checkpoint T): additional verified K4 plaintext** — any publicly
attributable, position-specific statement fixing a plaintext letter outside the two known
cribs, especially in zero-based `34-62` or `74-96`. Checkpoint T showed the binding
constraint is no longer compute but **constraint density**: survivors appear only where the
crib geometry goes blind. One extra verified letter would restore falsifiability to
long-period, per-row and reset-at-boundary models that are currently *untestable* rather
than untested. This now **outranks further cryptanalysis**.

Documentary work continues in parallel, unchanged in priority order:

**Pursue Request 2: the unedited 2005 Zetter/Scheidt interview material** — raw audio or full
transcript, interviewer notes, cut questions, drafts, fact-check correspondence.

**Secondary documentary target (added at Checkpoint S2):** the original / full 1991 ABC *World
News Tonight* Scheidt interview audio or video, sought specifically to recover the muffled and cut
passage (`taking the standard`, `you've got that computer there`, `addons`, `modular`) in context.
Until that context exists, the fragment supports **no** claim — see
`docs/external/checkpoint-S2-1991-scheidt-reevaluation.md` §F for the prohibition list.

Checkpoint S locates the bottleneck: the blocker is no longer *testing* architectures but
*identifying* one. Every architecture nameable from public evidence has been tested and failed,
and the documentary record now explains why — the harder process was **custom-built for the
project and then adapted**, so its prior coincidence with any nameable family is low.
Scheidt is the only living source who has publicly described the fourth process, and the
published article is self-described as a partial transcript edited for length.

Do **not** fill the gap with order-3 recursion, generic double transposition, arbitrary grid
routes, random alphabets, arbitrary long keys, generic modern stream ciphers, or another
historical-cipher catalogue. **No EXP-040 exists**, and Checkpoint S §7 records exactly which gate
conditions the closest candidate failed.

**Filter for any future proposal** (Checkpoint S §5): key entropy must lie within the EXP-019
unicity bound of roughly 66–76 letters. Sanborn intended K4 to be solved *later*, not never, so a
key exceeding the message's capacity contradicts the stated design intent.

**Contamination lock on Box 6 Folder 9:** the manuscript states it contains embedded K4 clues.
Only explicit factual statements are admitted. Do not mine it for acrostics, numbers,
capitalisation, chapter titles, place names, word counts or repeated phrases without a deliberate
and separately recorded change to the protocol.

## Contamination protocol

Do not access or use alleged complete K4 plaintext, purported solution dumps, leaked solution material, private K5 plaintext, or private K5 ciphertext.

Public construction photographs, public documentary sources, production records, historical-cipher references and explicit process provenance are safe. Clearly solution-looking pages must be quarantined before they influence cryptanalysis.

For Folder 9 specifically, explicit first-person factual statements may be used, but the announced **embedded K4 clues** must not be mined unless the user intentionally changes the contamination protocol.

Do not claim K4 solved unless there is one fixed deterministic 97-character decryption procedure that reproduces independently and satisfies all published constraints.
