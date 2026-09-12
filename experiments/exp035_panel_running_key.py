"""EXP-035  Running key from the authoritative cipher-side text above K4.

Preregistered in docs/exp035-preregistration.md before implementation.

Model:  k[i] = f(S[g(i)]),  C[i] = conv(P[i], k[i]),  f : Sigma -> Z26 ANY function.

f is never enumerated; every function is decided exactly by consistency, so key alphabet
is not a parameter. Index maps: G1 a linear offset with NO modulo wrapping (EXP-029's
audited defect was a promised-bounded window that wrapped), and G2 the same row-local
index k rows above, declared as a TEXT-order family and not a physical claim.

Invariant carried from EXP-034: the usable-constraint count is computed over every
constrained position BEFORE any verdict is formed. Cases with <= 3 constraints are
UNDECIDED and excluded from the elimination. Adversarial controls are only counted when
they are capable of changing the verdict.
"""
import sys, os, json, hashlib, collections, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load, REPO_ROOT
from k4lib.conventions import all_conventions

MIN_CONSTRAINTS = 4                       # preregistered

k4 = load()
CT = k4.ciphertext
CRIB = {i: p for i, p, _ in k4.crib_positions()}
JP = sorted(CRIB)
conventions = all_conventions()

rowfile = os.path.join(REPO_ROOT, "data", "cipher_side_rows.json")
rowdoc = json.load(open(rowfile))
ROWS = {int(k): v for k, v in rowdoc["rows"].items()}
ROWSHA = hashlib.sha256(open(rowfile, "rb").read()).hexdigest()

print("# EXP-035 running key from the authoritative cipher-side text")
print(f"ciphertext sha256      {k4.sha256}")
print(f"cipher_side_rows sha256 {ROWSHA}\n")

# ---------------------------------------------------------------- input verification
row_len = {r: len(ROWS[r]) for r in ROWS}
vchecks = [("28 rows present", sorted(ROWS) == list(range(1, 29))),
           ("rows 1-24 hold 745 characters", sum(row_len[r] for r in range(1, 25)) == 745),
           ("rows 25-28 hold 124 characters", sum(row_len[r] for r in range(25, 29)) == 124),
           ("rows 26-28 equal K4[4:35], K4[35:66], K4[66:97]",
            ROWS[26] == CT[4:35] and ROWS[27] == CT[35:66] and ROWS[28] == CT[66:97]),
           ("row 25 ends in OBKR", ROWS[25].endswith("OBKR")),
           ("rows 1-24 are NOT uniformly 31",
            sorted({row_len[r] for r in range(1, 25)}) == [29, 30, 31, 32, 33]),
           ("four question marks in total",
            sum(v.count("?") for v in ROWS.values()) == 4)]
print("## Input verification")
for n, ok in vchecks:
    print(f"   [{'PASS' if ok else 'FAIL'}] {n}")
assert all(ok for _, ok in vchecks)
print(f"   row-length distribution rows 1-24: "
      f"{dict(sorted(collections.Counter(row_len[r] for r in range(1, 25)).items()))}")
print()
print("## Why the physical same-column model is NOT here")
print("   With a monospaced punch and a common row width every row would hold the same")
print("   character count. Rows 1-24 hold 29-33, so either row width or letter pitch")
print("   varies by row; data/physical.json records at MEDIUM confidence that Sanborn")
print("   kerned the lettering and avoided fixed-width spacing. Between a 29- and a")
print("   33-character row the pitch differs by 13.8%, so character centres in different")
print("   rows would not sit above one another except by coincidence. The physical route")
print("   is PARKED (evidence Request 4), not tested with a manufactured lattice.")
print()

# ---------------------------------------------------------------- declared streams
def build_streams():
    out = {}
    out["above"] = "".join(ROWS[r] for r in range(1, 25))
    out["above_rev"] = out["above"][::-1]
    out["k12"] = "".join(ROWS[r] for r in range(1, 15))
    out["k3"] = "".join(ROWS[r] for r in range(15, 25)) + ROWS[25][:27]
    out["full28"] = "".join(ROWS[r] for r in range(1, 29))
    out["full28_rev"] = out["full28"][::-1]
    return out


STREAMS = build_streams()
print("## Declared source streams")
for n, s in STREAMS.items():
    print(f"   {n:<11} {len(s):>4} chars, {s.count('?')} question marks"
          + ("   [carries the unresolved 432-vs-435 letter discrepancy]" if n == "k12" else ""))
assert len(STREAMS["above"]) == 745 and len(STREAMS["full28"]) == 869
assert len(STREAMS["k3"]) == 337, len(STREAMS["k3"])
print()


def apply_qmark(s, rule):
    return s.replace("?", "") if rule == "strip" else s


# ---------------------------------------------------------------- the decision
def decide(symbols, conv, ct=CT, crib=None, qrule="retain"):
    """symbols: dict crib position -> source symbol (or None if unconstrained).

    Returns (verdict, usable_constraints, witness, forced map, n_constrained).
    The constraint count is computed over EVERY constrained position before a verdict is
    formed - the EXP-034 invariant. No early return.
    """
    crib = crib if crib is not None else CRIB
    seen, constraints, witness, nc = {}, 0, None, 0
    blocked = False
    for i in JP:
        s = symbols.get(i)
        if s is None:
            continue
        if s == "?" and qrule == "block":
            blocked = True
            continue
        nc += 1
        k = conv.key_index(crib[i], ct[i])
        if s in seen:
            constraints += 1
            if seen[s][0] != k and witness is None:
                witness = {"symbol": s, "positions": [seen[s][1], i],
                           "key_values": [seen[s][0], k]}
        else:
            seen[s] = (k, i)
    if blocked:
        return "BLOCKED", constraints, None, seen, nc
    return ("CONTRADICTION" if witness else "FEASIBLE"), constraints, witness, seen, nc


def g1_symbols(stream, offset):
    return {i: stream[offset + i] for i in JP}


ROW_OF = {}
for r, lo, hi in ((25, 0, 4), (26, 4, 35), (27, 35, 66), (28, 66, 97)):
    for i in range(lo, hi):
        ROW_OF[i] = (r, (28 + i) if r == 25 else (i - {26: 3, 27: 34, 28: 65}[r]))


def g2_symbols(k, convention):
    """TEXT-order only: same row-local index, k rows above. Not a physical claim."""
    out = {}
    for i in JP:
        r, col = ROW_OF[i]
        tr = r - k
        if tr < 1:
            continue
        row = ROWS[tr]
        if convention == "left":
            idx = col - 1
        elif convention == "right":
            idx = len(row) - (row_len[r] - col) - 1
        else:                                          # centred
            idx = col - 1 + (len(row) - row_len[r]) // 2
        if 0 <= idx < len(row):
            out[i] = row[idx]
    return out


# ---------------------------------------------------------------- controls
print("## Controls")
rng = random.Random(869)
ctrl = collections.Counter()
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def plant_and_check(symbols, conv, noninjective=False):
    f = {ch: rng.randrange(26) for ch in ALPHA + "?"}
    if noninjective:
        for ch in "AEIOU":
            f[ch] = 3
    PT = ["X"] * 97
    for i, p in CRIB.items():
        PT[i] = p
    synth = list(CT)
    for i in JP:
        if symbols.get(i) is not None:
            synth[i] = conv.encrypt_letter(PT[i], f[symbols[i]])
    synth = "".join(synth)
    v, c, _, forced, nc = decide(symbols, conv, ct=synth)
    ok = v == "FEASIBLE" and all(val[0] == f[s] for s, val in forced.items())
    # adversarial: only counted when it CAN change the verdict, i.e. some source symbol
    # occurs at two or more constrained positions
    buckets = collections.defaultdict(list)
    for i in JP:
        if symbols.get(i) is not None:
            buckets[symbols[i]].append(i)
    shared = [v2 for v2 in buckets.values() if len(v2) > 1]
    adv = None
    if shared:
        victim = shared[0][-1]
        bad = list(synth)
        bad[victim] = ALPHA[(ALPHA.index(bad[victim]) + 11) % 26]
        v2, _, _, _, _ = decide(symbols, conv, ct="".join(bad))
        adv = (v2 == "CONTRADICTION")
    return ok, adv, nc


for name, stream in STREAMS.items():
    for qrule in ("retain", "strip"):
        s = apply_qmark(stream, qrule)
        for _ in range(3):
            off = rng.randrange(0, len(s) - 97 + 1)
            conv = conventions[rng.randrange(12)]
            ok, adv, nc = plant_and_check(g1_symbols(s, off), conv,
                                          noninjective=rng.random() < 0.3)
            ctrl["g1_planted_total"] += 1
            ctrl["g1_planted_pass"] += bool(ok)
            if adv is not None:
                ctrl["g1_adv_total"] += 1
                ctrl["g1_adv_pass"] += bool(adv)
            else:
                ctrl["g1_adv_not_capable"] += 1
for k in (1, 2, 5, 13, 24):
    for al in ("left", "right", "centred"):
        conv = conventions[rng.randrange(12)]
        sym = g2_symbols(k, al)
        if not sym:
            continue
        ok, adv, nc = plant_and_check(sym, conv)
        ctrl["g2_planted_total"] += 1
        ctrl["g2_planted_pass"] += bool(ok)
        if adv is not None:
            ctrl["g2_adv_total"] += 1
            ctrl["g2_adv_pass"] += bool(adv)
        else:
            ctrl["g2_adv_not_capable"] += 1

print(f"   G1 planted positives : {ctrl['g1_planted_pass']}/{ctrl['g1_planted_total']}"
      " detected and f recovered on every constrained symbol")
print(f"   G1 adversarial       : {ctrl['g1_adv_pass']}/{ctrl['g1_adv_total']} flipped"
      f"  ({ctrl['g1_adv_not_capable']} not counted - incapable of changing the verdict)")
print(f"   G2 planted positives : {ctrl['g2_planted_pass']}/{ctrl['g2_planted_total']}")
print(f"   G2 adversarial       : {ctrl['g2_adv_pass']}/{ctrl['g2_adv_total']} flipped"
      f"  ({ctrl['g2_adv_not_capable']} not counted)")
assert ctrl["g1_planted_pass"] == ctrl["g1_planted_total"]
assert ctrl["g1_adv_pass"] == ctrl["g1_adv_total"]
assert ctrl["g2_planted_pass"] == ctrl["g2_planted_total"]
assert ctrl["g2_adv_pass"] == ctrl["g2_adv_total"]
print()

# ---------------------------------------------------------------- the real test
print("## THE REAL TEST")
rows_out, feasible = [], []
cdist = collections.Counter()
seen_cases = {}
dupes = 0
stats = collections.Counter()

for name, stream in STREAMS.items():
    for qrule in ("retain", "strip", "block"):
        s = apply_qmark(stream, "strip" if qrule == "strip" else "retain")
        if len(s) < 97:
            continue
        for offset in range(0, len(s) - 97 + 1):
            sym = g1_symbols(s, offset)
            key = (tuple(sym[i] for i in JP), qrule if qrule == "block" else "x")
            if key in seen_cases:
                dupes += 12
                continue
            seen_cases[key] = (name, qrule, offset)
            for conv in conventions:
                v, c, w, _, nc = decide(sym, conv, qrule=qrule)
                cdist[c] += 1
                stats["cases"] += 1
                rec = {"map": "G1", "stream": name, "qrule": qrule, "offset": offset,
                       "convention": conv.name, "constraints": c, "constrained": nc,
                       "verdict": v}
                if v == "BLOCKED":
                    stats["blocked"] += 1
                elif c < MIN_CONSTRAINTS:
                    rec["verdict"] = "UNDECIDED"
                    stats["undecided"] += 1
                elif v == "FEASIBLE":
                    feasible.append(rec)
                else:
                    stats["contradiction"] += 1
                rows_out.append(rec)

for k in range(1, 25):
    for al in ("left", "right", "centred"):
        sym = g2_symbols(k, al)
        for qrule in ("retain", "block"):
            for conv in conventions:
                v, c, w, _, nc = decide(sym, conv, qrule=qrule)
                cdist[c] += 1
                stats["cases"] += 1
                rec = {"map": "G2", "k": k, "alignment": al, "qrule": qrule,
                       "convention": conv.name, "constraints": c, "constrained": nc,
                       "verdict": v}
                if v == "BLOCKED":
                    stats["blocked"] += 1
                elif c < MIN_CONSTRAINTS:
                    rec["verdict"] = "UNDECIDED"
                    stats["undecided"] += 1
                elif v == "FEASIBLE":
                    feasible.append(rec)
                else:
                    stats["contradiction"] += 1
                rows_out.append(rec)

g1 = [r for r in rows_out if r["map"] == "G1"]
g2 = [r for r in rows_out if r["map"] == "G2"]
print(f"   cases decided        : {stats['cases']:,}"
      f"   (G1 {len(g1):,}, G2 {len(g2):,})")
print(f"   duplicate G1 windows deduplicated : {dupes:,}")
print(f"   CONTRADICTION        : {stats['contradiction']:,}")
print(f"   UNDECIDED (<= {MIN_CONSTRAINTS - 1} constraints) : {stats['undecided']:,}")
print(f"   BLOCKED by a '?' under the block rule : {stats['blocked']:,}")
print(f"   FEASIBLE among decided : {len(feasible)}")
print()
print("   constraint-count distribution:")
for c in sorted(cdist):
    tag = "   <- UNDECIDED" if c < MIN_CONSTRAINTS else f"   chance survival 26^-{c} = {26.0**-c:.1e}"
    print(f"      {c:>2} constraints : {cdist[c]:>7,} cases{tag}")
print()
dec_g1 = sum(1 for r in g1 if r["verdict"] in ("FEASIBLE", "CONTRADICTION"))
dec_g2 = sum(1 for r in g2 if r["verdict"] in ("FEASIBLE", "CONTRADICTION"))
print(f"## Per index map")
print(f"   G1 linear offset : {len(g1):,} cases, {dec_g1:,} decided, "
      f"{sum(1 for r in g1 if r['verdict'] == 'FEASIBLE')} feasible")
print(f"   G2 row-local     : {len(g2):,} cases, {dec_g2:,} decided, "
      f"{sum(1 for r in g2 if r['verdict'] == 'FEASIBLE')} feasible")
print()
per = collections.Counter((r["stream"], r["qrule"]) for r in g1
                          if r["verdict"] in ("FEASIBLE", "CONTRADICTION"))
print("   decided G1 cases by stream and question-mark rule. Streams that are SPANS of a")
print("   longer stream contribute no separate cases: every k12 window is an `above`")
print("   window, and `k3` and the rows-1-24 part of `full28` likewise, so they are")
print("   deduplicated by realised symbol tuple rather than re-tested. Their windows ARE")
print("   covered - under the stream that first supplied them.")
for (nm, qr), n in sorted(per.items()):
    print(f"      {nm:<11} {qr:<7} {n:>6,}")
print()

if not feasible:
    print("## RESULT: NEGATIVE on every decided case")
    print("   No key that is an arbitrary function of a single symbol of the authoritative")
    print("   cipher-side text - taken at a fixed linear offset with no wrapping, or at the")
    print("   same row-local index a fixed number of rows above - can produce K4 from a")
    print("   plaintext carrying the public cribs, under the 12 committed conventions.")
    print("   Because f was decided rather than enumerated, this covers every key alphabet")
    print("   and every non-injective symbol map at once.")
    print()
    print("   What it costs the leading architecture: Checkpoint K ranked a long key from an")
    print("   unidentified external source first, and said it could only move when a source")
    print("   was identified. The new evidence identified the most physically obvious")
    print("   candidate - the 745 characters engraved directly above K4 - and it fails as a")
    print("   direct single-symbol running key. That is a real loss for the hypothesis, not")
    print("   a neutral result.")
else:
    print("## FEASIBLE CASES RECORDED - not tuned around, not a solution")
    for r in feasible[:20]:
        print(f"   {r}")
    print("   Any G2 hit is NOT promoted to a physical claim: see the preregistered")
    print("   asymmetry. Any follow-up requires a new preregistration.")
print()
print("## Scope")
print(f"   {stats['undecided']:,} cases are UNDECIDED for lack of constraint and are NOT")
print("   claimed eliminated. Untouched: functions of two source symbols, position-")
print("   modulated f, resets mid-message, non-shift combiners, transposition-composed")
print("   or fractionating architectures, and every physically-aligned model, which")
print("   remains parked on evidence Request 4. Verdicts touching the k12 stream inherit")
print("   the unresolved 432-vs-435 letter discrepancy in rows 1-14.")

out = os.path.join(REPO_ROOT, "results", "exp035")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "summary.json"), "w") as fh:
    json.dump({"experiment": "EXP-035", "ciphertext_sha256": k4.sha256,
               "cipher_side_rows_sha256": ROWSHA,
               "prereg": "docs/exp035-preregistration.md",
               "model": "k[i] = f(S[g(i)]), f any function, decided exactly",
               "min_constraints": MIN_CONSTRAINTS,
               "streams": {n: len(s) for n, s in STREAMS.items()},
               "stats": dict(stats), "deduplicated": dupes,
               "constraint_distribution": dict(cdist),
               "feasible": feasible, "controls": dict(ctrl),
               "rows": rows_out}, fh, indent=1)
print(f"\n   wrote results/exp035/summary.json ({len(rows_out):,} case records)")
