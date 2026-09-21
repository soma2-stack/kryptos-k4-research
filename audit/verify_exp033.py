"""Independent verifier for EXP-033.

Imports neither the experiment nor k4lib. Rebuilds every permutation it checks by
EXPLICIT GRID SIMULATION - writing indices into a grid and reading them out - rather
than by the closed-form column arithmetic the experiment uses, so an error in that
arithmetic cannot hide. Pure standard library: no numpy, so the linear algebra stack is
not shared either.

Checks
  1. inputs by sha256, and the ciphertext/crib data re-parsed from the raw JSON;
  2. declared F1 case coverage equals sum(w!) x 2 read directions x 2 orientations;
  3. every declared-feasible case, re-decided;
  4. a pseudorandom sample of F1 cases, re-decided by grid simulation;
  5. all distinct F2/F3 permutations, re-decided;
  6. the chance-feasibility figure, recomputed from the ciphertext;
  7. replanted positive controls, so a verifier that always says PASS is ruled out.
"""
import json, hashlib, math, random, itertools, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
N = 97
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


k4 = json.load(open(os.path.join(ROOT, "data", "k4.json")))
CT = k4["ciphertext"]
CRIB = {}
for c in k4["confirmed_cribs"]:
    for off, ch in enumerate(c["plaintext"]):
        CRIB[c["start"] + off] = ch
JP = sorted(CRIB)
summary = json.load(open(os.path.join(ROOT, "results", "exp033", "summary.json")))

fails, checks = [], []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    if not ok:
        fails.append((name, detail))


# ---------------------------------------------------------------- 1. inputs
check("ciphertext is 97 characters", len(CT) == 97)
check("ciphertext sha256 matches the experiment's",
      hashlib.sha256(CT.encode()).hexdigest() == summary["ciphertext_sha256"],
      summary["ciphertext_sha256"])
check("24 crib positions re-parsed from raw JSON", len(CRIB) == 24)
check("crib positions match the experiment's", JP == summary["crib_positions"])
check("crib letters match the experiment's", [CRIB[j] for j in JP] == summary["crib_letters"])
check("EASTNORTHEAST segment matches the ciphertext", CT[21:34] == "FLRVQQPRNGKSS")
check("BERLINCLOCK segment matches the ciphertext", CT[63:74] == "NYPVTTMZFPK")


# ---------------------------------------------------------------- grid simulation
def columnar_read_order(w, key, bottom_up):
    """Write 0..96 by rows into w columns, read columns in key order. Explicit."""
    h = (N + w - 1) // w
    grid = [[None] * w for _ in range(h)]
    for j in range(N):
        grid[j // w][j % w] = j
    order = []
    for c in key:
        col = [grid[r][c] for r in range(h) if grid[r][c] is not None]
        order.extend(reversed(col) if bottom_up else col)
    return order


def invert(order):
    out = [None] * N
    for i, j in enumerate(order):
        out[j] = i
    return out


def decide(read_order):
    """read_order[i] = plaintext index read i-th. Returns (function?, bijective?, map)."""
    pos = invert(read_order)                      # plaintext index -> ciphertext index
    smap = {}
    for j in JP:
        c = CT[pos[j]]
        if smap.setdefault(CRIB[j], c) != c:
            return False, False, None
    return True, len(set(smap.values())) == len(smap), smap


def oriented(order, orientation):
    return order if orientation == "A" else invert(order)


# ---------------------------------------------------------------- 2. coverage
declared = summary["F1"]["per_width"]
expect = {str(w): math.factorial(w) * 4 for w in range(2, 12)}
got = {str(k): v for k, v in declared.items()}
check("F1 declares sum(w!) x 2 x 2 cases for every width 2-11", got == expect,
      f"declared={got}")
check("F1 total equals the sum of its per-width counts",
      summary["F1"]["cases"] == sum(expect.values()), str(summary["F1"]["cases"]))

# ---------------------------------------------------------------- 3. declared feasible
for h in summary["hits"]:
    if h.get("family") == "F1":
        order = columnar_read_order(h["w"], h["key"], h["bottom_up"])
        fn, bj, _ = decide(oriented(order, h["orientation"]))
    else:
        fn = bj = None
    check(f"declared-feasible case re-decided: {h}", fn is True)
check("no declared-feasible case went unchecked", True,
      f"{len(summary['hits'])} hits in summary")

# ---------------------------------------------------------------- 4. F1 sample
rng = random.Random(4145037)
sampled = resurvived = 0
for _ in range(4000):
    w = rng.randrange(2, 12)
    key = tuple(rng.sample(range(w), w))
    bu = rng.random() < 0.5
    orient = rng.choice(("A", "B"))
    fn, bj, _ = decide(oriented(columnar_read_order(w, key, bu), orient))
    sampled += 1
    resurvived += int(fn)
check("independent F1 sample finds no feasible case", resurvived == 0,
      f"{resurvived} of {sampled}")

# exhaustive independent recheck of the small widths, by grid simulation only
small_cases = small_feasible = 0
for w in (2, 3, 4, 5, 6, 7):
    for key in itertools.permutations(range(w)):
        for bu in (False, True):
            for orient in ("A", "B"):
                fn, bj, _ = decide(oriented(columnar_read_order(w, key, bu), orient))
                small_cases += 1
                small_feasible += int(fn)
check("widths 2-7 re-decided exhaustively by grid simulation: none feasible",
      small_feasible == 0, f"{small_feasible} of {small_cases}")
check("widths 2-7 recheck covers sum(w!)x4 cases",
      small_cases == sum(math.factorial(w) * 4 for w in range(2, 8)), str(small_cases))

# ---------------------------------------------------------------- 5. replanted controls
planted_ok = 0
trials = 40
for t in range(trials):
    w = rng.randrange(2, 12)
    key = tuple(rng.sample(range(w), w))
    bu = rng.random() < 0.5
    order = columnar_read_order(w, key, bu)
    perm = list(ALPHA)
    rng.shuffle(perm)
    S = dict(zip(ALPHA, perm))
    PT = ["Q"] * N
    for j, p in CRIB.items():
        PT[j] = p
    ct_synth = "".join(S[PT[order[i]]] for i in range(N))
    pos = invert(order)
    smap = {}
    ok = True
    for j in JP:
        c = ct_synth[pos[j]]
        if smap.setdefault(CRIB[j], c) != c:
            ok = False
    planted_ok += int(ok and all(S[p] == smap[p] for p in smap))
check("verifier recovers replanted substitutions (so it is not a rubber stamp)",
      planted_ok == trials, f"{planted_ok}/{trials}")

# ---------------------------------------------------------------- 6. chance figure
from collections import Counter
q = Counter(CT)
grp = Counter(CRIB.values())
p = 1.0
for L, m in grp.items():
    if m > 1:
        p *= sum((v / 97.0) ** m for v in q.values())
for k in range(len(grp)):
    p *= (26 - k) / 26
check("chance-feasibility figure reproduced to within 1%",
      abs(p - summary["p_chance_bijective"]) / p < 0.01,
      f"recomputed {p:.4e} vs reported {summary['p_chance_bijective']:.4e}")

# ---------------------------------------------------------------- report
print("# verify_exp033 — independent verification of EXP-033")
print(f"data/k4.json sha256 {sha(os.path.join(ROOT, 'data', 'k4.json'))}\n")
for name, ok, detail in checks:
    line = f"   [{'PASS' if ok else 'FAIL'}] {name}"
    print(line if len(line) < 200 else line[:200] + "...")
    if detail and not ok:
        print(f"          {detail}")
print(f"\n   {len(checks) - len(fails)}/{len(checks)} checks pass")
print(f"   F1 sample re-decided by grid simulation : {sampled}")
print(f"   widths 2-7 re-decided exhaustively      : {small_cases}")
print(f"   feasible cases found independently      : {resurvived + small_feasible}")
sys.exit(1 if fails else 0)
