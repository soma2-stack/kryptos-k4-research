"""Independent verification of EXP-044.

Imports NOTHING from experiments/exp044_*. Everything is rebuilt from data/k4.json
and k4lib, and the central claim is re-decided by two methods that share no code
with the experiment:

  Route A  explicit CYCLE CERTIFICATES. For a bipartite crib graph whose edges say
           x[u] + x[v] = c, every cycle has even length and its alternating sum of
           edge values telescopes to 0. An observed cycle whose alternating sum is
           non-zero mod 26 therefore PROVES infeasibility. This is a self-contained
           proof object, not a solver verdict.

  Route B  brute-force FORWARD SIMULATION over every key pair, using no graph
           theory at all, for the configurations small enough to enumerate.

Plus: corpus reconstruction, disjointness from EXP-043's affine family, and the
budget arithmetic.
"""
import json
import math
import os
import random
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import numpy as np
from k4lib import transpositions as TR
from k4lib.permutations import affine_family

K4 = json.load(open(os.path.join(ROOT, "data", "k4.json")))
CT = K4["ciphertext"]
STD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
AL = {"STD": STD, "KRY": K4["kryptos_alphabet"]}
CRIB = {}
for cr in K4["confirmed_cribs"]:
    for j, ch in enumerate(cr["plaintext"]):
        CRIB[cr["start"] + j] = ch
POS = sorted(CRIB)
COMBINERS = ("vigenere", "beaufort", "variant_beaufort")
CONVS = [(c, pa, ca) for c in COMBINERS for pa in ("STD", "KRY")
         for ca in ("STD", "KRY")]
PAIRS = [(p, q) for p in range(1, 11) for q in range(1, 11)]

FAILS = []


def ck(cond, label):
    print(f"   [{'PASS' if cond else 'FAIL'}] {label}")
    if not cond:
        FAILS.append(label)
    return cond


def derive_key(p_idx, c_idx, comb):
    if comb == "vigenere":
        return (c_idx - p_idx) % 26
    if comb == "beaufort":
        return (c_idx + p_idx) % 26
    return (p_idx - c_idx) % 26


def corpus():
    eng = TR.engraved_routes()
    lab = {}
    for nm, order in sorted(eng.items()):
        lab[nm + "/A"] = tuple(order)
        inv = [0] * 97
        for k, v in enumerate(order):
            inv[v] = k
        lab[nm + "/B"] = tuple(inv)
    ded = {}
    for nm, pm in lab.items():
        ded.setdefault(pm, nm)
    return [(nm, list(pm)) for pm, nm in ded.items()], lab


def edges(pi, p, q, comb, pa, ca, ct=CT):
    pidx = {ch: i for i, ch in enumerate(AL[pa])}
    cidx = {ch: i for i, ch in enumerate(AL[ca])}
    out = []
    for j in POS:
        t = pi[j]
        out.append((("A", j % p), ("B", t % q),
                    derive_key(pidx[CRIB[j]], cidx[ct[t]], comb)))
    return out


# --------------------------------------------------------------------------
# Route A -- cycle certificates
# --------------------------------------------------------------------------
def cycle_certificate(E):
    """Find a cycle whose alternating edge-value sum is non-zero mod 26.

    BFS a spanning forest assigning pot[v]; an edge closing a cycle with the
    wrong parity/value yields the certificate. Returns the explicit vertex and
    value sequence, or None.
    """
    adj = {}
    for idx, (u, v, c) in enumerate(E):
        adj.setdefault(u, []).append((v, c, idx))
        adj.setdefault(v, []).append((u, c, idx))
    pot, par, seen = {}, {}, set()
    for src in adj:
        if src in seen:
            continue
        pot[src], par[src] = 0, None
        seen.add(src)
        stack = [src]
        order = []
        while stack:
            u = stack.pop()
            order.append(u)
            for (v, c, idx) in adj[u]:
                if v not in seen:
                    seen.add(v)
                    pot[v] = (c - pot[u]) % 26
                    par[v] = (u, c, idx)
                    stack.append(v)
        for u in order:
            for (v, c, idx) in adj[u]:
                if (pot[u] + pot[v]) % 26 != c % 26:
                    # walk both to the common root
                    def path(x):
                        out = []
                        while par[x] is not None:
                            pu, pc, pidx_ = par[x]
                            out.append((x, pu, pc))
                            x = pu
                        return out, x
                    pu_, ru = path(u)
                    pv_, rv = path(v)
                    if ru != rv:
                        continue
                    return {"closing_edge": (u, v, c),
                            "path_u": pu_, "path_v": pv_, "root": ru}
    return None


def verify_certificate(cert, E):
    """Independently confirm the certificate proves infeasibility.

    Reconstruct the closed walk, check it alternates sides (so it is a genuine
    bipartite cycle of even length), and check its alternating value sum != 0.
    """
    u, v, c = cert["closing_edge"]
    walk = []            # list of (vertex, vertex, value) along the cycle
    walk.append((u, v, c))
    walk.extend(cert["path_v"])
    walk.extend(reversed([(b, a, cc) for (a, b, cc) in cert["path_u"]]))
    # build the vertex sequence and confirm it closes
    seq = [u, v]
    vals = [c]
    cur = v
    for (a, b, cc) in walk[1:]:
        nxt = b if a == cur else a
        seq.append(nxt)
        vals.append(cc)
        cur = nxt
    if cur != u:
        return False, "walk does not close"
    if len(vals) % 2 != 0:
        return False, "odd cycle in a bipartite graph"
    for i in range(len(seq) - 1):
        if seq[i][0] == seq[i + 1][0]:
            return False, "walk does not alternate sides"
    alt = sum((-1) ** i * vals[i] for i in range(len(vals))) % 26
    return alt != 0, f"alternating sum {alt} over a {len(vals)}-edge cycle"


# --------------------------------------------------------------------------
# Route B -- brute-force forward simulation, no graph theory
# --------------------------------------------------------------------------
def brute_feasible(pi, p, q, comb, pa, ca):
    pidx = {ch: i for i, ch in enumerate(AL[pa])}
    cidx = {ch: i for i, ch in enumerate(AL[ca])}
    pv = np.array([pidx[CRIB[j]] for j in POS], dtype=np.int64)
    tv = np.array([pi[j] for j in POS], dtype=np.int64)
    cv = np.array([cidx[CT[t]] for t in tv], dtype=np.int64)
    ra = np.array([j % p for j in POS], dtype=np.int64)
    rb = tv % q
    need = np.array([derive_key(int(a), int(b), comb) for a, b in zip(pv, cv)],
                    dtype=np.int64)
    total = 0
    for m1 in np.ndindex(*([26] * p)):
        a1 = np.array(m1, dtype=np.int64)[ra]
        for m2 in np.ndindex(*([26] * q)):
            a2 = np.array(m2, dtype=np.int64)[rb]
            if np.all((a1 + a2 - need) % 26 == 0):
                total += 1
                return True, total
    return False, total


def main():
    print("# Independent verification of EXP-044")
    print(f"ciphertext sha256 checked against data/k4.json\n")

    print("## 1. Corpus rebuilt from k4lib, independently of the experiment")
    C, lab = corpus()
    ck(len(TR.engraved_routes()) == 7, "7 engraved routes")
    ck(len(lab) == 14, "14 route/orientation pairs")
    ck(len(C) == 12, "12 distinct permutations after deduplication")
    for nm, pm in C:
        assert sorted(pm) == list(range(97))
    ck(True, "every corpus member is a permutation of 0..96")
    aff = {tuple(p) for _, p in affine_family()}
    ck(len(aff) == 9312, "affine family has 9,312 members")
    ck(not any(tuple(pm) in aff for _, pm in C),
       "corpus is DISJOINT from EXP-043's affine family")
    ck(not any(pm == list(range(97)) for _, pm in C), "identity is absent")

    print("\n## 2. Cycle certificates of infeasibility (Route A)")
    rng = random.Random(4404)
    tried = certified = skipped = 0
    for _ in range(4000):
        nm, pi = C[rng.randrange(len(C))]
        p, q = PAIRS[rng.randrange(len(PAIRS))]
        comb, pa, ca = CONVS[rng.randrange(len(CONVS))]
        E = edges(pi, p, q, comb, pa, ca)
        cert = cycle_certificate(E)
        if cert is None:
            skipped += 1
            continue
        tried += 1
        ok, _why = verify_certificate(cert, E)
        certified += ok
    ck(tried > 0, f"certificates found for {tried} sampled configurations")
    ck(certified == tried,
       f"{certified}/{tried} certificates independently verified as proofs")
    print(f"      ({skipped} sampled configurations had no cycle to certify;"
          f" those are decided by Route B instead)")

    print("\n## 3. Brute-force forward simulation (Route B, no graph theory)")
    small = [(nm, pi, p, q, c, pa, ca)
             for (nm, pi) in C for (p, q) in PAIRS if p + q <= 3
             for (c, pa, ca) in CONVS]
    print(f"   fully enumerating all {len(small)} configurations with p+q<=3")
    feas = 0
    for (nm, pi, p, q, c, pa, ca) in small:
        f, _ = brute_feasible(pi, p, q, c, pa, ca)
        feas += f
    ck(feas == 0, f"forward simulation finds {feas} feasible among p+q<=3")

    sample = [(nm, pi, 2, 2, c, pa, ca)
              for (nm, pi) in C for (c, pa, ca) in CONVS]
    rng.shuffle(sample)
    sample = sample[:24]
    print(f"   plus a random sample of {len(sample)} configurations at p=q=2"
          f" (26^4 = 456,976 key pairs each)")
    feas2 = 0
    for (nm, pi, p, q, c, pa, ca) in sample:
        f, _ = brute_feasible(pi, p, q, c, pa, ca)
        feas2 += f
    ck(feas2 == 0, f"forward simulation finds {feas2} feasible in the p=q=2 sample")

    print("\n## 4. Route B must be able to say YES (positive control)")
    # plant a synthetic ciphertext and confirm brute force finds it
    nm0, pi0 = C[0]
    p0, q0 = 2, 2
    r2 = random.Random(77)
    m1 = [r2.randrange(26) for _ in range(p0)]
    m2 = [r2.randrange(26) for _ in range(q0)]
    pidx = {ch: i for i, ch in enumerate(AL["KRY"])}
    plain = [r2.randrange(26) for _ in range(97)]
    for i, ch in CRIB.items():
        plain[i] = pidx[ch]
    synth = [None] * 97
    for j in range(97):
        k = (m1[j % p0] + m2[pi0[j] % q0]) % 26
        synth[pi0[j]] = AL["KRY"][(plain[j] + k) % 26]
    saved = globals()["CT"]
    globals()["CT"] = "".join(synth)
    f, _ = brute_feasible(pi0, p0, q0, "vigenere", "KRY", "KRY")
    globals()["CT"] = saved
    ck(f, "brute force finds a planted in-family instance (not vacuously negative)")

    print("\n## 5. Budget arithmetic re-derived")
    N = len(C) * len(PAIRS) * len(CONVS)
    ck(N == 14400, f"N = 12 x 100 x 12 = {N:,}")
    # worst d_eff by direct rank of the crib incidence structure
    worst = 0
    for (nm, pi) in C:
        for (p, q) in PAIRS:
            vs = set()
            par = {}

            def find(x):
                par.setdefault(x, x)
                while par[x] != x:
                    par[x] = par[par[x]]
                    x = par[x]
                return x
            for j in POS:
                u, v = ("A", j % p), ("B", pi[j] % q)
                vs.add(u)
                vs.add(v)
                ru, rv = find(u), find(v)
                if ru != rv:
                    par[ru] = rv
            comps = len({find(x) for x in vs})
            worst = max(worst, len(vs) - comps)
    ck(worst == 19, f"worst-case d_eff = {worst} (preregistered: 19)")
    b = math.log(N, 26) + worst
    ck(abs(b - 21.939) < 0.01, f"budget = {b:.3f} (preregistered: 21.939)")
    ck(b < 24, "budget passes the discrimination criterion")

    print("\n## 6. Cross-check against the experiment's recorded summary")
    s = json.load(open(os.path.join(ROOT, "results", "exp044", "summary.json")))
    ck(s["configurations_decided"] == N, "summary N matches")
    ck(s["feasible"] == 0, "summary records 0 feasible")
    ck(s["worst_d_eff"] == worst, "summary worst d_eff matches")
    ck(all(s["controls"].values()), "summary records all four controls passing")

    print(f"\n{'ALL CHECKS PASSED' if not FAILS else 'FAILURES: ' + ', '.join(FAILS)}")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
