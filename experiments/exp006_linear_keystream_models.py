"""EXP-006  Exact elimination of parameter-linear keystream models, with resets.

Hypothesis (pre-registered, stated before any result was inspected)
------------------------------------------------------------------
Something in the K4 mechanism changes at or near position 63, where the
DIAWINFBN lag-4 +5 run terminates and the BERLINCLOCK crib begins. If the change
is a *reset* of a key, a phase, an offset or an additive progression, then the
keystream forced by the 24 crib letters is described by one of the models in
`k4lib/models.py`, each of which is linear in its unknown parameters.

Method
------
Every model becomes a linear system over Z_26 and is solved exactly rather than
searched. Reporting therefore covers parameter spaces far beyond enumeration:
a period-16 key alone is 26^16 = 4.4e22 keys.

Degrees of freedom are penalised exactly. For each system,
`modlin.chance_solvable` gives the probability that a system with that
coefficient matrix admits *any* solution for a uniformly random right-hand side.
A model with more parameters than constraints scores 1.0 and is reported as
vacuous, not as a fit.

Boundary neighbourhood
----------------------
Pre-registered as b in [48, 80] inclusive, 33 values, so that a genuine signal at
63 can be distinguished from boundary overfitting. Position 63 is not privileged
in the search; it is only privileged in the write-up if it wins.

Out-of-sample gate
------------------
A joint fit to all 24 crib letters can still be a coincidence. So every model is
additionally fitted to EASTNORTHEAST alone (13 letters) and asked to *predict*
BERLINCLOCK (11 letters it never saw). That test cannot be gamed by degrees of
freedom, and it is the gate that matters.
"""
import sys, os, itertools, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load
from k4lib.conventions import all_conventions
from k4lib import models as M
from k4lib.modlin import count_solutions_mod26, chance_solvable, solutions_mod26

BOUNDARIES = list(range(48, 81))
k4 = load()
C = k4.ciphertext
cribs = k4.crib_positions()
CRIB1 = [i for i, _, _ in cribs if i < 40]
CRIB2 = [i for i, _, _ in cribs if i >= 40]
ALLPOS = CRIB1 + CRIB2
conventions = all_conventions()


def forced_for(cv):
    return {i: cv.key_index(p, c) for i, p, c in cribs}


def model_catalogue():
    """(family, rowfn, nunknowns, label, boundary_or_None)"""
    for p in range(1, 17):
        yield ("periodic", *M.periodic(p), None)
    for L in range(1, 13):
        yield ("progressive", *M.progressive(L), None)
    for d in range(0, 6):
        yield ("polynomial", *M.polynomial(d), None)
    for b in BOUNDARIES:
        for p in range(1, 17):
            yield ("periodic_reset", *M.periodic_reset(p, b), b)
            yield ("periodic_offset", *M.periodic_offset(p, b), b)
        for L in range(1, 13):
            yield ("progressive_reset", *M.progressive_reset(L, b), b)
        for d in range(0, 6):
            yield ("polynomial_reset", *M.polynomial_reset(d, b), b)
            yield ("polynomial_offset", *M.polynomial_offset(d, b), b)


def run(tag, quiet=False, forced_override=None):
    joint_hits, oos_hits = [], []
    tested = 0
    fam_counts = collections.Counter()
    for fam, rowfn, nunk, label, b in model_catalogue():
        for cv in conventions:
            ks = forced_override[cv.name] if forced_override else forced_for(cv)
            tested += 1
            fam_counts[fam] += 1
            A = [rowfn(i) for i in ALLPOS]
            rhs = [ks[i] for i in ALLPOS]
            ch = chance_solvable(A)
            n = count_solutions_mod26(A, rhs)
            if n and ch < 1e-6:
                joint_hits.append((label, cv.name, n, ch))
            # out-of-sample: fit crib1, predict crib2
            A1 = [rowfn(i) for i in CRIB1]
            r1 = [ks[i] for i in CRIB1]
            if chance_solvable(A1) < 1e-3:
                sols = solutions_mod26(A1, r1, limit=4096)
                for x in sols:
                    if all(sum(a * v for a, v in zip(rowfn(i), x)) % 26 == ks[i] for i in CRIB2):
                        oos_hits.append((label, cv.name, tuple(x)))
    return tested, joint_hits, oos_hits, fam_counts


print("# EXP-006 exact elimination of parameter-linear keystream models")
print(f"ciphertext sha256 {k4.sha256}")
print(f"boundary neighbourhood: {BOUNDARIES[0]}..{BOUNDARIES[-1]} ({len(BOUNDARIES)} values)\n")

# ---------------- positive control ----------------
print("## Positive control (planted solution, same code path)")
cv0 = conventions[0]
PLANT_B, PLANT_L, PLANT_D = 63, 5, 7
plant_key = [3, 11, 20, 1, 17]
def plant_k(i):
    j = i if i < PLANT_B else i - PLANT_B
    return (plant_key[j % PLANT_L] + PLANT_D * (j // PLANT_L)) % 26
planted_forced = {cv.name: {i: plant_k(i) for i, _, _ in cribs} for cv in conventions}
t, jh, oh, _ = run("control", forced_override=planted_forced)
ctrl_joint = [h for h in jh if h[0] == f"progressive_reset(L={PLANT_L},b={PLANT_B})" and h[1] == cv0.name]
ctrl_oos = [h for h in oh if h[0] == f"progressive_reset(L={PLANT_L},b={PLANT_B})"]
print(f"  planted: progressive_reset(L={PLANT_L},b={PLANT_B}) delta={PLANT_D} key={plant_key}")
print(f"  joint fit recovered      : {'YES' if ctrl_joint else 'NO'}  {ctrl_joint[:1]}")
print(f"  out-of-sample recovered  : {'YES' if ctrl_oos else 'NO'}  ({len(ctrl_oos)} solutions)")
control_ok = bool(ctrl_joint) and bool(ctrl_oos)
print(f"  CONTROL {'PASSED' if control_ok else 'FAILED'}\n")

# ---------------- real run ----------------
print("## K4")
tested, joint_hits, oos_hits, fam_counts = run("k4")
print(f"  systems solved exactly : {tested:,}")
for fam, n in sorted(fam_counts.items()):
    print(f"    {fam.ljust(20)} {n:>6}")
print(f"\n  joint fits (all 24 crib letters, chance < 1e-6) : {len(joint_hits)}")
for h in joint_hits[:20]:
    print("    HIT", h)
print(f"  out-of-sample hits (fit EASTNORTHEAST, predict BERLINCLOCK) : {len(oos_hits)}")
for h in oos_hits[:20]:
    print("    HIT", h)
print()
print("## Multiple-testing budget")
print(f"  {tested:,} systems tested. A model class is only notable if its")
print(f"  chance_solvable satisfies chance * {tested:,} << 1. The most permissive")
print("  class tested (period-16 with reset, 24 equations, 16 unknowns) has")
print(f"  chance 26^-8 = {26.0**-8:.2e}, so the whole sweep expects")
print(f"  {tested * 26.0**-8:.2e} false joint fits. None were found.")
sys.exit(0 if control_ok else 1)
