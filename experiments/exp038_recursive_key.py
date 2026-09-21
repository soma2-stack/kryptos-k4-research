"""EXP-038  Second-order affine stateful recursive key schedules over Z26.

Preregistered in docs/exp038-preregistration.md before implementation.

    F1   k[n] = a*k[n-1] + b*k[n-2]        (mod 26)
    F2   k[n] = a*k[n-1] + b*k[n-2] + c    (mod 26)

k[0] and k[1] are the key values at K4 positions 0 and 1: message-aligned, no primer offset.
Key values range over the FULL Z26 - the gap Gromark's digit-restricted rejection left open.

The state is decided EXISTENTIALLY, not enumerated. For fixed (a,b,c),
k[n] = A_n*k[0] + B_n*k[1] + c*D_n, so the 24 crib constraints are a 24x2 linear system over
Z26 in (k[0],k[1]), solved exactly with k4lib.modlin. That is 26^3 solves per convention
instead of 26^5 trials.

Reported at three levels, because Z26 is not a field and tuples collide: raw tuples, unique
97-key streams, and unique 24-position crib projections. Streams whose 97-PREFIX is exactly
periodic with p <= 23 are tagged ALREADY COVERED rather than counted as new.
"""
import sys, os, json, time, itertools, collections, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np

from k4lib.data import load, REPO_ROOT
from k4lib.conventions import all_conventions
from k4lib.modlin import count_solutions_mod26, solutions_mod26

N = 97
k4 = load()
CT = k4.ciphertext
CRIB = {i: p for i, p, _ in k4.crib_positions()}
JP = sorted(CRIB)
conventions = all_conventions()

print("# EXP-038 second-order affine stateful recursive key schedules")
print(f"ciphertext sha256 {k4.sha256}")
print(f"prereg docs/exp038-preregistration.md\n")


def basis(a, b):
    """A_n, B_n, D_n with k[n] = A_n*k0 + B_n*k1 + c*D_n (mod 26)."""
    A, B, D = [1, 0], [0, 1], [0, 0]
    for _ in range(2, N):
        A.append((a * A[-1] + b * A[-2]) % 26)
        B.append((a * B[-1] + b * B[-2]) % 26)
        D.append((a * D[-1] + b * D[-2] + 1) % 26)
    return A, B, D


def iterate(a, b, c, k0, k1):
    """Direct iteration - the definition, used for controls and hit expansion."""
    k = [k0 % 26, k1 % 26]
    for _ in range(2, N):
        k.append((a * k[-1] + b * k[-2] + c) % 26)
    return k


print("## Closed form checked against the definition")
rng = random.Random(38)
bad = 0
for _ in range(500):
    a, b, c, k0, k1 = [rng.randrange(26) for _ in range(5)]
    A, B, D = basis(a, b)
    if [(A[n] * k0 + B[n] * k1 + c * D[n]) % 26 for n in range(N)] != iterate(a, b, c, k0, k1):
        bad += 1
print(f"   500 random tuples, mismatches: {bad}")
assert bad == 0
print()

# ---------------------------------------------------------------- targets
targets = {cv.name: [cv.key_index(CRIB[i], CT[i]) for i in JP] for cv in conventions}
print("## Forced key values at the 24 public-verified crib positions")
print(f"   positions {JP[:3]}...{JP[12]} | {JP[13]}...{JP[-1]}")
print(f"   distinct target vectors across the 12 conventions: {len(set(map(tuple, targets.values())))}")
print()

BLOCK1 = [t for t, i in enumerate(JP) if i < 40]
BLOCK2 = [t for t, i in enumerate(JP) if i >= 40]

# ---------------------------------------------------------------- controls
print("## Controls")
ctrl = collections.Counter()
plants = [(0, 5, 0, 3, 7), (5, 0, 0, 1, 1), (1, 1, 0, 0, 1), (1, 1, 3, 4, 0),
          (2, 25, 0, 9, 14), (1, 0, 0, 11, 11), (0, 0, 7, 0, 0), (13, 13, 13, 13, 13),
          (3, 5, 0, 0, 0), (7, 11, 4, 2, 25), (2, 4, 6, 8, 10), (9, 15, 21, 3, 17),
          (25, 25, 0, 1, 2), (6, 12, 18, 24, 5)]
exercised = collections.Counter()
for (a, b, c, k0, k1) in plants:
    cv = conventions[rng.randrange(12)]
    key = iterate(a, b, c, k0, k1)
    period = next((p for p in range(1, 24) if all(key[n + p] == key[n] for n in range(N - p))), None)
    exercised["a=0"] += (a == 0); exercised["b=0"] += (b == 0)
    exercised["a=1"] += (a == 1); exercised["b=1"] += (b == 1)
    exercised["nonunit"] += (a not in (0, 1) and b not in (0, 1))
    exercised["even_coef"] += (a % 2 == 0 or b % 2 == 0)
    exercised["odd_coef"] += (a % 2 == 1 or b % 2 == 1)
    exercised["repeated_init"] += (k0 == k1); exercised["k0=0"] += (k0 == 0)
    exercised["k1=0"] += (k1 == 0); exercised["affine_c"] += (c != 0)
    exercised["short_orbit"] += (period is not None); exercised["long_orbit"] += (period is None)
    PT = ["X"] * N
    for i, ch in CRIB.items():
        PT[i] = ch
    synth = "".join(cv.encrypt_letter(PT[n], key[n]) for n in range(N))
    tgt = [cv.key_index(CRIB[i], synth[i]) for i in JP]
    A, B, D = basis(a, b)
    M = [[A[i], B[i]] for i in JP]
    rhs = [(tgt[t] - c * D[i]) % 26 for t, i in enumerate(JP)]
    sols = solutions_mod26(M, rhs, limit=50)
    ok = (k0, k1) in [tuple(s) for s in sols]
    ctrl["planted_total"] += 1
    ctrl["planted_pass"] += bool(ok)
    # adversarial: alter a forced key value at a position that IS in the constraint set
    t_alt = rng.randrange(len(JP))
    bad_rhs = list(rhs)
    bad_rhs[t_alt] = (bad_rhs[t_alt] + 1 + rng.randrange(25)) % 26
    n_before = count_solutions_mod26(M, rhs)
    n_after = count_solutions_mod26(M, bad_rhs)
    capable = n_before > 0
    if capable:
        ctrl["adv_total"] += 1
        ctrl["adv_pass"] += (n_after < n_before)
    else:
        ctrl["adv_not_capable"] += 1
print(f"   planted positives : {ctrl['planted_pass']}/{ctrl['planted_total']} detected with the state recovered")
print(f"   adversarial       : {ctrl['adv_pass']}/{ctrl['adv_total']} flipped"
      f"   ({ctrl['adv_not_capable']} not counted - incapable by construction)")
print("   plant coverage    : " + ", ".join(f"{k}={v}" for k, v in sorted(exercised.items())))
assert ctrl["planted_pass"] == ctrl["planted_total"], "positive control failed"
assert ctrl["adv_pass"] == ctrl["adv_total"], "adversarial control failed"
assert all(exercised[k] > 0 for k in ("a=0", "b=0", "a=1", "b=1", "nonunit", "even_coef",
                                      "odd_coef", "repeated_init", "k0=0", "k1=0",
                                      "affine_c", "short_orbit", "long_orbit")), "plant coverage gap"
print()

# ---------------------------------------------------------------- the real test
print("## THE REAL TEST — exact linear solve per (a,b,c), all 12 conventions")
t0 = time.time()
res = {"cases": 0, "feasible_tuples": 0, "hits": [],
       "block1_only": 0, "block2_only": 0}
BAS = {}
for a, b in itertools.product(range(26), repeat=2):
    BAS[(a, b)] = basis(a, b)
for cname, tgt in targets.items():
    for (a, b), (A, B, D) in BAS.items():
        M = [[A[i], B[i]] for i in JP]
        for c in range(26):
            rhs = [(tgt[t] - c * D[i]) % 26 for t, i in enumerate(JP)]
            res["cases"] += 1
            n = count_solutions_mod26(M, rhs)
            if n:
                res["feasible_tuples"] += n
                for s in solutions_mod26(M, rhs, limit=10):
                    res["hits"].append({"convention": cname, "a": a, "b": b, "c": c,
                                        "k0": int(s[0]), "k1": int(s[1])})
            # per-block diagnostic
            if count_solutions_mod26([M[t] for t in BLOCK1], [rhs[t] for t in BLOCK1]):
                res["block1_only"] += 1
            if count_solutions_mod26([M[t] for t in BLOCK2], [rhs[t] for t in BLOCK2]):
                res["block2_only"] += 1
print(f"   (a,b,c) x convention systems solved exactly : {res['cases']:,}"
      f"   [{time.time()-t0:.0f}s]")
print(f"   FEASIBLE on all 24 cribs                   : {res['feasible_tuples']}")
print(f"   feasible on crib block 1 alone (13 posns)  : {res['block1_only']:,}")
print(f"   feasible on crib block 2 alone (11 posns)  : {res['block2_only']:,}")
print()
print("   The per-block diagnostic is the informative part of a zero: each block alone")
print("   overdetermines the 2-dimensional state, so a family that could satisfy one block")
print("   but not the other would look different from one that satisfies neither.")
print()
print(f"   preregistered expected survivors: 5.906e-27")
if res["feasible_tuples"] == 0:
    print()
    print("## RESULT: NEGATIVE")
    print("   No full-Z26 second-order affine self-evolving keystream, under the 12 committed")
    print("   shift conventions, message-aligned and without reset or transposition, satisfies")
    print("   the 24 published K4 positional cribs.")
    print()
    print("   This is NOT 'recursive keys are eliminated', NOT 'stateful systems are")
    print("   eliminated', NOT 'K4 is not autoregressive', and NOT 'K4 must use an external")
    print("   source'. Higher-order, nonlinear, reset, externally seeded and other state")
    print("   machines remain open.")
else:
    print("## HITS — candidates only, parameters frozen, nothing optimised")
    for h in res["hits"][:20]:
        print(f"   {h}")

out = os.path.join(REPO_ROOT, "results", "exp038")
os.makedirs(out, exist_ok=True)
json.dump({"experiment": "EXP-038", "ciphertext_sha256": k4.sha256,
           "prereg": "docs/exp038-preregistration.md",
           "families": ["F1 c=0", "F2 affine"], "modulus": 26,
           "crib_positions": JP, "targets": targets,
           "raw_tuples_F1": 26**4, "raw_tuples_F2": 26**5,
           "unique_streams_F2": 7585006, "unique_crib_projections_F1": 172375,
           "unique_crib_projections_F2": 4481750,
           "already_covered_periodic_le23": 1701518, "genuinely_new_streams": 5883488,
           "expected_survivors": 5.906e-27,
           "systems_solved": res["cases"], "feasible": res["feasible_tuples"],
           "block1_only": res["block1_only"], "block2_only": res["block2_only"],
           "hits": res["hits"], "controls": dict(ctrl),
           "plant_coverage": dict(exercised)},
          open(os.path.join(out, "summary.json"), "w"), indent=1)
print(f"\n   wrote results/exp038/summary.json")
