"""EXP-013  Trifid, at the periods the cribs can actually decide.

EXP-012 showed that a 27-cell trifid cube (10^28.0 arrangements) is out-reached by
crib constraints only at periods 2 and 3, where enough whole blocks fall inside a
crib. Those two periods are tested here; every other period is deliberately left
untested, because EXP-012 showed a fit there would carry no information.

Mechanism
---------
Each letter sits in a 3x3x3 cube at coordinates (a,b,c). For a block of d
plaintext letters the coordinates are written as three rows and read off in threes:

    d=3   seq = a1a2a3 b1b2b3 c1c2c3 -> C1=(a1,a2,a3) C2=(b1,b2,b3) C3=(c1,c2,c3)
    d=2   seq = a1a2 b1b2 c1c2       -> C1=(a1,a2,b1) C2=(b2,c1,c2)

So the coordinates of every ciphertext letter in a fully known block are forced by
the coordinates of its plaintext letters. The search is therefore constraint
propagation over a bijection between 27 symbols and 27 cells, not blind enumeration.

Completeness
------------
Blocks are taken most-constrained-first: at each step the block with the fewest
still-unassigned plaintext letters is processed next, so blocks whose letters are
already fixed act as pure checks and prune immediately. Any run that hits the node
cap is reported as INCOMPLETE and counts as heuristic failure, never as elimination.
"""
import sys, os, itertools, random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from k4lib.data import load

NODE_CAP = 300_000_000
k4 = load()
C = k4.ciphertext
N = len(C)
Pmap = {i: p for i, p, _ in k4.crib_positions()}
CELLS = [(a, b, c) for a in range(3) for b in range(3) for c in range(3)]


def outputs(d, coords):
    seq = [x[0] for x in coords] + [x[1] for x in coords] + [x[2] for x in coords]
    return [tuple(seq[3 * j:3 * j + 3]) for j in range(d)]


def blocks_for(d, align, pmap, n):
    return [s for s in range(align, n - d + 1, d) if all(s + t in pmap for t in range(d))]


def search(d, align, pmap, ct, n, cap=NODE_CAP):
    blks = blocks_for(d, align, pmap, n)
    if not blks:
        return 0, 0, blks, False
    nodes = 0
    sols = 0
    capped = [False]

    def unassigned(s, assign):
        return [L for L in dict.fromkeys(pmap[s + t] for t in range(d)) if L not in assign]

    def rec(remaining, assign, used):
        nonlocal nodes, sols
        if capped[0]:
            return
        if not remaining:
            sols += 1
            return
        best = min(remaining, key=lambda s: len(unassigned(s, assign)))
        rest = [s for s in remaining if s != best]
        plain = [pmap[best + t] for t in range(d)]
        unknown = unassigned(best, assign)
        free = [c for c in CELLS if c not in used]
        for combo in itertools.permutations(free, len(unknown)):
            nodes += 1
            if nodes > cap:
                capped[0] = True
                return
            a2 = dict(assign)
            u2 = set(used)
            for L, cell in zip(unknown, combo):
                a2[L] = cell
                u2.add(cell)
            ok = True
            for t, ocell in enumerate(outputs(d, [a2[L] for L in plain])):
                cl = ct[best + t]
                if cl in a2:
                    if a2[cl] != ocell:
                        ok = False
                        break
                elif ocell in u2:
                    ok = False
                    break
                else:
                    a2[cl] = ocell
                    u2.add(ocell)
            if ok:
                rec(rest, a2, u2)

    rec(blks, {}, set())
    return sols, nodes, blks, capped[0]


print("# EXP-013 trifid at testable periods")
print(f"ciphertext sha256 {k4.sha256}\n")

print("## Positive control: plant a cube, encipher, recover it")
random.seed(20260912)
symbols = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + ["+"]
cube = dict(zip(symbols, random.sample(CELLS, 27)))
inv = {v: k for k, v in cube.items()}
pt = "EASTNORTHEASTXXBERLINCLOCKXXNORTHEASTBERLIN"
d = 3
ct = []
for s in range(0, len(pt) - d + 1, d):
    ct.extend(inv[o] for o in outputs(d, [cube[ch] for ch in pt[s:s + d]]))
ct = "".join(ct)
cpmap = {i: ch for i, ch in enumerate(pt[:len(ct)])}
nsol, nodes, blks, capped = search(3, 0, cpmap, ct, len(ct))
print(f"   planted cube, {len(blks)} usable blocks -> solutions {nsol} "
      f"(nodes {nodes:,}{', CAPPED' if capped else ''})")
control_ok = nsol > 0 and not capped
print(f"   CONTROL {'PASSED' if control_ok else 'FAILED'}\n")

print("## K4")
total = 0
incomplete = []
for d in (2, 3):
    for align in range(d):
        nsol, nodes, blks, capped = search(d, align, Pmap, C, N)
        total += nodes
        status = "INCOMPLETE (node cap) - heuristic failure, NOT elimination" \
            if capped else "exhaustive"
        print(f"   period {d} align {align}: blocks {len(blks):<2} "
              f"covered {len(blks)*d:<2} nodes {nodes:>13,}  solutions {nsol}"
              f"  [{status}]", flush=True)
        if capped:
            incomplete.append((d, align))

print(f"\n   total nodes: {total:,} (cap {NODE_CAP:,} per run)")
if incomplete:
    print(f"   INCOMPLETE runs: {incomplete}")
    print("   Those alignments are reported as INCONCLUSIVE, not negative.")
else:
    print("   Every run completed within the cap: each is an exhaustive")
    print("   elimination, not a failed search.")
print("   Periods 4+ deliberately not searched: EXP-012 shows the cube has more")
print("   freedom there than the cribs constrain, so a fit would mean nothing.")
sys.exit(0 if control_ok else 1)
