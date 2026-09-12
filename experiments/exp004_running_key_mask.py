"""EXP-004  Running-key "mask" drawn from the sculpture's own text.

Pre-registered hypothesis
-------------------------
Sanborn has described K4 as using a masking technique. Every periodicity test in
this repository (EXP-001, EXP-003) fails, and a *long* key -- one as long as the
message -- is precisely the construction that makes periodicity tests fail while
leaving the cipher itself elementary. The obvious long keys available to the
sculptor are the sculpture's own texts.

    k[i] = index( M[ (o + dir*i) mod len(M) ] )

Both cribs must satisfy a single offset `o` simultaneously, so a mask source of
length L offers only L alignments per direction -- a very small space for a
24-letter test. That is what makes this cheap and worth running.

This is a material difference from the recorded negative "Basic feedback /
self-masking ciphers, lags 1-12": that family used the ciphertext at a short lag
as its own key. Here the key is an *external* fixed text at any alignment.

Transcription risk
------------------
K1-K3 plaintexts in data/mask_sources.json are unverified working
transcriptions. A single wrong letter would break an exact-match test, so the
gate is a *fuzzy* score (letters matched out of 24) and the report gives the
exact binomial tail, so a near-miss could not be mistaken for a negative.
"""
import sys, os, json, math, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load, REPO_ROOT
from k4lib.conventions import all_conventions
from k4lib.alphabets import ALPHABETS, index_map

k4 = load()
cribs = k4.crib_positions()
positions = [i for i, _, _ in cribs]
conventions = all_conventions()
sources = json.load(open(os.path.join(REPO_ROOT, "data", "mask_sources.json")))["sources"]

print("# EXP-004 running-key mask from sculpture text")
print(f"ciphertext sha256 {k4.sha256}\n")
print("## Mask sources")
for s in sources:
    flag = "verified" if s["verified"] else "UNVERIFIED - see docs/next-steps.md"
    print(f"  {s['id'].ljust(18)} len={len(s['text']):>4}  {flag}")
print()


def binom_tail(n, k, p):
    return sum(math.comb(n, j) * p**j * (1 - p)**(n - j) for j in range(k, n + 1))


results = []
trials = 0
for s in sources:
    M, L = s["text"], len(s["text"])
    for kalpha in ("STD", "KRY"):
        kidx = index_map(ALPHABETS[kalpha])
        mvals = [kidx[ch] for ch in M]
        for direction in (1, -1):
            for o in range(L):
                stream = [mvals[(o + direction * i) % L] for i in positions]
                for cv in conventions:
                    trials += 1
                    got = sum(1 for j, i in enumerate(positions)
                              if cv.key_index(cribs[j][1], cribs[j][2]) == stream[j])
                    results.append((got, s["id"], kalpha, direction, o, cv.name))

results.sort(reverse=True)
best = results[0][0]
print("## Search")
print(f"alignments evaluated : {trials:,}")
print(f"exact 24/24 hits     : {sum(1 for r in results if r[0] == 24)}")
print(f"best score           : {best}/24\n")
print("## Top 10 alignments (calibration, not findings)")
for got, sid, ka, d, o, cvn in results[:10]:
    print(f"  {got:>2}/24  {sid.ljust(18)} keyalpha={ka} dir={d:+d} offset={o:<4} {cvn}")
print()
p1 = binom_tail(24, best, 1 / 26)
print("## Null calibration")
print(f"P(single alignment scores >= {best}/24) = {p1:.3e}")
print(f"expected count over {trials:,} alignments = {p1 * trials:.2f}")
print(f"observed count at >= {best}/24 = {sum(1 for r in results if r[0] >= best)}")
print()
hist = collections.Counter(r[0] for r in results)
print("## Score histogram")
for sc in sorted(hist):
    print(f"  {sc:>2}/24 : {hist[sc]:>7}")
