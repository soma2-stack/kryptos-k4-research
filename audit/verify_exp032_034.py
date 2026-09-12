"""Independent verifier for EXP-032 and EXP-034.

Imports neither experiment nor k4lib. Re-derives the geometry, the shift conventions,
the sources and the lags from the raw JSON and from first principles, re-decides every
verdict, and re-plants its own positive controls so a rubber-stamp verifier is excluded.
"""
import json, hashlib, os, sys, random, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KRY = "KRYPTOSABCDEFGHIJLMNQUVWXZ"
N = 97

k4 = json.load(open(os.path.join(ROOT, "data", "k4.json")))
CT = k4["ciphertext"]
assert k4["kryptos_alphabet"] == KRY, "KRYPTOS alphabet differs from the verifier's"
CRIB = {}
for c in k4["confirmed_cribs"]:
    for off, ch in enumerate(c["plaintext"]):
        CRIB[c["start"] + off] = ch

checks, fails = [], []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    if not ok:
        fails.append(name)


# ---------------------------------------------------------------- conventions, rebuilt
def idx(alpha, ch):
    return alpha.index(ch)


def key_index(p, c, combiner, pa, ca):
    pi, ci = idx(pa, p), idx(ca, c)
    if combiner == "vigenere":
        return (ci - pi) % 26
    if combiner == "beaufort":
        return (ci + pi) % 26
    return (pi - ci) % 26                       # variant_beaufort


def apply_key(p, k, combiner, pa, ca):
    pi = idx(pa, p)
    v = {"vigenere": (pi + k) % 26, "beaufort": (k - pi) % 26,
         "variant_beaufort": (pi - k) % 26}[combiner]
    return ca[v]


CONV = [(cb, pn, cn) for cb in ("vigenere", "beaufort", "variant_beaufort")
        for pn in ("STD", "KRY") for cn in ("STD", "KRY")]
ALPHAS = {"STD": STD, "KRY": KRY}
NAME = {(cb, pn, cn): f"{cb}/P={pn}/C={cn}" for cb, pn, cn in CONV}
check("verifier rebuilds 12 conventions", len(CONV) == 12)

# ---------------------------------------------------------------- EXP-032
s32 = json.load(open(os.path.join(ROOT, "results", "exp032", "summary.json")))


def col_of(i):
    if i < 4:
        return 28 + i
    if i < 35:
        return i - 3
    if i < 66:
        return i - 34
    return i - 65


check("row 26/27/28 of the NSA transcription equal K4[4:35], K4[35:66], K4[66:97]",
      CT[4:35] == "UOXOGHULBSOLIFBBWFLRVQQPRNGKSSO"
      and CT[35:66] == "TWTQSJQSSEKZZWATJKLUDIAWINFBNYP"
      and CT[66:97] == "VTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR")
by_col = collections.defaultdict(list)
for i in sorted(CRIB):
    by_col[col_of(i)].append(i)
coll = {c: v for c, v in sorted(by_col.items()) if len(v) > 1}
check("column collisions reproduced: exactly columns 29 and 30",
      coll == {29: [32, 63], 30: [33, 64]}, str(coll))
check("EXP-032 reports the same collisions",
      {int(k): v for k, v in s32["column_collisions"].items()} == coll)
check("EXP-032 reports 2 constraints per case", s32["constraints_per_case"] == 2)

feas32 = []
for cb, pn, cn in CONV:
    forced, ok = {}, True
    for i in sorted(CRIB):
        c = col_of(i)
        k = key_index(CRIB[i], CT[i], cb, ALPHAS[pn], ALPHAS[cn])
        if c in forced and forced[c] != k:
            ok = False
        forced.setdefault(c, k)
    if ok:
        feas32.append(NAME[(cb, pn, cn)])
check("EXP-032 re-decided independently: same feasible set",
      sorted(feas32) == sorted(s32["feasible"]), f"verifier {feas32} vs {s32['feasible']}")
check("EXP-032 elimination stands: no convention feasible", feas32 == [])

# replant, so the verifier is not vacuous
rng = random.Random(99)
replant = 0
for cb, pn, cn in CONV:
    f = {c: rng.randrange(26) for c in range(1, 32)}
    PT = ["X"] * N
    for i, p in CRIB.items():
        PT[i] = p
    synth = "".join(apply_key(PT[i], f[col_of(i)], cb, ALPHAS[pn], ALPHAS[cn])
                    for i in range(N))
    forced, ok = {}, True
    for i in sorted(CRIB):
        c = col_of(i)
        k = key_index(CRIB[i], synth[i], cb, ALPHAS[pn], ALPHAS[cn])
        if c in forced and forced[c] != k:
            ok = False
        forced.setdefault(c, k)
    replant += int(ok and all(forced[c] == f[c] for c in forced))
check("verifier recovers replanted column keys", replant == 12, f"{replant}/12")

# ---------------------------------------------------------------- EXP-034
s34 = json.load(open(os.path.join(ROOT, "results", "exp034", "summary.json")))
SRC = {"ct_fwd": [CT[j] for j in range(N)], "ct_rev": [CT[N - 1 - j] for j in range(N)]}
for m in (2, 3, 5, 7, 11):
    SRC[f"ct_dec_{m}"] = [CT[(m * j) % N] for j in range(N)]
SRC["pt"] = [CRIB.get(j) for j in range(N)]
check("verifier rebuilds the same 8 sources", sorted(SRC) == sorted(s34["sources"]))

rows = {(r["source"], r["lag"], r["convention"]): r for r in s34["rows"]}
check("EXP-034 reports 8 x 96 x 12 rows", len(rows) == 8 * 96 * 12 == s34["cases"])

mismatch = ndecided = nfeas = 0
for name, src in SRC.items():
    for lag in range(1, 97):
        for cb, pn, cn in CONV:
            seen, nc, bad = {}, 0, False
            for i in sorted(CRIB):
                j = i - lag
                if j < 0 or src[j] is None:
                    continue
                k = key_index(CRIB[i], CT[i], cb, ALPHAS[pn], ALPHAS[cn])
                s = src[j]
                if s in seen:
                    nc += 1
                    if seen[s] != k:
                        bad = True
                else:
                    seen[s] = k
            verdict = ("UNDECIDED" if nc < s34["min_constraints"]
                       else ("CONTRADICTION" if bad else "FEASIBLE"))
            r = rows[(name, lag, NAME[(cb, pn, cn)])]
            if r["verdict"] != verdict or r["constraints"] != nc:
                mismatch += 1
            ndecided += int(verdict != "UNDECIDED")
            nfeas += int(verdict == "FEASIBLE")
check("EXP-034 re-decided independently: every verdict and constraint count agrees",
      mismatch == 0, f"{mismatch} mismatches")
check("EXP-034 decided-case count agrees", ndecided == s34["decided"],
      f"verifier {ndecided} vs {s34['decided']}")
check("EXP-034 elimination stands: no decided case feasible", nfeas == 0, str(nfeas))
check("EXP-034 constraint count is independent of the verdict (the bug that was fixed)",
      max(r["constraints"] for r in s34["rows"] if r["verdict"] == "CONTRADICTION") >= 8)

replant34 = 0
for name in sorted(SRC):
    for lag in (4, 17, 53):
        cb, pn, cn = CONV[rng.randrange(12)]
        f = {ch: rng.randrange(26) for ch in STD}
        PT = ["X"] * N
        for i, p in CRIB.items():
            PT[i] = p
        src = SRC[name] if name != "pt" else [PT[j] for j in range(N)]
        synth = list(CT)
        for i in range(N):
            j = i - lag
            if j >= 0 and src[j] is not None:
                synth[i] = apply_key(PT[i], f[src[j]], cb, ALPHAS[pn], ALPHAS[cn])
        synth = "".join(synth)
        seen, bad = {}, False
        for i in sorted(CRIB):
            j = i - lag
            if j < 0 or SRC[name][j] is None:
                continue
            k = key_index(CRIB[i], synth[i], cb, ALPHAS[pn], ALPHAS[cn])
            s = SRC[name][j]
            if s in seen and seen[s] != k:
                bad = True
            seen.setdefault(s, k)
        replant34 += int(not bad and all(seen[s] == f[s] for s in seen))
check("verifier recovers replanted text-dependent keys", replant34 == 24, f"{replant34}/24")

print("# verify_exp032_034 — independent verification")
print(f"data/k4.json sha256 "
      f"{hashlib.sha256(open(os.path.join(ROOT, 'data', 'k4.json'), 'rb').read()).hexdigest()}\n")
for name, ok, detail in checks:
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}")
    if detail and not ok:
        print(f"          {detail}")
print(f"\n   {len(checks) - len(fails)}/{len(checks)} checks pass")
print(f"   EXP-034 cases re-decided from scratch: {8 * 96 * 12:,}"
      f"  (decided {ndecided:,}, feasible {nfeas})")
sys.exit(1 if fails else 0)
