"""Independent graph-connectivity verification of AB's saved UNSAT certificates.

No import of checkpoint_AB or k4lib. Rebuild dependencies using index arithmetic.
Run after checkpoint_AB.py; this verifier does not write files.
"""
import itertools
import json
from pathlib import Path

C = 'OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR'
P = {**dict(enumerate('EASTNORTHEAST',21)), **dict(enumerate('BERLINCLOCK',63))}


def verify(dim,d,phase,reset,axes,q):
    regions = [(0,4),(4,35),(35,66),(66,97)] if reset else [(0,97)]
    expr = {}
    for lo,hi in regions:
        a = lo
        first = True
        while a < hi:
            length = min((phase if first and phase else d),hi-a)
            for j in range(length):
                expr[a+j] = tuple((P.get(a+(dim*j+t)%length,'@'+str(a+(dim*j+t)%length)),
                                    axes[(dim*j+t)//length]) for t in range(dim))
            a += length
            first = False
    graph = {v:set() for tup in expr.values() for v in tup}
    for i,j in itertools.combinations(range(97),2):
        if i%q==j%q and C[i]==C[j]:
            for a,b in zip(expr[i],expr[j]):
                graph[a].add(b); graph[b].add(a)
    comp = {}
    for root in graph:
        if root in comp:
            continue
        todo = [root]
        comp[root] = root
        while todo:
            for v in graph[todo.pop()]:
                if v not in comp:
                    comp[v] = root; todo.append(v)
    for i,j in itertools.combinations(range(97),2):
        if i%q==j%q and C[i]!=C[j] and all(comp[a]==comp[b] for a,b in zip(expr[i],expr[j])):
            return True
    for a,b in itertools.combinations(set(P.values()),2):
        if all(comp[a,t]==comp[b,t] for t in range(dim)):
            return True
    return False


a = json.loads((Path(__file__).resolve().parents[1]/'results/checkpoint_AB.json').read_text(encoding='utf-8-sig'))
count = 0
for r in a['coordinate_sweep']:
    assert verify(r['dim'],r['period'],0,r['row_reset'],tuple(range(r['dim'])),1) == (r['status']=='UNSAT')
    count += 1
for r in a['small_period_sweep']:
    for q in range(1,98):
        assert verify(r['dim'],r['period'],r['phase'],r['row_reset'],r['axes'],q) == (q in r['rejected_outer_periods'])
        count += 1
print('PASS: independently checked',count,'symbolic verdicts')
