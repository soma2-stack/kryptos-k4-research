"""EXP-041  Additive two-tap propagating plaintext feedback.

Preregistered in docs/exp041-preregistration.md BEFORE implementation.

    k[i] = alpha*P[i-a] + beta*P[i-b] + gamma          (mod 26)
    P[i] = uncombine(C[i], k[i])

The recursion is linear, so every P[i] is affine in the unknowns -- the b warm-up
key values, plus one if gamma is free -- and each crib position contributes one
linear equation over Z26. Solvability is decided exactly by CRT through GF(2) and
GF(13). There is no search and no scoring anywhere.

Outside EXP-038: substituting P = C - k gives k[i] + k[i-a] + k[i-b] = C[i-a] +
C[i-b], a key recurrence WITH a ciphertext driving term, where EXP-038 registered
an autonomous one. Outside EXP-040 because a < b makes it genuinely two-tap.
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
ALPHA = {"STD": STD, "KRY": KRY}
CRIB = {}
for _cr in K4["confirmed_cribs"]:
    assert CT_REAL[_cr["start"]:_cr["start"] + len(_cr["plaintext"])] == _cr["ciphertext_segment"]
    for _j, _ch in enumerate(_cr["plaintext"]):
        CRIB[_cr["start"] + _j] = _ch
POS = sorted(CRIB)

COMBINERS = ("vigenere", "beaufort", "variant_beaufort")
COEFFS = ((1, 1), (1, 25), (25, 1), (25, 25))
B_MAX = 19                      # frozen: b >= 20 is weak, never a survivor
UNITS = [u for u in range(1, 26) if math.gcd(u, 26) == 1]


def affine(ct, a, b, al, be, gamma_free, comb, ca, reverse):
    """P[i] = const[i] + sum_t coef[i][t]*u_t, over all 97 positions."""
    cidx = {ch: i for i, ch in enumerate(ALPHA[ca])}
    cv = [cidx[ch] for ch in ct]
    n = b + (1 if gamma_free else 0)
    const = [0] * 97
    coef = [[0] * n for _ in range(97)]
    seeds = sorted(range(96, 96 - b, -1)) if reverse else list(range(b))
    seedidx = {s: k for k, s in enumerate(seeds)}
    order = range(96, -1, -1) if reverse else range(97)
    for i in order:
        if i in seedidx:
            j = seedidx[i]
            if comb == "vigenere":
                const[i] = cv[i]; coef[i][j] = 25
            elif comb == "beaufort":
                const[i] = (-cv[i]) % 26; coef[i][j] = 1
            else:
                const[i] = cv[i]; coef[i][j] = 1
        else:
            ia = i + a if reverse else i - a
            ib = i + b if reverse else i - b
            kc = [(al * coef[ia][t] + be * coef[ib][t]) % 26 for t in range(n)]
            kk = (al * const[ia] + be * const[ib]) % 26
            if gamma_free:
                kc[n - 1] = (kc[n - 1] + 1) % 26
            if comb == "vigenere":
                const[i] = (cv[i] - kk) % 26; coef[i] = [(-c) % 26 for c in kc]
            elif comb == "beaufort":
                const[i] = (kk - cv[i]) % 26; coef[i] = kc[:]
            else:
                const[i] = (cv[i] + kk) % 26; coef[i] = kc[:]
    return const, coef, n


def system(ct, cribs, a, b, al, be, gf, comb, pa, ca, rev):
    const, coef, n = affine(ct, a, b, al, be, gf, comb, ca, rev)
    pidx = {ch: i for i, ch in enumerate(ALPHA[pa])}
    rows = [coef[i] for i in sorted(cribs)]
    rhs = [(pidx[cribs[i]] - const[i]) % 26 for i in sorted(cribs)]
    return rows, rhs, const, coef, n


def canonical(rows, rhs, n):
    """Canonical form up to unit scaling of each unknown, then RREF -- used to
    collapse configurations that impose exactly the same test."""
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


def reconstruct(ct, a, b, al, be, gf, comb, pa, ca, rev, u):
    """Rebuild all 97 plaintext letters from a solution vector and re-encrypt."""
    const, coef, n = affine(ct, a, b, al, be, gf, comb, ca, rev)
    vals = [(const[i] + sum(coef[i][t] * u[t] for t in range(n))) % 26 for i in range(97)]
    return "".join(ALPHA[pa][v] for v in vals)


def sweep(ct, cribs, report=False):
    """Decide every distinct configuration. Returns (n_enumerated, distinct, feasible)."""
    seen, feasible, enumerated = set(), [], 0
    for b in range(2, B_MAX + 1):
        for a in range(1, b):
            for (al, be) in COEFFS:
                for gf in (False, True):
                    for comb in COMBINERS:
                        for pa in ("STD", "KRY"):
                            for ca in ("STD", "KRY"):
                                for rev in (False, True):
                                    enumerated += 1
                                    rows, rhs, _, _, n = system(
                                        ct, cribs, a, b, al, be, gf, comb, pa, ca, rev)
                                    key = canonical(rows, rhs, n)
                                    if key in seen:
                                        continue
                                    seen.add(key)
                                    if count_solutions_mod26(rows, rhs):
                                        feasible.append(
                                            dict(a=a, b=b, alpha=al, beta=be, gamma_free=gf,
                                                 combiner=comb, plain_alpha=pa,
                                                 cipher_alpha=ca, reverse=rev,
                                                 chance=chance_solvable(rows)))
    return enumerated, len(seen), feasible


def main():
    print("# EXP-041  additive two-tap propagating plaintext feedback")
    print("prereg: docs/exp041-preregistration.md\n")

    # ------------------------------------------------------------- controls
    print("## Controls")
    a0, b0, comb0, pa0, ca0 = 3, 7, "vigenere", "STD", "STD"
    import random
    random.seed(20260921)
    plain = [random.randrange(26) for _ in range(97)]
    for i, ch in CRIB.items():
        plain[i] = STD.index(ch)                      # the REAL cribs at REAL positions
    warm = [random.randrange(26) for _ in range(b0)]
    synth = [None] * 97
    for i in range(97):
        k = warm[i] if i < b0 else (plain[i - a0] + plain[i - b0]) % 26
        synth[i] = (plain[i] + k) % 26                # vigenere encrypt
    synth_ct = "".join(STD[v] for v in synth)

    rows, rhs, _, _, n = system(synth_ct, CRIB, a0, b0, 1, 1, False, comb0, pa0, ca0, False)
    nsol = count_solutions_mod26(rows, rhs)
    rec = None
    if nsol:
        sols = solutions_mod26(rows, rhs, limit=1)
        rec = reconstruct(synth_ct, a0, b0, 1, 1, False, comb0, pa0, ca0, False, sols[0])
    ok_pos = bool(nsol) and rec == "".join(STD[v] for v in plain)
    print(f"  positive control: planted a={a0} b={b0} two-tap carrying the real cribs -> "
          f"{nsol} solution(s), full plaintext rebuilt exactly -> "
          f"{'PASS' if ok_pos else 'FAIL'}")

    # adversarial: corrupt a position the dependency graph says must conflict
    bad = list(synth_ct)
    bad[30] = STD[(STD.index(bad[30]) + 11) % 26]
    r2, h2, _, _, _ = system("".join(bad), CRIB, a0, b0, 1, 1, False, comb0, pa0, ca0, False)
    ok_adv = count_solutions_mod26(r2, h2) == 0
    print(f"  adversarial control: corruption at index 30 (inside the crib span) -> "
          f"{'rejected' if ok_adv else 'still accepted'} -> {'PASS' if ok_adv else 'FAIL'}")

    # blind region: a change beyond every crib must be absorbed
    blind = list(synth_ct)
    blind[96] = STD[(STD.index(blind[96]) + 5) % 26]
    r3, h3, _, _, _ = system("".join(blind), CRIB, a0, b0, 1, 1, False, comb0, pa0, ca0, False)
    ok_blind = count_solutions_mod26(r3, h3) > 0
    print(f"  blind-region control: corruption at index 96 (beyond every crib) -> "
          f"{'absorbed' if ok_blind else 'rejected'} -> "
          f"{'PASS (confirms crib-span theory)' if ok_blind else 'FAIL'}")

    if not (ok_pos and ok_adv and ok_blind):
        print("\nCONTROLS FAILED - results not reported")
        return 1

    # ---------------------------------------------------------------- sweep
    print("\n## Sweep against the real K4 ciphertext")
    enumerated, distinct, feasible = sweep(CT_REAL, CRIB)
    print(f"  configurations enumerated : {enumerated:,}")
    print(f"  distinct tests decided    : {distinct:,}")
    print(f"  FEASIBLE                  : {len(feasible)}")
    for f in feasible[:20]:
        print(f"    {f}")

    confirmed = []
    for f in feasible:
        rows, rhs, _, _, n = system(CT_REAL, CRIB, f["a"], f["b"], f["alpha"], f["beta"],
                                    f["gamma_free"], f["combiner"], f["plain_alpha"],
                                    f["cipher_alpha"], f["reverse"])
        for u in solutions_mod26(rows, rhs, limit=200) or []:
            pt = reconstruct(CT_REAL, f["a"], f["b"], f["alpha"], f["beta"], f["gamma_free"],
                             f["combiner"], f["plain_alpha"], f["cipher_alpha"],
                             f["reverse"], u)
            if all(pt[i] == ch for i, ch in CRIB.items()):
                confirmed.append({**f, "solution": list(u)})
                break
    print(f"  survivors reproducing every crib letter after reconstruction: {len(confirmed)}")

    print("\n## Declared-weak range (b >= 20), reported, never counted as survivors")
    for b in range(20, 24):
        print(f"    b={b}: chance ~26^({b}-24) -> WEAK / UNDECIDABLE, excluded in advance")

    out = {"experiment": "EXP-041", "prereg": "docs/exp041-preregistration.md",
           "enumerated": enumerated, "distinct": distinct,
           "feasible": feasible, "confirmed": confirmed,
           "controls": {"positive": ok_pos, "adversarial": ok_adv, "blind_region": ok_blind}}
    os.makedirs(os.path.join(ROOT, "results", "exp041"), exist_ok=True)
    json.dump(out, open(os.path.join(ROOT, "results", "exp041", "summary.json"), "w"),
              indent=2, sort_keys=True, default=str)
    print("\n  wrote results/exp041/summary.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
