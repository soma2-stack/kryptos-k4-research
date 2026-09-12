"""Independent verifier for EXP-039.

Imports neither the EXP-039 implementation nor k4lib. Keyword ranking, the repeated-letter
tie rule, ragged no-padding column lengths, the one-pass columnar permutation, composition,
all nine ordered pairs, deduplication and both feasibility criteria are reimplemented here.

The columnar permutation is built by EXPLICIT GRID SIMULATION - writing indices into a ragged
grid and reading columns out - rather than by the index arithmetic the experiment uses, so an
error in that arithmetic cannot hide behind itself. With nine pairs, verification is exhaustive.
"""
import json, hashlib, os, sys, itertools, collections, random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
N = 97
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEYWORDS = ("KRYPTOS", "PALIMPSEST", "ABSCISSA")

k4 = json.load(open(os.path.join(ROOT, "data", "k4.json")))
CT = k4["ciphertext"]
CRIB = {}
for c in k4["confirmed_cribs"]:
    for off, ch in enumerate(c["plaintext"]):
        CRIB[c["start"] + off] = ch
JP = sorted(CRIB)
S = json.load(open(os.path.join(ROOT, "results", "exp039", "summary.json")))

checks, fails = [], []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    if not ok:
        fails.append(name)


check("ciphertext sha256 matches", hashlib.sha256(CT.encode()).hexdigest() == S["ciphertext_sha256"])
check("97 characters, 24 crib positions", len(CT) == 97 and len(CRIB) == 24)
check("crib segments match the ciphertext",
      CT[21:34] == "FLRVQQPRNGKSS" and CT[63:74] == "NYPVTTMZFPK")

# ---------------------------------------------------------------- ranking, rebuilt by hand
def rank_columns(kw):
    """Selection sort on (letter, index) - deliberately not the library's sorted()."""
    remaining = list(range(len(kw)))
    order = []
    while remaining:
        best = remaining[0]
        for c in remaining[1:]:
            if (kw[c], c) < (kw[best], best):
                best = c
        order.append(best)
        remaining.remove(best)
    return order


EXPECT = {"KRYPTOS": [0, 5, 3, 1, 6, 4, 2],
          "PALIMPSEST": [1, 7, 3, 2, 4, 0, 5, 6, 8, 9],
          "ABSCISSA": [0, 7, 1, 3, 4, 2, 5, 6]}
for kw in KEYWORDS:
    ro = rank_columns(kw)
    check(f"{kw}: read order reproduced independently {ro}", ro == EXPECT[kw], str(ro))
    check(f"{kw}: read order is a permutation of its {len(kw)} columns",
          sorted(ro) == list(range(len(kw))))
    check(f"{kw}: matches the read order the experiment recorded", ro == S["read_orders"][kw])
check("widths are 7 / 10 / 8", [len(k) for k in KEYWORDS] == [7, 10, 8])
check("repeated letters present and tie-broken left to right",
      rank_columns("PALIMPSEST").index(0) < rank_columns("PALIMPSEST").index(5)
      and rank_columns("ABSCISSA").index(0) < rank_columns("ABSCISSA").index(7)
      and rank_columns("ABSCISSA").index(2) < rank_columns("ABSCISSA").index(5)
      < rank_columns("ABSCISSA").index(6))


def single_pass(kw):
    """EXPLICIT grid simulation: fill row-wise into a ragged grid, read columns in key order."""
    w = len(kw)
    h = (N + w - 1) // w
    grid = [[None] * w for _ in range(h)]
    for j in range(N):
        grid[j // w][j % w] = j
    out = []
    for c in rank_columns(kw):
        for r in range(h):
            if grid[r][c] is not None:
                out.append(grid[r][c])
    assert len(out) == N and sorted(out) == list(range(N))
    perm = [None] * N
    for pos, j in enumerate(out):
        perm[j] = pos                      # input j -> output position
    return perm


SINGLE = {kw: single_pass(kw) for kw in KEYWORDS}
check("no padding: every column length is ceil((97-c)/w)",
      all(len([j for j in range(N) if j % len(kw) == c]) == (N - c + len(kw) - 1) // len(kw)
          for kw in KEYWORDS for c in range(len(kw))))
check("total symbols preserved at 97 by each single pass",
      all(sorted(p) == list(range(N)) for p in SINGLE.values()))

COMP = {(a, b): tuple(SINGLE[b][SINGLE[a][j]] for j in range(N))
        for a, b in itertools.product(KEYWORDS, repeat=2)}
check("nine ordered pairs built", len(COMP) == 9 == S["ordered_pairs"])
check("all nine composed permutations are distinct",
      len(set(COMP.values())) == 9 == S["distinct_permutations"])
check("no composition is the identity", tuple(range(N)) not in set(COMP.values()))
check("no composition equals one of its own single passes",
      not any(p == tuple(t) for p in COMP.values() for t in SINGLE.values()))
check("all three keyword pairs genuinely fail to commute",
      all(COMP[(a, b)] != COMP[(b, a)] for a, b in itertools.combinations(KEYWORDS, 2)))


def decide(perm, ct=CT, crib=None):
    crib = crib if crib is not None else CRIB
    smap = {}
    for j in sorted(crib):
        c = ct[perm[j]]
        if crib[j] in smap and smap[crib[j]] != c:
            return False, False, None
        smap[crib[j]] = c
    return True, len(set(smap.values())) == len(smap), smap


nfun = nbij = 0
byname = {(r["first"], r["second"]): r for r in S["results"]}
for pair, perm in COMP.items():
    fn, bij, _ = decide(perm)
    nfun += int(fn)
    nbij += int(bij)
    r = byname[pair]
    check(f"verdict reproduced for {pair[0]} -> {pair[1]}",
          fn == r["feasible_function"] and bij == r["feasible_bijection"])
check("independent FEASIBLE-FUNCTION count agrees", nfun == S["feasible_function"] == 0, str(nfun))
check("independent FEASIBLE-BIJECTION count agrees", nbij == S["feasible_bijection"] == 0, str(nbij))

# the verifier must not be a rubber stamp
rng = random.Random(3939)
ok = tot = 0
nonbij_ok = False
for pair, perm in COMP.items():
    sub = dict(zip(ALPHA, rng.sample(ALPHA, 26)))
    PT = ["X"] * N
    for i, ch in CRIB.items():
        PT[i] = ch
    synth = [None] * N
    for j in range(N):
        synth[perm[j]] = sub[PT[j]]
    fn, bij, smap = decide(perm, ct="".join(synth))
    tot += 1
    ok += int(fn and bij and all(sub[p] == smap[p] for p in smap))
check("verifier recovers replanted substitutions under every pair (not a rubber stamp)",
      ok == tot == 9, f"{ok}/{tot}")
perm = COMP[("KRYPTOS", "ABSCISSA")]
collapse = {ch: ("A" if ch in "EIOU" else ch) for ch in ALPHA}
PT = ["X"] * N
for i, ch in CRIB.items():
    PT[i] = ch
synth = [None] * N
for j in range(N):
    synth[perm[j]] = collapse[PT[j]]
fn, bij, _ = decide(perm, ct="".join(synth))
check("non-bijective plant is FEASIBLE-FUNCTION but NOT FEASIBLE-BIJECTION", fn and not bij)

# adversarial mutation inside a repeated-plaintext-letter group must flip a plant
dup = [p for p, n in collections.Counter(CRIB.values()).items() if n > 1]
flipped = 0
for pair, perm in COMP.items():
    sub = dict(zip(ALPHA, rng.sample(ALPHA, 26)))
    synth = [None] * N
    for j in range(N):
        synth[perm[j]] = sub[PT[j]]
    v = [j for j in JP if CRIB[j] == dup[0]][-1]
    synth[perm[v]] = ALPHA[(ALPHA.index(synth[perm[v]]) + 7) % 26]
    fn, _, _ = decide(perm, ct="".join(synth))
    flipped += int(not fn)
check("adversarial mutation in a repeated-letter group flips every plant", flipped == 9, str(flipped))

print("# verify_exp039 — independent verification of EXP-039\n")
for name, o, detail in checks:
    print(f"   [{'PASS' if o else 'FAIL'}] {name}")
    if detail and not o:
        print(f"          {detail}")
print(f"\n   {len(checks) - len(fails)}/{len(checks)} checks pass")
print(f"   composed permutations re-decided exhaustively : 9")
print(f"   feasible cases found independently            : {nfun} function, {nbij} bijection")
sys.exit(1 if fails else 0)
