"""EXP-002  Mengenlehreuhr lit-lamp count as the K4 keystream.

Pre-registered hypothesis
-------------------------
The BERLINCLOCK crib names the Mengenlehreuhr. If the clock is the key rather
than a hint at a destination, the natural reading is the number of lit lamps at
a time of day that advances by a fixed step per ciphertext character:

    k[i] = readout( (t0 + step*i) mod 1440 ) + d   (mod 26)

Free parameters, all bounded and enumerated in full:
    t0        start minute of day          1440
    step      minutes per character        +-1..60                 120
    readout   lamps_lit | lamps_lit_sec | minutes_mod26 (control)    3
    d         constant key offset          free, solved not searched
    convention 12 shift conventions                                 12

Gate: all 24 confirmed crib letters must be produced exactly. `d` is not
searched: for a candidate to pass, the 24 residuals (k_required - readout) must
be *equal*, and that common value is d. Reporting therefore covers the full
1440*120*3*12*26 = 161,740,800 parameter space at 1/26 of the cost.

Distinct from the recorded negative "24-sector World Clock geometry", which
concerns the Urania Weltzeituhr, and from "World Clock tape as conventional
key", which uses a city-name tape as a Vigenere keyword.
"""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load
from k4lib.conventions import all_conventions
from k4lib import analysis as an
from k4lib import berlin_clock as bc

k4 = load()
cribs = k4.crib_positions()
positions = [i for i, _, _ in cribs]
T = bc.lit_table()
conventions = all_conventions()
required = {cv.name: an.sparse_keystream(cv, cribs) for cv in conventions}

print("# EXP-002 Mengenlehreuhr lamp-count keystream")
print(f"ciphertext sha256 {k4.sha256}")
print(f"lamp rows {bc.ROWS}, max lit {bc.MAX_LIT}\n")

print("## Analytic pre-filter (d = 0 forced)")
print("A readout bounded by R cannot produce a required key index above R.")
for cv in conventions:
    ks = required[cv.name]
    lo, hi, _ = an.value_range_required(ks)
    verdict = []
    for rname, (_, (rlo, rhi)) in bc.READOUTS.items():
        verdict.append(f"{rname}:{'possible' if hi <= rhi and lo >= rlo else 'EXCLUDED'}")
    print(f"  {cv.name.ljust(34)} required {lo}-{hi}  " + "  ".join(verdict))
print()

steps = [s for s in range(-60, 61) if s != 0]
best = collections.defaultdict(lambda: (0, None))
hits = []
variants = 0

for rname, (fn, _) in bc.READOUTS.items():
    for t0 in range(1440):
        for step in steps:
            vals = [fn((t0 + step * i) % 1440, i, T) for i in positions]
            for cv in conventions:
                variants += 1
                ks = required[cv.name]
                bins = [0] * 26
                for j, i in enumerate(positions):
                    bins[(ks[i] - vals[j]) % 26] += 1
                m = max(bins)
                if m == 24:
                    hits.append((rname, t0, step, cv.name, bins.index(24)))
                if m > best[rname][0]:
                    best[rname] = (m, (t0, step, cv.name, bins.index(m)))

print("## Search")
print(f"parameter sets evaluated : {variants:,}")
print(f"equivalent full space    : {variants * 26:,}  (offset d solved, not searched)")
print(f"exact 24/24 hits         : {len(hits)}")
for h in hits:
    print("  HIT", h)
print()
print("## Best partial match per readout (calibration, not a finding)")
for rname, (score, params) in best.items():
    t0, step, cvname, d = params
    print(f"  {rname.ljust(15)} {score}/24  t0={t0} step={step} d={d} {cvname}")
print()
print("Expected best-of-N under the null: with ~5.2M independent draws of 24")
print("letters at p=1/26 each, the modal count alone reaches 7-8/24 by chance.")
print("Anything at or below that level is noise, exactly as prior 4x22 work found.")
