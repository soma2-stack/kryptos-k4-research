"""Checkpoint AP -- frontier census + the crib cycle-rank theorem.

Two jobs, both exact and both independent of any experiment module:

 1. THEOREM.  For any family whose crib equations are affine over Z26 with at
    most two unknowns per crib, the number of independent constraints the 24
    public crib letters impose is a purely GRAPH-THEORETIC invariant of a
    signed, anchored multigraph.  We state the invariant, compute it
    combinatorially, and check it against exact linear algebra over Z26
    (CRT through GF(2) and GF(13)) on every family below.

 2. CENSUS.  For each surviving architecture, report exact free parameters,
    which of them the cribs reach, d_eff, N, and log26(N)+d_eff.

Nothing here scores plaintext and nothing is fitted.
"""
import sys, os, json, math, itertools, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load
from k4lib.modlin import rank_mod_p

k4 = load()
CRIBS = sorted(i for i, _, _ in k4.crib_positions())
E = len(CRIBS)
assert E == 24, E
assert CRIBS == list(range(21, 34)) + list(range(63, 74)), CRIBS

# --------------------------------------------------------------------------
# exact rank over Z26 via CRT.  Z26 is not a field, so "rank" is reported as
# the pair (rank mod 2, rank mod 13).  d_eff is the max, which is the one that
# bounds the number of surviving parameter assignments from above.
# --------------------------------------------------------------------------
def z26_ranks(A):
    if not A or not A[0]:
        return (0, 0)
    return (rank_mod_p(A, 2), rank_mod_p(A, 13))


# --------------------------------------------------------------------------
# THE GRAPH INVARIANT
#
# Each crib i contributes  sum_{v in S_i} eps_{i,v} * u_v = c_i  with |S_i|<=2.
# Build a multigraph H on the unknowns actually appearing:
#   * |S_i| = 2 -> an edge {u,v} carrying sign sigma = -eps_u*eps_v
#   * |S_i| = 1 -> the vertex is ANCHORED (pinned to a known value)
#   * |S_i| = 0 -> the crib is a free-standing constraint (contributes to mu)
#
# Claim (verified below):  d_eff = sum over components K of
#     |K|      if K is anchored OR unbalanced
#     |K| - 1  otherwise
# and the independent-constraint count is mu = E - d_eff.
#
# A component is UNBALANCED when some cycle in it has sign product -1: such a
# cycle pins an absolute value rather than only a difference, which is exactly
# what an anchor does.  Balance is invisible mod 2 (where -1 == 1), which is
# why the theorem is stated over GF(13) and the mod-2 rank is reported
# separately rather than silently averaged.
# --------------------------------------------------------------------------
def graph_invariant(n_unknowns, rows):
    """rows: list of {var: eps}.  Returns (d_eff_pred, mu_pred, detail)."""
    parent = list(range(n_unknowns))
    # potential[v] in {+1,-1}: the switching sign relating v to its root
    pot = [1] * n_unknowns

    def find(v):
        """Return (root, sign) with value[v] = sign * value[root].
        No path compression: the graphs here have at most a few dozen vertices,
        and a buggy signed compression is a worse trade than a linear walk."""
        root, s = v, 1
        while parent[root] != root:
            s *= pot[root]
            root = parent[root]
        return root, s

    touched = set()
    anchored_root = set()
    unbalanced_root = set()
    free_constraints = 0

    for r in rows:
        vs = sorted(r)
        touched.update(vs)
        if len(vs) == 0:
            free_constraints += 1
        elif len(vs) == 1:
            root, _ = find(vs[0])
            anchored_root.add(root)
        else:
            u, v = vs
            eu, ev = r[u], r[v]
            sigma = -eu * ev
            ru, su = find(u)
            rv, sv = find(v)
            if ru == rv:
                # cycle: balanced iff the implied sign agrees
                if su * sv != sigma:
                    unbalanced_root.add(ru)
            else:
                parent[rv] = ru
                pot[rv] = su * sv * sigma
                if rv in anchored_root:
                    anchored_root.discard(rv); anchored_root.add(ru)
                if rv in unbalanced_root:
                    unbalanced_root.discard(rv); unbalanced_root.add(ru)

    comps = collections.defaultdict(list)
    for v in touched:
        comps[find(v)[0]].append(v)

    d_eff = 0
    for root, members in comps.items():
        special = (root in anchored_root) or (root in unbalanced_root)
        d_eff += len(members) if special else len(members) - 1
    mu = E - d_eff
    return d_eff, mu, {"touched": len(touched), "components": len(comps),
                       "anchored": len(anchored_root),
                       "unbalanced": len(unbalanced_root),
                       "free_constraints": free_constraints}


def to_matrix(n, rows):
    return [[r.get(v, 0) % 26 for v in range(n)] for r in rows]


# --------------------------------------------------------------------------
# FAMILY BUILDERS.  Each returns (n_unknowns, rows) where rows[i] is the crib
# equation for CRIBS[i] as {unknown_index: coefficient in {+1,-1}}.
# --------------------------------------------------------------------------
def fam_single_periodic(p, beaufort_positions=()):
    """One periodic mask of period p.  P[i] = C[i] - k[i mod p]."""
    rows = []
    for i in CRIBS:
        eps = -1 if i in beaufort_positions else 1
        rows.append({i % p: eps})
    return p, rows


def fam_two_mask_sandwich(p, q, perm):
    """M2 . pi . M1 with periodic additive masks of periods p and q.

    Crib at plaintext position i passes through M1 slot (i mod p) and lands at
    ciphertext position perm[i], which uses M2 slot (perm[i] mod q).
    Unknowns: 0..p-1 are M1 slots, p..p+q-1 are M2 slots.
    """
    rows = []
    for i in CRIBS:
        a = i % p
        b = p + (perm[i] % q)
        rows.append({a: 1, b: 1} if a != b else {a: 2})
    return p + q, rows


def fam_monoalphabetic_after_perm(perm):
    """S . pi with S a FREE A-Z -> A-Z map: 26 unknowns, one per plaintext letter."""
    crib_letter = {i: p for i, p, _ in k4.crib_positions()}
    rows = []
    for i in CRIBS:
        rows.append({ord(crib_letter[i]) - 65: 1})
    return 26, rows


def fam_one_tap_feedback(lag, n_chains_note=None):
    """Propagating one-tap autokey: chains by residue class of the lag."""
    # chain id = i mod lag; the single unknown per chain is its primer.
    rows = []
    chains = {}
    for i in CRIBS:
        c = i % lag
        if c not in chains:
            chains[c] = len(chains)
        rows.append({chains[c]: 1})
    return len(chains), rows


def fam_progressive_key(period, prog):
    """Periodic mask whose slot value advances by `prog` each full cycle:
    k_eff[i] = k[i mod period] + prog * (i // period).  The progression is a
    KNOWN constant, so it moves to the right-hand side and the unknowns are
    still exactly the `period` slots.  Included to show that a deterministic
    irregular schedule built on a known rule changes nothing structural."""
    return fam_single_periodic(period)


# --------------------------------------------------------------------------
# PART 1 -- verify the graph invariant against exact linear algebra
# --------------------------------------------------------------------------
def check(label, n, rows, expect_mu=None):
    d_pred, mu_pred, detail = graph_invariant(n, rows)
    A = to_matrix(n, rows)
    r2, r13 = z26_ranks(A)
    ok = (d_pred == r13)
    flag = "OK " if ok else "MISMATCH"
    note = "" if r2 == r13 else f"  (mod2 rank {r2} differs: sign-blind)"
    extra = ""
    if expect_mu is not None:
        extra = f"  [historical mu={expect_mu} {'match' if expect_mu == mu_pred else 'DIFFER'}]"
    print(f"   {flag} {label:<46} d_eff={d_pred:<3} mu={mu_pred:<3} "
          f"rank13={r13:<3} comps={detail['components']:<3}"
          f"{note}{extra}")
    return ok, d_pred, mu_pred


def main():
    print("# Checkpoint AP -- crib cycle-rank theorem and frontier census")
    print(f"ciphertext sha256 {k4.sha256}")
    print(f"crib positions: {CRIBS[0]}..{CRIBS[12]} and {CRIBS[13]}..{CRIBS[-1]}  (E={E})\n")

    failures = []
    print("## Part 1 -- graph invariant vs exact rank over Z26")
    print("   predicted d_eff must equal the exact GF(13) rank in every case\n")

    print("### single periodic mask (reproduces the known blind spot)")
    for p in list(range(2, 30)):
        ok, d, mu = check(f"period p={p}", *fam_single_periodic(p))
        if not ok:
            failures.append(f"periodic p={p}")

    print("\n### single periodic mask, mixed Vigenere/Beaufort signs (unbalanced cycles)")
    for p in (5, 8, 12):
        bp = set(CRIBS[::2])
        ok, d, mu = check(f"period p={p}, alternating sign", *fam_single_periodic(p, bp))
        if not ok:
            failures.append(f"signed periodic p={p}")

    print("\n### free monoalphabetic map behind a permutation (EXP-033 shape)")
    ok, d, mu = check("S free on A-Z, any fixed pi", *fam_monoalphabetic_after_perm(None))
    if not ok:
        failures.append("mono")

    print("\n### one-tap propagating feedback (reproduces the crib-span law)")
    for lag in (1, 3, 7, 13, 21, 25, 40):
        ok, d, mu = check(f"lag={lag}", *fam_one_tap_feedback(lag))
        if not ok:
            failures.append(f"feedback lag={lag}")

    print("\n### two-mask sandwich M2.pi.M1, identity pi")
    ident = list(range(97))
    for (p, q) in ((8, 10), (3, 9), (5, 7), (11, 13), (24, 25)):
        ok, d, mu = check(f"p={p}, q={q}, pi=identity",
                          *fam_two_mask_sandwich(p, q, ident))
        if not ok:
            failures.append(f"sandwich {p},{q}")

    print("\n### two-mask sandwich, affine pi (a=7,b=3) -- EXP-043 shape")
    aff = [(7 * i + 3) % 97 for i in range(97)]
    for (p, q) in ((3, 9), (8, 10), (11, 13)):
        ok, d, mu = check(f"p={p}, q={q}, pi=7i+3 mod 97",
                          *fam_two_mask_sandwich(p, q, aff))
        if not ok:
            failures.append(f"affine sandwich {p},{q}")

    print("\n### RANDOMISED STRESS TEST -- exercises the unbalanced-cycle branch")
    import random
    rng = random.Random(20260921)
    unb_seen = bal_seen = 0
    stress_fail = 0
    for trial in range(4000):
        n = rng.randrange(2, 12)
        rows = []
        for _ in range(E):
            k = rng.choice((1, 1, 2, 2, 2))
            vs = rng.sample(range(n), min(k, n))
            rows.append({v: rng.choice((1, -1)) for v in vs})
        d_pred, mu_pred, detail = graph_invariant(n, rows)
        r13 = rank_mod_p(to_matrix(n, rows), 13)
        if detail["unbalanced"]:
            unb_seen += 1
        else:
            bal_seen += 1
        if d_pred != r13:
            stress_fail += 1
            if stress_fail <= 3:
                print(f"   MISMATCH n={n} pred={d_pred} rank13={r13} {detail}")
    # NEGATIVE CONTROL: the sign-blind formula (d_eff = |V| - components,
    # ignoring balance) must FAIL, otherwise the balance correction is
    # decoration rather than content.
    naive_fail = 0
    for trial in range(4000):
        n = rng.randrange(2, 12)
        rows = []
        for _ in range(E):
            k = rng.choice((1, 1, 2, 2, 2))
            vs = rng.sample(range(n), min(k, n))
            rows.append({v: rng.choice((1, -1)) for v in vs})
        d_pred, _, detail = graph_invariant(n, rows)
        naive = detail["touched"] - detail["components"]
        if naive != rank_mod_p(to_matrix(n, rows), 13):
            naive_fail += 1
    print(f"   negative control: the sign-blind |V|-c formula is wrong in"
          f" {naive_fail}/4,000 of the same shape -- balance is load-bearing")
    if naive_fail == 0:
        failures.append("negative control did not fire")

    print(f"   4,000 random signed systems: {stress_fail} mismatches"
          f"   (components with an unbalanced cycle occurred in {unb_seen} trials,"
          f" all-balanced in {bal_seen})")
    if stress_fail:
        failures.append("randomised stress test")

    print(f"\n   graph-invariant agreement: "
          f"{'ALL CASES AGREE' if not failures else 'FAILURES: ' + ', '.join(failures)}")
    return failures




# --------------------------------------------------------------------------
# PART 2 -- the census
# --------------------------------------------------------------------------
def budget(N, d_eff):
    return math.log(N, 26) + d_eff if N > 0 else float("inf")


def census():
    from k4lib import transpositions as TR
    print("\n\n## Part 2 -- frontier census")
    print("   a family can discriminate only if log26(N) + d_eff < 24,")
    print("   equivalently log26(N) < mu = 24 - d_eff.\n")

    rows_out = []

    # ---- Area 1: engraved-geometry routes inside a two-mask sandwich -----
    print("### Area 1 -- non-affine pi (engraved-geometry routes) in M2.pi.M1")
    eng = TR.engraved_routes()
    perms = {}
    for nm, order in sorted(eng.items()):
        perms[nm + "/A"] = order
        inv = [0] * 97
        for k_, v in enumerate(order):
            inv[v] = k_
        perms[nm + "/B"] = inv
    print(f"   independently declared pi corpus: {len(eng)} engraved routes"
          f" x 2 orientations = {len(perms)}")
    best = []
    for (p, q) in itertools.product(range(1, 15), repeat=2):
        if p > q:
            continue
        ds = []
        for nm, perm in perms.items():
            n, rws = fam_two_mask_sandwich(p, q, perm)
            d, mu, _ = graph_invariant(n, rws)
            ds.append(d)
        dmax = max(ds)
        # N = routes x orientations x 12 conventions x this (p,q)
        N = len(perms) * 12
        b = budget(N, dmax)
        best.append((b, p, q, dmax, N))
    best.sort()
    for b, p, q, d, N in best[:8]:
        print(f"   p={p:<3} q={q:<3} worst d_eff={d:<3} N={N:<5}"
              f" log26N={math.log(N, 26):.2f}  budget={b:.2f}"
              f"  {'DISCRIMINATING' if b < 24 else 'blind'}")
    n_ok = sum(1 for b, *_ in best if b < 24)
    print(f"   {n_ok} of {len(best)} (p,q) pairs with p<=q<=14 are discriminating")
    rows_out.append(("A1 engraved-route sandwich", min(b for b, *_ in best), n_ok > 0))

    # ---- Area 2: structured non-shift combiners --------------------------
    print("\n### Area 2 -- small rule-generated non-shift combiners")
    # affine combiner C = a*P + k[i mod p], a in the 12 units of Z26.
    # a is a GLOBAL unknown reached by every crib, so it is one extra vertex
    # joined to every crib edge -- it cannot be erased.
    crib_letter = {i: pl for i, pl, _ in k4.crib_positions()}
    for p in (5, 8, 10, 13):
        # unknowns: 0 = a, 1..p = slots.  crib: a*P_i + k_r = C_i
        # P_i is KNOWN, so the coefficient on `a` is a known constant, not +-1;
        # the two-unknown graph theorem needs +-1, so fall back to exact rank.
        A = []
        for i in CRIBS:
            r = [0] * (1 + p)
            r[0] = (ord(crib_letter[i]) - 65) % 26
            r[1 + (i % p)] = 1
            A.append(r)
        r13 = rank_mod_p(A, 13)
        N = 12 * 12          # 12 multipliers x 12 committed conventions
        b = budget(N, r13)
        print(f"   affine combiner a*P+k, p={p:<3} d_eff={r13:<3} N={N:<5}"
              f" budget={b:.2f}  {'DISCRIMINATING' if b < 24 else 'blind'}"
              f"   [motivation: none in the Kryptos record]")

    # ---- Area 4: deterministic irregular schedules -----------------------
    print("\n### Area 4 -- deterministic irregular schedules")
    print("   Reduction: for k_eff[i] = k[s(i)] + g(i) with s and g KNOWN, the")
    print("   additive g moves to the right-hand side, so d_eff depends only on")
    print("   the partition s induces on the 24 crib positions.")
    schedules = {}
    schedules["periodic p=13"] = lambda i: i % 13
    schedules["progressive p=13 (+1/cycle)"] = lambda i: i % 13
    schedules["triangular i(i+1)/2 mod 13"] = lambda i: (i * (i + 1) // 2) % 13
    schedules["squares i^2 mod 13"] = lambda i: (i * i) % 13
    schedules["Fibonacci-indexed mod 13"] = None
    fib = [0, 1]
    while len(fib) < 100:
        fib.append(fib[-1] + fib[-2])
    schedules["Fibonacci-indexed mod 13"] = lambda i: fib[i] % 13
    schedules["row-structured (4/31/31/31)"] = lambda i: (
        0 if i < 4 else 1 + (i - 4) // 31)
    for nm, s in schedules.items():
        blocks = len(set(s(i) for i in CRIBS))
        rws = [{s(i): 1} for i in CRIBS]
        d, mu, _ = graph_invariant(max(s(i) for i in CRIBS) + 1, rws)
        print(f"   {nm:<34} crib blocks={blocks:<3} d_eff={d:<3} mu={mu:<3}"
              f"  max log26(N) affordable = {mu}")
    return rows_out


if __name__ == "__main__":
    f = main()
    census()
    sys.exit(1 if f else 0)
