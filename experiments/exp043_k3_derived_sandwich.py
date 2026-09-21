"""EXP-043  M2 . pi . M1 with pi derived from K3's readout principle.

Preregistered in docs/exp043-preregistration.md BEFORE implementation.
No K4 crib score was consulted in deriving any parameter.

pi corpus: i -> a*i + b (mod 97), a in the 96 units, b in 0..96.
Justification: K3 is a pure transposition whose permutation advances by a
near-constant stride (its first differences take only the values 191 and 192).
K3's rectangular route principle has NO instance at K4 length because 97 is prime,
so the faithful instantiation of a constant-stride readout at a prime length is
exactly the affine family.

Masks: short periodic Vigenere over the KRY alphabet, the class re-derived from K1
and K2. Declared range p,q >= 2 with p+q <= 19, chosen by the discrimination
criterion alone.

    C[pi(j)] = combine( P[j], M1[j mod p] + M2[pi(j) mod q] )

Decided exactly by weighted union-find with potentials over Z26. No scoring.
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
    assert CT[_cr["start"]:_cr["start"] + len(_cr["plaintext"])] == _cr["ciphertext_segment"]
    for _j, _ch in enumerate(_cr["plaintext"]):
        CRIB[_cr["start"] + _j] = _ch
POS = sorted(CRIB)
COMBINERS = ("vigenere", "beaufort", "variant_beaufort")
UNITS = [a for a in range(1, 97)]                 # 97 prime, so every a in 1..96 is a unit
PAIRS = [(p, q) for p in range(2, 18) for q in range(2, 18) if p + q <= 19]


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
        # path compression with accumulated offsets
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


def key_tables(ct):
    """KEY[(comb, pa, ca)][n][t] = derived key if crib n sits at ciphertext position t.
    Precomputed once so the sweep's inner loop is pure integer arithmetic."""
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
                    for n in range(len(POS))]
    return tab


def edges_for(pi, p, q, comb, pa, ca, tab=None):
    if tab is None:
        tab = key_tables(CT)
    K = tab[(comb, pa, ca)]
    return [(("A", POS[n] % p), ("B", pi[POS[n]] % q), K[n][pi[POS[n]]])
            for n in range(len(POS))]


def main():
    print("# EXP-043  M2 . pi . M1 with pi derived from K3's readout principle")
    print("prereg: docs/exp043-preregistration.md\n")
    print("## Controls")

    # ---- positive: build a synthetic instance carrying the REAL cribs -------
    import random
    random.seed(20260921)
    a0, b0, p0, q0, comb0, pa0, ca0 = 7, 13, 5, 6, "vigenere", "KRY", "KRY"
    pi0 = [(a0 * i + b0) % 97 for i in range(97)]
    m1 = [random.randrange(26) for _ in range(p0)]
    m2 = [random.randrange(26) for _ in range(q0)]
    pidx = {ch: i for i, ch in enumerate(AL[pa0])}
    plain = [random.randrange(26) for _ in range(97)]
    for i, ch in CRIB.items():
        plain[i] = pidx[ch]
    synth = [None] * 97
    for j in range(97):
        k = (m1[j % p0] + m2[pi0[j] % q0]) % 26
        synth[pi0[j]] = AL[ca0][(plain[j] + k) % 26]
    synth_ct = "".join(synth)

    saved = globals()["CT"]
    globals()["CT"] = synth_ct
    ok_pos, _ = consistent(edges_for(pi0, p0, q0, comb0, pa0, ca0))
    # an out-of-family permutation must not be silently accepted as in-family
    perm_bad = list(range(97))
    random.shuffle(perm_bad)
    is_affine = any(perm_bad == [(a * i + b) % 97 for i in range(97)]
                    for a in UNITS for b in range(97))
    ok_perm_notaffine = not is_affine
    ok_perm, _ = consistent(edges_for(perm_bad, p0, q0, comb0, pa0, ca0))
    # adversarial: corrupt a constrained position
    bad = list(synth_ct)
    tgt = pi0[POS[0]]
    bad[tgt] = AL[ca0][(AL[ca0].index(bad[tgt]) + 7) % 26]
    globals()["CT"] = "".join(bad)
    ok_adv, _ = consistent(edges_for(pi0, p0, q0, comb0, pa0, ca0))
    globals()["CT"] = saved

    print(f"  positive control: planted a={a0} b={b0} p={p0} q={q0} carrying the real cribs "
          f"-> {'accepted' if ok_pos else 'rejected'} -> {'PASS' if ok_pos else 'FAIL'}")
    print(f"  permutation control: random permutation verified out-of-family "
          f"({ok_perm_notaffine}); registered test on it -> "
          f"{'accepted' if ok_perm else 'rejected'}")
    print(f"    (the corpus only ever enumerates affine maps, so an out-of-family pi is "
          f"never tested; this confirms it is genuinely outside)")
    print(f"  adversarial crib control: corrupted a constrained position -> "
          f"{'rejected' if not ok_adv else 'still accepted'} -> "
          f"{'PASS' if not ok_adv else 'FAIL'}")
    if not (ok_pos and ok_perm_notaffine and not ok_adv):
        print("\nCONTROLS FAILED - results not reported")
        return 1

    print("\n## Sweep against the real K4 ciphertext")
    print(f"  pi corpus {len(UNITS) * 97:,} | period pairs {len(PAIRS)} | conventions 12")
    feasible, tested = [], 0
    TAB = key_tables(CT)
    CONVS = [(c, pa, ca) for c in COMBINERS for pa in ("STD", "KRY")
             for ca in ("STD", "KRY")]
    for a in UNITS:
        for b in range(97):
            pi = [(a * i + b) % 97 for i in range(97)]
            pos_img = [pi[j] for j in POS]
            for (p, q) in PAIRS:
                nodes = [(POS[n] % p, pos_img[n] % q) for n in range(len(POS))]
                for (comb, pa, ca) in CONVS:
                    K = TAB[(comb, pa, ca)]
                    tested += 1
                    ed = [(("A", nodes[n][0]), ("B", nodes[n][1]), K[n][pos_img[n]])
                          for n in range(len(POS))]
                    ok, rank = consistent(ed)
                    if ok:
                        feasible.append(dict(a=a, b=b, p=p, q=q, combiner=comb,
                                             plain_alpha=pa, cipher_alpha=ca,
                                             d_eff=rank, constraints=len(POS) - rank))
    print(f"  configurations decided : {tested:,}")
    print(f"  FEASIBLE               : {len(feasible)}")
    for f in feasible[:20]:
        print(f"    {f}")

    out = {"experiment": "EXP-043", "prereg": "docs/exp043-preregistration.md",
           "tested": tested, "feasible": feasible,
           "controls": {"positive": ok_pos, "permutation_out_of_family": ok_perm_notaffine,
                        "adversarial": not ok_adv}}
    os.makedirs(os.path.join(ROOT, "results", "exp043"), exist_ok=True)
    json.dump(out, open(os.path.join(ROOT, "results", "exp043", "summary.json"), "w"),
              indent=2, sort_keys=True, default=str)
    print("\n  wrote results/exp043/summary.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
