"""Independent verification of the two exact claims made at Checkpoint T.

Deliberately standalone: it does NOT import k4lib, and it re-derives the row
split, the crib pairs and the alphabets from the pinned JSON data files only.

T-A  Pure transposition of the K4 message is PROVED IMPOSSIBLE.
     A permutation preserves the letter multiset. The two verified cribs force
     the plaintext to contain at least three 'E's; the ciphertext contains two.

T-B  The verified crib set imposes ZERO equality constraints on any
     message-aligned periodic key of period 27, 28 or 29. Any "fit" reported at
     those periods is vacuous, not evidence.

Also re-derives, by a different route from EXP-020, the two row-local column
collisions (32 vs 63, 33 vs 64) and confirms all 12 conventions fail them.
"""
import json, os, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K4 = json.load(open(os.path.join(ROOT, "data", "k4.json")))
ROWS = json.load(open(os.path.join(ROOT, "data", "cipher_side_rows.json")))["rows"]
CT = K4["ciphertext"]
fails = []


def check(label, cond):
    print(f"   [{'PASS' if cond else 'FAIL'}] {label}")
    if not cond:
        fails.append(label)


print("## 0. Inputs")
check("ciphertext is 97 characters", len(CT) == 97)
# rebuild K4 from the authoritative sculpture rows rather than trusting a constant
rebuilt = ROWS["25"][-4:] + ROWS["26"] + ROWS["27"] + ROWS["28"]
check("K4 == row25[-4:] + rows 26,27,28", rebuilt == CT)
SEGMENTS = [(0, 4, 25), (4, 35, 26), (35, 66, 27), (66, 97, 28)]
check("row segment lengths are 4,31,31,31", [b - a for a, b, _ in SEGMENTS] == [4, 31, 31, 31])

PAIRS = []
for cr in K4["confirmed_cribs"]:
    s, pt = cr["start"], cr["plaintext"]
    check(f"crib {pt} matches ciphertext at {s}", CT[s:s + len(pt)] == cr["ciphertext_segment"])
    PAIRS += [(s + j, p, c) for j, (p, c) in enumerate(zip(pt, cr["ciphertext_segment"]))]
check("24 known plaintext/ciphertext pairs", len(PAIRS) == 24)
POS = [i for i, _, _ in PAIRS]

print("\n## T-A  pure transposition PROVED IMPOSSIBLE")
ct_counts = collections.Counter(CT)
pt_counts = collections.Counter(p for _, p, _ in PAIRS)
# counted by explicit iteration rather than Counter arithmetic, to stay independent
short = []
for letter in sorted(pt_counts):
    need = sum(1 for _, p, _ in PAIRS if p == letter)
    have = sum(1 for ch in CT if ch == letter)
    if need > have:
        short.append((letter, need, have))
print(f"   crib plaintext needs / ciphertext supplies: {short}")
check("at least one letter is oversubscribed", len(short) >= 1)
check("the violating letter is E, needing 3 against 2", short == [("E", 3, 2)])
print("   A permutation of the 97 K4 characters preserves the letter multiset exactly,")
print("   so a plaintext requiring three E's cannot be carried by a ciphertext holding two.")
print("   Scope: transposition of the K4 message alone, with no substitution layer.")

print("\n## T-B  periods 27, 28, 29 carry zero constraint power")
for n in range(2, 40):
    residues = set()
    for i in POS:
        residues.add(i % n)
    constraints = len(POS) - len(residues)
    if n in (27, 28, 29):
        check(f"period {n} imposes 0 equality constraints", constraints == 0)
    elif 24 <= n <= 26:
        print(f"   period {n}: only {constraints} constraint(s) — very weak")
check("period 26 imposes exactly 1 constraint", len(POS) - len({i % 26 for i in POS}) == 1)
check("period 30 imposes exactly 1 constraint", len(POS) - len({i % 30 for i in POS}) == 1)

print("\n## T-C  replication of the EXP-020 row-local column collisions")
local = {}
for i in POS:
    for a, b, r in SEGMENTS:
        if a <= i < b:
            local.setdefault(i - a, []).append(i)
coll = {l: v for l, v in local.items() if len(v) > 1}
print(f"   row-local indices shared by two crib positions: {coll}")
check("collisions are exactly {28: [32, 63], 29: [33, 64]}", coll == {28: [32, 63], 29: [33, 64]})

STD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KRY = K4["kryptos_alphabet"]
check("KRY is a permutation of the 26 letters", sorted(KRY) == sorted(STD))
ALPHA = {"STD": STD, "KRY": KRY}
matches = 0
for comb in ("vigenere", "beaufort", "variant_beaufort"):
    for pa in ("STD", "KRY"):
        for ca in ("STD", "KRY"):
            k = {}
            for i, p, c in PAIRS:
                pi = ALPHA[pa].index(p)
                ci = ALPHA[ca].index(c)
                k[i] = {"vigenere": (ci - pi) % 26,
                        "beaufort": (ci + pi) % 26,
                        "variant_beaufort": (pi - ci) % 26}[comb]
            if k[32] == k[63] and k[33] == k[64]:
                matches += 1
print(f"   conventions satisfying both collisions: {matches} of 12 "
      f"(null expectation 12 * 26**-2 = {12 / 676:.4f})")
check("no convention survives the row-local restart prediction", matches == 0)

print(f"\n{'ALL CHECKS PASSED' if not fails else 'FAILURES: ' + str(fails)}")
sys.exit(1 if fails else 0)
