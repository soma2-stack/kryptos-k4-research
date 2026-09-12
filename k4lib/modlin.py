"""Exact linear algebra over Z_26, by CRT through GF(2) and GF(13).

Z_26 is not a field, so Gaussian elimination does not apply directly. But
26 = 2 * 13 with both factors prime, so a system A x = b (mod 26) is solvable
iff it is solvable mod 2 and mod 13, and its solution set is the CRT product of
the two. That gives *exact solution counts* rather than brute-force search, which
matters here: reporting "0 of 11,881,376 candidates fit" and reporting "the
solution space is empty" are the same fact, but only the second scales.

Any keystream model that is linear in its unknown parameters can be tested this
way: linear recurrences, polynomial progressions, segmented progressions,
periodic keys, and combinations of them.
"""


def _rref(rows, ncols, p):
    """Row-reduce `rows` (each length ncols+1, last entry = RHS) mod prime p."""
    rows = [r[:] for r in rows]
    pivots, r = [], 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(rows)) if rows[i][c] % p), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = pow(rows[r][c], p - 2, p)
        rows[r] = [(v * inv) % p for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] % p:
                f = rows[i][c]
                rows[i] = [(a - f * b) % p for a, b in zip(rows[i], rows[r])]
        pivots.append(c)
        r += 1
        if r == len(rows):
            break
    return rows, pivots, r


def solve_mod_p(A, b, p):
    """Return (particular, nullspace_basis) mod p, or None if inconsistent."""
    n = len(A[0]) if A else 0
    rows = [list(ai) + [bi] for ai, bi in zip(A, b)]
    rows, pivots, rank = _rref(rows, n, p)
    for i in range(rank, len(rows)):
        if all(v % p == 0 for v in rows[i][:n]) and rows[i][n] % p:
            return None
    part = [0] * n
    for i, c in enumerate(pivots):
        part[c] = rows[i][n] % p
    free = [c for c in range(n) if c not in pivots]
    basis = []
    for f in free:
        v = [0] * n
        v[f] = 1
        for i, c in enumerate(pivots):
            v[c] = (-rows[i][f]) % p
        basis.append(v)
    return part, basis


def count_solutions_mod26(A, b):
    """Number of x in Z_26^n with A x = b (mod 26). 0 means inconsistent."""
    n = len(A[0]) if A else 0
    total = 1
    for p in (2, 13):
        r = solve_mod_p([[a % p for a in row] for row in A], [v % p for v in b], p)
        if r is None:
            return 0
        total *= p ** len(r[1])
    return total


def solutions_mod26(A, b, limit=None):
    """Enumerate solutions mod 26 via CRT over the mod-2 and mod-13 solution sets."""
    n = len(A[0]) if A else 0
    parts = {}
    for p in (2, 13):
        r = solve_mod_p([[a % p for a in row] for row in A], [v % p for v in b], p)
        if r is None:
            return []
        parts[p] = r
    out = []

    def expand(p):
        part, basis = parts[p]
        acc = [part]
        for v in basis:
            acc = [[(x + t * y) % p for x, y in zip(s, v)] for s in acc for t in range(p)]
        return acc

    s2, s13 = expand(2), expand(13)
    # CRT: x = 13*inv13_2*a + 2*inv2_13*b  (mod 26); 13*1 = 13, 2*7 = 14
    for a in s2:
        for c in s13:
            out.append([(13 * x + 14 * y) % 26 for x, y in zip(a, c)])
            if limit and len(out) >= limit:
                return out
    return out


def rank_mod_p(A, p):
    if not A:
        return 0
    n = len(A[0])
    rows = [[a % p for a in row] + [0] for row in A]
    _, _, r = _rref(rows, n, p)
    return r


def chance_solvable(A):
    """P(a system with this coefficient matrix is solvable for a uniformly random RHS).

    This is the degrees-of-freedom penalty. A model with more free parameters than
    equations has chance 1 and its "fit" means nothing. Exact, not asymptotic:
    for each prime factor p of 26 the image of A has size p^rank, out of p^n_eq
    possible right-hand sides.
    """
    m = len(A)
    if m == 0:
        return 1.0
    q = 1.0
    for p in (2, 13):
        q *= p ** (rank_mod_p(A, p) - m)
    return q
