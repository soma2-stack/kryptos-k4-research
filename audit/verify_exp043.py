"""Independent verification of EXP-043.

Imports neither the experiment nor k4lib. Deliberately different methods:

  * Route A -- CYCLE CERTIFICATES. The experiment decided consistency with weighted
    union-find. This verifier instead extracts an explicit cycle in the bipartite
    graph and evaluates the alternating sum of derived keys around it. A non-zero
    sum is a self-contained proof of infeasibility, checkable by plain arithmetic.

  * Route B -- FORWARD SIMULATION. For a sample it enumerates the mask values
    directly, ENCRYPTS, and demands K4 return at the crib positions -- no graph
    theory at all.

  * Route C -- re-derivation of the K1/K3 facts the corpus rests on, and of the
    permutation corpus, counts and budget.
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
ROWS = json.load(open(os.path.join(ROOT, "data", "cipher_side_rows.json")))["rows"]
MS = {s["id"]: s["text"] for s in
      json.load(open(os.path.join(ROOT, "data", "mask_sources.json")))["sources"]}
CRIB = {}
for _cr in K4["confirmed_cribs"]:
    for _j, _ch in enumerate(_cr["plaintext"]):
        CRIB[_cr["start"] + _j] = _ch
POS = sorted(CRIB)
COMB = ("vigenere", "beaufort", "variant_beaufort")
PAIRS = [(p, q) for p in range(2, 18) for q in range(2, 18) if p + q <= 19]
fails = []


def check(label, cond):
    print(f"   [{'PASS' if cond else 'FAIL'}] {label}")
    if not cond:
        fails.append(label)


def dkey(p_idx, c_idx, comb):
    if comb == "vigenere":
        return (c_idx - p_idx) % 26
    if comb == "beaufort":
        return (c_idx + p_idx) % 26
    return (p_idx - c_idx) % 26


print("## Route C  the K1/K3 facts the corpus rests on, re-derived here")
stream = "".join(ROWS[str(i)] for i in range(1, 29))
check("cipher-side stream is 869 characters", len(stream) == 869)
K1c = stream[:63]
rest = stream[63 + 372:]
K3c = rest[:rest.index("?") + 1]
K4c = rest[rest.index("?") + 1:]
check("the K4 segment equals data/k4.json", K4c == CT)


def vig(ct, key, pa, ca):
    pi = {c: i for i, c in enumerate(pa)}
    ci = {c: i for i, c in enumerate(ca)}
    out, k = [], 0
    for ch in ct:
        if ch not in ci:
            continue
        out.append(pa[(ci[ch] - pi[key[k % len(key)]]) % 26])
        k += 1
    return "".join(out)


check("K1 decrypts exactly as Vigenere KRY/KRY with PALIMPSEST",
      vig(K1c, "PALIMPSEST", KRY, KRY) == MS["K1_plaintext"])
ct3 = "".join(c for c in K3c if c.isalpha())
import collections
check("K3 is a PURE transposition (identical letter multisets)",
      collections.Counter(ct3) == collections.Counter(MS["K3_plaintext"]))
check("97 is prime, so no nontrivial rectangle exists at K4 length",
      [d for d in range(2, 97) if 97 % d == 0] == [])
check("336 admits 18 nontrivial rectangles, so K3's principle needs compositeness",
      len([d for d in range(2, 336) if 336 % d == 0]) == 18)
units = list(range(1, 97))
check("the affine corpus is 96 multipliers x 97 offsets = 9,312", len(units) * 97 == 9312)
check("the affine family is closed under inversion",
      all([(pow(a, -1, 97) * (j - b)) % 97 for j in range(97)] ==
          sorted(range(97), key=lambda i: (a * i + b) % 97)
          for a in (2, 5, 96) for b in (0, 7)))
N = 9312 * len(PAIRS) * 12
check("declared period range gives 136 ordered pairs", len(PAIRS) == 136)
print(f"   N = {N:,}, log26(N) = {math.log(N, 26):.2f}")
check("budget log26(N) + worst d_eff stays under 24", math.log(N, 26) + 18 < 24)

S = json.load(open(os.path.join(ROOT, "results", "exp043", "summary.json")))
check("experiment decided the full corpus", S["tested"] == N)
check("experiment reported zero FEASIBLE", len(S["feasible"]) == 0)
check("experiment controls passed", all(S["controls"].values()))

print("\n## Route A  cycle certificates of infeasibility")


def cycle_certificate(pi, p, q, comb, pa, ca):
    """Find a cycle whose alternating key sum is non-zero: a proof of infeasibility."""
    pidx = {ch: i for i, ch in enumerate(AL[pa])}
    cidx = {ch: i for i, ch in enumerate(AL[ca])}
    adj = {}
    edges = []
    for n, j in enumerate(POS):
        t = pi[j]
        u, v = ("A", j % p), ("B", t % q)
        c = dkey(pidx[CRIB[j]], cidx[CT[t]], comb)
        adj.setdefault(u, []).append((v, c, len(edges)))
        adj.setdefault(v, []).append((u, (-c) % 26, len(edges)))
        edges.append((u, v, c))
    pot, seen = {}, set()
    for start in adj:
        if start in pot:
            continue
        pot[start] = 0
        stack = [start]
        while stack:
            x = stack.pop()
            for (y, w, ei) in adj[x]:
                if y not in pot:
                    pot[y] = (pot[x] + w) % 26
                    stack.append(y)
                elif ei not in seen:
                    seen.add(ei)
                    if (pot[x] + w) % 26 != pot[y] % 26:
                        return (x, y, ei, (pot[x] + w - pot[y]) % 26)
    return None


import random
random.seed(20260921)
certified = unproven = 0
for _ in range(4000):
    a = random.choice(units)
    b = random.randrange(97)
    p, q = random.choice(PAIRS)
    comb = random.choice(COMB)
    pa = random.choice(["STD", "KRY"])
    ca = random.choice(["STD", "KRY"])
    pi = [(a * i + b) % 97 for i in range(97)]
    cert = cycle_certificate(pi, p, q, comb, pa, ca)
    if cert is None:
        unproven += 1
    else:
        certified += 1
print(f"   randomly sampled 4,000 configurations")
print(f"   cycle certificates of infeasibility found : {certified:,}")
print(f"   configurations with no certificate        : {unproven:,}")
check("every sampled configuration is certified infeasible", unproven == 0)

print("\n## Route B  forward simulation, no graph theory")
found = 0
tried = 0
for a in (1, 2, 3):
    for b in (0, 1):
        pi = [(a * i + b) % 97 for i in range(97)]
        for (p, q) in [(2, 2), (2, 3), (3, 2)]:
            for comb in COMB:
                pidx = {ch: i for i, ch in enumerate(AL["KRY"])}
                cidx = {ch: i for i, ch in enumerate(AL["KRY"])}
                for m1 in range(26 ** p):
                    M1 = [(m1 // 26 ** t) % 26 for t in range(p)]
                    for m2 in range(26 ** q):
                        M2 = [(m2 // 26 ** t) % 26 for t in range(q)]
                        tried += 1
                        ok = True
                        for j in POS:
                            t = pi[j]
                            k = (M1[j % p] + M2[t % q]) % 26
                            pv = pidx[CRIB[j]]
                            cv = ((pv + k) % 26 if comb == "vigenere" else
                                  (k - pv) % 26 if comb == "beaufort" else (pv - k) % 26)
                            if AL["KRY"][cv] != CT[t]:
                                ok = False
                                break
                        if ok:
                            found += 1
print(f"   enumerated {tried:,} explicit mask pairs and encrypted forward")
check("Route B finds no feasible configuration", found == 0)

print(f"\n{'ALL CHECKS PASSED' if not fails else 'FAILURES: ' + str(fails)}")
sys.exit(1 if fails else 0)
