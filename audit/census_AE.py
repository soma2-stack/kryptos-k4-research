"""Checkpoint AE — reproducible diagnostics behind the K4 decidability census.

Not an experiment: no cipher is run, no keyspace is searched, no plaintext beyond the
two public cribs is used or inferred. Every number quoted in
docs/analysis/k4-decidability-census.md is regenerated here, and the assertions at the
end fail loudly if any of them drifts.

Standard library only; imports no project code.
"""
import collections
import itertools
import json
import os
import random
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K4 = json.load(open(os.path.join(ROOT, "data", "k4.json")))
CT = K4["ciphertext"]
PLAIN = {}
for _cr in K4["confirmed_cribs"]:
    assert CT[_cr["start"]:_cr["start"] + len(_cr["plaintext"])] == _cr["ciphertext_segment"]
    for _j, _ch in enumerate(_cr["plaintext"]):
        PLAIN[_cr["start"] + _j] = _ch
POS = sorted(PLAIN)
BLIND = (27, 28, 29)
checks = []


def constraints_at(period, positions):
    """Independent equality constraints a shared periodic schedule receives."""
    return len(positions) - len({i % period for i in positions})


def blocks(size, align, known=PLAIN):
    out = []
    start = align
    while start + size <= 97:
        if all(start + t in known for t in range(size)):
            out.append((start, "".join(known[start + t] for t in range(size))))
        start += size
    return out


print("## 1. Crib geometry")
print(f"   two contiguous runs: 21-33 (13 letters) and 63-73 (11 letters)")
print(f"   unknown: head 0-20, gap 34-62, tail 74-96  ({97 - len(POS)} positions)")
within = max(j - i for i in POS for j in POS if j > i and (j < 34) == (i < 34))
cross = sorted({j - i for i in POS for j in POS if i < 34 <= j})
print(f"   max within-run distance {within}; cross-crib distances span {min(cross)}-{max(cross)}")
pl = collections.Counter(PLAIN.values())
cl = collections.Counter(CT[i] for i in POS)
print(f"   distinct plaintext letters {len(pl)}, repeats {dict(sorted((k, v) for k, v in pl.items() if v > 1))}")
print(f"   distinct ciphertext letters {len(cl)}, repeats {dict(sorted((k, v) for k, v in cl.items() if v > 1))}")
checks.append(("13 distinct crib plaintext letters", len(pl) == 13))
checks.append(("14 distinct crib ciphertext letters", len(cl) == 14))
checks.append(("no within-run distance exceeds 12", within == 12))
checks.append(("cross-crib distances lie in [30,52]", (min(cross), max(cross)) == (30, 52)))

print("\n## 2. Classes B and G — shared periodic schedule")
row = []
for n in range(2, 41):
    row.append((n, constraints_at(n, POS)))
print("   " + "  ".join(f"p{n}:{c}" for n, c in row[:20]))
print("   " + "  ".join(f"p{n}:{c}" for n, c in row[20:]))
zero = [n for n, c in row if c == 0]
weak = [n for n, c in row if 0 < c <= 5]
print(f"   ZERO constraints at periods {zero}; five or fewer at {weak}")
checks.append(("periods 27,28,29 receive zero constraints", zero == [27, 28, 29]))
checks.append(("period 26 receives exactly one", constraints_at(26, POS) == 1))

print("\n## 3. Classes I and J — repeated plaintext blocks (the only polygraphic lever)")
for size in range(2, 6):
    per = []
    for align in range(size):
        bl = blocks(size, align)
        rep = {w: n for w, n in collections.Counter(w for _, w in bl).items() if n > 1}
        per.append((align, len(bl), rep))
    print(f"   size {size}: " + "; ".join(f"align{a}: {n} blocks, repeats {r or 'none'}"
                                          for a, n, r in per))
tri0 = {w: [s for s, x in blocks(3, 0) if x == w]
        for w, n in collections.Counter(w for _, w in blocks(3, 0)).items() if n > 1}
tri1 = {w: [s for s, x in blocks(3, 1) if x == w]
        for w, n in collections.Counter(w for _, w in blocks(3, 1)).items() if n > 1}
checks.append(("digraph blocks are all distinct at both alignments",
               all(len({w for _, w in blocks(2, a)}) == len(blocks(2, a)) for a in (0, 1))))
checks.append(("size 4 and 5 blocks are all distinct at every alignment",
               all(len({w for _, w in blocks(s, a)}) == len(blocks(s, a))
                   for s in (4, 5) for a in range(s))))
checks.append(("the only trigram repeats are EAS at 21/30 and AST at 22/31",
               tri0 == {"EAS": [21, 30]} and tri1 == {"AST": [22, 31]}))

print("\n## 4. Class D — source-symbol lookup k[i] = f(S[g(i)])")
d = len({CT[i] for i in POS})
print(f"   with K4's own ciphertext as source and identity g: {d} distinct symbols over the")
print(f"   24 crib positions, so at most {24 - d} equality constraints on f")
print("   a source with 24 distinct symbols at the crib positions gives ZERO: vacuous")
checks.append(("ciphertext-as-source yields 10 equality constraints", 24 - d == 10))

print("\n## 5. Class L — arbitrary fixed 26x26 combiner C = T[P[i]][k[i]]")
for n in (2, 3, 5, 8, 10, 13, 17, 26):
    pairs = [(PLAIN[i], i % n) for i in POS]
    rep = sum(v - 1 for v in collections.Counter(pairs).values() if v > 1)
    print(f"   periodic key p={n:2d}: {rep:2d} repeated (plaintext,key) inputs "
          f"-> {rep:2d} constraints on 676 free cells")
checks.append(("an arbitrary table is unconstrained at periods 8, 10, 13 and 26",
               all(sum(v - 1 for v in collections.Counter(
                   [(PLAIN[i], i % n) for i in POS]).values() if v > 1) == 0
                   for n in (8, 10, 13, 26))))

print("\n## 6. Class H — two masks separated by a permutation, M2 . pi . M1")
print("   crib position j gives  a[j mod p] + b[pi(j) mod q] = C[pi(j)] - P[j].")
print("   Solvability conditions = independent cycles of the bipartite graph")
print("   = E - |vertices touched| + components.")
random.seed(20260913)
hrows = []
for p, q in [(3, 3), (5, 5), (7, 7), (8, 10), (10, 10), (12, 12), (13, 13)]:
    seen = []
    for _ in range(400):
        pi = list(range(97))
        random.shuffle(pi)
        parent = {}

        def find(x):
            parent.setdefault(x, x)
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        verts, edges = set(), 0
        for j in POS:
            u, v = ("a", j % p), ("b", pi[j] % q)
            verts |= {u, v}
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
            edges += 1
        seen.append(edges - len(verts) + len({find(x) for x in verts}))
    lo, mean = min(seen), sum(seen) / len(seen)
    hrows.append((p, q, lo, mean))
    print(f"   p={p:2d} q={q:2d}: free {p + q:3d}, 24-(p+q-1) = {24 - (p + q - 1):3d}, "
          f"measured min {lo:3d}, mean {mean:5.2f}")
checks.append(("24-(p+q-1) is a LOWER bound, never exceeded downward",
               all(lo >= max(0, 24 - (p + q - 1)) for p, q, lo, _ in hrows)))
checks.append(("the K1/K2 pair (8,10) retains at least 7 constraints",
               [r for r in hrows if r[:2] == (8, 10)][0][2] == 7))

print("\n## 7. Request 7 — value of ONE additional verified plaintext position")
gains = []
for cand in range(97):
    if cand in PLAIN:
        continue
    unlocked = [n for n in BLIND
                if constraints_at(n, POS + [cand]) > constraints_at(n, POS)]
    breadth = sum(1 for n in range(2, 41)
                  if constraints_at(n, POS + [cand]) > constraints_at(n, POS))
    gains.append((len(unlocked), breadth, cand))
gains.sort(key=lambda g: (-g[0], -g[1], g[2]))
best = [c for u, b, c in gains if u == 3 and b == max(b2 for u2, b2, _ in gains if u2 == 3)]
print(f"   positions unlocking all three blind periods: {sum(1 for u, _, _ in gains if u == 3)}"
      f" of {len(gains)} unknown positions")
print(f"   positions unlocking none: {sorted(c for u, _, c in gains if u == 0)}")
print(f"   best single positions (all three blind periods + widest breadth): {sorted(best)}")
checks.append(("exactly three unknown positions unlock no blind period",
               sorted(c for u, _, c in gains if u == 0) == [20, 47, 74]))
checks.append(("the best single positions are the head and tail extremes",
               sorted(best) == [1, 3, 91, 93, 95, 96]))

print("\n## assertions")
bad = [name for name, ok in checks if not ok]
for name, ok in checks:
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}")
print(f"\n{'ALL CENSUS FIGURES REPRODUCED' if not bad else 'FAILURES: ' + str(bad)}")
sys.exit(1 if bad else 0)
