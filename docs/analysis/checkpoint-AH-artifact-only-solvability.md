# Checkpoint AH — K4 artifact-only solvability audit

Date: 2026-09-13. Branch: `codex/k4-continuation`.
Starting HEAD: `f418e9b0c708cda91153982419d63afac749dac7`.
Scope: artifact diagnostics and mathematical audit; no cipher experiment.

## Finding and scope

**NO EXP-040 JUSTIFIED. K4 remains UNSOLVED.** No examined artifact feature supplies a new
parameter or reduction that makes an open AE class both independently motivated and falsifiable.
This does **not** establish that K4 requires private information, that artifact-only solution is
impossible, or that the statistical feature inventory exhausts every computable property of K4.

The public-solvability premise changes the evidence gate in one important way: a parameter may be
justified by a reproducible derivation from the sculpture or ciphertext. A private transcript is
not logically necessary. AG answered whether the documentary corpus *already supplied* a
parameter; its negative cannot answer whether the public artifact contains an undiscovered one.

No broad web research, private material, new cipher family, key search, language scoring, Trifid
survivor work, clock model, or EXP-040 execution was performed. Historical files and
`docs/current-status.md` are unchanged. AE remains the current cryptanalytic checkpoint; the
scope qualifications below are prospective and preserve prior experimental results.

Required reading: current status, AE result/census, AG audit/result. Coverage was checked against
T, W, AB, AC, AD, AF, the existing U/V Layer-A/Layer-B summaries, and the declared EXP-029–039
scopes. Only `data/k4.json` and public `data/cipher_side_rows.json` feed computations.
Older metadata in `data/physical.json` contains superseded counts and disallowed-source fields;
those fields supply no observations or parameters here. No private archive fact is used to
motivate a mechanism.

## Reproducible diagnostics

- Protocol: `audit/checkpoint_AH_protocol.md`, written before the new diagnostic execution.
- Audit: `audit/checkpoint_AH.py`.
- Independent scalar checks: `audit/checkpoint_AH_verify.py`.
- Full numeric observations, 276 crib pairs, distances, and controls: `results/checkpoint_AH.json`.

Run from repository root:

```text
python audit/checkpoint_AH.py --output results/checkpoint_AH.json
python audit/checkpoint_AH_verify.py
```

NumPy 2.4.6, PCG64 seed 20260913, 10,000 draws under each of two nulls: iid uniform A–Z of
length 97, and random permutations of K4 preserving its exact frequencies, support, length and
total repeated-symbol pair count. Twelve statistics were fixed before execution. Maxima include
all lags 1–48 or periods 2–48 inside each draw, avoiding selection of a favorable individual lag.
All 96 lag counts are recorded, but short-overlap lags 49–96 are not used to declare significance.

Two-sided plus-one Monte Carlo p-values are doubled smaller tails, then Bonferroni-adjusted over
24 feature/null comparisons. Correlated comparisons make this conservative. There is no claim
of correction for the entire project's historical hypothesis search. A Monte Carlo fraction of
zero is never proof of zero probability. Conditional permutations cannot assess histogram rarity.

| Statistic | K4 observation | Two-sided p, matched permutation | Two-sided p, uniform | Adjusted p, matched / uniform |
|---|---:|---:|---:|---:|
| Alphabet support | 26 | fixed by null | 1.0000 | — / 1 |
| Equal single-letter pairs | 168; IoC 0.03608247 | fixed by null | 0.4336 | — / 1 |
| Repeated bigram pairs | 10 | 0.1392 | 0.3006 | 1 / 1 |
| Repeated trigram pairs | 0 | 1.0000 | 1.0000 | 1 / 1 |
| Adjacent doubles | 6 | 0.2622 | 0.3196 | 1 / 1 |
| Maximum lag coincidence score | 3.03579; lag 7 has 9 matches in 90 pairs | 0.3008 | 0.4356 | 1 / 1 |
| Maximum residue coincidence score | 1.12848 over periods 2–48 | 0.0322 | 0.0208 | 0.7727 / 0.4992 |
| Largest STD adjacent-difference bin | 7 | 0.7793 | 0.7849 | 1 / 1 |
| Largest KRY adjacent-difference bin | 7 | 0.7735 | 0.7779 | 1 / 1 |
| Equal translated trigram pairs, STD | 7 | 0.9559 | 0.9661 | 1 / 1 |
| Equal translated trigram pairs, KRY | 8 | 0.6787 | 0.6721 | 1 / 1 |
| Composition difference among fixed physical rows | Pearson statistic 69.19724 | 0.6087 | 0.7215 | 1 / 1 |

The relatively small unadjusted p for maximum residue coincidences is a **deficit** of large
peaks, not evidence for a recovered period. It fails the declared correction. Lag and period
scores use binomial expressions only as scales; their dependent pairs are calibrated by
simulation, never interpreted as independent normal observations.

A translated trigram pair means two triples with the same two successive numeric differences,
equivalently equal up to one additive offset in the selected alphabet. STD and KRY were already
public, committed alphabets; no alternative labeling was optimized.

Independent verification compares all twelve vectorized statistics against scalar Counter and
explicit-pair definitions on 44 sequences (K4, simple diagnostic extremes, iid controls and exact
histogram shuffles). It checks saved observations, p-value arithmetic, arbitrary relabeling
invariance where claimed, and exact crib records. This is diagnostic verification, not independent
cryptanalytic confirmation of a hypothesis.

## Phase 1 — objective signal inventory

Here S means invariance under a **fixed bijective symbol substitution**, T under an arbitrary
position permutation, and Both under their composition. These flags do not claim invariance
under periodic, homophonic or arbitrary position-dependent maps. Geometry and plaintext/ciphertext
alignment are separate from string statistics.

| Signal / exact observation | Unusual? | S | T | Both | Mathematical use and coverage | Human discovery |
|---|---|:---:|:---:|:---:|---|---|
| 97 letters; prime length | Exact, no meaningful random-length null without a length-selection process | yes | yes | yes | Excludes unpadded complete b-symbol blocks when b does not divide 97; does not choose a route. O/T/AB/AE | Easy count |
| All 26 letters occur | Ordinary under uniform null | yes | yes | yes | Any fixed map of an at-most-25-symbol intermediate plus permutations is impossible. AB/AC already prove it | Easy inventory; strong exact exclusion |
| Histogram: K occurs 8 times; M and Y once; all counts in JSON | Ordinary under uniform null | up to relabeling | yes | up to relabeling | Weakens unchanged English histogram models; not evidence for a specific mask. EXP-007/033, T | Frequency count |
| 168 equal-symbol pairs, IoC 0.03608247 | Ordinary vs uniform | yes | yes | yes | Compatible with many polyalphabetic, fractionating and stateful mechanisms; cannot choose among them | Standard frequency analysis |
| Six doubles: BB, QQ, SS, SS, ZZ, TT | Not rare under matched null | yes as equality | no | no | Standard same-alphabet Playfair constraints only at fixed block alignment; EXP-007 and AB | Visible, but no generic period |
| Ten repeated bigrams, none repeated more than twice | Matched p=0.1392 | yes up to relabeling | no | no | Kasiski-style suggestions require controls; no repeated trigram provides a strong spacing lever | Easy scan |
| No repeated substrings of length 3–6 | Not rare | yes | no | no | No strong exact repeat hook; absence cannot exclude fractionation or feedback | Easy scan |
| Repeated-symbol distances: all recorded; lag 7 peak 9/90 | Adjusted p=1 for maximum lag | yes | no | no | Does not recover period 7 or a reset; existing periodic families covered at declared scopes | Countable, statistically ambiguous |
| Residue coincidences over periods 2–48 | No significant adjusted maximum | yes | no | no | No internally selected schedule among AE B/G/H/L | Standard periodicity test |
| Adjacent numeric differences, STD and KRY | Largest bin 7 in each, ordinary | no; constant shifts preserve | no | no | Useful only after fixing numeric alphabet and operation; EXP-001/006/008/016 | Table arithmetic feasible |
| Translated trigram repeats, STD 7 / KRY 8 pairs | Ordinary | no; constant shifts preserve | no | no | No repeated-difference hook selecting a state or polygraphic rule | Discoverable with effort |
| Row split 4/31/31/31 at indices 4,35,66 | Public count, not a statistical claim | yes | no for letter assignment | no | Supplies boundary candidates, not reset behavior. EXP-020/032/T | Directly visible row membership |
| Row composition statistic 69.19724 | Ordinary under matched null | yes | no | no | No detected change of alphabet distribution at rows; low power for subtle changes | Rough manual count possible |
| Crib equality partition: 13 distinct plaintext symbols | Exact; not a discovered random signal | yes for separately relabeled streams | only with known reindexing | only with known reindexing | 11 independent equal-image demands for a fixed direct map; 12 of 13 equal-P pairs have unequal C. T/AB/AE | Strong exact contradiction |
| Crib ciphertext partition: 14 distinct symbols | Exact | yes | only with known reindexing | only with known reindexing | Inverse injectivity demands also fail; no direct fixed bijection. T/AE | Strong exact contradiction |
| Two direct fixed points, positions 32 and 73 | No rarity inference needed for exact exclusion | no under independent output relabeling | no | no | Refutes direct no-self-encipherment mechanisms, not masked interiors. EXP-007/AB | Easy crib check |
| R→P at 27 and 65, distance 38 | T already gives 0.242 chance of at least one constant repeated-P group | label-dependent relation | no | no | Does not imply a 38-step state recurrence or key period | Noticeable coincidence |
| Repeated crib blocks | No repeats at size 2/4/5 for aligned complete blocks; EAS/AST at distance 9 for size 3 | yes | no | no | Exact conditional block-map constraints; AA/AC/AE | Usable only with a block/context rule |
| Cross-crib position differences 30–52; within-crib 1–12 | Exact geometry | yes | no unless indices tracked | no | Period collision counts, not a selected period. T/AE | Arithmetic feasible |
| Ciphertext repeated contexts / possible state reuse | Bigram/trigram counts above; not rare | yes for equality | no | no | Same output symbol is not necessarily same hidden state; EXP-008/034/038/T cover specified dependencies | No identifiable state from output equality alone |
| Public KRYPTOS alphabet | Explicit public order | physical metadata remains; numeric values do not | metadata remains | metadata remains | Fixes one natural indexing alphabet, already in all 12 conventions; EXP-014/036 | Strong public teaching feature, already used |
| K1/K2/K3 section lengths and boundaries | Objective counts with punctuation units stated below | length yes | yes within section | yes within section | No forced progression to a K4 parameter | Countable; extrapolation ambiguous |
| Misspellings, omissions, coordinates, compass/orientation, spacing | Presence alone has no calibrated rarity model | generally no | generally no | no | Public observations may encode instructions, but no unique decoder is recorded. V; EXP-023/032/035 and T at defined scopes | Potential instruction channel, currently unparsed |

Every row records either a concrete observation or a clearly delimited missing measurement.
This inventory covers the requested categories; it is not a proof that no unexamined invariant
exists. No physical spacing measurement or exact alphabet-panel anomaly is invented.

The repeated bigrams and zero-based starts are:
`DI 55/83; EK 44/92; FB 17/61; GK 30/85; HU 9/88; KZ 45/77;
QS 38/41; SO 13/33; SS 32/42; TJ 50/80`.
Their distances vary; selecting a divisor after seeing them has no independent force.

## Phase 2 — what K1–K3 publicly teach

| Public training feature | Recoverable lesson | Proposed extrapolation | Classification / existing coverage |
|---|---|---|---|
| Visible KRYPTOS-keyed tableau and solved K1/K2 | Component alphabet order can differ from ordinary A–Z; a repeating key is distinct from that alphabet | Use KRY component indexing as a finite alternative | Directly recoverable; already in 12 committed conventions and EXP-014/036. PALIMPSEST and ABSCISSA are repeating keys, not automatically alphabet keywords |
| K1/K2 repeating keys of lengths 10 and 8 | Repeated parameters permit cryptanalysis across a section | K4 inherits 8/10, their sum/difference, or their lcm | Weak analogy unless a separate decoding instruction selects it; literal/direct reuse already represented by EXP-001 and other declared scopes |
| K3 transposition | A solver must consider position changes even when letter identity is preserved | Fourth section composes earlier forms | Weak analogy; EXP-003/016/033/036/039 already formalize substantial parts. It does not choose permutation, width, order or number of passes |
| Different behavior in successive sections | Re-evaluate assumptions at boundaries | Deterministic increasing complexity or cumulative operations | Not forced: K1 and K2 use related operations; K3 changes kind. There is no unique numerical or operational continuation |
| IQLUSION, UNDERGRUUND, restored LAYER TWO | Preserve exact spellings and distinguish errors from instructions | Letters differing from standard spelling encode a K4 schedule | Potential public clue, but extraction order, alphabet and interpretation remain free; V already audits these. No rarity claim from a tiny selected list |
| K2 omitted separator and accidental ID BY ROWS | Engraved counts and intended cryptographic text may differ | Restore/delete a letter inside K4 or reset every carved row | Does not follow. K4 anchors remain fixed; row behavior already tested by EXP-020/032/T. ID BY ROWS is not an intended instruction |
| K2 coordinates and K3 narrative | Plaintext can carry a later semantic task | Coordinates or themes become K4 arithmetic | Weak analogy/Layer-B ambiguity; no forced Layer-A rule. No clock-source revival |
| Exact public section inventory | K1=63 letters; K2=369 letters+3 question marks; K3=336 letters+1 question mark; K4=97 letters | Form new periods by section-length/date arithmetic | Counts are directly recoverable; arithmetic recipes are numerology without a selected operation. Total 869 physical characters is not 869 A–Z letters |

The KRY alphabet is a genuine internally recoverable parameter. It was not missed. Cumulative
learning can explain why a solver knows to test substitution and transposition, but “combine
what you learned” does not determine a new pipeline. Historical cipher knowledge supplies a
prior over mechanisms; it does not make every finite catalog entry an independent hypothesis.

## Phase 3 — crib-induced algebra, before selecting a family

Let J be the 24 verified plaintext indices. The full 276 unordered pairs split as follows:

| Pair relation | Count |
|---|---:|
| Equal P, equal C | 1 |
| Equal P, unequal C | 12 |
| Unequal P, equal C | 10 |
| Unequal P, unequal C | 253 |

These are observations, not 276 independent equations. For a direct function S,
`P_i=P_j ⇒ C_i=C_j`; a bijection adds the reverse implication. Thirteen distinct P letters
give `24−13=11` independent equal-image requirements, which already fail. The inverse
partition has `24−14=10` independent requirements. Those two counts must not be added as
independent random events. Only R's pair at 27/65 survives equal-image checking.

For fixed numeric alphabets p_i and c_i, the already used weakly model-dependent relations are:

1. Additive mask: `d_i=c_i−p_i mod 26`. A phase reuse g(i)=g(j) requires d_i=d_j.
   Beaufort conventions replace this with c_i+p_i or p_i−c_i; all 12 committed vectors are
   recorded. These equations do not apply to an unspecified fractionating intermediate.
2. Canceling a shared mask gives `c_i−c_j=p_i−p_j mod 26`. This unifies repeated-P,
   equal-phase, source-collision and reset tests rather than creating a new family.
3. A fixed affine map implies `c_i−c_j=a(p_i−p_j)`; any repeated P with unequal C already
   refutes it. For general linear equations over Z26, solve separately modulo 2 and 13
   or use Smith normal form; coefficient count alone is not rank.
4. A proposed first-order key state obeys `d_i=d_j ⇒ d_(i+1)=d_(j+1)` wherever both
   successors are known. T already tests this under all 12 conventions. A repeated C
   does not imply a repeated d or a repeated state.
5. A source rule `d_i=f(source_i)` induces `24−number_of_distinct_sources` equalities.
   EXP-034 tests declared single-symbol feedback sources; unique source tuples give no
   equality constraints. Larger contexts cannot be justified just because shorter ones failed.
6. A two-mask permutation model gives a bipartite cycle system:
   `d_j=a_(j mod p)+b_(π(j) mod q)`, where `d_j=C_numeric[π(j)]−P_numeric[j]`.
   Independent conditions are `edges−touched_vertices+components`. This is AE class H,
   not a new deduction selecting π or the two periods.
7. Under an unknown fixed outer bijection, the full intermediate equality partition must
   equal C's equality partition. AB/AC already propagate this through fixed coordinate models.
   The internal alphabet-size bound survives arbitrary fixed symbol maps plus permutations.
8. A pure permutation requires each plaintext symbol's multiplicity to fit the ciphertext
   inventory. Three verified E's versus two ciphertext E's is an exact contradiction for
   K4-only pure transposition. No statistical null or guessed plaintext is needed.

For transparency the standard A=0 additive vector is:

```text
[21,34): 1 11 25 2 3 2 24 24 6 2 10 0 25
[63,74): 12 20 24 10 11 6 10 14 17 13 0
```

No new universal cipher equation follows from numeric subtraction: it chooses an algebra.
There is no transformation-independent P-to-C equality if arbitrary position bijections and
unknown mixing are admitted. Crib algebra refines a *declared* model; it cannot identify one
merely by naming its free intermediate variables.

### Prospective precision about AE's information counts

The blind-period table is exact for a **message-indexed** shared schedule:
`r=24−|{j mod p:j∈J}|`. For a transposition followed by a ciphertext-indexed mask it is
instead `r=24−|{π(j) mod p:j∈J}|`, with π defined as plaintext-to-ciphertext position.
This depends on π. EXP-036 already makes the distinction and enforces its gate per case;
AE's class-G shorthand must not erase it. No historical numerical result is changed and no
permutation is selected by this correction.

A raw count “free parameters < 24” is a useful heuristic for independent Z26 lookup values,
**not a universal necessary condition for falsifiability**. Domain restrictions, injectivity,
global inventory, equations over different fields, and partial-block propagation can constrain
a larger parameterization. AB already warned about this. In particular, 45–48 ternary coordinate
classes cannot simply be subtracted from 24 A–Z observations. This audit accepts the verified
Trifid compatibility results without using that mixed-unit count as a proof of vacuity.

For a fixed model define S_J as its set of realizable 24-symbol ciphertext projections, allowing
all permitted parameters and unknown plaintext completions. Its exact uniform-null compatibility
probability is `|S_J|/26^24`. For a fixed linear model, ranks over mod 2 and mod 13 give the
appropriate image size; for lookup models, collisions give equality counts. For a model selected
using ciphertext features, controls must repeat that selection. There is no warrant to apply a
fixed-model false-positive probability after searching for a favorable feature.

## Phase 4 — ciphertext-only discrimination and its power

The diagnostics can reject extreme distributional assumptions; they cannot reliably distinguish
periodic polyalphabetic, autokey, stateful, homophonic, fractionating and multi-stage masks that
produce similar short output distributions.

For one explicit power illustration, bootstrap 10,000 iid 97-letter samples from the **public
K3 ciphertext's empirical symbol profile**. Since K3 is a transposition, this retains its
plaintext marginal frequencies without needing a new plaintext corpus. Every draw exceeds the
uniform 95th-percentile collision threshold (202 pairs), and none is as flat as K4's 168.
Observed power is 10,000/10,000 for that very specific alternative; a one-sided 95% lower bound
is approximately 0.9997. The zero lower-tail count gives an approximately 0.0003 upper bound,
not zero probability. This is conditional on a K3-like iid frequency model; it does not bound
all possible English passages or establish power against every monoalphabetic cipher.

A fixed bijection or permutation preserves the collision count. Thus the flat inventory
weakens unmodified K3-like histogram architectures, while the exact E-count proof does more
for pure transposition. Among flat-output architectures, these statistics have demonstrated
**no useful discrimination**. Failure to reject random controls is not proof of randomness or
encryption strength.

For any proposed P and any C of equal length, unrestricted position shifts can choose
`k_i=C_i−P_i mod 26`. An unrestricted state machine can emit that finite sequence using a
position counter. Consequently output coincidences cannot identify the inner stage in those
unrestricted classes. Public solvability would require a recoverable restriction on that rule;
the premise alone does not tell us the restriction.

## Phase 5 — public physical features and missing representation

The cipher-side row transcription is an actual public input: it fixes row membership, section
boundaries, punctuation positions and the 4/31/31/31 K4 split. It does not fix a Cartesian grid.
EXP-032's ordinal-column model and T's reset models are exact tests of those declared indexing
rules, not evidence that equal ordinal positions are vertically aligned on the sculpture.

For row-local reuse the cribs share local slots at (32,63) and (33,64), giving two independent
equalities. A separate row-constant model has 3 exercised row values and 21 equalities; the
physical rows do not imply constancy. Arbitrary row-and-column dependence gives 24 distinct
arguments and no constraint.

The alphabet/tableau is intentionally public and demonstrably useful in earlier sections.
However, the repository represents its KRY alphabet and idealized generated table much better
than it represents every **as-carved cell, margin label, spacing, omission and anomaly**.
EXP-014 tests the generated 26×26 table as running-key streams; this is not a complete
measurement or instruction audit of the physical panel. A reported count alone, including the
legacy 867 figure, is not a verified cell inventory. No anomaly's location or wording is
asserted here without such a record.

This is a representation gap, not a discovered cryptographic parameter. It does not justify
an overlay, route, alphabet mutation, padding cell or key. Mirrored viewing of cut-through
letters gives an orientation choice but no decryption instruction. Compass features and
coordinates provide referents; a numeric transformation still needs a reproducible extraction
rule. K1/K2 misspellings remain exact public text, not an arbitrary pool of key letters.

No retracted clock facts, uniform 31-column claims, dates-as-keys, 7×14 padding assumptions,
or solution-adjacent geometry are admitted.

## Phases 6–7 — human discovery and finite-family gate

| Possible hook | Inferable parameter / choices remaining | Free parameters and constraints | Prior scope and human-solvability assessment |
|---|---|---|---|
| Public KRY alphabet | One fixed 26-symbol order; no new choice | Zero alphabet freedom after choosing KRY; direct fixed substitution has 13 exercised entries/11 equalities and fails | Directly discoverable and already used |
| Physical row-local key | 31 potential values, 22 exercised by cribs | 22 exercised Z26 values; 2 equality constraints; 12 conventions. Uniform bound 12/26²≈0.01775 for any fit | Already EXP-032/T negative. No full plaintext follows from 22 values; nine row slots remain unobserved |
| Physical row-constant key | A constant per row is an extra assumption | 3 exercised values, 21 equalities; total four rows leaves first row's value unobserved | Considered at S/AG; no new artifact instruction selects constancy |
| Lag-7 peak | Does not identify a key period; many maxima inspected | If p=7 direct additive were selected, 7 values/17 equalities; 12 conventions give bound 12/26^17≈1.06×10^-23 | Strong hypothetical test but already covered; matched maximum p=0.3008 gives no new selection |
| K1/K2 periods 8/10 around permutation | Period inheritance and π are not derivable | 18 mask values; at most 17 effective on connected occupied graph; at least 7 cycle constraints for fixed π; plus all freedom in choosing π | AE H already present. No artifact-derived finite permutation set; 26^-7 is a fixed-model uniform probability, not post-selection evidence |
| Prime length as a cyclic route | 97 fixes modulus only | 96×97=9,312 affine position permutations; key/map freedom remains | Exact affine-mod-97 route family already tested in EXP-003/016; prime length does not select one |
| Free hidden block/table/state map | No parameter is inferred | Unique exercised arguments memorize observations; zero collision constraints in the known AE regimes | No intended-solver discovery path or determined plaintext |
| Verified physical tableau anomaly | No anomaly/decoder established in present representation | Search size, exercised parameters, constraints and false-positive rate undefined until a rule is derived | An acquisition/representation task, not a serious cipher candidate |

No surviving **serious artifact-derived cipher candidate** exists, so there is no new candidate
whose full search size or plaintext determinacy can honestly be calculated. The exact counts
above explain why familiar attractive ideas fail either novelty or motivation. They are not
licenses to execute them again.

More generally, the 24 cribs are not the artifact's entire information budget: the other 73
ciphertext symbols, global inventory, public tableau, and a justified language prior can constrain
a structured model. Conversely, a deterministic decoder with a low-description-length key can
be recoverable even if its nominal key is long. The relevant entropy is uncertainty **conditional
on public artifact information** and the selected model. Neither a generic unicity estimate nor
an assumption of intended solvability identifies the decoder. No language prior was fitted here.

## Coverage ledger

| Earlier work | Internal hook already addressed | Limit retained |
|---|---|---|
| EXP-001/003/006/007/008/014/016 | Forced-key algebra, direct periodicity, affine routes, drift/reset, histogram and exact crib exclusions, feedback, generated tableau streams | Declared numeric alphabets, equations and route bounds |
| EXP-029/030/031 | Direct clock tapes, arbitrary single-symbol lookup and multi-face variants | Scoped negatives; withdrawn significance stays withdrawn; no clock-source revival |
| EXP-032/033 | Ordinal row-slot keys; arbitrary fixed maps over declared permutations | Ordinal slots are not measured x-coordinates; wider/unlisted permutations not automatically closed |
| EXP-034/035 | Self-key/source collisions and public cipher-panel streams | Single-source-symbol rules and exact declared traversals |
| EXP-036/037 | Earlier cipher forms composed with transposition; standard Porta | Composition-order asymmetry and per-case constraint gate preserved; arbitrary tables excluded |
| EXP-038/039 | Shared affine recurrence; finite public-keyword double transposition | Exact recurrence and nine frozen permutations only |
| T/U/V/W | Raw constraints, physical resets, public clues, inheritance and normal-form reductions | Thematic interpretation is not a forced extraction rule |
| AA/AB/AC/AD | Hidden-stage vacuity, equality propagation, inventory and verified coordinate constraints | Structured and free maps distinguished; no Trifid survivor pursuit |
| AE/AF/AG | Constraint geometry, arbitrary-table scope, documentary gate | Artifact-derived motivation is allowed; no new such parameter found |

## Exactly one highest-information artifact-only next action

**Create a verified cell-by-cell transcription of the intentionally public alphabet/tableau
panel, including headers, margins and departures from the generated KRY table, from an
unaltered sufficiently legible public image; then determine whether any confirmed departure
encodes one unambiguous instruction.**

This is one bounded public-artifact audit. Preserve uncertain readings as unknown, do not choose
among readings by crib fit, and do not search extraction recipes. It addresses an actual missing
representation in this repository and needs no private interview or archive. It may yield
nothing; its value is making an unmodeled public channel assessable. No cipher experiment follows
unless a confirmed feature independently specifies a finite rule that passes the gate.
