# Checkpoint W — residual map for multi-stage hand-executable K4 architectures

**Branch:** `claude/k4-post-j`

**Starting HEAD:** `f1484c071d17e0d06262693b1456c5a777627d25`

**Purpose:** take the strengthened Checkpoint-V Layer-A statement — Scheidt described K4 as **more than one stage**, with a **masking technique** involved — and determine which genuinely multi-stage, hand-executable architecture classes remain outside EXP-001…039.

**Decision up front:** **NO EXP-040 JUSTIFIED.** The new evidence changes the ranking of the residual space, but still does not select the missing stage, the stage order, a key schedule, or a bounded parameter family.

The important new result is a **normal-form reduction**: most apparent “multi-stage” proposals collapse algebraically into classes already tested. The live residual is much smaller than “all combinations of classical ciphers.” It consists mainly of architectures containing at least one **non-commuting, state-varying, or polygraphic/fractionating stage**.

---

## 1. Evidence used and what it does not say

Checkpoint V established two points that are load-bearing here:

1. The 2015 Scheidt workshop is direct Layer-A evidence that K4 is **more than one stage** and that a masking technique is involved.
2. Sanborn’s restored K2 phrase `LAYER TWO` is a **real clue** — he directly said solvers had been “missing a clue” — but its target is unresolved. It is **not** admitted as evidence that K4 has exactly two cryptographic stages.

Older documentary constraints remain in force:

- K4’s harder process is strongly supported as **custom/adapted for the project**, not safely assumed to be an unchanged textbook cipher.
- It should suppress ordinary English statistics better than K1–K3.
- It should be realistically teachable/executable in the 1989–90 workflow.
- Sanborn intended eventual solution, so effective key entropy should remain within the project’s EXP-019 recoverability bound rather than act like a one-time pad.
- No direct statement says to reuse `PALIMPSEST`, `ABSCISSA`, K3’s transposition, or any K1–K3 method inside K4.

Therefore “more than one stage” is a **structural filter**, not permission to concatenate arbitrary historical ciphers.

---

## 2. Algebraic collapse rules — why many multi-stage ideas are not new

These reductions are architecture-level facts. They matter because stage count alone does not imply a larger cryptanalytic family.

### W-R1 — fixed substitutions collapse

For fixed monoalphabetic substitutions `S1` and `S2`,

`S2(S1(P)) = S(P)`

for one fixed substitution `S = S2 ∘ S1`.

So two or ten fixed monoalphabetic stages are still one monoalphabetic stage. Direct fixed substitution is already contradicted by the cribs, and fixed substitution composed with the declared transposition families is covered by EXP-033.

### W-R2 — fixed substitution commutes with pure transposition

A fixed letterwise map and a position permutation commute:

`T(S(P)) = S(T(P))`.

Therefore `S → T` and `T → S` are not separate architectures. Any chain containing only fixed substitutions and transpositions reduces to:

`one fixed substitution + one net permutation`.

EXP-033 covers a very large declared one-permutation family; EXP-039 adds nine genuinely new double-columnar net permutations. What remains open is **permutation scope**, not stage count.

### W-R3 — multiple transpositions collapse to one permutation

`T3 ∘ T2 ∘ T1` is just one permutation `π`.

Thus “double transposition” or “three transpositions” is not intrinsically a new algebraic type. Pure transposition remains impossible by Checkpoint T’s letter-multiset proof. A fixed substitution plus multiple transpositions is still the W-R2 normal form.

This is why general double-transposition proposals only matter when their **net permutation lies outside the permutation corpus already tested**.

### W-R4 — same-index Caesar/Vigenère-like shift stages collapse

Two position-preserving additive shift masks compose into one additive shift mask:

`Shift_b(i)(Shift_a(i)(P[i])) = Shift_(a(i)+b(i))(P[i])`.

For periodic masks, the effective period divides `lcm(p1,p2)`. The demonstrated K1/K2 key lengths 10 and 8 would combine to an effective period dividing **40**, which is already inside EXP-001’s direct no-transposition period≤48 search.

So stacking K1/K2-like shifts **without an intervening non-commuting stage** is not a new class.

With a transposition between them, however, the two masks are indexed on different sides of the permutation and no longer collapse. That becomes a genuine residual below.

### W-R5 — evidenced Quagmire/shift-table variants already reduce to existing families

The combiner audit already established:

- Quagmire I–III are set-equivalent to existing STD/KRY shift conventions;
- Gronsfeld is a strict subset of an existentially decided shift key;
- Porta is genuinely distinct under the evidenced orderings, but EXP-037 closed standard Porta direct and composed with the EXP-036 transposition families;
- Quagmire IV remains outside coverage only by introducing a second unevidenced keyed alphabet.

Therefore “try another tableau” is not a residual class until a specific non-shift table family is independently motivated.

---

## 3. What EXP-001…039 already close in multi-stage space

| Normal-form architecture | Status | Existing coverage |
| --- | --- | --- |
| fixed substitution + one declared transposition | **negative** | EXP-033, arbitrary fixed `A–Z→A–Z` map |
| periodic shift/polyalphabetic + one declared transposition, either order | **negative** | EXP-036, periods 2–23, declared T families |
| standard Porta + one declared transposition, either order | **negative** | EXP-037 |
| fixed substitution + the 9 preregistered double-columnar net permutations | **negative** | EXP-039 |
| multiple fixed substitutions | **reduces to one substitution** | crib contradiction / EXP-033 when transposed |
| multiple transpositions only | **reduces to pure transposition; impossible** | Checkpoint T |
| multiple same-index shift stages, no transposition between them | **reduces to one shift schedule** | EXP-001 directly through period 48; broader structured schedules heavily covered |
| row resets / one internal restart / row-local periodicity | **negative at the established boundaries** | EXP-006/015/020 and Checkpoint T |
| low-order autonomous recurrence alone | **negative in declared scope** | EXP-038 + Checkpoint T order-1 functional contradiction |

The crucial consequence is that a surviving “more-than-one-stage” architecture must contain something that **does not algebraically disappear into these normal forms**.

---

## 4. Ranked residual architectures

The table below ranks classes by documentary fit, hand executability, current coverage and whether the present 24 crib letters can realistically decide them.

### Residual A — polygraphic/fractionating inner stage + an outer position-varying mask

**Shape:**

`plaintext → polygraphic/fractionating transform → periodic/irregular masking stage → ciphertext`

Examples such as Playfair/Bifid/Hill are **illustrations of the structural class, not claims that K4 uses them**.

**Why this is genuinely open:** several structural impossibilities in the repository apply when the named system is the **final output stage**. An outer mask can destroy those invariants.

Most importantly, `docs/evidence-grades.md` already records a genuine residual opening:

> a 25-symbol system followed by a second encoding layer that re-expands to 26 letters is **not eliminated at all** by EXP-012’s output-alphabet argument.

So standard 5×5 fractionation is impossible as K4’s final emitted alphabet, but **an inner 25-symbol fractionator followed by a position-varying 26-letter mask is not ruled out by that argument**.

Likewise, a final mask can hide fixed points, doubled-letter restrictions, and simple inner-stage frequency structure that would otherwise reject a stand-alone classical system.

**Documentary grade:** **MODERATE STRUCTURAL FIT**. Scheidt’s “more than one stage” + masking language makes this class more relevant than it was before Checkpoint V, and fractionation is hand-executable and historically grounded. No source names a fractionator.

**Why it does not become EXP-040:** the evidence does not choose the inner grid/table, block rule, period, outer mask, alphabet, or stage parameters. Once those are left free, the model becomes underdetermined. A named inner system chosen only because its stand-alone form was previously rejected would be a rescue pattern.

**Current verdict:** **highest-value structural residual, but not bounded by evidence.**

---

### Residual B — mask → transposition → mask (“sandwich”)

**Shape:**

`M_pre → T → M_post`

where at least one mask varies with position. This is genuinely different from EXP-036’s one-mask-plus-transposition architecture because the pre- and post-transposition masks are indexed on **different positions** and cannot generally be collapsed through `T`.

For additive masks the crib equation has the form, schematically:

`effective_difference(j) = a[j mod p] + b[π(j) mod q]`

rather than one residue-class key. This is a low-rank two-index structure, not an arbitrary per-position key.

**Special motivated-looking subcase:** periods **8 and 10**, inherited only as the demonstrated K2/K1 key lengths. That would be finite and potentially crib-falsifiable for a fixed transposition family.

**But:** Checkpoint V found **no direct statement that K4 reuses K1/K2 key lengths or methods**. Choosing `{8,10}` would therefore convert an ambiguous “earlier sections contain clues” report into an exact Layer-A inheritance rule that no source actually states.

`LAYER TWO` also does not fix this: it is a genuine clue, but its Layer-A meaning is unresolved and it does not say “two masks.”

**Documentary grade:** **LOW–MODERATE**. Multi-stage is direct; the specific sandwich architecture is inference.

**Current verdict:** **nearest clean algebraic residual among monographic hand ciphers, but fails the evidence gate.**

---

### Residual C — periodic shift/polyalphabetic mask + a net permutation outside EXP-036

**Shape:**

`periodic mask ↔ permutation`

where the net permutation is outside the declared EXP-036 corpus.

Two concrete openings exist:

1. net permutations produced by wider/keyed transpositions outside the width limits;
2. the nine double-columnar net permutations from EXP-039, now paired with a **periodic** rather than fixed monoalphabetic mask.

The second is finite in principle: EXP-039 already froze nine exact net permutations, and a periodic shift schedule could be tested on top of them.

**Why it is not EXP-040 now:** EXP-039 itself graded the double-columnar keyword choice as **structural, not documentary**. Adding a periodic mask stacks one speculative architectural choice on another. No source says K4 uses double columnar transposition, and no source says those three Kryptos words are transposition keys.

**Documentary grade:** **LOW–MODERATE**.

**Current verdict:** technically testable, evidentially under-motivated.

---

### Residual D — transposition + stateful/autokey/feedback mask

**Shape:**

`T ↔ R`

where `R` evolves from plaintext, ciphertext, or previous key state.

EXP-008 tests many feedback/autokey forms **without** a general transposition. EXP-038 closes one autonomous order-2 affine recurrence **without transposition**. EXP-036’s transposition layer uses periodic shift keys, not feedback.

So the composition is not globally closed.

**Why it remains low-ranked:** no Sanborn/Scheidt source names feedback, autokey, recurrence, or self-evolving state. Checkpoint T also found the cribs hostile to low-memory autonomous state. Extending a failed low-order state model by inserting a transposition would be exactly the sort of rescue move the project has tried to avoid.

**Documentary grade:** **WEAK**.

**Current verdict:** open logically, not experiment-grade.

---

### Residual E — periodic/state-varying non-shift tables + transposition

**Shape:**

`position-varying table family ↔ T`

The live gap in the combiner matrix is a periodic/state-varying table family that is **not** one of the three shift forms.

Coverage already removes the obvious named cases:

- Quagmire I–III: duplicates;
- Gronsfeld: subset;
- standard Porta: EXP-037 negative;
- Quagmire IV: requires an unsupported second alphabet.

A free periodic 26×26 table is not a meaningful finite hypothesis; with enough free table entries it becomes an arbitrary fit to the cribs.

**Documentary grade:** **MODERATE at the class level, near-zero for any specific remaining table family**. “Masking” is consistent with it, but no table is named.

**Current verdict:** model-selection blocked, not compute blocked.

---

### Residual F — custom full-26 fractionation, with or without another stage

A custom fractionator that emits all 26 letters, preserves total length 97, and remains compatible with the positional crib semantics is not eliminated by the named-classic audit.

This includes constructions where fractionation itself is the masking stage, and constructions where it is composed with transposition or a second mask.

**Documentary grade:** **WEAK–MODERATE**. Fractionation naturally masks frequency structure and is historically hand-operable, but no source identifies it.

**Testability:** poor until exact equations are frozen. “Custom full-26 fractionation” is a description of a design space, not a cipher.

**Current verdict:** real residual, unbounded.

---

### Residual G — external-source mask + another stage

A running key or externally read source could be composed with a transposition/fractionator and remain outside several direct-source negatives.

However Checkpoint U demoted artistic referents (World Clock, Morse, compass, panel geometry) as **Layer-A key sources**, and EXP-004/014/023/024/029–031/035 already exhausted every source the project can currently name in their declared direct uses.

Without an independently identified source, “external running key + something” has an unbounded source parameter.

**Documentary grade:** **MODERATE shape / ZERO source specificity**.

**Current verdict:** blocked on evidence naming a source.

---

### Residual H — homophonic/variable mapping + another stage

Length-preserving variable mappings can suppress frequencies strongly, and an outer/inner transposition would make them still harder.

But the project’s testability analysis already shows free-selector / multi-chart homophonic families have enormous accidental-fit counts with only 24 crib letters. No named table or selector rule is documented.

**Documentary grade:** **WEAK**.

**Current verdict:** underconstrained with current cribs.

---

## 5. A key structural consequence of the new multi-stage evidence

Several old “impossibility” results must continue to be read at their stated scope:

- `Playfair impossible` means **Playfair as the observed final monographic/polygraphic mapping at the crib positions**, not “Playfair can never appear as an inner stage followed by a mask.”
- `25-symbol output impossible` means a 25-symbol system cannot be the **final output inventory**; it does not eliminate a 25-symbol inner stage followed by a position-varying 26-letter outer encoding.
- direct Hill/reflector/fractionation negatives do not automatically eliminate those mechanisms when an outer non-commuting mask changes the observable invariants.

This is **not a revival of those named ciphers**. It is a scope correction forced by the now-stronger evidence that K4 is multi-stage.

The right research object is therefore not “which rejected cipher should be rescued?” It is:

> **what kinds of inner-stage invariants survive an unknown outer mask, and which outer-mask classes are constrained enough by the 24 cribs to make the inner stage testable?**

That is a better formulation than another historical-cipher catalogue sweep.

---

## 6. Constraint-density reality check

Checkpoint T remains binding: the bottleneck is constraint density, not CPU time.

Every added stage introduces intermediate symbols or additional key/state parameters. With only 24 known plaintext positions:

- fixed maps and short periodic masks are strongly rejectable because repeated plaintext letters or residue collisions create exact equalities;
- polygraphic stages consume unknown neighboring plaintext and sharply reduce local constraints;
- two independent masks can use most of the 24 equations merely to determine their own states;
- independent row/block resets destroy cross-crib equalities;
- periods 27–29 remain a complete blind spot for message-aligned periodic equality tests.

Therefore a residual can be logically open and still be scientifically untestable with the present cribs.

A third public crib remains the single most valuable cryptanalytic input.

---

## 7. EXP-040 gate applied to the nearest candidates

### Candidate W-A: named inner fractionator + outer periodic mask

- documentary support for **multi-stage + masking:** passes at class level;
- documentary support selecting a particular fractionator: **fails**;
- exact equations/bounded parameters: fails until a particular square/grid/block rule and mask are named;
- crib power: unknown and likely highly family-dependent;
- risk of post-hoc rescue: high, because the outer mask can be used to resurrect a stand-alone family already rejected.

**Gate result: FAIL.**

### Candidate W-B: periods 8 and 10 around a transposition

- exact definition: can be frozen;
- bounded: yes for a declared transposition family;
- likely falsifiable: yes in principle because the two periodic masks impose shared residue parameters rather than 97 free values;
- documentary support for multi-stage: strong;
- documentary support for **reusing K1/K2 periods 8 and 10 around K3-like transposition:** **fails**. Checkpoint V explicitly found no such inheritance statement.

**Gate result: FAIL on evidence, despite good mathematical form.**

### Candidate W-C: the nine EXP-039 double-columnar permutations + periodic mask

- exact/bounded: yes;
- crib power: computable;
- documentary support for periodic masking: moderate by precedent;
- documentary support for those double-columnar keys/permutations: weak/structural only;
- adding the mask compounds speculative assumptions.

**Gate result: FAIL on evidence.**

No other residual comes closer without adding still more free structure.

---

## 8. Durable conclusion

The new Scheidt evidence does **not** reopen the entire historical-cipher catalogue. It does something more useful:

1. It confirms that **single-stage untouched ciphers are now a poor default model**.
2. Algebra removes most naive multi-stage combinations because fixed substitutions and transpositions collapse, and same-index shift masks collapse.
3. The genuine live space is concentrated in architectures with at least one:
   - polygraphic/fractionating inner stage hidden by an outer mask;
   - mask on **both sides** of a non-commuting transposition;
   - state-varying non-shift table;
   - stateful/external-source component;
   - custom full-26 fractionator.
4. Every one of those residuals is currently blocked by **missing model-selection evidence or missing crib constraints**, not by lack of compute.

> **NO EXP-040 JUSTIFIED.**

The best immediate documentary target remains the unedited Zetter/Scheidt material, because one sentence identifying the base stage or the operational meaning/order of “masking” could collapse this residual map into a finite experiment.

The best cryptanalytic target remains Request 7: one additional position-specific public K4 plaintext letter, especially in positions 34–62 or 74–96.

K4 remains unsolved.
