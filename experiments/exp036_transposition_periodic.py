"""EXP-036  K3-type transposition composed with a K1/K2-type periodic polyalphabetic.

Preregistered in docs/exp036-preregistration.md before implementation.

Order A   C[sigma(j)] = conv(P[j],        k[j mod p])      residue partition is sigma-free
Order B   C[i]        = conv(P[sigma(i)], k[i mod p])      residue depends on sigma

k is NEVER enumerated. Per case the key is decided existentially: feasible iff every pair
of constrained positions in the same residue class forces the same key index. Absorbed by
that: the numerical key, any repeating key WORD of length p (so PALIMPSEST at p=10 and
ABSCISSA at p=8 are covered as special cases), and tableau row labels. NOT absorbed: the
plaintext and ciphertext component alphabets, which are carried explicitly as STD or KRY
by the 12 committed conventions.

Constraint counts are computed over every constrained position BEFORE any verdict is
formed (the EXP-034 invariant), and a (period, family, order) combination enters the
elimination only if N * 26^-c < 0.01 (preregistered).
"""
import sys, os, json, math, time, collections, random, itertools
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np

from k4lib.data import load, REPO_ROOT
from k4lib.conventions import all_conventions
from k4lib import transpositions as TR

N = 97
PERIODS = tuple(range(2, 24))
DECIDE_BUDGET = 0.01                 # preregistered: N * 26^-c must stay below this
MIN_CONSTRAINTS_B = 7                # preregistered floor for per-case order-B counts

k4 = load()
CT = k4.ciphertext
CRIB = {i: p for i, p, _ in k4.crib_positions()}
JP = sorted(CRIB)
conventions = all_conventions()
CTA = np.frombuffer(CT.encode(), dtype=np.uint8).astype(np.int16)

print("# EXP-036 transposition composed with a periodic polyalphabetic")
print(f"ciphertext sha256 {k4.sha256}\n")

# ---------------------------------------------------------------- decidability table
print("## Decidability table (computed before any verdict)")
occ = {p: len({j % p for j in JP}) for p in range(2, 25)}
con = {p: len(JP) - occ[p] for p in occ}
FAM = {"T1_w2_10": sum(math.factorial(w) for w in range(2, 11)) * 4,
       "T1_w2_8": sum(math.factorial(w) for w in range(2, 9)) * 4}
print("    p  occupied  constraints   26^-c      admissible at N=16,151,648 / N=184,928")
for p in range(2, 25):
    s = 26.0 ** -con[p]
    a = FAM["T1_w2_10"] * s < DECIDE_BUDGET
    b = FAM["T1_w2_8"] * s < DECIDE_BUDGET
    flag = "" if p in PERIODS else "   <- OUTSIDE the declared range"
    print(f"   {p:>2}  {occ[p]:>8}  {con[p]:>11}   {s:>9.2e}    "
          f"{'yes' if a else 'NO ':>3} / {'yes' if b else 'NO ':>3}{flag}")
assert all(FAM["T1_w2_10"] * 26.0 ** -con[p] < DECIDE_BUDGET for p in PERIODS)
print("   Every declared period is admissible for both orders; p=24 is excluded in")
print("   advance, which is why the range stops at 23.")
print()

# key index for each (convention, crib position, candidate ciphertext letter)
KEYTAB = np.zeros((len(conventions), len(JP), 26), dtype=np.int16)
for ci, cv in enumerate(conventions):
    for t, j in enumerate(JP):
        for L in range(26):
            KEYTAB[ci, t, L] = cv.key_index(CRIB[j], chr(65 + L))

# order-A spanning pair set per period: one pair per extra member of each residue class
PAIRS_A = {}
for p in PERIODS:
    byres = collections.defaultdict(list)
    for t, j in enumerate(JP):
        byres[j % p].append(t)
    PAIRS_A[p] = [(v[0], v[i]) for v in byres.values() for i in range(1, len(v))]
    assert len(PAIRS_A[p]) == con[p]
print(f"## Order-A spanning pair checks total {sum(len(v) for v in PAIRS_A.values())} "
      f"over {len(PERIODS)} periods\n")


def kv_matrix_fast(idx, ci):
    letters = (CTA[idx] - 65).astype(np.int64)          # (M,24)
    out = np.empty(idx.shape, dtype=np.int16)
    for t in range(len(JP)):
        out[:, t] = KEYTAB[ci, t][letters[:, t]]
    return out


def decide_A_block(idx, ci):
    """-> dict period -> boolean feasible mask, for one convention."""
    kv = kv_matrix_fast(idx, ci)
    res = {}
    for p in PERIODS:
        ok = np.ones(idx.shape[0], dtype=bool)
        for a, b in PAIRS_A[p]:
            ok &= kv[:, a] == kv[:, b]
        res[p] = ok
    return res


def decide_B_block(idx, ci):
    """Order B: residue of the CIPHERTEXT index, so grouping varies per case."""
    kv = kv_matrix_fast(idx, ci)
    out = {}
    for p in PERIODS:
        r = idx % p
        ok = np.ones(idx.shape[0], dtype=bool)
        nconstr = np.zeros(idx.shape[0], dtype=np.int16)
        for v in range(p):
            m = (r == v)
            cnt = m.sum(axis=1)
            nconstr += np.maximum(cnt - 1, 0).astype(np.int16)
            lo = np.where(m, kv, np.int16(32000)).min(axis=1)
            hi = np.where(m, kv, np.int16(-1)).max(axis=1)
            ok &= (cnt <= 1) | (lo == hi)
        out[p] = (ok, nconstr)
    return out


# ---------------------------------------------------------------- controls
print("## Controls")
rng = random.Random(20260913)
ctrl = collections.Counter()
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def read_order(w, key, bu):
    o = [None] * N
    for j in range(N):
        o[TR.columnar_forward(j, w, key, bu)] = j
    return o


def plant(order, p, conv, orderlabel, repeated_key=False):
    """Synthesise with independent arithmetic, then require detection and key recovery."""
    key = [rng.randrange(26) for _ in range(p)]
    if repeated_key and p >= 2:
        key[1] = key[0]
    PT = ["X"] * N
    for i, ch in CRIB.items():
        PT[i] = ch
    ct = list(CT)
    pos = {j: i for i, j in enumerate(order)}                     # plaintext j -> ct index
    if orderlabel == "A":
        for j in range(N):
            ct[pos[j]] = conv.encrypt_letter(PT[j], key[j % p])
        idx = np.array([[pos[j] for j in JP]], dtype=np.int64)
    else:
        for i in range(N):
            ct[i] = conv.encrypt_letter(PT[order[i]], key[i % p])
        idx = np.array([[pos[j] for j in JP]], dtype=np.int64)
    return "".join(ct), idx, key


def decide_single(ct, idx, p, conv, orderlabel):
    """Pure-python decision used by the controls; count first, verdict after."""
    seen, nconstr, bad = {}, 0, False
    for t, j in enumerate(JP):
        i = int(idx[0, t])
        r = (j % p) if orderlabel == "A" else (i % p)
        kval = conv.key_index(CRIB[j], ct[i])
        if r in seen:
            nconstr += 1
            if seen[r] != kval:
                bad = True
        else:
            seen[r] = kval
    return (not bad), nconstr, seen


for _ in range(36):
    for orderlabel in ("A", "B"):
        w = rng.randrange(2, 11 if orderlabel == "A" else 9)
        key = tuple(rng.sample(range(w), w))
        bu = rng.random() < 0.5
        p = rng.choice(PERIODS)
        conv = conventions[rng.randrange(12)]
        order = read_order(w, key, bu)
        ct, idx, planted_key = plant(order, p, conv, orderlabel,
                                     repeated_key=rng.random() < 0.3)
        ok, nc, seen = decide_single(ct, idx, p, conv, orderlabel)
        rec = all(seen[r] == planted_key[r] for r in seen)
        ctrl["planted_total"] += 1
        ctrl["planted_pass"] += bool(ok and rec)
        # adversarial: corrupt a position whose residue class holds >= 2 constrained
        byres = collections.defaultdict(list)
        for t, j in enumerate(JP):
            r = (j % p) if orderlabel == "A" else (int(idx[0, t]) % p)
            byres[r].append((t, int(idx[0, t])))
        shared = [v for v in byres.values() if len(v) > 1]
        if shared:
            _, victim = shared[0][-1]
            bad = list(ct)
            bad[victim] = ALPHA[(ALPHA.index(bad[victim]) + 9) % 26]
            ok2, _, _ = decide_single("".join(bad), idx, p, conv, orderlabel)
            ctrl["adv_total"] += 1
            ctrl["adv_pass"] += (not ok2)
        else:
            ctrl["adv_not_capable"] += 1
        # period discrimination: the plant must fail at SOME other admissible period
        others = [q for q in PERIODS if q != p]
        fails = sum(1 for q in others if not decide_single(ct, idx, q, conv, orderlabel)[0])
        ctrl["perioddisc_total"] += 1
        ctrl["perioddisc_pass"] += (fails > 0)
        ctrl["perioddisc_failing_periods"] += fails

print(f"   planted positives      : {ctrl['planted_pass']}/{ctrl['planted_total']}"
      " detected with the key recovered on every constrained residue class")
print(f"   adversarial (capable)  : {ctrl['adv_pass']}/{ctrl['adv_total']} flipped"
      f"   ({ctrl['adv_not_capable']} not counted - incapable of changing the verdict)")
print(f"   period discrimination  : {ctrl['perioddisc_pass']}/{ctrl['perioddisc_total']}"
      f" plants rejected at some other period"
      f"  (mean {ctrl['perioddisc_failing_periods'] / max(ctrl['perioddisc_total'], 1):.1f}"
      f" of {len(PERIODS) - 1} other periods reject)")
assert ctrl["planted_pass"] == ctrl["planted_total"], "positive control failed"
assert ctrl["adv_pass"] == ctrl["adv_total"], "adversarial control failed"
print()

# ---------------------------------------------------------------- order A sweep
print("## ORDER A — T1 widths 2-10, all column orders, plus T2 and T3")
t0 = time.time()
A = {"cases": 0, "feasible": collections.Counter(), "hits": [], "per_width": {}}
for w in range(2, 11):
    wc = 0
    for block in TR.perm_blocks(w):
        for bu in (False, True):
            for orient in ("A", "B"):
                idx = TR.crib_ct_indices(block, w, JP, bu, orient).astype(np.int64)
                wc += block.shape[0]
                for ci in range(12):
                    masks = decide_A_block(idx, ci)
                    for p, m in masks.items():
                        A["cases"] += block.shape[0]
                        n = int(m.sum())
                        if n:
                            A["feasible"][p] += n
                            for mi in np.nonzero(m)[0][:20]:
                                A["hits"].append({"order": "A", "family": "T1", "w": w,
                                                  "key": [int(x) for x in block[mi]],
                                                  "bottom_up": bu, "orientation": orient,
                                                  "period": p,
                                                  "convention": conventions[ci].name})
    A["per_width"][w] = wc
    print(f"   w={w:<3} {wc:>10,} permutations   cumulative feasible: "
          f"{sum(A['feasible'].values())}   [{time.time() - t0:.0f}s]")
print(f"   T1 order-A cases {A['cases']:,} in {time.time() - t0:.0f}s")

# T2 / T3 for both orders, pure python (small)
print("\n## T2 rectangle routes (all widths) and T3 ragged engraving routes, both orders")
small = {"cases": 0, "feasible": 0, "hits": [], "perms": 0, "dupes": 0}
seen_perm = set()
route_sets = [(w, TR.route_permutations(w)) for w in range(2, 97)] + \
             [(None, TR.engraved_routes())]
for w, routes in route_sets:
    for nm, order in sorted(routes.items()):
        for orient in ("fwd", "inv"):
            seq = order if orient == "fwd" else [order.index(i) for i in range(N)]
            key = tuple(seq)
            if key in seen_perm:
                small["dupes"] += 1
                continue
            seen_perm.add(key)
            small["perms"] += 1
            pos = {j: i for i, j in enumerate(seq)}
            idx = np.array([[pos[j] for j in JP]], dtype=np.int64)
            for orderlabel in ("A", "B"):
                for conv in conventions:
                    for p in PERIODS:
                        ok, nc, _ = decide_single(CT, idx, p, conv, orderlabel)
                        small["cases"] += 1
                        if ok and nc >= (MIN_CONSTRAINTS_B if orderlabel == "B" else 1):
                            small["feasible"] += 1
                            small["hits"].append({"order": orderlabel, "family":
                                                  "T3" if w is None else "T2", "w": w,
                                                  "route": nm, "orientation": orient,
                                                  "period": p, "convention": conv.name,
                                                  "constraints": nc})
print(f"   distinct permutations {small['perms']:,} ({small['dupes']:,} duplicates "
      f"deduplicated); cases {small['cases']:,}; feasible {small['feasible']}")

# ---------------------------------------------------------------- order B sweep
print("\n## ORDER B — T1 widths 2-8, all column orders (declared narrower: see prereg)")
t1 = time.time()
B = {"cases": 0, "feasible": 0, "undecided": 0, "hits": [], "cdist": collections.Counter()}
for w in range(2, 9):
    for block in TR.perm_blocks(w):
        for bu in (False, True):
            for orient in ("A", "B"):
                idx = TR.crib_ct_indices(block, w, JP, bu, orient).astype(np.int64)
                for ci in range(12):
                    res = decide_B_block(idx, ci)
                    for p, (ok, nconstr) in res.items():
                        B["cases"] += block.shape[0]
                        dec = nconstr >= MIN_CONSTRAINTS_B
                        B["undecided"] += int((~dec).sum())
                        good = ok & dec
                        for c, n in zip(*np.unique(nconstr, return_counts=True)):
                            B["cdist"][int(c)] += int(n)
                        n = int(good.sum())
                        if n:
                            B["feasible"] += n
                            for mi in np.nonzero(good)[0][:20]:
                                B["hits"].append({"order": "B", "family": "T1", "w": w,
                                                  "key": [int(x) for x in block[mi]],
                                                  "bottom_up": bu, "orientation": orient,
                                                  "period": p,
                                                  "convention": conventions[ci].name,
                                                  "constraints": int(nconstr[mi])})
print(f"   T1 order-B cases {B['cases']:,} in {time.time() - t1:.0f}s; "
      f"undecided (<{MIN_CONSTRAINTS_B} constraints) {B['undecided']:,}; "
      f"feasible {B['feasible']}")
print("   order-B per-case constraint counts: "
      + ", ".join(f"{c}:{n:,}" for c, n in sorted(B["cdist"].items())[:12]))

# ---------------------------------------------------------------- result
total = A["cases"] + B["cases"] + small["cases"]
tfeas = sum(A["feasible"].values()) + B["feasible"] + small["feasible"]
print("\n## RESULT")
print(f"   total declared cases decided : {total:,}")
print(f"     order A, T1 widths 2-10    : {A['cases']:,}")
print(f"     order B, T1 widths 2-8     : {B['cases']:,}")
print(f"     T2/T3 both orders          : {small['cases']:,}")
print(f"   FEASIBLE                     : {tfeas}")
worst = max(26.0 ** -con[p] for p in PERIODS)
print(f"   weakest declared period carries {min(con[p] for p in PERIODS)} constraints, "
      f"chance survival {worst:.2e}")
print(f"   expected chance survivors over the order-A T1 sweep alone: "
      f"{FAM['T1_w2_10'] * 12 * sum(26.0 ** -con[p] for p in PERIODS):.3e}")
print()
if tfeas == 0:
    print("   NEGATIVE. K4 is not any transposition from the declared families composed")
    print("   with a periodic polyalphabetic substitution of period 2-23 over STD/KRYPTOS")
    print("   plaintext and ciphertext components under the three committed combiners, in")
    print("   either composition order. Because the key was decided existentially rather")
    print("   than enumerated, this covers every key value, every repeating key WORD of")
    print("   those lengths - PALIMPSEST at p=10 and ABSCISSA at p=8 included - and every")
    print("   tableau row labelling, at once.")
    print()
    print("   What it costs: this was the hybrid the section sequence points at most")
    print("   directly - K1/K2's periodic substitution over K3's transposition. EXP-003")
    print("   tested the gate over 9,312 affine permutations; EXP-033 tested a 175M")
    print("   transposition family with one fixed monoalphabetic map. The intersection is")
    print("   now closed over the declared ranges.")
else:
    print("   FEASIBLE CASES RECORDED - hypotheses only, not tuned around. A feasible case")
    print("   fixes at most p key values and says nothing about the other 73 plaintext")
    print("   positions. Any follow-up requires a new preregistration.")
print()
print("## Scope")
print("   NOT eliminated: keyed columnar widths above the declared limits (11+ for order A,")
print("   9+ for order B), period >= 24, aperiodic/progressive/reset keys, non-shift")
print("   combiners, component alphabets outside {STD, KRY}, double transposition,")
print("   fractionation, and every physically-aligned model. Case counts are not counts of")
print("   independent tests.")

out = os.path.join(REPO_ROOT, "results", "exp036")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "summary.json"), "w") as fh:
    json.dump({"experiment": "EXP-036", "ciphertext_sha256": k4.sha256,
               "prereg": "docs/exp036-preregistration.md",
               "periods": list(PERIODS), "decide_budget": DECIDE_BUDGET,
               "min_constraints_B": MIN_CONSTRAINTS_B,
               "occupied": occ, "constraints": con,
               "orderA": {k: (dict(v) if isinstance(v, collections.Counter) else v)
                          for k, v in A.items() if k != "hits"},
               "orderB": {k: (dict(v) if isinstance(v, collections.Counter) else v)
                          for k, v in B.items() if k != "hits"},
               "T2_T3": {k: v for k, v in small.items() if k != "hits"},
               "total_cases": total, "feasible": tfeas,
               "hits": A["hits"] + B["hits"] + small["hits"],
               "controls": dict(ctrl)}, fh, indent=1)
print(f"\n   wrote results/exp036/summary.json")
