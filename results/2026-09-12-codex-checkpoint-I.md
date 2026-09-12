# Checkpoint I — audited handoff; arbitrary tape lookup eliminated

Base: `0cb2b38d2b81980d9c7b099c3727423335f9d86e`.
Branch: `codex/k4-continuation`. Preregistration: `56ab721`.
K4 remains unsolved. No plaintext candidate or verifier submission.

## Audit result

The final frozen transcription agrees with the committed data: upper 62, lower
58, total 120. The withdrawn 97-letter coincidence stays withdrawn. Original
EXP-024 and EXP-029 source files and photographic data are unchanged.

EXP-005's four controls pass; all 8,112 primitive arithmetic combinations agree
with independent formulas. EXP-024's synthetic planted construction was checked
without executing its search. EXP-028 passes all 21 invariants; its tautological
latitude check is now accurately labelled as an order guard.

An independent direct-encryption implementation exactly reproduced EXP-029's
histogram: {0:4668, 1:4186, 2:1870, 3:646, 4:134, 5:14, 7:2}.
This bounded replication was justified by an actual scope/implementation bug:
EXP-029 wraps modulo 120 although its description promises windows entirely
inside a known arc. Its two tapes are rotations, leaving 5,760 distinct
(full numeric stream, convention) pairs among 11,520 labels. The two 7/24
maxima are duplicate descriptions of one stream. **Retract the reported
Poisson significance interpretation**, not the zero-hit result.

The full nonwrapping subset contains 2 tapes x 24 starts x 2 directions x
2 key alphabets x 12 conventions = **2,304 cases, zero exact hits**.
Its histogram is {0:943, 1:833, 2:369, 3:124, 4:30, 5:4, 7:1}.
96 independent endpoint controls cover both tapes, both directions, legal
endpoints and all conventions. Circular seams remain modelling assumptions,
not observed adjacency to the same face.

Two confirmed graph bugs were repaired: competing complete orders could silently
replace one another, and conflicts did not block completeness. The graph now
preserves the first complete reading and rejects conflicting or unmarked records
as complete; reversed partial observations also trigger conflicts. All current
observations remain conflict-free and the frozen target-era face remains complete.
Synthetic adversarial controls demonstrate the new failures are caught. Incomplete
historical clock construction still raises ReconstructionIncomplete.

## New experiment: EXP-030

Choice B was made before results: eliminate a broader fixed-lookup/indexing
architecture using the available evidence rather than await photographs.
The motivation and exact scope were committed before execution.

Model: `k[i] = f(T[(offset + step*i) mod 120])`.
T is the unchanged frozen CET upper-then-lower tape. Offset and step each range
0..119; all 12 existing shift conventions are tested. f is **any function**
A-Z -> Z26, including every permutation/keyword alphabet and non-injective maps.
Thus **172,800 structural cases**, each representing all 26^26 functions, are
solved exactly. No enumeration of functions is necessary: if the same visited
letter requires two different key values, no fixed function can exist. Conversely,
a consistent partial mapping extends to a full function. This is an exact
feasibility criterion, not a heuristic or language score.

**Result: 172,800 contradictions; zero feasible mappings.** The sequential
step +1/-1 subset alone has 2,880 cases and zero feasible mappings.
**120 planted controls passed**, covering all conventions, a nonstandard
permutation, a non-injective map, both directions, non-coprime and zero steps.
Each real verdict was checked by an independent pairwise formulation.
A separate verifier importing neither k4lib nor the experiment independently
validated **all 172,800 saved contradiction witnesses**, complete case coverage,
and input/output hashes. Compressed full case certificates occupy about 423 KiB.

Grade: **EXHAUSTIVELY ELIMINATED WITHIN THE SPECIFIED MODEL**, conditional on the
frozen transcription and the public crib data. This expands EXP-029's negative
from two key alphabets to every fixed letter-to-number function and every constant
step on the 120-letter tape. No multiple-testing significance claim is needed for
this exact contradiction result. Case counts are not counts of independent tests.

## Limits and next move

This does not eliminate arbitrary plaintext/ciphertext alphabets, a changing lookup,
nonconstant traversal, mixed substitution/transposition, fractionation, multiple
faces, a different evidence-supported tape, or unrelated mechanisms. Confidence
falls specifically in the single-face fixed-lookup family. There is no calibrated
probability update for the whole clock hypothesis.

Several inherited architecture-level claims were overbroad; see docs/codex-audit.md.
They do not establish that external running keys are the only surviving mechanism.
Nor does this audit independently verify every older large search.

The highest-value *evidence* step now is obtaining actual target-era photograph
bytes and archive metadata, both to independently verify the inherited CET reading
and to unlock new multi-face paths. More free parameters on this same tape would
currently be less informative. A search for the three exact archive targets did
not yield usable image bytes or an accession-specific record; no image has been
reconstructed or substituted. That evidence subtask is paused, with the precise
request in docs/codex-image-request.md. Other cipher architectures remain open,
not exhaustively ranked by this checkpoint.

## Reproduce only this checkpoint

```sh
python audit/verify_handoff.py
python experiments/exp028_graph_invariants.py
python experiments/exp030_tape_lookup.py
python audit/verify_exp030.py
```

Do not use run_all.sh just to reproduce this checkpoint: it runs older large
searches. Full parameters, frozen input, hashes and controls are in
results/exp030/summary.json; every case is in results/exp030/cases.jsonl.gz.
