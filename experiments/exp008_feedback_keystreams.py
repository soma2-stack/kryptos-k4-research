"""EXP-008  Data-dependent keystreams: autokey, feedback, and self-referential keys.

Hypothesis (pre-registered)
---------------------------
EXP-006 eliminated every keystream that is a function of *position alone*, and
EXP-003 eliminated transposition plus a periodic key. The natural surviving
class is a keystream that is a function of the *text*: classic autokey, running
feedback from the ciphertext, or a self-referential key drawn from K4 itself at
a reversed or decimated alignment.

These are still parameter-linear. For a source letter stream S and lag L,

    k[i] = a * S[i-L] + b                 (single tap, 2 unknowns)
    k[i] = a * S[i-L] + c * S[i-M] + b    (two taps, 3 unknowns)
    k[i] = a * S[i-L] + d * i + b         (tap plus drift, 3 unknowns)

and each gains one unknown when a reset or offset is allowed at a boundary. The
ciphertext is known at every position, so all 24 crib letters give equations:
2 unknowns against 24 equations is a chance of 26^-22 = 1e-31, which makes this
one of the most discriminating tests available anywhere in this repository.

Sources tested
--------------
  ciphertext forward           S[j] = C[j]
  ciphertext reversed          S[j] = C[96-j]        (self-referential key)
  ciphertext decimated         S[j] = C[(m*j) mod 97] for m in 2,3,5,7,11
  plaintext (classic autokey)  S[j] = P[j], only where the crib supplies it

Boundary neighbourhood is the same pre-registered [48,80] used by EXP-006.
"""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load
from k4lib.conventions import all_conventions
from k4lib.alphabets import ALPHABETS, index_map
from k4lib.modlin import count_solutions_mod26, chance_solvable

BOUNDARIES = list(range(48, 81))
k4 = load()
C = k4.ciphertext
cribs = k4.crib_positions()
POS = [i for i, _, _ in cribs]
P = {i: p for i, p, _ in cribs}
conventions = all_conventions()


def sources(aname):
    idx = index_map(ALPHABETS[aname])
    cv = [idx[ch] for ch in C]
    out = {"cipher_fwd": lambda j: cv[j] if 0 <= j < 97 else None,
           "cipher_rev": lambda j: cv[96 - j] if 0 <= j < 97 else None}
    for m in (2, 3, 5, 7, 11):
        out[f"cipher_dec{m}"] = (lambda j, m=m: cv[(m * j) % 97] if 0 <= j < 97 else None)
    out["plain"] = lambda j: (idx[P[j]] if j in P else None)
    return out


def solve(rows, rhs, label, bag, tested):
    if len(rows) < 6:
        return
    ch = chance_solvable(rows)
    if ch > 1e-6:
        return
    n = count_solutions_mod26(rows, rhs)
    if n:
        bag.append((label, n, ch))


print("# EXP-008 data-dependent (autokey / feedback / self-referential) keystreams")
print(f"ciphertext sha256 {k4.sha256}\n")

# ------------------------------------------------ positive control
print("## Positive control")
idxS = index_map(ALPHABETS["STD"])
Cv = [idxS[ch] for ch in C]
PLANT_L, PLANT_A, PLANT_B = 7, 5, 11
planted = {i: (PLANT_A * Cv[i - PLANT_L] + PLANT_B) % 26 for i in POS}
rows = [[Cv[i - PLANT_L], 1] for i in POS]
rhs = [planted[i] for i in POS]
nc = count_solutions_mod26(rows, rhs)
print(f"  planted k[i] = {PLANT_A}*C[i-{PLANT_L}] + {PLANT_B}")
print(f"  recovered: {'YES' if nc else 'NO'} ({nc} solution(s), chance {chance_solvable(rows):.2e})")
control_ok = nc > 0
print(f"  CONTROL {'PASSED' if control_ok else 'FAILED'}\n")

hits = []
tested = 0
fam = collections.Counter()

for aname in ("STD", "KRY"):
    S = sources(aname)
    for sname, f in S.items():
        maxlag = 12 if sname == "plain" else 40
        for L in range(0, maxlag + 1):
            # single tap (the right-hand side depends on the convention)
            for cv in conventions:
                ks = {i: cv.key_index(p, c) for i, p, c in cribs}
                r2, b2 = [], []
                for i in POS:
                    v = f(i - L)
                    if v is not None:
                        r2.append([v, 1]); b2.append(ks[i])
                tested += 1; fam["single_tap"] += 1
                solve(r2, b2, f"{aname}/{sname}/L={L}/single/{cv.name}", hits, tested)
                # tap plus linear drift in position
                r3 = [row + [i] for row, i in zip(r2, [i for i in POS if f(i - L) is not None])]
                tested += 1; fam["tap_plus_drift"] += 1
                solve(r3, b2, f"{aname}/{sname}/L={L}/drift/{cv.name}", hits, tested)
                # tap plus reset offset at boundary
                for b in BOUNDARIES:
                    idxs = [i for i in POS if f(i - L) is not None]
                    r4 = [row + [1 if i >= b else 0] for row, i in zip(r2, idxs)]
                    tested += 1; fam["tap_plus_reset"] += 1
                    solve(r4, b2, f"{aname}/{sname}/L={L}/reset{b}/{cv.name}", hits, tested)

# two-tap, ciphertext forward only (the largest family, kept separate)
for aname in ("STD", "KRY"):
    f = sources(aname)["cipher_fwd"]
    for L in range(0, 25):
        for M in range(L + 1, 26):
            for cv in conventions:
                ks = {i: cv.key_index(p, c) for i, p, c in cribs}
                r, b = [], []
                for i in POS:
                    v1, v2 = f(i - L), f(i - M)
                    if v1 is not None and v2 is not None:
                        r.append([v1, v2, 1]); b.append(ks[i])
                tested += 1; fam["two_tap"] += 1
                solve(r, b, f"{aname}/cipher_fwd/L={L},M={M}/two_tap/{cv.name}", hits, tested)

print("## Search")
print(f"  systems solved exactly : {tested:,}")
for k, v in sorted(fam.items()):
    print(f"    {k.ljust(18)} {v:>7}")
print(f"\n  fits with chance < 1e-6 : {len(hits)}")
for h in hits[:25]:
    print("    HIT", h)
print()
print("## Multiple-testing budget")
print(f"  The most permissive family tested has 4 unknowns against >= 20 equations,")
print(f"  chance <= 26^-16 = {26.0**-16:.2e}. Over {tested:,} systems the sweep expects")
print(f"  {tested * 26.0**-16:.2e} false fits.")
sys.exit(0 if control_ok else 1)
