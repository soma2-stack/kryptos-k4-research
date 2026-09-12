"""EXP-024  The Weltzeituhr test: preregistered, validated, and BLOCKED on data.

What this experiment is
-----------------------
Checkpoint D concluded that the surviving architecture is a long, low-entropy,
externally sourced, position-indexed keystream, and that the strongest concrete
candidate source is the historical Weltzeituhr - the object the BERLINCLOCK crib
names. This session tried to reconstruct that object well enough to run the test.

It could not be done. `data/weltzeituhr.json` records what was recovered and, more
importantly, what was not. Rather than guess the missing fields, this experiment
does three honest things:

  1. preregisters the reading procedures NOW, while the name list is unavailable,
     which is the cleanest possible preregistration - they cannot be tuned to data
     that does not exist here;
  2. validates the whole pipeline end to end on a STRUCTURALLY FAITHFUL SYNTHETIC
     clock with a planted keystream, proving the test would detect a real hit;
  3. states exactly which six fields must be supplied for the real test to run.

No historical name is invented anywhere. The synthetic clock uses deliberately
fake syllables so it can never be mistaken for reconstructed data.

Why the procedures are the ones they are
----------------------------------------
Each is motivated by the object: a person walks around a cylinder, so readings go
clockwise or anticlockwise; names sit in an upper and a lower band, so a reader
takes upper-then-lower, lower-then-upper, or alternates; a reader may circle the
whole upper band before the lower; a visitor in Berlin naturally starts at the
Berlin sector; and the object is also indexed by time zone, so UTC order is
natural. None was chosen because it improves a crib score - none has been run
against the cribs at all, because the data to do so does not exist here.
"""
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load, REPO_ROOT
from k4lib.conventions import all_conventions
from k4lib.alphabets import ALPHABETS, index_map
from k4lib.weltzeituhr import synthetic_clock, procedures

k4 = load()
cribs = k4.crib_positions()
positions = [i for i, _, _ in cribs]
conventions = all_conventions()
wz = json.load(open(os.path.join(REPO_ROOT, "data", "weltzeituhr.json")))

print("# EXP-024 Weltzeituhr test: preregistered, validated, blocked on data")
print(f"ciphertext sha256 {k4.sha256}\n")

print("## What the object model records as RECOVERED")
g = wz["geometry"]
print(f"   24 sectors, 15 degrees each; three-part cylinder      [{g['confidence']}]")
print(f"   upper and lower aluminium disks carry the city names  [{g['three_parts']['confidence']}]")
print(f"   the city cylinder is STATIC; the hour ring rotates     [{g['rotation']['confidence']}]")
print(f"   compass-rose mosaic at the base                        [presence HIGH]")
print(f"   lettering is STAMPED from punches/templates            [{wz['construction']['confidence']}]")
print(f"   1997 restoration under Hans-Joachim Kunsch, who also built it in 1969")
print()
print("## What is UNKNOWN, and therefore blocks the test")
for i, b in enumerate(wz["reconstruction_status"]["blocking_items"], 1):
    print(f"   {i}. {b}")
print()

print("## Preregistered reading procedures (defined before any data exists)")
clock = synthetic_clock(seed=1)
procs = procedures(clock, berlin_sector=13)
for name in procs:
    print(f"   {name}")
print(f"   total: {len(procs)} procedures")
print()

# ------------------------------------------------------------ validation
print("## End-to-end validation on a SYNTHETIC clock (fake names, real structure)")
cv0 = conventions[0]
tape = procs["cw/start0/ul"]
OFF = 137
ki = index_map(ALPHABETS["STD"])
planted_key = [ki[tape[(OFF + i) % len(tape)]] for i in range(97)]

# build a synthetic ciphertext from a synthetic plaintext under that keystream,
# keeping the real crib letters at the real crib positions
PT = ["X"] * 97
for i, p, _ in cribs:
    PT[i] = p
CT = "".join(cv0.encrypt_letter(p, k) for p, k in zip(PT, planted_key))
synth_cribs = [(i, p, CT[i]) for i, p, _ in cribs]

found = []
trials = 0
for pname, t in procs.items():
    L = len(t)
    for kalpha in ("STD", "KRY"):
        kk = index_map(ALPHABETS[kalpha])
        mv = [kk[c] for c in t]
        for direction in (1, -1):
            for o in range(L):
                stream = [mv[(o + direction * i) % L] for i in positions]
                for cv in conventions:
                    trials += 1
                    got = sum(1 for j, (i, p, c) in enumerate(synth_cribs)
                              if cv.key_index(p, c) == stream[j])
                    if got == 24:
                        found.append((pname, kalpha, direction, o, cv.name))
print(f"   planted: reading 'cw/start0/ul', STD alphabet, dir +1, offset {OFF}, {cv0.name}")
print(f"   alignments scanned: {trials:,}")
print(f"   exact 24/24 recoveries: {len(found)}")
for f in found[:3]:
    print(f"     {f}")
ctrl = any(f[0] == "cw/start0/ul" and f[3] == OFF and f[1] == "STD" for f in found)
print(f"   CONTROL {'PASSED' if ctrl else 'FAILED'} - the pipeline detects a genuine")
print("   Weltzeituhr-derived keystream when one is present.\n")

print("## Status of the real test")
print("   NOT RUN. The per-sector name list for 1988-89 is UNKNOWN and was not")
print("   guessed. Supplying the six blocking items above makes this experiment")
print("   executable immediately: replace synthetic_clock() with the real structure")
print("   and the same 22 procedures, 2 alphabets, 2 directions, every offset and 12")
print("   conventions run unchanged.")
print()
print(f"   Scale when it runs: ~{trials:,} alignments for a clock of this size, so the")
print("   multiple-testing correction is known in advance too. At 24 crib letters the")
print("   exact binomial tail governs, as in EXP-004 and EXP-023.")
print()
print("## Grade")
print("   UNTESTABLE WITH CURRENT PUBLIC DATA - in this environment. The modern")
print("   per-sector list IS published; it could not be retrieved here because the")
print("   network policy blocks direct page fetches and search summaries decline to")
print("   enumerate. This is an environment limit, NOT a claim that the data is")
print("   unavailable to a human researcher. The 1988-89 list additionally requires")
print("   the full 1997 change record, of which only three renames and four of the")
print("   twenty additions are documented in sources reached.")
sys.exit(0 if ctrl else 1)
