"""EXP-029  The RESTRICTED Weltzeituhr test: EXP-024's preregistered machinery, one real face.

Tier 1 is satisfied for the first time: the CET/UTC+1 face - the face the BERLINCLOCK crib
names - is completely transcribed, both bands and order, from a target-era photograph
(4 Nov 1989), and carries 120 letters, more than the 97-letter window a running-key test
needs. EXP-027's Tier-1 rule permits a RESTRICTED run: exactly those alignments whose
window falls inside the known arc, with the restriction reported.

This experiment imports EXP-024's preregistered components UNCHANGED - the same
`procedures()` from k4lib.weltzeituhr, the same two key alphabets, both directions, every
offset, and all twelve shift conventions - and applies them to the frozen reconstruction in
`data/weltzeituhr_photos.json` -> tier1_frozen_reconstruction. EXP-024 itself is not
modified and not re-run here.

What "restricted" costs, stated plainly: with ONE face, the 22 procedures collapse. Reading
direction and start sector are meaningless for a single sector, whole-band-first is
identical to band-order, and the alternating readings degenerate to a single band. So the
22 procedures yield only a handful of DISTINCT tapes. This covers a small fraction of the
preregistered space and is not EXP-024.

The criterion is preregistered and unchanged: all 24 known crib letters must be reproduced
simultaneously. A planted positive control runs on the REAL tape, so a negative result is
a measurement rather than an absence of evidence.
"""
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load, REPO_ROOT
from k4lib.conventions import all_conventions
from k4lib.alphabets import ALPHABETS, index_map
from k4lib.weltzeituhr import procedures, normalise

k4 = load()
cribs = k4.crib_positions()
positions = [i for i, _, _ in cribs]
conventions = all_conventions()

photos = json.load(open(os.path.join(REPO_ROOT, "data", "weltzeituhr_photos.json"),
                        encoding="utf-8"))
FR = photos["tier1_frozen_reconstruction"]

print("# EXP-029 restricted Weltzeituhr test")
print(f"ciphertext sha256 {k4.sha256}\n")

print("## The frozen reconstruction under test (cited verbatim, frozen before testing)")
print(f"   sector : {FR['sector']}")
print(f"   basis  : {FR['basis']}")
print(f"   upper  : {' '.join(FR['upper'])}   ({FR['letters']['upper']} letters, {FR['confidence']['upper']})")
print(f"   lower  : {' '.join(FR['lower'])}   ({FR['letters']['lower']} letters, {FR['confidence']['lower']})")
print(f"   total  : {FR['letters']['total']} letters")
print(f"   risk   : {FR['known_risk']}")
print()

clock = {"sectors": [{"upper": FR["upper"], "lower": FR["lower"]}]}
procs = procedures(clock, berlin_sector=0)

# distinct tapes, since a one-sector clock collapses most procedures
tapes = collections.OrderedDict()
for name, t in procs.items():
    tapes.setdefault(t, []).append(name)

print("## How far the 22 preregistered procedures collapse on one face")
print(f"   procedures defined      : {len(procs)}  (the 2 utc-order readings of the 22 need a")
print( "                             multi-sector clock and are inapplicable to one face)")
print(f"   DISTINCT tapes produced : {len(tapes)}")
usable = {t: n for t, n in tapes.items() if len(t) >= 97}
print(f"   tapes >= 97 letters     : {len(usable)}  (shorter tapes cannot carry a 97-window)")
for t, names in tapes.items():
    tag = "USABLE" if len(t) >= 97 else "too short"
    print(f"     {len(t):>3} letters  [{tag}]  {len(names)} procedure(s), e.g. {names[0]}")
    print(f"                  {t[:72]}{'...' if len(t) > 72 else ''}")
print()

def tail(kmin, n=24, p=1.0 / 26.0):
    from math import comb
    return sum(comb(n, k) * p**k * (1 - p)**(n - k) for k in range(kmin, n + 1))


def scan(tape_list):
    """EXP-024's scan, unchanged: 2 key alphabets x 2 directions x every offset x 12 conventions."""
    hits, best, trials, top = [], [], 0, []
    for tape in tape_list:
        L = len(tape)
        for kalpha in ("STD", "KRY"):
            kk = index_map(ALPHABETS[kalpha])
            mv = [kk[c] for c in tape]
            for direction in (1, -1):
                for o in range(L):
                    stream = [mv[(o + direction * i) % L] for i in positions]
                    for cv in conventions:
                        trials += 1
                        got = sum(1 for j, (i, p, c) in enumerate(cribs)
                                  if cv.key_index(p, c) == stream[j])
                        best.append(got)
                        if got >= 6:
                            top.append((got, kalpha, direction, o, cv.name))
                        if got == 24:
                            hits.append((kalpha, direction, o, cv.name, tape))
    return hits, best, trials, top

# ------------------------------------------------------------------ positive control
print("## Positive control on the REAL tape (not a synthetic one)")
ctrl_tape = list(usable)[0]
OFF, CVI, KA = 41, 0, "STD"
ki = index_map(ALPHABETS[KA])
planted = [ki[ctrl_tape[(OFF + i) % len(ctrl_tape)]] for i in range(97)]
cv0 = conventions[CVI]
PT = ["X"] * 97
for i, p, _ in cribs:
    PT[i] = p
CT = "".join(cv0.encrypt_letter(p, k) for p, k in zip(PT, planted))
planted_cribs = [(i, p, CT[i]) for i, p, _ in cribs]

_real = cribs
k4.__dict__  # no mutation; swap the crib list locally instead
cribs = planted_cribs
hits, best, trials, _ = scan([ctrl_tape])
cribs = _real
ok = any(h[2] == OFF and h[0] == KA and h[1] == 1 and h[3] == cv0.name for h in hits)
print(f"   planted: offset {OFF}, {KA} alphabet, direction +1, {cv0.name}")
print(f"   alignments scanned {trials:,}; exact 24/24 recoveries {len(hits)}")
print(f"   CONTROL {'PASSED' if ok else 'FAILED'} - a genuine keystream read off THIS face")
print("   would be detected by this scan.\n")
assert ok, "positive control failed - do not interpret the real result"

# ------------------------------------------------------------------ the real test
print("## THE REAL TEST - all alignments, real cribs")
hits, best, trials, top = scan(list(usable))
dist = collections.Counter(best)
print(f"   tapes tested          : {len(usable)}")
print(f"   alignments scanned    : {trials:,}")
print(f"   criterion             : all 24 crib letters reproduced simultaneously")
print(f"   exact 24/24 matches   : {len(hits)}")
print()
print("   distribution of crib letters reproduced (this is the actual measurement):")
for k in sorted(dist, reverse=True)[:9]:
    print(f"      {k:>2}/24 cribs : {dist[k]:>9,} alignments")
exp_mean = 24 / 26
print(f"   best achieved         : {max(best)}/24")
print(f"   mean                  : {sum(best)/len(best):.3f}/24   (chance expectation {exp_mean:.3f})")
print()
print("   Is the best alignment notable? Tested properly, not asserted:")
for kmin in (6, 7):
    exp = tail(kmin) * trials
    obs = sum(v for k, v in dist.items() if k >= kmin)
    print(f"      >= {kmin}/24 : observed {obs}, expected {exp:.2f} under chance")
import math
lam = tail(7) * trials
obs7 = sum(v for k, v in dist.items() if k >= 7)
pois = 1 - sum(math.exp(-lam) * lam**k / math.factorial(k) for k in range(obs7))
print(f"      Poisson P(>= {obs7} at >= 7/24 | chance) = {pois:.3f}")
print("      A ~2-sigma blip on a maximum I picked out after looking, over twelve")
print("      conventions that are not independent of one another. Unremarkable, and")
print("      nowhere near the 24/24 the preregistered criterion requires. Recorded, not")
print("      pursued - chasing it is exactly how this programme would fool itself.")
for t in sorted(top, reverse=True)[:4]:
    print(f"        {t[0]}/24  {t[1]} dir{t[2]:+d} offset {t[3]:>3}  {t[4]}")
print()
print("## Multiple testing")
print(f"   Chance of 24/24 at one alignment is 26^-24 ~ 1.5e-34. Over {trials:,} alignments the")
print(f"   expected number of spurious exact hits is ~{trials * 26.0**-24:.2e}. So a single exact")
print("   hit would be meaningful - and there are none. No correction is needed for a null.")
print()
if hits:
    print("## HITS - to be treated as hypotheses, NOT as a solution")
    for h in hits[:10]:
        print(f"   {h[:4]}")
    print("   No external verifier is to be consulted on this basis.")
else:
    print("## RESULT: NEGATIVE")
    print("   The complete target-era CET/UTC+1 face does NOT serve as a running key for K4")
    print("   under any of the tested alignments: any usable preregistered reading of that one")
    print("   face, either key alphabet, either direction, every offset, all twelve shift")
    print("   conventions. Nothing comes close: the best alignment reproduces")
    print(f"   {max(best)}/24 of 24 crib letters, against a chance mean of 0.92 - and the")
    print("   criterion is 24/24.")
    print()
    print("## What this does and does NOT eliminate")
    print("   ELIMINATED (exhaustively, within the stated model): the single-face running-key")
    print("   reading of the Berlin/CET face, for these tapes and this alignment space.")
    print("   NOT eliminated:")
    print("     - readings that span SEVERAL faces, which is most of EXP-024's space and needs")
    print("       the neighbouring faces' bands, which are only partially read;")
    print("     - any non-running-key use of the object (indicator, coordinate, digit source);")
    print("     - readings under a different transcription of the lower band, since mine is")
    print("       graded MEDIUM-HIGH, not certain;")
    print("     - the Weltzeituhr hypothesis itself. This is one honest negative, not a verdict")
    print("       on the object.")
print()
print("## Protocol")
print("   EXP-024 is unmodified and was not re-run. The reconstruction was frozen in the")
print("   dataset BEFORE this test ran (tier1_frozen_reconstruction.declared) and is cited")
print("   verbatim above. No external verifier consulted. No crib beyond the public")
print("   EASTNORTHEAST and BERLINCLOCK material was used.")
