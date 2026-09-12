# Result record — 2026-09-12 (session 5) — Checkpoint E

Branch `claude/dreamy-archimedes-79k6u0`. Ciphertext SHA-256
`eea813570c7f1fd3b34674e47b5c3da8948026f5cefee612a0b38ffaa515ceab`.
Regenerate with `./run_all.sh`. Python 3.11, standard library only.

**Blind experiment intact. No new contamination incidents.** `solvekryptos.com` was
excluded on every query; no claimed-solution site was used as a historical source;
no purported K4 plaintext was sought or seen. Only `EASTNORTHEAST` and
`BERLINCLOCK` were used as constraints.

**Outcome: primarily B**, with parts of D and E. The 1988–89 Weltzeituhr could not
be reconstructed; the hypothesis is neither confirmed nor rescued; and a second
external-source candidate named by Sanborn himself was tested and failed.

---

## 1 — Historical reconstruction: what was recovered

Full trail in `docs/checkpoint-E-research-log.md`; structured object in
`data/weltzeituhr.json`.

**Corrected a repository error.** The 24-sided city-name cylinder is **static**; a
**rotating hour ring** carries the hours through the zones, driven by a converted
Trabant gearbox. Earlier notes here described the drum itself as rotating.

**The band structure the brief asked for, recovered.** The cylinder is in **three
parts**: city names on the **upper** aluminium disk, the rotating hour ring in the
**middle**, city names on the **lower** disk.

**Other recoveries:** letters are **stamped**, implying punches or templates existed
(survival unknown); the rotunda carries an entry for the **international date line**;
Hans-Joachim Kunsch executed the 1969 construction on site *and* led the Oct–Dec 1997
restoration (350,000 DM) — one person spanning both states of the object.

**1997 changes, partially documented:** renames Leningrad → Sankt Petersburg,
Alma Ata → Almaty, Bratislava → Pressburg; about twenty additions of cities the GDR
had omitted politically, of which only **Tel Aviv, Cape Town, Seoul, Jerusalem** are
named; some zone reassignments, of which only **Kyiv** is named.

**Irreconcilable conflict, recorded unresolved:** total places reported as **80**
(1969), **146**, and **148**.

**UNKNOWN and not filled with modern data:** the ordered per-sector name list for
1988–89; upper-versus-lower assignment; Berlin's and Moscow's sectors; the date
line's position; the cylinder's orientation relative to north; sixteen of the twenty
1997 additions; any removals; the full zone-reassignment list.

---

## 2 — Why the reconstruction failed, stated precisely

The route is sound: modern per-sector list → subtract the twenty 1997 additions →
reverse the renames → revert the zone moves. Four additions and three renames are in
hand; the rest are not.

**The immediate blocker is this environment, not the historical record.** `WebFetch`
is blocked by the network egress proxy for *every* external domain attempted. Only
`WebSearch` works, returning summaries that decline to enumerate long lists. The
modern per-sector list **is published** — `weltzeituhr-berlin.de` has a places-by-time-zone
page — and a human with an ordinary browser could obtain it in minutes.

That distinction matters and is not a technicality: it is the difference between
"the data is lost" and "this agent cannot reach it".

---

## 3 — EXP-024: the Weltzeituhr test, preregistered and validated but not run

Rather than guess the missing names, the test was built and left loaded.

- **22 reading procedures preregistered** while the name list is unavailable — the
  cleanest possible preregistration, since they cannot be tuned to data that does
  not exist here. Each is motivated by the object: clockwise and anticlockwise
  (a person walks around a cylinder); upper-then-lower, lower-then-upper and
  alternating (names sit in two bands); whole-upper-band-then-lower; starting at the
  Berlin sector; and UTC order (the object is also indexed by time zone).
- **End-to-end validation on a structurally faithful synthetic clock** with
  deliberately fake syllables, so it can never be mistaken for reconstructed data. A
  keystream planted at offset 137 of one reading was recovered exactly by the same
  pipeline that would run on the real object. **CONTROL PASSED.**
- **Scale known in advance:** ~480,000 alignments for a clock of this size.
- **Methodological note for whoever runs it:** the planted key was recovered under
  *three* procedure labels, not one. Circular readings of the same clock share
  substrings, so those alignments are **not independent** and the naive binomial
  correction will be conservative in the wrong direction.

**Grade: UNTESTABLE WITH CURRENT PUBLIC DATA — in this environment.** Supplying the
six blocking items in `data/weltzeituhr.json` makes it executable immediately.

---

## 4 — EXP-023: the Morse material as a keystream source · HEURISTIC NEGATIVE

A different external source, and one **Sanborn named himself**: in November 2025 he
said the codes of Kryptos, *from the Morse material onward*, concern "delivering a
message". The K0 Morse plates are physically part of the installation, short, fixed
and public — a low-entropy external source, exactly what EXP-019's unicity bound
requires. One plate reads `WHAT IS YOUR POSITION` (Q-code QTH), which is
thematically what a position-indexed keystream *is*.

The inherited handoff used K0 Morse only as a binary **selector** — a lead EXP-009
explained away as a 1-in-1,024 selection effect. Using it as the key **tape** had
never been tested.

**Scope:** seven fragments plus two concatenations, every offset, both directions,
both key alphabets, 12 conventions — **13,680 alignments**. Planted control recovered.

**Result: 0 exact hits, best 5/24.** Observed 11 alignments at ≥5/24 against **26.5
expected** — below chance, so there is no excess at the top of the distribution at all.

**Grade: HEURISTIC NEGATIVE, not elimination.** The transcriptions are community-sourced;
one plate's text is reported to continue under a rock; the ending of
`DIGETALINTERPRETATIT` is disputed; and the physical order of the slabs is unknown, so
the concatenations are a listing convention rather than evidence. It also leaves
untouched any use of the Morse material other than as a letter tape — its dot/dash
structure, for instance.

---

## 5 — EXP-022 extended: place-name statistics · HEURISTIC NEGATIVE

Checkpoint D tested whether the forced key letters look like English prose. But the
Weltzeituhr tape would be **proper nouns**, whose letter statistics differ. A second
profile was built from a generic list of major world cities — general knowledge, not
reconstructed clock data — so it tests the city-tape hypothesis without the clock.

**Result: best p = 0.0158, Bonferroni over 24 tests = 0.380.** Three tests below
p < 0.05 against 1.2 expected: a mild excess, nothing surviving correction.

Consistent with Checkpoint D's English-prose result (best p = 0.018, corrected 0.428).
**The Checkpoint D heuristic negative is preserved, not rescued.**

---

## 6 — The cribs as instructions on the clock: coherent, and blocked by the same gaps

`BERLINCLOCK` → go to the clock; `EASTNORTHEAST` → a bearing from the compass rose
beneath it. This is physically natural and hand-executable — stand on the rose, face
ENE, read the sector in front of you — and it gives both cribs a job.

It is blocked by **two** UNKNOWNs, not one: the per-sector contents *and* the
cylinder's orientation relative to north. Without orientation a bearing cannot name
a sector at all.

A caution recorded against over-reading any future orientation datum: with 24 faces
every 15°, **any** bearing lies within 7.5° of some face centre. Proximity will carry
no information; only an exact, independently documented alignment would.

**Grade: SUPPORTED INTERPRETATION** of what the cribs might instruct; **UNTESTABLE
WITH CURRENT PUBLIC DATA** as a mechanism.

---

## 7 — Status of the Weltzeituhr hypothesis, not forced to survive

It was **neither confirmed nor rescued**. Standing:

- The architectural case is unchanged and still good: a long, low-entropy,
  externally sourced, position-indexed keystream is what survives EXP-019 and
  EXP-021, and the clock is the object a confirmed crib names.
- Two independent statistical probes that *would* have supported a text-derived
  keystream — English prose and place-name profiles — both fail correction.
- The specific test cannot be run.

**Grade: PROMISING HYPOTHESIS, UNTESTABLE WITH CURRENT PUBLIC DATA.** It has not
earned promotion, and nothing here was adjusted to keep it alive. If the recovered
name list eventually produces no fit across the 22 preregistered readings, it should
be downgraded to EXHAUSTIVELY ELIMINATED WITHIN THAT MODEL and abandoned.

---

## Checkpoint E — what was achieved

- **(B) Established that the critical historical configuration cannot currently be
  recovered here**, with the boundary drawn precisely: the modern list is published
  but unreachable in this environment; the 1988–89 list additionally needs the full
  1997 change record, of which about a third is documented.
- **(D, partial) Authentic reconstruction changed the object model** — the cylinder
  is static with an internal rotating hour ring, correcting a repository error; the
  three-part upper/hour-ring/lower structure is established; lettering is stamped.
  None of this weakens the hypothesis, but it changes what a reading procedure may
  assume.
- **(E, partial) A second external source named by Sanborn was tested and failed.**
  The Morse material as a key tape: 13,680 alignments, best 5/24, below chance.

**Next action, in priority order:**
1. Retrieve the modern per-sector list from `weltzeituhr-berlin.de` with an ordinary
   browser, then run EXP-024 unchanged. This is a minutes-long task for a human and
   is the single highest-value step available.
2. Obtain the 1997 restoration records under Hans-Joachim Kunsch — one document that
   would specify every change at once, enabling the 1989 reconstruction by subtraction.
3. Establish the cylinder's orientation relative to north, without which no
   bearing-based reading can be evaluated.

**K4 remains unsolved. No mechanism is claimed and no verifier submission is
warranted.**
