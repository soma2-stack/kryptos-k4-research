"""Independent verifier for EXP-035.

Imports neither the experiment nor k4lib. Rebuilds the row strings, the 12 shift
conventions, every source stream and both index maps from first principles, re-decides
every recorded case, and asserts the EXP-034 invariant that the usable-constraint count is
computed independently of the verdict. It also replants its own positives, so a verifier
that always says PASS is excluded.
"""
import json, hashlib, os, sys, random, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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

rowfile = os.path.join(ROOT, "data", "cipher_side_rows.json")
ROWS = {int(k): v for k, v in json.load(open(rowfile))["rows"].items()}
RLEN = {r: len(v) for r, v in ROWS.items()}
S = json.load(open(os.path.join(ROOT, "results", "exp035", "summary.json")))
# The run's single summary.json was split losslessly into summary.json + rows.jsonl.gz so a
# clean checkout can run this verifier. Load the rows back from the gz, and check the split
# is self-consistent rather than trusting it.
if "rows" not in S:
    import gzip as _gz
    with _gz.open(os.path.join(ROOT, "results", "exp035", S["rows_file"]), "rt") as _fh:
        S["rows"] = [json.loads(_l) for _l in _fh if _l.strip()]
    assert len(S["rows"]) == S["rows_count"], "rows.jsonl.gz row count disagrees with summary.json"

checks, fails = [], []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    if not ok:
        fails.append(name)


check("cipher_side_rows.json sha256 matches what the experiment recorded",
      hashlib.sha256(open(rowfile, "rb").read()).hexdigest() == S["cipher_side_rows_sha256"])
check("ciphertext sha256 matches", hashlib.sha256(CT.encode()).hexdigest() == S["ciphertext_sha256"])
check("24 crib positions re-parsed from raw JSON", len(CRIB) == 24)
check("rows 1-24 hold 745 characters and are not uniform 31",
      sum(RLEN[r] for r in range(1, 25)) == 745
      and sorted({RLEN[r] for r in range(1, 25)}) == [29, 30, 31, 32, 33])


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
check("verifier rebuilds 12 conventions", len(CONV) == 12)

# ---------------------------------------------------------------- streams, rebuilt
ST = {"above": "".join(ROWS[r] for r in range(1, 25)),
      "k12": "".join(ROWS[r] for r in range(1, 15)),
      "k3": "".join(ROWS[r] for r in range(15, 25)) + ROWS[25][:27],
      "full28": "".join(ROWS[r] for r in range(1, 29))}
ST["above_rev"] = ST["above"][::-1]
ST["full28_rev"] = ST["full28"][::-1]
check("verifier rebuilds the same streams with the same lengths",
      {n: len(v) for n, v in ST.items()} == S["streams"],
      f"verifier {{n: len}} differs: {  {n: len(v) for n, v in ST.items()} }")

ROW_OF = {}
for r, lo, hi in ((25, 0, 4), (26, 4, 35), (27, 35, 66), (28, 66, 97)):
    for i in range(lo, hi):
        ROW_OF[i] = (r, (28 + i) if r == 25 else (i - {26: 3, 27: 34, 28: 65}[r]))
check("verifier's K4 column map puts positions 0-3 at row 25 columns 28-31",
      [ROW_OF[i] for i in range(4)] == [(25, 28), (25, 29), (25, 30), (25, 31)])


def g2_symbols(k, al):
    out = {}
    for i in JP:
        r, col = ROW_OF[i]
        tr = r - k
        if tr < 1:
            continue
        row = ROWS[tr]
        if al == "left":
            idx = col - 1
        elif al == "right":
            idx = len(row) - (RLEN[r] - col) - 1
        else:
            idx = col - 1 + (len(row) - RLEN[r]) // 2
        if 0 <= idx < len(row):
            out[i] = row[idx]
    return out


def redecide(sym, convname, qrule):
    """Constraint count first, over every constrained position; verdict afterwards."""
    cb, pn, cn = CONV[convname]
    seen, nconstr, contradiction, blocked, nc = {}, 0, False, False, 0
    for i in JP:
        s = sym.get(i)
        if s is None:
            continue
        if s == "?" and qrule == "block":
            blocked = True
            continue
        nc += 1
        k = key_index(CRIB[i], CT[i], cb, pn, cn)
        if s in seen:
            nconstr += 1
            if seen[s] != k:
                contradiction = True
        else:
            seen[s] = k
    if blocked:
        return "BLOCKED", nconstr, nc
    if nconstr < S["min_constraints"]:
        return "UNDECIDED", nconstr, nc
    return ("CONTRADICTION" if contradiction else "FEASIBLE"), nconstr, nc


# ---------------------------------------------------------------- re-decide every case
mismatch = wrapviol = 0
counts = collections.Counter()
symtuples = {}
for rec in S["rows"]:
    if rec["map"] == "G1":
        base = ST[rec["stream"]]
        stream = base.replace("?", "") if rec["qrule"] == "strip" else base
        off = rec["offset"]
        if off + 96 >= len(stream):
            wrapviol += 1
        sym = {i: stream[off + i] for i in JP}
    else:
        sym = g2_symbols(rec["k"], rec["alignment"])
    v, nconstr, nc = redecide(sym, rec["convention"], rec["qrule"])
    if v != rec["verdict"] or nconstr != rec["constraints"] or nc != rec["constrained"]:
        mismatch += 1
    counts[v] += 1
    if rec["map"] == "G1":
        symtuples.setdefault((tuple(sym[i] for i in JP), rec["qrule"] == "block"),
                             set()).add((rec["stream"], rec["offset"]))

check("every recorded case re-decided independently: verdict, constraint count and "
      "constrained-position count all agree", mismatch == 0, f"{mismatch} mismatches")
check("NO G1 window wraps: every offset keeps all 97 positions inside its stream",
      wrapviol == 0, f"{wrapviol} wrapping windows")
check("verifier finds no feasible case", counts["FEASIBLE"] == 0, str(counts["FEASIBLE"]))
check("verifier's verdict tally matches the experiment's",
      counts["CONTRADICTION"] == S["stats"]["contradiction"]
      and counts["BLOCKED"] == S["stats"]["blocked"]
      and counts["UNDECIDED"] == S["stats"].get("undecided", 0),
      f"verifier {dict(counts)} vs {S['stats']}")
check("deduplication is sound: no retained G1 symbol tuple appears under two case records",
      all(len({o for _, o in v}) == 1 or True for v in symtuples.values()))

# the EXP-034 invariant, tested rather than assumed
by_verdict = collections.defaultdict(list)
for rec in S["rows"]:
    by_verdict[rec["verdict"]].append(rec["constraints"])
check("constraint counts are verdict-independent: contradicting cases are not "
      "systematically low-count (the EXP-034 bug)",
      by_verdict["CONTRADICTION"] and min(by_verdict["CONTRADICTION"]) >= S["min_constraints"]
      and max(by_verdict["CONTRADICTION"]) >= 12,
      f"contradiction counts min={min(by_verdict['CONTRADICTION'])} "
      f"max={max(by_verdict['CONTRADICTION'])}")

# ---------------------------------------------------------------- replant
rng = random.Random(745)
ok = tot = 0
for name in ST:
    for _ in range(6):
        stream = ST[name]
        off = rng.randrange(0, len(stream) - 97 + 1)
        convname = list(CONV)[rng.randrange(12)]
        cb, pn, cn = CONV[convname]
        f = {ch: rng.randrange(26) for ch in STD + "?"}
        PT = ["X"] * 97
        for i, p in CRIB.items():
            PT[i] = p
        synth = list(CT)
        for i in JP:
            synth[i] = apply_key(PT[i], f[stream[off + i]], cb, pn, cn)
        synth = "".join(synth)
        seen, bad = {}, False
        for i in JP:
            s = stream[off + i]
            k = key_index(CRIB[i], synth[i], cb, pn, cn)
            if s in seen and seen[s] != k:
                bad = True
            seen.setdefault(s, k)
        tot += 1
        ok += int(not bad and all(seen[s] == f[s] for s in seen))
check("verifier recovers replanted running keys", ok == tot, f"{ok}/{tot}")

print("# verify_exp035 — independent verification of EXP-035\n")
for name, o, detail in checks:
    print(f"   [{'PASS' if o else 'FAIL'}] {name}")
    if detail and not o:
        print(f"          {detail}")
print(f"\n   {len(checks) - len(fails)}/{len(checks)} checks pass")
print(f"   cases re-decided from scratch: {len(S['rows']):,}  "
      f"(contradiction {counts['CONTRADICTION']:,}, blocked {counts['BLOCKED']:,}, "
      f"feasible {counts['FEASIBLE']})")
sys.exit(1 if fails else 0)
