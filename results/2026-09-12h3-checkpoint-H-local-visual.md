# Checkpoint H (session 10) — first locally-read pixels, and a date that decides everything

> **SUPERSEDED IN PART — see [Checkpoint H, 1974 correction](2026-09-12h4-checkpoint-H-1974-correction.md).**
> Two claims in this record are withdrawn. (1) The CET face's date is **not** disputed
> between mid-1970s and [1985, 1997): a separately published Straube frame explicitly
> dated **1974** already shows KOPENHAGEN and WIEN, so `nachgraviert 1985` cannot be read
> as first addition, and this frame reads consistently as **mid-1970s**. (2) The 46-name
> arithmetic gap is **not** "closed": the remainder is unexplained, not dated to 1985.
> The CET transcription itself stands unchanged; only the era it attests has changed —
> and the change makes the Tier-1 gap ~14 years instead of ~4.

This is the first session in which this agent has actually *seen* a photograph of the
Weltzeituhr. Four images were pasted into the conversation. Every reading below is my
own visual reading, marked LOCAL VISUAL EVIDENCE in `data/weltzeituhr_photos.json`,
and it supersedes the external-agent text handoff wherever the two cover the same face.

## What the uploads were, and were not

- The uploaded ZIP (`claude_weltzeituhr_pack.zip`) contained **no image bytes** — its own
  README says so. Its `weltzeituhr_modern_146_official.json` is content-identical to the
  repo copy. So the four pasted images are the only pixels this programme has had.
- The images are conversation attachments, not files on disk: no path, no sha256. A later
  session without them cannot re-verify these readings and must treat them as this
  session's testimony. That limitation is recorded in the dataset.
- `i.pinimg.com` re-tested: `connect_rejected`. Egress to image hosts remains closed.

## The CET face, read in full

```
UPPER (alphabetical, 9 names, 62 letters)
  AMSTERDAM BERLIN BRUSSEL BUDAPEST MADRID PARIS PRAG STOCKHOLM WARSCHAU
LOWER (6 names, 35 letters)
  KOPENHAGEN LONDON WIEN ROM BELGRAD TUNIS
TOTAL 97
```

My upper-band reading reproduces the external handoff's nine names **and their order**
independently. The lower band the handoff called untranscribable resolves to six names;
I read **LONDON**, which the handoff missed, and place **ROM** in the lower band. The
lower band is **not** alphabetical: by latitude it runs north-to-south with one
inversion (ROM before BELGRAD). So no single ordering rule governs both bands, and any
reading procedure that assumes one does is wrong.

The letter-count shortfall that dominated the last three checkpoints is now **zero on
this face**. That is a real advance in the reconstruction and it is not a cryptanalytic
result.

## On the 97 — deliberately deflated

62 + 35 = 97 is exactly K4's length. It is **OBSERVATION, NOT EVIDENCE**:

- I did not predict 97 in advance.
- 24 faces × 3 natural quantities ≈ 72 values over a 4–137 range → ~0.54 exact hits at
  97 expected by chance. One hit is unremarkable.
- The count is fragile: without LONDON it is 91; an unseen seventh lower line exceeds 97.
- The face's date is unresolved, so this may not even be the target-era face.

The single non-free element is *which* face: the Berlin/CET face named by the
`BERLINCLOCK` crib, and the face this programme was already targeting before the count
was taken. That does not lift the Weltzeituhr hypothesis above PROMISING HYPOTHESIS, and
it is not grounds for running EXP-024.

## Two physical rules, now established

1. **Half-hour notation is literal `+30`** — NEW DELHI +30, COLOMBO +30, RANGUN +30,
   KABUL +30, read directly. This independently confirms the Tagesspiegel report of a
   `+ 30'` inscription. Consequence: any tape reading crossing those faces must choose
   whether to skip or transliterate digits, since K4 has none — a free choice, hence an
   extra degree of freedom that must be penalised.
2. **Upper = northern, lower = southern, within each UTC sector** — confirmed on four
   independent face pairs (KRASNOJARSK / HANOI·BANGKOK·PHNOM PENH·JAKARTA;
   IRKUTSK·ULAN-BATOR / PEKING…SINGAPUR; JAKUTSK / PJÖNGJANG·TOKYO·SEOUL;
   CHABAROWSK·WLADIWOSTOK / SYDNEY·CANBERRA·MELBOURNE), and matching the account of the
   upper metal ring as the northern-hemisphere structural ring. Band assignment is now
   **predictable from latitude**, which removes the 2^k half of the per-face layout
   entropy. The k! within-band ordering remains.

## The stability question is now answered — negatively

**NOWOSIBIRSK sits with KRASNOJARSK in the April 1984 frame and with
OMSK/ALMATY/TASCHKENT in the modern frame.** A place changed faces. Local visual at both
ends. Backward reversal from the modern list therefore cannot assume a place keeps its
face; membership must be read per era. This is the strongest single argument against
reconstructing 1988–89 from the modern list plus a change log.

Within the target window, stability is **UNTESTED** — I hold no two frames of the same
face in two different target-era years. Not established, not refuted.

Target-era spellings read locally that differ from the modern list: **SWERDLOWSK,
ASCHCHABAD, ALMA-ATA, LENINGRAD, PHOENGJANG**. At least five names differ, so the
target-era letter multiset differs from the modern one. The Soviet-zone blocker reaches
individual spellings, not merely zone boundaries.

## The arithmetic gap closes; a sharper problem replaces it

146 modern − 80 original (1969) − 20 added (1997) = **46**, exactly the quantity flagged
as unexplained last session. The **1985 first major maintenance** is the third change
boundary that quantity requires. With boundaries at 1969, 1985 and 1997, any frame
datable to **[1985, 1997)** shows the 1988–89 target state. Dating became a yes/no
question instead of an open growth curve. (The arithmetic closing exactly is suggestive;
it is not proof that 1985 added 46 names — the source names only four.)

But the one frame with a fully transcribed face is **internally contradictory**:

| evidence | implies |
|---|---|
| KOPENHAGEN, WIEN, ROM present (named 1985 additions) | ≥ 1985 |
| WELT caption "mid-1970s"; 1970s clothing and vehicles | < 1985 |
| **ATHEN** — the fourth named 1985 addition — **not visible** | < 1985 |
| LENINGRAD, MOSKAU present (local visual, caption-free) | < 1997 |

Either the Tagesspiegel 1985 change set is wrong, or the WELT caption is. The cheapest
reconciliation is that 1985 **re-engraved** names already on the drum — which would
vindicate the 1970s caption and, ironically, also argue for stability. That is a
reconciliation, not evidence. No further analysis of the pixels in hand can settle it.

## Reconstruction metric (EXP-027, regenerated)

| quantity | value |
|---|---|
| faces identified | **15 / 24 (62.5%)** |
| faces locally transcribed by me | 14 |
| faces with upper band transcribed | 14 |
| faces with lower band transcribed | 8 |
| faces with upper band COMPLETE | 2 |
| faces with lower band COMPLETE | 1 |
| faces COMPLETE (both bands, ordered) | **1** (CET; local visual) |
| adjacency edges OBSERVED | 11 |
| adjacency edges TRANSITIVE | 25 |
| longest contiguous chain | **7 faces** (UTC−2W … UTC+4) |
| faces from 1988–89 evidence | 2 |
| faces from 1984 evidence only | 6 |
| faces from the DISPUTED-DATE frame | 7 (includes CET) |

Pseudo-nodes that name a band or a group rather than a face (2) are excluded from the
face count so circumference is never overstated. A band read as partial is loaded with
an explicit incompleteness marker, so a partially read face can never count as complete.

## TIER-1 VERDICT: **NOT MET**

Tier 1 has two parts:

- (a) a complete contiguous physical tape of ≥ 97 letters — **SATISFIED** (CET, 97).
- (b) that tape attested for the 1988–89 target era — **NOT SATISFIED**.

**EXP-024 remains frozen, unrun and unmodified.** Its 22 procedures are untouched.
97 readable letters on a face of unresolved date is not Tier-1 satisfaction.

## The single highest-value next item

The blocker is no longer transcription. It is **dating one image**. Any one of these
unblocks Tier 1, in cost order:

1. **The akg-images / picture-alliance catalogue record for the Straube photograph**
   used by WELT (article 217168174, image 1920313707). The agency's own caption metadata
   carries a shoot date or range. One archive page, and it decides (b) outright.
2. Any **dated 1985–1996 photograph showing the CET/Berlin face legibly** — which would
   attest the target-era tape directly and make the Straube date irrelevant.
3. **Primary documentation of the 1985 maintenance change set** (maintenance ledger,
   works order, or contemporary 1985 press report) establishing whether 1985 *added* or
   *re-engraved* Athen/Kopenhagen/Wien/Rom.

Item 1 is the cheapest by a wide margin and is web-only. I am not working around it by
guessing the date.
