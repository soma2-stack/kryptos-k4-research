# Checkpoint H critical correction: 1985 maintenance changes

Date: 2026-09-12
Prepared outside Claude's restricted-web environment.

## Source

Tagesspiegel, Kerstin Decker, 14 Apr 2019:
`50 Jahre Alex: Die Weltzeituhr kennt jeder, niemand ihren Erfinder`

https://www.tagesspiegel.de/berlin/die-weltzeituhr-kennt-jeder-niemand-ihren-erfinder-6541270.html

The article is a long profile/interview with Weltzeituhr designer Erich John and contains several directly relevant historical details.

## Critical finding

The article states that during the **first major maintenance in 1985** the following names were newly engraved:

- **Athen**
- **Kopenhagen**
- **Wien**
- **Rom**

It separately states that **Istanbul** was added in **1997** at the request of Berlin's governing mayor.

Evidence grade: STRONG SECONDARY / DESIGNER-PROFILE CONTEXT. This is not a primary maintenance ledger, but it is materially stronger than later unsourced summaries and is embedded in an interview/profile of Erich John.

## Immediate consequence: Source 3 dating conflict

`docs/external/checkpoint-H-web-photo-handoff.md` Source 3 was captioned by WELT as **mid-1970s**, yet the externally transcribed lower UTC+1 band visibly includes at least **KOPENHAGEN** and **WIEN**, which this Tagesspiegel source says were only added in **1985**.

Therefore at least one of the following is wrong:

1. the WELT mid-1970s date/caption;
2. the external lower-band transcription;
3. the Tagesspiegel 1985 historical account.

Until resolved, Source 3 MUST NOT be used as mid-1970s evidence for the presence of Kopenhagen/Wien/Rom, and its date grade should be downgraded to **DATE DISPUTED** for cryptanalytic reconstruction.

The upper UTC+1 transcription may still be useful as physical-order evidence from some pre-1997 date, but the image cannot currently establish a mid-1970s state safely.

This directly supports Claude's own Checkpoint-H conclusion that layout stability is pivotal and that source dates must be tested rather than assumed.

## Important positive implication for the 1988-89 target state

Because these engravings were added in 1985, the target 1988-89 state SHOULD contain, barring a later removal before 1989:

- Athen
- Kopenhagen
- Wien
- Rom

This is evidence about the target-era membership, not merely modern membership.

Do not promote that to exact band/order without visual or primary-layout evidence.

## Half-hour placement question substantially answered

The same Tagesspiegel article quotes/describes Erich John explaining that historical half-hour places had a literal **`+ 30'`** inscription after their names. It specifically names:

- New Delhi
- Kabul
- Rangun

This means the repo's open question about how half-hour locations were represented should be updated: at least these historical entries were placed on ordinary faces with an explicit +30-minute annotation rather than receiving separate faces.

Evidence grade: STRONG SECONDARY / DESIGNER-ATTRIBUTED.

This is especially useful because it explains how 24 whole-hour faces can carry locations offset by 30 minutes.

## Original political-selection evidence reinforced

The article also states:

- Athens was absent originally because of the Greek military dictatorship;
- Bonn was omitted as a politically undesirable example;
- the DDR preferred cities considered politically "progressive" or promising;
- New York could not realistically be omitted.

This reinforces the existing rule that historical city membership cannot be reconstructed from modern importance/geography alone.

## Structural description from the designer profile

The article describes the clock physically as:

- upper metal ring = north-hemisphere structural ring;
- lower metal ring = south-hemisphere structural ring;
- equator = hour band in the middle.

Do NOT infer from this wording that all cities on the upper/lower panels are strictly separated by geographic hemisphere; the modern visible inscriptions appear more complicated. Treat it as physical-design terminology unless independent evidence proves a city-placement rule.

## Recommended repo actions

1. Mark Source 3's historical date as **DISPUTED** rather than mid-1970s ground truth.
2. Add 1985 as a documented change boundary before the target 1988-89 state.
3. Add Athen, Kopenhagen, Wien, Rom as documented 1985 additions.
4. Add Istanbul as a documented 1997 addition.
5. Resolve the half-hour-placement open question at least for New Delhi/Kabul/Rangun as `name +30'` on an ordinary face.
6. Recompute the unexplained 1969->modern arithmetic after subtracting documented 1985 additions separately from 1997 changes.
7. Prioritize any dated 1988-89 UTC+1 image, because that directly bypasses the date conflict and captures the target state after the 1985 engravings.

## Blindness / contamination

No purported K4 plaintext was sought or exposed. This is historical object evidence only.
