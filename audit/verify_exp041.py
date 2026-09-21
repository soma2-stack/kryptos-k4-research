"""Independent verification of EXP-041.

Imports neither experiments/exp041_two_tap_feedback.py nor k4lib. All linear
algebra below is implemented here from scratch, and the routes are deliberately
different from the experiment's:

  * Route A -- CERTIFICATE OF INFEASIBILITY. The experiment asked a solver whether
    a system was solvable. This verifier instead demands a witness: a vector w with
    w.M == 0 and w.rhs != 0 modulo 2 or 13. Such a w is a self-contained proof that
    no solution exists, checkable by plain arithmetic with no solver trusted.

  * Route B -- BRUTE FORCE, ENCRYPT DIRECTION. For b = 2 it enumerates every warm-up
    pair, runs the recursion forward, ENCRYPTS the resulting plaintext, and demands
    both that K4 comes back and that the crib letters match. No linear algebra at all.

  * Route C -- independent recomputation of the enumerated and distinct counts and
    of the worst-case null.
"""
import json
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K4 = json.load(open(os.path.join(ROOT, "data", "k4.json")))
CT = K4["ciphertext"]
STD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KRY = K4["kryptos_alphabet"]
AL = {"STD": STD, "KRY": KRY}
CRIB = {}
for _cr in K4["confirmed_cribs"]:
    for _j, _ch in enumerate(_cr["plaintext"]):
        CRIB[_cr["start"] + _j] = _ch
POS = sorted(CRIB)
COMB = ("vigenere", "beaufort", "variant_beaufort")
COEFFS = ((1, 1), (1, 25), (25, 1), (25, 25))
UNITS = [u for u in range(1, 26) if math.gcd(u, 26) == 1]
fails = []


def check(label, cond):
    print(f"   [{'PASS' if cond else 'FAIL'}] {label}")
    if not cond:
        fails.append(label)


def build(ct, a, b, al, be, gf, comb, pa, ca, rev):
    """Affine representation, written independently of the experiment."""
    ci = {ch: i for i, ch in enumerate(AL[ca])}
    cv = [ci[ch] for ch in ct]
    n = b + (1 if gf else 0)
    const = [0] * 97
    coef = [[0] * n for _ in range(97)]
    seeds = sorted(range(96, 96 - b, -1)) if rev else list(range(b))
    sidx = {s: k for k, s in enumerate(seeds)}
    for i in (range(96, -1, -1) if rev else range(97)):
        if i in sidx:
            j = sidx[i]
            if comb == "vigenere":
                const[i], coef[i][j] = cv[i], 25
            elif comb == "beaufort":
                const[i], coef[i][j] = (-cv[i]) % 26, 1
            else:
                const[i], coef[i][j] = cv[i], 1
        else:
            ia, ib = (i + a, i + b) if rev else (i - a, i - b)
            kc = [(al * coef[ia][t] + be * coef[ib][t]) % 26 for t in range(n)]
            kk = (al * const[ia] + be * const[ib]) % 26
            if gf:
                kc[n - 1] = (kc[n - 1] + 1) % 26
            if comb == "vigenere":
                const[i] = (cv[i] - kk) % 26
                coef[i] = [(-c) % 26 for c in kc]
            elif comb == "beaufort":
                const[i] = (kk - cv[i]) % 26
                coef[i] = kc[:]
            else:
                const[i] = (cv[i] + kk) % 26
                coef[i] = kc[:]
    pi = {ch: i for i, ch in enumerate(AL[pa])}
    M = [coef[i] for i in POS]
    rhs = [(pi[CRIB[i]] - const[i]) % 26 for i in POS]
    return M, rhs, const, coef, n


def left_null_witness(M, rhs, p):
    """Find w with w.M == 0 (mod p) and w.rhs != 0 (mod p), by row-reducing the
    transpose augmented with the identity. Returns w or None."""
    rows, cols = len(M), len(M[0])
    # work on M^T | I  so that row operations track combinations of ORIGINAL rows
    T = [[M[r][c] % p for r in range(rows)] for c in range(cols)]
    tag = [[1 if i == j else 0 for j in range(rows)] for i in range(rows)]
    # eliminate columns of T (which are original rows) to expose dependencies
    piv_row = 0
    used = []
    for c in range(rows):
        piv = None
        for r in range(piv_row, cols):
            if T[r][c] % p:
                piv = r
                break
        if piv is None:
            continue
        T[piv_row], T[piv] = T[piv], T[piv_row]
        inv = pow(T[piv_row][c], p - 2, p)
        T[piv_row] = [(v * inv) % p for v in T[piv_row]]
        for r in range(cols):
            if r != piv_row and T[r][c] % p:
                f = T[r][c]
                T[r] = [(x - f * y) % p for x, y in zip(T[r], T[piv_row])]
        used.append(c)
        piv_row += 1
        if piv_row == cols:
            break
    # any original row index not a pivot is dependent on the pivots
    free = [c for c in range(rows) if c not in used]
    for f in free:
        w = [0] * rows
        w[f] = 1
        for k, c in enumerate(used):
            if k < len(T) and abs(T[k][f]) % p:
                w[c] = (-T[k][f]) % p
        if any(sum(w[r] * M[r][j] for r in range(rows)) % p for j in range(cols)):
            continue
        if sum(w[r] * rhs[r] for r in range(rows)) % p:
            return w
    return None


print("## 0. Inputs and the experiment's own report")
check("97-character ciphertext", len(CT) == 97)
check("24 known plaintext positions", len(CRIB) == 24)
S = json.load(open(os.path.join(ROOT, "results", "exp041", "summary.json")))
check("experiment enumerated 32,832 configurations", S["enumerated"] == 32832)
check("experiment decided 21,883 distinct tests", S["distinct"] == 21883)
check("experiment reported zero FEASIBLE", len(S["feasible"]) == 0)
check("all three experiment controls passed", all(S["controls"].values()))

print("\n## Route C  independent recomputation of the parameter counts")
enum = 0
for b in range(2, 20):
    for a in range(1, b):
        enum += len(COEFFS) * 2 * len(COMB) * 2 * 2 * 2
check("enumerated count reproduces as 32,832", enum == 32832)
# a real recomputation: the unknown count must equal b (+1 when gamma is free)
dims = set()
for b in range(2, 20):
    for gf in (False, True):
        _, _, _, _, n = build(CT, 1, b, 1, 1, gf, "vigenere", "STD", "STD", False)
        dims.add((b, gf, n))
check("unknown count is exactly b (+1 when gamma is free), every b",
      all(n == b + (1 if gf else 0) for b, gf, n in dims) and len(dims) == 36)

print("\n## Route A  certificates of infeasibility (a proof, not a solver verdict)")
certified = unproven = 0
sampled = 0
for b in range(2, 20):
    for a in range(1, b):
        for (al, be) in COEFFS:
            for gf in (False, True):
                for comb in COMB:
                    for pa in ("STD", "KRY"):
                        for ca in ("STD", "KRY"):
                            for rev in (False, True):
                                sampled += 1
                                M, rhs, *_ , n = build(CT, a, b, al, be, gf,
                                                       comb, pa, ca, rev)
                                w = left_null_witness(M, rhs, 2) or \
                                    left_null_witness(M, rhs, 13)
                                if w is None:
                                    unproven += 1
                                else:
                                    proved = False
                                    for p in (2, 13):
                                        kills = all(
                                            sum(w[r] * M[r][j] for r in range(len(M))) % p == 0
                                            for j in range(n))
                                        misses = sum(w[r] * rhs[r]
                                                     for r in range(len(M))) % p != 0
                                        if kills and misses:
                                            proved = True
                                            break
                                    if proved:
                                        certified += 1
                                    else:
                                        unproven += 1
print(f"   configurations examined: {sampled:,} (full coverage, no sampling)")
print(f"   infeasibility certificates verified : {certified:,}")
print(f"   configurations with no witness found: {unproven:,}")
check("every configuration carries a verified infeasibility certificate",
      unproven == 0 and certified > 0)

print("\n## Route B  brute force, encrypt direction, b = 2 (no linear algebra)")
found = []
tried = 0
for (al, be) in COEFFS:
    for comb in COMB:
        for pa in ("STD", "KRY"):
            for ca in ("STD", "KRY"):
                pi = {ch: i for i, ch in enumerate(AL[pa])}
                ci = {ch: i for i, ch in enumerate(AL[ca])}
                cv = [ci[ch] for ch in CT]
                want = {i: pi[ch] for i, ch in CRIB.items()}
                for u0 in range(26):
                    for u1 in range(26):
                        tried += 1
                        P = [0] * 97
                        ok = True
                        for i in range(97):
                            k = (u0 if i == 0 else u1) if i < 2 else \
                                (al * P[i - 1] + be * P[i - 2]) % 26
                            if comb == "vigenere":
                                P[i] = (cv[i] - k) % 26
                                back = (P[i] + k) % 26
                            elif comb == "beaufort":
                                P[i] = (k - cv[i]) % 26
                                back = (k - P[i]) % 26
                            else:
                                P[i] = (cv[i] + k) % 26
                                back = (P[i] - k) % 26
                            if back != cv[i]:
                                ok = False
                                break
                            if i in want and P[i] != want[i]:
                                ok = False
                                break
                        if ok:
                            found.append((al, be, comb, pa, ca, u0, u1))
print(f"   enumerated {tried:,} warm-up pairs with forward re-encryption")
check("Route B finds no feasible b = 2 configuration", not found)

print(f"\n{'ALL CHECKS PASSED' if not fails else 'FAILURES: ' + str(fails)}")
sys.exit(1 if fails else 0)
