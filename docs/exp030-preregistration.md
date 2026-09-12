# EXP-030 preregistration — arbitrary lookup and constant tape stepping

Declared before running EXP-030. Starting checkpoint:
`0cb2b38d2b81980d9c7b099c3727423335f9d86e`.

Hypothesis: a fixed city-letter lookup supplies a shift key while a pointer
advances by a constant step on the frozen CET tape:

`key[i] = f(T[(offset + step*i) mod 120])`.

T is the frozen upper-then-lower 120-letter transcription, normalized by the
existing letters-only rule. No changes to transcription or historical claims.
Lower-then-upper is a rotation and contributes no additional circular paths.

Motivation: separate failure of the tape from failure of the two previously
selected key alphabets. A fixed lookup includes all keyword alphabets, numerical
letter substitutions, and even non-injective maps. Constant stepping is a
bounded indexing architecture motivated by clock progression; no particular
step or circular seam is claimed to be historically attested.

Evidence-fixed: tape, ciphertext, 24 crib positions. Fitted: offset 0..119,
step 0..119 (including non-coprime steps and the degenerate zero step), the
12 existing plaintext/ciphertext alphabet and combiner conventions, and any
function f from A-Z to Z26 (26^26 possibilities). Total 172,800 structural
cases, solved analytically rather than enumerating functions. Sequential
steps +1 and -1 are reported separately. Arbitrary plaintext/ciphertext
alphabets, changing f, transposition, feedback, and multiple faces are excluded.

Exact gate/theorem: a function exists iff every pair of crib positions visiting
the same tape letter demands the same key value. A bijective alphabet exists
iff, additionally, different visited letters demand distinct values. A consistent
partial function always extends to A-Z; a partial injection extends to a permutation.
Thus the gate is necessary AND sufficient for crib feasibility within this model.

Before real data: planted controls for all 12 conventions, a nonstandard
permutation and a deliberately non-injective mapping, both sequential directions,
and non-coprime stepping. Check the solver against independent pairwise equality
tests. Use synthetic X filler with only the public cribs inserted; it is not a
candidate K4 plaintext. Controls must pass or stop.

Save every case with its first contradiction witness or partial lookup, plus
parameters, input hashes, controls and summary. No node cap, no language scoring,
no score chasing. Independent pairwise verification must validate all case
verdicts. A surviving fitted mapping is merely feasible, never predictive evidence
or a solution. No verifier submission. No post-result expansion in this experiment.

Choice B: this algebraic family offers immediate, exact information without
unavailable photographs. This is a judgment about cost and falsifiability, not a
quantified probability that this is Sanborn's mechanism. Afterward, reassess;
do not keep expanding the clock model merely to obtain a fit.
