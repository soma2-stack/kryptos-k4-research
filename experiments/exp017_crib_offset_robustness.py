"""EXP-017  Are the conclusions robust to a crib-alignment error?

Motivation
----------
Every structural result in this repository - the three-alphabet lower bound, the
alphabet-free period elimination, the Playfair and reflector eliminations - is
derived from the crib positions in `data/k4.json`, whose own notes say to "verify
against a primary transcript before relying on them for publication". Sanborn's
released clues are quoted 1-indexed; this repository uses 0-indexed half-open
spans. An off-by-one is the single most plausible error in the whole chain.

So: recompute the main invariants with each crib slid by -3..+3 positions, both
independently and together, and see which conclusions survive.

A conclusion that holds at every offset is robust to the alignment question. One
that holds only at offset 0 is contingent on the transcription being exactly right,
and must be labelled that way.
"""
import sys, os, itertools, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load
from k4lib.analysis import index_of_coincidence

k4 = load()
C = k4.ciphertext
N = len(C)
SPANS = [(c["plaintext"], c["start"]) for c in k4.cribs]
OFFSETS = range(-3, 4)


def cribs_at(d1, d2):
    out = []
    for (pt, s), d in zip(SPANS, (d1, d2)):
        s2 = s + d
        if s2 < 0 or s2 + len(pt) > N:
            return None
        out.extend((s2 + k, ch, C[s2 + k]) for k, ch in enumerate(pt))
    return out


def invariants(cribs):
    n = len(cribs)
    E = set()
    for a, b in itertools.combinations(range(n), 2):
        _, pa, ca = cribs[a]
        _, pb, cb = cribs[b]
        if (pa == pb and ca != cb) or (ca == cb and pa != pb):
            E.add((a, b))
    adj = collections.defaultdict(set)
    for a, b in E:
        adj[a].add(b)
        adj[b].add(a)

    def chromatic():
        for k in range(1, 7):
            col = [-1] * n

            def bt(v):
                if v == n:
                    return True
                for c in range(k):
                    if all(col[u] != c for u in adj[v]):
                        col[v] = c
                        if bt(v + 1):
                            return True
                        col[v] = -1
                return False
            if bt(0):
                return k
        return None

    pos = [i for i, _, _ in cribs]
    elim = [p for p in range(1, 25)
            if any((pos[a] - pos[b]) % p == 0 for a, b in E)]
    fixed = sum(1 for _, p, c in cribs if p == c)
    # Playfair: a doubled ciphertext digraph from a distinct plaintext digraph
    P = {i: p for i, p, _ in cribs}
    pf = []
    for align in (0, 1):
        pf.append(any(C[s] == C[s + 1]
                      for s in range(align, N - 1, 2)
                      if s in P and s + 1 in P))
    return chromatic(), elim, fixed, all(pf)


base = invariants(cribs_at(0, 0))
print("# EXP-017 robustness of the structural results to crib misalignment")
print(f"ciphertext sha256 {k4.sha256}\n")
print("## Baseline (offsets 0,0)")
print(f"   minimum alphabets forced : {base[0]}")
print(f"   periods eliminated <=24  : {base[1]}")
print(f"   fixed points C[i]==P[i]  : {base[2]}")
print(f"   Playfair killed on BOTH digraph alignments : {base[3]}\n")

print("## Sweep: each crib slid independently by -3..+3")
print("   d1  d2   min alphabets   #periods elim   fixed pts   Playfair dead")
rows = []
for d1 in OFFSETS:
    for d2 in OFFSETS:
        cr = cribs_at(d1, d2)
        if cr is None:
            continue
        k, elim, fixed, pf = invariants(cr)
        rows.append((d1, d2, k, len(elim), fixed, pf))
        mark = "  <= baseline" if (d1, d2) == (0, 0) else ""
        print(f"   {d1:+d}  {d2:+d}      {k}              {len(elim):>2}"
              f"             {fixed}           {pf}{mark}")

print("\n## What survives")
ks = [r[2] for r in rows]
print(f"   minimum alphabets forced: min {min(ks)}, max {max(ks)} across "
      f"{len(rows)} alignments")
print(f"   >= 3 alphabets at every offset tested: {all(k >= 3 for k in ks)}")
pf_all = all(r[5] for r in rows)
print(f"   Playfair dead at every offset tested  : {pf_all}")
always = [p for p in range(1, 25)
          if all(p in invariants(cribs_at(d1, d2))[1]
                 for d1, d2 in itertools.product(OFFSETS, OFFSETS)
                 if cribs_at(d1, d2) is not None)]
print(f"   periods eliminated at EVERY offset    : {always}")
print()
print("## Reading")
print("   The index of coincidence argument (EXP-007, pure transposition) and the")
print("   output-alphabet argument (EXP-012, all 26 letters present) use no crib")
print("   positions at all, so they are unaffected by alignment entirely.")
print()
print("   Results that hold at every offset are robust to an off-by-one. Results")
print("   that hold only at offset 0 depend on the transcription being exactly")
print("   right and are flagged in docs/research-state.md accordingly.")
