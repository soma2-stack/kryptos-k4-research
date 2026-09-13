"""Independent verification of the Checkpoint AC certificates.

Imports NOTHING from audit/checkpoint_AC.py and nothing from k4lib. It rebuilds the
model from data/k4.json and the saved certificates only, and it deliberately uses a
different method at every step:

  * SAT certificates are checked by RUNNING THE CIPHER FORWARD. The solver worked
    backwards from the ciphertext through an equality argument; this verifier takes
    the certificate's plaintext cells, performs the Trifid coordinate-row
    fractionation directly by building and slicing the coordinate rows, applies the
    certificate's outer map, and demands the result equal the K4 ciphertext
    character for character.

  * The UNSAT certificate is checked by BREADTH-FIRST CLOSURE over an explicit
    adjacency list rather than by the solver's union-find, re-deriving that the
    named ciphertext letters really are forced to share two axes, and then applying
    the pigeonhole count.

A SAT certificate proves only that the conditional architecture is compatible with
the ciphertext and the two public cribs. It is NOT a K4 solution.
"""
import gzip
import hashlib
import itertools
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K4 = json.load(open(os.path.join(ROOT, "data", "k4.json")))
CT = K4["ciphertext"]
CERTDIR = os.path.join(ROOT, "results", "checkpoint_AC")
ROWS = [(0, 4), (4, 35), (35, 66), (66, 97)]

PLAIN = {}
for cr in K4["confirmed_cribs"]:
    for j, ch in enumerate(cr["plaintext"]):
        PLAIN[cr["start"] + j] = ch

fails = []


def check(label, cond):
    if not cond:
        fails.append(label)
    print(f"   [{'PASS' if cond else 'FAIL'}] {label}")


def segments(period, reset):
    out = []
    for lo, hi in (ROWS if reset else [(0, 97)]):
        a = lo
        while a < hi:
            out.append((a, min(a + period, hi)))
            a = min(a + period, hi)
    return out


def trifid_forward(cells, period, reset):
    """Run the fractionation forward: build the three coordinate rows for each
    block, concatenate them, and cut the result into consecutive triples."""
    out = [None] * 97
    for a, b in segments(period, reset):
        rows = []
        for axis in range(3):
            rows.extend(cells[i][axis] for i in range(a, b))
        for j in range(b - a):
            out[a + j] = tuple(rows[3 * j:3 * j + 3])
    return out


print("## Checkpoint AC certificate verification (independent reimplementation)")
print(f"   ciphertext length {len(CT)}, distinct letters {len(set(CT))}, "
      f"known plaintext positions {len(PLAIN)}")
check("ciphertext uses all 26 letters", len(set(CT)) == 26)

summary = json.load(open(os.path.join(CERTDIR, "summary.json")))
ab = summary["ab_reproduction"]
check("AB sweep reproduction: 175 of 194 rejected", ab["rejected"] == 175)
check("AB continuous remainder matches the published list",
      ab["continuous"] == [5, 7, 10, 13, 14, 16, 23, 28, 29])
check("AB row-reset remainder matches the published list",
      ab["row_reset"] == [4, 7, 11, 14, 19, 20, 22, 23, 26, 28])

n_sat = n_unsat = 0
for cfg in summary["configurations"]:
    period, reset, status = cfg["period"], cfg["row_reset"], cfg["status"]
    tag = f"p={period:2d} {'row-reset' if reset else 'continuous'}"
    name = f"p{period:02d}_{'reset' if reset else 'cont'}.json"
    cert = json.load(open(os.path.join(CERTDIR, name)))
    check(f"{tag}: saved certificate agrees with the summary",
          cert["status"] == status and cert["period"] == period)

    if status == "SAT":
        n_sat += 1
        cells = [tuple(x) for x in cert["plaintext_cells"]]
        outer = {k: tuple(v) for k, v in cert["outer_map"].items()}
        check(f"{tag}: outer map covers 26 letters injectively",
              len(outer) == 26 and len(set(outer.values())) == 26)
        check(f"{tag}: every cell is a coordinate triple over 0..2",
              all(len(c) == 3 and all(x in (0, 1, 2) for x in c)
                  for c in list(cells) + list(outer.values())))
        # THE forward check: fractionate, read out, compare with K4
        produced = trifid_forward(cells, period, reset)
        inverse = {v: k for k, v in outer.items()}
        rebuilt = "".join(inverse.get(t, "?") for t in produced)
        check(f"{tag}: forward Trifid + outer map reproduces K4 exactly", rebuilt == CT)
        # crib semantics
        same = all(cells[i] == cells[j] for i in PLAIN for j in PLAIN
                   if PLAIN[i] == PLAIN[j])
        diff = all(cells[i] != cells[j] for i in PLAIN for j in PLAIN
                   if PLAIN[i] != PLAIN[j])
        check(f"{tag}: equal crib letters share a cell", same)
        check(f"{tag}: distinct crib letters occupy distinct cells", diff)
        check(f"{tag}: plaintext occupies at most 26 of the 27 cells",
              len(set(cells)) <= 26)

    elif status == "UNSAT":
        n_unsat += 1
        # Re-derive the forced sharing by BFS closure over an explicit adjacency
        # list, independently of the solver's union-find.
        adj = {}

        def link(x, y):
            adj.setdefault(x, set()).add(y)
            adj.setdefault(y, set()).add(x)

        # where each plaintext coordinate is read out to: v[pos][axis] -> (slot, ct letter)
        for a, b in segments(period, reset):
            L = b - a
            for j in range(L):
                for k in range(3):
                    m = 3 * j + k
                    link(("v", a + (m % L), m // L), ("T", k, CT[a + j]))
        # positions holding the same known plaintext letter share a cube cell
        by_letter = {}
        for i, ch in PLAIN.items():
            by_letter.setdefault(ch, []).append(i)
        for positions in by_letter.values():
            for i, j in itertools.combinations(positions, 2):
                for t in range(3):
                    link(("v", i, t), ("v", j, t))

        def component(seed):
            seen, stack = {seed}, [seed]
            while stack:
                cur = stack.pop()
                for nxt in adj.get(cur, ()):
                    if nxt not in seen:
                        seen.add(nxt)
                        stack.append(nxt)
            return seen

        # class ids from the BFS components (independent of the solver's union-find)
        alphabet = sorted(set(CT))
        seen_comp, cid = {}, {}
        for k in range(3):
            for l in alphabet:
                node = ("T", k, l)
                if node not in cid:
                    comp = component(node)
                    n = len(seen_comp)
                    seen_comp[n] = comp
                    for x in comp:
                        cid[x] = n
        tri = {l: tuple(cid[("T", k, l)] for k in range(3)) for l in alphabet}
        crib_tri = {}
        for ch, positions in by_letter.items():
            i = positions[0]
            crib_tri[ch] = tuple(cid[("v", i, t)] if ("v", i, t) in cid else
                                 cid.setdefault(("v", i, t), len(seen_comp) + t)
                                 for t in range(3))
        nclasses = max(max(tri.values(), key=max)) + 1
        nclasses = max(nclasses, max(max(v) for v in crib_tri.values()) + 1)

        if cert["reason"] == "pigeonhole_ternary_axis":
            det = cert["detail"]
            letters, slots = det["letters"], det["shared_axes"]
            check(f"{tag}: pigeonhole needs more than three letters", len(letters) > 3)
            for slot in slots:
                check(f"{tag}: axis {slot} of {','.join(letters)} is one component",
                      len({cid[("T", slot, l)] for l in letters}) == 1)
            free = [t for t in range(3) if t not in slots]
            check(f"{tag}: exactly one free axis remains", len(free) == 1)
            print(f"      -> {len(letters)} letters agree in axes {slots}; the injective")
            print(f"         outer map needs them pairwise distinct in axis {free[0]},")
            print(f"         which holds only 3 values. {len(letters)} > 3 -> UNSAT.")
        else:
            # SUPPLEMENTARY reproducibility record, not the proof of exhaustion.
            # The independent DFS above is the primary UNSAT verification. Replaying
            # the trace additionally confirms that every conflict the solver recorded
            # is real under this file's own constraints, which is a useful cross-check
            # on the solver's internals but is NOT by itself a proof that the solver's
            # tree was complete.
            check(f"{tag}: UNSAT reason is exhaustive search",
                  cert["reason"] == "exhaustive_backtracking")
            order, mark = [], set()
            for entry in cert.get("search_order_hint", []):
                key = (("T", entry[0], entry[1]) if entry[0] != "v"
                       else ("v", entry[1], entry[2]))
                c = cid.get(key)
                if c is not None and c not in mark:
                    mark.add(c)
                    order.append(c)
            check(f"{tag}: search order covers every class exactly once",
                  len(order) == cert["classes"])
            depth_of = {c: d for d, c in enumerate(order)}
            done_letter, done_crib, done_plain = {}, {}, {}
            for l in alphabet:
                done_letter.setdefault(max(depth_of[c] for c in tri[l]),
                                       []).append((l, tri[l]))
            for ch, t in crib_tri.items():
                done_crib.setdefault(max(depth_of[c] for c in t), []).append((ch, t))
            for t in sorted({tuple(cid[("v", i, k)] for k in range(3))
                             for i in range(97)}):
                done_plain.setdefault(max(depth_of[c] for c in t), []).append(t)
            weight = [[0] * len(order) for _ in range(3)]
            for l in alphabet:
                for k in range(3):
                    weight[k][tri[l][k]] += 1

            # ---------------------------------------------------------------
            # PRIMARY UNSAT VERIFICATION: an independent exhaustive DFS.
            #
            # Everything it searches over -- the classes, the seven constraint
            # families, the axis weights -- was rebuilt above in this file from
            # data/k4.json. It neither imports nor calls audit/checkpoint_AC.py, and
            # it does not read the solver's verdict or its conflict trace. The only
            # thing taken from the certificate is the VARIABLE ORDER, used purely as
            # a heuristic; variable order cannot change a SAT/UNSAT answer, only how
            # long the search takes. If this DFS finds a solution it reports SAT and
            # the check below fails, which is the outcome that would falsify
            # Checkpoint AC.
            # ---------------------------------------------------------------
            dfs_val = [-1] * len(order)
            dfs_axis = [[0, 0, 0] for _ in range(3)]
            dfs_cells, dfs_crib, dfs_plain = set(), set(), {}
            dfs_nodes = [0]

            def independent_dfs(d):
                dfs_nodes[0] += 1
                if d == len(order):
                    return True                      # a full assignment: SAT
                c = order[d]
                for v in (0, 1, 2):
                    # (7) axis multiplicity: an injection onto 26 of the 27 cells
                    # uses each value of each axis at most nine times
                    if any(dfs_axis[k][v] + weight[k][c] > 9 for k in range(3)):
                        continue
                    for k in range(3):
                        dfs_axis[k][v] += weight[k][c]
                    dfs_val[c] = v
                    got_l, got_c, got_p, ok = [], [], [], True
                    # (4) the outer readout is injective on ciphertext letters
                    for l, t in done_letter.get(d, ()):
                        cell = tuple(dfs_val[x] for x in t)
                        if cell in dfs_cells:
                            ok = False
                            break
                        dfs_cells.add(cell)
                        got_l.append(cell)
                    # (5) distinct known plaintext letters occupy distinct cells
                    if ok:
                        for ch, t in done_crib.get(d, ()):
                            cell = tuple(dfs_val[x] for x in t)
                            if cell in dfs_crib:
                                ok = False
                                break
                            dfs_crib.add(cell)
                            got_c.append(cell)
                    # (6) the plaintext alphabet must fit in the cube
                    if ok:
                        for t in done_plain.get(d, ()):
                            cell = tuple(dfs_val[x] for x in t)
                            dfs_plain[cell] = dfs_plain.get(cell, 0) + 1
                            got_p.append(cell)
                        if len(dfs_plain) > 26:
                            ok = False
                    if ok and independent_dfs(d + 1):
                        return True
                    for cell in got_l:
                        dfs_cells.discard(cell)
                    for cell in got_c:
                        dfs_crib.discard(cell)
                    for cell in got_p:
                        dfs_plain[cell] -= 1
                        if not dfs_plain[cell]:
                            del dfs_plain[cell]
                    dfs_val[c] = -1
                    for k in range(3):
                        dfs_axis[k][v] -= weight[k][c]
                return False

            found = independent_dfs(0)
            check(f"{tag}: INDEPENDENT exhaustive DFS confirms UNSAT", not found)
            print(f"      -> independent DFS exhausted the whole tree in "
                  f"{dfs_nodes[0]:,} nodes (solver reported {cert['nodes']:,})")
            if found:
                print("      *** the independent search found a solution: "
                      "Checkpoint AC requires correction ***")

            val = [-1] * len(order)
            axis_used = [[0, 0, 0] for _ in range(3)]
            used, used_crib, plain_count = set(), set(), {}
            stack = []          # (depth, value, added_letter, added_crib, added_plain)
            blob = gzip.open(os.path.join(CERTDIR, cert["refutation_trace_file"]),
                             "rt").read()
            check(f"{tag}: refutation trace matches its recorded sha256",
                  hashlib.sha256(blob.encode()).hexdigest()
                  == cert["refutation_trace_sha256"])
            trace = [json.loads(line) for line in blob.split("\n")]
            check(f"{tag}: trace length matches the certificate",
                  len(trace) == cert["refutation_trace_steps"])
            pos_in = [0]
            bad_trace = []

            def undo_to(d):
                while stack and stack[-1][0] >= d:
                    dd, vv, al, ac, ap = stack.pop()
                    for cell in al:
                        used.discard(cell)
                    for cell in ac:
                        used_crib.discard(cell)
                    for cell in ap:
                        plain_count[cell] -= 1
                        if not plain_count[cell]:
                            del plain_count[cell]
                    for k in range(3):
                        axis_used[k][vv] -= weight[k][order[dd]]
                    val[order[dd]] = -1

            expect = 0          # next depth the trace must be speaking about
            for d, v, outcome in trace:
                undo_to(d)
                if len(stack) != d:
                    bad_trace.append(("depth mismatch", d, len(stack)))
                    break
                c = order[d]
                if any(axis_used[k][v] + weight[k][c] > 9 for k in range(3)):
                    if outcome != "axis_overflow":
                        bad_trace.append(("axis conflict not declared", d, v, outcome))
                        break
                    continue
                if outcome == "axis_overflow":
                    bad_trace.append(("declared axis conflict does not hold", d, v))
                    break
                for k in range(3):
                    axis_used[k][v] += weight[k][c]
                val[c] = v
                al, ac, ap, hit = [], [], [], None
                for l, t in done_letter.get(d, ()):
                    cell = tuple(val[x] for x in t)
                    if cell in used:
                        hit = "outer_cell_reused"
                        break
                    used.add(cell)
                    al.append(cell)
                if hit is None:
                    for ch, t in done_crib.get(d, ()):
                        cell = tuple(val[x] for x in t)
                        if cell in used_crib:
                            hit = "crib_cell_reused"
                            break
                        used_crib.add(cell)
                        ac.append(cell)
                if hit is None:
                    for t in done_plain.get(d, ()):
                        cell = tuple(val[x] for x in t)
                        plain_count[cell] = plain_count.get(cell, 0) + 1
                        ap.append(cell)
                    if len(plain_count) > 26:
                        hit = "plaintext_cells_exceed_26"
                stack.append((d, v, al, ac, ap))
                if hit is not None:
                    if outcome != hit:
                        bad_trace.append(("wrong conflict label", d, v, outcome, hit))
                        break
                    undo_to(d)
                elif outcome != "descend":
                    bad_trace.append(("claimed conflict does not hold", d, v, outcome))
                    break
            check(f"{tag}: every step of the refutation trace re-derives here",
                  not bad_trace)
            if bad_trace:
                print(f"      first discrepancy: {bad_trace[0]}")
            # Per-prefix completeness. The earlier form of this check only asked
            # whether values 0, 1 and 2 each appeared SOMEWHERE at each depth, which
            # does not establish tree exhaustion: a trace could omit one child under
            # one prefix and still satisfy it. This version walks the trace as a tree
            # and requires that every internal node accounts for all three branches
            # under its own prefix.
            prefix, branches, malformed = [], {}, []
            for d, v, outcome in trace:
                del prefix[d:]
                key = tuple(prefix)
                branches.setdefault(key, set()).add(v)
                if outcome == "descend":
                    prefix.append(v)
            bad_prefix = [k for k, vs in branches.items() if vs != {0, 1, 2}]
            check(f"{tag}: every prefix in the trace accounts for all three branches",
                  not bad_prefix)
            check(f"{tag}: the trace's root prefix is exhausted",
                  branches.get((), set()) == {0, 1, 2})
            print(f"      -> supplementary trace replay: {len(trace):,} steps, "
                  f"{len(branches):,} distinct prefixes, all branches accounted for")

    else:
        fails.append(f"{tag}: unexpected status {status}")

check("every configuration resolved (no solver-incomplete cases)",
      n_sat + n_unsat == 19)
print(f"\n   {n_sat} SAT certificates reconstructed, {n_unsat} UNSAT certificate re-derived")
print(f"\n{'ALL CHECKS PASSED' if not fails else 'FAILURES: ' + str(fails)}")
sys.exit(1 if fails else 0)
