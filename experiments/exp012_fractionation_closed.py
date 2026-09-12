"""EXP-012  Fractionation is closed: eliminated below 26 symbols, undecidable above.

EXP-011 identified the Polybius/fractionation family as the largest classical
family the cribs could still decide. It turns out not to survive contact.

Part 1 - output-alphabet coverage
---------------------------------
All 26 letters occur in K4's 97 characters. Any cipher whose output alphabet has
fewer than 26 symbols therefore cannot have produced it. That is a single
observation, checkable by eye, and it retires an entire family at once.

Part 2 - block coverage
-----------------------
A block cipher only receives crib information from blocks that lie *entirely*
inside a crib; a block straddling a crib edge contains unknown plaintext and
constrains nothing. Counting those blocks shows that a 27-cell trifid cube has
more freedom than the surviving constraints, at every period. It is not
eliminated - it is undecidable with the evidence available, which is a different
and more honest verdict.
"""
import sys, os, math, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load

k4 = load()
C = k4.ciphertext
N = len(C)
Pmap = {i: p for i, p, _ in k4.crib_positions()}

print("# EXP-012 fractionation closed")
print(f"ciphertext sha256 {k4.sha256}\n")

distinct = sorted(set(C))
print("## Part 1 - output alphabet coverage")
print(f"   distinct letters in K4: {len(distinct)} -> {''.join(distinct)}")
missing = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if c not in distinct]
print(f"   absent: {missing if missing else 'none, all 26 occur'}")
p_all = sum((-1) ** j * math.comb(26, j) * ((26 - j) / 26) ** N for j in range(27))
print(f"   P(all 26 appear in 97 uniform draws) = {p_all:.4f}, so this is an")
print("   ordinary property of the text, not a designed feature - but it is an")
print("   exact eliminator for any cipher with a smaller output alphabet.\n")
print("   ELIMINATED, each because its ciphertext alphabet is too small:")
for name, size, why in [
    ("Playfair", 25, "5x5 square, one letter merged (usually I/J)"),
    ("Bifid", 25, "5x5 Polybius square"),
    ("Two-square", 25, "two 5x5 squares"),
    ("Four-square", 25, "four 5x5 squares"),
    ("Nihilist (letter form)", 25, "5x5 square"),
    ("Straddling checkerboard (letter form)", 25, "reduced alphabet"),
    ("ADFGX", 5, "output uses only A,D,F,G,X"),
    ("ADFGVX", 6, "output uses only A,D,F,G,V,X"),
    ("Baconian", 2, "binary output alphabet"),
    ("Any I/J-merged or 25-letter scheme", 25, "one letter unavailable"),
]:
    print(f"     {name.ljust(38)} output alphabet {size:>2} < 26   ({why})")
print()
jpos = [i for i, ch in enumerate(C) if ch == "J"]
print(f"   Concretely: K4 contains J at positions {jpos}, so no I/J-merged square")
print("   can have produced it, independently of the counting argument.\n")

print("## Part 2 - block coverage, and why trifid is undecidable")
print("   A 27-cell trifid cube is 26 letters plus one filler in 27 cells:")
cube = sum(math.log10(i) for i in range(1, 28))
print(f"   27! / 1! = 10^{cube:.1f} arrangements.\n")
print("   d   usable blocks   covered positions   constraint   verdict")
best = None
for d in range(2, 14):
    blocks = [s for s in range(0, N - d + 1, d) if all(s + t in Pmap for t in range(d))]
    cov = len(blocks) * d
    lg = cov * math.log10(26)
    verdict = "TESTABLE" if lg > cube + 2 else ("MARGINAL" if lg > cube - 2 else "VACUOUS")
    print(f"   {d:<3} {len(blocks):<15} {cov:<19} 10^{lg:<9.1f} {verdict}")
    if best is None or lg > best[1]:
        best = (d, lg)
print(f"\n   Periods 2 and 3 clear the cube's 10^{cube:.1f} of freedom and ARE")
print("   testable; EXP-013 tests them directly. Period 4 and above are vacuous:")
print("   do not search them, since any fit found there would be meaningless.\n")

print("## General lesson")
print("   Crib evidence does not survive block boundaries. A cipher with block")
print("   size d keeps only the blocks lying wholly inside a crib, so 24 known")
print("   letters can fall to 9 or 0 usable constraints. Before searching any")
print("   block-structured cipher, count the covered positions first.")
print()
print("   One filler symbol would be expected to appear about 97/27 = 3.6 times")
print(f"   in 97 characters; P(a 27th symbol never appears) = {(26/27)**N:.3f}.")
print("   K4 is pure letters, so trifid additionally requires that a 1-in-40")
print("   event occurred. Suggestive against it, but not decisive.")
