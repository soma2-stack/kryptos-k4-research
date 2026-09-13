"""Checkpoint AI: deterministic ideal/CIA tableau comparison.

This is an artifact-transcription audit, not a cipher experiment.  It deliberately
does not infer unreadable photograph cells from the generated tableau or CIA text.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "tableau_checkpoint_AI.json"

STD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KRY = "KRYPTOSABCDEFGHIJLMNQUVWXZ"

# Verbatim line strings from the CIA institutional "Panel 2 - Cipher (Text Version)".
CIA_ROWS = [
    "ABCDEFGHIJKLMNOPQRSTUVWXYZABCD",
    "AKRYPTOSABCDEFGHIJLMNQUVWXZKRYP",
    "BRYPTOSABCDEFGHIJLMNQUVWXZKRYPT",
    "CYPTOSABCDEFGHIJLMNQUVWXZKRYPTO",
    "DPTOSABCDEFGHIJLMNQUVWXZKRYPTOS",
    "ETOSABCDEFGHIJLMNQUVWXZKRYPTOSA",
    "FOSABCDEFGHIJLMNQUVWXZKRYPTOSAB",
    "GSABCDEFGHIJLMNQUVWXZKRYPTOSABC",
    "HABCDEFGHIJLMNQUVWXZKRYPTOSABCD",
    "IBCDEFGHIJLMNQUVWXZKRYPTOSABCDE",
    "JCDEFGHIJLMNQUVWXZKRYPTOSABCDEF",
    "KDEFGHIJLMNQUVWXZKRYPTOSABCDEFG",
    "LEFGHIJLMNQUVWXZKRYPTOSABCDEFGH",
    "MFGHIJLMNQUVWXZKRYPTOSABCDEFGHI",
    "NGHIJLMNQUVWXZKRYPTOSABCDEFGHIJL",
    "OHIJLMNQUVWXZKRYPTOSABCDEFGHIJL",
    "PIJLMNQUVWXZKRYPTOSABCDEFGHIJLM",
    "QJLMNQUVWXZKRYPTOSABCDEFGHIJLMN",
    "RLMNQUVWXZKRYPTOSABCDEFGHIJLMNQ",
    "SMNQUVWXZKRYPTOSABCDEFGHIJLMNQU",
    "TNQUVWXZKRYPTOSABCDEFGHIJLMNQUV",
    "UQUVWXZKRYPTOSABCDEFGHIJLMNQUVW",
    "VUVWXZKRYPTOSABCDEFGHIJLMNQUVWX",
    "WVWXZKRYPTOSABCDEFGHIJLMNQUVWXZ",
    "XWXZKRYPTOSABCDEFGHIJLMNQUVWXZK",
    "YXZKRYPTOSABCDEFGHIJLMNQUVWXZKR",
    "ZZKRYPTOSABCDEFGHIJLMNQUVWXZKRY",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZABCD",
]


def ideal_rows() -> list[str]:
    rows = [STD + STD[:4]]
    for r, label in enumerate(STD):
        rotated = KRY[r:] + KRY[:r]
        rows.append(label + rotated + rotated[:4])
    rows.append(STD + STD[:4])
    return rows


def main() -> None:
    ideal = ideal_rows()
    differences = []
    rows = []
    for row_index, (expected, official) in enumerate(zip(ideal, CIA_ROWS)):
        width = max(len(expected), len(official))
        cells = []
        for col in range(width):
            e = expected[col] if col < len(expected) else None
            o = official[col] if col < len(official) else None
            status = "MATCH" if e == o else "DIFFERENCE"
            # Neither admitted installed-sculpture photograph is an orthographic,
            # complete cell survey.  Preserve the photo field as unknown.
            cells.append(
                {
                    "column_zero_based": col,
                    "ideal_symbol": e,
                    "official_symbol": o,
                    "photograph_visible_symbol": None,
                    "photograph_confidence": "UNKNOWN",
                    "photograph_reading": "not independently addressable in admitted photographs",
                    "status": status,
                }
            )
            if status == "DIFFERENCE":
                differences.append(
                    {
                        "type": "extra_terminal" if e is None and o is not None else "uncertain",
                        "row_zero_based": row_index,
                        "row_role": "body_N" if row_index == 14 else "other",
                        "column_zero_based": col,
                        "expected": e,
                        "official": o,
                        "physical": None,
                        "source": "CIA textual artifact transcription",
                        "confidence": "VERIFIED_TEXTUAL_ONLY",
                        "cryptographic_consequence": "none uniquely specified",
                    }
                )
        rows.append(
            {
                "row_zero_based": row_index,
                "role": "top_header" if row_index == 0 else "bottom_header" if row_index == 27 else "body",
                "label": None if row_index in (0, 27) else STD[row_index - 1],
                "ideal": expected,
                "official": official,
                "ideal_length": len(expected),
                "official_length": len(official),
                "photo_row_confidence": "UNKNOWN",
                "cells": cells,
            }
        )

    payload = {
        "checkpoint": "AI",
        "date": "2026-09-13",
        "scope": "artifact measurement only; no cipher search",
        "ideal_tableau": {
            "alphabet": KRY,
            "alphabet_length": len(KRY),
            "header_alphabet": STD,
            "rows_total": 28,
            "body_rows": 26,
            "header_rows": 2,
            "generated_body_line_rule": "row label + left rotation of KRY + first four symbols of that rotation",
            "header_line_rule": "A-Z followed by A-D",
            "body_line_length": 31,
            "header_line_length": 30,
            "character_count": sum(map(len, ideal)),
        },
        "textual_artifact_transcription": {
            "authority": "Central Intelligence Agency",
            "url": "https://www.cia.gov/legacy/headquarters/kryptos-sculpture",
            "heading": "Panel 2 - Cipher ( Text Version )",
            "retrieved": "2026-09-13",
            "normalization": "none; line strings copied exactly as displayed",
            "character_count": sum(map(len, CIA_ROWS)),
        },
        "photographic_sources": [
            {
                "authority": "Library of Congress, Carol M. Highsmith Archive",
                "record": "LC-DIG-highsm-13337 / LC-HS503-2081",
                "url": "https://www.loc.gov/pictures/item/2011631531/",
                "master_url": "https://cdn.loc.gov/master/pnp/highsm/13300/13337u.tif",
                "master_sha256": "302fb88dee8db7f484a85d9d7f9bbd39f69de37cbf7bb25ae5a2e35bf8b8cf52",
                "dimensions": [3384, 4283],
                "assessment": "installed original; oblique curved view; not a complete orthographic cell survey",
            },
            {
                "authority": "Central Intelligence Agency",
                "url": "https://www.cia.gov/static/bc5188e5768e6c394ec8dff5f1083da0/1949f/kryptos_sculpture_lg.jpg",
                "sha256": "31013cb7c25557174afb228879c654c81b192867661b7c0f477cb31d9c02420a",
                "dimensions": [980, 1305],
                "assessment": "close oblique detail; does not expose a complete tableau terminal edge",
            },
        ],
        "physical_artifact": {
            "independently_verified_character_count": None,
            "reason": "no admitted photograph provides a complete, orthographic, cell-addressable tableau",
            "geometry_verified": [
                "horizontal row organization",
                "curved copper surface",
                "perspective-dependent apparent spacing",
            ],
            "geometry_not_verified": [
                "uniform fixed-width columns",
                "common vertical lattice across all rows",
                "terminal-L spacing or physical presence",
                "any fixed HILL vertical or diagonal alignment",
            ],
        },
        "rows": rows,
        "differences": differences,
        "counts": {
            "ideal": sum(map(len, ideal)),
            "official_textual": sum(map(len, CIA_ROWS)),
            "official_minus_ideal": sum(map(len, CIA_ROWS)) - sum(map(len, ideal)),
            "verified_physical": None,
            "textual_extras": sum(1 for d in differences if d["expected"] is None and d["official"] is not None),
            "textual_omissions": sum(1 for d in differences if d["expected"] is not None and d["official"] is None),
            "textual_substitutions": sum(1 for d in differences if d["expected"] is not None and d["official"] is not None),
        },
        "extra_terminal_L": {
            "official_text_contains": True,
            "row_zero_based": 14,
            "body_row_zero_based": 13,
            "row_label": "N",
            "full_line_column_zero_based": 31,
            "body_column_zero_based": 30,
            "inside_regular_line": False,
            "physical_presence": "UNKNOWN",
            "physical_spacing": "UNKNOWN",
            "adjacent_official_row_lengths": {"M": 31, "N": 32, "O": 31},
            "meaning_HILL": "NOT FORCED",
        },
        "decision": {
            "previously_unmodeled_finite_rule": False,
            "exp040_justified": False,
            "k4_status": "UNSOLVED",
        },
    }
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload["counts"], sort_keys=True))


if __name__ == "__main__":
    main()
