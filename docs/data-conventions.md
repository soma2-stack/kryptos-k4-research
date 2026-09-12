# Data conventions

## Fixed inputs

`data/k4.json` is the single source of truth for the 97-character ciphertext and crib coordinate convention.

All code and notes must say whether an index is zero- or one-based. This repository uses **zero-based, half-open** spans: `start=21, end=34` means ciphertext indices 21 through 33.

## Evaluation gate

Every proposed mechanism must provide:

1. The complete input text and normalization rules.
2. All parameters, including geometry, route direction, offsets, alphabet order, and encryption/decryption convention.
3. Exact output at both crib spans.
4. A falsifiable account of the remaining 73 characters.
5. A saved result record sufficient for a second researcher to reproduce it.

Crib-only fitting is not evidence of a solution. A flexible homophonic mapping can generate apparent English while merely absorbing the known constraints.
