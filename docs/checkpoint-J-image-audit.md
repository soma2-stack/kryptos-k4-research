# Checkpoint J — independently inspected image evidence

Input identity was not inferred from filenames. All three uploads lack EXIF and
IPTC metadata. After inspecting them separately, independently retrieved publisher
images were compared visually:

| Local ID | Identification | Basis | Use |
|---|---|---|---|
| J01 | Picture Alliance 16008401 | Exact scene/framing match to linked archive preview, 414x600 | Context; text too small for reliable complete transcription |
| J02 | Picture Alliance 16008415 | Exact scene/framing/banner match to linked archive preview, 600x389 | Priority-face reading at uploaded 1280x830 resolution |
| J03 | HanisauLand asset 153695.jpg; PA accession UNKNOWN | Match to independently fetched 4065x2575 source | Main reading, corroborated by J02 |

The upload versions differ in bytes/resolution from publisher derivatives; visual
identity is not claimed as a byte-hash match. Dates come from publisher captions
and established visual identities, not an assumption that banners prove the day.

Sources checked 2026-09-12:
- https://www.picture-alliance.com/webseries/weltzeituhr-in-berlin-w194131
- https://www.hanisauland.de/wissen/spezial/geschichte/deutsche-einheit/mauerfall-2009-kapitel-4.html

Both archive entries are captioned 04.11.1989; the bpb image caption identifies the
same day and credits picture alliance / akg. Direct source URLs and SHA-256 hashes
are in data/weltzeituhr_checkpoint_J.json; uploaded bytes and the larger bpb source
are preserved under data/evidence/checkpoint-J. No photograph is represented as a
new observer's independent human transcription.

## Frozen lines (top to bottom)

| Face | Upper | Lower |
|---|---|---|
| UTC+0 | REYKJAVIK / DUBLIN / LONDON / LISSABON / ALGIER / MADEIRA / BISSAU | CASABLANCA / CONAKRY / DAKAR / BAMAKO / ACCRA |
| UTC+1 | AMSTERDAM / BERLIN / BRUSSEL / BUDAPEST / MADRID / PARIS / PRAG / STOCKHOLM / WARSCHAU | KOPENHAGEN / WIEN / BERN / BELGRAD / ROM / TUNIS / BRAZZAVILLE / KINSHASA / LUANDA |
| UTC+2 | BUKAREST / HELSINKI / SOFIA / ATHEN / NIKOSIA | BEIRUT / DAMASKUS / KAIRO / KHARTUM / LUSAKA / MAPUTO |

The bands' physical ends are visible. The substantial blank spaces above the UTC+0
lower list and between KAIRO and KHARTUM are visible empty space, not cropped-away
lines. Three faces total 272 normalized letters (81+120+71). Order is visual,
not inferred from geographic membership or alphabetic/latitude sorting.

**Retraction:** the inherited claim that ATHEN is absent in November 1989 is false.
It appears between SOFIA and NIKOSIA in both close images. This settles the current
reading, not the date when ATHEN was first added. The old UNKNOWN is resolved, not
silently counted as a conflicting city name.

UTC+3 upper: MURMANSK / LENINGRAD / MOSKAU / KIEW, MEDIUM-HIGH confidence.
Lower accepted as a partial ordered observation: ANTALYA / UNKNOWN / BAGDAD / ADEN /
SANA / ADDIS ABEBA / MOGADISCHU / DARESSALAM / UNKNOWN. Lower confidence LOW-MEDIUM;
second/last exact strings remain unresolved. ANTALYA appears in place of inherited
ANKARA; the conflict is retained, not overwritten. No UTC+3 text enters EXP-031.
Other legible side-face fragments, uncertain Greenland spellings and blank bands
are recorded separately in the dataset, outside the experiment arc.

The original photo dataset stays intact as historical evidence and to preserve
prior experiment hashes. The new explicit snapshot governs EXP-031; old graph
readiness figures do not describe this new snapshot. No universal order rule or
modern city list was consulted. Current evidence is sufficient for the narrowly
preregistered multi-face experiment, so no further image is required to run it.
