"""Independent verifier for EXP-037.

Imports neither the experiment nor k4lib, and uses no numpy. The 13 Porta tables are built
here from the documented definition - NOT imported from the production generator - and
reciprocity is checked independently. Permutations are rebuilt by explicit grid simulation.
"""
import json, hashlib, math, os, random, itertools, sys, collections, gzip

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
N = 97
STD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KRY = "KRYPTOSABCDEFGHIJLMNQUVWXZ"
ORD = {"STD": STD, "KRY": KRY}

k4 = json.load(open(os.path.join(ROOT, "data", "k4.json")))
CT = k4["ciphertext"]
CRIB = {}
for c in k4["confirmed_cribs"]:
    for off, ch in enumerate(c["plaintext"]):
        CRIB[c["start"] + off] = ch
JP = sorted(CRIB)
S = json.load(open(os.path.join(ROOT, "results", "exp037", "summary.json")))
PERIODS = tuple(S["periods"])

checks, fails = [], []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    if not ok:
        fails.append(name)


# ---------------------------------------------------------------- tables, built here
def porta(order):
    """Independent construction from the documented rule; deliberately written
    differently from the experiment's (explicit half lists rather than index arithmetic)."""
    lower, upper = list(order[:13]), list(order[13:])
    rows = []
    for n in range(13):
        m = {}
        rot = upper[n:] + upper[:n]
        for a in range(13):
            m[lower[a]] = rot[a]
            m[rot[a]] = lower[a]
        rows.append(m)
    return rows


for name, order in ORD.items():
    rows = porta(order)
    check(f"{name}: 13 tables built", len(rows) == 13)
    check(f"{name}: every table is a permutation of all 26 letters",
          all(sorted(r.keys()) == sorted(STD) and sorted(r.values()) == sorted(STD)
              for r in rows))
    check(f"{name}: every table is self-reciprocal (checked independently)",
          all(all(r[r[ch]] == ch for ch in STD) for r in rows))
    check(f"{name}: every table has zero fixed points",
          all(not any(r[ch] == ch for ch in STD) for r in rows))
    check(f"{name}: every table sends every letter to the opposite half",
          all(all((order.index(ch) < 13) != (order.index(r[ch]) < 13) for ch in STD)
              for r in rows))
r = porta(STD)
check("textbook anchor: row 0 is A<->N ... M<->Z",
      r[0]["A"] == "N" and r[0]["M"] == "Z" and r[0]["N"] == "A")
check("textbook anchor: row 1 is A<->O ... L<->Z, M<->N",
      r[1]["A"] == "O" and r[1]["L"] == "Z" and r[1]["M"] == "N")

ROWOF = {}
for name, order in ORD.items():
    t = {}
    for n, rr in enumerate(porta(order)):
        for ch in STD:
            t[(ch, rr[ch])] = n
    ROWOF[name] = t
    check(f"{name}: exactly 338 of 676 letter pairs are realisable, each by ONE row",
          len(t) == 338, str(len(t)))

# ---------------------------------------------------------------- the direct elimination
for name, order in ORD.items():
    same = [(i, CRIB[i], CT[i]) for i in JP
            if (order.index(CRIB[i]) < 13) == (order.index(CT[i]) < 13)]
    unreal = [i for i in JP if (CRIB[i], CT[i]) not in ROWOF[name]]
    check(f"{name}: crib pairs sharing a half == pairs realisable by no row",
          sorted(i for i, _, _ in same) == sorted(unreal))
    check(f"{name}: {len(same)} crib pairs are unrealisable, so the DIRECT family dies at "
          f"every period", len(same) == 16 == S["direct"][name]["unrealisable_pairs"],
          f"verifier {len(same)} vs summary {S['direct'][name]['unrealisable_pairs']}")
    check(f"{name}: summary reports no feasible direct period",
          S["direct"][name]["feasible_periods"] == [])

# ---------------------------------------------------------------- null probability
for name, order in ORD.items():
    cnt = collections.Counter(0 if order.index(ch) < 13 else 1 for ch in CT)
    q = sum(cnt[1 - (0 if order.index(CRIB[i]) < 13 else 1)] / 97.0 for i in JP) / 24
    check(f"{name}: cross-half null re-derived from the ciphertext, not assumed "
          f"(P(all 24) ~ {q ** 24:.2e})", 1e-9 < q ** 24 < 1e-6)

# ---------------------------------------------------------------- permutations
def read_order(w, key, bu):
    h = (N + w - 1) // w
    grid = [[None] * w for _ in range(h)]
    for j in range(N):
        grid[j // w][j % w] = j
    out = []
    for c in key:
        col = [grid[rr][c] for rr in range(h) if grid[rr][c] is not None]
        out.extend(reversed(col) if bu else col)
    return out


def invert(o):
    out = [None] * N
    for i, j in enumerate(o):
        out[j] = i
    return out


def decide(order_seq, q, name, lab):
    pos = invert(order_seq)
    seen, nconstr, bad, unreal = {}, 0, False, 0
    for j in JP:
        i = pos[j]
        key = (CRIB[j], CT[i])
        rw = ROWOF[name].get(key, -1)
        if rw < 0:
            unreal += 1
        res = (j % q) if lab == "A" else (i % q)
        if res in seen:
            nconstr += 1
            if seen[res] != rw:
                bad = True
        else:
            seen[res] = rw
    return (unreal == 0 and not bad), nconstr, unreal


rng = random.Random(1563)
small_cases = small_feas = parity = 0
for w in range(2, 7):
    for key in itertools.permutations(range(w)):
        for bu in (False, True):
            base = read_order(w, key, bu)
            for orient in ("fwd", "inv"):
                o = base if orient == "fwd" else invert(base)
                for name in ORD:
                    ok0, _, unreal0 = decide(o, 2, name, "A")
                    if unreal0 == 0:
                        parity += 1
                    for q in PERIODS:
                        for lab in ("A", "B"):
                            ok, nc, unreal = decide(o, q, name, lab)
                            small_cases += 1
                            small_feas += int(ok)
check("widths 2-6 re-decided exhaustively across periods, orderings and both orders: "
      "none feasible", small_feas == 0, str(small_feas))
check("widths 2-6: no permutation even passes the cross-half filter", parity == 0, str(parity))

samp = sfeas = sparity = 0
for _ in range(8000):
    w = rng.randrange(7, 11)
    o = read_order(w, tuple(rng.sample(range(w), w)), rng.random() < 0.5)
    if rng.random() < 0.5:
        o = invert(o)
    name = rng.choice(list(ORD))
    ok, nc, unreal = decide(o, rng.choice(PERIODS), name, rng.choice(("A", "B")))
    samp += 1
    sfeas += int(ok)
    sparity += int(unreal == 0)
check("pseudorandom sample of widths 7-10 finds no feasible case", sfeas == 0, str(sfeas))
check("sampled permutations passing the cross-half filter is consistent with the null",
      sparity == 0, str(sparity))

# ---------------------------------------------------------------- replant, both directions
ok_ct = tot = 0
rows_used = set()
for t in range(60):
    name = rng.choice(list(ORD))
    tabs = porta(ORD[name])
    w = rng.randrange(2, 9)
    o = read_order(w, tuple(rng.sample(range(w), w)), rng.random() < 0.5)
    pos = invert(o)
    q = rng.choice([p for p in PERIODS if p >= 2])
    ks = [rng.randrange(13) for _ in range(q)]
    if t < 13:
        ks[0] = t % 13
    rows_used.update(ks)
    lab = rng.choice(("A", "B"))
    PT = ["X"] * N
    for i, ch in CRIB.items():
        PT[i] = ch
    ct = list(CT)
    if lab == "A":
        for j in range(N):
            ct[pos[j]] = tabs[ks[j % q]][PT[j]]
    else:
        for i in range(N):
            ct[i] = tabs[ks[i % q]][PT[o[i]]]
    ct = "".join(ct)
    seen, bad, unreal = {}, False, 0
    for j in JP:
        i = pos[j]
        rw = ROWOF[name].get((CRIB[j], ct[i]), -1)
        if rw < 0:
            unreal += 1
        res = (j % q) if lab == "A" else (i % q)
        if res in seen and seen[res] != rw:
            bad = True
        seen.setdefault(res, rw)
    tot += 1
    ok_ct += int(unreal == 0 and not bad and all(seen[rr] == ks[rr] for rr in seen))
check("verifier recovers replanted Porta row schedules under both composition orders",
      ok_ct == tot, f"{ok_ct}/{tot}")
check("replants exercised every Porta row", len(rows_used) == 13, str(len(rows_used)))

check("experiment reports zero feasible composed cases", S["feasible"] == 0)
check("experiment reports zero cross-half survivors",
      S["composed"]["parity_survivors"] == 0 and S["T2_T3"]["parity_survivors"] == 0)
check("constraint counts depend only on the period, never on the verdict",
      all(S["constraints"][str(q)] == 24 - len({j % q for j in JP}) for q in PERIODS))

print("# verify_exp037 — independent verification of EXP-037\n")
for name, ok, detail in checks:
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}")
    if detail and not ok:
        print(f"          {detail}")
print(f"\n   {len(checks) - len(fails)}/{len(checks)} checks pass")
print(f"   widths 2-6 re-decided exhaustively : {small_cases:,}")
print(f"   widths 7-10 sampled                : {samp:,}")
print(f"   feasible cases found independently : {small_feas + sfeas}")
sys.exit(1 if fails else 0)
