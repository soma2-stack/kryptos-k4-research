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
