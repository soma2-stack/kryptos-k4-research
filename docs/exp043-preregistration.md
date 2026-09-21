# Preregistration — EXP-043: `M2 ∘ π ∘ M1` with `π` derived from K3

**Branch:** `claude/dreamy-archimedes-79k6u0`. **Written before implementation.**
**Starting HEAD:** `5b8fcac3b5508a32be7567dacc46d8f24222f274`.

**No K4 crib score was consulted at any point in the derivation below.** Every parameter comes
from K1–K3 mechanics re-derived from repository data, or from the arithmetic of 97.

## 1. Phase 1 — K1–K3 mechanics, re-derived from the data

Cipher-side rows 1–28 concatenate to 869 characters and split at the `?` characters into
K1 63, K2 372, K3 337, K4 97. The K4 segment reproduces `data/k4.json` exactly.

| section | mechanism, independently re-derived | status |
| --- | --- | --- |
| **K1** | Vigenère, **plaintext alphabet KRY, ciphertext alphabet KRY**, keyword **PALIMPSEST** (10) | **exact match** to the repository plaintext |
| **K2** | Vigenère, **KRY/KRY**, keyword **ABSCISSA** (8) | matches the first **361** characters exactly; the tail diverges at the documented omitted character (K2's ciphertext carries 369 letters against a 370-character intended plaintext) |
| **K3** | **pure transposition** — ciphertext and plaintext letter multisets are identical, so there is no substitution, no key alphabet and **no period at all** | permutation recovered exactly |
| **K4** | unknown | — |

**K3's permutation was recovered as a concrete object**, not described from memory. Searching
rectangular route compositions against K3's own published plaintext yields 12 exact
descriptions — `(7,48)→(84,4)`, `(14,24)→(42,8)`, `(21,16)→(28,12)`, each with two readout
conventions — and all 12 induce **one and the same permutation** of the 336 positions. Its first
differences take exactly two values (191 and 192); its cycle type is two cycles of length 168;
its order is 168; it is not an involution.

## 2. Phase 2 — what does and does not transfer to K4

**The exact K3 principle has no K4 instance.** K3's permutation is a composition of rectangular
column readouts, which requires a rectangle `r × c = n` with `1 < r, c < n`. K3's length 336 has
**18** such rectangles. **97 is prime and has 0.** This is arithmetic, not judgement: the K3 route
principle cannot be instantiated at K4 length, and any "resized" version necessarily breaks the
rule and lands in ragged keyed columnar, already covered by EXP-033 and EXP-036.

**What does transfer is the readout's defining local property.** K3's permutation advances by a
near-constant stride — its first differences take only the two adjacent values 191 and 192, which
is exactly what a column readout does. At a **prime** length the constant-stride readouts are
precisely the **affine maps** `i ↦ a·i + b (mod 97)`. That family is therefore the unique faithful
instantiation of K3's readout principle at `n = 97`, and it is finite: `a` ∈ 96 units, `b` ∈ 97
offsets, **9,312 permutations**.

**The mask class is likewise K1/K2-native**: a short periodic Vigenère over the KRY alphabet,
which was re-derived from the data above rather than assumed.

**Explicitly rejected derivations:** arbitrary route catalogues; random grids; generic geometric
traversals; keyword permutations on unsupported words; any clock or compass route motivated by
`BERLINCLOCK` or `EASTNORTHEAST` appearing in the plaintext (Layer B semantics, per Checkpoint U).

**Secondary question — is there a period or parameter rule across K1–K3?** **No, and it is
falsified rather than merely unsupported.** Any rule extrapolating a K4 period from PALIMPSEST(10)
and ABSCISSA(8) requires K3 to have a key length. K3 is a pure transposition and has none. The
`(8,10)` pair is therefore **not** independently warranted, and is admitted below only as two
ordinary members of a declared period sweep, never as a privileged choice.

## 3. Phase 3 — canonicalisation

- **`π` and `π⁻¹` are both in the corpus.** The affine family is closed under inversion (verified
  for all 96 multipliers), so orientation contributes **no** additional configurations.
- **The offset `b` is NOT absorbed by mask phase.** This was tested, not assumed. Because 97 is
  prime, no `q < 97` divides it, so reducing `(a·j + b) mod 97` further mod `q` is not a clean
  shift of the mask index. Witness: `a = 1, p = 3, q = 9` gives `d_eff ∈ {9, 10, 11}` across `b`.
  **The full 9,312 corpus is retained** — the conservative choice.
- Duplicate constraint systems are collapsed at run time by canonical form, as in EXP-041/042.

## 4. Phase 4 — the model

`C[π(j)] = combine(P[j], M1[j mod p] + M2[π(j) mod q])`, a bipartite system over Z26 whose
solvability is decided exactly by weighted union-find with potentials.

## 5. Phase 5 — budget, computed before implementation

- **Declared period range: `p, q ≥ 2` with `p + q ≤ 19`** — 57 pairs. This cut was chosen **by the
  discrimination criterion alone**, before any K4 test, as the largest range keeping expected
  survivors below 0.01.
- `N` = 9,312 × 57 × 12 conventions = **6,369,408**; `log₂₆(N)` = **4.81**.
- Worst-case `d_eff` over the declared range = **18** → **budget 22.81 < 24. PASSES.**
- **Expected accidental survivors ≈ 2.3 × 10⁻³** (conservative: computed at `N` = 12.7M).

## 6. Decision rule

**FEASIBLE** iff the bipartite system is consistent over Z26. No English scoring, no ranking of
near misses, no thresholds. A configuration satisfies all 24 authenticated crib equations or it
does not.

## 7. Controls

1. **Positive.** A synthetic 97-character instance built from one registered `π` and mask
   configuration, preserving the **real crib plaintext at the real K4 positions**; the solver must
   accept it and recover the mask values.
2. **Permutation control.** A known **out-of-family** permutation (not affine mod 97) must not be
   silently accepted as an in-family case.
3. **Adversarial crib control.** Modify a constrained position; feasibility must change.

## 8. Verification

An independent verifier, not importing the experiment, must reconstruct the permutation
generation, the canonicalisation, the parameter counts, the constraint ranks, the feasible total
and the controls — preferring algebraic infeasibility certificates.

## 9. If a survivor appears

It is **not** a solution. Required before any claim: reconstruct the full 97-character plaintext;
verify exact re-encryption to canonical K4; confirm no parameter was selected using crib
information; verify independently; and identify predictions **outside** the two known crib
intervals. A serious survivor must make new predictions.

## 10. Prohibited post-hoc moves

No widening of the period range, the permutation family, the alphabets or the conventions after
seeing results; no language scoring; no promoting `(8,10)` on the basis of its constraint count.
