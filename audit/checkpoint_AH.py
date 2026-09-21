"""Checkpoint AH: fixed artifact diagnostics, never a cipher/key search.
Run: python audit/checkpoint_AH.py --output results/checkpoint_AH.json
Protocol: audit/checkpoint_AH_protocol.md. NumPy required; no project imports.
"""
import argparse
from collections import Counter, defaultdict
from itertools import combinations
import hashlib
import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
D = json.loads((ROOT / "data/k4.json").read_text())
C = D["ciphertext"]
STD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KRY = D["kryptos_alphabet"]
P = {c["start"] + j: x for c in D["confirmed_cribs"]
     for j, x in enumerate(c["plaintext"])}
POS = sorted(P)
assert len(C) == 97 and len(P) == 24
assert C[21:34] == "FLRVQQPRNGKSS" and C[63:74] == "NYPVTTMZFPK"
assert "".join(P[i] for i in range(21, 34)) == "EASTNORTHEAST"
assert "".join(P[i] for i in range(63, 74)) == "BERLINCLOCK"
NAMES = ["support", "letter_collision_pairs", "bigram_collision_pairs",
         "trigram_collision_pairs", "adjacent_doubles", "max_lag_z_1_48",
         "max_period_z_2_48", "STD_max_difference_bin", "KRY_max_difference_bin",
         "STD_translated_trigram_pairs", "KRY_translated_trigram_pairs",
         "row_composition"]
X = np.array([STD.index(x) for x in C], dtype=np.int64)
KMAP = np.array([KRY.index(x) for x in STD])
PAIRS = {n: np.triu_indices(n, 1) for n in (95, 96)}
ROWS = [(0, 4), (4, 35), (35, 66), (66, 97)]


def pair_collisions(a):
    i, j = PAIRS[a.shape[1]]
    return (a[:, i] == a[:, j]).sum(axis=1)


def features(a):
    hist = np.stack([(a == k).sum(axis=1) for k in range(26)], axis=1)
    lag = np.stack([(a[:, :-d] == a[:, d:]).sum(axis=1)
                    for d in range(1, 97)], axis=1)
    q = 1 / 26
    n = np.arange(96, 48, -1)
    lag_z = ((lag[:, :48] - n*q) / np.sqrt(n*q*(1-q))).max(axis=1)
    per_z = []
    for p in range(2, 49):
        distances = np.arange(p, 97, p)
        m = (97 - distances).sum()
        v = lag[:, distances - 1].sum(axis=1)
        per_z.append((v - m*q) / np.sqrt(m*q*(1-q)))
    big = a[:, :-1]*26 + a[:, 1:]
    tri = a[:, :-2]*676 + a[:, 1:-1]*26 + a[:, 2:]
    diffmax, translated = [], []
    for b in (a, KMAP[a]):
        diff = (b[:, 1:] - b[:, :-1]) % 26
        diffmax.append(np.stack([(diff == k).sum(axis=1)
                                 for k in range(26)], axis=1).max(axis=1))
        translated.append(pair_collisions(diff[:, :-1]*26 + diff[:, 1:]))
    rowstat = np.zeros(a.shape[0])
    for s, e in ROWS:
        h = np.stack([(a[:, s:e] == k).sum(axis=1) for k in range(26)], axis=1)
        expected = hist * ((e-s)/97)
        rowstat += np.divide((h-expected)**2, expected,
                             out=np.zeros_like(expected), where=expected > 0).sum(axis=1)
    return np.stack([(hist > 0).sum(axis=1), (hist*(hist-1)//2).sum(axis=1),
                     pair_collisions(big), pair_collisions(tri), lag[:, 0],
                     lag_z, np.stack(per_z, axis=1).max(axis=1),
                     *diffmax, *translated, rowstat], axis=1)


def raw():
    repeats = {}
    for size in range(2, 7):
        groups = defaultdict(list)
        for i in range(98-size):
            groups[C[i:i+size]].append(i)
        repeats[str(size)] = {w: v for w, v in sorted(groups.items()) if len(v) > 1}
    distances = {ch: [j-i for i, j in combinations([k for k, x in enumerate(C) if x == ch], 2)]
                 for ch in STD}
    pairs = [{"i": i, "j": j, "distance": j-i, "same_P": P[i] == P[j],
              "same_C": C[i] == C[j], "cross_crib": i < 34 <= j}
             for i, j in combinations(POS, 2)]
    algebra = {}
    for pa in (STD, KRY):
        for ca in (STD, KRY):
            pv = {i: pa.index(P[i]) for i in POS}
            cv = {i: ca.index(C[i]) for i in POS}
            for comb in ("C-P", "C+P", "P-C"):
                k = {i: ((cv[i]-pv[i]) if comb == "C-P" else
                         (cv[i]+pv[i]) if comb == "C+P" else
                         (pv[i]-cv[i])) % 26 for i in POS}
                name = ("STD" if pa == STD else "KRY") + "/" + (
                    "STD" if ca == STD else "KRY") + "/" + comb
                algebra[name] = {"values": [k[i] for i in POS],
                    "first_differences": [[(k[i+1]-k[i]) % 26 for i in range(s, e-1)]
                                          for s, e in ((21,34),(63,74))],
                    "unique_values": len(set(k.values()))}
    block = {}
    for size in range(2, 6):
        block[str(size)] = []
        for offset in range(size):
            g = defaultdict(list)
            for i in range(offset, 98-size, size):
                if all(j in P for j in range(i, i+size)):
                    g["".join(P[j] for j in range(i, i+size))].append(i)
            block[str(size)].append({w: v for w, v in g.items() if len(v) > 1})
    local_groups = defaultdict(list)
    for i in POS:
        start = next(s for s, e in ROWS if s <= i < e)
        local_groups[i-start].append(i)
    return {"histogram": dict(sorted(Counter(C).items())),
            "ioc": sum(n*(n-1) for n in Counter(C).values())/(97*96),
            "repeated_substrings": repeats, "symbol_distances": distances,
            "lag_matches_1_96": [sum(C[i] == C[i+d] for i in range(97-d)) for d in range(1,97)],
            "crib_pairs": pairs, "crib_pair_counts": dict(Counter(
                f"P{int(p['same_P'])}C{int(p['same_C'])}" for p in pairs)),
            "fixed_points": [i for i in POS if P[i] == C[i]],
            "period_constraints_1_96": {str(p): 24-len({i%p for i in POS}) for p in range(1,97)},
            "algebra_12_conventions": algebra, "block_repeats": block,
            "row_local_shared_crib_groups": [v for _, v in sorted(local_groups.items()) if len(v) > 1]}


def run():
    rng = np.random.Generator(np.random.PCG64(20260913))
    obs = features(X[None, :])[0]
    stats = {}
    null_arrays = {}
    for kind in ("uniform", "histogram_permutation"):
        blocks = []
        for _ in range(40):
            a = rng.integers(0, 26, size=(250, 97)) if kind == "uniform" else np.stack(
                [rng.permutation(X) for _ in range(250)])
            blocks.append(features(a))
        vals = np.concatenate(blocks)
        null_arrays[kind] = vals
        stats[kind] = {}
        for j, name in enumerate(NAMES):
            lo = (1 + int(np.count_nonzero(vals[:, j] <= obs[j] + 1e-9))) / 10001
            hi = (1 + int(np.count_nonzero(vals[:, j] >= obs[j] - 1e-9))) / 10001
            stats[kind][name] = {"observed": float(obs[j]), "mean": float(vals[:, j].mean()),
                "q025": float(np.quantile(vals[:, j], .025)), "q975": float(np.quantile(vals[:, j], .975)),
                "p_lower": lo, "p_upper": hi, "p_two_sided": min(1, 2*min(lo, hi)),
                "p_bonferroni_24": min(1, 48*min(lo, hi)),
                "invariant_under_null": bool(np.all(np.abs(vals[:, j]-obs[j]) < 1e-9))}
    rows = json.loads((ROOT/"data/cipher_side_rows.json").read_text())["rows"]
    k3 = "".join(rows[str(r)] for r in range(15,25)) + rows["25"].split("?")[0]
    assert len(k3) == 336
    assert rows["25"].split("?")[1] + rows["26"] + rows["27"] + rows["28"] == C
    sample = rng.choice(np.array(list(k3)), size=(10000, 97))
    h = np.stack([(sample == x).sum(axis=1) for x in STD], axis=1)
    coll = (h*(h-1)//2).sum(axis=1)
    threshold = float(np.quantile(null_arrays["uniform"][:, 1], .95))
    result = {"protocol": "audit/checkpoint_AH_protocol.md", "seed": 20260913,
              "numpy_version": np.__version__, "draws_per_null": 10000,
              "ciphertext_sha256": hashlib.sha256(C.encode()).hexdigest(),
              "raw": raw(), "statistics": stats,
              "power_illustration_K3_iid_profile": {
                  "uniform_95pct_collision_threshold": threshold,
                  "power_exceeding_threshold": float(np.mean(coll > threshold)),
                  "fraction_at_or_below_K4": float(np.mean(coll <= obs[1])),
                  "K3_inventory": dict(sorted(Counter(k3).items()))}}
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
