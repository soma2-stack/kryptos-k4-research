"""Keystream models that are *linear in their unknown parameters*.

Each model maps a ciphertext position to a coefficient row over its unknowns.
Combined with the key index forced at a crib position, every model below becomes
a linear system over Z_26 that `modlin` solves exactly. That buys three things a
brute-force search cannot:

  * exact solution counts instead of sampled hits;
  * an exact degrees-of-freedom penalty (`modlin.chance_solvable`), so a model
    with more parameters than constraints is scored as the vacuity it is;
  * models whose parameter space is far too large to enumerate (a period-16 key
    is 26^16 = 4.4e22 keys) tested in microseconds.

Every model that resets at a boundary takes `b` as its boundary position.
"""


def periodic(p):
    def f(i):
        r = [0] * p
        r[i % p] = 1
        return r
    return f, p, f"periodic(p={p})"


def periodic_reset(p, b):
    """Same key, phase restarted at b: the key word begins again at position b."""
    def f(i):
        r = [0] * p
        r[(i % p) if i < b else ((i - b) % p)] = 1
        return r
    return f, p, f"periodic_reset(p={p},b={b})"


def periodic_offset(p, b):
    """Same key and phase, but a constant added to every key index from b onward."""
    def f(i):
        r = [0] * (p + 1)
        r[i % p] = 1
        if i >= b:
            r[p] = 1
        return r
    return f, p + 1, f"periodic_offset(p={p},b={b})"


def progressive(L):
    """Key word of length L, shifted by delta on each repetition (progressive key)."""
    def f(i):
        r = [0] * (L + 1)
        r[i % L] = 1
        r[L] = i // L
        return r
    return f, L + 1, f"progressive(L={L})"


def progressive_reset(L, b):
    def f(i):
        r = [0] * (L + 1)
        j = i if i < b else i - b
        r[j % L] = 1
        r[L] = j // L
        return r
    return f, L + 1, f"progressive_reset(L={L},b={b})"


def polynomial(d):
    def f(i):
        return [pow(i, e, 26) for e in range(d + 1)]
    return f, d + 1, f"polynomial(deg={d})"


def polynomial_reset(d, b):
    """Index restarts at b: the progression begins againrather than continuing."""
    def f(i):
        j = i if i < b else i - b
        return [pow(j, e, 26) for e in range(d + 1)]
    return f, d + 1, f"polynomial_reset(deg={d},b={b})"


def polynomial_offset(d, b):
    def f(i):
        r = [pow(i, e, 26) for e in range(d + 1)] + [1 if i >= b else 0]
        return r
    return f, d + 2, f"polynomial_offset(deg={d},b={b})"


def build_system(rowfn, nunk, positions, forced):
    A = [rowfn(i) for i in positions]
    b = [forced[i] for i in positions]
    return A, b


# --- Physically-motivated models: the carved line structure of K4 ------------
# K4 is rendered as OBKR + three lines of 31 characters (boundaries at absolute
# positions 4, 35, 66). These models take that structure as GIVEN by the object:
# the reset positions are not searched, so they add no free parameters at all.

K4_LINE_STARTS = (0, 4, 35, 66)


def _line_of(i, starts=K4_LINE_STARTS):
    ln = 0
    for k, s in enumerate(starts):
        if i >= s:
            ln = k
    return ln, i - starts[ln]


def line_reset(p, starts=K4_LINE_STARTS):
    """Key of period p restarting at every carved line. Unknowns: p."""
    def f(i):
        _, off = _line_of(i, starts)
        r = [0] * p
        r[off % p] = 1
        return r
    return f, p, f"line_reset(p={p})"


def line_offset(p, starts=K4_LINE_STARTS):
    """Period-p key restarting per line, plus a constant added per line."""
    n = len(starts)
    def f(i):
        ln, off = _line_of(i, starts)
        r = [0] * (p + n)
        r[off % p] = 1
        r[p + ln] = 1
        return r
    return f, p + n, f"line_offset(p={p})"


def line_progressive(L, starts=K4_LINE_STARTS):
    """Progressive key restarting at each line: K[j mod L] + delta*(j//L)."""
    def f(i):
        _, j = _line_of(i, starts)
        r = [0] * (L + 1)
        r[j % L] = 1
        r[L] = j // L
        return r
    return f, L + 1, f"line_progressive(L={L})"


def line_index_key(p, starts=K4_LINE_STARTS):
    """Key advances once per LINE, not per character: k[i] = K[line(i) mod p]."""
    def f(i):
        ln, _ = _line_of(i, starts)
        r = [0] * p
        r[ln % p] = 1
        return r
    return f, p, f"line_index_key(p={p})"


def column_key(width=31, starts=K4_LINE_STARTS):
    """k[i] = K[column within its line]. 31 unknowns - vacuous as a fit, but it
    makes a sharp testable PREDICTION wherever two crib positions share a column."""
    def f(i):
        _, off = _line_of(i, starts)
        r = [0] * width
        r[off % width] = 1
        return r
    return f, width, f"column_key(w={width})"
