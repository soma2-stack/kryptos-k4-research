# Codex handoff audit — preliminary findings

Base: `0cb2b38d2b81980d9c7b099c3727423335f9d86e`; continuation only on
`codex/k4-continuation`. Main and Claude's branch are preserved.

Read README, contribution and contamination rules, research state, evidence
grades, negative results, next steps, checkpoint H final report, reconstruction
code and data, experiment declarations and library APIs; inspected the core
arithmetic and EXP-024/028/029 implementations in detail. This is a focused
handoff audit, not independent replication of all older large searches.

Confirmed: frozen upper 62 + lower 58 = 120, including the nine lower names in
the supplied order. EXP-028 baseline passes 21/21. EXP-005 recovers 4/4 planted
methods. The original 97-letter coincidence remains withdrawn.

Findings to resolve:

1. EXP-029 uses modulo-120 windows, contrary to its promise to stay inside a
   known arc. The two usable tapes are circular rotations, so its 11,520 labels
   duplicate 5,760 parameterized streams. Its two reported 7/24 maxima are the
   same alignment under a rotation, not two distinct observations. The Poisson
   significance calculation is not calibrated for this duplicated, dependent
   family. Retract the numerical significance interpretation; do not pursue it.
   The zero-hit negative still covers its nonwrapping subset.
2. EXP-029's control at offset 41 wraps the full 97-letter message (41+96>119).
   Verify bounded windows and endpoint controls separately. EXP-024 stays frozen.
3. No EXP-028 or EXP-029 raw log was committed. The written EXP-029 histogram
   therefore needs independent reproduction, justified by finding 1.
4. DrumGraph silently replaces a complete order with a different complete order;
   face_complete ignores conflicts. Synthetic reproductions confirm both bugs.
   Preserve the first complete reading, record conflicts, fail completeness closed.
5. EXP-028's purported latitude test compares a hardcoded list to itself. It
   verifies no geographic fact. Relabel it without weakening the frozen tape guard.
6. Photograph bytes/hashes and exact accession for UPLOAD-6 are absent. The freeze
   timing is a declaration within a single commit, not independently timestamped
   before the result. Preserve it as reported; do not claim independently verified
   chronology, visual transcription, or exact dating. Banner content alone does
   not logically prove an exact day. Actual image plus archive metadata is needed.
7. Older summaries retain withdrawn universal claims: low IoC does not prove that
   no English plaintext exists; parameter entropy alone does not prove
   unfalsifiability; equal K4/K5 lengths do not prove a length-preserving outer
   layer; concatenation verifies a proposed line split internally, not physically;
   simulations do not establish that a unique external-key architecture survives.
   These are not premises for the continuation. Historical records stay intact,
   with this audit taking precedence over their overbroad interpretations.

No external plaintext source accessed; no new plaintext assumptions; no verifier.
Pending: independent scoped replication, fixes, then preregistered EXP-030.
