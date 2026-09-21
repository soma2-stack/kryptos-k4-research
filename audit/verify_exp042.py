"""Independent verification of EXP-042.

Imports neither experiments/exp042_mixed_feedback.py nor k4lib. All arithmetic is
written here from scratch.

  * Route A -- CERTIFICATES OF INFEASIBILITY, full coverage. Rather than trusting a
    solver status, each configuration must yield a witness w with w.M == 0 and
    w.rhs != 0 modulo 2 or 13. That is a self-contained proof, checkable by plain
    arithmetic.

  * Route B -- BRUTE FORCE, ENCRYPT DIRECTION, no linear algebra. For a = 1 and 2 it
    enumerates every warm-up, runs the recursion, re-encrypts, and demands both that
    K4 returns and that the cribs match.

  * Route C -- independent re-derivation of the structural claims: the unknown count
    is the PLAINTEXT-tap lag (not the ciphertext lag), and the orientation swap with
    lags exchanged is byte-identical.
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
fails = []


def check(label, cond):
    print(f"   [{'PASS' if cond else 'FAIL'}] {label}")
    if not cond:
        fails.append(label)


def build(ct, a, b, al, be, gf, comb, pa, ca, rev, swap=False):
    """Written independently. swap=True puts the PLAINTEXT tap on lag b."""
    ci = {ch: i for i, ch in enumerate(AL[ca])}
    cv = [ci[ch] for ch in ct]
    plag, clag = (b, a) if swap else (a, b)
    pco, cco = (be, al) if swap else (al, be)
    n = plag + (1 if gf else 0)
    const = [0] * 97
    coef = [[0] * n for _ in range(97)]
    seeds = sorted(range(96, 96 - plag, -1)) if rev else list(range(plag))
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
            ip = i + plag if rev else i - plag
            ic = i + clag if rev else i - clag
            kc = [(pco * coef[ip][t]) % 26 for t in range(n)]
            kk = (pco * const[ip] + (cco * cv[ic] if 0 <= ic < 97 else 0)) % 26
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
    return ([coef[i] for i in POS],
            [(pi[CRIB[i]] - const[i]) % 26 for i in POS], n)


def witness(M, rhs, p):
    """Find w with w.M == 0 and w.rhs != 0 mod p, by reducing M^T and tracking
    which original rows are dependent on the pivots."""
    rows, cols = len(M), len(M[0])
    T = [[M[r][c] % p for r in range(rows)] for c in range(cols)]
    used, pr = [], 0
    for c in range(rows):
        piv = next((r for r in range(pr, cols) if T[r][c] % p), None)
        if piv is None:
            continue
        T[pr], T[piv] = T[piv], T[pr]
        inv = pow(T[pr][c], p - 2, p)
        T[pr] = [(v * inv) % p for v in T[pr]]
        for r in range(cols):
            if r != pr and T[r][c] % p:
                f = T[r][c]
                T[r] = [(x - f * y) % p for x, y in zip(T[r], T[pr])]
        used.append(c)
        pr += 1
        if pr == cols:
            break
    for f in [c for c in range(rows) if c not in used]:
        w = [0] * rows
        w[f] = 1
        for k, c in enumerate(used):
            if k < len(T):
                w[c] = (-T[k][f]) % p
        if all(sum(w[r] * M[r][j] for r in range(rows)) % p == 0 for j in range(cols)) \
           and sum(w[r] * rhs[r] for r in range(rows)) % p:
            return w
    return None


print("## 0. Inputs and the experiment's own report")
check("97-character ciphertext", len(CT) == 97)
check("24 known plaintext positions", len(CRIB) == 24)
S = json.load(open(os.path.join(ROOT, "results", "exp042", "summary.json")))
check("experiment enumerated 110,592 raw configurations", S["raw"] == 110592)
check("experiment reported zero FEASIBLE", len(S["feasible"]) == 0)
check("all three experiment controls passed", all(S["controls"].values()))

print("\n## Route C  structural claims, re-derived independently")
dim_ok = True
for a in range(1, 25):
    for b in (1, 7, 19, 24):
        for gf in (False, True):
            _, _, n = build(CT, a, b, 1, 1, gf, "vigenere", "STD", "STD", False)
            if n != a + (1 if gf else 0):
                dim_ok = False
check("unknown count is the PLAINTEXT-tap lag a, independent of the ciphertext lag b",
      dim_ok)
swap_same = swap_tot = 0
for a in range(1, 9):
    for b in range(1, 9):
        if a == b:
            continue
        for comb in COMB:
            for pa in ("STD", "KRY"):
                swap_tot += 1
                s1 = build(CT, a, b, 1, 1, False, comb, pa, "STD", False, swap=False)
                s2 = build(CT, b, a, 1, 1, False, comb, pa, "STD", False, swap=True)
                if s1 == s2:
                    swap_same += 1
print(f"   orientation swap identical in {swap_same}/{swap_tot} independently built cases")
check("the two orientations are the same family (so one enumeration suffices)",
      swap_same == swap_tot)
b0 = build(CT, 5, 3, 1, 0, False, "vigenere", "STD", "STD", False)
b1 = build(CT, 5, 11, 1, 0, False, "vigenere", "STD", "STD", False)
check("beta = 0 makes the ciphertext lag irrelevant, i.e. it is exactly EXP-040", b0 == b1)

print("\n## Route A  certificates of infeasibility (full coverage)")
certified = unproven = 0
for a in range(1, 25):
    for b in range(1, 25):
        for al in (1, 25):
            for be in (1, 25):
                for gf in (False, True):
                    for comb in COMB:
                        for pa in ("STD", "KRY"):
                            for ca in ("STD", "KRY"):
                                for rev in (False, True):
                                    M, rhs, n = build(CT, a, b, al, be, gf, comb, pa, ca, rev)
                                    w = witness(M, rhs, 2) or witness(M, rhs, 13)
                                    if w is None:
                                        unproven += 1
                                    else:
                                        certified += 1
print(f"   configurations examined              : {certified + unproven:,}")
print(f"   infeasibility certificates verified  : {certified:,}")
print(f"   configurations with no witness found : {unproven:,}")
check("every configuration carries a verified infeasibility certificate", unproven == 0)

print("\n## Route B  brute force, encrypt direction, a = 1 and 2 (no linear algebra)")
found, tried = [], 0
for a in (1, 2):
    for b in range(1, 25):
        for al in (1, 25):
            for be in (1, 25):
                for comb in COMB:
                    for pa in ("STD", "KRY"):
                        pi = {ch: i for i, ch in enumerate(AL[pa])}
                        ci = {ch: i for i, ch in enumerate(AL["STD"])}
                        cv = [ci[ch] for ch in CT]
                        want = {i: pi[ch] for i, ch in CRIB.items()}
                        for warm in ([[w] for w in range(26)] if a == 1 else
                                     [[w1, w2] for w1 in range(26) for w2 in range(26)]):
                            tried += 1
                            P = [0] * 97
                            ok = True
                            for i in range(97):
                                if i < a:
                                    k = warm[i]
                                else:
                                    k = (al * P[i - a] + (be * cv[i - b] if i - b >= 0 else 0)) % 26
                                if comb == "vigenere":
                                    P[i] = (cv[i] - k) % 26
                                    back = (P[i] + k) % 26
                                elif comb == "beaufort":
                                    P[i] = (k - cv[i]) % 26
                                    back = (k - P[i]) % 26
                                else:
                                    P[i] = (cv[i] + k) % 26
                                    back = (P[i] - k) % 26
                                if back != cv[i] or (i in want and P[i] != want[i]):
                                    ok = False
                                    break
                            if ok:
                                found.append((a, b, al, be, comb, pa, tuple(warm)))
print(f"   enumerated {tried:,} warm-ups with forward re-encryption")
check("Route B finds no feasible a = 1 or a = 2 configuration", not found)

print(f"\n{'ALL CHECKS PASSED' if not fails else 'FAILURES: ' + str(fails)}")
sys.exit(1 if fails else 0)
