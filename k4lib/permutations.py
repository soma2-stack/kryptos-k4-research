"""Transposition families over the 97 K4 positions.

97 is prime, so every map i -> (a*i + b) mod 97 with a != 0 is a bijection.
That makes the affine family *complete and finite*: 96 * 97 = 9312 permutations,
enumerable with no sampling and no free parameters left over. It contains every
decimation and rotation of the text and is closed under inversion and
composition. Rectangular routes are a separate, differently-shaped family and
are generated alongside it.

A permutation is represented as a list `perm` of length 97 where `perm[i]` is
the ciphertext index paired with plaintext position i.
"""

from math import gcd

N = 97


def affine_family():
    """Yield (label, perm) for all 9312 affine index maps mod 97."""
    for a in range(1, N):
        for b in range(N):
            yield f"affine a={a} b={b}", [(a * i + b) % N for i in range(N)]


def _grid(width, boustrophedon):
    """Row-major fill of 97 cells into rows of `width`; returns rows of indices."""
    rows, idx = [], 0
    while idx < N:
        row = list(range(idx, min(idx + width, N)))
        idx += width
        rows.append(row)
    if boustrophedon:
        for r in range(1, len(rows), 2):
            rows[r] = rows[r][::-1]
    return rows


def _read(rows, mode, width):
    if mode == "rows":
        return [c for row in rows for c in row]
    if mode == "rows_rev":
        return [c for row in reversed(rows) for c in row]
    if mode == "cols":
        return [row[c] for c in range(width) for row in rows if c < len(row)]
    if mode == "cols_rev":
        return [row[c] for c in range(width - 1, -1, -1) for row in rows if c < len(row)]
    if mode == "cols_boust":
        out = []
        for c in range(width):
            col = [row[c] for row in rows if c < len(row)]
            out.extend(col if c % 2 == 0 else col[::-1])
        return out
    raise ValueError(mode)


def route_family(widths=range(2, 49)):
    """Rectangular write/read routes over the 97 positions."""
    seen = set()
    for w in widths:
        for boust in (False, True):
            rows = _grid(w, boust)
            for mode in ("rows", "rows_rev", "cols", "cols_rev", "cols_boust"):
                order = _read(rows, mode, w)
                if len(order) != N or len(set(order)) != N:
                    continue
                for rev in (False, True):
                    perm = order[::-1] if rev else order
                    key = tuple(perm)
                    if key in seen:
                        continue
                    seen.add(key)
                    yield f"route w={w} boust={int(boust)} {mode} rev={int(rev)}", perm


def inverse(perm):
    inv = [0] * N
    for i, p in enumerate(perm):
        inv[p] = i
    return inv
