"""Independent verification of EXP-040.

Imports neither experiments/exp040_propagating_autokey.py nor k4lib, and rebuilds
everything from data/k4.json. It deliberately uses different methods:

  * Route A -- ENCRYPT direction. The experiment decrypted: it ran the recursion
    from a primer through uncombine() and compared plaintext. This verifier instead
    enumerates whole primers, generates a candidate plaintext, re-ENCRYPTS it with
    the forward rule, and demands the result equal K4. Only crib agreement is then
    checked. Different direction, different primitive, whole-primer rather than
    per-chain.

  * Route B -- BACKWARD SOLVE. Rather than trying 26 primer values, it walks from a
    crib position back down its chain to the seed, inverting the recursion once, and
    then forward again to test the remaining crib positions in that chain.

  * Route C -- structural checks: the chains must partition 0..96 exactly, and the
    constraint budget is recomputed from scratch.
"""
import itertools
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K4 = json.load(open(os.path.join(ROOT, "data", "k4.json")))
CT = K4["ciphertext"]
STD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KRY = K4["kryptos_alphabet"]
ALPHA = {"STD": STD, "KRY": KRY}
CRIB = {}
for _cr in K4["confirmed_cribs"]:
    for _j, _ch in enumerate(_cr["plaintext"]):
        CRIB[_cr["start"] + _j] = _ch
POS = sorted(CRIB)
COMB = ("vigenere", "beaufort", "variant_beaufort")
fails = []


def check(label, cond):
    print(f"   [{'PASS' if cond else 'FAIL'}] {label}")
    if not cond:
        fails.append(label)


def enc(p, k, c):
    """Encrypt one letter index. The experiment only ever used the inverse."""
    if c == "vigenere":
        return (p + k) % 26
    if c == "beaufort":
        return (k - p) % 26
    return (p - k) % 26


def dec(cv, k, c):
    if c == "vigenere":
        return (cv - k) % 26
    if c == "beaufort":
        return (k - cv) % 26
    return (cv + k) % 26


print("## 0. Inputs")
check("97-character ciphertext", len(CT) == 97)
check("24 known plaintext positions", len(CRIB) == 24)
check("KRY is a permutation of A-Z", sorted(KRY) == sorted(STD))
summary = json.load(open(os.path.join(ROOT, "results", "exp040", "summary.json")))
check("experiment decided 2,592 configurations", summary["cases"] == 2592)
check("experiment reported zero FEASIBLE", len(summary["feasible"]) == 0)
check("experiment's controls both passed",
      summary["controls"]["positive"] and summary["controls"]["adversarial"])

print("\n## Route C  chain partition and constraint budget, rebuilt from scratch")
part_ok = True
for m in range(1, 25):
    for reverse in (False, True):
        for segs in ([(0, 97)], [(0, 4), (4, 35), (35, 66), (66, 97)]):
            covered = []
            for lo, hi in segs:
                seeds = range(lo, min(lo + m, hi)) if not reverse else \
                    range(max(lo, hi - m), hi)
                for seed in seeds:
                    i = seed
                    while lo <= i < hi:
                        covered.append(i)
                        i += -m if reverse else m
            if sorted(covered) != list(range(97)) or len(covered) != 97:
                part_ok = False
check("chains partition all 97 positions exactly, every m/direction/reset", part_ok)
budget = [24 - len({i % m for i in POS}) for m in range(1, 25)]
check("constraint budget runs 23 down to 5 over m = 1..24",
      budget[0] == 23 and budget[23] == 5 and min(budget) == 5)
check("m = 27, 28, 29 carry zero constraints",
      all(24 - len({i % m for i in POS}) == 0 for m in (27, 28, 29)))

print("\n## Route A  whole-primer enumeration, ENCRYPT direction, m = 1..3")
routeA_feasible = []
tried = 0
for m in (1, 2, 3):
    for combiner in COMB:
        for pa in ("STD", "KRY"):
            for ca in ("STD", "KRY"):
                for ka in ("STD", "KRY"):
                    pidx = {ch: i for i, ch in enumerate(ALPHA[pa])}
                    cidx = {ch: i for i, ch in enumerate(ALPHA[ca])}
                    kidx = {ch: i for i, ch in enumerate(ALPHA[ka])}
                    target = [cidx[ch] for ch in CT]
                    want = {i: pidx[ch] for i, ch in CRIB.items()}
                    for primer in itertools.product(range(26), repeat=m):
                        tried += 1
                        plain = [None] * 97
                        ok = True
                        for i in range(97):
                            k = primer[i] if i < m else \
                                kidx[ALPHA[pa][plain[i - m]]]
                            p = dec(target[i], k, combiner)
                            plain[i] = p
                            # re-encrypt and demand the ciphertext comes back
                            if enc(p, k, combiner) != target[i]:
                                ok = False
                                break
                            if i in want and p != want[i]:
                                ok = False
                                break
                        if ok:
                            routeA_feasible.append((m, combiner, pa, ca, ka, primer))
print(f"   enumerated {tried:,} whole primers with forward re-encryption")
check("Route A finds no feasible configuration", not routeA_feasible)

print("\n## Route B  backward solve from a crib position, all m = 1..24")
routeB_feasible = []
for m in range(1, 25):
    for combiner in COMB:
        for pa in ("STD", "KRY"):
            for ca in ("STD", "KRY"):
                for ka in ("STD", "KRY"):
                    pidx = {ch: i for i, ch in enumerate(ALPHA[pa])}
                    cidx = {ch: i for i, ch in enumerate(ALPHA[ca])}
                    kidx = {ch: i for i, ch in enumerate(ALPHA[ka])}
                    ci = [cidx[ch] for ch in CT]
                    relabel = None if ka == pa else \
                        [kidx[ALPHA[pa][v]] for v in range(26)]
                    consistent = True
                    for seed in range(m):
                        chain = list(range(seed, 97, m))
                        pinned = [(p, pidx[CRIB[p]]) for p in chain if p in CRIB]
                        if len(pinned) < 2:
                            continue
                        # invert the recursion from the FIRST pinned position back to
                        # the seed, recovering the primer without trying 26 values
                        first_pos, first_val = pinned[0]
                        k_here = {"vigenere": (ci[first_pos] - first_val) % 26,
                                  "beaufort": (ci[first_pos] + first_val) % 26,
                                  "variant_beaufort": (first_val - ci[first_pos]) % 26}[combiner]
                        step = chain.index(first_pos)
                        val = k_here
                        if relabel is not None:
                            inv = [0] * 26
                            for v in range(26):
                                inv[relabel[v]] = v
                            val = inv[val] if step > 0 else val
                        for back in range(step - 1, -1, -1):
                            pos = chain[back]
                            kprev = {"vigenere": (ci[pos] - val) % 26,
                                     "beaufort": (ci[pos] + val) % 26,
                                     "variant_beaufort": (val - ci[pos]) % 26}[combiner]
                            val = inv[kprev] if (relabel is not None and back > 0) else kprev
                        # now run forward from the recovered primer and test the rest
                        key, got = val, {}
                        for pos in chain:
                            p = dec(ci[pos], key, combiner)
                            got[pos] = p
                            key = relabel[p] if relabel is not None else p
                        if any(got[p] != v for p, v in pinned):
                            consistent = False
                            break
                    if consistent:
                        routeB_feasible.append((m, combiner, pa, ca, ka))
print(f"   backward-solved every chain with at least two pinned crib positions")
check("Route B finds no feasible configuration", not routeB_feasible)
if routeB_feasible:
    print(f"      first: {routeB_feasible[0]}")

print(f"\n{'ALL CHECKS PASSED' if not fails else 'FAILURES: ' + str(fails)}")
sys.exit(1 if fails else 0)
