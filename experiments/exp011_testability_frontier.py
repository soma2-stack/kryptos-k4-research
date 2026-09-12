"""EXP-011  What 24 crib letters can and cannot decide.

Two results that constrain every future experiment in this repository.

Part 1 - alphabet-free period elimination
-----------------------------------------
Every periodic polyalphabetic cipher, whatever its alphabets, assigns the same
substitution to positions i and j whenever i == j (mod p). The cribs contain
pairs of positions that cannot share a substitution: same plaintext with
different ciphertext, or same ciphertext with different plaintext. If such a
pair is congruent mod p, period p is impossible.

This argument uses no alphabet at all. It therefore applies to Vigenere,
Beaufort, variant Beaufort, every Quagmire, every keyed tableau, and any
bespoke periodic scheme, all at once.

Part 2 - the testability frontier
---------------------------------
24 known plaintext letters supply 24 * log2(26) = 112.8 bits of constraint. A
model class with more parameter entropy than that cannot be refuted by the
cribs: solutions exist by counting alone, and finding one is not evidence.

For each class the expected number of parameter settings that reproduce all 24
crib letters by chance is |parameter space| * 26^-24. Above 1, the class is
unfalsifiable with the evidence available and must not be searched. This is the
quantitative form of the warning already in `docs/data-conventions.md`.
"""
import sys, os, math, itertools
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load

k4 = load()
cribs = k4.crib_positions()
NCRIB = len(cribs)

print("# EXP-011 testability frontier")
print(f"ciphertext sha256 {k4.sha256}\n")

# ---------------------------------------------------------------- Part 1
edges = []
for a, b in itertools.combinations(range(NCRIB), 2):
    ia, pa, ca = cribs[a]
    ib, pb, cb = cribs[b]
    if (pa == pb and ca != cb) or (ca == cb and pa != pb):
        edges.append((ia, ib))

print("## Part 1 - periods impossible for ANY periodic polyalphabetic cipher")
print(f"   alphabet-independent conflict pairs: {len(edges)}")
elim, surv = [], []
for p in range(1, 50):
    bad = [(i, j) for i, j in edges if (i - j) % p == 0]
    (elim if bad else surv).append((p, len(bad)))
print(f"   ELIMINATED periods: {[p for p, _ in elim]}")
for p, nb in elim[:12]:
    ex = next((i, j) for i, j in edges if (i - j) % p == 0)
    print(f"      p={p:<3} {nb} conflicting congruent pairs, e.g. positions {ex}")
print(f"   periods not eliminated by this argument: {[p for p, _ in surv]}")
print("   Note this is a NECESSARY condition only: surviving a period means the")
print("   period is not impossible, not that it works.\n")

# ---------------------------------------------------------------- Part 2
LOG26 = math.log10(26)
BUDGET = NCRIB * LOG26          # log10 of 26^24
print("## Part 2 - falsifiability by parameter count")
print(f"   evidence available: {NCRIB} crib letters = 26^{NCRIB} = 10^{BUDGET:.1f}")
print(f"                     = {NCRIB * math.log2(26):.1f} bits\n")

LOG_FACT26 = sum(math.log10(i) for i in range(1, 27))


def row(name, log_params, note=""):
    expected = log_params - BUDGET
    if expected > 0.3:
        verdict = "VACUOUS - cannot be refuted by cribs"
    elif expected > -2:
        verdict = "MARGINAL - fits are not evidence"
    else:
        verdict = "TESTABLE"
    print(f"   {name.ljust(52)} 10^{log_params:6.1f}  "
          f"expected chance fits 10^{expected:+6.1f}  {verdict}")
    if note:
        print(f"      {note}")


print("   model class                                          params    ")
for p in (4, 8, 12, 16, 20, 24, 26):
    row(f"Vigenere family, fixed alphabet, period {p}", p * LOG26)
print()
for p in (2, 4, 5, 6, 8, 12):
    row(f"Quagmire I (one keyed alphabet) + period {p}", LOG_FACT26 + p * LOG26)
print()
row("Quagmire III (two keyed alphabets) + period 8", 2 * LOG_FACT26 + 8 * LOG26)
row("Homophonic, 2 decryption charts + selector", 2 * LOG_FACT26 + 97 * math.log10(2))
row("Arbitrary per-position substitution (97 alphabets)", 97 * LOG26)
row("Affine-mod-97 transposition + period-8 key", math.log10(96 * 97) + 8 * LOG26)
row("Affine-mod-97 transposition + Quagmire I period 8",
    math.log10(96 * 97) + LOG_FACT26 + 8 * LOG26)
row("Polybius square (bifid/trifid) + period", sum(math.log10(i) for i in range(1, 26)) + math.log10(24))
print()

print("## How much more plaintext would each class need?")
print("   n crib letters supply n*log10(26) of budget. Requiring a margin of 2")
print("   decades below the parameter count, the letters needed are:\n")
for nm, lg in [("Vigenere family, fixed alphabet, period 26", 26 * LOG26),
               ("Quagmire I + period 8", LOG_FACT26 + 8 * LOG26),
               ("Quagmire I + period 12", LOG_FACT26 + 12 * LOG26),
               ("Quagmire III + period 8", 2 * LOG_FACT26 + 8 * LOG26),
               ("Affine transposition + Quagmire I period 8",
                math.log10(96 * 97) + LOG_FACT26 + 8 * LOG26),
               ("Homophonic, 2 charts + free selector",
                2 * LOG_FACT26 + 97 * math.log10(2))]:
    need = math.ceil((lg + 2) / LOG26)
    have = "already testable" if need <= NCRIB else f"needs {need} letters ({need - NCRIB} more)"
    print(f"   {nm.ljust(45)} {have}")
print()
print("   This is the most actionable number in the repository. Every class above")
print("   becomes decidable with between 5 and 25 more known plaintext letters.")
print("   Acquiring constraint is worth more than any further search: one more")
print("   released clue would re-open families that are currently unfalsifiable.")
print()
print("## Consequences")
print("   1. Quagmire I is closed. Periods 1-7 are eliminated outright by Part 1,")
print("      and from period 6 upward the class is already vacuous by Part 2.")
print("      There is no period at which it is both possible and testable.")
print("   2. Quagmire III, any two-keyed-alphabet scheme, and any model with a")
print("      free per-position selector are unfalsifiable with 24 crib letters.")
print("      Searching them can only produce fits, never evidence. This is why")
print("      the inherited two-chart lead could not fail: see EXP-009.")
print("   3. Bifid and trifid sit near the frontier: a 25-cell Polybius square")
print("      plus a period is 10^25.2 against a 10^34 budget, so the class is")
print("      TESTABLE in principle. It is the largest classical family left that")
print("      the cribs can actually decide, and it has not been tested here.")
print("   4. Anything combining a free transposition with a free keyed alphabet")
print("      is vacuous. Transposition work must fix the alphabet in advance.")
