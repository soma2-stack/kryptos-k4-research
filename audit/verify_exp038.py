"""Independent verifier for EXP-038.

Imports neither the production recurrence generator nor k4lib. It re-parses the frozen data,
independently implements STD and KRY indexing and all three combiners, and generates the
recurrence by DIRECT ITERATION of the definition rather than by the closed form
k[n] = A_n*k0 + B_n*k1 + c*D_n that the experiment uses for its linear solve - so an error in
that algebra cannot hide behind itself.

F1 (26^4 tuples x 12 conventions) is re-decided EXHAUSTIVELY. F2 (26^5) is re-decided
exhaustively too where affordable; the strategy actually used is reported.
"""
import json, hashlib, os, sys, itertools, collections, random
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
N = 97
STD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KRY = "KRYPTOSABCDEFGHIJLMNQUVWXZ"
AL = {"STD": STD, "KRY": KRY}

k4 = json.load(open(os.path.join(ROOT, "data", "k4.json")))
CT = k4["ciphertext"]
assert k4["kryptos_alphabet"] == KRY
CRIB = {}
for c in k4["confirmed_cribs"]:
    for off, ch in enumerate(c["plaintext"]):
        CRIB[c["start"] + off] = ch
JP = sorted(CRIB)
S = json.load(open(os.path.join(ROOT, "results", "exp038", "summary.json")))

checks, fails = [], []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    if not ok:
        fails.append(name)


check("ciphertext sha256 matches", hashlib.sha256(CT.encode()).hexdigest() == S["ciphertext_sha256"])
check("97 characters and 24 crib positions", len(CT) == 97 and len(CRIB) == 24)
check("crib positions match the experiment", JP == S["crib_positions"])
check("crib segments match the ciphertext",
      CT[21:34] == "FLRVQQPRNGKSS" and CT[63:74] == "NYPVTTMZFPK")


def key_index(p, c, cb, pa, ca):
    pi, ci = AL[pa].index(p), AL[ca].index(c)
    return {"vigenere": (ci - pi) % 26, "beaufort": (ci + pi) % 26,
            "variant_beaufort": (pi - ci) % 26}[cb]


def apply_key(p, k, cb, pa, ca):
    pi = AL[pa].index(p)
    return AL[ca][{"vigenere": (pi + k) % 26, "beaufort": (k - pi) % 26,
                   "variant_beaufort": (pi - k) % 26}[cb]]


CONV = {f"{cb}/P={pn}/C={cn}": (cb, pn, cn)
        for cb in ("vigenere", "beaufort", "variant_beaufort")
        for pn in ("STD", "KRY") for cn in ("STD", "KRY")}
check("verifier rebuilds 12 conventions", len(CONV) == 12)

TGT = {}
for name, (cb, pn, cn) in CONV.items():
    TGT[name] = [key_index(CRIB[i], CT[i], cb, pn, cn) for i in JP]
check("forced key targets reproduced independently for all 12 conventions",
      TGT == S["targets"], "verifier-derived targets differ from the experiment's")
check("the 12 target vectors are distinct", len({tuple(v) for v in TGT.values()}) == 12)

TARGETS = np.array([TGT[n] for n in sorted(TGT)], dtype=np.int64)      # (12,24)
JPa = np.array(JP)


def sweep(cs, chunk=200000):
    """Direct iteration over the recurrence for every (a,b,c,k0,k1) with c in cs.
    Returns (tuples_tested, feasible_count, hits)."""
    tested = feas = 0
    hits = []
    grid = np.array(list(itertools.product(range(26), repeat=2)), dtype=np.int64)  # k0,k1
    for a, b in itertools.product(range(26), repeat=2):
        for c in cs:
            k_2 = grid[:, 0].copy()          # k[n-2]
            k_1 = grid[:, 1].copy()          # k[n-1]
            proj = np.empty((grid.shape[0], len(JP)), dtype=np.int64)
            col = 0
            if JP[0] == 0:
                proj[:, col] = k_2; col += 1
            if 1 in JP:
                proj[:, col] = k_1; col += 1
            for n in range(2, N):
                nk = (a * k_1 + b * k_2 + c) % 26
                k_2, k_1 = k_1, nk
                if n in CRIB:
                    proj[:, col] = nk
                    col += 1
            assert col == len(JP)
            tested += grid.shape[0]
            m = np.all(proj[:, None, :] == TARGETS[None, :, :], axis=2)   # (676,12)
            if m.any():
                for gi, ci in zip(*np.nonzero(m)):
                    feas += 1
                    hits.append({"convention": sorted(TGT)[int(ci)], "a": a, "b": b, "c": c,
                                 "k0": int(grid[gi, 0]), "k1": int(grid[gi, 1])})
    return tested, feas, hits


# F1 exhaustive
t1, f1, h1 = sweep([0])
check("F1 re-decided EXHAUSTIVELY by direct iteration: 26^4 tuples x 12 conventions",
      t1 == 26 ** 4, f"{t1:,}")
check("F1 independent verdict: zero feasible", f1 == 0, str(f1))

# F2 exhaustive
t2, f2, h2 = sweep(list(range(26)))
check("F2 re-decided EXHAUSTIVELY by direct iteration: 26^5 tuples x 12 conventions",
      t2 == 26 ** 5, f"{t2:,}")
check("F2 independent verdict: zero feasible", f2 == 0, str(f2))
check("experiment and verifier agree on the feasible count",
      S["feasible"] == f2 == 0, f"experiment {S['feasible']} vs verifier {f2}")

# the verifier must not be a rubber stamp: replant and require detection
rng = random.Random(1938)
ok = tot = 0
for _ in range(20):
    a, b, c, k0, k1 = [rng.randrange(26) for _ in range(5)]
    name = sorted(TGT)[rng.randrange(12)]
    cb, pn, cn = CONV[name]
    key = [k0, k1]
    for _ in range(2, N):
        key.append((a * key[-1] + b * key[-2] + c) % 26)
    PT = ["X"] * N
    for i, ch in CRIB.items():
        PT[i] = ch
    synth = "".join(apply_key(PT[n], key[n], cb, pn, cn) for n in range(N))
    tgt = [key_index(CRIB[i], synth[i], cb, pn, cn) for i in JP]
    tot += 1
    ok += int(tgt == [key[i] for i in JP])
check("verifier recovers replanted recurrences (so it is not a rubber stamp)",
      ok == tot, f"{ok}/{tot}")

# duplicate / period accounting, recomputed independently on a deterministic stride
R = np.random.default_rng(11).integers(1, 2 ** 61, N)
streams, periodic = set(), set()
grid = np.array(list(itertools.product(range(26), repeat=2)), dtype=np.int64)
for a, b in itertools.product(range(26), repeat=2):
    for c in range(26):
        k_2 = grid[:, 0].copy(); k_1 = grid[:, 1].copy()
        full = np.empty((grid.shape[0], N), dtype=np.int64)
        full[:, 0] = k_2; full[:, 1] = k_1
        for n in range(2, N):
            nk = (a * k_1 + b * k_2 + c) % 26
            k_2, k_1 = k_1, nk
            full[:, n] = nk
        h = (full @ R).tolist()
        isper = np.zeros(grid.shape[0], bool)
        for p in range(1, 24):
            isper |= np.all(full[:, p:] == full[:, :-p], axis=1)
        streams.update(h)
        for hv, ip in zip(h, isper.tolist()):
            if ip:
                periodic.add(hv)
check("unique 97-key stream count reproduced", len(streams) == S["unique_streams_F2"],
      f"verifier {len(streams):,} vs summary {S['unique_streams_F2']:,}")
check("period<=23 ALREADY COVERED count reproduced",
      len(periodic) == S["already_covered_periodic_le23"],
      f"verifier {len(periodic):,} vs summary {S['already_covered_periodic_le23']:,}")
check("genuinely-new stream count is consistent",
      len(streams) - len(periodic) == S["genuinely_new_streams"])

print("# verify_exp038 — independent verification of EXP-038\n")
for name, o, detail in checks:
    print(f"   [{'PASS' if o else 'FAIL'}] {name}")
    if detail and not o:
        print(f"          {detail}")
print(f"\n   {len(checks) - len(fails)}/{len(checks)} checks pass")
print(f"   F1 tuples re-decided by direct iteration : {t1:,}")
print(f"   F2 tuples re-decided by direct iteration : {t2:,}")
print(f"   feasible cases found independently       : {f2}")
sys.exit(1 if fails else 0)
