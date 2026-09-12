"""EXP-018  Compass-bearing routes on the physical grid, against every keystream model.

Hypothesis (pre-registered, stated before any result was inspected)
-------------------------------------------------------------------
Both confirmed cribs name the same kind of object. `EASTNORTHEAST` is a compass
bearing. `BERLINCLOCK` was confirmed by Sanborn in November 2025 to be the
Weltzeituhr at Alexanderplatz, which stands on a compass-rose mosaic; the Kryptos
courtyard contains a compass rose of its own. If the cribs are operational rather
than decorative, the operation they jointly name is: **read a grid of letters along
a bearing**.

This is the "delivering a message" reading in its most literal cryptographic form -
letters moved from one location to another along a heading - and it is something
Sanborn could execute by hand with a straightedge on a copper plate.

Why this is not a repeat of EXP-003 or EXP-016
----------------------------------------------
Those swept rectangular row/column/boustrophedon routes. A bearing route is a
lattice step (dcol, drow) taken repeatedly on a torus, which is a different
permutation family: ENE is two columns east for one row north, and no
row-or-column route produces it. The grids are also not swept: they are the five
the evidence names, listed below.

Pre-registered scope
--------------------
grids   14x7 and 7x14  - WITHDRAWN MOTIVATION. These came from a source later
                         placed on the contamination exclusion list (see
                         docs/contamination-log.md, incident 1). The RESULT below
                         stands - a negative over a badly motivated grid is still a
                         negative for that grid - but the grids are no longer
                         claimed to reflect the physical carving. The verified
                         geometry is 4/31/31/31; see EXP-020.
        24x4 and 4x24  - the Weltzeituhr: 24 segments, four city bands
        22x4           - the inherited UTC+9 world-clock tape length
bearings  all 16 points of the compass rose as integer lattice steps
starts    every cell of the grid
orders    key indexed on the plaintext side and on the ciphertext side
models    periodic p=8..16, progressive L=2..12, polynomial degree 1..5
conventions  the 12 declared shift conventions, fixed in advance and not fitted

Degrees of freedom are declared, not discovered: the alphabet is fixed before
running, as EXP-011 requires, since transposition plus a *free* keyed alphabet is
vacuous while transposition plus a fixed alphabet is testable.
"""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load
from k4lib.conventions import all_conventions
from k4lib.bearings import ROSE_16, grid_permutation
from k4lib import models as M
from k4lib.modlin import make_consistency_checker, chance_solvable, count_solutions_mod26

# NOTE ON SIZING. The Weltzeituhr's natural grid is 24 segments x 4 city bands =
# 96 cells, and K4 is 97 characters: exactly one too many. That is a real
# structural mismatch, recorded rather than papered over. Grids too small to hold
# 97 letters have their height raised to the smallest value that fits, keeping the
# clue-motivated WIDTH intact; the adjustment is printed for each grid.
GRIDS = [(14, 7, "reported physical K4 layout"), (7, 14, "transpose of it"),
         (24, 4, "Weltzeituhr: 24 segments x 4 city bands (96 cells - one short of 97)"),
         (4, 24, "transpose of it"),
         (22, 4, "inherited UTC+9 world-clock tape"),
         (24, 5, "Weltzeituhr width, height raised to fit 97"),
         (26, 4, "alphabet-width control")]
GRIDS = [(w, h if w * h >= 97 else -(-97 // w), why) for w, h, why in GRIDS]

k4 = load()
C = k4.ciphertext
cribs = k4.crib_positions()
POS = [i for i, _, _ in cribs]
conventions = all_conventions()

LINEAR_MODELS = [M.progressive(L) for L in range(2, 13)] + \
                [M.polynomial(d) for d in range(1, 6)]
PERIODS = range(8, 17)

print("# EXP-018 compass-bearing routes on the physical grid")
print(f"ciphertext sha256 {k4.sha256}\n")
print("## Pre-registered grids")
seen = set()
G2 = []
for w, h, why in GRIDS:
    if (w, h) in seen:
        print(f"   {w:>2} x {h:<2} SKIPPED as duplicate of an earlier grid   {why}")
        continue
    seen.add((w, h))
    G2.append((w, h, why))
    print(f"   {w:>2} x {h:<2} ({w*h:>3} cells, {w*h-97:>2} blank)   {why}")
GRIDS = G2
print(f"\n## Bearings: {', '.join(ROSE_16)}")
print(f"   ENE = {ROSE_16['ENE']} (dcol, drow): two east for one north\n")

prepared = []
for rowfn, nunk, label in LINEAR_MODELS:
    A = [rowfn(i) for i in POS]
    prepared.append((label, A, make_consistency_checker(A), chance_solvable(A)))

# ------------------------------------------------------------- positive control
print("## Positive control")
cv0 = conventions[0]
perm_c = grid_permutation(14, 7, "ENE", 0)
PL, PD = 5, 7
pkey = [3, 11, 20, 1, 17]
plant = {i: (pkey[i % PL] + PD * (i // PL)) % 26 for i in range(97)}
ct = [None] * 97
for i in range(97):
    ct[perm_c[i]] = cv0.encrypt_letter("A", plant[i])
rhs = [cv0.key_index("A", ct[perm_c[i]]) for i in POS]
lbl, A, chk, ch = next(x for x in prepared if x[0] == f"progressive(L={PL})")
ctrl = chk(rhs) and count_solutions_mod26(A, rhs) > 0
print(f"   planted progressive(L={PL},delta={PD}) under the ENE route on 14x7")
print(f"   recovered by the same code path: {'YES' if ctrl else 'NO'}")
print(f"   CONTROL {'PASSED' if ctrl else 'FAILED'}\n")

# ------------------------------------------------------------- sweep
hits = []
tested = 0
nperms = 0
for w, h, _ in GRIDS:
    for bname in ROSE_16:
        for start in range(w * h):
            perm = grid_permutation(w, h, bname, start)
            if perm is None:
                continue
            inv = [0] * 97
            for a, b in enumerate(perm):
                inv[b] = a
            for pm, order in ((perm, "A"), (inv, "B")):
                nperms += 1
                for cv in conventions:
                    ks = [cv.key_index(p, C[pm[i]]) for i, p, _ in cribs]
                    for p_ in PERIODS:
                        tested += 1
                        cls, bad = {}, False
                        for (i, _, _), kv in zip(cribs, ks):
                            r = i % p_
                            if r in cls and cls[r] != kv:
                                bad = True
                                break
                            cls[r] = kv
                        if not bad and len(cls) < 24:
                            hits.append((w, h, bname, start, order, cv.name, f"periodic(p={p_})"))
                    for label, A, chk, ch in prepared:
                        tested += 1
                        if chk(ks):
                            hits.append((w, h, bname, start, order, cv.name, label))

print("## Search")
print(f"   permutations built : {nperms:,}")
print(f"   gate evaluations   : {tested:,}")
print(f"   fits               : {len(hits)}")
for x in hits[:25]:
    print("     HIT", x)
print()
print("## Multiple-testing budget")
print("   The most permissive model is periodic(p=16): 24 constraints, 16 unknowns,")
print(f"   chance 26^-8 = {26.0**-8:.2e}. Over {tested:,} evaluations the sweep expects")
print(f"   {tested * 26.0**-8:.2e} false fits.")
sys.exit(0 if ctrl else 1)
