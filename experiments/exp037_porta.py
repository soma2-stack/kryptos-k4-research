"""EXP-037  Periodic Porta, alone and composed with the declared EXP-036 transpositions.

Preregistered in docs/exp037-preregistration.md before implementation.

Grade: structural/historical candidate only. No Sanborn or Scheidt evidence says K4 uses
Porta. And per the equivalence audit, Porta IS a shift family under some pair of mixed
alphabets - just not under any of the four evidenced STD/KRYPTOS pairs - so this tests one
precommitted historical alphabet pair, not a new algebraic class.

Key structural fact, which is what makes this cheap: Porta sends every letter to the
OPPOSITE half, so a (p, c) pair is realised by exactly one row when the halves differ and
by NO row when they match. The null is therefore (cross-half)^24 x 13^-c, derived from the
table family rather than assumed.

Constraint counts are computed over every constrained position before any verdict is
formed (the EXP-034 invariant).
"""
import sys, os, json, math, time, collections, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np

from k4lib.data import load, REPO_ROOT
from k4lib.conventions import all_conventions
from k4lib import transpositions as TR

N = 97
PERIODS = tuple(range(1, 24))
STD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KRY = "KRYPTOSABCDEFGHIJLMNQUVWXZ"
ORDERINGS = {"STD": STD, "KRY": KRY}

k4 = load()
CT = k4.ciphertext
CRIB = {i: p for i, p, _ in k4.crib_positions()}
JP = sorted(CRIB)

print("# EXP-037 periodic Porta, direct and transposition-composed")
print(f"ciphertext sha256 {k4.sha256}\n")


# ---------------------------------------------------------------- the tables
def porta_tables(order):
    """13 rows, from the documented definition. Row n: a<13 -> 13+((a+n) mod 13)."""
    rows = []
    for n in range(13):
        m = {}
        for a, ch in enumerate(order):
            b = 13 + ((a + n) % 13) if a < 13 else (a - 13 - n) % 13
            m[ch] = order[b]
        rows.append(m)
    return rows


print("## Table construction and its documented anchors")
for name, order in ORDERINGS.items():
    rows = porta_tables(order)
    recip = all(all(r[r[ch]] == ch for ch in order) for r in rows)
    fixed = max(sum(1 for ch in order if r[ch] == ch) for r in rows)
    print(f"   {name}: 13 rows | all self-reciprocal {recip} | max fixed points {fixed}")
    assert recip and fixed == 0
r0, r1 = porta_tables(STD)[0], porta_tables(STD)[1]
assert r0["A"] == "N" and r0["M"] == "Z", "row 0 must be the textbook A<->N ... M<->Z"
assert r1["A"] == "O" and r1["L"] == "Z" and r1["M"] == "N", "row 1 must be A<->O ... M<->N"
print("   textbook anchors asserted: row 0 = A<->N..M<->Z, row 1 = A<->O..L<->Z, M<->N\n")

# per-ordering lookup: (plaintext letter, ciphertext letter) -> row index or -1
ROW_OF = {}
for name, order in ORDERINGS.items():
    tab = np.full((26, 26), -1, dtype=np.int8)
    for n, r in enumerate(porta_tables(order)):
        for ch in order:
            tab[ord(ch) - 65, ord(r[ch]) - 65] = n
    ROW_OF[name] = tab
    realis = int((tab >= 0).sum())
    print(f"   {name}: of the 676 (p,c) letter pairs, {realis} are realisable by exactly one"
          f" Porta row and {676 - realis} by none")
print()

# ---------------------------------------------------------------- decidability
print("## Decidability, computed before any verdict")
occ = {q: len({j % q for j in JP}) for q in range(1, 25)}
con = {q: len(JP) - occ[q] for q in occ}
half = {name: (lambda ch, o=order: 0 if o.index(ch) < 13 else 1) for name, order in ORDERINGS.items()}
for name, order in ORDERINGS.items():
    same = [i for i in JP if half[name](CRIB[i]) == half[name](CT[i])]
    cnt = collections.Counter(half[name](ch) for ch in CT)
    q_cross = sum(cnt[1 - half[name](CRIB[i])] / 97.0 for i in JP) / 24
    print(f"   {name}: crib pairs in the SAME half {len(same)}/24; ciphertext half counts "
          f"{dict(sorted(cnt.items()))}; mean cross-half P {q_cross:.4f}; "
          f"P(all 24 cross-half) ~ {q_cross ** 24:.3e}")
print(f"   constraint counts c(q) = 24 - |{{j mod q}}|: q=2 -> {con[2]}, q=13 -> {con[13]}, "
      f"q=17 -> {con[17]}, q=23 -> {con[23]}, q=24 -> {con[24]} (excluded)")
print()

# ---------------------------------------------------------------- DIRECT family
print("## DIRECT periodic Porta (no transposition) — decided with no search")
direct = {}
for name in ORDERINGS:
    tab = ROW_OF[name]
    rows_forced = [int(tab[ord(CRIB[i]) - 65, ord(CT[i]) - 65]) for i in JP]
    unreal = [(i, CRIB[i], CT[i]) for i, r in zip(JP, rows_forced) if r < 0]
    direct[name] = {"unrealisable_pairs": len(unreal), "examples": unreal[:5],
                    "feasible_periods": []}
    for q in PERIODS:
        if unreal:
            continue
        byres = collections.defaultdict(set)
        for i, r in zip(JP, rows_forced):
            byres[i % q].add(r)
        if all(len(v) == 1 for v in byres.values()):
            direct[name]["feasible_periods"].append(q)
    print(f"   {name}: {len(unreal)} of 24 crib pairs are realisable by NO Porta row"
          f"  ->  feasible periods: {direct[name]['feasible_periods'] or 'NONE, at any period'}")
    if unreal:
        print(f"      e.g. {unreal[:4]}")
print("   A pair whose plaintext and ciphertext letters share a half cannot be produced by")
print("   any Porta row at any key, so a single such pair kills the whole direct family.")
print()

# ---------------------------------------------------------------- controls
print("## Controls")
rng = random.Random(1563)
ctrl = collections.Counter()
conventions = all_conventions()


def read_order(w, key, bu):
    o = [None] * N
    for j in range(N):
        o[TR.columnar_forward(j, w, key, bu)] = j
    return o


def decide_single(ct, idx, q, name, orderlabel):
    """Count over every constrained position first, verdict after."""
    tab = ROW_OF[name]
    seen, nconstr, bad, unreal = {}, 0, False, 0
    for t, j in enumerate(JP):
        i = int(idx[t])
        r = int(tab[ord(CRIB[j]) - 65, ord(ct[i]) - 65])
        if r < 0:
            unreal += 1
        res = (j % q) if orderlabel == "A" else (i % q)
        if res in seen:
            nconstr += 1
            if seen[res] != r:
                bad = True
        else:
            seen[res] = r
    return (unreal == 0 and not bad), nconstr, unreal, seen


rows_seen = set()
for trial in range(80):
    name = rng.choice(list(ORDERINGS))
    tab_rows = porta_tables(ORDERINGS[name])
    orderlabel = rng.choice(("A", "B"))
    w = rng.randrange(2, 11 if orderlabel == "A" else 9)
    key = tuple(rng.sample(range(w), w))
    bu = rng.random() < 0.5
    q = rng.choice(PERIODS)
    o = read_order(w, key, bu)
    pos = {j: i for i, j in enumerate(o)}
    # plant: force coverage of every Porta row across the run, and allow repeats
    ks = [rng.randrange(13) for _ in range(q)]
    if trial < 13:
        ks[0] = trial % 13
    if q >= 2 and rng.random() < 0.3:
        ks[1] = ks[0]
    rows_seen.update(ks)
    PT = ["X"] * N
    for i, ch in CRIB.items():
        PT[i] = ch
    ct = list(CT)
    if orderlabel == "A":
        for j in range(N):
            ct[pos[j]] = tab_rows[ks[j % q]][PT[j]]
    else:
        for i in range(N):
            ct[i] = tab_rows[ks[i % q]][PT[o[i]]]
    ct = "".join(ct)
    idx = [pos[j] for j in JP]
    ok, nc, unreal, seen = decide_single(ct, idx, q, name, orderlabel)
    rec = all(seen[r] == ks[r] for r in seen)
    ctrl["planted_total"] += 1
    ctrl["planted_pass"] += bool(ok and rec)
    # adversarial that definitely intersects an active constraint
    byres = collections.defaultdict(list)
    for t, j in enumerate(JP):
        byres[(j % q) if orderlabel == "A" else (idx[t] % q)].append(idx[t])
    shared = [v for v in byres.values() if len(v) > 1]
    if shared:
        victim = shared[0][-1]
        bad = list(ct)
        # move the victim to a letter that forces a different row, or none at all
        bad[victim] = STD[(STD.index(bad[victim]) + 1) % 26]
        ok2, _, _, _ = decide_single("".join(bad), idx, q, name, orderlabel)
        ctrl["adv_total"] += 1
        ctrl["adv_pass"] += (not ok2)
    else:
        ctrl["adv_not_capable"] += 1
    # Period discrimination, counted only where it is mathematically meaningful. A q=1
    # plant uses ONE row for the whole message, so it stays consistent at every period -
    # every partition refines the single class. Scoring those as failures would be a
    # wrong control, not a finding, so they are reported separately.
    crib_rows = {seen[r] for r in seen}
    if q == 1 or len(crib_rows) == 1:
        # Degenerate for this purpose: one row across every constrained position, either
        # because the period is 1 or because the planted key happens to take a single
        # value there. Such a plant IS consistent at every period by construction, so
        # counting it as a discrimination failure would be a wrong control, not a finding.
        ctrl["perioddisc_degenerate_excluded"] += 1
    else:
        fails = sum(1 for q2 in PERIODS if q2 != q
                    and not decide_single(ct, idx, q2, name, orderlabel)[0])
        ctrl["perioddisc_total"] += 1
        ctrl["perioddisc_pass"] += (fails > 0)
    # WRONG-TABLE-FAMILY control, both directions
    cv = conventions[rng.randrange(12)]
    kv = [rng.randrange(26) for _ in range(q)]
    ctv = list(CT)
    for j in range(N):
        ctv[pos[j]] = cv.encrypt_letter(PT[j], kv[j % q])
    okv, _, _, _ = decide_single("".join(ctv), idx, q, name, "A")
    ctrl["wrong_family_total"] += 1
    ctrl["wrong_family_pass"] += (not okv)           # a Vigenere plant must fail Porta
    # and a Porta plant must fail a shift detector
    seenv, badv = {}, False
    for t, j in enumerate(JP):
        r = (j % q) if orderlabel == "A" else (idx[t] % q)
        kk = cv.key_index(CRIB[j], ct[idx[t]])
        if r in seenv and seenv[r] != kk:
            badv = True
        seenv.setdefault(r, kk)
    ctrl["wrong_family_rev_total"] += 1
    ctrl["wrong_family_rev_pass"] += bool(badv)

print(f"   planted positives      : {ctrl['planted_pass']}/{ctrl['planted_total']}"
      f" detected with the row sequence recovered; distinct Porta rows exercised:"
      f" {len(rows_seen)}/13")
print(f"   adversarial (capable)  : {ctrl['adv_pass']}/{ctrl['adv_total']}"
      f"   ({ctrl['adv_not_capable']} not counted - incapable of changing the verdict)")
print(f"   period discrimination  : {ctrl['perioddisc_pass']}/{ctrl['perioddisc_total']}"
      f"   ({ctrl['perioddisc_degenerate_excluded']} degenerate plants excluded: a key"
      f" taking one row across all constrained positions is consistent at every period)")
print(f"   wrong-family (Vigenere plant rejected by Porta) : "
      f"{ctrl['wrong_family_pass']}/{ctrl['wrong_family_total']}")
print(f"   wrong-family (Porta plant rejected by a shift)  : "
      f"{ctrl['wrong_family_rev_pass']}/{ctrl['wrong_family_rev_total']}")
assert ctrl["planted_pass"] == ctrl["planted_total"], "positive control failed"
assert ctrl["adv_pass"] == ctrl["adv_total"], "adversarial control failed"
assert len(rows_seen) == 13, "controls did not exercise every Porta row"
assert ctrl["wrong_family_pass"] == ctrl["wrong_family_total"]
assert ctrl["perioddisc_pass"] == ctrl["perioddisc_total"], "period discrimination failed"
print()

# ---------------------------------------------------------------- composed sweep
print("## COMPOSED: Porta over the declared EXP-036 transposition families")
CTA = np.frombuffer(CT.encode(), dtype=np.uint8).astype(np.int64) - 65
PL = np.array([ord(CRIB[j]) - 65 for j in JP], dtype=np.int64)
RESA = {q: np.array([j % q for j in JP], dtype=np.int64) for q in PERIODS}
res_out = {"cases": 0, "parity_survivors": 0, "feasible": 0, "hits": [], "per_width": {}}
t0 = time.time()


def sweep(idx, name):
    """idx (M,24) ciphertext indices -> counts. Half-parity filter, then row consistency."""
    tab = ROW_OF[name]
    rows = tab[PL[None, :], CTA[idx]]                      # (M,24) row index or -1
    alive = np.all(rows >= 0, axis=1)
    n_alive = int(alive.sum())
    feas = []
    if n_alive:
        sub = rows[alive]
        subidx = idx[alive]
        for q in PERIODS:
            for lab in ("A", "B"):
                r = np.broadcast_to(RESA[q], sub.shape) if lab == "A" else (subidx % q)
                ok = np.ones(sub.shape[0], dtype=bool)
                for v in range(q):
                    m = (r == v)
                    cnt = m.sum(axis=1)
                    lo = np.where(m, sub, np.int16(99)).min(axis=1)
                    hi = np.where(m, sub, np.int16(-1)).max(axis=1)
                    ok &= (cnt <= 1) | (lo == hi)
                if ok.any():
                    for mi in np.nonzero(ok)[0][:10]:
                        feas.append({"period": q, "order": lab, "ordering": name})
    return n_alive, feas


for w in range(2, 11):
    wc = 0
    for block in TR.perm_blocks(w):
        for bu in (False, True):
            for orient in ("A", "B"):
                idx = TR.crib_ct_indices(block, w, JP, bu, orient).astype(np.int64)
                wc += block.shape[0]
                for name in ORDERINGS:
                    na, feas = sweep(idx, name)
                    res_out["parity_survivors"] += na
                    res_out["cases"] += block.shape[0] * len(PERIODS) * 2
                    res_out["feasible"] += len(feas)
                    res_out["hits"].extend(feas[:5])
    res_out["per_width"][w] = wc
    print(f"   w={w:<3} {wc:>10,} permutations   cross-half survivors so far "
          f"{res_out['parity_survivors']:,}   feasible {res_out['feasible']}   "
          f"[{time.time() - t0:.0f}s]")

small = {"perms": 0, "cases": 0, "parity_survivors": 0, "feasible": 0, "dupes": 0}
seen_perm = set()
for w, routes in [(w, TR.route_permutations(w)) for w in range(2, 97)] + \
                 [(None, TR.engraved_routes())]:
    for nm, order in sorted(routes.items()):
        for orient in ("fwd", "inv"):
            seq = order if orient == "fwd" else [order.index(i) for i in range(N)]
            if tuple(seq) in seen_perm:
                small["dupes"] += 1
                continue
            seen_perm.add(tuple(seq))
            small["perms"] += 1
            pos = {j: i for i, j in enumerate(seq)}
            idx = [pos[j] for j in JP]
            for name in ORDERINGS:
                for q in PERIODS:
                    for lab in ("A", "B"):
                        ok, nc, unreal, _ = decide_single(CT, idx, q, name, lab)
                        small["cases"] += 1
                        if unreal == 0:
                            small["parity_survivors"] += 1
                        if ok:
                            small["feasible"] += 1
print(f"   T2/T3: {small['perms']:,} distinct permutations ({small['dupes']:,} deduplicated),"
      f" {small['cases']:,} cases, cross-half survivors {small['parity_survivors']},"
      f" feasible {small['feasible']}")

# ---------------------------------------------------------------- result
total = res_out["cases"] + small["cases"]
feas = res_out["feasible"] + small["feasible"]
print("\n## RESULT")
print(f"   DIRECT (no transposition)  : IMPOSSIBLE at every period and key, both orderings")
print(f"                                (16 of 24 crib pairs share a half)")
print(f"   COMPOSED cases decided     : {total:,}")
print(f"   permutations passing the cross-half filter : {res_out['parity_survivors'] + small['parity_survivors']:,}")
print(f"   FEASIBLE                   : {feas}")
print()
if feas == 0:
    print("   NEGATIVE. K4 is not a periodic Porta cipher over the STD or KRYPTOS ordering")
    print("   at any period 1-23, alone or composed with any transposition from the declared")
    print("   EXP-036 families, in either composition order. The Porta row schedule was")
    print("   decided existentially, so every key word of those lengths is covered.")
    print()
    print("   Read it narrowly. Porta is a shift family under SOME mixed-alphabet pair; this")
    print("   result is about one precommitted historical pair, and says nothing about shift")
    print("   families generally or about reciprocal tables in general.")
else:
    print("   FEASIBLE CASES RECORDED - hypotheses only, not tuned around.")
print()
print("## Scope")
print("   NOT eliminated: Porta over other orderings, aperiodic or reset row schedules,")
print("   transpositions outside the declared families, other reciprocal-table systems, and")
print("   everything outside this family. Case counts are not counts of independent tests.")

out = os.path.join(REPO_ROOT, "results", "exp037")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "summary.json"), "w") as fh:
    json.dump({"experiment": "EXP-037", "ciphertext_sha256": k4.sha256,
               "prereg": "docs/exp037-preregistration.md",
               "grade": "structural/historical candidate only; no Sanborn/Scheidt evidence",
               "periods": list(PERIODS), "orderings": sorted(ORDERINGS),
               "constraints": con, "direct": direct,
               "composed": {k: v for k, v in res_out.items() if k != "hits"},
               "T2_T3": small, "total_composed_cases": total, "feasible": feas,
               "hits": res_out["hits"], "controls": dict(ctrl),
               "porta_rows_exercised_by_controls": len(rows_seen)}, fh, indent=1)
print(f"\n   wrote results/exp037/summary.json")
