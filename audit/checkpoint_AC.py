"""Checkpoint AC — exact finite CSP closure of the 19 residual Trifid configurations.

Conditional model (NO historical source selects any of it):

    plaintext
      -> Trifid-style coordinate-row fractionation on a shared 3x3x3 cube,
         origin zero, given period, continuous OR physical-row reset,
         shortened terminal blocks
      -> ONE fixed injective readout on the used cube cells
      -> ciphertext

Key reduction. The outer map is a single injection, so equal ciphertext letters
force equal intermediate cells and unequal ciphertext letters force unequal cells.
Writing T[l] for the cell that ciphertext letter l comes from, the intermediate
sequence is X[i] = T[C[i]]. Inverting the coordinate-row concatenation then makes
EVERY plaintext coordinate v[pos][axis] a copy of one component of one T[l]. So the
whole architecture is determined by T, and the search is over T alone.

The remaining constraints are exactly:
  (a) positions holding the same known plaintext letter share a cell,
  (b) positions holding distinct known plaintext letters take distinct cells,
  (c) T is injective  (26 ciphertext letters -> 26 distinct cells of 27),
  (d) the plaintext occupies at most 26 distinct cells, so a 26-letter plaintext
      alphabet assignment exists.

(a) is imposed statically by union-find, leaving free classes over {0,1,2}; the
search is an exhaustive backtracking over those classes with two prunings:
  - axis multiplicity: an injection onto 26 of 27 cells uses each value of each
    axis at most 9 times, so no value may be forced on more than 9 letters in one
    axis;
  - incremental all-different on completed cells.

Exhaustion is complete: UNSAT here is a real UNSAT for the stated model, and SAT
produces a certificate that audit/checkpoint_AC_verify.py reconstructs from
scratch. A SAT result means only that the conditional architecture is compatible
with the ciphertext and the two public cribs. It is NOT a K4 solution and NOT
evidence that K4 uses Trifid.

Standard library only. Writes results/checkpoint_AC/*.json.
"""
import gzip
import hashlib
import itertools
import json
import os
import sys
import time
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K4 = json.load(open(os.path.join(ROOT, "data", "k4.json")))
CT = K4["ciphertext"]
ROWS = [(0, 4), (4, 35), (35, 66), (66, 97)]
LETTERS = sorted(set(CT))

PLAIN = {}
for _cr in K4["confirmed_cribs"]:
    assert CT[_cr["start"]:_cr["start"] + len(_cr["plaintext"])] == _cr["ciphertext_segment"]
    for _j, _ch in enumerate(_cr["plaintext"]):
        PLAIN[_cr["start"] + _j] = _ch

# the 19 configurations left UNRESOLVED by the Checkpoint AB propagation sweep,
# independently reproduced in this file by reproduce_ab_sweep()
CONFIGS = ([(d, False) for d in (5, 7, 10, 13, 14, 16, 23, 28, 29)]
           + [(d, True) for d in (4, 7, 11, 14, 19, 20, 22, 23, 26, 28)])


def blocks(period, reset):
    out = []
    for lo, hi in (ROWS if reset else [(0, 97)]):
        a = lo
        while a < hi:
            b = min(a + period, hi)
            out.append((a, b))
            a = b
    return out


def coordinate_source(period, reset):
    """v[(pos, axis)] = (component index, ciphertext letter) — v is determined by T.

    Within a block of length L the coordinate rows are concatenated as
    stream[m] = v[a + (m mod L)][m // L], and regrouped as X[a+j][k] = stream[3j+k]
    with X[a+j] = T[C[a+j]].
    """
    src = {}
    for a, b in blocks(period, reset):
        L = b - a
        for j in range(L):
            for k in range(3):
                m = 3 * j + k
                src[(a + (m % L), m // L)] = (k, CT[a + j])
    return src


class Union:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        self.parent.setdefault(x, x)
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            self.parent[a] = b


def build(period, reset):
    """Static union-find, then class-indexed triples for letters and positions."""
    src = coordinate_source(period, reset)
    assert len(src) == 97 * 3
    uf = Union()
    by_letter = {}
    for i, ch in PLAIN.items():
        by_letter.setdefault(ch, []).append(i)
    for positions in by_letter.values():
        for i, j in itertools.combinations(positions, 2):
            for t in range(3):
                uf.union(src[(i, t)], src[(j, t)])
    for k in range(3):
        for letter in LETTERS:
            uf.find((k, letter))
    reps = sorted({uf.find((k, l)) for k in range(3) for l in LETTERS}, key=str)
    index = {c: n for n, c in enumerate(reps)}
    letter_classes = [tuple(index[uf.find((k, l))] for k in range(3)) for l in LETTERS]
    position_classes = {i: tuple(index[uf.find(src[(i, t)])] for t in range(3))
                        for i in range(97)}
    return len(reps), letter_classes, position_classes, by_letter


def intermediate_expr(period, reset):
    """X[i] as a tuple of plaintext-coordinate symbols (position, axis).

    This is the dual of coordinate_source(): it expresses the INTERMEDIATE cell at
    each position in terms of plaintext coordinates, which is the formulation the
    Checkpoint AB propagation sweep uses.
    """
    expr = {}
    for a, b in blocks(period, reset):
        L = b - a
        stream = [(i, t) for t in range(3) for i in range(a, b)]
        for j, i in enumerate(range(a, b)):
            expr[i] = tuple(stream[3 * j:3 * j + 3])
    return expr


def reproduce_ab_sweep():
    """Independent re-derivation of the Checkpoint AB necessary-condition sweep.

    Sound one-sided propagation only: equal ciphertext forces equal intermediate
    cells under one injective outer map, and positions sharing a known plaintext
    letter share a cube cell. UNRESOLVED is not SAT.
    """
    by_letter = {}
    for i, ch in PLAIN.items():
        by_letter.setdefault(ch, []).append(i)
    unresolved = {}
    for reset in (False, True):
        alive = []
        for period in range(1, 98):
            expr = intermediate_expr(period, reset)
            uf = Union()
            for positions in by_letter.values():
                for i, j in itertools.combinations(positions, 2):
                    for t in range(3):
                        uf.union((i, t), (j, t))
            for i, j in itertools.combinations(range(97), 2):
                if CT[i] == CT[j]:
                    for x, y in zip(expr[i], expr[j]):
                        uf.union(x, y)
            canon = {i: tuple(uf.find(x) for x in expr[i]) for i in range(97)}
            ok = True
            for i, j in itertools.combinations(range(97), 2):
                if CT[i] != CT[j] and canon[i] == canon[j]:
                    ok = False
                    break
            if ok:
                firsts = {ch: ps[0] for ch, ps in by_letter.items()}
                for a, b in itertools.combinations(sorted(firsts), 2):
                    ia, ib = firsts[a], firsts[b]
                    if all(uf.find((ia, t)) == uf.find((ib, t)) for t in range(3)):
                        ok = False
                        break
            if ok:
                alive.append(period)
        unresolved[reset] = alive
    return unresolved


def solve(period, reset, node_limit=None):
    m, letter_classes, position_classes, by_letter = build(period, reset)
    firsts = {ch: ps[0] for ch, ps in by_letter.items()}

    for a, b in itertools.combinations(sorted(firsts), 2):
        if position_classes[firsts[a]] == position_classes[firsts[b]]:
            return dict(status="UNSAT", reason="crib_cells_collapse",
                        detail=[a, b], nodes=0, classes=m)
    for a, b in itertools.combinations(range(26), 2):
        if letter_classes[a] == letter_classes[b]:
            return dict(status="UNSAT", reason="outer_map_not_injective",
                        detail=[LETTERS[a], LETTERS[b]], nodes=0, classes=m)

    # Pigeonhole certificate. If four or more ciphertext letters are forced onto the
    # same class in two of the three axes, their cells already agree there, so the
    # injective outer map needs them pairwise distinct in the one remaining axis --
    # which holds only three values. Four letters cannot fit.
    for slots in itertools.combinations(range(3), 2):
        free = [t for t in range(3) if t not in slots][0]
        groups = {}
        for li, triple in enumerate(letter_classes):
            groups.setdefault((triple[slots[0]], triple[slots[1]]), []).append(li)
        for key, members in groups.items():
            if len(members) > 3:
                return dict(status="UNSAT", reason="pigeonhole_ternary_axis",
                            nodes=0, classes=m,
                            detail={"letters": [LETTERS[li] for li in members],
                                    "shared_axes": list(slots),
                                    "shared_classes": list(key),
                                    "free_axis": free,
                                    "values_available": 3})

    # per class and axis, how many letters take their axis value from that class
    axis_weight = [Counter() for _ in range(3)]
    for triple in letter_classes:
        for k in range(3):
            axis_weight[k][triple[k]] += 1

    # Variable order matters enormously: the binding constraint is that the 26
    # letters occupy 26 distinct cells, and that test can only fire once all three
    # classes of a letter are assigned. So order the letters greedily by overlap
    # with what is already placed, and emit each letter's classes in that order.
    # Every step then completes at least one cell and the all-different prunes.
    use = Counter()
    for triple in letter_classes:
        for c in triple:
            use[c] += 1
    remaining = set(range(26))
    placed, order, seen = [], [], set()
    while remaining:
        best = max(remaining, key=lambda li: (
            sum(1 for c in set(letter_classes[li]) if c in seen),
            sum(use[c] for c in set(letter_classes[li])), -li))
        remaining.discard(best)
        placed.append(best)
        for c in letter_classes[best]:
            if c not in seen:
                seen.add(c)
                order.append(c)
    for c in range(m):                       # classes touched only by plaintext cells
        if c not in seen:
            order.append(c)
    assert sorted(order) == list(range(m))
    depth_of = {c: d for d, c in enumerate(order)}

    letters_done = {}
    for li, triple in enumerate(letter_classes):
        letters_done.setdefault(max(depth_of[c] for c in triple), []).append(li)
    plain_cells = sorted(set(position_classes.values()))
    plain_done = {}
    for pi, triple in enumerate(plain_cells):
        plain_done.setdefault(max(depth_of[c] for c in triple), []).append(pi)

    # Constraint (b): the 13 distinct known plaintext letters are distinct letters of
    # the cube, so they must occupy distinct cells. Enforced incrementally during the
    # search -- checking only the static class triples would miss two different class
    # triples that happen to take the same values.
    crib_triples = sorted({position_classes[ps[0]] for ps in by_letter.values()})
    assert len(crib_triples) == len(by_letter)
    crib_done = {}
    for ci, triple in enumerate(crib_triples):
        crib_done.setdefault(max(depth_of[c] for c in triple), []).append(ci)

    value = [-1] * m
    # axis_used[k][v] = letters already forced to value v on axis k
    axis_used = [[0, 0, 0] for _ in range(3)]
    cells = set()
    crib_seen = set()
    plain_seen = Counter()
    nodes = [0]
    trace = []                    # replayable refutation trace: (depth, value, outcome)

    def recurse(depth):
        nodes[0] += 1
        if node_limit and nodes[0] > node_limit:
            raise TimeoutError
        if depth == m:
            return True
        c = order[depth]
        for v in (0, 1, 2):
            bad = False
            for k in range(3):
                w = axis_weight[k][c]
                if w and axis_used[k][v] + w > 9:      # injection onto 26 of 27 cells
                    bad = True
                    break
            if bad:
                trace.append((depth, v, "axis_overflow"))
                continue
            for k in range(3):
                axis_used[k][v] += axis_weight[k][c]
            value[c] = v
            added, added_plain, added_crib, ok = [], [], [], True
            why = None
            for li in letters_done.get(depth, ()):
                cell = tuple(value[cc] for cc in letter_classes[li])
                if cell in cells:
                    ok = False
                    why = "outer_cell_reused"
                    break
                cells.add(cell)
                added.append(cell)
            if ok:
                for ci in crib_done.get(depth, ()):
                    cell = tuple(value[cc] for cc in crib_triples[ci])
                    if cell in crib_seen:
                        ok = False
                        why = "crib_cell_reused"
                        break
                    crib_seen.add(cell)
                    added_crib.append(cell)
            if ok:
                for pi in plain_done.get(depth, ()):
                    cell = tuple(value[cc] for cc in plain_cells[pi])
                    plain_seen[cell] += 1
                    added_plain.append(cell)
                if len(plain_seen) > 26:               # plaintext alphabet must fit
                    ok = False
                    why = "plaintext_cells_exceed_26"
            if not ok:
                trace.append((depth, v, why))
            else:
                trace.append((depth, v, "descend"))
                if recurse(depth + 1):
                    return True
            for cell in added:
                cells.discard(cell)
            for cell in added_crib:
                crib_seen.discard(cell)
            for cell in added_plain:
                plain_seen[cell] -= 1
                if not plain_seen[cell]:
                    del plain_seen[cell]
            value[c] = -1
            for k in range(3):
                axis_used[k][v] -= axis_weight[k][c]
        return False

    try:
        sat = recurse(0)
    except TimeoutError:
        return dict(status="SOLVER_INCOMPLETE", reason="node_limit",
                    nodes=nodes[0], classes=m)
    if not sat:
        # Portable search-order hint. Each class is named by one (axis, ciphertext
        # letter) pair that belongs to it, so an independent verifier that rebuilds
        # the classes by its own route can map the order onto its own numbering.
        # The hint only orders variables; the verifier still derives every constraint
        # itself and still searches exhaustively, so it cannot import a wrong verdict.
        name_of = {}
        for li, triple in enumerate(letter_classes):
            for k in range(3):
                name_of.setdefault(triple[k], (k, LETTERS[li]))
        for i in range(97):
            for t in range(3):
                name_of.setdefault(position_classes[i][t], ("v", i, t))
        hint = [list(name_of[c]) for c in order]
        return dict(status="UNSAT", reason="exhaustive_backtracking",
                    nodes=nodes[0], classes=m, search_order_hint=hint,
                    refutation_trace=[[d, v, o] for d, v, o in trace])
    outer = {LETTERS[li]: [value[c] for c in letter_classes[li]] for li in range(26)}
    plain = [[value[c] for c in position_classes[i]] for i in range(97)]
    crib_cells = {ch: plain[ps[0]] for ch, ps in by_letter.items()}
    # Deliberately NOT recorded: any letter labelling of the 73 unknown positions.
    # Every bijection from the unused cells to the unused letters completes the model
    # equally well, so such a labelling would carry no information and would amount to
    # manufacturing a plaintext candidate.
    return dict(status="SAT", reason="exhaustive_backtracking", nodes=nodes[0],
                classes=m, outer_map=outer, plaintext_cells=plain,
                crib_cells=crib_cells,
                distinct_plaintext_cells=len({tuple(x) for x in plain}))


def main():
    started = time.time()
    print("## independent reproduction of the Checkpoint AB sweep")
    ab = reproduce_ab_sweep()
    print(f"   continuous unresolved  : {ab[False]}")
    print(f"   row-reset  unresolved  : {ab[True]}")
    rejected = (97 - len(ab[False])) + (97 - len(ab[True]))
    print(f"   rejected {rejected} of 194 audited configurations")
    assert ab[False] == [5, 7, 10, 13, 14, 16, 23, 28, 29]
    assert ab[True] == [4, 7, 11, 14, 19, 20, 22, 23, 26, 28]
    assert rejected == 175

    out = {"ciphertext_sha256": hashlib.sha256(CT.encode()).hexdigest(),
           "ab_reproduction": {"continuous": ab[False], "row_reset": ab[True],
                               "rejected": rejected, "audited": 194},
           "configurations": []}
    print("\n## exact finite CSP over the 19 residual configurations")
    limit = int(os.environ.get("AC_NODE_LIMIT", "40000000"))
    for period, reset in CONFIGS:
        t0 = time.time()
        res = solve(period, reset, node_limit=limit)
        res.update(period=period, row_reset=reset, seconds=round(time.time() - t0, 2))
        out["configurations"].append(res)
        tag = f"p={period:2d} {'row-reset ' if reset else 'continuous'}"
        print(f"   {tag} -> {res['status']:17s} nodes={res['nodes']:>10,} "
              f"{res['seconds']:7.2f}s")
        stem = f"p{period:02d}_{'reset' if reset else 'cont'}"
        outdir = os.path.join(ROOT, "results", "checkpoint_AC")
        # Refutation traces are large, so they go to a gzipped sidecar (the same
        # convention EXP-034/035 use), with a hash recorded in the certificate.
        tr = res.pop("refutation_trace", None)
        if tr is not None:
            blob = "\n".join(json.dumps(step, separators=(",", ":")) for step in tr)
            with gzip.open(os.path.join(outdir, stem + ".trace.jsonl.gz"), "wt") as fh:
                fh.write(blob)
            res["refutation_trace_file"] = stem + ".trace.jsonl.gz"
            res["refutation_trace_steps"] = len(tr)
            res["refutation_trace_sha256"] = hashlib.sha256(blob.encode()).hexdigest()
        json.dump(res, open(os.path.join(outdir, stem + ".json"), "w"),
                  indent=2, sort_keys=True)

    counts = Counter(c["status"] for c in out["configurations"])
    out["summary"] = dict(counts)
    print(f"\n   summary: {dict(counts)}  ({time.time() - started:.1f}s total)")
    json.dump(out, open(os.path.join(ROOT, "results", "checkpoint_AC", "summary.json"),
                        "w"), indent=2, sort_keys=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
