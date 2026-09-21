# Checkpoint AG — evidence-to-census reconciliation audit

**Date:** 2026-09-13

**Branch:** `codex/k4-continuation`

**Starting HEAD:** `e8be9e7d45db994bad6c150dd5b8f1c75bfefdf7`

**Type:** prospective documentary/decidability audit, not a cryptanalytic experiment

## Decision

**NO.** The repository does not contain an independently motivated structural parameter that
turns an open Checkpoint-AE class into a finite, non-vacuous, falsifiable family not already
tested at the required scope.

The documentary record establishes constraints on the *kind* of design: K4 is more than one
stage; masking suppresses recognizable English statistics; the design was historically grounded
and tailored for Kryptos; stage order was not disclosed; and Sanborn may have altered Scheidt's
handoff. None of those facts identifies a transform, period, key length, tableau, recurrence,
reset, alignment rule, parameter-reuse rule, or exact change. They therefore do not supply the
shared parameter that Checkpoint AE shows is necessary to make 24 crib letters informative.

No EXP-040 preregistration is created. K4 remains **UNSOLVED**.

## Scope and fixed crib geometry

Only these verified positional anchors are used:

- zero-based `[21,34)`: `EASTNORTHEAST` → `FLRVQQPRNGKSS`
- zero-based `[63,74)`: `BERLINCLOCK` → `NYPVTTMZFPK`

There are 24 known plaintext/ciphertext pairs. They become independent rejection constraints
only when a proposed architecture forces two or more observations to share parameters.
Checkpoint AE's fixed geometry is retained:

- periodic classes: `p=24,25,26` give 5, 3, 1 constraints; `p=27,28,29` give 0;
- no plaintext blocks repeat at sizes 2, 4, or 5 at either admissible alignment;
- arbitrary fixed 26×26 combiners have no repeated `(plaintext,key)` input at
  `p=8,10,13,26`;
- free hidden stages can memorize distinct observations and are compatible by construction.

“Compatible” is not evidence.

## Documentary statement ledger

“Shared parameters” below means parameters forced to recur across the 24 crib observations.
Where no mathematical family is specified, there are **0 operationally identified shared
parameters** and the 24 known pairs impose **0 architecture-specific constraints**: the count is
not 24 merely because 24 letters are known.

| ID | Source / date / speaker | Necessary statement or faithful paraphrase | Grade and form | Exact structural parameter implied | AE class affected | Prior coverage | Shared parameters / crib constraints | Falsifiability, chance, and meaning of a negative | Gate result |
|---|---|---|---|---|---|---|---|---|---|
| D1 | Jan. 1990 *Washington Post*; reporter description of the project | A modern system was created for the project by an expert cryptographer. | B/C; reporter paraphrase | None. “Modern” and “created for” name no operation. | Broadly E–M | N/A without equations | 0 / 0 | Not falsifiable; any positive is compatibility; no defined negative. | **not operational** |
| D2 | 1991 ABC B-roll; Ed Scheidt; 2004 third-party transcript | Roughly four months were spent selecting appropriate codes; Scheidt helped design the encryption, later taught Sanborn “this is how you do it,” and called it unique to Jim's design. | B+; direct testimony in later transcript | A teachable, project-tailored procedure, but no family, schedule, key, or stage order. | D–M as a design filter | No exact family selected | 0 / 0 | Not falsifiable. A negative against any guessed family would not test “tailored.” | **not operational; too many free parameters** |
| D3 | 1991 ABC B-roll; Ed Scheidt | Fragmentary words resembling “standard,” “computer,” “addons,” and “modular.” | D/LOW; cut, muffled direct-speech fragment | None: subject and referent are missing. | None admissibly | Not tested or usable | 0 / 0 | Any result would be architecture manufacture. | **insufficient provenance** |
| D4 | 19 Jul. 1999 *Washington Post*; Ed Scheidt | Methods could have a historic basis without exposing current government methods; the work was intended eventually to be decipherable. | B+; direct quotations in reporting | Historical grounding and recoverability are filters, not a named historical family or entropy value. | All classes; especially D–J | Named classical families already broadly covered, but no family follows from this sentence | 0 / 0 | Not falsifiable as a transform; a negative against one historical cipher proves only that cipher. | **not operational** |
| D5 | 21 Jan. 2005 WIRED; Ed Scheidt | Kryptos used four processes, two similar and two different. The surrounding wording moves among four sections. | B+; direct interview, edited | Best-supported reading is one high-level process per section, not four serial K4 stages. | Broad stage census only | Already reconciled at S/Y | 0 / 0 | Treating it as four K4 layers would create parameters not in the source. | **not operational** |
| D6 | 21 Jan. 2005 WIRED; Ed Scheidt | In K4 he masked/disguised English so frequency and counting no longer give the earlier access; the masking technique may not be known. | B+; direct interview, edited | Functional goal only: suppress recognizable English statistics. No mask equation or parameter reuse. | G–L most directly | Many named masks tested; arbitrary masks remain open/vacuous | 0 / 0 until mask defined | Every sufficiently free mask fits. A positive is expected; a negative can address only an independently specified subset. | **not operational; too many free parameters** |
| D7 | 2005 WIRED and 2015 workshop; Ed Scheidt | Scheidt did not verify final K4 and allowed that Sanborn could have added things, another step, or further masking. | B/B+; direct edited interview and event transcript | Additional uncertainty; no identity, location, or rule for the change. | H–M | No exact “Sanborn change” family exists | 0 / 0 | Not falsifiable. A guessed extra step is post-hoc rescue. | **too many free parameters** |
| D8 | 2005 WIRED Sanborn material, synthesized at S/S2; Jim Sanborn | Sanborn selected among systems and put his own artistic touch on the work; accounts differ on whether he modified a finished Scheidt procedure. | B+ direct recollection; interpretation is disputed by contemporaneous Scheidt testimony | Modification occurred or was possible, but the modified component and operation are unstated. | H–M | N/A | 0 / 0 | No finite family follows. A negative against one modification proves nothing about “artistic touch.” | **not operational** |
| D9 | 24 Oct. 2015 workshop; Ed Scheidt | He would consider K4 “more than one stage,” immediately in the masking discussion. | B/B+; direct-event transcript, secondary transcription | Lower bound on stage count; masking is Layer A. It does not say exactly two or name/order stages. | G–M | Multi-stage residuals inventoried at W/AA/AE | 0 / 0 by itself | Not falsifiable without stage definitions. | **not operational; too many free parameters** |
| D10 | 24 Oct. 2015 workshop; Ed Scheidt and participants | Period, sentence boundaries, and special characters were discussed conceptually. | B; event transcript | No period value, reset, punctuation rule, or alignment. | B, C, G, H, L, M | Declared periodic/reset families already tested at their stated scopes | 0 / 0 from the statement | A chosen period would be unsupported; negative would prove only the chosen model. | **unsupported period/key inheritance** |
| D11 | 24 Oct. 2015 workshop; explicit question to Ed Scheidt | Asked whether masking came before or after encryption; no clear answer/choice was given. | B; event transcript | Stage order remains an unresolved branch, not a parameter value. | G–M | Both orders tested only for declared older families | 0 / 0 | Testing both over a free mask expands rather than bounds the family. | **unsupported stage order** |
| D12 | 24 Jul. 2007 PBS/NOVA broadcast; narrator/editorial explanation | Concealment can occur before enciphering, with illustrative examples. | A for what aired; editorial narration, not Scheidt testimony | No K4 stage order. | M and pre-mask variants of G–K | N/A | 0 / 0 | Cannot select pre-encryption concealment. | **insufficient provenance** |
| D13 | Preserved report of a 2004-era talk; Ed Scheidt attribution | K4 used “a bit of stego”; later clarification says a steganographic piece existed but not how or where. | C; attendee/report paraphrase | No carrier, extraction, alignment, insertion/deletion, or stage placement. May concern Layer B. | D, M; possibly K | No exact family selected | 0 / undefined | Free extraction/alignment is vacuous; negative against one stego scheme proves only that scheme. | **Layer-B evidence rather than Layer-A evidence; insufficient provenance** |
| D14 | 2010 Crimson Shield report; Ed Scheidt attribution | Kryptos algorithms were more unique while underlying mathematical principles were familiar. | C/B-; reported direct wording, not K4-specific | Adaptation of familiar principles, without naming principle or K4 applicability. | Broad D–M | Named familiar families broadly covered | 0 / 0 | Cannot distinguish any open class. | **not operational; insufficient provenance** |
| D15 | 2006/2010/2014 WIRED; reporter attribution to Sanborn; 2006 direct Sanborn wording on `LAYER TWO` | Earlier solved parts contain K4 clues (reporter narration); Sanborn directly said omission of `LAYER TWO` meant solvers were missing a clue. | C+/B- for inheritance wording; B+ direct for “missing a clue” | No Layer-A target, reuse rule, key length, period, or stage is stated. | H if read as K1/K2 reuse; otherwise Layer B/ambiguous | K1/K2-style declared shifts and K3-style declared transpositions already broadly tested | 0 / 0 under admitted wording | Literal 8/10 inheritance would be testable in some architectures, but is not supplied by the source. | **unsupported period/key inheritance; Layer-B evidence rather than Layer-A evidence** |
| D16 | Undated Sanborn draft `KRYPTOS: From The Source`, Box 6 Folder 9; Jim Sanborn | Sanborn knew Vigenere and recruited Scheidt for contemporary expertise; K4 was meant to take much longer. | B+; first-person archival manuscript, explicit facts only | Difficulty and expertise priors, not a K4 tableau, alphabet, period, or method. | All, weakly A/B/F/G | Vigenere descendants at declared scopes already covered | 0 / 0 | Does not select a new finite family. Embedded prose clues are excluded by protocol. | **not operational; already tested** for the obvious Vigenere reading |
| D17 | Same draft, fabrication account; Jim Sanborn | Straight horizontal row lines were scribed and individual stencils placed on them. | B+; first-person archival manuscript | Physical row membership/order only; no cryptographic reset, row-constant key, common x-grid, or pitch. | C, G, M if an extra row rule is assumed | Row-local/reset models already covered at declared scopes; row-constant mask considered at S | 0 documentary mask parameters / 0 constraints until a row rule is added | A row-constant additive rule would have 3 variables and 21 constraints, but constancy is invented. | **unsupported reset/alignment behavior** |
| D18 | Same draft; Jim Sanborn | Some plaintext and a partial code key were placed in DCI Webster's custody. | B+; first-person archival manuscript | A key existed, but its section, content, length, alphabet, and schedule are unknown. | B–H, L | N/A without content | 0 / 0 | “There was a key” is compatible with nearly every keyed family. | **not operational; too many free parameters** |

### Exact repository provenance for the ledger

| IDs | Repository file(s) |
|---|---|
| D1, D8 | `docs/external/checkpoint-S-sanborn-scheidt-synthesis.md`; contemporaneous press basis also recorded in `docs/external/checkpoint-R-box16-folder2-audit.md` |
| D2, D3 | `docs/external/checkpoint-S-1991-abc-scheidt-broll-audit.md`; conservative rereading in `docs/external/checkpoint-S2-1991-scheidt-reevaluation.md` |
| D4 | `docs/external/checkpoint-S2-1999-washington-post-scheidt-provenance.md` |
| D5–D7 | `docs/external/checkpoint-Y-masking-source-consolidation.md`; 2005 source grading also in `docs/external/checkpoint-V-source-ledger.md` |
| D9–D11 | `docs/external/checkpoint-X-2015-scheidt-workshop-stage-order-audit.md` |
| D12 | `docs/external/checkpoint-Z-pbs-abc-primary-source-hunt.md`; attribution correction in `docs/external/perplexity-scheidtnova-audit-2026-09-13.md` |
| D13, D14 | `docs/external/checkpoint-Y-masking-source-consolidation.md` |
| D15 | `docs/external/checkpoint-V-k1-k3-clue-inheritance-research.md` and `docs/external/checkpoint-V-source-ledger.md` |
| D16–D18 | `docs/external/checkpoint-R-folder9-book-audit.md` |

## Census reconciliation

The following are the only candidate readings that approach a quantitative gate. None is newly
licensed by the documentary evidence.

| Candidate reading | AE class | Genuinely shared parameters | Independent crib constraints | False-positive behavior | Prior status | Exact failure |
|---|---|---:|---:|---|---|---|
| Same-index additive masks with inherited K1/K2 periods 8 and 10 | B | Effective schedule period divides `lcm(8,10)=40` | Governed by the resulting period | Already in the declared direct shift sweep through period 48 | EXP-001 scope | **subsumed by a prior experiment**, and inheritance is unsupported |
| Period-8 and period-10 additive masks separated by a fixed permutation `M2 ∘ π ∘ M1` | H | 18 mask values, 17 effective after one additive gauge; `π` must also be fixed | At least 7 for fixed `π` (measured mean 7.60 over audited permutations) | Heuristically about `26^-7` survival per fixed convention if the cycle equations behave independently and uniformly; familywise chance grows with every tried `π`/convention | Open but unsupported at AE | **unsupported period/key inheritance**; no source states 8/10 reuse or `π` |
| One additive key value constant on each carved crib-bearing row | C | 3 row values | 21 | `26^-21` per fixed convention under the simple equality model | Explicitly rejected as an EXP-040 candidate at S; row/reset families otherwise tested at declared scopes | Physical rows are documented; **row-key constancy is not**. A negative proves only that invented three-value mask. |
| Periodic declared shift/combiner family at `p=24,25,26` | B/G | `p` schedule values (plus any fixed declared transform parameters) | 5 / 3 / 1 | Approx. `26^-5`, `26^-3`, `26^-1` for one fixed independent additive family; multiple comparisons rapidly erode meaning | Structurally open/degrading | **unsupported period**; compatibility would be weak evidence |
| Periodic schedule at `p=27,28,29` | B/G | `p` schedule values | 0 / 0 / 0 | Survival probability 1 under crib-consistency fitting | Undecidable with current crib geometry | **vacuous under current crib geometry** |
| Arbitrary fixed 26×26 combiner at `p=8,10,13,26` | L | 676 table cells globally; all 24 exercised input pairs are distinct at these periods | 0 | Survival probability 1; the table memorizes every observation | Vacuous at AE/AF | **vacuous under current crib geometry; too many free parameters** |
| Structured Trifid inner stage plus fixed injective readout | J | 45–48 free ternary coordinate classes in the surviving configurations | 24 observed letter equations, insufficient to determine those classes | 15 conditionally-SAT configurations are expected compatibility, not evidence | Narrowed at AB/AC; not closed | No source names Trifid/cube/period/reset/readout; **too many free parameters**. No chasing or relabeling is authorized. |
| Free digraphic/4-graphic/5-graphic inner stage plus free outer mask | I/K | One free value per distinct observed block/output | 0 because the observed blocks do not repeat | Survival probability 1 | Proved vacuous at AA/AE | **vacuous under current crib geometry** |
| Named external source or finite recurrence | D/E | Would depend on the named source or recurrence coefficients | Potentially nonzero only after the rule is frozen | Cannot be computed before selection | All declared sources and bounded recurrences tested at their scopes | No documentary source or recurrence is named; **not operational** |
| Length-changing/steganographic inner stage | M | Alignment/extraction rule plus transform parameters | Undefined until alignment is supplied | Free alignment can absorb failures | Requires an extra rule at AE | **unsupported alignment behavior** |

Checkpoint AF's scope correction is preserved: the `p<=23` negative closes the declared
Vigenere/Beaufort/variant-Beaufort conventions, relevant declared transposition compositions,
Quagmire/Gronsfeld reductions, and standard Porta. It is **not** a theorem against arbitrary
periodic 26×26 tables; those are class L and can be completely unconstrained.

## Failure classification

- **Not operational:** modern, custom, adapted, complex, different, historic basis, masking,
  familiar principles, and teachable/recreatable.
- **Already tested/subsumed:** obvious direct K1/K2 shift reuse; same-index 8/10 masks collapse
  to a period dividing 40; declared substitution/transposition and reset families at their
  registered scopes.
- **Vacuous under present geometry:** free block maps, free outer masks, arbitrary tables without
  repeated inputs, and periods 27–29.
- **Too many free parameters:** unspecified Sanborn changes, generic stego, arbitrary
  multi-stage masking, and free alignments.
- **Unsupported stage order:** the workshop was directly asked and supplied no answer; PBS
  pre-encipherment language is editorial.
- **Unsupported period/key inheritance:** no source says K4 inherits periods 8/10, earlier keys,
  or K3's transposition.
- **Layer B rather than Layer A:** `LAYER TWO`, earlier-section clues, and steganographic
  interpretations remain ambiguous unless a source ties them to the ciphertext transform.
- **Insufficient provenance:** the muffled 1991 fragment, attendee/report paraphrases, the
  unverified UGA object lead, and any inference from unavailable transcript content.

## Answer to the reconciliation question

No open AE class is converted by the existing documentary record into a family satisfying all
three requirements:

1. finite/precommitted from evidence rather than selected after seeing results;
2. non-vacuous under the 24-letter geometry;
3. not already contained in an earlier declared experiment.

The closest numerical case is class H at inherited periods 8 and 10: for a fixed permutation it
has at least 7 independent crib constraints. Its decisive parameter—the inheritance of 8 and 10
and the intervening permutation—is absent from the evidence. The strongest purely physical case,
a row-constant mask, has 21 constraints but invents constancy/reset from the mere existence of
rows. Neither passes the documentary gate.

## Exactly one highest-information next action

**Recover and authenticate the original `ScheidtNova.doc` binary, then audit only Scheidt's
verbatim answers for one reusable Layer-A parameter (transform family, stage order, period/key
length, reset/alignment rule, tableau construction, recurrence, or exact Sanborn change).**

This is one bounded acquisition action against a publicly indexed object. Requests are already
pending; do not duplicate outreach. If the file is obtained, preserve the binary, hash it,
establish provenance, contamination-screen it, and only then apply the AE gate. Anything less
specific than a reusable operational parameter does not change this decision.
