"""Checkpoint AJ: build the K4 representation and physical-evidence map.

No image coordinates are fitted and no cipher transform is tested.  Physical
unknowns stay null rather than being copied from the CIA textual rendering.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
K4 = json.loads((ROOT / "data" / "k4.json").read_text(encoding="utf-8"))
PANEL = json.loads((ROOT / "data" / "cipher_side_rows.json").read_text(encoding="utf-8"))
OUT = ROOT / "data" / "k4_physical_layout_checkpoint_AJ.json"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def main() -> None:
    ct = K4["ciphertext"]
    published = [
        {"k4_start": 0, "k4_end": 4, "panel_row": 25, "panel_col_start": 27, "text": PANEL["rows"]["25"][-4:]},
        {"k4_start": 4, "k4_end": 35, "panel_row": 26, "panel_col_start": 0, "text": PANEL["rows"]["26"]},
        {"k4_start": 35, "k4_end": 66, "panel_row": 27, "panel_col_start": 0, "text": PANEL["rows"]["27"]},
        {"k4_start": 66, "k4_end": 97, "panel_row": 28, "panel_col_start": 0, "text": PANEL["rows"]["28"]},
    ]
    assert "".join(x["text"] for x in published) == ct

    by_position = []
    for i, symbol in enumerate(ct):
        seg = next(s for s in published if s["k4_start"] <= i < s["k4_end"])
        panel_col = seg["panel_col_start"] + i - seg["k4_start"]
        by_position.append(
            {
                "k4_index_zero_based": i,
                "symbol": symbol,
                "published_panel_row_one_based": seg["panel_row"],
                "published_row_column_zero_based": panel_col,
                "physical_character_center": None,
                "physical_confidence": "UNKNOWN",
            }
        )

    crib_spans = []
    for crib in K4["confirmed_cribs"]:
        positions = by_position[crib["start"] : crib["end"]]
        groups = []
        for p in positions:
            key = (p["published_panel_row_one_based"],)
            if not groups or groups[-1]["panel_row"] != key[0]:
                groups.append(
                    {
                        "panel_row": key[0],
                        "column_start": p["published_row_column_zero_based"],
                        "column_end_inclusive": p["published_row_column_zero_based"],
                        "k4_start": p["k4_index_zero_based"],
                        "k4_end_exclusive": p["k4_index_zero_based"] + 1,
                    }
                )
            else:
                groups[-1]["column_end_inclusive"] = p["published_row_column_zero_based"]
                groups[-1]["k4_end_exclusive"] = p["k4_index_zero_based"] + 1
        crib_spans.append(
            {
                "plaintext": crib["plaintext"],
                "k4_interval": [crib["start"], crib["end"]],
                "ciphertext": crib["ciphertext_segment"],
                "published_row_groups": groups,
                "physical_spacing_relation": "UNKNOWN",
            }
        )

    sources = [
        {
            "id": "LOC_HIGHSM_13337",
            "authority": "Library of Congress, Carol M. Highsmith Archive",
            "identifier": "LC-DIG-highsm-13337 / LC-HS503-2081",
            "photographer": "Carol M. Highsmith",
            "date": "between 1980 and 2006",
            "native_resolution": [3384, 4283],
            "master_available": True,
            "master_sha256": "302fb88dee8db7f484a85d9d7f9bbd39f69de37cbf7bb25ae5a2e35bf8b8cf52",
            "camera_angle": "oblique interior/back view across curved screen",
            "visible_k4_rows": ["row 25 starts ECDM", "row 26 starts UOX", "row 27 starts TWT", "row 28 starts VTT"],
            "full_row_starts_visible": True,
            "full_row_ends_visible": False,
            "measurement_suitability": "row identity HIGH; exact count/pitch/terminal geometry UNSUITABLE",
        },
        {
            "id": "CIA_UPWARD_980",
            "authority": "Central Intelligence Agency",
            "identifier": "kryptos_sculpture_lg.jpg",
            "photographer": None,
            "date": None,
            "native_resolution": [980, 1305],
            "master_available": False,
            "sha256": "31013cb7c25557174afb228879c654c81b192867661b7c0f477cb31d9c02420a",
            "camera_angle": "extreme upward oblique detail",
            "visible_k4_rows": [],
            "full_row_starts_visible": False,
            "full_row_ends_visible": False,
            "measurement_suitability": "unsuitable for K4 row geometry",
        },
        {
            "id": "GSA_36111",
            "authority": "U.S. General Services Administration Fine Arts Collection",
            "identifier": "media 36111; artwork 23717",
            "photographer": "Jim Sanborn (page credit)",
            "date": None,
            "native_resolution": [500, 330],
            "master_available": "UNKNOWN",
            "sha256": "59b6367a8fa3fd1fdc71c2e965a5afda1da73f0e9632ef0887e9451a9cee3913",
            "camera_angle": "front/context view of full screen",
            "visible_k4_rows": ["present but below cell-reading resolution"],
            "full_row_starts_visible": "geometrically yes; not textually legible",
            "full_row_ends_visible": "geometrically yes; not textually legible",
            "measurement_suitability": "context only; unsuitable for character centers or counts",
        },
        {
            "id": "GSA_36112",
            "authority": "U.S. General Services Administration Fine Arts Collection",
            "identifier": "media 36112; artwork 23717",
            "photographer": "Jim Sanborn (page credit)",
            "date": None,
            "native_resolution": [500, 336],
            "master_available": "UNKNOWN",
            "sha256": "70d76617f3bb696a470af40cb63c2ff0a4706ef35ac0727ec16372893a04b7db",
            "camera_angle": "wide courtyard context",
            "visible_k4_rows": [],
            "full_row_starts_visible": False,
            "full_row_ends_visible": False,
            "measurement_suitability": "unsuitable",
        },
    ]

    result = {
        "checkpoint": "AJ",
        "date": "2026-09-13",
        "scope": "physical-layout audit only; no cipher search",
        "canonical_linear_k4": {"text": ct, "length": len(ct), "sha256": sha256_text(ct)},
        "published_textual_layout": {
            "authority": PANEL["provenance"]["primary"],
            "segments": published,
            "segment_lengths": [s["k4_end"] - s["k4_start"] for s in published],
            "status": "verified textual mapping; not a metric survey",
        },
        "physical_engraving": {
            "exact_k4_row_count": None,
            "minimum_directly_identified_contiguous_rows": 3,
            "directly_identified_row_starts": ["UOX", "TWT", "VTT"],
            "row_25_start_ECDM_visible": True,
            "row_25_terminal_OBKR_visible": False,
            "obkr_separate_row": False,
            "obkr_separate_row_basis": "institutional text places it after ? on row 25; photograph shows no extra row between ECDM and UOX",
            "exact_row_lengths": None,
            "fixed_column_lattice": "NOT ESTABLISHED",
            "quantitative_coordinates": None,
            "reason": "no admitted orthographic image shows both ends of the K4-bearing rows; curvature invalidates one global planar homography",
            "verified_features": [
                "horizontal baselines",
                "curved cut-through copper screen",
                "three consecutive physical rows beginning UOX, TWT, VTT",
                "preceding physical row begins ECDM",
            ],
            "unknown_features": [
                "physical visibility and placement of row-25 terminal OBKR",
                "physical character counts of rows 25-28",
                "row left/right x coordinates and widths",
                "character centers, pitch, gap distribution and kerning outliers",
                "shared vertical columns or systematic stagger",
            ],
        },
        "crib_spans": crib_spans,
        "images": sources,
        "spacing_anomalies": {
            "verified": [],
            "status": "NONE ESTABLISHED; not equivalent to proof of uniform spacing",
            "multiplicity_note": "no 96-gap scan was performed because defensible coordinates are unavailable",
        },
        "glyph_features": {
            "cut_through": "VERIFIED",
            "stencil_bridges": "visible and structurally expected for cut-through metal",
            "intentional_marks": [],
            "damage_or_restoration_at_k4": "UNKNOWN",
        },
        "cipher_gate": {
            "new_finite_parameter": False,
            "row_break_selects_reset": False,
            "prior_coverage": ["EXP-020", "EXP-032", "Checkpoint T", "Checkpoint AH"],
            "exp040_justified": False,
            "k4_status": "UNSOLVED",
        },
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "canonical_length": len(ct),
        "published_segments": result["published_textual_layout"]["segment_lengths"],
        "physical_exact_row_count": result["physical_engraving"]["exact_k4_row_count"],
        "new_finite_parameter": result["cipher_gate"]["new_finite_parameter"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
