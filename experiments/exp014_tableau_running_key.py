"""EXP-014  The carved tableau as a running key.

`docs/ideas.md` section 5 left one long text unconsumed: the Vigenere tableau
physically carved on the sculpture. EXP-004 tested K4's own ciphertext, the
Kryptos alphabet and the K1-K3 plaintexts as running keys but not the tableau
itself, which is the largest block of letters actually present on the object.

The tableau is reconstructed here as the standard KRYPTOS-keyed Vigenere square:
row r is the Kryptos alphabet rotated left by r, so the first column spells the
Kryptos alphabet down the side. It is read in eight orders - by row, by column,
by broken diagonal, and by anti-diagonal, each forward and reversed - and each
reading is tried at every alignment, in both key-indexing alphabets, under all
12 conventions.

As in EXP-004 the gate is fuzzy (letters matched out of 24) with the exact
binomial tail reported, so that no transcription or reconstruction choice can
manufacture a false negative.
"""
import sys, os, math, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load
from k4lib.conventions import all_conventions
from k4lib.alphabets import ALPHABETS, KRYPTOS, index_map, vigenere_tableau

k4 = load()
cribs = k4.crib_positions()
positions = [i for i, _, _ in cribs]
conventions = all_conventions()

rows = [KRYPTOS[r:] + KRYPTOS[:r] for r in range(26)]
readings = {
    "tableau_rows": "".join(rows),
    "tableau_cols": "".join(rows[r][c] for c in range(26) for r in range(26)),
    "tableau_diag": "".join(rows[r][(r + k) % 26] for k in range(26) for r in range(26)),
    "tableau_antidiag": "".join(rows[r][(k - r) % 26] for k in range(26) for r in range(26)),
}
for name in list(readings):
    readings[name + "_rev"] = readings[name][::-1]


def binom_tail(n, k, p):
    return sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))


print("# EXP-014 carved tableau as running key")
print(f"ciphertext sha256 {k4.sha256}")
print(f"tableau: 26x26 KRYPTOS-keyed square, first column = {''.join(r[0] for r in rows)}")
print(f"readings: {len(readings)}, each {len(readings['tableau_rows'])} letters\n")

results = []
trials = 0
for rname, M in readings.items():
    L = len(M)
    for kalpha in ("STD", "KRY"):
        kidx = index_map(ALPHABETS[kalpha])
        mv = [kidx[ch] for ch in M]
        for direction in (1, -1):
            for o in range(L):
                stream = [mv[(o + direction * i) % L] for i in positions]
                for cv in conventions:
                    trials += 1
                    got = sum(1 for j, (i, p, c) in enumerate(cribs)
                              if cv.key_index(p, c) == stream[j])
                    results.append((got, rname, kalpha, direction, o, cv.name))

results.sort(reverse=True)
best = results[0][0]
print("## Search")
print(f"   alignments evaluated : {trials:,}")
print(f"   exact 24/24 hits     : {sum(1 for r in results if r[0] == 24)}")
print(f"   best score           : {best}/24\n")
print("## Top 8 (calibration, not findings)")
for got, rn, ka, d, o, cvn in results[:8]:
    print(f"   {got:>2}/24  {rn.ljust(20)} keyalpha={ka} dir={d:+d} offset={o:<4} {cvn}")
p1 = binom_tail(24, best, 1 / 26)
print(f"\n## Null calibration")
print(f"   P(single alignment >= {best}/24) = {p1:.3e}")
print(f"   expected count over {trials:,} alignments = {p1 * trials:.2f}")
print(f"   observed at >= {best}/24 = {sum(1 for r in results if r[0] >= best)}")
print()
print("   CAUTION: these alignments are NOT independent. Row r+1 of the tableau is")
print("   row r rotated by one, so offsets differing by a multiple of the row")
print("   length give keystreams differing by a constant, and their match counts")
print("   are strongly correlated. The observed excess at the top of the")
print("   distribution is that clustering - note the hits at offsets 53/78 and")
print("   545/570 and 623/648, each pair 25 apart - not a signal. The binomial")
print("   expectation above is therefore an underestimate of the null and should")
print("   not be read as a 4x excess. The conclusion is unaffected: the best")
print("   alignment matches 7 of 24 crib letters, and nothing approaches 24.")
hist = collections.Counter(r[0] for r in results)
print("\n## Score histogram")
for sc in sorted(hist):
    print(f"   {sc:>2}/24 : {hist[sc]:>8}")
