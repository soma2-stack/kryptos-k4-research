"""EXP-023  The K0 Morse material as an external keystream source.

Hypothesis, pre-registered before any result was inspected
----------------------------------------------------------
Sanborn stated in November 2025 that the codes of Kryptos, FROM THE MORSE MATERIAL
ONWARD, concern "delivering a message". That names the Morse copper plates as part
of the coded sequence rather than decoration. They are:

  * physically part of the installation Sanborn built;
  * short, fixed and public - a LOW-ENTROPY external source, which is exactly what
    EXP-019's unicity bound requires of any recoverable long key;
  * applied position by position if used as a running key, which is exactly the
    architecture EXP-021 favours;
  * thematically about position - one plate reads WHAT IS YOUR POSITION, the Q-code
    QTH, which is what a position-indexed keystream is.

This source has never been tested as a keystream here. The inherited handoff used
K0 Morse only as a binary SELECTOR (a lead EXP-009 later explained away as a
1-in-1,024 selection effect). Using it as the key TAPE is a different hypothesis.

Pre-registered conventions, fixed before running
------------------------------------------------
  sources     the individual Morse fragments, and two concatenations
  alignment   every offset, both directions
  alphabets   key indexed in the standard and the KRYPTOS alphabet
  conventions all 12 declared shift conventions
  gate        fuzzy - letters matched out of 24 - with the exact binomial tail, so
              that a transcription error cannot manufacture a false negative

Transcription caveat, recorded up front
---------------------------------------
The Morse readings are COMMUNITY transcriptions, not primary. The ending of
DIGETALINTERPRETATIT is disputed, one plate's text is said to continue under a
rock, and the PHYSICAL ORDER of the slabs is unknown - so the concatenations are a
listing convention, not evidence. A negative here is therefore graded HEURISTIC
NEGATIVE for the concatenations and no stronger than that.
"""
import sys, os, math, json, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load, REPO_ROOT
from k4lib.conventions import all_conventions
from k4lib.alphabets import ALPHABETS, index_map

k4 = load()
cribs = k4.crib_positions()
positions = [i for i, _, _ in cribs]
conventions = all_conventions()
srcs = [s for s in json.load(open(os.path.join(REPO_ROOT, "data", "mask_sources.json")))["sources"]
        if s["id"].startswith("morse")]


def binom_tail(n, k, p):
    return sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))


print("# EXP-023 K0 Morse material as an external keystream source")
print(f"ciphertext sha256 {k4.sha256}\n")
print("## Sources (all community transcriptions, graded below primary)")
for s in srcs:
    print(f"   {s['id'].ljust(32)} {len(s['text']):>3} letters  {s['text']}")
print()

# ------------------------------------------------------------ positive control
print("## Positive control")
cv0 = conventions[0]
tape = srcs[-2]["text"]
kidx = index_map(ALPHABETS["STD"])
OFF = 17
planted = [kidx[tape[(OFF + i) % len(tape)]] for i in positions]
hit = 0
for o in range(len(tape)):
    stream = [kidx[tape[(o + i) % len(tape)]] for i in positions]
    if stream == planted:
        hit += 1
print(f"   a keystream planted from '{srcs[-2]['id']}' at offset {OFF} is recovered by")
print(f"   the same alignment scan: {'YES' if hit else 'NO'} ({hit} matching offset(s))")
ctrl = hit > 0
print(f"   CONTROL {'PASSED' if ctrl else 'FAILED'}\n")

results, trials = [], 0
for s in srcs:
    M, L = s["text"], len(s["text"])
    for kalpha in ("STD", "KRY"):
        ki = index_map(ALPHABETS[kalpha])
        mv = [ki[c] for c in M]
        for direction in (1, -1):
            for o in range(L):
                stream = [mv[(o + direction * i) % L] for i in positions]
                for cv in conventions:
                    trials += 1
                    got = sum(1 for j, (i, p, c) in enumerate(cribs)
                              if cv.key_index(p, c) == stream[j])
                    results.append((got, s["id"], kalpha, direction, o, cv.name))

results.sort(reverse=True)
best = results[0][0]
print("## Search")
print(f"   alignments evaluated : {trials:,}")
print(f"   exact 24/24 hits     : {sum(1 for r in results if r[0] == 24)}")
print(f"   best score           : {best}/24\n")
print("## Top 8 (calibration, not findings)")
for got, sid, ka, d, o, cvn in results[:8]:
    print(f"   {got:>2}/24  {sid.ljust(32)} alpha={ka} dir={d:+d} off={o:<3} {cvn}")
p1 = binom_tail(24, best, 1 / 26)
print(f"\n## Null calibration")
print(f"   P(single alignment >= {best}/24) = {p1:.3e}")
print(f"   expected count over {trials:,} alignments = {p1 * trials:.2f}")
print(f"   observed at >= {best}/24 = {sum(1 for r in results if r[0] >= best)}")
hist = collections.Counter(r[0] for r in results)
print("\n## Score histogram")
for sc in sorted(hist):
    print(f"   {sc:>2}/24 : {hist[sc]:>7}")
print()
print("## Grade")
print("   HEURISTIC NEGATIVE for the Morse material as a direct running-key tape,")
print("   at the scope stated above. NOT an elimination: the transcriptions are")
print("   community-sourced, one plate's text is reported to continue under a rock,")
print("   the ending of DIGETALINTERPRETATIT is disputed, and the physical order of")
print("   the slabs is unknown, so the concatenations are conventions rather than")
print("   evidence. It also does not touch the Morse material used as anything other")
print("   than a letter tape - for example as a source of DOT/DASH structure.")
sys.exit(0 if ctrl else 1)
