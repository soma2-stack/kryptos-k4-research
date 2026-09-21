> **Repository-audit correction — 2026-09-21.** EXP-043's affine-family result is a scoped negative. Its K3 motivation is now reproducible via `audit/verify_exp043_k3_derivation.py`, but K3 plaintext provenance remains separately un-frozen (`verified:false`). Do not state that every possible K3-derived permutation is eliminated; only the registered affine-mod-97 surrogate family is.

# Compact canonical K4 knowledge state

Updated 2026-09-21 through EXP-043 and Checkpoint AM. This file is memory, not a
replacement for historical checkpoint documents. Read it before selecting work.

## Current status

K4 remains UNSOLVED. No complete plaintext, key, or deterministic 97-character method is
admitted. EXP-040 through EXP-043 have now run at their registered scopes; do not revive or
broaden them without a genuinely new, independently motivated constraint.

## Canonical ciphertext and verified cribs

```text
OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR
```

Length is 97. Verified zero-based anchors are `[21,34) = EASTNORTHEAST` (ciphertext
`FLRVQQPRNGKSS`) and `[63,74) = BERLINCLOCK` (ciphertext `NYPVTTMZFPK`). There are 24 known
plaintext letters. Do not slide, extend, or infer additional plaintext.

## Canonical cryptanalytic frontier

The current prospective state is **post-EXP-043**. Checkpoint AE remains an important historical
decidability census, and AF–AL remain useful scope clarifications/audits, but they are no longer
the latest operational frontier because EXP-040 through EXP-043 were subsequently preregistered,
run, and recorded. The binding rule is unchanged: constraint density, shared parameters, and
independently motivated finite domains are required; compatibility is not evidence.

For current work, treat EXP-040–043 as scoped negatives at their registered domains. Do not infer
that all feedback, all two-mask sandwiches, or all K3-derived permutations are eliminated. In
particular, the EXP-043 affine-family negative is stronger than its currently committed
independent verification of the K3-to-affine motivation; see `docs/repo-audit-2026-09-21.md`.

### Documented scoped negatives

- Pure transposition is impossible: crib multiplicity requires at least three E's while the
  ciphertext has two. This does not eliminate substitution-plus-transposition generally.
- EXP-020 / Checkpoint T: declared row-reset, row-structured traversal, and 12 shift/combiner
  conventions across periods 2–40 are negative. Physical row breaks do not choose reset.
- EXP-033: declared single transpositions composed with any fixed A–Z function are zero at the
  registered scope.
- EXP-036: declared periodic shift-family conventions, periods 2–23, with declared
  transpositions are zero at the registered scope; not a theorem about arbitrary 26x26 tables.
- EXP-037: preregistered standard Porta is negative. Quagmire I–III and Gronsfeld reduce to
  covered families; Quagmire IV needs an unsupported second alphabet.
- EXP-038: full-Z26 second-order affine self-evolving keystreams, message-aligned with no
  primer/warm-up, reset, reversed recurrence, plaintext/ciphertext feedback, or transposition, across
  12 committed shift conventions, are exhaustively negative; generic recurrence is not eliminated.
- EXP-039: ordered pairs from `{KRYPTOS, PALIMPSEST, ABSCISSA}` in standard no-padding double
  columnar transposition followed by a fixed monoalphabetic map are zero; double transposition
  generally is not eliminated.
- Standard Fractionated Morse, direct Gromark, Digrafid, and declared direct clock-source
  models were rejected at their documented scopes. Do not broaden those negatives silently.
- Free inner/outer masks, free polygraphic maps, arbitrary position functions, and arbitrary
  26x26 combiners are vacuous or underconstrained under the present crib geometry.
- EXP-040 (2026-09-21): propagating text-autokey is exhaustively negative at its registered
  scope — plaintext or ciphertext fed back, forward or reversed, primer 1–24 letters, 12
  committed conventions, both key-index alphabets, with and without physical-row reset at m<=3;
  2,592 exact decisions, 0 feasible, 3 controls pass, independently verified three ways. All
  keyword primers are subsumed (every primer value per chain was enumerated). This does NOT
  eliminate two-tap/mixed feedback, feedback through a non-identity function, feedback composed
  with a transposition, or primers longer than 24.
- EXP-041 (2026-09-21): additive two-tap propagating PLAINTEXT feedback is exhaustively negative
  — 1 <= a < b <= 19, coefficients in {+-1}^2, gamma zero or free, 3 combiners, STD/KRY on both
  sides, forward and reverse; 32,832 enumerated, 21,883 distinct tests, 0 feasible. All 32,832
  carry a verified left-null-space certificate of infeasibility (full coverage). Outside EXP-038
  because substituting P = C - k yields a key recurrence WITH a ciphertext driving term; outside
  EXP-040 because a < b. Ciphertext two-tap is a DUPLICATE of EXP-008 and was excluded. Does NOT
  eliminate nonlinear or table feedback, >=3 taps, mixed plaintext/ciphertext taps, feedback with
  transposition, irregular schedules, or position-dependent functions.
- EXP-042 (2026-09-21): mixed plaintext/ciphertext two-tap propagating feedback is exhaustively
  negative — a,b in 1..24, alpha/beta in {+-1} with beta != 0, gamma zero or free, 3 combiners,
  STD/KRY both sides, forward and reverse; 110,592 raw, 68,972 distinct, 0 feasible, all 110,592
  carrying verified infeasibility certificates. PROVEN during screening: the ciphertext tap is a
  known driving term, so the recurrence is FIRST ORDER in k with lag a alone and unknowns equal
  the PLAINTEXT-tap lag; the two orientations are byte-identical with lags exchanged (126/126 and
  336/336 independently); beta=0 is exactly EXP-040.
- **The simple feedback corridor is PROVISIONALLY EXHAUSTED** (EXP-040/041/042). Do NOT escalate
  to three taps, nonlinear f, 26x26 feedback tables or arbitrary state machines: those add
  flexibility without evidence and fail the discrimination budget below.
- EXP-043 (2026-09-21): `M2 . pi . M1` with pi derived from K3 is exhaustively negative —
  15,197,184 configurations, 0 feasible, verified by cycle certificates and 4.36e8 forward
  simulations. DERIVED FACTS (no K4 crib score used): K1 = Vigenere KRY/KRY + PALIMPSEST (exact);
  K2 = KRY/KRY + ABSCISSA (first 361 chars, tail diverges at the documented omitted character);
  K3 = PURE transposition (identical letter multisets) with a UNIQUE recovered permutation of 336
  positions, first differences only 191/192, cycle type 168+168. K3's rectangular route principle
  needs r*c=n with 1<r,c<n: 336 admits 18 such rectangles, **97 is PRIME and admits 0**, so the
  exact principle has NO K4 instance. Its faithful prime-length surrogate is the affine-mod-97
  family (9,312), now tested and negative.
- **No period rule exists across K1-K3** — any extrapolation from PALIMPSEST(10)/ABSCISSA(8)
  requires K3 to have a key length, and K3 has none. The (8,10) pair is NOT independently
  warranted; treat it only as an ordinary member of a declared sweep.
- EXP-044 (2026-09-21): the engraved-geometry route corpus (`k4lib.transpositions.
  engraved_routes()` x 2 orientations, deduplicated to 12 distinct permutations) inside TWO
  additive periodic masks, p,q in 1..10, 12 committed conventions -- 14,400 configurations,
  0 feasible, budget 21.94 < 24, four controls pass including a blind-region control.
  Verified by 4,000/4,000 cycle certificates and brute-force forward simulation. The corpus is
  VERIFIED DISJOINT from EXP-043's 9,312 affine permutations. Closes ONLY this corpus at
  p,q <= 10; says nothing about other permutations, p or q > 10, non-additive masks, or >=3 stages.
- Hidden trigraphic stages behind additive masks are refuted only for periods 1, 3, and 9 by
  the repeated crib trigrams; this is not a universal fractionation negative.

## CRIB CYCLE-RANK THEOREM (Checkpoint AP) -- use this instead of guessing d_eff

`audit/frontier_census_AP.py`, `docs/analysis/checkpoint-AP-crib-cycle-rank-theorem.md`.

If every crib equation is affine over Z26 with at most two unknowns and +-1 coefficients,
build the multigraph on the unknowns: a 2-unknown crib is an EDGE with sign -eps_u*eps_v,
a 1-unknown crib ANCHORS its vertex. Then over GF(13)

    d_eff = sum over components K of   |K|      if K is anchored or UNBALANCED
                                       |K| - 1  otherwise
    mu    = 24 - d_eff = the number of independent constraints

A component is UNBALANCED if some cycle has sign product -1; such a cycle pins an absolute
value exactly as an anchor does. Balance is INVISIBLE mod 2, so state it over GF(13) and
report the mod-2 rank separately -- Z26 is not a field. The sign-blind formula |V|-c is
wrong in 4,000/4,000 random cases; the balance correction is load-bearing.

Verified with 0 mismatches against exact Z26 rank on every architecture shape in this
repository plus 4,000 random signed systems.

It SUBSUMES, as corollaries rather than separate facts: the zero at periods 27-29; the
5/3/1 counts at 24-26; the two-mask `24-(p+q-1)` bound AND the AE correction that
disconnection RAISES the count; the crib-span law; AA-Theorem 1; AC-Result 1.

**SCHEDULE PARTITION COROLLARY.** For any deterministic schedule `k_eff[i] = k[s(i)] + g(i)`
with s and g KNOWN, the additive g moves to the right-hand side, so d_eff depends ONLY on the
partition s induces on the 24 crib positions. A progressive key is budget-identical to its
underlying periodic key. Irregularity helps only where it COLLIDES crib positions into one
slot. Do NOT propose "make the schedule irregular" as a route to more discrimination.

Measured: periodic p=13 -> mu 11; progressive p=13 -> mu 11 (identical); Fibonacci mod 13 ->
15; squares/triangular mod 13 -> 17; row-structured 4/31/31/31 -> 21.

## Census verdicts (Checkpoint AP)

- Non-shift combiners such as the affine `a*P+k`: finite and discriminating, but NOTHING in
  the Kryptos record selects a multiplicative combiner. Category C -- do not run on cheapness.
- Multi-stage fractionation: Trifid residual budget is 47.6 against 24 available. Category B,
  underdetermined. SAT there is what the budget predicts, not evidence.
- Deterministic irregular schedules: category D as a DISTINCT direction, by the corollary above.

## Historical AL frontier (superseded prospectively by EXP-040–043)

Six practical classes were reviewed. The conditional top three are: (1) declared periodic
masks at p=24–26 (5/3/1 crib constraints), (2) two short masks around a fixed permutation
(about 7 constraints at the K1/K2 pair, more only when parameters are frozen), and (3) a
specifically declared low-state recurrence outside EXP-038. Structured fractionation and
deterministic non-position-preserving alignment remain open only as templates. Periods 27–29
receive zero current crib constraints. None has a puzzle-selected finite parameter set, so no
EXP-040 is justified.

**DISCRIMINATION BUDGET (the organising theorem; apply before writing any code).**
With `d_eff` = rank over Z26 of the map (parameters -> the 24 crib plaintext values), a family of
N classes has expected accidental survivors `N * 26^(d_eff - 24)` and can discriminate only if

    log26(N) + d_eff < 24

`d_eff` counts only parameters a crib actually reaches — that IS the crib-span law. Using the
nominal parameter count instead is wrong and mislabels decisive families as undecidable. The
inequality reproduces every measured result: EXP-040 21.4, EXP-041 23.1, EXP-042 23.6, periodic
p=24 19.8, p=27 24.8 (cannot discriminate), AC Trifid 47.6, shared 26x26 feedback table 677. See
`results/2026-09-21-frontier-after-feedback-corridor.md`.

Every surviving class is now in one of two buckets: (i) log26(N)+d_eff >= 24, undiscriminable by
24 letters no matter the compute; or (ii) discriminable but with no evidence selecting its
parameters (M2.pi.M1, periods 24-26). The productive third bucket — decisive AND motivated — is
EMPTY. Further progress requires new information, not new search. One extra authenticated letter
is worth a factor of 26.

**Crib-span law (EXP-040, reconfirmed independently by EXP-041 and EXP-042).** In a propagating feedback model a ciphertext change
downstream of every crib position in its own chain is absorbed by the primer and is undetectable.
So a feedback family's power is bounded by crib **span**, not crib count: the tail beyond each
chain's last crib carries zero constraint. This is the feedback analogue of the period 27–29 blind
spot and should be quoted whenever a feedback model is proposed. Use it as a cheap pre-test:
compute the dependency components, count how many cribs share one, and reject the family before
coding if the answer is at most one. Confirmed in two independent families (EXP-040 one-tap,
EXP-041 two-tap).

Useful authenticated missing-plaintext targets are indices 1, 3, 91, 93, 95, and 96. One
legitimate letter there would constrain the blind periods and materially increase information.

## Physical artifact state (AI–AK)

The ideal generated KRY tableau has 866 cells; the institutional CIA textual transcription has
867 characters. The only modeled textual difference is an extra terminal `L` on the N row; its
physical copper presence remains UNKNOWN. Checkpoint AI found no artifact-selected cipher rule.
Checkpoint AJ found that textual `4/31/31/31` is not a complete physical measurement, no fixed
column lattice or spacing key is established, and rows 26–28 endpoints remain unmeasured.
Checkpoint AK prospectively verifies from an artist-supplied WIRED image that physical row 25
ends `?OBKR`; `OBKR` is not a separate engraved row. Full physical row 26–28 geometry remains
unestablished. Do not infer routes, resets, or Hill from these facts.

## Public documentary state

ScheidtNova.doc is located only through public index metadata; its payload is not recovered and
its server-side status is unknown. The unedited 2005 Kim Zetter/WIRED Scheidt material is not
located. GBH Open Vault `V_3AC501960CC4454A8FD950703CBED5A9` resolves to AAPB
`cpb-aacip-15-1615gc34`, a 56:46 NOVA ScienceNow broadcast master, not a complete Scheidt
interview. The exact UGA/Peabody object remains a search-result lead only. PBS narration about
concealment before enciphering is editorial, not a Scheidt stage-order statement. Pending
outreach: GBH, Kim Zetter, TecSec/Ed Scheidt, and Elonka Dunin. Do not duplicate requests.

## Disputed 2015 workshop "periodic" exchange (Checkpoint AM)

**K4 periodicity is NOT authenticated evidence and must not enter the constraint set.**

A machine transcript places "Would you consider it periodic?" / "Yeah." inside the
47:35-48:16 gap of the human Bean/Cipherbrain transcript of YouTube `25YFYKKKkDo`.
It carries no authenticated speaker labels. Checkpoint AM attempted primary-audio
authentication and returned `UNRESOLVED` for an environmental reason: `youtube.com`,
`scienceblogs.de`, `web.archive.org` and `huggingface.co` are all denied by the
network egress policy (proxy logs a 403 CONNECT), so no audio was obtained and none
was assessed. A second, structural blocker also stands: speaker attribution by
timbre/cadence/mic position needs a human ear, which no ASR substitute supplies.

All four points remain open: wording, referent of "it", speaker identity, polarity.
Note the live confusion risk - the same conversation uses "period" in the
*punctuation* sense at ~46:23-46:40.

**Do not re-run this audio pass on this environment.** It unblocks only on a network
that permits the recording *plus a human listener*, or a speaker-labelled human
transcript covering 47:35-48:16, or a participant's direct statement.

Authenticated 2015 workshop content remains only what Checkpoint X established:
K4 is **more than one stage**, and masking is part of Layer A. No period, period
value, reset rule or schedule is licensed by this recording.

## Scheidt “Stego” lead (Checkpoint AN, corrected prospectively by AO)

**PROVENANCE-LIMITED LEAD; grade C.** A surviving John B. Wilson page attributes to Ed Scheidt
the statement that K4 had “a piece relating to Stego,” while reportedly adding that he did not
state “how or in what context.”

Checkpoint AO found that the original Scheidt communication, metadata, underlying talk record,
and any independent contemporary copy have **not** been recovered. Therefore this phrase does
**not** meet the project's A / strong-B threshold and must **not** be treated as an authenticated
K4 structural constraint.

Canonical treatment: preserve it only as a provenance target. Do NOT infer any carrier, null
cipher, acrostic, grille, binary scheme, insertion/deletion rule, physical-layout mechanism,
stage order, period, key length, alphabet, recurrence, reset or alignment. It does not justify
EXP-044.

See `docs/external/checkpoint-AO-scheidt-stego-provenance-correction.md`.

## Contamination boundary

Reject alleged full K4 plaintexts, leaked or claimed solutions, auction-secret material, private
K5 material, stolen/private documents, solution dumps, and sites primarily intended to reveal
claimed solutions. If encountered, stop reading, record only safe URL/domain and category in
`rejected-contamination.md`, and never quote plaintext.

## Operating rule

Every worker performs exactly one bounded, repository-novel investigation, records whether it is
NEW / CONFIRMATION / CONTRADICTION / ALREADY KNOWN / LOW VALUE / IDEA CANDIDATE / BLOCKED, and
does not promote a cryptanalytic claim without reviewer support. Historical files are immutable;
prospective corrections go in this memory and the ledgers.

