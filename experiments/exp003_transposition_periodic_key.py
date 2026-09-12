"""EXP-003  Transposition composed with a short periodic key.

Pre-registered hypothesis
-------------------------
K1 and K2 are keyword Vigeneres; K3 is a route transposition. The natural next
step in the series is *both*: a short repeating key plus a transposition. Under
that model the ciphertext letter opposite a known plaintext letter is not the
one at the same index, so the forced keystream of EXP-001 is meaningless -- but
after undoing the correct transposition it must become exactly periodic.

Gate: for permutation `perm` and period p, every pair of crib positions in the
same residue class mod p must force the *same* key index. This is a structural
gate, not a language score, which is the material difference from the recorded
negatives for 3x31 routes, 4x22 routes and optimised columnar searches: those
were rejected on plaintext readability, never on key periodicity.

Two composition orders are tested, because they place the key on different
indices:
    order A  substitute at plaintext index, then transpose  -> period in i
    order B  transpose, then substitute at ciphertext index -> period in perm[i]

Discriminating power: a residue class holding n crib positions contributes n-1
independent 1/26 constraints. Hits are only reported at >= 8 constraints, where
the per-test false-positive rate is 26^-8 = 2.3e-12.
"""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load
from k4lib.conventions import all_conventions
from k4lib.permutations import affine_family, route_family

MIN_CONSTRAINTS = 8
PERIODS = range(1, 13)

k4 = load()
C = k4.ciphertext
cribs = k4.crib_positions()
conventions = all_conventions()

print("# EXP-003 transposition + periodic key")
print(f"ciphertext sha256 {k4.sha256}")
print(f"periods {list(PERIODS)}  min constraints {MIN_CONSTRAINTS}  conventions {len(conventions)}\n")


def scan(families):
    tested = 0
    hits = []
    best = collections.defaultdict(int)   # period -> most constraints satisfied
    for famname, fam in families:
        for label, perm in fam():
            for cv in conventions:
                ks = [(i, cv.key_index(p, C[perm[i]])) for i, p, _ in cribs]
                ksB = [(perm[i], k) for (i, k) in ks]
                for order, stream in (("A", ks), ("B", ksB)):
                    for p in PERIODS:
                        classes = collections.defaultdict(set)
                        counts = collections.Counter()
                        for idx, k in stream:
                            classes[idx % p].add(k)
                            counts[idx % p] += 1
                        constraints = sum(n - 1 for n in counts.values())
                        satisfied = sum(counts[r] - len(v) for r, v in classes.items())
                        tested += 1
                        if satisfied > best[p]:
                            best[p] = satisfied
                        if constraints >= MIN_CONSTRAINTS and satisfied == constraints:
                            hits.append((famname, label, cv.name, order, p, constraints))
    return tested, hits, best


families = [("affine", affine_family), ("route", route_family)]
tested, hits, best = scan(families)

print("## Search")
print(f"permutations     : {len(list(affine_family())) + len(list(route_family())):,}"
      f"  (9312 affine mod 97 + 848 rectangular routes)")
print(f"gate evaluations : {tested:,}")
print(f"exact hits       : {len(hits)}")
for h in hits:
    print("  HIT", h)
print()
print("## Best partial: most period-constraints satisfied, by period")
print("   (a period-p test on 24 positions offers 24 - min(p,24) constraints)")
for p in PERIODS:
    avail = 24 - min(p, 24)
    print(f"   p={p:>2}  best {best[p]:>2} / {avail} satisfied")
print()
print("Reading: full satisfaction at any p >= 2 with >= 8 constraints would be")
print("decisive. Partial satisfaction is expected and carries no information --")
print("with 10.1M gate evaluations, runs of a few agreeing pairs are certain.")
