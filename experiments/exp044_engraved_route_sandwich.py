"""EXP-044  M2 . pi . M1 with pi an engraved-geometry route over K4's own row structure.

Preregistered in docs/exp044-preregistration.md BEFORE implementation.
No K4 crib score was consulted in choosing any parameter.

pi corpus: k4lib.transpositions.engraved_routes() x {forward, inverse}, deduplicated
to 12 distinct permutations. Justification: K4's TEXTUAL row structure 4/31/31/31 is
Grade-A authenticated; routes over that ragged grid are the repository's existing
formalisation of it. EXP-033 tested them only behind a fixed monoalphabetic map;
EXP-036's transposition corpus is keyed columnar and excludes them; EXP-043's pi
corpus is affine mod 97 and is verified disjoint from this one.

    C[pi(j)] = combine( P[j], M1[j mod p] + M2[pi(j) mod q] )

Decided exactly by weighted union-find with potentials over Z26. No scoring,
no key enumeration.
"""
import json
import math
import os
import random
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from k4lib import transpositions as TR
from k4lib.permutations import affine_family

K4 = json.load(open(os.path.join(ROOT, "data", "k4.json")))
CT = K4["ciphertext"]
STD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KRY = K4["kryptos_alphabet"]
AL = {"STD": STD, "KRY": KRY}
CRIB = {}
for _cr in K4["confirmed_cribs"]:
    assert CT[_cr["start"]:_cr["start"] + len(_cr["plaintext"])] == _cr["ciphertext_segment"]
    for _j, _ch in enumerate(_cr["plaintext"]):
        CRIB[_cr["start"] + _j] = _ch
POS = sorted(CRIB)
N_POS = len(POS)
assert N_POS == 24
COMBINERS = ("vigenere", "beaufort", "variant_beaufort")
PAIRS = [(p, q) for p in range(1, 11) for q in range(1, 11)]


def derive_key(p_idx, c_idx, comb):
    if comb == "vigenere":
        return (c_idx - p_idx) % 26
    if comb == "beaufort":
        return (c_idx + p_idx) % 26
    return (p_idx - c_idx) % 26


def consistent(edges):
    """Decide a[u] + b[v] = c over Z26 by weighted union-find with potentials.

    Writing t[v] = -b[v] turns it into pot[u] - pot[v] = c, a difference system.
    Returns (consistent, rank) where rank = vertices touched - components.
    """
    parent, off = {}, {}

    def find(x):
        if x not in parent:
            parent[x], off[x] = x, 0
            return x, 0
        root, acc = x, 0
        while parent[root] != root:
            acc = (acc + off[root]) % 26
            root = parent[root]
        cur, cacc = x, acc
        while parent[cur] != cur:
            nxt, noff = parent[cur], off[cur]
            parent[cur], off[cur] = root, cacc
            cacc = (cacc - noff) % 26
            cur = nxt
        return root, acc

    verts = set()
    for u, v, c in edges:
        verts.add(u)
        verts.add(v)
        ru, au = find(u)
        rv, av = find(v)
        if ru == rv:
            if (au - av) % 26 != c % 26:
                return False, None
        else:
            parent[ru] = rv
            off[ru] = (c - au + av) % 26
    roots = {find(x)[0] for x in verts}
    return True, len(verts) - len(roots)


def route_corpus():
    """The declared pi corpus: engraved routes x orientations, deduplicated."""
    eng = TR.engraved_routes()
    labelled = {}
    for nm, order in sorted(eng.items()):
        labelled[nm + "/A"] = tuple(order)
        inv = [0] * 97
        for k, v in enumerate(order):
            inv[v] = k
        labelled[nm + "/B"] = tuple(inv)
    dedup = {}
    for nm, pm in labelled.items():
        dedup.setdefault(pm, nm)
    return [(nm, list(pm)) for pm, nm in dedup.items()], labelled


def key_tables(ct):
    """KEY[(comb,pa,ca)][n][t] = key implied if crib n lands at ciphertext position t."""
    tab = {}
    for comb in COMBINERS:
        for pa in ("STD", "KRY"):
            pidx = {ch: i for i, ch in enumerate(AL[pa])}
            pv = [pidx[CRIB[j]] for j in POS]
            for ca in ("STD", "KRY"):
                cidx = {ch: i for i, ch in enumerate(AL[ca])}
                cvals = [cidx[ch] for ch in ct]
                tab[(comb, pa, ca)] = [
                    [derive_key(pv[n], cvals[t], comb) for t in range(97)]
                    for n in range(N_POS)]
    return tab


def edges_for(pi, p, q, comb, pa, ca, tab):
    K = tab[(comb, pa, ca)]
    return [(("A", POS[n] % p), ("B", pi[POS[n]] % q), K[n][pi[POS[n]]])
            for n in range(N_POS)]


def main():
    print("# EXP-044  M2 . pi . M1 with pi an engraved-geometry route")
    print("prereg: docs/exp044-preregistration.md\n")

    corpus, labelled = route_corpus()
    print("## Corpus, fixed before any test")
    print(f"   engraved routes            : {len(TR.engraved_routes())}")
    print(f"   x 2 orientations           : {len(labelled)}")
    print(f"   distinct after dedup       : {len(corpus)}")
    aff = {tuple(p) for _, p in affine_family()}
    overlap = [nm for nm, pm in corpus if tuple(pm) in aff]
    print(f"   affine family size         : {len(aff)}")
    print(f"   overlap with EXP-043       : {len(overlap)}  {overlap if overlap else '(disjoint)'}")
    ident = list(range(97))
    print(f"   identity present           : {any(pm == ident for _, pm in corpus)}")
    assert not overlap, "corpus must be disjoint from EXP-043"
    assert not any(pm == ident for _, pm in corpus)
    CONVS = [(c, pa, ca) for c in COMBINERS for pa in ("STD", "KRY")
             for ca in ("STD", "KRY")]
    N = len(corpus) * len(PAIRS) * len(CONVS)
    print(f"   period pairs               : {len(PAIRS)}  (p,q in 1..10)")
    print(f"   conventions                : {len(CONVS)}")
    print(f"   N                          : {N:,}\n")

    # ---------------------------------------------------------------- controls
    print("## Controls")
    rng = random.Random(20260921)
    route0_name, pi0 = corpus[0][0], corpus[0][1]
    p0, q0, comb0, pa0, ca0 = 7, 9, "vigenere", "KRY", "KRY"
    m1 = [rng.randrange(26) for _ in range(p0)]
    m2 = [rng.randrange(26) for _ in range(q0)]
    pidx = {ch: i for i, ch in enumerate(AL[pa0])}
    plain = [rng.randrange(26) for _ in range(97)]
    for i, ch in CRIB.items():
        plain[i] = pidx[ch]
    synth = [None] * 97
    for j in range(97):
        k = (m1[j % p0] + m2[pi0[j] % q0]) % 26
        synth[pi0[j]] = AL[ca0][(plain[j] + k) % 26]
    synth_ct = "".join(synth)
    stab = key_tables(synth_ct)

    ok_pos, rank_pos = consistent(edges_for(pi0, p0, q0, comb0, pa0, ca0, stab))
    print(f"   positive control            : {'PASS' if ok_pos else 'FAIL'}"
          f"  (planted {route0_name} p={p0} q={q0}, rank {rank_pos})")

    perm_bad = list(range(97))
    rng.shuffle(perm_bad)
    not_affine = tuple(perm_bad) not in aff
    not_engraved = tuple(perm_bad) not in {tuple(p) for _, p in corpus}
    ok_perm, _ = consistent(edges_for(perm_bad, p0, q0, comb0, pa0, ca0, stab))
    print(f"   out-of-family permutation   : "
          f"{'PASS' if (not_affine and not_engraved and not ok_perm) else 'FAIL'}"
          f"  (non-affine={not_affine}, non-engraved={not_engraved}, feasible={ok_perm})")

    # adversarial: corrupt a CRIB-CONSTRAINED ciphertext position
    victim = pi0[POS[0]]
    bad = list(synth_ct)
    bad[victim] = STD[(STD.index(bad[victim]) + 13) % 26]
    ok_adv, _ = consistent(edges_for(pi0, p0, q0, comb0, pa0, ca0,
                                     key_tables("".join(bad))))
    print(f"   adversarial crib corruption : {'PASS' if not ok_adv else 'FAIL'}"
          f"  (position {victim} flips feasibility)")

    # blind-region: corrupt a position OUTSIDE every crib image
    crib_img = {pi0[j] for j in POS}
    blind = next(t for t in range(97) if t not in crib_img)
    bad2 = list(synth_ct)
    bad2[blind] = STD[(STD.index(bad2[blind]) + 13) % 26]
    ok_blind, _ = consistent(edges_for(pi0, p0, q0, comb0, pa0, ca0,
                                       key_tables("".join(bad2))))
    print(f"   blind-region control        : {'PASS' if ok_blind else 'FAIL'}"
          f"  (position {blind} is unreachable, stays feasible)")

    assert ok_pos and not ok_perm and not ok_adv and ok_blind
    assert not_affine and not_engraved
    print()

    # ---------------------------------------------------------------- sweep
    print("## Exhaustive sweep over the declared corpus")
    tab = key_tables(CT)
    t0 = time.time()
    feasible = []
    decided = 0
    dmin, dmax = 99, -1
    for (nm, pi) in corpus:
        for (p, q) in PAIRS:
            for (comb, pa, ca) in CONVS:
                ok, rank = consistent(edges_for(pi, p, q, comb, pa, ca, tab))
                decided += 1
                if ok:
                    dmin = min(dmin, rank)
                    dmax = max(dmax, rank)
                    feasible.append(dict(route=nm, p=p, q=q, combiner=comb,
                                         plain_alpha=pa, cipher_alpha=ca,
                                         rank=rank))
    el = time.time() - t0
    print(f"   decided   : {decided:,} configurations in {el:.1f}s")
    print(f"   FEASIBLE  : {len(feasible)}")
    if feasible:
        for f in feasible[:20]:
            print("     ", f)

    # worst-case budget recomputed from the actual run
    worst_d = 0
    for (nm, pi) in corpus:
        for (p, q) in PAIRS:
            verts = {("A", POS[n] % p) for n in range(N_POS)} | \
                    {("B", pi[POS[n]] % q) for n in range(N_POS)}
            _, r = consistent([(u, v, 0) for (u, v, _c) in
                               edges_for(pi, p, q, "vigenere", "STD", "STD", tab)])
            worst_d = max(worst_d, r if r is not None else 0)
    budget = math.log(decided, 26) + worst_d
    print(f"\n   worst d_eff (from run)      : {worst_d}")
    print(f"   log26(N)                    : {math.log(decided, 26):.3f}")
    print(f"   budget                      : {budget:.3f}"
          f"   {'PASS' if budget < 24 else 'FAIL'}")
    print(f"   expected accidental survivors: {decided * 26.0 ** -(24 - worst_d):.4f}")

    out = {
        "id": "EXP-044",
        "preregistration": "docs/exp044-preregistration.md",
        "routes_distinct": len(corpus),
        "route_labels": sorted(nm for nm, _ in corpus),
        "period_pairs": len(PAIRS),
        "conventions": len(CONVS),
        "configurations_decided": decided,
        "feasible": len(feasible),
        "feasible_detail": feasible[:50],
        "worst_d_eff": worst_d,
        "log26_N": round(math.log(decided, 26), 4),
        "budget": round(budget, 4),
        "expected_accidental_survivors": round(decided * 26.0 ** -(24 - worst_d), 6),
        "disjoint_from_exp043": True,
        "controls": {"positive": bool(ok_pos), "out_of_family": not ok_perm,
                     "adversarial": not ok_adv, "blind_region": bool(ok_blind)},
        "seconds": round(el, 2),
    }
    d = os.path.join(ROOT, "results", "exp044")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "summary.json"), "w") as fh:
        json.dump(out, fh, indent=2)
    print(f"\n   wrote results/exp044/summary.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
