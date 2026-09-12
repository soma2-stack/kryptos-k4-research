"""EXP-033  Arbitrary monoalphabetic substitution composed with a declared transposition.

Preregistered in docs/exp032-033-preregistration.md before implementation.

Model:  C[i] = S(P[sigma(i)])   with sigma from the declared family and S : A-Z -> A-Z
ANY function. S is never enumerated. Per permutation, all 26^26 functions are decided
exactly by consistency of the induced partial map on the 24 public crib positions:

    FEASIBLE-FUNCTION   the map plaintext letter -> ciphertext letter is well defined
    FEASIBLE-BIJECTIVE  and injective

Why this family and not another: every experiment in this repository up to EXP-031
assumes the key depends on message position. The argument that K4 must be
position-preserving rested on the K4/K5 length correspondence, which docs/codex-audit.md
finding 7 withdraws. Nothing here scores plaintext; nothing is fitted.

Deduplication stated in advance: a monoalphabetic substitution commutes with a
transposition, so composition order is not a parameter. Orientation (the map or its
inverse) is.
"""
import sys, os, json, math, time, hashlib, collections, itertools, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np

from k4lib.data import load, REPO_ROOT
from k4lib import transpositions as TR

k4 = load()
CT = k4.ciphertext
cribs = k4.crib_positions()
CRIB = {i: p for i, p, _ in cribs}
JP = sorted(CRIB)                                  # 24 crib plaintext positions
PL = [CRIB[j] for j in JP]
CTA = np.frombuffer(CT.encode(), dtype=np.int8)

# constraint groups fixed by the cribs, before any search
groups = collections.defaultdict(list)
for t, j in enumerate(JP):
    groups[CRIB[j]].append(t)
GROUPS = [v for v in groups.values() if len(v) > 1]
REPS = np.array([v[0] for v in groups.values()], dtype=np.int64)

print("# EXP-033 monoalphabetic substitution composed with a declared transposition")
print(f"ciphertext sha256 {k4.sha256}\n")
print("## Constraint inventory (fixed before the search)")
print(f"   crib positions            : {len(JP)}")
print(f"   distinct plaintext letters: {len(groups)}  "
      + " ".join(f"{L}x{len(v)}" for L, v in sorted(groups.items(), key=lambda kv: -len(kv[1]))))
print(f"   equality constraints      : {sum(len(v) - 1 for v in groups.values())}")
q = collections.Counter(CT)
pchance = 1.0
for L, v in groups.items():
    if len(v) > 1:
        pchance *= sum((c / 97.0) ** len(v) for c in q.values())
inj = math.prod((26 - k) / 26 for k in range(len(groups)))
print(f"   P(random permutation FEASIBLE-BIJECTIVE), from K4's own letter")
print(f"   frequencies              : {pchance * inj:.3e}")
print()

closed_form_failures = TR.selftest()
print(f"## Closed-form self-test against reference implementations: "
      f"{'PASS' if not closed_form_failures else 'FAIL'} ({len(closed_form_failures)} failures)")
assert not closed_form_failures
print()


# ---------------------------------------------------------------- exact decision, vectorised
def decide_block(ctidx):
    """ctidx: (M,24) ciphertext indices. -> (feasible_function, feasible_bijective) masks."""
    letters = CTA[ctidx]
    ok = np.ones(letters.shape[0], dtype=bool)
    for g in GROUPS:
        ok &= np.all(letters[:, g] == letters[:, g[0]][:, None], axis=1)
    reps = np.sort(letters[:, REPS], axis=1)
        # injective iff no two representative images coincide
    inj_mask = np.all(np.diff(reps, axis=1) != 0, axis=1)
    return ok, ok & inj_mask


def decide_single(perm_read_order, orientation):
    """Pure-python decision for one permutation given as read-order -> plaintext index."""
    if orientation == "A":
        pos = {j: i for i, j in enumerate(perm_read_order)}      # plaintext j -> ct index
    else:
        pos = {perm_read_order[i]: None for i in range(TR.N)}
        inv = {}
        for i, j in enumerate(perm_read_order):
            inv[i] = j
        # orientation B: C[i] = S(P[t(i)]) with t(i) = perm_read_order[i]
        pos = {}
        for i, j in enumerate(perm_read_order):
            pos[j] = i
        # identical to A for a read-order representation; kept explicit for clarity
    smap, used = {}, {}
    for j in JP:
        p, c = CRIB[j], CT[pos[j]]
        if smap.setdefault(p, c) != c:
            return False, False, None
    bij = len(set(smap.values())) == len(smap)
    return True, bij, smap


# ---------------------------------------------------------------- controls
print("## Controls")
rng = random.Random(20260912)
ctrl = collections.Counter()
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def synth_ciphertext(read_order, S):
    """C[i] = S(P[sigma(i)]); read_order[i] = sigma(i). Independent arithmetic."""
    PT = ["Q"] * TR.N
    for j, p in CRIB.items():
        PT[j] = p
    return "".join(S[PT[read_order[i]]] for i in range(TR.N))


def crib_letters_under(read_order, ct):
    smap = {}
    pos = {j: i for i, j in enumerate(read_order)}
    for j in JP:
        p, c = CRIB[j], ct[pos[j]]
        if smap.setdefault(p, c) != c:
            return None, False
    return smap, len(set(smap.values())) == len(smap)


def columnar_read_order(w, key, bottom_up):
    """read_order[i] = plaintext index read i-th, from the reference implementation."""
    order = [None] * TR.N
    for j in range(TR.N):
        order[TR.columnar_forward(j, w, key, bottom_up)] = j
    return order


planted = []
for _ in range(20):                                   # F1 plants
    w = rng.randrange(2, 12)
    key = tuple(rng.sample(range(w), w))
    bu = rng.random() < 0.5
    planted.append(("F1", columnar_read_order(w, key, bu), (w, key, bu)))
for _ in range(12):                                   # F2 plants
    w = rng.randrange(2, 97)
    routes = TR.route_permutations(w)
    nm = rng.choice(sorted(routes))
    planted.append(("F2", routes[nm], (w, nm)))
for nm, seq in sorted(TR.engraved_routes().items()):   # F3 plants: all of them
    planted.append(("F3", seq, (nm,)))

for fam, order, label in planted:
    perm = list(ALPHA)
    rng.shuffle(perm)
    S = dict(zip(ALPHA, perm))
    ct = synth_ciphertext(order, S)
    smap, bij = crib_letters_under(order, ct)
    ctrl["planted_total"] += 1
    if smap is not None and bij and all(S[p] == smap[p] for p in smap):
        ctrl["planted_pass"] += 1
    # adversarial 1: corrupt one crib-constrained ciphertext character
    pos = {j: i for i, j in enumerate(order)}
    victim = pos[JP[0]]
    bad = list(ct)
    bad[victim] = ALPHA[(ALPHA.index(bad[victim]) + 13) % 26]
    smap2, _ = crib_letters_under(order, "".join(bad))
    ctrl["adv_corrupt_total"] += 1
    ctrl["adv_corrupt_pass"] += (smap2 is None)
    # adversarial 2: a permutation that differs ON THE CONSTRAINED SLOTS must not
    # reproduce the planted substitution. A swap of two unconstrained slots changes
    # nothing the cribs can see, so the swap is chosen between two crib slots whose
    # ciphertext letters actually differ - otherwise the control tests nothing.
    cand = [(j1, j2) for j1 in JP for j2 in JP
            if j1 < j2 and ct[pos[j1]] != ct[pos[j2]]]
    if cand:
        j1, j2 = cand[rng.randrange(len(cand))]
        other = list(order)
        other[pos[j1]], other[pos[j2]] = other[pos[j2]], other[pos[j1]]
        smap3, bij3 = crib_letters_under(other, ct)
        ctrl["adv_wrongperm_total"] += 1
        ctrl["adv_wrongperm_pass"] += (smap3 is None or not bij3
                                       or any(S[p] != smap3[p] for p in smap3))
# non-injective control
order = TR.engraved_routes()["eng_cols_down"]
collapse = {ch: ("A" if ch in "EIOU" else ch) for ch in ALPHA}
ct = synth_ciphertext(order, collapse)
smap, bij = crib_letters_under(order, ct)
ctrl["noninj_found_as_function"] = int(smap is not None)
ctrl["noninj_rejected_as_bijection"] = int(smap is not None and not bij)

print(f"   planted positives      : {ctrl['planted_pass']}/{ctrl['planted_total']}"
      " detected, substitution recovered on every constrained letter")
print(f"   adversarial corruption : {ctrl['adv_corrupt_pass']}/{ctrl['adv_corrupt_total']} rejected")
print(f"   adversarial wrong perm : {ctrl['adv_wrongperm_pass']}/{ctrl['adv_wrongperm_total']} rejected")
print(f"   non-injective plant    : found as FEASIBLE-FUNCTION="
      f"{bool(ctrl['noninj_found_as_function'])}, "
      f"rejected as FEASIBLE-BIJECTIVE={bool(ctrl['noninj_rejected_as_bijection'])}")
assert ctrl["planted_pass"] == ctrl["planted_total"]
assert ctrl["adv_corrupt_pass"] == ctrl["adv_corrupt_total"]
assert ctrl["adv_wrongperm_pass"] == ctrl["adv_wrongperm_total"]
assert ctrl["noninj_found_as_function"] and ctrl["noninj_rejected_as_bijection"]
print()

# ---------------------------------------------------------------- F1 exhaustive sweep
WIDTHS = tuple(range(2, 12))
print(f"## F1  keyed columnar transposition, widths {WIDTHS[0]}-{WIDTHS[-1]}, ALL column orders")
t0 = time.time()
f1 = {"cases": 0, "feasible_function": 0, "feasible_bijective": 0, "hits": [], "per_width": {}}
for w in WIDTHS:
    wcases = 0
    for block in TR.perm_blocks(w):
        for bu in (False, True):
            for orient in ("A", "B"):
                idx = TR.crib_ct_indices(block, w, JP, bu, orient)
                fn, bj = decide_block(idx)
                wcases += block.shape[0]
                f1["cases"] += block.shape[0]
                f1["feasible_function"] += int(fn.sum())
                f1["feasible_bijective"] += int(bj.sum())
                if fn.any():
                    for m in np.nonzero(fn)[0][:50]:
                        f1["hits"].append({"family": "F1", "w": w,
                                           "key": [int(x) for x in block[m]],
                                           "bottom_up": bu, "orientation": orient,
                                           "bijective": bool(bj[m])})
    f1["per_width"][w] = wcases
    print(f"   w={w:<3} {wcases:>12,} cases   cumulative feasible: "
          f"function {f1['feasible_function']}, bijective {f1['feasible_bijective']}"
          f"   [{time.time() - t0:.0f}s]")
print(f"   F1 total cases {f1['cases']:,} in {time.time() - t0:.0f}s")
print()

# ---------------------------------------------------------------- F2 and F3
print("## F2  unkeyed rectangle routes, all widths 2-96   /   F3  ragged engraving-grid routes")
small = {"F2": {}, "F3": {}}
seen_perms = {}
dupes = 0
f23 = {"cases": 0, "feasible_function": 0, "feasible_bijective": 0, "hits": []}
for fam, gen in (("F2", ((w, TR.route_permutations(w)) for w in range(2, 97))),
                 ("F3", [(None, TR.engraved_routes())])):
    for w, routes in gen:
        for nm, order in sorted(routes.items()):
            for orient in ("A", "B"):
                seq = order if orient == "A" else [order.index(i) for i in range(TR.N)]
                key = tuple(seq)
                f23["cases"] += 1
                if key in seen_perms:
                    dupes += 1
                    continue
                seen_perms[key] = (fam, w, nm, orient)
                ok, bij, smap = decide_single(seq, "A")
                f23["feasible_function"] += int(ok)
                f23["feasible_bijective"] += int(ok and bij)
                if ok:
                    f23["hits"].append({"family": fam, "w": w, "route": nm,
                                        "orientation": orient, "bijective": bool(bij),
                                        "substitution": smap})
print(f"   declared cases {f23['cases']:,}; distinct permutations {len(seen_perms):,}; "
      f"duplicates deduplicated {dupes:,}")
print(f"   feasible: function {f23['feasible_function']}, bijective {f23['feasible_bijective']}")
print("   F3 is the independent formalisation of the uncommitted supervisory scratch")
print("   result: elementary routes on K4's real ragged engraving grid.")
print()

# ---------------------------------------------------------------- result
total = f1["cases"] + len(seen_perms)
tf = f1["feasible_function"] + f23["feasible_function"]
tb = f1["feasible_bijective"] + f23["feasible_bijective"]
print("## RESULT")
print(f"   declared cases decided     : {total:,}")
print(f"   FEASIBLE-BIJECTIVE         : {tb}")
print(f"   FEASIBLE-FUNCTION          : {tf}")
print(f"   expected chance survivors  : {total * pchance * inj:.3e}")
print()
if tb == 0 and tf == 0:
    print("   NEGATIVE. K4 is not any monoalphabetic substitution composed with any")
    print("   transposition in the declared family. Because the substitution was decided")
    print("   exactly rather than enumerated, this covers every mixed, keyword and")
    print("   reciprocal alphabet, and every non-injective letter map, at once.")
    print()
    print("   This replaces a statistic with a decision. K4's index of coincidence")
    print("   (0.03608) already disfavoured this whole architecture at about z = -3.9,")
    print("   but docs/codex-audit.md finding 7 is right that a low IoC does not prove no")
    print("   English plaintext exists. The cribs now settle it inside this family without")
    print("   any distributional assumption.")
else:
    print("   SURVIVORS RECORDED. Not a solution and not tuned around: a feasible case")
    print("   fixes at most 13 of 26 substitution letters and says nothing about the")
    print("   other 84 plaintext positions. Any follow-up needs a new preregistration.")
print()
print("## Scope of the elimination")
print("   Exactly the declared family and the public cribs. NOT eliminated: keyed")
print("   columnar widths >= 12, keyed routes outside the family, double transposition,")
print("   any polyalphabetic composition (a free per-position alphabet is vacuous here -")
print("   EXP-011), fractionation, or substitution with nulls or length change.")
print("   Case counts are not counts of independent tests.")

out_dir = os.path.join(REPO_ROOT, "results", "exp033")
os.makedirs(out_dir, exist_ok=True)
summary = {"experiment": "EXP-033", "ciphertext_sha256": k4.sha256,
           "model": "C[i] = S(P[sigma(i)]), S any A-Z -> A-Z decided exactly",
           "prereg": "docs/exp032-033-preregistration.md",
           "crib_positions": JP, "crib_letters": PL,
           "groups": {L: v for L, v in groups.items()},
           "p_chance_bijective": pchance * inj,
           "F1": {k: v for k, v in f1.items() if k != "hits"},
           "F2_F3": {k: v for k, v in f23.items() if k != "hits"},
           "distinct_small_permutations": len(seen_perms), "deduplicated": dupes,
           "total_cases": total, "feasible_function": tf, "feasible_bijective": tb,
           "hits": f1["hits"] + f23["hits"], "controls": dict(ctrl),
           "closed_form_selftest_failures": len(closed_form_failures)}
with open(os.path.join(out_dir, "summary.json"), "w") as fh:
    json.dump(summary, fh, indent=1, default=str)
print(f"\n   wrote results/exp033/summary.json")
