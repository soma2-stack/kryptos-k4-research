"""Checkpoint AB: deterministic necessary-condition audit, not EXP-040.

Only the supplied ciphertext and two cribs are used. stdout is deterministic JSON.
Symbolic survivors are NOT SAT certificates. No unknown plaintext is filled.
"""
import hashlib
import itertools as it
import json
from collections import defaultdict

C = 'OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR'
P = dict(list(enumerate('EASTNORTHEAST', 21)) + list(enumerate('BERLINCLOCK', 63)))
ROWS = [(0, 4), (4, 35), (35, 66), (66, 97)]


def consistent(values, ct, schedule=lambda i: 0):
    """Exact existence of injective maps on supplied concrete intermediate values."""
    forward, inverse = {}, {}
    for i, x in sorted(values.items()):
        r, y = schedule(i), ct[i]
        if (r, x) in forward and forward[r, x] != y:
            return False
        if (r, y) in inverse and inverse[r, y] != x:
            return False
        forward[r, x], inverse[r, y] = y, x
    return True


def expressions(dim, period, phase=0, reset=False, axes=None, pmap=P):
    """Coordinate-row concatenation, regroup into dim-tuples; shortened end blocks.

    Unknown letters have independent coordinate variables per position, a relaxation.
    A positive phase gives a shortened first block; later blocks have full period.
    """
    axes = tuple(range(dim)) if axes is None else axes
    result = {}
    for lo, hi in ROWS if reset else [(0, 97)]:
        cuts = [lo] + list(range(lo + (phase or period), hi, period)) + [hi]
        for a, b in zip(cuts, cuts[1:]):
            stream = [(pmap.get(i, '@' + str(i)), axis)
                      for axis in axes for i in range(a, b)]
            for j, i in enumerate(range(a, b)):
                result[i] = tuple(stream[dim*j:dim*(j+1)])
    return result


def symbolic(expr, q, crib=P, ct=C):
    """Union forced coordinate equalities from equal C in the same mask residue.

    Check collapsed unequal ciphertext tuples and collapsed distinct input cells.
    This is sound UNSAT propagation, not a complete finite-domain solver.
    """
    parent = {}
    def find(x):
        parent.setdefault(x, x)
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[max(a, b)] = min(a, b)
    pairs = list(it.combinations(range(97), 2))
    for i, j in pairs:
        if i % q == j % q and ct[i] == ct[j]:
            for a, b in zip(expr[i], expr[j]):
                union(a, b)
    canon = {i: tuple(find(x) for x in v) for i, v in expr.items()}
    for i, j in pairs:
        if i % q == j % q and ct[i] != ct[j] and canon[i] == canon[j]:
            return {'status': 'UNSAT', 'reason': 'output_collision', 'positions': [i, j]}
    dim = len(expr[0])
    for a, b in it.combinations(sorted(set(crib.values())), 2):
        if all(find((a, t)) == find((b, t)) for t in range(dim)):
            return {'status': 'UNSAT', 'reason': 'input_cells_collapse', 'letters': [a, b]}
    return {'status': 'UNRESOLVED'}


def groups(values):
    out = defaultdict(list)
    for i, x in sorted(values.items()):
        out[x].append(i)
    return dict(out)


def main():
    assert len(C) == 97 and len(set(C)) == 26 and len(P) == 24
    assert consistent({0: 1, 1: 2, 2: 1}, 'ABA')
    assert not consistent({0: 1, 1: 2, 2: 1}, 'ABB')
    assert not consistent({0: 1, 1: 2}, 'AA')
    assert consistent({0: 1, 1: 2}, 'AA', lambda i: i % 2)
    symbolic_controls = 0
    for dim, side in [(2,5),(3,3)]:
        alphabet = sorted(set(P.values()))
        cells = list(it.product(range(side), repeat=dim))
        square = dict(zip(alphabet,cells))
        for d in [2,3,4,17,97]:
            for reset in [False,True]:
                for axes in it.permutations(range(dim)):
                    ex = expressions(dim,d,reset=reset,axes=axes)
                    # Synthetic cell assignments only, not a K4 plaintext completion.
                    val = lambda x: square[x[0]][x[1]] if x[0] in square else cells[int(x[0][1:]) % len(cells)][x[1]]
                    ct = [tuple(val(x) for x in ex[i]) for i in range(97)]
                    assert symbolic(ex,1,ct=ct)['status']=='UNRESOLVED'
                    symbolic_controls += 1
    # Independent concrete coordinate implementation checks every symbolic dependency.
    for dim, side in [(2, 5), (3, 3)]:
        for d in range(1, 98):
            for reset in [False, True]:
                ex = expressions(dim, d, reset=reset)
                assignment = {x: (ord(x[0][-1]) + x[1]) % side
                              for v in ex.values() for x in v}
                for lo, hi in ROWS if reset else [(0, 97)]:
                    for a in range(lo, hi, d):
                        b = min(a+d, hi)
                        coords = [[assignment[P.get(i, '@'+str(i)), t]
                                   for t in range(dim)] for i in range(a,b)]
                        flat = sum(([v[t] for v in coords] for t in range(dim)), [])
                        assert [tuple(assignment[x] for x in ex[i]) for i in range(a,b)] == [tuple(flat[t:t+dim]) for t in range(0,len(flat),dim)]
    periods = []
    for q in range(1, 98):
        g = groups({i: i % q for i in P})
        pairs = [(i,j) for v in g.values() for i,j in it.combinations(v,2)]
        periods.append({'q': q, 'additive_equalities_if_values_known':24-len(g),
                        'pair_comparisons':len(pairs),
                        'cross_crib_pairs':sum(i < 34 and j >= 63 for i,j in pairs)})
    digraphs = {i:P[i]+P[i+1] for i in P if i+1 in P}
    pair_audit = []
    for phase in [0,1]:
        starts = [i for i in digraphs if i % 2 == phase]
        inputs = [digraphs[i] for i in starts]
        outputs = [C[i:i+2] for i in starts]
        pair_audit.append({'phase':phase, 'starts':starts,
                           'unique_inputs':len(set(inputs)),
                           'unique_outputs':len(set(outputs)),
                           'doubled_output_starts':[i for i in starts if C[i]==C[i+1]]})
    sweep = []
    # All message-length-distinct periods, origin fixed, both physical hypotheses.
    for dim in [2,3]:
        for reset in [False,True]:
            for d in range(1,98):
                ex = expressions(dim,d,reset=reset)
                known = [i for i,v in ex.items() if all(not a.startswith('@') for a,_ in v)]
                row = {'dim':dim,'period':d,'row_reset':reset,
                       'known_output_positions':known, **symbolic(ex,1)}
                sweep.append(row)
    small = []
    # Periods 2,3 inherited from EXP-013; all phases/axis orders; q up to full N.
    for dim in [2,3]:
        for d in [2,3]:
            for phase in range(d):
                for reset in [False,True]:
                    for axes in it.permutations(range(dim)):
                        ex = expressions(dim,d,phase,reset,axes)
                        rejected = [q for q in range(1,98) if symbolic(ex,q)['status']=='UNSAT']
                        small.append({'dim':dim,'period':d,'phase':phase,'row_reset':reset,
                                      'axes':axes,'rejected_outer_periods':rejected})
    print(json.dumps({'ciphertext_sha256':hashlib.sha256(C.encode()).hexdigest(),
                      'controls':'PASS', 'symbolic_positive_controls':symbolic_controls,
                      'plaintext_groups':groups(P),
                      'ciphertext_crib_groups':groups({i:C[i] for i in P}),
                      'repeated_digraphs':{x:v for x,v in groups(digraphs).items() if len(v)>1},
                      'pair_audit':pair_audit,
                      'period_constraints':periods,'coordinate_sweep':sweep,
                      'small_period_sweep':small}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
