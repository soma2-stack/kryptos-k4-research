# Checkpoint AA — residual multi-stage architecture elimination

**Branch:** `claude/k4-post-j`. **Starting HEAD:** `adf9a1867496928539f50de608efd157e9ba6a2c`.

**Decision up front: `NO EXP-040 JUSTIFIED`.**

Checkpoint W mapped the residual space and correctly concluded that most multi-stage
proposals collapse algebraically. Checkpoint AA does the next thing: it makes the *survivors*
quantitative. The central result is that the highest-ranked residual — Residual W-A, an inner
polygraphic/fractionating stage hidden by an outer mask — is not merely under-motivated. For
almost every block size it is **provably vacuous**: it imposes zero constraint on anything,
so it cannot be an experiment at all.

All exact claims are re-checked by `audit/verify_checkpoint_AA.py` (24 checks, no project
imports). No web search was used; this checkpoint is repo- and mathematics-driven.

---

## 1. The erasure theorem

Everything below follows from one observation that the project had been using informally.

> **AA-Theorem 1 (outer-mask erasure).** Let the architecture end in a position-varying
> monographic stage, `C[i] = M_i(X[i])`, where `X = F(P)` is produced by any inner transform
> `F`. Suppose the mask parameters covering the 24 crib positions are free, and suppose the
> inner family `F` is a free map on blocks. Then the architecture fits the cribs for **every**
> mask assignment, provided no two observed plaintext blocks are equal.

*Proof.* Fix any mask. Invert it at the crib positions to obtain `X[i] = M_i⁻¹(C[i])`, which
is total and well defined. `F` must satisfy `F(block) = image` for each observed block. If all
observed blocks are distinct, these are assignments to distinct arguments of a free function,
so a consistent `F` always exists. ∎

**Corollary (falsifiability budget).** An architecture is testable only if

`(free mask parameters touching cribs) + (free inner parameters actually exercised) < 24`.

Every stage added to the chain spends from a fixed budget of 24. This is the precise,
countable form of Checkpoint T's finding that constraint density — not compute — is binding.

**AA-Theorem 1 also settles the user's question 3.** Every impossibility proof in this
repository is a statement about the **observable end-to-end map**, and by the theorem it
*must* be: an unconstrained outer stage erases all internal structure, so no proof about an
internal stage is even possible from the cribs alone. Checkpoint W was right to flag the
scope issue, but the correct conclusion is stronger than "those proofs were too broad." It is
that **internal-stage proofs cannot exist** until the outer stage is bounded. The path forward
is never "rescue a rejected cipher as an inner stage"; it is "bound the outer stage first."

---

## 2. Residual A resolved: the polygraphic inner stage is vacuous

> **Scope correction added 2026-09-13 at Checkpoint AC (prospective; nothing below is
> rewritten).** This heading is broader than the result it reports. The theorem, the body of
> this section and the ranked-table row all correctly say a **free** inner map on blocks behind
> a **free** outer mask, and that result stands unchanged. Read without those qualifiers the
> heading is false: Codex Checkpoint AB exhibits a **structured** polygraphic inner stage
> (Trifid coordinates on one shared cube) under a **bounded** outer map — a single fixed
> injective readout — for which 175 of 194 configurations are refutable, confirmed
> independently at Checkpoint AC, which closed 4 more of the remaining 19 by exact CSP.
> Checkpoint AC also sharpens this section's corollary: bounding the outer stage is
> **necessary but not sufficient**. With the outer map pinned all the way to the identity, a
> free inner map on digraphs still imposes zero constraints, because the 11 crib digraphs and
> their 11 ciphertext images are each all distinct. Constraints return only when the outer
> stage is bounded **and** the inner stage shares one parameter set across many positions.
> See `docs/analysis/checkpoint-AC-aa-ab-reconciliation-trifid-closure.md`.

The theorem's hypothesis — *no two observed plaintext blocks are equal* — is checkable. It is
the whole ball game, and it had never been checked.

Blocks lying wholly inside a crib, by block size and alignment:

| Block size | Alignment | Full blocks | Distinct | Repeats |
| --- | --- | --- | --- | --- |
| 2 | 0 | 11 | 11 | **none** |
| 2 | 1 | 11 | 11 | **none** |
| 3 | 0 | 7 | 6 | `EAS` at 21 and 30 |
| 3 | 1 | 7 | 6 | `AST` at 22 and 31 |
| 3 | 2 | 6 | 6 | none |
| 4 | all four | 4–5 | = | **none** |
| 5 | all five | 2–4 | = | **none** |

### AA-Result 1 — digraphic and 4/5-graphic inner stages impose *zero* constraint

For block sizes 2, 4 and 5, at every alignment, the observed blocks are all distinct.
By AA-Theorem 1, **every** outer mask is admissible. This covers the entire illustrative list
in the brief — Playfair, Bifid at period 2, Hill 2×2, and any four- or five-symbol
recombination — when the inner stage is left free and hidden behind a mask.

Verified by direct construction rather than by argument alone: over 4,000 random
(period, key) outer masks, a consistent digraphic inner map exists **4,000 times out of
4,000**. Requiring the inner map to be injective, as a real cipher must be, admits 93.6% —
against a birthday null of 92.2% for 11 images drawn from 676. **The injectivity filter is a
coincidence detector, not a cryptanalytic constraint**: it discards true and false models at
the same rate.

This is a stronger and cleaner verdict than "under-motivated". The family is **VACUOUS**. It
fails gate conditions 7 and 10 by construction: no result it could return would falsify
anything. Running it would produce survivors at exactly the chance rate — precisely the
failure mode Checkpoint T identified at periods 27–29.

### AA-Result 2 — the single surviving polygraphic constraint, and it is already spent

Block size 3 is the sole exception: one repeated trigram per alignment, `EAS` at 21/30 and
`AST` at 22/31, **both at distance 9**.

A free trigraphic inner stage forces the intermediate text to repeat at those two places.
Under a periodic additive outer mask of period `p`, the mask cancels only when `p | 9`, and
then the *ciphertext* must repeat. It does not:

- `CT[21:24] = FLR` versus `CT[30:33] = GKS`
- `CT[22:25] = LRV` versus `CT[31:34] = KSS`

**Therefore a free trigraphic inner stage under a periodic additive mask of period 1, 3 or 9
is exactly REFUTED.** For every other period the two trigrams fall in different residue
classes, the mask absorbs the difference, and no constraint survives.

That is a genuine, search-free elimination — and it is also the *complete* extent of what the
current cribs can say about any hidden polygraphic stage. Three periods.

### What this does and does not mean

It does **not** say K4 has no polygraphic stage. It says the 24 crib letters cannot see one
behind a free mask. The question is not open-but-hard; it is **not a question the present data
can be asked**. Pinning the inner stage to a named keyed system (a specific 5×5 square, a
specific Playfair key) would restore testability — and would immediately fail gate condition 5,
because no source names a square, a key, or even a fractionator.

---

## 3. Residual B: mask → transposition → mask

`C[π(j)] = P[j] + a[j mod p] + b[π(j) mod q]` for additive masks and a known `π`.

This does not collapse, correctly, because the two masks are indexed on opposite sides of a
non-commuting permutation (Checkpoint W, W-R4). Its constraint structure is a **bipartite
linear system** over Z26: crib position `j` links class `a[j mod p]` to class `b[π(j) mod q]`.

Independent constraints = `24 − (occupied_a + occupied_b − components)`, which for a connected
generic instance is `24 − (p + q − 1)`:

| p, q | free parameters | generic independent constraints |
| --- | --- | --- |
| 3, 3 | 6 | 19 |
| 5, 5 | 10 | 15 |
| 7, 7 | 14 | 11 |
| **8, 10** | 18 | **7** |
| 10, 10 | 20 | 5 |
| 12, 12 | 24 | 1 |
| 13, 13 | 26 | **−1 — no power at all** |

So the sandwich is genuinely testable for short periods and dies around `p + q ≈ 24`, exactly
as the falsifiability budget predicts. The much-discussed K1/K2 pair (8, 10) retains only
**7** constraints, and only if the bipartite graph is connected — disconnection lowers it
further, and disconnection is common when `π` is structured.

**Verdict: mathematically the healthiest residual, and still a gate failure.** Checkpoint V
found no statement that K4 reuses K1/K2 key lengths or methods. Choosing `{8, 10}` converts
"earlier sections contain clues" into an exact Layer-A inheritance rule that no source states,
and `LAYER TWO` does not supply it. Gate condition 5 fails. Unchanged from Checkpoint W; what
AA adds is that even if the evidence existed, the test would be weak.

---

## 4. Residual C: transposition + feedback / autokey mask

The brief's key question — is this new, or does it only look new because a permutation was
inserted? — has a clean answer under AA-Theorem 1.

A feedback mask draws its key from previous plaintext, ciphertext or key state. Insert a
transposition and the mask's source symbols are read at **permuted** positions. For an unknown
`π`, the lagged source of position `i` is an unknown intermediate symbol, so the mask value at
every crib position is a free unknown. That is exactly the theorem's hypothesis: free mask
parameters covering the cribs, hence **vacuous**.

For a *known* `π` from a declared family the model is testable, but then it is a
reparameterisation of EXP-034 (key as a function of one lagged symbol) and EXP-038
(autonomous recurrence) composed with the EXP-036 permutation corpus — and Checkpoint T's
order-1 functional contradiction already shows the cribs are hostile to low-memory autonomous
state. **Nothing survives that is both new and constrained.** No source names feedback,
autokey or recurrence, so gate condition 1 fails as well.

---

## 5. Residual D: non-shift / changing tableau masks

Unchanged from Checkpoint W, and the falsifiability budget explains why sharply. A
position-varying tableau family has, at minimum, one free row-selection per position unless a
period pins it. With a period `p` the family has `p` table choices; with free tables it has 24
free parameters over the cribs and is vacuous by AA-Theorem 1.

The named cases are closed (Quagmire I–III duplicates, Gronsfeld a subset, standard Porta
negative at EXP-037, Quagmire IV needing an unevidenced second alphabet). What remains is "some
other table", which is a description of a space, not a hypothesis. **Open but non-actionable**,
exactly as the brief anticipated.

---

## 6. Residual E: custom / stateful mask

The documentary record does license a project-specific technique — but "custom" is not
permission to search arbitrary functions, and the budget makes the limit explicit.

The minimum structure that stays historically plausible and hand-teachable is roughly: a
deterministic rule over the 26-letter alphabet, driven by position and/or a short key, runnable
with pencil, paper and a printed tableau, and reproducible by a non-cryptographer after a short
handover (1991 Scheidt). Any such rule with fewer than ~24 free parameters over the cribs is in
principle testable; any with more is not.

The problem is that the evidence names **no rule**, and the space of rules with under 24
parameters is not enumerable without one. **Marked UNTESTABLE WITH CURRENT CRIBS.**

---

## 7. The six algebraic questions, answered

**Q1 — Which two-stage constructions are equivalent to already-tested one-stage models?**
Fixed substitution ∘ fixed substitution (one substitution). Fixed substitution ∘ transposition
in either order, since they commute (EXP-033). Transposition ∘ transposition (one permutation;
pure transposition is impossible by Checkpoint T's multiset proof). Same-index additive masks
with nothing non-commuting between them (one mask of period dividing `lcm`; the 8/10 pair gives
40, inside EXP-001's period ≤ 48 sweep). These are Checkpoint W's W-R1…W-R4, confirmed.

**Q2 — Which survive only because a non-commuting step separates two masks?**
Exactly one class: the sandwich `M2 ∘ π ∘ M1` of §3. That is the whole of it. Feedback masks
separated by a transposition (§4) do not survive — they become vacuous rather than new.

**Q3 — Which old impossibility results were accidentally too broad?**
None were stated too broadly, but the reason is stronger than Checkpoint W recorded: by
AA-Theorem 1, **every** crib-based proof is necessarily a statement about the observable
end-to-end map, and internal-stage proofs are impossible in principle while the outer stage is
free. The scope caveats in `docs/evidence-grades.md` are therefore not a weakness to be
repaired but a structural fact to be planned around.

**Q4 — Does any surviving architecture constrain both crib regions jointly?**
Only the sandwich, and only through `π`. Without a transposition, cross-crib coupling arises
solely from residue collisions, whose exact census is Checkpoint T's period table — zero at
periods 27–29. With a free polygraphic inner stage the two regions are fully independent, since
all blocks are distinct: this is another way of stating AA-Result 1.

**Q5 — Does any surviving model have fewer effective degrees of freedom than 24?**
The sandwich, for `p + q < 24`. Nothing else. The polygraphic residuals have *zero* effective
constraints, not merely too few.

**Q6 — What can be rejected with no search at all?**
Four things, all now established: pure transposition, by the letter-multiset contradiction
(Checkpoint T); direct monoalphabetic substitution, by repeated-letter conflicts; a free
trigraphic inner stage under a periodic additive mask of period 1, 3 or 9, by the absent
ciphertext repeat (AA-Result 2); and — as *unfalsifiable* rather than false — every free
polygraphic inner stage at block size 2, 4 or 5 behind a free mask (AA-Result 1).

---

## 8. Ranked residual table

| Architecture | Evidence support | Already covered? | Algebraically collapses? | Crib-constrained? | Finite? | Action |
| --- | --- | --- | --- | --- | --- | --- |
| Free digraphic / 4- / 5-graphic inner + outer mask | class-level only | no | no | **NO — zero constraints (AA-1)** | n/a | **CLOSE as vacuous** |
| Free trigraphic inner + periodic additive mask | class-level only | no | no | only for `p ∈ {1,3,9}` | yes | **REFUTED at those periods; vacuous elsewhere** |
| Mask → transposition → mask (sandwich) | multi-stage direct; periods **not** evidenced | no | no | yes, `24−(p+q−1)` | yes given `π`, `p`, `q` | **HOLD — fails gate 5** |
| Periodic mask + net permutation outside EXP-036 | low–moderate, structural | partly (EXP-036/039) | no | yes | yes | HOLD — compounds speculation |
| Transposition + feedback / autokey mask | none names feedback | EXP-034/038 in effect | becomes vacuous with unknown `π` | no | no | **CLOSE as vacuous / duplicate** |
| Non-shift / changing tableau + transposition | class-level only | named cases closed | no | only if periodised | no | Open, non-actionable |
| Custom stateful mask | licensed but unnamed | no | n/a | depends on rule | no | **UNTESTABLE WITH CURRENT CRIBS** |
| External-source mask + another stage | shape only, zero source specificity | EXP-004/014/023/024/029–031/035 | no | no | no | Blocked on a named source |
| Homophonic / variable mapping + stage | weak | no | no | no | no | Underconstrained |

---

## 9. EXP-040 gate

The strongest surviving architecture is the **sandwich `M2 ∘ π ∘ M1`**. Against the ten conditions:

| # | Condition | Result |
| --- | --- | --- |
| 1 | one specific architecture survives | **pass** |
| 2 | stage order explicitly defined | pass for a test, but Checkpoints X and Y record that Scheidt **declined** to fix the order — so the definition would be an assumption, not evidence |
| 3 | each stage mathematically defined | pass |
| 4 | finite alphabet conventions | pass — the 12 committed conventions |
| 5 | key/parameter sources finite **and justified** | **FAIL** — no source states any period, key or inheritance from K1/K2 |
| 6 | search size statable in advance | pass |
| 7 | both crib regions constrain the model | pass, weakly — 7 constraints at (8, 10) |
| 8 | not already covered | pass |
| 9 | preregisterable criteria | pass |
| 10 | falsifies a meaningful family | marginal at (8, 10) |

**Condition 5 fails, and conditions 2, 7 and 10 are weak. `NO EXP-040 JUSTIFIED`.**

No preregistration is written and no experiment code is created.

---

## 10. What would unlock this

The falsifiability budget makes the priority arithmetic explicit rather than rhetorical.

1. **A third public crib** — Request 7. Each additional verified plaintext letter raises the
   budget by one, and letters in positions 34–62 or 74–96 also create new block repeats. The
   entire polygraphic residual is vacuous *because there are no repeated blocks*; a handful of
   new letters would very likely create some, converting AA-Result 1 from a closure into a
   real experiment.
2. **One sentence fixing the outer mask** — the unedited Zetter/Scheidt material, or the
   original `ScheidtNova.doc`. By AA-Theorem 1, bounding the outer stage is the *only* way any
   inner stage becomes testable. This is not one option among several; it is the structural
   prerequisite.

Note the two are complementary, not alternatives: (1) raises the budget, (2) lowers the cost.

K4 remains unsolved.
