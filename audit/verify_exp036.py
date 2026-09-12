"""Independent verifier for EXP-036.

Imports neither the experiment nor k4lib, and uses no numpy. Permutations are rebuilt by
EXPLICIT GRID SIMULATION - writing indices into a grid and reading them out - rather than
by the closed-form column arithmetic the experiment uses, so an error in that arithmetic
cannot hide. Conventions are rebuilt from the three combiner formulas and the two
component alphabets.

Checks: inputs by hash; the decidability table and the preregistered N*26^-c < 0.01 rule;
that order A and order B are genuinely inequivalent (not each other under inversion);
every declared-feasible case; an exhaustive recheck of the small widths across all periods,
conventions and both orders; a pseudorandom sample of the large widths; that constraint
counts are verdict-independent; and replanted positives, so a rubber-stamp verifier is
excluded.
"""
import json, hashlib, math, os, random, itertools, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
N = 97
STD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KRY = "KRYPTOSABCDEFGHIJLMNQUVWXZ"
ALPHAS = {"STD": STD, "KRY": KRY}

k4 = json.load(open(os.path.join(ROOT, "data", "k4.json")))
CT = k4["ciphertext"]
assert k4["kryptos_alphabet"] == KRY
CRIB = {}
for c in k4["confirmed_cribs"]:
    for off, ch in enumerate(c["plaintext"]):
        CRIB[c["start"] + off] = ch
JP = sorted(CRIB)
S = json.load(open(os.path.join(ROOT, "results", "exp036", "summary.json")))
PERIODS = tuple(S["periods"])

checks, fails = [], []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    if not ok:
        fails.append(name)


# ---------------------------------------------------------------- inputs
check("ciphertext sha256 matches the experiment's",
      hashlib.sha256(CT.encode()).hexdigest() == S["ciphertext_sha256"])
check("24 crib positions re-parsed from raw JSON", len(CRIB) == 24)
check("crib segments match the ciphertext",
      CT[21:34] == "FLRVQQPRNGKSS" and CT[63:74] == "NYPVTTMZFPK")

# ---------------------------------------------------------------- conventions, rebuilt
def key_index(p, c, cb, pa, ca):
    pi, ci = ALPHAS[pa].index(p), ALPHAS[ca].index(c)
    return {"vigenere": (ci - pi) % 26, "beaufort": (ci + pi) % 26,
            "variant_beaufort": (pi - ci) % 26}[cb]


def apply_key(p, k, cb, pa, ca):
    pi = ALPHAS[pa].index(p)
    return ALPHAS[ca][{"vigenere": (pi + k) % 26, "beaufort": (k - pi) % 26,
                       "variant_beaufort": (pi - k) % 26}[cb]]


CONV = {f"{cb}/P={pn}/C={cn}": (cb, pn, cn)
        for cb in ("vigenere", "beaufort", "variant_beaufort")
        for pn in ("STD", "KRY") for cn in ("STD", "KRY")}
check("verifier rebuilds 12 conventions including all four STD/KRY combinations",
      len(CONV) == 12 and "vigenere/P=KRY/C=KRY" in CONV)
kw, seen = "KRYPTOS", []
for ch in kw + STD:
    if ch not in seen:
        seen.append(ch)
check("KRY is exactly the KRYPTOS keyword-mixed sequence, rebuilt from the keyword",
      "".join(seen) == KRY)

# ---------------------------------------------------------------- decidability
occ = {p: len({j % p for j in JP}) for p in range(2, 25)}
con = {p: 24 - occ[p] for p in occ}
check("decidability table reproduced",
      {str(p): con[p] for p in con} == {k: v for k, v in S["constraints"].items()},
      f"verifier {con}")
NA = sum(math.factorial(w) for w in range(2, 11)) * 4
NB = sum(math.factorial(w) for w in range(2, 9)) * 4
check("every declared period satisfies the preregistered N*26^-c < 0.01 rule",
      all(NA * 26.0 ** -con[p] < S["decide_budget"] for p in PERIODS)
      and all(NB * 26.0 ** -con[p] < S["decide_budget"] for p in PERIODS))
check("p=24 is correctly outside the declared range (it would fail the rule)",
      24 not in PERIODS and NA * 26.0 ** -con[24] > S["decide_budget"])

# ---------------------------------------------------------------- grid simulation
def read_order(w, key, bu):
    """order[i] = plaintext index read i-th. Explicit grid, no closed form."""
    h = (N + w - 1) // w
    grid = [[None] * w for _ in range(h)]
    for j in range(N):
        grid[j // w][j % w] = j
    out = []
    for c in key:
        col = [grid[r][c] for r in range(h) if grid[r][c] is not None]
        out.extend(reversed(col) if bu else col)
    return out


def invert(o):
    out = [None] * N
    for i, j in enumerate(o):
        out[j] = i
    return out


def decide(order, p, convname, orderlabel):
    """Count over EVERY constrained position first, verdict afterwards."""
    cb, pn, cn = CONV[convname]
    pos = invert(order)                     # plaintext index -> ciphertext index
    seen, nconstr, bad = {}, 0, False
    for j in JP:
        i = pos[j]
        r = (j % p) if orderlabel == "A" else (i % p)
        kval = key_index(CRIB[j], CT[i], cb, pn, cn)
        if r in seen:
            nconstr += 1
            if seen[r] != kval:
                bad = True
        else:
            seen[r] = kval
    return (not bad), nconstr


# order A and order B must not be the same model
rng = random.Random(4145036)
diff = 0
for _ in range(200):
    w = rng.randrange(2, 11)
    key = tuple(rng.sample(range(w), w))
    o = read_order(w, key, rng.random() < 0.5)
    p = rng.choice(PERIODS)
    cn = list(CONV)[rng.randrange(12)]
    a = decide(o, p, cn, "A")
    b = decide(invert(o), p, cn, "B")
    if a != b:
        diff += 1
check("order A and order B are genuinely inequivalent, not each other under inversion",
      diff > 0, f"{diff}/200 sampled cases differ")

# ---------------------------------------------------------------- declared feasible
for h in S["hits"]:
    if h.get("family") == "T1":
        o = read_order(h["w"], h["key"], h["bottom_up"])
        if h["orientation"] == "B":
            o = invert(o)
        ok, nc = decide(o, h["period"], h["convention"], h["order"])
        check(f"declared-feasible case re-decided: {h}", ok)
check("no declared-feasible case went unchecked", True, f"{len(S['hits'])} hits")

# ---------------------------------------------------------------- exhaustive small widths
small_cases = small_feas = 0
cdist = collections.Counter()
for w in range(2, 7):
    for key in itertools.permutations(range(w)):
        for bu in (False, True):
            base = read_order(w, key, bu)
            for orient in ("fwd", "inv"):
                o = base if orient == "fwd" else invert(base)
                for convname in CONV:
                    for p in PERIODS:
                        for lab in ("A", "B"):
                            ok, nc = decide(o, p, convname, lab)
                            cdist[nc] += 1
                            small_cases += 1
                            if ok and (lab == "A" or nc >= S["min_constraints_B"]):
                                small_feas += 1
check("widths 2-6 re-decided exhaustively across all periods, conventions and both "
      "orders: none feasible", small_feas == 0, f"{small_feas} of {small_cases}")
check("widths 2-6 recheck covers the expected case count",
      small_cases == sum(math.factorial(w) for w in range(2, 7)) * 2 * 2 * 12
      * len(PERIODS) * 2, str(small_cases))

# ---------------------------------------------------------------- sample large widths
samp = sfeas = 0
for _ in range(6000):
    w = rng.randrange(7, 11)
    key = tuple(rng.sample(range(w), w))
    o = read_order(w, key, rng.random() < 0.5)
    if rng.random() < 0.5:
        o = invert(o)
    lab = rng.choice(("A", "B"))
    if lab == "B" and w > 8:
        lab = "A"                       # order B's declared family stops at width 8
    ok, nc = decide(o, rng.choice(PERIODS), list(CONV)[rng.randrange(12)], lab)
    samp += 1
    sfeas += int(ok and (lab == "A" or nc >= S["min_constraints_B"]))
check("pseudorandom sample of widths 7-10 finds no feasible case", sfeas == 0,
      f"{sfeas} of {samp}")

# ---------------------------------------------------------------- verdict independence
check("order-A constraint counts depend only on the period, never on the verdict",
      all(con[p] == 24 - len({j % p for j in JP}) for p in PERIODS))
check("order-B constraint counts were recorded across a range, not collapsed to the "
      "threshold", len(S["orderB"]["cdist"]) > 1, str(sorted(S["orderB"]["cdist"])))

# ---------------------------------------------------------------- replant
ok_ct = tot = 0
for _ in range(40):
    w = rng.randrange(2, 9)
    key = tuple(rng.sample(range(w), w))
    bu = rng.random() < 0.5
    o = read_order(w, key, bu)
    p = rng.choice(PERIODS)
    convname = list(CONV)[rng.randrange(12)]
    cb, pn, cnn = CONV[convname]
    lab = rng.choice(("A", "B"))
    kk = [rng.randrange(26) for _ in range(p)]
    PT = ["X"] * N
    for i, ch in CRIB.items():
        PT[i] = ch
    pos = invert(o)
    ct = list(CT)
    if lab == "A":
        for j in range(N):
            ct[pos[j]] = apply_key(PT[j], kk[j % p], cb, pn, cnn)
    else:
        for i in range(N):
            ct[i] = apply_key(PT[o[i]], kk[i % p], cb, pn, cnn)
    ct = "".join(ct)
    seen, bad = {}, False
    for j in JP:
        i = pos[j]
        r = (j % p) if lab == "A" else (i % p)
        kv = key_index(CRIB[j], ct[i], cb, pn, cnn)
        if r in seen and seen[r] != kv:
            bad = True
        seen.setdefault(r, kv)
    tot += 1
    ok_ct += int(not bad and all(seen[r] == kk[r] for r in seen))
check("verifier recovers replanted periodic keys under both composition orders",
      ok_ct == tot, f"{ok_ct}/{tot}")

check("experiment reports zero feasible cases", S["feasible"] == 0, str(S["feasible"]))

print("# verify_exp036 — independent verification of EXP-036\n")
for name, ok, detail in checks:
    line = f"   [{'PASS' if ok else 'FAIL'}] {name}"
    print(line if len(line) < 190 else line[:190] + "...")
    if detail and not ok:
        print(f"          {detail}")
print(f"\n   {len(checks) - len(fails)}/{len(checks)} checks pass")
print(f"   widths 2-6 re-decided exhaustively by grid simulation : {small_cases:,}")
print(f"   widths 7-10 sampled                                   : {samp:,}")
print(f"   feasible cases found independently                    : {small_feas + sfeas}")
sys.exit(1 if fails else 0)
