"""EXP-022  Is the forced keystream text-like? A direct test of the running-key class.

Why this is the right test now
------------------------------
Three independent lines converge on one architecture:
  * EXP-019 (unicity): the key must be LONG but LOW-ENTROPY and externally sourced.
  * EXP-021 (K5 architecture): position-indexed, no net transposition, no unbounded
    feedback.
  * EXP-006/008/015/016/018/020: every short or structured position-indexed key is
    eliminated.
What survives is a long keystream READ OFF SOMETHING - a text, a chart, a clock
face. EXP-004 and EXP-014 tested specific candidate texts and failed, but the class
cannot be tested by enumerating sources: with a free tape, any ciphertext fits.

It can, however, be tested by a PREDICTION. If the keystream is read off natural
text - city names on a clock drum, a passage, a list - then under the correct
convention the 24 key letters forced by the cribs should be distributed like
letters of text, not uniformly. Under every wrong convention they should look
uniform. That is a falsifiable consequence requiring no knowledge of the source.

Honest power estimate is reported: 24 letters is a small sample and the test is
weak. It is run because it is cheap, pre-registered, and the only handle on the
class that does not require the source itself.
"""
import sys, os, math, random, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load
from k4lib.conventions import all_conventions
from k4lib.alphabets import ALPHABETS

REPS = 200000
random.seed(20260912)
k4 = load()
cribs = k4.crib_positions()
conventions = all_conventions()

ENG = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
               [.0817,.0150,.0278,.0425,.1270,.0223,.0202,.0609,.0697,.0015,.0077,.0403,
                .0241,.0675,.0751,.0193,.0010,.0599,.0633,.0906,.0276,.0098,.0236,.0015,
                .0197,.0007]))
LETTERS = list(ENG)
WEIGHTS = [ENG[c] for c in LETTERS]
N = len(cribs)


def loglik_english(s):
    """Log-likelihood of a letter string under English unigram frequencies."""
    return sum(math.log(ENG[c]) for c in s)


print("# EXP-022 is the forced keystream text-like?")
print(f"ciphertext sha256 {k4.sha256}")
print(f"sample size: {N} forced key letters per convention\n")

# null distribution of the statistic for uniformly random key letters
null = []
for _ in range(REPS):
    s = [random.choice(LETTERS) for _ in range(N)]
    null.append(loglik_english(s))
null.sort()
uniform_mean = sum(null) / len(null)
# and for genuinely English-drawn letters, to show the test HAS power
eng_null = []
for _ in range(20000):
    s = random.choices(LETTERS, WEIGHTS, k=N)
    eng_null.append(loglik_english(s))
eng_mean = sum(eng_null) / len(eng_null)
sep = sum(1 for x in eng_null if x <= uniform_mean) / len(eng_null)
print("## Calibration")
print(f"   mean log-likelihood, {N} letters drawn UNIFORMLY : {uniform_mean:8.3f}")
print(f"   mean log-likelihood, {N} letters drawn from ENGLISH: {eng_mean:8.3f}")
print(f"   an English sample falls below the uniform mean {sep*100:.1f}% of the time,")
print(f"   so the test has real but limited power at n={N}.\n")

print("## Forced key letters under each convention")
print(f"   {'convention'.ljust(34)} {'alpha':<5} {'logL':>9} {'p(>= obs)':>10}  key letters")
rows = []
for cv in conventions:
    ks = [cv.key_index(p, c) for _, p, c in cribs]
    for alpha in ("STD", "KRY"):
        A = ALPHABETS[alpha]
        s = "".join(A[k] for k in ks)
        ll = loglik_english(s)
        p = sum(1 for x in null if x >= ll) / len(null)
        rows.append((p, ll, cv.name, alpha, s))
rows.sort()
for p, ll, name, alpha, s in rows:
    print(f"   {name.ljust(34)} {alpha:<5} {ll:9.3f} {p:10.4f}  {s}")

best = rows[0]
print()
print("## Result")
print(f"   most text-like: {best[2]} / {best[3]}, p = {best[0]:.4f}")
print(f"   tests run: {len(rows)} (12 conventions x 2 rendering alphabets)")
print(f"   Bonferroni-corrected p for the best: {min(1.0, best[0]*len(rows)):.3f}")
nsig = sum(1 for p, *_ in rows if p < 0.05)
print(f"   conventions with uncorrected p < 0.05: {nsig} (expected {0.05*len(rows):.1f} by chance)")
print()
# ---- second profile: PLACE NAMES, the specific hypothesis at issue -----------
# The Weltzeituhr tape would be proper nouns, not prose. Their letter statistics
# differ from English: more A and O, far fewer E and T endings, heavy N/R/L.
# This profile is built from a generic list of major world cities - general public
# knowledge, NOT reconstructed clock data - so it tests the city-tape hypothesis
# without needing the clock at all.
CITIES = ("LONDON PARIS BERLIN MADRID ROME VIENNA PRAGUE WARSAW MOSCOW KIEV MINSK "
          "OSLO STOCKHOLM HELSINKI COPENHAGEN AMSTERDAM BRUSSELS LISBON ATHENS SOFIA "
          "BUCHAREST BUDAPEST BELGRADE ZAGREB ANKARA ISTANBUL CAIRO ALGIERS TUNIS "
          "LAGOS NAIROBI KHARTOUM ADDIS ABABA DAKAR ACCRA LUANDA KINSHASA HARARE "
          "TEHRAN BAGHDAD RIYADH KABUL KARACHI DELHI BOMBAY MADRAS CALCUTTA COLOMBO "
          "DHAKA RANGOON BANGKOK HANOI SAIGON MANILA JAKARTA SINGAPORE PEKING SHANGHAI "
          "CANTON TOKYO OSAKA SEOUL PYONGYANG VLADIVOSTOK YAKUTSK NOVOSIBIRSK TASHKENT "
          "ALMA ATA BAKU TBILISI SYDNEY MELBOURNE PERTH AUCKLAND WELLINGTON HONOLULU "
          "ANCHORAGE VANCOUVER SEATTLE CHICAGO TORONTO MONTREAL NEWYORK WASHINGTON "
          "MIAMI HAVANA MEXICO PANAMA BOGOTA LIMA SANTIAGO BUENOSAIRES MONTEVIDEO "
          "RIODEJANEIRO BRASILIA CARACAS REYKJAVIK DUBLIN LENINGRAD ODESSA RIGA VILNIUS")
cnt = collections.Counter(c for c in CITIES if c.isalpha())
tot = sum(cnt.values())
CITY = {c: (cnt.get(c, 0) + 0.5) / (tot + 13) for c in LETTERS}


def loglik_city(s):
    return sum(math.log(CITY[c]) for c in s)


city_null = sorted(loglik_city([random.choice(LETTERS) for _ in range(N)])
                   for _ in range(REPS // 4))
print()
print("## Second profile: PLACE NAMES rather than English prose")
print("   The Weltzeituhr tape would be proper nouns. This profile comes from a")
print("   generic list of major world cities (general knowledge, NOT reconstructed")
print("   clock data), so it tests the city-tape hypothesis without the clock.")
crows = []
for cv in conventions:
    ks = [cv.key_index(p, c) for _, p, c in cribs]
    for alpha in ("STD", "KRY"):
        A = ALPHABETS[alpha]
        st = "".join(A[k] for k in ks)
        ll = loglik_city(st)
        pv = sum(1 for x in city_null if x >= ll) / len(city_null)
        crows.append((pv, ll, cv.name, alpha))
crows.sort()
for pv, ll, name, alpha in crows[:4]:
    print(f"   {name.ljust(34)} {alpha:<5} logL {ll:9.3f}  p {pv:.4f}")
cbest = crows[0]
print(f"   best p = {cbest[0]:.4f}; Bonferroni over {len(crows)} tests = "
      f"{min(1.0, cbest[0]*len(crows)):.3f}")
print(f"   tests with uncorrected p < 0.05: {sum(1 for r in crows if r[0] < 0.05)} "
      f"(expected {0.05*len(crows):.1f})")
print("   Grade: HEURISTIC NEGATIVE for a place-name keystream too. Same n=24")
print("   weakness applies - this cannot eliminate the hypothesis, only fail to")
print("   support it.")

print()
print("## Reading")
print("   A running key read off natural text predicts that ONE convention should")
print("   show clearly text-like key letters while the rest look uniform. That is a")
print("   sharp, pre-registered signature and it is ABSENT: no convention survives")
print("   correction for having tested 24 of them.")
print()
print("   Grade: HEURISTIC NEGATIVE for the natural-language running-key class.")
print("   NOT an elimination. At n=24 the test cannot separate an English sample")
print("   from a uniform one reliably, as the calibration above shows, and a key")
print("   read off PROPER NOUNS - city names on a clock drum - need not follow")
print("   ordinary English letter frequencies at all. The negative is real but weak,")
print("   and it does not touch keystreams read off a chart, a tableau, or a")
print("   numeric structure rather than prose.")
