"""Structure probes for partially-known keystreams.

At a known-plaintext position the key index is forced. K4 gives 24 such
positions out of 97, so every probe here works on a *sparse* keystream:
a dict {position: key_index}. Each probe returns a verdict plus the number of
independent constraints it actually tested, because a probe with too few
constraints passes by accident and must never be reported as a finding.
"""

from collections import defaultdict


def sparse_keystream(convention, crib_positions, permutation=None, ciphertext=None):
    """{plaintext position -> forced key index}.

    `permutation` maps a plaintext position to the ciphertext position it was
    drawn from (i.e. a transposition applied before the shift layer). When it is
    None the identity is used and `ciphertext` is ignored.
    """
    ks = {}
    for i, p_letter, c_letter in crib_positions:
        if permutation is not None:
            c_letter = ciphertext[permutation[i]]
        ks[i] = convention.key_index(p_letter, c_letter)
    return ks


def period_consistency(ks, period):
    """Is the sparse keystream consistent with a repeating key of `period`?

    Returns (consistent, constraints) where `constraints` counts the collisions
    actually tested: sum over residue classes of (occupancy - 1). A result with
    0 constraints is vacuous.
    """
    classes = defaultdict(set)
    counts = defaultdict(int)
    for i, k in ks.items():
        classes[i % period].add(k)
        counts[i % period] += 1
    constraints = sum(n - 1 for n in counts.values())
    consistent = all(len(v) == 1 for v in classes.values())
    return consistent, constraints


def affine_index_fits(ks):
    """All (a, b) with k[i] == (a*i + b) mod 26 at every known position."""
    return [(a, b) for a in range(26) for b in range(26)
            if all(k == (a * i + b) % 26 for i, k in ks.items())]


def is_arithmetic(seq):
    """(True, step) if `seq` is an arithmetic progression mod 26."""
    if len(seq) < 2:
        return False, None
    step = (seq[1] - seq[0]) % 26
    return all((seq[j + 1] - seq[j]) % 26 == step for j in range(len(seq) - 1)), step


def first_difference(seq):
    return [(seq[j + 1] - seq[j]) % 26 for j in range(len(seq) - 1)]


def value_range_required(ks):
    """(min, max, set) of forced key indices - falsifies bounded key sources."""
    vals = sorted(ks.values())
    return vals[0], vals[-1], sorted(set(vals))


def index_of_coincidence(text):
    n = len(text)
    if n < 2:
        return 0.0
    counts = defaultdict(int)
    for ch in text:
        counts[ch] += 1
    return sum(c * (c - 1) for c in counts.values()) / (n * (n - 1))


def conflicts(crib_positions):
    """Evidence against a monoalphabetic layer.

    Returns (same_cipher_diff_plain, same_plain_diff_cipher) as lists of
    (letter, [(position, other_letter), ...]).
    """
    by_c, by_p = defaultdict(list), defaultdict(list)
    for i, p, c in crib_positions:
        by_c[c].append((i, p))
        by_p[p].append((i, c))
    scd = [(c, v) for c, v in sorted(by_c.items()) if len({p for _, p in v}) > 1]
    spd = [(p, v) for p, v in sorted(by_p.items()) if len({c for _, c in v}) > 1]
    return scd, spd
