"""Independent verification of the exact claims made at Checkpoint AA.

Standalone: imports no project code, rebuilds the crib pairs from data/k4.json.

AA-A  Block-distinctness. For block sizes 2, 4 and 5, at EVERY alignment, no two
      blocks lying wholly inside a crib are equal. For block size 3 exactly one
      repeated block exists per alignment 0 and 1, at distance 9.

AA-B  Erasure. If an inner stage is a free map on blocks and no two observed
      blocks are equal, the intermediate text is unconstrained at the crib
      positions, so ANY outer mask assignment is realisable. Demonstrated by
      explicit construction of a witness for an arbitrary mask.

AA-C  The one surviving polygraphic constraint: a free trigraphic inner stage
      under a periodic additive mask of period p dividing 9 is REFUTED, because
      the repeated trigram would force a ciphertext repeat that does not occur.
"""
import json, os, sys, collections, random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K4 = json.load(open(os.path.join(ROOT, "data", "k4.json")))
CT = K4["ciphertext"]
fails = []


def check(label, cond):
    print(f"   [{'PASS' if cond else 'FAIL'}] {label}")
    if not cond:
        fails.append(label)


P = {}
for cr in K4["confirmed_cribs"]:
    s, pt = cr["start"], cr["plaintext"]
    assert CT[s:s + len(pt)] == cr["ciphertext_segment"]
    for j, ch in enumerate(pt):
        P[s + j] = ch

print("## 0. Inputs")
check("97-character ciphertext", len(CT) == 97)
check("24 known plaintext positions", len(P) == 24)


def full_blocks(b, align):
    """Blocks of size b at the given alignment lying wholly inside a crib."""
    out = []
    start = align
    while start + b <= 97:
        if all(start + t in P for t in range(b)):
            out.append((start, "".join(P[start + t] for t in range(b))))
        start += b
    return out


print("\n## AA-A  block distinctness")
for b in (2, 4, 5):
    for align in range(b):
        blocks = full_blocks(b, align)
        words = [w for _, w in blocks]
        check(f"size {b} alignment {align}: {len(words)} blocks, all distinct",
              len(words) == len(set(words)))

tri_repeats = {}
for align in range(3):
    blocks = full_blocks(3, align)
    counts = collections.Counter(w for _, w in blocks)
    rep = [w for w, n in counts.items() if n > 1]
    tri_repeats[align] = [(w, [s for s, x in blocks if x == w]) for w in rep]
    print(f"   size 3 alignment {align}: repeats {tri_repeats[align]}")
check("alignment 0 repeats exactly EAS at 21 and 30",
      tri_repeats[0] == [("EAS", [21, 30])])
check("alignment 1 repeats exactly AST at 22 and 31",
      tri_repeats[1] == [("AST", [22, 31])])
check("alignment 2 has no repeat", tri_repeats[2] == [])
check("both repeats sit at distance 9", 30 - 21 == 9 and 31 - 22 == 9)

print("\n## AA-B  erasure: a free digraphic inner stage admits ANY outer mask")
random.seed(20260913)
LET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
TRIALS = 4000
as_function = 0
also_injective = 0
for trial in range(TRIALS):
    p = random.randrange(2, 26)
    mask = [random.randrange(26) for _ in range(p)]
    blocks = full_blocks(2, trial % 2)
    inner = {}
    consistent = True
    for start, word in blocks:
        img = "".join(LET[(LET.index(CT[start + t]) - mask[(start + t) % p]) % 26]
                      for t in range(2))
        if inner.setdefault(word, img) != img:
            consistent = False
    if consistent:
        as_function += 1
        if len(set(inner.values())) == len(inner):
            also_injective += 1
check("EVERY random mask admits a consistent digraphic inner map (100%)",
      as_function == TRIALS)
print(f"   consistent as a function : {as_function}/{TRIALS}")

# the only residual filter is that a real cipher's block map must be injective;
# that is a birthday effect, not a cryptanalytic constraint.
n = len(full_blocks(2, 0))
birthday = 1.0
for i in range(n):
    birthday *= (1 - i / 676)
rate = also_injective / TRIALS
print(f"   additionally injective   : {also_injective}/{TRIALS} = {rate:.4f}")
print(f"   birthday null for {n} blocks drawn from 676 : {birthday:.4f}")
check("the injectivity filter matches its birthday null (within 0.03)",
      abs(rate - birthday) < 0.03)
print("   -> the architecture imposes NO cryptanalytic constraint. The only rejection")
print("      is an accidental image collision, which discards true and false models")
print("      at the same rate. The family is VACUOUS, not merely untested.")

print("\n## AA-C  the one surviving polygraphic constraint (trigraphic, p | 9)")
for align, (word, (i, j)) in ((0, ("EAS", (21, 30))), (1, ("AST", (22, 31)))):
    for p in (1, 3, 9):
        forced = all(CT[i + t] == CT[j + t] for t in range(3))
        check(f"align {align}, period {p}: ciphertext repeat {CT[i:i+3]}/{CT[j:j+3]} "
              f"is absent, so the model is refuted", not forced)
print("   For every period not dividing 9 the two trigrams fall in different residue")
print("   classes, the mask absorbs the difference, and no constraint survives.")

print(f"\n{'ALL CHECKS PASSED' if not fails else 'FAILURES: ' + str(fails)}")
sys.exit(1 if fails else 0)
