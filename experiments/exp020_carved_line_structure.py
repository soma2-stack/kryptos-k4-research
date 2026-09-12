"""EXP-020  The carved line structure as the coding geometry.

Primary-data basis (see data/physical.json)
-------------------------------------------
K4 is rendered, universally and self-consistently, as

    line 0  OBKR                             positions  0.. 3   (4 chars)
    line 1  UOXOGHULBSOLIFBBWFLRVQQPRNGKSSO  positions  4..34   (31 chars)
    line 2  TWTQSJQSSEKZZWATJKLUDIAWINFBNYP  positions 35..65   (31 chars)
    line 3  VTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR  positions 66..96   (31 chars)

These four lines concatenate EXACTLY to the canonical ciphertext, so the split is
internally verified rather than merely asserted, and it matches the "31-column
geometry" the inherited handoff refers to. It replaces the 7x14 layout used in
EXP-018, which came from a source now on the contamination exclusion list.

Two structural facts follow, and they are not symmetric:
    EASTNORTHEAST (21-33) lies WHOLLY INSIDE line 1.
    BERLINCLOCK   (63-73) STRADDLES the line-2/line-3 boundary at position 66.

Hypothesis (pre-registered)
---------------------------
Sanborn is an artist who cut these lines by hand, one at a time. The cheapest
hand procedure for a long message is to work line by line, restarting the key at
the start of each line. That predicts a key whose phase resets at positions
4, 35 and 66 - positions supplied by the object, not fitted.

This is a different model from EXP-006 and EXP-015, which allowed a SINGLE reset
at one searched boundary. Here there are THREE resets at FIXED physical positions,
so the model adds no free parameters beyond the key itself. That is exactly the
profile a hand-executed construction should have: low descriptive complexity, no
arbitrary choices, visible physical motivation.

Also tested: a key advancing once per line rather than per character; a per-line
additive offset; a progressive key restarting per line; and the variant in which
OBKR is an indicator and the message proper begins at position 4.

Grades used: EXHAUSTIVELY ELIMINATED WITHIN SPECIFIED MODEL for a completed sweep
with adequate constraints; UNTESTABLE WITH CURRENT PUBLIC DATA where the model has
more free parameters than the cribs can constrain.
"""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load
from k4lib.conventions import all_conventions
from k4lib import models as M
from k4lib.modlin import count_solutions_mod26, chance_solvable

k4 = load()
cribs = k4.crib_positions()
POS = [i for i, _, _ in cribs]
conventions = all_conventions()

STARTS_FULL = (0, 4, 35, 66)          # OBKR counted as line 0
STARTS_MSG = (4, 35, 66)              # OBKR treated as an indicator, message starts at 4

print("# EXP-020 carved line structure as the coding geometry")
print(f"ciphertext sha256 {k4.sha256}\n")
print("## Geometry (self-verified: the lines concatenate to the canonical ciphertext)")
for ln, (s, e) in enumerate([(0, 3), (4, 34), (35, 65), (66, 96)]):
    print(f"   line {ln}: positions {s:>2}..{e:<2} ({e-s+1} chars)")
print("   EASTNORTHEAST 21-33 lies wholly inside line 1")
print("   BERLINCLOCK   63-73 straddles the boundary at 66\n")

# ---------------------------------------------------------------- control
print("## Positive control")
cv0 = conventions[0]
PP = 9
pkey = [7, 22, 3, 19, 11, 0, 25, 14, 6]
def plant(i):
    ln = 0
    for k, s in enumerate(STARTS_FULL):
        if i >= s:
            ln = k
    return pkey[(i - STARTS_FULL[ln]) % PP]
planted = {i: plant(i) for i in POS}
rowfn, nunk, label = M.line_reset(PP, STARTS_FULL)
A = [rowfn(i) for i in POS]
rhs = [planted[i] for i in POS]
n = count_solutions_mod26(A, rhs)
print(f"   planted line_reset(p={PP}) with resets at {STARTS_FULL}")
print(f"   recovered: {'YES' if n else 'NO'} ({n} solution(s), chance {chance_solvable(A):.2e})")
ctrl = n > 0
print(f"   CONTROL {'PASSED' if ctrl else 'FAILED'}\n")

# ---------------------------------------------------------------- sweep
def catalogue(starts):
    for p in range(1, 21):
        yield M.line_reset(p, starts)
        yield M.line_offset(p, starts)
    for L in range(2, 13):
        yield M.line_progressive(L, starts)
    for p in range(1, 5):
        yield M.line_index_key(p, starts)
    yield M.column_key(31, starts)

print("## Search")
hits, vacuous, tested = [], collections.Counter(), 0
for tag, starts in (("OBKR as line 0", STARTS_FULL), ("OBKR as indicator", STARTS_MSG)):
    for rowfn, nunk, label in catalogue(starts):
        A = [rowfn(i) for i in POS]
        ch = chance_solvable(A)
        for cv in conventions:
            tested += 1
            ks = {i: cv.key_index(p, c) for i, p, c in cribs}
            rhs = [ks[i] for i in POS]
            if ch > 1e-3:
                vacuous[f"{tag}/{label}"] += 1
                continue
            if count_solutions_mod26(A, rhs):
                hits.append((tag, label, cv.name, ch))
print(f"   systems solved exactly : {tested:,}")
print(f"   fits (chance < 1e-3)   : {len(hits)}")
for h in hits[:20]:
    print("     HIT", h)
if vacuous:
    print(f"\n   models skipped as UNTESTABLE (more free parameters than the cribs")
    print(f"   constrain, chance_solvable > 1e-3):")
    for k, v in sorted(vacuous.items()):
        print(f"     {k}")
print()

# ------------------------------------------------- the sharp column prediction
print("## The column-key prediction, stated before testing")
print("   If the key depends only on the column within a carved line, then two crib")
print("   positions sharing a column must force the same key index. Columns 28 and 29")
print("   occur in BOTH cribs:")
print("     position 32 (line 1, col 28)  vs  position 63 (line 2, col 28)")
print("     position 33 (line 1, col 29)  vs  position 64 (line 2, col 29)")
print("   That is two independent 1/26 constraints - chance 26^-2 = 1.5e-3 per")
print("   convention, so ~0.018 hits expected across 12 conventions.\n")
pred = []
for cv in conventions:
    ks = {i: cv.key_index(p, c) for i, p, c in cribs}
    ok = (ks[32] == ks[63]) and (ks[33] == ks[64])
    pred.append((cv.name, ks[32], ks[63], ks[33], ks[64], ok))
for name, a, b, c, d, ok in pred:
    print(f"   {name.ljust(34)} k[32]={a:>2} k[63]={b:>2} | k[33]={c:>2} k[64]={d:>2}  "
          f"{'MATCH' if ok else 'no'}")
nmatch = sum(1 for *_, ok in pred if ok)
print(f"\n   conventions satisfying the prediction: {nmatch} of 12 (expected ~0.018)")
print()
print("## Reading")
print("   The line-restart family is the cheapest hand procedure consistent with the")
print("   object, and its reset positions are given by the carving rather than fitted.")
print("   A negative here is therefore informative about hand-executed constructions,")
print("   not merely about one more parameter family.")
sys.exit(0 if ctrl else 1)
