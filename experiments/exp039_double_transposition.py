"""EXP-039  Fixed monoalphabetic substitution composed with DOUBLE columnar transposition,
keys drawn only from the precommitted Kryptos keyword list.

Preregistered in docs/exp039-preregistration.md before any crib verdict was computed.

Model:  C[pi(j)] = S(P[j])   with   pi = T2 o T1,   pi(j) = t2(t1(j))

A fixed monoalphabetic substitution commutes with a pure position permutation, so
S o T2 o T1 and T2 o T1 o S are the SAME model; the case count is not doubled for
substitution order. S is never enumerated - all 26^26 functions are decided exactly by
consistency, as in EXP-033. If no arbitrary function exists, no bijection exists either.

The cribs stay at their published PLAINTEXT positions. The permutation is applied first and
the constraint is formed at ciphertext position pi(j), never at j.

Grade: STRUCTURALLY MOTIVATED, not documentary. K3 shows Sanborn used transposition and the
three keywords are genuinely documented Kryptos words, but nothing says K4 uses double
columnar transposition.
"""
import sys, os, json, itertools, collections, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load, REPO_ROOT

N = 97
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEYWORDS = ("KRYPTOS", "PALIMPSEST", "ABSCISSA")
EXPECTED_READ_ORDER = {"KRYPTOS": [0, 5, 3, 1, 6, 4, 2],
                       "PALIMPSEST": [1, 7, 3, 2, 4, 0, 5, 6, 8, 9],
                       "ABSCISSA": [0, 7, 1, 3, 4, 2, 5, 6]}

k4 = load()
CT = k4.ciphertext
CRIB = {i: p for i, p, _ in k4.crib_positions()}
JP = sorted(CRIB)

print("# EXP-039 substitution o double columnar transposition, Kryptos-keyword keys")
print(f"ciphertext sha256 {k4.sha256}")
print("prereg docs/exp039-preregistration.md\n")


def read_order(kw):
    """Rank columns by (keyword letter, original column index); read in increasing rank."""
    return [c for _, c in sorted((ch, i) for i, ch in enumerate(kw))]


def col_lengths(w, n=N):
    return [(n - c + w - 1) // w for c in range(w)]


def single_pass(kw):
    """input position j -> output position. Row-wise fill, no padding, cols in key order."""
    w = len(kw)
    L = col_lengths(w)
    off, s = {}, 0
    for c in read_order(kw):
        off[c] = s
        s += L[c]
    assert s == N
    return [off[j % w] + (j // w) for j in range(N)]


print("## Frozen convention, hand-derived rankings asserted")
SINGLE = {}
for kw in KEYWORDS:
    ro = read_order(kw)
    assert ro == EXPECTED_READ_ORDER[kw], (kw, ro)
    SINGLE[kw] = single_pass(kw)
    assert sorted(SINGLE[kw]) == list(range(N))
    print(f"   {kw:<11} w={len(kw):>2}  read order {ro}")
print("   all three single passes are valid permutations of 0..96\n")

COMP = {(a, b): tuple(SINGLE[b][SINGLE[a][j]] for j in range(N))
        for a, b in itertools.product(KEYWORDS, repeat=2)}
uniq = collections.defaultdict(list)
for pair, p in COMP.items():
    uniq[p].append(pair)
print(f"## {len(COMP)} ordered pairs -> {len(uniq)} distinct composed permutations")
print(f"   identity among them: {any(p == tuple(range(N)) for p in uniq)}")
print(f"   equal to a single pass: "
      f"{any(p == tuple(t) for p in uniq for t in SINGLE.values())}")
print("   EXP-033 membership (audited in the preregistration): 0 of 9 - all genuinely new\n")


def decide(perm, ct=CT, crib=None):
    """Exact consistency. Returns (function?, bijection?, mapping, witness)."""
    crib = crib if crib is not None else CRIB
    smap = {}
    for j in sorted(crib):
        c = ct[perm[j]]
        p = crib[j]
        if p in smap and smap[p] != c:
            return False, False, None, {"plaintext_letter": p, "conflict": (smap[p], c),
                                        "at_plaintext_position": j,
                                        "at_ciphertext_position": perm[j]}
        smap[p] = c
    return True, len(set(smap.values())) == len(smap), smap, None


# ---------------------------------------------------------------- controls
print("## Controls")
rng = random.Random(39)
ctrl = collections.Counter()
cover = collections.Counter()
for (k1, k2), perm in sorted(COMP.items()):
    S = dict(zip(ALPHA, rng.sample(ALPHA, 26)))
    PT = ["X"] * N
    for i, ch in CRIB.items():
        PT[i] = ch
    synth = [None] * N
    for j in range(N):
        synth[perm[j]] = S[PT[j]]
    synth = "".join(synth)
    fn, bij, smap, _ = decide(perm, ct=synth)
    ok = fn and bij and all(S[p] == smap[p] for p in smap)
    ctrl["planted_total"] += 1
    ctrl["planted_pass"] += bool(ok)
    cover[f"first={k1}"] += 1
    cover[f"second={k2}"] += 1
    if k1 == k2:
        cover["same_key_pair"] += 1
    if len(k1) != len(k2):
        cover["different_widths"] += 1
    if k1 in ("PALIMPSEST", "ABSCISSA") or k2 in ("PALIMPSEST", "ABSCISSA"):
        cover["repeated_letter_keyword"] += 1
    # adversarial: mutate a ciphertext symbol inside a REPEATED-plaintext-letter group,
    # so the mutation is capable of breaking an equality constraint by construction
    dup = [p for p, n in collections.Counter(CRIB.values()).items() if n > 1]
    victim_pt = rng.choice(dup)
    victim_j = [j for j in JP if CRIB[j] == victim_pt][-1]
    bad = list(synth)
    bad[perm[victim_j]] = ALPHA[(ALPHA.index(bad[perm[victim_j]]) + 1 + rng.randrange(25)) % 26]
    fn2, _, _, _ = decide(perm, ct="".join(bad))
    ctrl["adv_total"] += 1
    ctrl["adv_pass"] += (not fn2)

# non-bijective plant: must be FEASIBLE-FUNCTION but NOT FEASIBLE-BIJECTION
perm = COMP[("KRYPTOS", "ABSCISSA")]
collapse = {ch: ("A" if ch in "EIOU" else ch) for ch in ALPHA}
PT = ["X"] * N
for i, ch in CRIB.items():
    PT[i] = ch
synth = [None] * N
for j in range(N):
    synth[perm[j]] = collapse[PT[j]]
fn3, bij3, _, _ = decide(perm, ct="".join(synth))
ctrl["nonbij_function"] = int(fn3)
ctrl["nonbij_rejected_as_bijection"] = int(fn3 and not bij3)

print(f"   planted positives : {ctrl['planted_pass']}/{ctrl['planted_total']}"
      " detected with the substitution recovered")
print(f"   adversarial       : {ctrl['adv_pass']}/{ctrl['adv_total']} flipped"
      " (each mutates a repeated-plaintext-letter group, so all are capable by construction)")
print(f"   non-bijective plant: FEASIBLE-FUNCTION={bool(fn3)}, "
      f"rejected as bijection={bool(ctrl['nonbij_rejected_as_bijection'])}")
print("   coverage          : " + ", ".join(f"{k}={v}" for k, v in sorted(cover.items())))
assert ctrl["planted_pass"] == ctrl["planted_total"], "positive control failed"
assert ctrl["adv_pass"] == ctrl["adv_total"], "adversarial control failed"
assert ctrl["nonbij_function"] and ctrl["nonbij_rejected_as_bijection"], "non-bijective control failed"
assert all(cover[f"first={k}"] and cover[f"second={k}"] for k in KEYWORDS)
assert cover["same_key_pair"] == 3 and cover["different_widths"] == 6
print()

# ---------------------------------------------------------------- the real test
print("## THE REAL TEST — exact consistency, no scoring")
rows, nfun, nbij = [], 0, 0
for (k1, k2), perm in sorted(COMP.items()):
    fn, bij, smap, wit = decide(perm)
    nfun += int(fn)
    nbij += int(bij)
    rows.append({"first": k1, "second": k2, "feasible_function": fn,
                 "feasible_bijection": bij,
                 "mapping": smap, "witness": wit})
    tag = ("FEASIBLE-BIJECTION" if bij else "FEASIBLE-FUNCTION") if fn else "CONTRADICTION"
    extra = ""
    if wit:
        extra = (f"  plaintext {wit['plaintext_letter']} needs both "
                 f"{wit['conflict'][0]} and {wit['conflict'][1]}"
                 f" (P pos {wit['at_plaintext_position']} -> C pos {wit['at_ciphertext_position']})")
    print(f"   {k1:<11} -> {k2:<11} {tag}{extra}")
print()
print(f"   permutations tested        : {len(COMP)} (all 9 genuinely new)")
print(f"   FEASIBLE-FUNCTION          : {nfun}")
print(f"   FEASIBLE-BIJECTION         : {nbij}")
print(f"   preregistered expectation  : 8.83e-16 function, 4.97e-17 bijection")
print()
if nfun == 0:
    print("## RESULT: NEGATIVE at the strongest level — contradiction on the FUNCTION criterion")
    print("   No standard no-padding double columnar transposition using an ordered pair drawn")
    print("   from {KRYPTOS, PALIMPSEST, ABSCISSA}, followed by ANY fixed monoalphabetic")
    print("   substitution, satisfies the 24 published K4 positional cribs under the")
    print("   preregistered columnar convention.")
    print()
    print("   NOT 'double transposition is eliminated'. NOT 'K4 does not use transposition'.")
    print("   NOT 'K4 cannot use these words in another role'. NOT 'arbitrary two-stage routes")
    print("   are eliminated'. The negative applies only to this tiny motivated keyword family.")
else:
    print("## SURVIVORS — candidate architecture only, nothing optimised")
    for r in rows:
        if r["feasible_function"]:
            print(f"   {r['first']} -> {r['second']}: bijection={r['feasible_bijection']}, "
                  f"constrained letters={len(r['mapping'])}, "
                  f"unconstrained={26 - len(r['mapping'])}")
            print(f"      forced mapping: {r['mapping']}")

out = os.path.join(REPO_ROOT, "results", "exp039")
os.makedirs(out, exist_ok=True)
json.dump({"experiment": "EXP-039", "ciphertext_sha256": k4.sha256,
           "prereg": "docs/exp039-preregistration.md",
           "grade": "STRUCTURALLY MOTIVATED, not documentary",
           "keywords": list(KEYWORDS), "read_orders": {k: read_order(k) for k in KEYWORDS},
           "ordered_pairs": 9, "distinct_permutations": len(uniq),
           "exp033_overlap": 0, "genuinely_new": 9,
           "null_P_function": 9.8076e-17, "null_P_bijection": 5.5193e-18,
           "expected_survivors_function": 8.83e-16,
           "feasible_function": nfun, "feasible_bijection": nbij,
           "results": rows, "controls": dict(ctrl), "control_coverage": dict(cover)},
          open(os.path.join(out, "summary.json"), "w"), indent=1)
print(f"\n   wrote results/exp039/summary.json")
