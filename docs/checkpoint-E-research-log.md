# Checkpoint E — historical research log (Weltzeituhr, pre-1997)

Session 5, 2026-09-12. Recorded so the next researcher does not repeat the same
searches, and so the boundary between "not found" and "does not exist" stays clear.

**Contamination protocol in force throughout.** `solvekryptos.com` was excluded on
every query. No claimed-K4-solution site was used as a historical source. No
purported K4 plaintext was sought, seen, or ingested. **No new incidents.**

## Environment limitation, stated first because it shapes everything below

`WebFetch` is blocked by this session's network egress proxy for **every** external
domain attempted — `en.wikipedia.org`, `de.wikipedia.org`, `media.defense.gov`,
`www.elonka.com`, `www.weltzeituhr-berlin.de`, `www.scientificamerican.com`. Only
`WebSearch` works, and it returns synthesised summaries that consistently decline to
enumerate long lists.

This matters for the verdict: **the modern per-sector city list is published** —
`weltzeituhr-berlin.de` has a "Places on the Worldtimeclock" page — but it could not
be retrieved here. The blocker is this environment, not the historical record. A
human researcher with an ordinary browser could obtain the modern list in minutes.

## What was searched

| Target from the brief | Searched | Result |
| --- | --- | --- |
| Kunsch Metallbau archive material | yes | Firm confirmed as builder and restorer; no archive contents surfaced |
| Hans-Joachim Kunsch | yes | **Recovered**: metalsmith/metal sculptor who executed the 1969 construction on site, and led the 1997 metal restoration |
| Stefan Kunsch statements | yes | Nothing surfaced |
| Erich John drawings | yes | Designer confirmed (Womacka planning group); no drawings surfaced |
| Original 1969 construction records | yes | Team size (~120 specialists), ~9 month build, Coswig gear factory, volunteer brigades. No documents |
| Original lettering templates | partial | **Recovered**: names are composed of **stamped** letters, implying punches/templates existed. Survival UNKNOWN |
| 1997 restoration records | yes | Oct–Dec 1997, 350,000 DM, under Kunsch. Three renames and four of twenty additions named |
| Names added / removed / renamed / moved in 1997 | yes | **Partial only** — see below |
| Berlin municipal records, museum/design archives | yes | Nothing retrievable |
| Photographs before 1990, postcards, newspaper photography | yes | Picture-agency and panorama pages surfaced, but images cannot be read through this toolchain |
| East German publications | yes | Nothing retrievable |

## What was recovered, with grades

**MULTIPLE INDEPENDENT SOURCES**
- 24-sided cylinder, one face per time zone, 15° each; 10 m high, 16 t; column 2.7 m × 1.5 m.
- Designed by Erich John; opened 30 September 1969.
- The city-name cylinder is **static**; a **rotating hour ring** carries the hours through the zones, driven by a converted Trabant gearbox. *This corrects an earlier error in this repository, which described the drum itself as rotating.*
- An orrery above rotates once per minute. A compass-rose mosaic sits at the base.
- 1997 restoration, Oct–Dec, 350,000 DM, metal restoration under Hans-Joachim Kunsch.

**SINGLE RELIABLE SOURCE**
- **Three-part cylinder**: city names on the **upper** aluminium disk, the rotating hour ring in the **middle**, city names on the **lower** disk. This is the upper/lower band structure the brief asked for.
- The rotunda also carries an entry for the **international date line**.
- Letters are **stamped**.
- 1997 renames: Leningrad → Sankt Petersburg; Alma Ata → Almaty; Bratislava → Pressburg (reported to have drawn Slovak diplomatic protest).
- 1997: ~20 cities added that the GDR had omitted for political reasons — **Tel Aviv, Cape Town, Seoul, Jerusalem** named; the other sixteen are not.
- 1997: time-zone assignments changed for some cities — **Kyiv** named; no full list.

**CONFLICTING, recorded unresolved**
- Total places: **80** (1969, one source) / **146** / **148**. These cannot be reconciled from sources reached.

**UNKNOWN — not filled with modern data**
- The ordered per-sector name list for 1988–89.
- Which names sit in the upper band versus the lower.
- Berlin's and Moscow's exact sectors.
- The date line's position on the rotunda.
- The cylinder's orientation relative to north.
- The sixteen unnamed 1997 additions; any 1997 removals; the full zone-reassignment list.

## The reconstruction route that would work

Take the published modern per-sector list → subtract the twenty 1997 additions →
reverse the three documented renames → revert the documented zone reassignments.

Four of the twenty additions and three renames are in hand. **The method is sound;
the inputs are missing.** The 1997 restoration records under Hans-Joachim Kunsch are
the single highest-value document, because they would specify every change at once.

## Note on the orientation datum

Even with a full name list, a reading that *starts from a compass bearing* — which
is what `EASTNORTHEAST` would supply — additionally needs the cylinder's orientation
relative to north. Without it a bearing cannot be converted into a sector.

And a caution against over-reading any future orientation datum: with 24 faces every
15°, **any** bearing lies within 7.5° of some face centre. Proximity alone will carry
no information; only an exact, independently documented alignment would.
