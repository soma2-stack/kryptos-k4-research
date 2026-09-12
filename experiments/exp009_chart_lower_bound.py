"""EXP-009  How many alphabets do the cribs force, and how much do selectors say?

Two questions the inherited handoff raised but never quantified.

1. `research-state.md` records a two-chart homophonic interpretation that "had no
   contradictions at the crib positions". Absence of contradiction is only
   evidence if contradiction was *likely*. This computes the exact minimum number
   of charts the cribs force, by reducing the question to graph colouring.

2. It records three separate selectors - opposite-tableau parity, a K0 Morse
   phase, and Kryptos rail alternation - each reported to separate the ten
   crib conflicts. This computes how many of the 2^24 possible binary selectors
   do that, which is the calibration figure those claims need.

Reduction
---------
Build a graph on the 24 crib positions. Join two positions when they cannot share
a chart:

    same plaintext, different ciphertext  -> different charts (a chart is a
                                             function in the encryption direction)
    same ciphertext, different plaintext  -> different charts (a chart is a
                                             function in the decryption direction)

The minimum number of charts is then exactly the chromatic number, and the number
of consistent binary selectors is 2^(components) when the graph is bipartite and
0 when it is not. Both are exact, not estimated.
"""
import sys, os, itertools, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load

k4 = load()
cribs = k4.crib_positions()
n = len(cribs)

DIRECTIONS = [
    ("bijective charts (substitution alphabets)", ("fwd", "inv")),
    ("charts are functions P->C (encryption direction)", ("fwd",)),
    ("charts are functions C->P (decryption direction)", ("inv",)),
]


def build(kinds):
    E = set()
    for a, b in itertools.combinations(range(n), 2):
        _, pa, ca = cribs[a]
        _, pb, cb = cribs[b]
        if "fwd" in kinds and pa == pb and ca != cb:
            E.add((a, b))
        if "inv" in kinds and ca == cb and pa != pb:
            E.add((a, b))
    return E


def adjacency(E):
    adj = collections.defaultdict(set)
    for a, b in E:
        adj[a].add(b)
        adj[b].add(a)
    return adj


def components(adj):
    seen, c = set(), 0
    for s in range(n):
        if s in seen:
            continue
        c += 1
        st = [s]
        seen.add(s)
        while st:
            u = st.pop()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    st.append(v)
    return c


def chromatic(adj):
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


print("# EXP-009 chart lower bound and selector information content")
print(f"ciphertext sha256 {k4.sha256}\n")

print("## The witness, by hand")
byp = collections.defaultdict(list)
for i, p, c in cribs:
    byp[p].append((i, c))
for p, v in sorted(byp.items()):
    if len({c for _, c in v}) >= 3:
        print(f"   plaintext {p} occurs at positions {[i for i, _ in v]} "
              f"and enciphers to {[c for _, c in v]} - three different letters.")
print("   No cipher with only two encryption alphabets can do that.\n")

results = {}
for name, kinds in DIRECTIONS:
    E = build(kinds)
    adj = adjacency(E)
    comp = components(adj)
    k = chromatic(adj)
    results[name] = (len(E), comp, k)
    print(f"## {name}")
    print(f"   edges {len(E)}   components {comp}   MINIMUM CHARTS = {k}")
    if k == 2:
        sel = 2 ** comp
        print(f"   consistent binary selectors: 2^{comp} = {sel:,} of 2^24 = {2**24:,}")
        print(f"   probability an arbitrary selector separates every conflict: "
              f"1 in {2**24 // sel:,}")
    else:
        print("   bipartite: NO. Two charts are impossible in this direction.")
    print()

print("## Reading")
print("   Encryption direction: at least THREE alphabets are forced. Any model")
print("   that assigns one of two charts per position - including a binary")
print("   parity, Morse or rail selector used that way - is eliminated outright.")
print()
print("   Decryption direction: two charts do suffice, but 16,384 of the 16.7M")
print("   possible selectors work. An arbitrary bit-stream separates all ten")
print("   conflicts with probability 1 in 1,024. The inherited observation that")
print("   parity, a Morse phase and rail alternation each 'had no contradictions'")
print("   is therefore worth about 10 bits, and `research-state.md` records that")
print("   multiple Morse phases were searched. A selector family with ~1,000")
print("   members is expected to contain a winner by chance alone.")
print()
print("   These three leads should be treated as explained, not as anomalies,")
print("   unless a selector is specified in advance and works without phase search.")
