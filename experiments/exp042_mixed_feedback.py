"""EXP-042  Mixed plaintext/ciphertext two-tap propagating feedback.

Preregistered in docs/exp042-preregistration.md BEFORE implementation.

    k[i] = alpha*P[i-a] + beta*C[i-b] + gamma      (beta != 0)
    C[i] = combine(P[i], k[i])

Substituting the encryption relation gives, for vigenere,

    k[i] + alpha*k[i-a] = alpha*C[i-a] + beta*C[i-b] + gamma

so the ciphertext tap is a KNOWN DRIVING TERM: it contributes nothing to the
recursive structure. The recurrence is FIRST ORDER in k with lag a, the unknowns
are the a warm-up values, and the components are chains mod a. The constraint
budget is therefore identical to EXP-040's.

Only ONE orientation is enumerated: the swap alpha*C[i-a] + beta*P[i-b] produces
byte-identical linear systems with the lags exchanged (proven in the prereg).
beta = 0 is excluded because it is exactly EXP-040.
"""
import json
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from k4lib.modlin import chance_solvable, count_solutions_mod26, solutions_mod26, _rref

K4 = json.load(open(os.path.join(ROOT, "data", "k4.json")))
CT_REAL = K4["ciphertext"]
STD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KRY = K4["kryptos_alphabet"]
AL = {"STD": STD, "KRY": KRY}
CRIB = {}
for _cr in K4["confirmed_cribs"]:
    assert CT_REAL[_cr["start"]:_cr["start"] + len(_cr["plaintext"])] == _cr["ciphertext_segment"]
    for _j, _ch in enumerate(_cr["plaintext"]):
        CRIB[_cr["start"] + _j] = _ch
POS = sorted(CRIB)
COMBINERS = ("vigenere", "beaufort", "variant_beaufort")
UNITS = [u for u in range(1, 26) if math.gcd(u, 26) == 1]
LAGS = range(1, 25)


def affine(ct, a, b, al, be, gf, comb, ca, rev):
    """P[i] = const[i] + sum_t coef[i][t]*u_t; unknowns are the a warm-up values."""
    ci = {ch: i for i, ch in enumerate(AL[ca])}
    cv = [ci[ch] for ch in ct]
    n = a + (1 if gf else 0)
    const = [0] * 97
    coef = [[0] * n for _ in range(97)]
    seeds = sorted(range(96, 96 - a, -1)) if rev else list(range(a))
    sidx = {s: k for k, s in enumerate(seeds)}
    for i in (range(96, -1, -1) if rev else range(97)):
        if i in sidx:
            j = sidx[i]
            if comb == "vigenere":
                const[i], coef[i][j] = cv[i], 25
            elif comb == "beaufort":
                const[i], coef[i][j] = (-cv[i]) % 26, 1
            else:
                const[i], coef[i][j] = cv[i], 1
        else:
            ip = i + a if rev else i - a
            ic = i + b if rev else i - b
            kc = [(al * coef[ip][t]) % 26 for t in range(n)]
            kk = (al * const[ip] + (be * cv[ic] if 0 <= ic < 97 else 0)) % 26
            if gf:
                kc[n - 1] = (kc[n - 1] + 1) % 26
            if comb == "vigenere":
                const[i] = (cv[i] - kk) % 26
                coef[i] = [(-c) % 26 for c in kc]
            elif comb == "beaufort":
                const[i] = (kk - cv[i]) % 26
                coef[i] = kc[:]
            else:
                const[i] = (cv[i] + kk) % 26
                coef[i] = kc[:]
    return const, coef, n


def system(ct, cribs, a, b, al, be, gf, comb, pa, ca, rev):
    const, coef, n = affine(ct, a, b, al, be, gf, comb, ca, rev)
    pi = {ch: i for i, ch in enumerate(AL[pa])}
    keys = sorted(cribs)
    return ([coef[i] for i in keys],
            [(pi[cribs[i]] - const[i]) % 26 for i in keys], const, coef, n)


def canonical(rows, rhs, n):
    M = [r[:] for r in rows]
    for t in range(n):
        col = [M[r][t] for r in range(len(M))]
        best = min(tuple((c * u) % 26 for c in col) for u in UNITS)
        for r in range(len(M)):
            M[r][t] = best[r]
    cols = sorted(range(n), key=lambda t: tuple(M[r][t] for r in range(len(M))))
    A = [[M[r][t] for t in cols] + [rhs[r]] for r in range(len(M))]
    out = []
    for p in (2, 13):
        red, _, rank = _rref([[v % p for v in r] for r in A], n, p)
        out.append((rank, tuple(tuple(r) for r in red[:rank])))
    return tuple(out)


def rebuild(ct, a, b, al, be, gf, comb, pa, ca, rev, u):
    const, coef, n = affine(ct, a, b, al, be, gf, comb, ca, rev)
    v = [(const[i] + sum(coef[i][t] * u[t] for t in range(n))) % 26 for i in range(97)]
    return "".join(AL[pa][x] for x in v)


def main():
    print("# EXP-042  mixed plaintext/ciphertext two-tap propagating feedback")
    print("prereg: docs/exp042-preregistration.md\n")

    print("## Controls")
    import random
    random.seed(20260921)
    a0, b0, al0, be0, comb0 = 5, 3, 1, 1, "vigenere"
    plain = [random.randrange(26) for _ in range(97)]
    for i, ch in CRIB.items():
        plain[i] = STD.index(ch)                       # REAL cribs at REAL positions
    warm = [random.randrange(26) for _ in range(a0)]
    cv = [0] * 97
    for i in range(97):
        k = warm[i] if i < a0 else (al0 * plain[i - a0] + be0 * cv[i - b0]) % 26
        cv[i] = (plain[i] + k) % 26
    synth = "".join(STD[x] for x in cv)

    rows, rhs, _, _, n = system(synth, CRIB, a0, b0, al0, be0, False, comb0, "STD", "STD", False)
    nsol = count_solutions_mod26(rows, rhs)
    rec = None
    if nsol:
        s = solutions_mod26(rows, rhs, limit=1)
        rec = rebuild(synth, a0, b0, al0, be0, False, comb0, "STD", "STD", False, s[0])
    ok_pos = bool(nsol) and rec == "".join(STD[x] for x in plain)
    print(f"  positive control: planted a={a0} b={b0} mixed feedback carrying the real cribs"
          f" -> {nsol} solution(s), full plaintext rebuilt exactly -> "
          f"{'PASS' if ok_pos else 'FAIL'}")

    bad = list(synth)
    bad[26] = STD[(STD.index(bad[26]) + 9) % 26]
    r2, h2, *_ = system("".join(bad), CRIB, a0, b0, al0, be0, False, comb0, "STD", "STD", False)
    ok_con = count_solutions_mod26(r2, h2) == 0
    print(f"  contradiction control: corruption at 26 inside a constrained chain -> "
          f"{'rejected' if ok_con else 'still accepted'} -> {'PASS' if ok_con else 'FAIL'}")

    blind = list(synth)
    blind[95] = STD[(STD.index(blind[95]) + 4) % 26]
    r3, h3, *_ = system("".join(blind), CRIB, a0, b0, al0, be0, False, comb0, "STD", "STD", False)
    ok_blind = count_solutions_mod26(r3, h3) > 0
    print(f"  blind-region control: corruption at 95, downstream of every crib in its chain "
          f"-> {'absorbed' if ok_blind else 'rejected'} -> "
          f"{'PASS (expected absorption)' if ok_blind else 'FAIL'}")

    if not (ok_pos and ok_con and ok_blind):
        print("\nCONTROLS FAILED - results not reported")
        return 1

    print("\n## Sweep against the real K4 ciphertext")
    seen, feasible, raw = set(), [], 0
    for a in LAGS:
        for b in LAGS:
            for al in (1, 25):
                for be in (1, 25):                     # beta = 0 excluded: it is EXP-040
                    for gf in (False, True):
                        for comb in COMBINERS:
                            for pa in ("STD", "KRY"):
                                for ca in ("STD", "KRY"):
                                    for rev in (False, True):
                                        raw += 1
                                        rows, rhs, _, _, n = system(
                                            CT_REAL, CRIB, a, b, al, be, gf, comb, pa, ca, rev)
                                        key = canonical(rows, rhs, n)
                                        if key in seen:
                                            continue
                                        seen.add(key)
                                        if count_solutions_mod26(rows, rhs):
                                            feasible.append(dict(
                                                a=a, b=b, alpha=al, beta=be, gamma_free=gf,
                                                combiner=comb, plain_alpha=pa, cipher_alpha=ca,
                                                reverse=rev,
                                                chance=chance_solvable(rows)))
    print(f"  raw configurations      : {raw:,}")
    print(f"  distinct tests decided  : {len(seen):,}")
    print(f"  FEASIBLE                : {len(feasible)}")
    for f in feasible[:20]:
        print(f"    {f}")

    confirmed = []
    for f in feasible:
        rows, rhs, *_ , n = system(CT_REAL, CRIB, f["a"], f["b"], f["alpha"], f["beta"],
                                   f["gamma_free"], f["combiner"], f["plain_alpha"],
                                   f["cipher_alpha"], f["reverse"])
        for u in solutions_mod26(rows, rhs, limit=200) or []:
            pt = rebuild(CT_REAL, f["a"], f["b"], f["alpha"], f["beta"], f["gamma_free"],
                         f["combiner"], f["plain_alpha"], f["cipher_alpha"], f["reverse"], u)
            if all(pt[i] == ch for i, ch in CRIB.items()):
                confirmed.append({**f, "solution": list(u)})
                break
    print(f"  survivors reproducing every crib after reconstruction: {len(confirmed)}")

    out = {"experiment": "EXP-042", "prereg": "docs/exp042-preregistration.md",
           "raw": raw, "distinct": len(seen), "feasible": feasible, "confirmed": confirmed,
           "controls": {"positive": ok_pos, "contradiction": ok_con,
                        "blind_region": ok_blind}}
    os.makedirs(os.path.join(ROOT, "results", "exp042"), exist_ok=True)
    json.dump(out, open(os.path.join(ROOT, "results", "exp042", "summary.json"), "w"),
              indent=2, sort_keys=True, default=str)
    print("\n  wrote results/exp042/summary.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
