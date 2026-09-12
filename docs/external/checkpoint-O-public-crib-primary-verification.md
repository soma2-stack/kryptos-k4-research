# External evidence handoff: public K4 crib positions verified

Date: 2026-09-12
Branch context before this handoff: `claude/k4-post-j` at `235fcaf5a06f7eb6323214dd53c353e8ee14ec4e`.

Purpose: resolve Checkpoint O's highest-priority evidence request: whether the public K4 clues are merely words known to occur somewhere in the plaintext, or whether they are tied to exact local plaintext/ciphertext positions. No alleged full K4 plaintext, purported solution, or private K5 material is used.

## Conclusion

The repository's 24 position-preserving crib constraints are supported by the public record.

- **BERLIN** is explicitly tied to K4 positions **64-69 (one-based)**: contemporaneous New York Times reporting says the 64th through 69th characters of the final panel, **when deciphered**, spell BERLIN.
- **CLOCK** is explicitly tied to positions **70-74 (one-based)**: the same New York Times report says Sanborn supplied five additional letters in the 70th through 74th positions and that they spell CLOCK; it immediately states that positions 64-74 therefore spell BERLIN CLOCK.
- **NORTHEAST** is explicitly tied to positions **26-34 (one-based)**: the January 2020 New York Times article, preserved through an NYT News Service republication, calls Sanborn's disclosures "cribs" and states that the new word NORTHEAST is at positions 26 through 34.
- **EAST** was released differently: Sanborn supplied a layout privately to several people in 2020, and New York Times reporter John Schwartz publicly confirmed that EAST "goes just before" the already-positioned NORTHEAST. Contemporaneous reporting records the four letters at positions 22-25, ciphertext FLRV, as EAST. This evidence chain is slightly weaker than the full NYT articles for BERLIN/CLOCK/NORTHEAST, but it still fixes EAST immediately before NORTHEAST and therefore supports the combined one-based span 22-34 = EASTNORTHEAST.

Thus the working zero-based half-open repository spans remain:

```text
EASTNORTHEAST  [21,34)  ciphertext FLRVQQPRNGKSS
BERLINCLOCK     [63,74)  ciphertext NYPVTTMZFPK
```

These are not merely occurrence constraints. They are local plaintext/ciphertext positional anchors.

## Evidence

### BERLIN and CLOCK — contemporaneous New York Times article

John Schwartz, *Sculptor Offers Another Clue in 24-Year-Old Mystery at C.I.A.*, The New York Times, 20 Nov 2014. Archived capture:

https://web.archive.org/web/20240224133656/https://www.nytimes.com/2014/11/21/us/another-kryptos-clue-is-offered-in-a-24-year-old-mystery-at-the-cia.html

Relevant text in the archived article:

- the fourth/final passage is 97 characters;
- "The 64th through 69th characters of the final panel, when deciphered, spelled out the word BERLIN";
- Sanborn then supplied "five additional letters, those in the 70th through 74th position";
- "They spell 'clock'";
- "This means that the letters from positions 64 to 74 spell out two words: 'Berlin clock.'"

Grade: **A/B boundary** for the positional disclosure: contemporaneous direct reporting based on Sanborn's clue, with direct quotation from Sanborn elsewhere in the same article. It is not an original Sanborn manuscript, but it is the publication through which he released the clue.

### NORTHEAST — 2020 New York Times report / NYT News Service republication

John Schwartz and Jonathan Corum, *This Sculpture Holds a Decades-Old C.I.A. Mystery. And Now, Another Clue.*, The New York Times, 29 Jan 2020. Original URL:

https://www.nytimes.com/interactive/2020/01/29/climate/kryptos-sculpture-final-clue.html

The article is preserved in an NYT News Service republication at:

https://artdaily.com/news/120517/Another-clue-for-a-CIA-sculpture-that-holds-a-decades-old-mystery

The republication identifies Sanborn's prior disclosures as "cribs" and states:

- BERLIN is in the 64th through 69th positions;
- CLOCK is in the next five, 70 through 74;
- "the word NORTHEAST" is "at positions 26 through 34."

The republication carries `© 2020 The New York Times Company` and bylines John Schwartz and Jonathan Corum.

Grade: **A/B boundary** for the position claim: contemporaneous NYT reporting, preserved as an NYT News Service republication.

### NORTHEAST — direct Sanborn NPR interview corroboration

NPR / All Things Considered, Mary Louise Kelly interview with Jim Sanborn, 30 Jan 2020. Public transcript mirrors include:

https://www.northcountrypublicradio.org/news/npr/801323608/a-new-and-final-clue-to-kryptos-a-long-standing-puzzle

https://www.capradio.org/news/npr/story?storyid=801323608

Sanborn says directly: "The new clue is the word northeast." He also confirms BERLIN and CLOCK as his previous two clues. The audio transcript itself does not supply the numeric 26-34 placement, so it corroborates the plaintext word and provenance while the NYT report supplies the exact positions.

Grade: **A** for Sanborn's authorship of the NORTHEAST clue; **not independently sufficient for numeric placement**.

### EAST — direct reporter confirmation of Sanborn's private release

New York Times reporter John Schwartz, 24 Aug 2020, public tweet (archived/cited widely):

`KRYPTOS NEWS: Jim Sanborn, creator of the Kryptos sculpture, quietly released four new plaintext letters to the unsolved portion, K4. EAST, which goes just before the recently released NORTHEAST.`

Original tweet citation:

https://twitter.com/jswatz/status/1297658577914667008

Contemporaneous follow-up reporting records Sanborn's own explanation that he had released the layout to several people as early as April 2020. A preserved account quoting Schwartz's exchange with Sanborn is:

https://inteltoday.org/2021/02/06/one-year-ago-kryptos-sculpture-jim-sanborn-this-is-the-third-and-to-be-sure-final-clue-update-and-then-came-a-4th-clue/

That account explicitly records:

- positions 22-25, ciphertext `FLRV`, as plaintext EAST;
- positions 26-34, ciphertext `QQPRNGKSS`, as NORTHEAST;
- Sanborn explaining that he intentionally released the layout to several people.

Because NORTHEAST is independently fixed at one-based 26-34 and Schwartz says the four-letter EAST goes immediately before it, EAST occupies one-based 22-25.

Grade: **B+**. The clue is directly attributed to Sanborn and publicly confirmed by the NYT reporter who checked with him, but unlike BERLIN/CLOCK/NORTHEAST the numeric placement was not found here in a full contemporaneous NYT article accessible during this audit.

## Consequence for K4 model semantics

The public clues support a **local position-preserving plaintext/ciphertext correspondence** at the disclosed spans. Therefore a proposed cipher architecture cannot evade the 24 crib constraints merely by saying the clue words occur elsewhere in a variable-length decoding.

A non-position-preserving / length-changing architecture must explain how it nevertheless satisfies these explicitly numbered plaintext anchors. It cannot simply slide BERLIN, CLOCK, NORTHEAST, or EAST to different plaintext positions after seeing a result.

### Checkpoint-O Fractionated Morse implication

This upgrades Checkpoint O's conditional statement. Under standard Fractionated Morse, six ciphertext letters represent 18 ternary Morse/separator symbols, while plaintext BERLIN needs at least 21 symbols internally; five ciphertext letters represent 15 symbols while CLOCK needs at least 22. Because BERLIN and CLOCK are explicitly tied to the corresponding numbered K4 positions, the standard length-changing Fractionated-Morse model is structurally incompatible with the public clue semantics. The rejection no longer rests merely on the repository's inherited working convention.

Scope remains narrow: this does **not** eliminate every imaginable Morse-derived or variable-length system. It eliminates standard Fractionated Morse as a model that must honor the published positional cribs.

## Repository indexing

The public reports use one-based human positions. `data/k4.json` uses zero-based half-open ranges. The conversion is:

```text
public 22-34  -> repo [21,34)  EASTNORTHEAST
public 64-74  -> repo [63,74)  BERLINCLOCK
```

No ciphertext, crib text, or index was changed by this evidence handoff. The handoff only resolves the provenance/status of the existing constraints.
