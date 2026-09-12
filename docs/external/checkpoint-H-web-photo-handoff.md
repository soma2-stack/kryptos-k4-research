# Checkpoint H external web-photo handoff

Date: 2026-09-12
Prepared outside Claude's restricted-web environment.
Purpose: provide source-backed historical Weltzeituhr evidence that Claude cannot retrieve directly.

## Handling / provenance rule

This file contains web-retrieved metadata and visual transcriptions made from images rendered by an external web-search environment. Treat these as EXTERNAL-AGENT TRANSCRIPTIONS, not as Claude's own visual verification. Preserve the source URL and confidence grade for every fact. Do not promote an uncertain transcription to historical ground truth without a second source or a locally viewable image.

The GitHub connector available to the external agent can only create UTF-8 text files, so the JPEG bytes could not be committed directly. The direct image URLs are recorded below. If image bytes later become available as session files, re-transcribe them independently and supersede the external-agent transcription where appropriate.

---

## Source 1 - Bundesarchiv, exact target-era frame

Accession: Bild 183-1989-0830-028
Archive: German Federal Archives / Bundesarchiv (Bild 183)
Photographer: Erwin Schneider
Date: 30 August 1989
Archive title: Berlin, Fernsehturm, Weltzeituhr
Confidence: PRIMARY / ARCHIVE-DATED

Bundesarchiv search record:
https://www.bild.bundesarchiv.de/dba/en/search/?query=Bild+183-1989-0830-028

Wikimedia Commons file page:
https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_183-1989-0830-028,_Berlin,_Fernsehturm,_Weltzeituhr.jpg

Direct Wikimedia image:
https://upload.wikimedia.org/wikipedia/commons/9/9d/Bundesarchiv_Bild_183-1989-0830-028%2C_Berlin%2C_Fernsehturm%2C_Weltzeituhr.jpg

Commons metadata states 567 x 800 px, 68,001 bytes, SHA-1 0c3d0288dc6711e386112dc22df050eac4f3abfc.

External-agent visual transcription from the rendered original:

- one visible upper panel: CHABAROWSK
- immediately adjacent upper panel: MAGADAN / SACHALIN

Interpretation already used by the repo remains supported: these correspond to UTC+10 and UTC+11 and directly observe one consecutive-zone adjacency in August 1989.

Grade: HIGH for the three readable names and their photographed adjacency; exact band = upper is visually clear.

---

## Source 2 - Bundesarchiv 1984 detail

Accession: Bild 183-1984-1419-014
Archive: German Federal Archives / Bundesarchiv
Photographer: Peter Heinz Junge
Archive caption date: 19 April 1984 (Commons structured date is month-level April 1984; original caption carries 19.4.84)
Title: Berlin, Weltzeituhr am Alexanderplatz
Confidence: PRIMARY / ARCHIVE-CAPTIONED

Commons file page:
https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_183-1984-1419-014,_Berlin,_Weltzeituhr_am_Alexanderplatz.jpg

Direct Wikimedia image:
https://upload.wikimedia.org/wikipedia/commons/d/d5/Bundesarchiv_Bild_183-1984-1419-014%2C_Berlin%2C_Weltzeituhr_am_Alexanderplatz.jpg

Commons metadata: 581 x 800 px, 69,083 bytes, SHA-1 3d84b3dd285ffaaee40d78f58ccf0b4ec5ac680b.

External-agent visual observations (do not use as a full transcription without local re-check): the image clearly shows multiple consecutive eastern faces, including panels containing ALMA-ATA / TASCHKENT, KRASNOJARSK / NOWOSIBIRSK, IRKUTSK / ULAN-BATOR, JAKUTSK, and a partial CHABAROWSK/WLADIWOSTOK region. This frame is useful for testing pre-1989 layout stability against the 30 Aug 1989 frame.

Grade: HIGH that these historical forms are visibly present; MEDIUM for exact face-by-face grouping until locally re-transcribed.

---

## Source 3 - mid-1970s color photograph exposing the Berlin / UTC+1 side

Publisher page: WELT
Article: "DDR als Urlaubsland: Wie alte Reisefuehrer das Land zeigen"
Article date: 9 Nov 2021
Photo caption on page: "Weltzeituhr und 'Interhotel Stadt Berlin' am sozialistisch umgestalteten Alexanderplatz in Ost-Berlin Mitte der 70er-Jahre"
Photo credit: pa/akg-images/Straube
Historical-date grade: SOURCE-CAPTIONED MID-1970s (not an exact day/year)

Article:
https://www.welt.de/reise/deutschland/article217168174/DDR-als-Urlaubsland-Wie-alte-Reisefuehrer-das-Land-zeigen.html

Direct rendered image used for transcription:
https://img.welt.de/img/reise/mobile217168152/1920313707-coriginal-w1200/Berlin-Alexanderplatz-Weltzeituhr-Foto.jpg

This is currently the highest-value externally found photograph for Claude's new Tier-1 goal because it visibly exposes the UTC+1/Berlin face before the 1997 restoration.

External-agent transcription of the UPPER UTC+1 panel, read directly from the rendered 1200px image:

AMSTERDAM
BERLIN
BRUSSEL
BUDAPEST
MADRID
PARIS
PRAG
STOCKHOLM
WARSCHAU

Confidence: HIGH. The entire upper group is legible in the rendered source.

This is historically valuable because it predates the 1997 restoration and gives the physical within-band order of nine UTC+1 entries, not merely membership.

The lower UTC+1 panel is visible but not sharp enough in the externally rendered copy for a responsible full transcription. The clearly readable subset includes KOPENHAGEN, WIEN, BELGRAD and TUNIS; other lines should remain UNKNOWN here until a higher-resolution crop or independent image is available. Do NOT infer the missing lower-band sequence from the modern list.

---

## Source 4 - second mid-1970s WELT / akg view

A second WELT image from the same general period provides a closer, more frontal arc from roughly UTC+0 through eastern zones.

Direct image:
https://img.welt.de/img/reise/mobile236442435/3522500817-ci102l-w1024/Berlin-Alexanderplatz-Weltzeituhr-Foto-Berlin-Alexanderplatz.jpg

A WELT page using this image identifies the historical East-Berlin setting; combine with Source 3 rather than treating it as an independent date unless its original agency metadata is recovered.

The upper UTC+1 order independently appears consistent with Source 3.

Grade: SUPPORTING IMAGE; DATE NOT YET PRIMARY-VERIFIED.

---

## Source 5 - 1970s/early-state evidence from WELT article caption

The Source 3 WELT page explicitly says the photograph depicts East Berlin "Mitte der 70er-Jahre" and credits `pa/akg-images/Straube`. This is stronger provenance than appearance/fashion dating and is the basis for treating Source 3 as pre-1997 historical-layout evidence.

---

## Source 6 - Berlin official publication: original count and political selection

Search-accessible Berlin government PDF:
https://www.berlin.de/aktuell/ausgaben/2019/dezember/aktuell-104-webversion.pdf

Publication: BERLINER EREIGNISSE / LIFE IN BERLIN, December 2019
Article: "Alexanderplatz - Transforming the square 50 years ago"
By Heike Schueler

Search-extracted passage reports that the original clock displayed **80 city names** on 24 aluminium plates and that each location was approved by the SED leadership. It specifically says **Athens was taboo because of the military government**.

This is important because it independently supports:

1. the original 1969 list was much smaller than the modern 146-name endpoint;
2. city inclusion/exclusion was politically curated, so historical membership cannot be reconstructed safely from modern geography alone;
3. absence from the historical clock can be politically meaningful rather than a simple space/importance decision.

Grade: RELIABLE GOVERNMENT PUBLICATION / SECONDARY HISTORICAL ACCOUNT.

Related independent Tagesspiegel profile of Erich John also states that Athens was omitted because of the military dictatorship and that the designers preferred politically "progressive" cities:
https://www.tagesspiegel.de/berlin/die-weltzeituhr-kennt-jeder-niemand-ihren-erfinder-6541270.html

---

## Source 7 - post-1997 closeup useful only as a differential aid

This is NOT historical-state evidence, but it is a high-resolution view of the modern lower UTC+1 face and may help interpret blurred historical text by comparison.

Image:
https://medienwerkstatt-online.de/lws_wissen/bilder/27607-4.jpg

Visible modern lower UTC+1 order:

OSLO
KOPENHAGEN
WIEN
BERN
PRESSBURG
BELGRAD
ROM
TUNIS
KINSHASA

Use only as MODERN comparison. Do not project these entries backward. Already-known historical facts require at least OSLO to be treated as a 1997 addition and PRESSBURG as the post-1997 replacement for BRATISLAVA.

---

## Immediate consequence for Checkpoint H

The mid-1970s Source 3 closes a significant part of the new Tier-1 blocker:

- UTC+1 upper band: physically ordered and pre-1997, 9 names, HIGH confidence.
- UTC+1 lower band: still incomplete from the externally rendered resolution.

So the next acquisition target is now narrower than "find the UTC+1 face": obtain a legible pre-1997 close-up (or high-res scan/crop) of the **lower UTC+1 band**, ideally the same face, sufficient to establish every historical line and its order.

Potential archival/search handles:

- WELT source photo credit: pa/akg-images/Straube, captioned mid-1970s.
- picture-alliance / akg-images may hold the original high-resolution frame.
- modern lower-face comparison gives a constrained candidate set but MUST NOT be used to fill historical UNKNOWN lines.

Do not run EXP-024 from this handoff alone unless the repo's Tier-1 completeness rule is genuinely satisfied after independent review.
