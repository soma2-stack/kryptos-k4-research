# Checkpoint AB — internal fractionation behind an outer mask

Branch `codex/k4-continuation`; starting commit `adf9a1867496928539f50de608efd157e9ba6a2c`.
This is a mathematical scope audit with deterministic support code, not EXP-040.
Only the supplied 97-letter ciphertext and the two public cribs are used. No web
search, additional plaintext, solution material, candidate scoring, or square-key search.

## Findings

1. **A fixed outer map cannot expand a 25-symbol inventory to 26.** This closes
   every 25-symbol inner output followed only by fixed letterwise maps and
   transpositions, regardless of the square, merge, period, or number of such stages.
2. An arbitrary outer bijection preserves the **entire equality partition** of
   intermediate positions. Coordinate equalities induced by ciphertext collisions
   can therefore reject an internal fractionator without choosing its square.
3. For the coordinate-row concatenation model defined below, propagation rejects
   **175 of 194 Trifid configurations** (all periods 1–97, origin zero, continuous or
   physical-row reset). These are new inner-stage scope results; unresolved cases
   are not claimed feasible. The period-2 continuous model fails at both phases;
   period 3 fails at phases 0 and 1 but phase 2 remains unresolved by this audit.
4. Periodic outer bijections erase cross-phase equality constraints but not all
   constraints. The finite small-period audit gives **156 UNSAT cases out of 7,760**
   labeled cases, including period-3 Bifid-like processing with outer periods 3 and 9.
5. Some earlier scope statements need qualification: incomplete crib blocks can
   constrain outputs; a large parameter count is not a proof of untestability;
   Fractionated Morse's local-span argument needs an additional local-decoding
   assumption. These qualifications are recorded here without editing earlier reports.

## Inputs and definitions

`C` is the user-supplied string, SHA-256
`eea813570c7f1fd3b34674e47b5c3da8948026f5cefee612a0b38ffaa515ceab`.
Known `P[21:34]=EASTNORTHEAST`, `P[63:74]=BERLINCLOCK`; all intervals are half-open.
We consider `C=M(F(P))` as a conditional architecture, not a documented stage order
or a claim of exactly two stages. Checkpoints X/Y/Z support multiple stages and
suppression of recognizable English statistics, but specify no operation, period,
key source, or order. Sanborn's possible modifications remain unspecified.

The terms *position preserving outer stage* and *local plaintext dependence* are
different. An outer letter map retains intermediate indices; a fractionator can
make intermediate index i depend on several plaintext indices. The known cribs
fix plaintext indices, not isolated independently decryptable ciphertext substrings.

## Outer-mask invariants

Let `X=F(P)`. A bijection exists on observed symbols exactly when
`X_i=X_j iff C_i=C_j` for every pair acted on by the same map. This condition is
both necessary and sufficient for extending a partial injective map to a permutation
of a common finite alphabet. An embedding of 25 symbols in A–Z is injective but is
not surjective; its image still has at most 25 letters.

| Outer stage | Surviving constraints | Information lost / qualification |
|---|---|---|
| Fixed monoalphabetic bijection | Full equality/inequality partition, distinct count, multiplicities up to relabeling, IoC, adjacent-pair equality patterns, length and indices | Letter names, numeric distances, coordinate identities and P-to-C fixed points disappear |
| Keyed monoalphabetic bijection | Same invariants; a specified keyword family only adds restrictions | A freely chosen keyword is no historical evidence; no need to enumerate alphabets |
| Periodic additive mask, fixed numeric alphabets | Within phase, `C_i-X_i=C_j-X_j mod 26`; equality and modular differences survive | Cross-phase equality disappears unless key entries are linked; labeling matters |
| Periodic arbitrary bijections | Equality iff equality within each residue; per-residue multiplicities and inventory bound | No modular-difference test; global multiplicities and adjacent-pair doubles can disappear |
| Independent position bijections | Length and order of intermediate slots | For every admissible X choose a permutation taking X_i to C_i independently. Cribs alone cannot restrict F through this mask |
| Stateful/feedback mask | Constraints only when the specified state forces reuse of a map; length if defined 1:1 | State transitions, initialization, observable state, and memory must be supplied. An unrestricted position-counting state reproduces the previous vacuity |
| Transposition plus mask | Length always for these operations; global histogram/equality after known reindexing for a fixed bijection | Unknown permutation destroys local adjacency/alignment. Periodic mask before vs after permutation is different; fixed maps commute with permutations |

A fixed non-injective map preserves equality only in the forward direction and
can reduce inventory, never increase it. Homophonic or state-dependent symbol
choice is not a fixed map. For q phase maps on s inner symbols,
`|alphabet(C)| <= min(26,q*s)` is necessary, as is at most s distinct output letters
within any phase. For s=25 this forces at least two effective maps, but does not
select their schedule. A 27-cell Trifid cube cannot have a total bijection into
26 letters; the monoalphabetic model here permits one unused cell and an injective
mapping of the at-most-26 *used* cells. A collision map from all 27 cells to 26
letters is a different, weaker model to which inverse-equality propagation does not apply.

## Reclassification of earlier negatives

A = survives the specified outer extension; B = final-output-only; C = conditional;
D = earlier test equations do not apply. Classification concerns the precise argument.

| Earlier argument | Class | Correct internal-stage scope |
|---|---|---|
| EXP-012: output inventory below 26 | C | Survives any fixed letterwise function and any transpositions (A in that subclass); disappears with sufficient phase/state-dependent maps |
| A literal J cannot be emitted by an I/J square | B | An outer renaming can name an inner symbol J. The stronger cardinality argument still holds for a fixed map |
| I/J input merge | C | Information about I vs J is irreversibly lost unless auxiliary information restores it. Cribs contain I but no J, so they cannot directly test that pair. Other merges must normalize the known letters explicitly |
| P-to-C fixed points / reflector reasoning | D | `M(X_i)=P_i` says nothing about whether `X_i=P_i`; no self-map negative transfers through unknown relabeling |
| Standard Playfair unequal output pair | C | A single injective map preserves unequal letters within an aligned pair. Different maps for its two positions need not |
| Repeated deterministic digraph | C | Equal input pairs force equal output pairs under equal contexts and outer schedules; reversed pairs require a reversal-equivariant F |
| EXP-013 Trifid p=2,3 | D | Its solver identifies plaintext and ciphertext labels in the same cube. Outer relabeling removes that identification. New propagation below recovers some, not automatically all, negatives |
| EXP-012/013: periods >=4 untestable | D | Parameter counting and whole-block coverage do not prove it. Partially known blocks and ciphertext collisions can propagate constraints |
| Fractionated Morse local span too short | C | Valid if that exact C substring independently encodes the claimed word(s); not implied by plaintext positions alone in a variable-rate transform |
| Complete-block Digrafid length divisibility | C | A complete-block output of even length stays even through any 1:1 mask. Historical incomplete-block handling was not established by the earlier audit; no universal Digrafid claim follows |

EXP-033 and EXP-039 decide `S(P[permuted index])`, not `S(F(P))` with coordinate
mixing. EXP-036 decides shifts on known individual P letters, not on unknown X.
EXP-038 likewise derives a key from P/C pairs; it cannot be reused as an internal
fractionator's outer-key negative. This audit does not rerun their large searches.

## Equality and collision extraction

There are 13 distinct known plaintext letters. Repeated groups (zero-based):

| Letter | Positions |
|---|---|
| E | 21,30,64 |
| T | 24,28,33 |
| A | 22,31 |
| S | 23,32 |
| N | 25,68 |
| O | 26,71 |
| R | 27,65 |
| L | 66,70 |
| C | 69,72 |

These produce 13 equal-letter pair comparisons (11 spanning equalities).
Known ciphertext groups are F:{21,71}, K:{31,73}, N:{29,63},
P:{27,65,72}, Q:{25,26}, R:{23,28}, S:{32,33}, T:{67,68}, V:{24,66},
plus five singletons. Thus the 24 observed crib slots have 14 distinct C letters,
11 equal-C pair comparisons and 10 spanning equalities. These counts concern the
crib projection; the coordinate propagation also uses all 97 *ciphertext* symbols.

Repeated overlapping digraphs: EA at 21/30, AS at 22/31, ST at 23/32.
All repeats have separation 9, so each pair of occurrences has opposite digraph
parity. There are no reversed digraph matches in the two runs. No repeated
aligned digraph constraint exists under either continuous pairing parity.

Equal plaintext letters imply equal complete coordinate vectors in one shared
square. They do not imply equal fractionated output symbols: each output tuple
may combine coordinates from different letters. Conversely equal C under a
common injective outer map forces equality of *all* coordinates in its two output
tuples. Different C forces an OR of coordinate inequalities. Those relations can
force distinct plaintext letters into the same cell, a contradiction.

## Symbolic internal coordinate model

For dimension m (2 or 3), let `v(L)=(v_0(L),...,v_(m-1)(L))` be an injective
assignment to a square/cube. For block `[a,a+d)`, concatenate the coordinate rows
in a fixed axis order and regroup into m-tuples. Standard order gives
`Xtuple_(a+j)[t] = v_floor((m*j+t)/d)(P_(a+(m*j+t) mod d))`.
At a shortened block use its actual length in place of d. A fixed readout of
tuples into symbols is absorbed by a fixed outer relabeling. A global reversal
of output coordinate order also preserves tuple equality and need not be searched
separately for arbitrary phase bijections. Arbitrary coordinate-stream routes,
inverse fractionation, alternating squares and variable block schedules are outside
this definition; this audit does not label them eliminated.

`audit/checkpoint_AB.py` builds these expressions without assigning a square:

1. Known letters share coordinate variables; each unknown position gets fresh
   coordinates, with no plaintext value guessed. This relaxes the alphabet and is
   safe for deriving impossibility.
2. Every pair of equal C in the same outer residue unions corresponding coordinate
   variables, including outputs crossing partially known blocks.
3. Reject if unequal C tuples are forced identical, or if two distinct known
   plaintext letters are forced into the same complete cell.
4. Otherwise report **UNRESOLVED**, never SAT. Finite coordinate-domain sizes,
   disjunctive inequalities, completion of the square, and allowed unknown letters
   can still create further contradictions.

For a specified concrete intermediate sequence `consistent()` is an exact
two-way-map existence checker. For symbolic tuples the union test is deliberately
one-sided. An exact extension is a finite CSP: domains 0..4 or 0..2, all-different
complete cells, forced tuple equalities, and OR-of-coordinate-inequalities for
different ciphertext. At most 194/291 coordinate variables exist before merging;
no 25! or 27! permutation enumeration is needed to express it. This is finite
but no runtime or feasibility guarantee is inferred from that fact.

### 5x5 cases and merge choices

For any standard or keyed 25-cell square, any single merged pair, and any fixed
outer function, the 26-letter inventory already rejects the complete architecture.
No crib assumption or normalization choice rescues it. The symbolic audit's m=2
rows assume the usual I/J merge (neither of the distinct known letters is merged);
their cell-collapse certificates must not be reused unchanged for a different merge.
The inventory theorem, however, covers every alternative merge.

With periodic outer maps, symbolic constraints are useful again. The p=3 model
in the audited three phases and both reset hypotheses rejects outer q=3 and q=9
for both axis orders, without fixing a square. Other values mostly remain
unresolved by propagation. This is a new bounded necessary-condition result, not
evidence for one of the survivors. A fixed standard square gives concrete values
at every wholly determined output; a keyed square requires the shared symbolic
variables. Both cribs constrain the same variables, allowing cross-crib coupling.

Reversing coordinate rows is tested in the small-period sweep. Removing spaces
before processing defines the stated index model. Retaining separators, counting
them only in scheduling, or resetting on words requires an explicit rule and
changes the dependency equations. No word boundary is inferred from BERLINCLOCK.

### Trifid results and partial blocks

EXP-013 used the same cube assignment for P labels and directly observed C labels.
Here the outer map is factored out and only cell equality is preserved. Of the
97 origin-zero periods, the following remain **unresolved by propagation**:

| Processing | Unresolved Trifid periods | Rejected |
|---|---|---|
| Continuous | 5,7,10,13,14,16,23,28,29 | 88/97 |
| Restart at 0,4,35,66 | 4,7,11,14,19,20,22,23,26,28 | 87/97 |

Periods above 97 are identical to one 97-symbol block at origin zero. Under row
restart all periods >=31 are likewise identical on these segments; counts are
labeled configurations, not independent tests. Arbitrary initial phases for large
periods were not swept. For p=2, both initial phases in continuous processing are
rejected. For p=3, phases 0 and 1 reject; phase 2 is unresolved. All three phases
with physical-row restart reject for p=3 in standard axis order. Full small-phase
and axis-order results are saved in JSON.

Example witness: continuous Trifid p=2, phase 0 forces S and T into the same cube
cell. Continuous p=4 forces output positions 24 and 69 to the same tuple despite
different C letters. Thus periods >=4 can indeed be falsifiable, even behind an
unknown outer bijection. At p=3, origin zero, output 33 is fully determined although
its block includes unknown positions 34 and 35; its coordinates all come from
known input 33. This directly refutes the whole-block-only coverage rule.

An outer bijection can rename or avoid the 27th symbol; its absence is not the
old uniform-output probability argument. A total 27-to-26 injection is impossible;
our partial-used-cell interpretation is explicitly weaker and preserves equality.

## Digraphic inner stage

Standard Playfair with a 5x5 output square is already excluded by inventory under
a fixed outer map. Independently, an injective common map cannot turn unequal
Playfair output letters into doubles. For continuous even-start pairs, ST at
32–33 corresponds to SS. For odd-start pairs, NO at 25–26 corresponds to QQ
(and IN at 67–68 to TT). Thus both prepared-text pairing parities fail even if
one ignores the inventory proof. Row restart at 4,35,66 still includes pair 32–33.

This local proof assumes the declared crib indices are indices in the prepared
pair stream. Standard insertion of separators/fillers before those positions
requires an explicit raw-to-prepared index map. Odd total output length is an
additional global problem: complete Playfair digraphs always emit an even count;
adding conventional padding gives 98 or another even number, not 97. A length-
preserving outer mask cannot remove padding.

A generic stationary bijection on A–Z digraphs has no Playfair no-double rule.
No aligned input pair repeats here, and the observed aligned output pairs are
distinct under both continuous parities. Therefore those local partial pair maps
extend to a permutation on 26^2 pairs (676 symbols): the outer monoalphabetic map
can be identity for this local existence argument. No complete-message existence
is claimed without an odd-tail convention. If a fixed one-symbol tail transform
is explicitly allowed, length ceases to be the obstacle. A generic pair transform
need not commute with reversal; imposing that property would be an extra hypothesis.

Periodic outer masks preserve a pair's no-double property only when both slots
use the same map. Consecutive positions have different residues for q>1. Repeated
pairs remain testable only when corresponding slots share schedules. Physical
row crossing splits BER|LINCLOCK and changes some pair boundaries, but establishes
no cryptographic reset by itself.

## Length and local-span audit

Every outer map in the main invariant table, including feedback with one output
per input and transposition, preserves the length of X. It cannot repair a mismatch.
It does not follow that every variable-rate F is impossible for this particular P.

| Inner process | Length rule | Consequence for 97 |
|---|---|---|
| Bifid/Trifid coordinate permutation with shortened end block | Exactly 1:1 on normalized symbols | Compatible; primality gives no exclusion |
| Same construction insisting on full blocks d | Pads to d*ceil(n/d) | To emit 97 directly requires d dividing 97; otherwise a separate deletion/serialization convention is needed |
| Standard Playfair | Prepared text has even length; may insert fillers | Cannot emit exactly 97 with a 1:1 outer stage |
| Generic full digraph substitution | 2 symbols per complete pair | Same odd-length problem; an explicit singleton-tail or indicator rule changes the family |
| Digrafid-like complete-pair construction | Even complete output under the assumed pair rule | Excluded under that rule only; no authoritative offline terminal convention was established in the earlier audit |
| Fractionated Morse | ceil((M+n-1+w)/3) under explicit terminal padding; M Morse marks, w extra word separators | Variable rate; may equal 97 for some input, but is not a universal 1:1 transform |
| Raw 5x5 coordinates / 3D coordinates | 2n / 3n coordinate symbols | Need regrouping/packing to n; letterwise masking alone does not compress |

For Fractionated Morse, the two cribs require 61 Morse marks total. If there are
97 normalized letters, 96 internal letter separators, no word separators and no
terminal padding, 97 ciphertext triples require 291 units, hence 195 marks total.
The 73 unknown letters must contribute 134 marks, within their possible 73–292
range (e.g. a length distribution of 12 one-mark and 61 two-mark codes). This is
only arithmetic compatibility, not a plaintext candidate or a full Morse fit.

The earlier BERLINCLOCK calculation (44 units versus 33 in eleven triples) correctly
rejects **local independent encoding inside those eleven ciphertext slots**.
It does not reject a continuous variable-length decoder whose output places the
word at plaintext positions 63–73 after processing a longer/different ciphertext
span. An outer mask does not fix length, but neither the 97-letter total nor the
plaintext positions alone prove that extra local-span premise. A full ternary-stream
constraint model would need separator, padding and indexing semantics first.

## Periodic masks: testability before searching

For concrete known intermediate positions S and q, additive masks give
`c(q)=|S|-|{i mod q:i in S}|` independent key-equality tests. For arbitrary
bijections the test is instead pairwise equality-pattern compatibility within
each residue. The exact uniform-output probability of matching a given pattern
with n_r observations and k_r distinct inputs is `(26)_(k_r)/26^n_r`, multiplied
over residues; using `26^-c(q)` for arbitrary bijections is wrong.

On the original 24 crib positions the differences are 1–12 within a run and
30–52 between runs. A collision exists precisely when q divides one of these
differences. Therefore no collisions at q=27,28,29 or q>=53; cross-crib coupling
occurs precisely for divisors of 30–52. Counts for *every* q=1..97 are in JSON.
At q=24,25,26 there are 5,3,1 spanning additive tests; counts then recover after
29, reach 11 around 40–44, and vanish above 52. There is no monotone cutoff at 24.

These are **not automatically the counts for F(P)**: compute its dependency
projection S first. Known intermediate outputs can move outside the crib spans,
and full-C symbolic equalities can constrain unknown input coordinates. Hence the
27–29 blind spot from Checkpoint T does not prove vacuity for every internal F.
For arbitrary bijections with q>=97 all 97 output positions have distinct states:
every admissible 97-symbol intermediate sequence fits by choosing each map's one
observed image. That is a genuine non-identifiability theorem, not a parameter
count. For smaller q, no such universal claim is made.

The small audit range is derived rather than chosen for a key search: inner
periods 2 and 3 revisit EXP-013; outer periods 1..97 cover all distinct schedules
on the 97-position message, with q>=97 equivalent for this test. 80 inner labeled
configurations (dimensions 2/3, both reset rules, all phases, all axis orders)
times 97 gives 7,760 propagation decisions. It searches no square or numeric key.

## Result table

| Internal family | Outer mask assumption | Old negative still valid? | Crib constraints | Finite? | New elimination? | Action |
|---|---|---|---|---|---|---|
| Bifid-like | Fixed monoalphabetic | Yes, inventory | Not needed for global proof | All squares/periods covered by theorem | Scope extended to fixed-map chains | Close |
| Bifid-like | Periodic bijections | Inventory globally no; per-phase yes | Shared coordinate equalities, including partial blocks | Specified schedule is finite | Some p=3/q=3,9 cases reject | Retain bounded CSP formulation; no positive evidence |
| Trifid-like | Fixed injective used-cell map | EXP-013 equations no | Tuple collision propagation | 194 origin-zero configurations | 175 reject | Remaining 19 unresolved in this scope |
| Playfair | Fixed monoalphabetic | Inventory, even length, prepared-pair doubles survive | Both pairing parities reject | Square-independent proof | Stronger explicit outer scope | Close standard case |
| Generic digraphic | Fixed monoalphabetic | No-double argument inapplicable | No aligned repeats; local bijective pair extension exists | 676! maps; finite but weakly constrained | No; complete even output excluded | Require a defined tail rule and table structure |
| Fractionated Morse | 1:1 outer mask | Local-span claim conditional | Stream constraints needed | Finite once conventions fixed | No global length elimination | Correct scope; do not run a word/key search |
| Digrafid-like | 1:1 outer mask | Complete-block length proof conditional | Depends on specified terminal convention | Once specified | Even complete-output subclass only | Obtain definition before broader claim |

## Candidate for Claude EXP-040 review

**No evidence-selected EXP-040 candidate is established.** There is a finite
mathematical remainder suitable for review: forward Trifid coordinate-row
concatenation, one shared 3x3x3 cube, shortened terminal blocks, followed by a
fixed injective readout on used cells; origin zero; continuous vs physical-row
reset. The exact residual periods are the 9+10 entries above: **19 configurations**.
Outer relabeling is eliminated existentially; an upper bound before constraints is
19*27!*27!/(27-26)! for cube and injection choices (vast, not a proposed enumeration).
A CSP on coordinate equalities, domain 0..2 and all-different cells is the finite
reduction; unknown inputs must belong to the specified 26-letter subset, and all
97 outputs must occupy at most 26 distinct cells. No extra plaintext is supplied.

Prior EXP-013 directly equated output labels with cube symbols and only searched
p=2,3. EXP-033/036/038/039 do not include coordinate mixing. Complete CSP UNSAT
would falsify each residual configuration; a satisfying partial-crib completion
would establish compatibility only. An independent historical reason for this
particular fractionator, schedule or cube is still absent. Thus hand Claude the
invariant and certificates, and let the global gate decide; no preregistration
file is created and no other branch is touched.

## Ten requested answers

1. Inventory under fixed maps, complete-output divisibility, and common-map
   Playfair pair inequalities remain valid internally at their specified scope.
2. Literal output labels and P-to-C fixed points disappear; global inventory and
   pair inequalities can disappear under changing maps. Direct Trifid equations change.
3. Yes: equality partition, including multiplicities and distinct count, survives a bijection.
4. Yes: all 25-cell plus fixed-map configurations fail inventory without a square;
   short periodic variants can also fail coordinate equality propagation.
5. Yes: both cribs share letter-coordinate variables and outer residue constraints.
   This need not determine the square or prove a surviving configuration feasible.
6. Yes: p=2 both continuous phases, p=3 phases 0/1, and many larger origin-zero
   periods are falsified in the audited injective-used-cell model.
7. Yes: standard Playfair fails inventory/length and, with prepared indices, pair inequalities.
8. Yes: complete even-output classes fail; shortened Bifid/Trifid blocks preserve 97.
9. Rows justify testing a reset hypothesis, not assuming it. The two reset choices
   yield different certified exclusions and unresolved periods.
10. A finite CSP remainder emerged, but no historically selected experiment family
    passed the evidence gate. Claude should review the mathematical narrowing.

## Reproduction and limits

Run `python audit/checkpoint_AB.py > results/checkpoint_AB.json`, then
`python audit/checkpoint_AB_verify.py`. Python standard library only. The verifier
rebuilds dependencies by arithmetic and uses graph connectivity instead of union-find.
The production audit includes 80 synthetic coordinate controls, concrete-map positive/
negative controls and 388 symbolic-vs-concrete dependency checks. None guesses
unknown K4 letters. Results are deterministic; raw case counts include duplicates.

Read before work: Checkpoints W/T/X/Y/Z, fractionation-frontier-audit,
negative-results, combiner-coverage-matrix; EXP-012/013/033/036/038/039 source,
available preregistrations and stored logs/summary results. All findings here are
conditional on the explicit forward model. No status file or Claude conclusion
is rewritten; this checkpoint supplies additional scope and computation.
