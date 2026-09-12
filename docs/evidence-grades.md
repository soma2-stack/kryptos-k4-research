# Evidence grades — audit of Checkpoint B

Written 2026-09-12 (session 3), before continuing. Several Checkpoint B conclusions
were stated more universally than the arguments support. This regrades every one of
them against a five-level scale, and says exactly what each argument does **not**
cover.

| Grade | Meaning |
| --- | --- |
| **PROVED IMPOSSIBLE** | A logical contradiction, given an explicitly stated model class. |
| **EXHAUSTIVELY ELIMINATED WITHIN A SPECIFIED MODEL** | The whole parameter space of a named model was solved or searched to completion. |
| **STRONGLY DISFAVORED** | Statistical evidence, with a stated null and a stated plaintext assumption. Not a proof. |
| **HEURISTIC NEGATIVE** | A search that did not finish, or a sampled rather than complete space. |
| **UNTESTABLE WITH CURRENT DATA** | The evidence cannot decide it. Not the same as false. |

---

## The scoping error that matters most

Three of Checkpoint B's headline results — the three-alphabet lower bound, the
alphabet-free period elimination, and the crib-conflict census — all rest on the
same hidden premise:

> plaintext position *i* is enciphered to ciphertext position *i* by a substitution
> acting on one letter at a time.

That is the class of **monographic, position-preserving substitution ciphers**.
Inside it, those results are proofs. Outside it they say nothing:

- under any **transposition**, P[i] no longer pairs with C[i], so the "conflicts"
  are between letters that were never enciphered together;
- under any **fractionating or polygraphic** cipher (bifid, trifid, Hill, Playfair),
  a ciphertext letter is not a function of a single plaintext letter at all.

I previously wrote "at least three encryption alphabets are forced" without that
qualifier. **Corrected**: at least three alphabets are forced *if the cipher is
monographic and position-preserving*. The same qualifier attaches to "the shortest
period K4 could have is 8".

This matters for the direction this session takes: a physical lookup or overlay
mechanism need not be position-preserving, so these results do not constrain it.

---

## Regraded conclusions

### Three alphabets forced (EXP-009)
**PROVED IMPOSSIBLE** — that two alphabets suffice — **within monographic,
position-preserving substitution ciphers.** Witness: plaintext `E` at positions 21,
30, 64 → `F`, `G`, `Y`. Robust across all 49 crib alignments (EXP-017).
**Does not constrain:** transposition-composed, polygraphic or fractionating systems.

### Period elimination {1–7, 9, 10, 14, 15, 17} (EXP-011)
**PROVED IMPOSSIBLE within the same class.** {1–7, 9} robust across all alignments.
**Does not constrain:** anything with a transposition layer.

### All 26 letters occur → fractionation dead (EXP-012)
Previously stated far too broadly. Split:

- **PROVED IMPOSSIBLE:** any cipher whose *final output alphabet* has fewer than 26
  symbols — standard 5×5 Playfair, bifid, two-square, four-square, ADFGX, ADFGVX,
  Baconian. A symbol that does not exist cannot be printed.
- **STRONGLY DISFAVORED, not proved:** 36-cell (6×6) fractionation carrying 26
  letters + 10 digits. All 97 outputs would have to avoid the 10 non-letter cells:
  P ≈ 2.0 × 10⁻¹⁴ under a uniform model. Overwhelming, but a probability.
- **STRONGLY DISFAVORED:** a 26-cell rectangular Polybius (2×13). Mixed coordinate
  pairs are mostly not valid cells; P(all 97 outputs valid) ≈ 1.4 × 10⁻⁷⁹.
- **NOT ELIMINATED AT ALL:** a 25-symbol system followed by a *second encoding
  layer* that re-expands to 26 letters. The coverage argument sees only the final
  layer. This is a genuine residual opening and was wrongly closed before.
- Trifid (27 cells, 1 filler): **STRONGLY DISFAVORED** on coverage (P(filler never
  printed) ≈ 0.026), and **EXHAUSTIVELY ELIMINATED WITHIN MODEL** at periods 2–3
  (EXP-013). Periods ≥ 4: **UNTESTABLE WITH CURRENT DATA.**

### Low IoC → pure transposition dead (EXP-007)
**STRONGLY DISFAVORED, not proved.** Correctly stated it is conditional on the
plaintext being ordinary English. But the audit makes it *stronger* than I credited:
a transposition preserves IoC exactly, so the plaintext would need IoC ≈ 0.036 —
**flatter than uniform random (0.0385)**, not merely non-English. A pure
transposition therefore requires an anti-clustered plaintext, which no natural
language produces. Grade stands as statistical, but the required alternative is
extreme. **Does not constrain:** substitution *followed by* transposition, which was
always outside the claim.

### Reflector machines; Playfair (EXP-007)
**PROVED IMPOSSIBLE given the recorded crib positions**, but **alignment-contingent**:
EXP-017 shows the violating observations do not survive every ±3 crib offset.
Downgrade to **STRONGLY DISFAVORED** until `data/k4.json` is checked against a
primary transcript.

### The linear-model sweeps (EXP-006, 008, 015, 016)
**EXHAUSTIVELY ELIMINATED WITHIN A SPECIFIED MODEL** — correct as stated. Each
solved a named parameter-linear family to completion with an exact solver and a
planted control. They say nothing about families outside the stated form.
EXP-016's order-B corner for progressive/polynomial models remains **UNTESTED**.

### The 112.8-bit testability frontier (EXP-011)
The sharpest correction. Parameter entropy alone does **not** prove a model
unfalsifiable. The counting argument assumes the model behaves *generically* — that
its parameters can be tuned independently to hit arbitrary crib letters. A
**structured** high-dimensional model can be perfectly falsifiable: its constraints
may be non-generic and its solution set provably empty.

Regrade: the frontier is a **heuristic for spotting overparameterized models**, not
a proof of unfalsifiability. Restated correctly:

> The penalty applies to **free** parameters, not to dimensionality.

This is decisive for what follows. A mechanism **determined by a physical object** —
a clock face, a tableau, a compass rose, a projection — may have thousands of
"entries", but none of them is fitted: they are all read off the object. Such a model
has close to **zero free parameters** and is therefore *maximally* testable, however
large it looks. The frontier argument does not block the physical direction; it
actively recommends it.

### The Mengenlehreuhr keystream (EXP-002)
Sound experiment, **wrong object.** Sanborn clarified in November 2025 that
`BERLINCLOCK` refers to the **Weltzeituhr** at Alexanderplatz, not the
Mengenlehreuhr. EXP-002 remains a valid elimination of the Set-Theory-Clock lamp
count, and is now also **not the principal BERLINCLOCK test**. That test had not
been run. It is the business of this session.

---

## Net effect on the hypothesis space

Nothing that was eliminated inside a stated model becomes alive again. What changes:

1. The strongest structural results are **conditional on the cipher being monographic
   and position-preserving** — so a physical, non-position-preserving mechanism is
   unconstrained by them.
2. A 25-symbol system **followed by another encoding layer** was wrongly closed and is
   re-opened.
3. The evidence-budget argument **does not** rule out physically-determined
   mechanisms, because those have no free parameters to penalise.
4. The principal `BERLINCLOCK` experiment has not yet been performed.
