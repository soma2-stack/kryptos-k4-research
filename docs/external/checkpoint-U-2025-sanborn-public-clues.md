# Checkpoint U — audit of the 2025 Sanborn public clues

**Date:** 2026-09-13. **Branch:** `claude/k4-post-j`. **Starting HEAD:** `a5cb0deb1014a86bcbde1e4dae710a87909aa50c`.

---

## 0. Provenance ceiling — read this before using anything below

**No primary source in this audit could be fetched.** Every news and archival domain
(`elonka.com`, `scientificamerican.com`, `washingtonpost.com`, `wired.com`, `npr.org`,
`smithsonianmag.com`, `apnews.com`, `en.wikipedia.org`, ACM) is blocked by this
environment's network egress policy. Direct `curl` returns `403` at the proxy tunnel.

Everything below therefore rests on **search-engine result summaries** of reputable
reporting, cross-checked by issuing independent queries and keeping only statements that
recurred across separate searches. That is a real but **limited** grade:

- I can report *that* a statement is widely attributed to Sanborn.
- I **cannot** certify verbatim wording, and no quotation below should be treated as
  exact unless a later session verifies it against the primary document.

Accordingly the highest grade awarded in this audit is **C+/B−**, below the B+ that the
1991 ABC transcript and the 1999 *Washington Post* article hold. **This audit must be
re-run with primary-source access before any of it becomes load-bearing.**

One concrete reliability signal: at least one outlet described K4 as **"79 encrypted
letters."** K4 is **97**. Downstream numeric detail in this reporting is not trustworthy.

### Contamination boundary respected

Searches repeatedly surfaced pages purporting to carry the 2025-discovered K4 plaintext,
reconstructions and solution write-ups (`solvekryptos.com/solution`, a GitHub repository,
Medium posts, and others). **None was opened.** No auction-secret material, no K5 private
material, no Folder 8 page, and no alleged plaintext was accessed. Later searches
explicitly blocked those domains.

---

## 1. The statements, direct wording separated from paraphrase

| # | Statement | Direct or paraphrase | Grade |
| --- | --- | --- | --- |
| U1 | Two events figure in the solution: Sanborn's second trip to Egypt in late 1986, and the fall of the Berlin Wall | **Paraphrase** of an open letter, consistent across sources | C+ |
| U2 | The "Berlin Clock" of the K4 clue is the **World Clock (Weltzeituhr)** at Alexanderplatz — the gathering place for the crowds that brought down the Wall — not the Mengenlehreuhr | **Paraphrase**, consistent across sources | C+/B− |
| U3 | The codes of Kryptos, from the Morse material at the beginning through K5, are about **delivering a message** | **Paraphrase**, close to quoted form | C+ |
| U4 | K5 is thematically connected to K2's *"it's buried out there somewhere"* | **Paraphrase** | C+ |
| U5 | "…what's the point? **Power resides with a secret, not without it.**" (August 2025 open letter, on his hope the buyer keeps K4 secret) | **Direct quotation** as reported | C+ |
| U6 | K5: announced 12 Nov 2025 at the International Spy Museum; **97 characters**; a **"similar but not identical"** system to K4; sited in a **public space**; released when K4 is cryptographically solved | **Mixed**; the quoted phrase is short and recurred verbatim | C+ |
| U7 | K4 and K5 **share some coded words in the same positions**, reportedly including `BERLINCLOCK` | **Paraphrase** | **C, single-thread — treat as unverified** |
| U8 | "**K4 has not been solved. K4 has been discovered and it points in the direction of K5.**" | **Direct quotation** as reported | C+ |

### U9 — the WIRED August 2025 item in the brief could not be sourced

The brief attributes to WIRED, August 2025, that K4's plaintext is *itself an instruction
for how to solve it*, *may involve other parts of the installation*, and *does not require
physical access to CIA grounds*.

**I could not source this, and the closest well-attested statement says the reverse.** The
2005 Kim Zetter WIRED interview — the repository's own Request 2 target — is consistently
reported as saying solvers **must** be on CIA grounds:

> "In part of the code that's been deciphered, I refer to an act that took place when I was
> at the agency and a location that's on the grounds of the agency. So … you have to
> decipher the piece and then go to the agency and find that place."

Three readings, none established:

1. The brief has **conflated** the 2005 WIRED/Zetter interview with 2025 reporting. The
   "other parts of the installation" language matches the 2005 interview closely.
2. A genuine 2025 **reversal** — plausible, since K5 is to stand in a *public space*, which
   would be pointless if solving required Langley access.
3. A 2025 WIRED piece exists that this environment's search simply did not surface.

**Recorded as UNVERIFIED. Not used anywhere below.** Only the first two clauses — "the
plaintext is an instruction" and "may involve other parts of the installation" — are
independently echoed, and only weakly, by U8's "it points in the direction of K5."

---

## 2. The chronology problem — preserved, not resolved

The contradiction, stated exactly:

- Sanborn is reported as saying both events "had a significant role to play **while he was
  writing the plain text of Kryptos in 1988**."
- His second Egypt trip was **late 1986** — consistent.
- The Berlin Wall fell on **9 November 1989** — *after* the stated writing year.

Evidence bearing on it, without resolving it:

- Sanborn is separately quoted saying he was "designing the project when the Berlin Wall
  fell," and that "there's no doubt I was influenced by all that was going on
  simultaneously."
- The sculpture is commonly dated to 1988 by **cost and commission**, and was dedicated
  **3 November 1990**. Fabrication and writing plainly spanned 1988–1990.

**Most probable reading: loose dating.** "1988" most likely names the start of the writing
period, or is the year Sanborn associates with the project generally, rather than a claim
that the plaintext was finalised before November 1989.

**But this is not established**, and two other readings survive: a reporting/transcription
error introducing "1988", or an unresolved inconsistency in Sanborn's own recollection
thirty-seven years later.

**Prohibited:** treating "1988", "1989", "1986", or any arithmetic on them as a
cryptographic parameter — a key length, an offset, a period, a seed or an index. There is
no evidence whatsoever for that, and the date is not even reliably reported.

---

## 3. The two-layer model

**Layer A — the cryptographic transformation.** The map from 97 plaintext letters to the 97
K4 ciphertext letters. This is the only layer the repository's experiments can test, and
the only layer whose failure keeps K4 unsolved in the cryptographic sense.

**Layer B — the post-decryption riddle.** Whatever the recovered plaintext then instructs
the solver to do: a place, an object, a further puzzle, or a route onward to K5.

### The layers are documented as distinct, by Sanborn, in his own words

The 2005 Zetter quotation is the clearest statement available, and it is explicitly
sequential:

> "…you have to **decipher the piece** *and then* **go to the agency and find that place**."

Decipher = Layer A. Go and find = Layer B. U8 makes the same division from the other
direction: K4 "has been **discovered**" — the plaintext is known to at least three people —
"and it **points in the direction of K5**." A text can only *point* if pointing is a
property of its content, not of its encipherment. **Layer A remains unsolved precisely
while Layer B is already in someone's hands.** That is the sharpest possible demonstration
that the two layers are separable.

### Which layer does each clue constrain?

| Clue | Layer A | Layer B | Reasoning |
| --- | --- | --- | --- |
| U1 Egypt 1986 / Berlin Wall | — | **B** | Attached to "writing the **plain text**" — thematic content, not method |
| U2 `BERLINCLOCK` = Weltzeituhr | — | **B** | `BERLINCLOCK` is a **plaintext** word. Saying what a decrypted word *denotes* is semantics, not a key source |
| U3 "delivering a message" | — | **B** | A statement of artistic theme spanning Morse → K5 |
| U4 K5 ↔ K2 "buried out there somewhere" | — | **B** | Thematic linkage between plaintexts |
| U5 "Power resides with a secret" | — | — | **Neither.** A statement about the auction and about secrecy as a value |
| U6 K5 is 97 chars, "similar but not identical" system | **A (weak, prospective)** | — | The only 2025 item touching method at all |
| U7 shared coded words in shared positions | **A (prospective)** | — | Would be a crib relation *once K5 exists* |
| U8 "points in the direction of K5" | — | **B** | Pointing is a content property |
| 2005 "go to the agency and find that place" | — | **B** | Explicitly post-decryption |

**Eight of the ten items are Layer B or neither. Exactly two touch Layer A, and both are
about K5, which does not yet exist publicly.**

---

## 4. Have we been conflating Layer A with Layer B? — Yes

This is the substantive finding of Checkpoint U.

The repository contains a family of experiments that took an **artistic or physical
referent** and used it as a **keystream, mask or route source** for Layer A:

| Experiment | Referent used as a Layer A key source |
| --- | --- |
| EXP-002 | Mengenlehreuhr lamp states as a keystream (161,740,800 cases) |
| EXP-018 | Compass bearings as transposition routes |
| EXP-023 | Morse material as a keystream |
| EXP-024 / EXP-029 / EXP-031 | Weltzeituhr faces as a letter tape and running key |
| EXP-035 | The sculpture's own panel text as a running key |

Every one of these is negative. Checkpoint U supplies the **explanation**, which the
project did not previously have: these referents are, on the best available reading of
Sanborn's own statements, **Layer B objects**. `BERLINCLOCK` is a *plaintext word* whose
2025 clarification tells the solver **where to go after decrypting**, not what to encrypt
with. The clue's natural home is the riddle, not the cipher.

**Consequences, stated carefully:**

1. **The negative results stand unchanged.** Nothing here revives or reverses them. They
   were correct.
2. **Their motivation is demoted** — from DOCUMENTARY-MOTIVATED to **SPECULATIVE**. The
   documentary record was never saying "use the clock as a key"; it was saying "the
   plaintext mentions a clock."
3. **Do not revive this class.** Any future proposal that converts an artistic referent
   (Weltzeituhr, Mengenlehreuhr, Morse, compass bearings, Egypt, the Wall) into a Layer A
   keystream now carries an **evidential burden it cannot currently meet**, and should be
   rejected at gate condition 1 rather than tested.
4. **This is a genuine reallocation of research effort**, and it is the reason Checkpoint U
   was worth running even though it produces no experiment.

### Does this change the "masking" and "riddle within a riddle" readings?

**Yes, and in a deflating direction.** "Riddle within a riddle" is most often reported in
connection with K1–K3, and under the two-layer model the natural reading of the *nesting*
is **Layer B nesting** — plaintext → riddle → K5 — not nested **cipher** layers.

This **weakens a long-standing motivation for multi-stage cipher composition** in this
project. It does not refute composition: Scheidt's own 1991/1999 statements about an
adapted, historically grounded method are Layer A evidence and are untouched. But
"masking" and "riddle within a riddle" should no longer be cited as documentary support for
stacking cipher stages. Checkpoint S's four-process interpretation is unaffected — that
concerns K1→K4, not K4's interior.

---

## 5. The K5 statements — the only Layer A content, and it is prospective

U6 and U7 are the sole 2025 items that bear on method. If verified they say:

- K5 is **97 characters**, matching K4 exactly.
- K5 uses a system **"similar but not identical"** to K4's.
- K4 and K5 **share coded words at shared positions**, reportedly including `BERLINCLOCK`.

Were K5 published, U7 would hand the project a **second ciphertext with a known plaintext
word at a known position under a related system** — structurally, a new crib and a
cross-text relation of exactly the kind Checkpoint T identified as the binding shortage.

It is unusable now, for three independent reasons:

1. **K5 is not published.** Its release is conditioned on K4 being cryptographically
   solved — the very thing that is blocked. This is a **closed loop**, not a lead.
2. **U7 is the weakest-sourced item in this audit** (single thread, paraphrase).
3. **"Similar but not identical" names nothing.** It presupposes K4's system without
   describing it, and supplies no transform, schedule, key source or composition order.

It therefore **fails EXP-040 gate conditions 2 and 3**, exactly as every documentary source
before it has.

---

## 6. Answers to the five questions

**Q1 — Does any 2025 clue provide a new position-specific plaintext constraint satisfying
Request 7?**
**No.** U2 changes what `BERLINCLOCK` *denotes*; it changes no position. Positions
`[63,74)` were already verified at Checkpoint P and are unmoved. U1, U3, U4 and U8 are
thematic and yield no letter at any position — and inferring plaintext words from thematic
clues is prohibited by the brief and by project protocol. U7 would be position-specific,
but only for **K5**, and only once K5 exists. **Request 7 remains open and remains the
project's highest-value target.**

**Q2 — Does any clue identify or materially bound the encryption method?**
**No, not usably.** U6's "similar but not identical" is the only method-adjacent statement
and it is about K5, is self-referential to an unknown system, and names no parameter.
Everything else is Layer B.

**Q3 — Does "the plaintext is an instruction" change the reading of earlier masking /
"riddle within a riddle" comments?**
**Yes** — see §4. It relocates the nesting from cipher stages to riddle stages and removes
"riddle within a riddle" from the evidence base for multi-stage composition. Note the
premise itself (U9) is **unverified**; the conclusion survives anyway because it rests on
the far better-attested U8 and the 2005 Zetter quotation, not on U9.

**Q4 — Does it demote prior experiments treating artistic/physical referents as direct
keystream sources?**
**Yes — their motivation, not their results.** EXP-002, EXP-018, EXP-023, EXP-024, EXP-029,
EXP-031 and EXP-035 remain valid negatives. Their documentary motivation drops to
SPECULATIVE, and the class should not be reopened.

**Q5 — Is any new bounded experiment justified?**
**No.**

---

## 7. Gate outcome

| Gate condition | Status |
| --- | --- |
| 1 documentary/physical motivation | Layer B clues are well attested but **motivate no Layer A model**; U6/U7 are C-grade and prospective |
| 2 exact frozen mathematical definition | **FAILS** — no transform, schedule, key source or composition named |
| 3 bounded parameter space | **FAILS** — nothing to bound |
| 4 power from the 24 crib letters | no new constraint offered |
| 5 materially outside EXP-001…039 | the referent families are already tested |
| 6–8 | not reached |

**`NO EXP-040 JUSTIFIED`.**

---

## 8. What would change this

1. **Primary-source access** to the August 2025 and November 2025 open letters, the
   *Washington Post* of 1 Nov 2025, and the claimed WIRED August 2025 piece — to lift this
   audit from C+ to B+ and to settle U7 and U9. This is now a **prerequisite** for treating
   any 2025 clue as load-bearing.
2. **Publication of K5.** If U6/U7 hold, K5 supplies a related 97-character ciphertext with
   shared plaintext at shared positions — the strongest constraint the project could
   receive. It is gated on K4 being solved.
3. **Request 7** — additional verified K4 plaintext — unchanged as the highest-value input,
   and untouched by anything in 2025.
4. **Request 2** — the unedited 2005 Zetter/Scheidt material — **rises in value.** This
   audit shows the 2005 interview is the clearest articulation of the Layer A / Layer B
   split on record, and the repository still holds only the edited published version.

K4 remains unsolved.
