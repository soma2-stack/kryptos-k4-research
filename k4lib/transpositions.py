"""Declared transposition families for EXP-033.

A transposition is represented by the map `t : plaintext index -> ciphertext index`.
Two orientations of the same map are tested, because we do not know which way round
Sanborn would have worked it:

    A   C[t(j)] = S(P[j])    so the ciphertext letter constraining crib j is CT[t(j)]
    B   C[i]    = S(P[t(i)]) so the ciphertext letter constraining crib j is CT[t^-1(j)]

For keyed columnar transposition both directions have a closed form, which is what makes
an exhaustive sweep over every column order affordable. The closed forms are checked
against explicit grid simulation by `selftest()` and, independently, by the verifier.
"""

import numpy as np

N = 97


def column_lengths(w, n=N):
    """Number of cells in each column when n letters are written by rows into w columns."""
    return np.array([(n - c + w - 1) // w for c in range(w)], dtype=np.int64)


def columnar_forward(j, w, key, bottom_up=False, n=N):
    """Reference implementation, one index at a time: plaintext j -> ciphertext i."""
    L = column_lengths(w, n)
    r, c = divmod(j, w)
    rank = list(key).index(c)
    off = sum(int(L[key[t]]) for t in range(rank))
    within = (int(L[c]) - 1 - r) if bottom_up else r
    return off + within


def columnar_inverse(j, w, key, bottom_up=False, n=N):
    """Reference implementation: the i with t(i) == j."""
    L = column_lengths(w, n)
    off, rank = 0, None
    for t in range(w):
        ln = int(L[key[t]])
        if off <= j < off + ln:
            rank = t
            break
        off += ln
    c = key[rank]
    within = j - off
    r = (int(L[c]) - 1 - within) if bottom_up else within
    return r * w + c


def grid_positions(w, n=N):
    """(row, col) of every plaintext index when written by rows into w columns."""
    return [(j // w, j % w) for j in range(n)]


# ------------------------------------------------------------------ permutation builders
def _perm_blocks(w, cap_block=400_000):
    """Yield numpy blocks covering ALL w! column orders, without materialising w! at once.

    Built by prepending each possible first column to every order of the rest, so only
    (w-1)! is ever held in memory.
    """
    import itertools
    if w <= 9:
        arr = np.array(list(itertools.permutations(range(w))), dtype=np.int8)
        for s in range(0, arr.shape[0], cap_block):
            yield arr[s:s + cap_block]
        return
    for head in range(w):
        rest = [c for c in range(w) if c != head]
        for sub in _perm_blocks(w - 1, cap_block):
            mapped = np.array(rest, dtype=np.int8)[sub]
            block = np.empty((mapped.shape[0], w), dtype=np.int8)
            block[:, 0] = head
            block[:, 1:] = mapped
            yield block


def perm_blocks(w, cap_block=400_000):
    return _perm_blocks(w, cap_block)


def crib_ct_indices(keys, w, crib_positions, bottom_up, orientation, n=N):
    """Vectorised closed form: ciphertext index constraining each crib position.

    keys: (M, w) int array of column orders. Returns (M, len(crib_positions)) int32.
    """
    M = keys.shape[0]
    L = column_lengths(w, n)
    Lk = L[keys]                                     # (M, w) length of each read column
    cum = np.zeros((M, w + 1), dtype=np.int64)
    np.cumsum(Lk, axis=1, out=cum[:, 1:])
    J = np.asarray(crib_positions, dtype=np.int64)

    if orientation == "A":
        rank = np.empty((M, w), dtype=np.int64)      # rank[m, c] = read order of column c
        rows = np.arange(M)[:, None]
        rank[rows, keys.astype(np.int64)] = np.arange(w, dtype=np.int64)[None, :]
        r, c = J // w, J % w
        t = rank[:, c]                               # (M, K)
        off = np.take_along_axis(cum[:, :w], t, axis=1)
        within = (L[c][None, :] - 1 - r[None, :]) if bottom_up else np.broadcast_to(r[None, :], (M, J.size))
        return (off + within).astype(np.int32)

    # orientation B: find the read slot containing j, then invert to a plaintext cell
    t = (cum[:, :w, None] <= J[None, None, :]).sum(axis=1) - 1      # (M, K)
    off = np.take_along_axis(cum[:, :w], t, axis=1)
    c = np.take_along_axis(keys.astype(np.int64), t, axis=1)
    within = J[None, :] - off
    Lc = L[c]
    r = (Lc - 1 - within) if bottom_up else within
    return (r * w + c).astype(np.int32)


# ------------------------------------------------------------------ unkeyed route family
def _write_rows(w, n=N):
    h = (n + w - 1) // w
    grid = [[None] * w for _ in range(h)]
    for j in range(n):
        grid[j // w][j % w] = j
    return grid, h


def route_permutations(w, n=N):
    """Unkeyed rectangle routes: write by rows, read by a named route.

    Returns {name: list mapping read order -> plaintext index}.
    """
    grid, h = _write_rows(w, n)
    out = {}

    def cells(seq):
        return [x for x in seq if x is not None]

    out["cols_lr"] = cells(grid[r][c] for c in range(w) for r in range(h))
    out["cols_rl"] = cells(grid[r][c] for c in range(w - 1, -1, -1) for r in range(h))
    out["cols_boustro"] = cells(
        grid[r][c] for c in range(w)
        for r in (range(h) if c % 2 == 0 else range(h - 1, -1, -1)))
    out["rows_boustro"] = cells(
        grid[r][c] for r in range(h)
        for c in (range(w) if r % 2 == 0 else range(w - 1, -1, -1)))
    out["rows_rl"] = cells(grid[r][c] for r in range(h) for c in range(w - 1, -1, -1))
    out["rows_bottom"] = cells(grid[r][c] for r in range(h - 1, -1, -1) for c in range(w))
    # diagonals
    out["diag_down"] = cells(grid[r][c] for s in range(h + w) for r in range(h)
                             for c in [s - r] if 0 <= s - r < w)
    out["diag_up"] = cells(grid[r][c] for s in range(h + w) for r in range(h - 1, -1, -1)
                           for c in [s - r] if 0 <= s - r < w)
    # spirals: four corners x two rotational senses
    for name, (r0, c0, clockwise) in {
            "spiral_tl_cw": (0, 0, True), "spiral_tl_ccw": (0, 0, False),
            "spiral_tr_cw": (0, w - 1, True), "spiral_tr_ccw": (0, w - 1, False),
            "spiral_bl_cw": (h - 1, 0, True), "spiral_bl_ccw": (h - 1, 0, False),
            "spiral_br_cw": (h - 1, w - 1, True), "spiral_br_ccw": (h - 1, w - 1, False)}.items():
        seen, seq, r, c = set(), [], r0, c0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] if clockwise else [(1, 0), (0, 1), (-1, 0), (0, -1)]
        if c0 == w - 1:
            dirs = dirs[::-1] if clockwise else dirs
        d = 0
        for _ in range(h * w * 4):
            if (r, c) not in seen and 0 <= r < h and 0 <= c < w:
                seen.add((r, c))
                seq.append(grid[r][c])
            if len(seen) == h * w:
                break
            nr, nc = r + dirs[d][0], c + dirs[d][1]
            if not (0 <= nr < h and 0 <= nc < w) or (nr, nc) in seen:
                d = (d + 1) % 4
                nr, nc = r + dirs[d][0], c + dirs[d][1]
                if not (0 <= nr < h and 0 <= nc < w) or (nr, nc) in seen:
                    break
            r, c = nr, nc
        seq = cells(seq)
        if len(seq) == n:
            out[name] = seq
    return {k: v for k, v in out.items() if len(v) == n}


# ------------------------------------------------------------------ ragged engraving grid
ENGRAVED_ROWS = ((25, 0, 4, 28), (26, 4, 35, 1), (27, 35, 66, 1), (28, 66, 97, 1))


def engraved_cells():
    """(row, column) of every K4 index under the corrected NSA geometry."""
    out = {}
    for row, lo, hi, first_col in ENGRAVED_ROWS:
        for j in range(lo, hi):
            out[j] = (row, first_col + (j - lo))
    return out


def engraved_routes():
    """Routes over K4's actual ragged engraving grid (EXP-033 subfamily F3).

    This is the independent formalisation of the uncommitted supervisory scratch result:
    elementary row/column routes on the real geometry rather than on a tidy rectangle.
    """
    cells = engraved_cells()
    by_col = {}
    for j, (row, col) in cells.items():
        by_col.setdefault(col, []).append((row, j))
    for col in by_col:
        by_col[col].sort()
    cols = sorted(by_col)
    out = {}
    out["eng_cols_down"] = [j for c in cols for _, j in by_col[c]]
    out["eng_cols_up"] = [j for c in cols for _, j in reversed(by_col[c])]
    out["eng_cols_rl_down"] = [j for c in reversed(cols) for _, j in by_col[c]]
    out["eng_cols_boustro"] = [j for k, c in enumerate(cols)
                               for _, j in (by_col[c] if k % 2 == 0 else list(reversed(by_col[c])))]
    rows = {}
    for j, (row, col) in cells.items():
        rows.setdefault(row, []).append((col, j))
    for row in rows:
        rows[row].sort()
    rkeys = sorted(rows)
    out["eng_rows_rl"] = [j for r in rkeys for _, j in reversed(rows[r])]
    out["eng_rows_boustro"] = [j for k, r in enumerate(rkeys)
                               for _, j in (rows[r] if k % 2 == 0 else list(reversed(rows[r])))]
    out["eng_rows_bottom_up"] = [j for r in reversed(rkeys) for _, j in rows[r]]
    return {k: v for k, v in out.items() if sorted(v) == list(range(N))}


def selftest():
    """Closed forms must agree with the reference one-index-at-a-time implementations."""
    import itertools, random
    rng = random.Random(7)
    bad = []
    for w in (2, 3, 5, 7, 8, 11, 13):
        keys = [tuple(rng.sample(range(w), w)) for _ in range(6)]
        karr = np.array(keys, dtype=np.int8)
        J = list(range(0, N, 7)) + [96, 0, 1]
        for bu in (False, True):
            gotA = crib_ct_indices(karr, w, J, bu, "A")
            gotB = crib_ct_indices(karr, w, J, bu, "B")
            for m, key in enumerate(keys):
                for t, j in enumerate(J):
                    if gotA[m, t] != columnar_forward(j, w, key, bu):
                        bad.append(("A", w, key, j, bu))
                    if gotB[m, t] != columnar_inverse(j, w, key, bu):
                        bad.append(("B", w, key, j, bu))
        # t must be a bijection on 0..96
        for key in keys:
            for bu in (False, True):
                img = sorted(columnar_forward(j, w, key, bu) for j in range(N))
                if img != list(range(N)):
                    bad.append(("bijection", w, key, bu))
    return bad
