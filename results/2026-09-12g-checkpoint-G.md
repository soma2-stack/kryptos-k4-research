# Result record — 2026-09-12 (session 7) — Checkpoint G

Branch `claude/dreamy-archimedes-79k6u0`. Ciphertext SHA-256
`eea813570c7f1fd3b34674e47b5c3da8948026f5cefee612a0b38ffaa515ceab`.
Regenerate with `./run_all.sh`. Python 3.11, standard library only.

**Blind experiment intact. No contamination incidents.** The supplied 146-place file
is object/history data, not K4 plaintext, and is admissible; its provenance is
recorded. `solvekryptos.com` excluded on every query. Only `EASTNORTHEAST` and
`BERLINCLOCK` remain admitted as constraints. **EXP-024 was not run and not
modified.**

**Outcome: G — one blocker is dominant and a human could act on it directly. But it
is not the blocker Checkpoint F named.** The identity of the bottleneck changed.

---

## 1 — Blocker 1: CLOSED for the modern endpoint

The supplied file validated cleanly before use:

| Check | Result |
| --- | --- |
| Declared vs actual entries | 146 / 146 |
| Every entry has name + UTC | yes |
| Indices contiguous 1–146 | yes |
| Duplicate names | none |
| sha256 | `06b777ab…` (recorded in the stored copy) |

Stored as `data/weltzeituhr_modern_official.json`, every record marked **MODERN**,
with the official source, URL and retrieval date. No historical `pre1997_*` field was
overwritten. The guard in `wz_panels.build_clock()` is untouched.

**Five cross-checks against independently established repo facts, all passed:**
all six documented 1997 additions are present; all documented renames show the new
form and not the old; Kiew sits at UTC+2, consistent with a documented zone move.

---

## 2 — Two structural findings from the data itself

**The 24 faces are confirmed, not inferred.** The list contains exactly **24 distinct
whole-hour zones, contiguous UTC−10 … UTC+13** — matching the 24 physical faces.
Checkpoint F had this as INFERRED; it is now established. Five half-hour places
(Marquesas, Teheran, Kabul, Neu-Delhi/Colombo, Rangun) are *extra* and cannot own a
face; **how they are physically placed is a new open question.**

**Apia is resolved, and it retires a blocker.** UTC+13 is the same *hour* as UTC−11,
one day apart, so Apia's 2011 change is a date-line/label matter on the **same
physical face** — not evidence of a panel change.

---

## 3 — Table order is not physical order: demonstrated, not cautioned

Checkpoint F independently established from December 1997 reporting that **Preßburg
stands on an aluminium panel between Bern and Belgrad**. In the supplied table:

```
62  Bratislava (Pressburg)
63  Belgrad
64  Rom
65  Tunis
66  Kinshasa
67  Bern
```

Bern is four entries away, with Rom, Tunis and Kinshasa interposed. **The website
table order is therefore demonstrably not the engraved order.** Your instruction not
to infer physical placement from table order is now an empirical finding.

Related: `Bratislava (Pressburg)` and `Vilnius (Wilna)` carry parentheses — almost
certainly a website convention, not engraved text. Parenthetical forms must not be
treated as engraved names without a photograph.

---

## 4 — A Checkpoint F error, corrected

**2015 was not a restoration.** In July 2015 the Weltzeituhr was placed under
**monument protection (Denkmalschutz)** by the Berlin State Heritage Office.
Checkpoint F recorded a "2015 restoration change set" as a seventh blocker; that came
from misreading an earlier summary. **Blocker 7 is retired.**

This helps rather than hurts: monument protection *bounds* later change, so the
modern published list most likely reflects the post-1997 state, and 1997 is the
principal reversal boundary — as Checkpoint E originally framed it.

(Noted for completeness: in September 2024 a delivery truck dented the **Wellington**
panel; repair was quoted at €23,000 requiring complete refabrication of the damaged
plates. Irrelevant to 1989, but it shows panels are individually refabricable.)

---

## 5 — 1997 change set advanced

A July 2015 taz article, *"Unter Schutz, aber nicht ganz echt"*, yielded two changes
no earlier source gave:

- **Managua** was **added in 1997** — "not only Tel Aviv … was missing in the
  original state, but also Managua". Sixth documented addition.
- **"Mexico City" → "Mexiko-Stadt"**. The GDR clock carried the **English** form. The
  writer flags this as surprising, which argues against confusion. Fifth documented
  rename, and the most counterintuitive one recovered so far.

| Category | Documented | Outstanding |
| --- | --- | --- |
| Additions 1997 | 6 of ~20 — Jerusalem, Tel Aviv, Kapstadt, Oslo, Seoul, **Managua** | 14 unnamed |
| Renames 1997 | 5 — Leningrad→Sankt Petersburg, Alma-Ata→Almaty, Aschchabad→Aschgabat, Bratislava→Preßburg, **Mexico City→Mexiko-Stadt** | unknown how many more |
| Zone moves 1997 | 1 — Kiew (origin UTC+3, INFERRED) | unknown |
| Removals 1997 | 0 | entirely unknown |

---

## 6 — Completion metric

| Measure | Value |
| --- | --- |
| Entries whose pre-1997 presence is determined | **12 / 146 (8.2%)** |
| Zones containing ≥1 classified entry | 7 |
| Sectors fully reconstructed (1989 names) | **0 / 24** |
| Historical **band** assignments known | **0 / 146** |
| Historical **order** relations known | **1** (Bern–Bratislava–Belgrad) |
| Unresolved 1997 additions | 14 of 20 |
| Unresolved 2015 changes | **n/a — blocker retired** |

---

## 7 — The main result: a name list can never unblock EXP-024

EXP-024's preregistered procedures read each sector's **upper** and **lower** band
**in physical order**. A name list supplies neither. So suppose the 1989 names per
sector were known *exactly* — how many physical arrangements remain?

Summing `k!` orderings × `2^k` band splits over the 24 sectors (UTC+1 alone has 19
names, UTC+2 and UTC+3 have 15 each):

> **≈ 10^125 arrangements remain consistent with a perfect name list.**

EXP-024 as preregistered tries ~10^6 alignments.

**Therefore recovering every 1997 change — even all twenty additions, every rename,
every zone move — would still not make the test runnable.** Guessing among the
arrangements is both computationally impossible and would destroy the preregistration
through unbounded multiple testing.

**The binding constraint is not which names were on the clock. It is where they sat.**

That reverses the priority order this programme has carried since Checkpoint D. The
Auswärtiges Amt correspondence, still the best route to the *name* list, is no longer
the dominant blocker — because names alone are insufficient.

---

## Checkpoint G — status and the single dominant blocker

| # | Blocker | Status |
| --- | --- | --- |
| 1 | modern per-sector list | **CLOSED** |
| 2 | ~20 names added 1997 | PARTIAL — 6 of 20 |
| 3 | 1997 zone reassignments | PARTIAL — Kiew only |
| 4 | removals 1997 | UNKNOWN |
| 5 | upper/lower band assignment | UNKNOWN — 0 of 146 |
| 6 | cylinder orientation vs north | UNKNOWN |
| 7 | 2015 change set | **RETIRED** — was monument protection, not restoration |
| 8 | **physical order within each sector** | **UNKNOWN — DOMINANT** |

**The dominant blocker, stated so a human can act on it:** dated, legible photographs
of the Weltzeituhr drum taken before October 1997 — ideally 1988–89 — at resolution
sufficient to read the names on the **upper and lower aluminium bands** of individual
sectors, together with enough of the neighbouring faces to fix order.

Candidate holders already identified: **DDR-Bildarchiv**, **picture-alliance**
(holds 1969–1982 material), **Getty Images** (~231 images tagged Weltzeituhr
Alexanderplatz), the **Bundesarchiv**, and the **DDR Museum**. Images cannot be read
through this toolchain; this is a human visual-transcription task.

One such photograph would settle several entries at once, and the 146-name modern
endpoint now makes any readable panel far easier to interpret — a photograph no
longer has to be read cold, only matched against a known candidate set for its zone.

**The Weltzeituhr running-key hypothesis is unchanged in standing: PROMISING
HYPOTHESIS, UNTESTABLE WITH CURRENT PUBLIC DATA.** It was not advanced and not
rescued. EXP-024 remains frozen, unmodified and unrun.

**K4 remains unsolved. No mechanism claimed, no verifier submission warranted.**
