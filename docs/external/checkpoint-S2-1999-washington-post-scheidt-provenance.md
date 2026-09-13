# Checkpoint S2 provenance repair — 1999 Washington Post Scheidt quotation

Date: 2026-09-12
Branch: `claude/k4-post-j`

## Source

John Schwartz, *Sculpture's Code Tests Mettle of Cryptographers*, **The Washington Post**, 19 July 1999.

Public archive URL:

`https://www.washingtonpost.com/archive/politics/1999/07/19/sculptures-code-tests-mettle-of-cryptographers/29ed7e9b-bd9b-48c2-9e8f-c13d75fd538e/`

This note repairs the provenance gap identified at Checkpoint S2. The quotation had appeared in an incoming audit note without an independent repository source record.

## Verified statements

The Washington Post article directly attributes the following points to Ed Scheidt:

1. He could use encryption methods with a **historic basis** because doing so would not compromise then-current government cryptographic methods.
2. He and Sanborn wanted to make something that could **eventually be deciphered or extracted**, rather than something that would never be solved.
3. Scheidt is described as having spent roughly four months devising the systems Sanborn would use.
4. The article says Sanborn then encrypted the chosen message himself once the code system was in hand.

## Evidence grade

**B+ documentary evidence** for the attributed Scheidt statements:

- contemporaneous mainstream reporting from 1999;
- direct quotations attributed to Scheidt;
- not a primary audio transcript, so below an original recording or contemporaneous interview master.

## Cryptanalytic consequence

This source materially narrows one interpretive question without naming a K4 transform.

The phrase **historic basis** argues against reading the 1990-era `modern / contemporary` language as evidence for an unexplained then-modern government primitive. A better synthesis is:

> Scheidt could draw on historically grounded cryptographic methods, adapt them to the sculpture, and do so without exposing current classified practice.

That strengthens the **adapted / historically grounded** interpretation and slightly raises the prior on a modified classical construction relative to a genuinely novel modern primitive.

It still does **not** identify:

- transposition versus substitution;
- a particular tableau or alphabet;
- running key versus periodic key;
- fractionation;
- a key schedule;
- a composition order;
- a key source;
- any exact K4 equation.

Therefore it does **not** repair EXP-040 gate conditions 2 or 3. No EXP-040 is justified from this source.

## Relation to Checkpoint S2

Checkpoint S2 said the quotation must not be relied on until independently sourced. That provenance gap is now **closed**.

The S2 conclusion otherwise stands:

- `custom / adapted` remains strongly supported;
- `historic basis` now gives that adaptation a better historical/classical anchor;
- no specific bounded architecture is selected;
- Request 2 (unedited 2005 Zetter/Scheidt material) remains the primary evidence target;
- original/full 1991 ABC interview audio/video remains secondary.

K4 remains unsolved.
