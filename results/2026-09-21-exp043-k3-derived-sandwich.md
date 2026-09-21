> **Prospective verification correction — 2026-09-21.** The registered affine-mod-97 EXP-043 negative remains unchanged. The K3 motivation is now independently reproduced by `audit/verify_exp043_k3_derivation.py`: an explicit 8x42 -> 24x14 double-rotation route reproduces all 336 K3 ciphertext letters and yields the cited 191/192 differences and 168+168 cycle type. The historical claim of "12 exact route descriptions" is not load-bearing because that scratch enumeration was not committed. K3 plaintext provenance remains `verified:false` pending a separately frozen primary/public source. See `docs/exp043-k3-derivation-verification-2026-09-21.md`.

# EXP-043 — `M2 ∘ π ∘ M1` with `π` derived from K3

**Branch:** `claude/dreamy-archimedes-79k6u0`. **Starting HEAD:** `5b8fcac`.
**Preregistration:** `docs/exp043-preregistration.md`, committed at `2d5a2a4` **before** implementation.
**Code:** `experiments/exp043_k3_derived_sandwich.py`. **Verifier:** `audit/verify_exp043.py`.

## Result

**15,197,184 configurations decided. 0 FEASIBLE.** All three controls pass; independently
verified three ways. **No K4 crib score was consulted in deriving any parameter.**

## Phase 1 — K1–K3 re-derived from repository data, not from description

The cipher-side rows concatenate to 869 characters and split at the `?` marks into K1 63, K2 372,
K3 337, K4 97; the K4 segment reproduces `data/k4.json` exactly.

| section | mechanism, re-derived here | status |
| --- | --- | --- |
| K1 | Vigenère, **KRY plaintext / KRY ciphertext**, keyword **PALIMPSEST** | **exact match** |
| K2 | Vigenère, **KRY/KRY**, keyword **ABSCISSA** | first **361** characters exact; the tail diverges at the documented omitted character — K2's ciphertext carries 369 letters against a 370-character intended plaintext |
| K3 | **pure transposition** — ciphertext and plaintext letter multisets identical, so no substitution, no key alphabet, **no period at all** | permutation recovered exactly |

**K3's permutation was recovered as a concrete object.** Searching rectangular route compositions
against K3's own published plaintext gives 12 exact descriptions — `(7,48)→(84,4)`,
`(14,24)→(42,8)`, `(21,16)→(28,12)`, each in two readout conventions — and **all 12 induce one and
the same permutation** of the 336 positions. Its first differences take exactly two values (191
and 192); its cycle type is two 168-cycles; its order is 168; it is not an involution.

## Phase 2 — the decisive arithmetic

**The exact K3 principle has no K4 instance.** A rectangular route needs `r × c = n` with
`1 < r, c < n`. K3's 336 admits **18** such rectangles. **97 is prime and admits 0.** Any
"resizing" therefore breaks the K3 rule and lands in ragged keyed columnar — already covered by
EXP-033 and EXP-036.

**What does transfer is the readout's defining local property.** K3's permutation advances by a
near-constant stride (first differences only 191 and 192 — the signature of a column readout). At
a **prime** length the constant-stride readouts are exactly the **affine maps** `i ↦ a·i + b mod 97`.
That family is the unique faithful instantiation of K3's readout principle at `n = 97`, and it is
finite: **9,312 permutations**. The mask class — short periodic Vigenère over KRY — was likewise
re-derived from K1 and K2 rather than assumed.

## Secondary question: is there a design rule across K1–K3? — Falsified, not merely unsupported

Any rule extrapolating a K4 period from PALIMPSEST (10) and ABSCISSA (8) **requires K3 to have a
key length. It has none** — K3 is a pure transposition, proven here by the identical letter
multisets. The `(8,10)` pair is therefore **not** independently warranted, and entered this
experiment only as two ordinary members of a declared sweep, never as a privileged choice.

## Phase 3 — canonicalisation, including a corrected hypothesis

- **`π` and `π⁻¹` are both in the corpus** — the affine family is closed under inversion, verified
  for all 96 multipliers. Orientation adds nothing.
- **The offset `b` is NOT absorbed by mask phase.** I hypothesised it was, tested it, and the test
  refuted it: because 97 is prime, no `q < 97` divides it, so reducing `(a·j + b) mod 97` again
  mod `q` is not a clean shift of the mask index. **Witness: `a = 1, p = 3, q = 9` gives
  `d_eff ∈ {9, 10, 11}` across `b`.** The full 9,312 corpus was retained — the conservative choice.

## Phase 5 — budget, fixed before implementation

Period range `p, q ≥ 2` with `p + q ≤ 19`, chosen **by the discrimination criterion alone**:
**136 ordered pairs** (M1 and M2 occupy distinct roles, so ordering matters — the preregistration
quoted the unordered count of 57, and the ordered count is the correct reading).

`N` = 9,312 × 136 × 12 = **15,197,184**; `log₂₆(N)` = **5.08**; worst `d_eff` = **18**;
**budget 23.08 < 24 — passes.** Expected accidental survivors ≈ 2.3 × 10⁻³.

## Controls — all pass

1. **Positive.** A planted `a=7, b=13, p=5, q=6` instance carrying the **real cribs at the real
   positions** is accepted.
2. **Permutation control.** A random permutation was verified to be genuinely **out of family**
   (not affine mod 97) and is rejected — the corpus never silently admits a non-affine `π`.
3. **Adversarial crib control.** Corrupting a constrained position flips feasibility.

## Independent verification — all checks pass

`audit/verify_exp043.py` imports neither the experiment nor `k4lib`.

- **Route A — cycle certificates.** The experiment used weighted union-find; the verifier instead
  extracts an explicit cycle and evaluates the alternating key sum around it. A non-zero sum is a
  self-contained proof of infeasibility. **4,000 sampled configurations, 4,000 certificates, none
  unproven.**
- **Route B — forward simulation, no graph theory.** **435,955,104** explicit mask pairs
  enumerated and encrypted forward; zero feasible.
- **Route C — the underlying facts re-derived**: the 869-character stream, K1's exact decryption,
  K3's pure-transposition property, the primality of 97, the 18 rectangles of 336, the corpus size,
  inversion closure and the budget.

## What is now closed, stated narrowly

The **only** permutation family that K1–K3 determine for K4 — the affine-mod-97 maps, being the
unique prime-length instantiation of K3's constant-stride readout — composed with two short
periodic Vigenère masks over the declared alphabets and period range, is **exhaustively negative**.

This does **not** eliminate: non-affine permutations; periods with `p + q > 19`; masks outside the
periodic Vigenère class; three or more stages; or any `π` that a future source might name.

**Class A is now materially weakened as the strongest surviving architecture.** Its `π` was the
one parameter K1–K3 could plausibly supply, and the supply has been exhausted: the exact K3
principle is arithmetically impossible at length 97, and its faithful prime-length surrogate is
now tested and negative.

K4 remains unsolved.
