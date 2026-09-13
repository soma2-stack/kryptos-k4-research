"""Independent structural checks for the Checkpoint AJ dataset."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
d = json.loads((ROOT / "data" / "k4_physical_layout_checkpoint_AJ.json").read_text(encoding="utf-8"))
panel = json.loads((ROOT / "data" / "cipher_side_rows.json").read_text(encoding="utf-8"))

ct = d["canonical_linear_k4"]["text"]
assert len(ct) == 97
s = d["published_textual_layout"]["segments"]
assert [x["k4_start"] for x in s] == [0, 4, 35, 66]
assert [x["k4_end"] for x in s] == [4, 35, 66, 97]
assert [len(x["text"]) for x in s] == [4, 31, 31, 31]
assert "".join(x["text"] for x in s) == ct
assert panel["rows"]["25"] == "ECDMRIPFEIMEHNLSSTTRTVDOHW?OBKR"
assert panel["rows"]["25"][-5:] == "?OBKR"
assert panel["rows"]["26"].startswith("UOX")
assert panel["rows"]["27"].startswith("TWT")
assert panel["rows"]["28"].startswith("VTT")

cribs = {x["plaintext"]: x for x in d["crib_spans"]}
assert cribs["EASTNORTHEAST"]["published_row_groups"] == [
    {"panel_row": 26, "column_start": 17, "column_end_inclusive": 29, "k4_start": 21, "k4_end_exclusive": 34}
]
assert cribs["BERLINCLOCK"]["published_row_groups"] == [
    {"panel_row": 27, "column_start": 28, "column_end_inclusive": 30, "k4_start": 63, "k4_end_exclusive": 66},
    {"panel_row": 28, "column_start": 0, "column_end_inclusive": 7, "k4_start": 66, "k4_end_exclusive": 74},
]
assert d["physical_engraving"]["exact_k4_row_count"] is None
assert d["physical_engraving"]["exact_row_lengths"] is None
assert d["physical_engraving"]["fixed_column_lattice"] == "NOT ESTABLISHED"
assert d["spacing_anomalies"]["verified"] == []
assert d["cipher_gate"]["exp040_justified"] is False
print("PASS: canonical/textual mapping exact; physical unknowns preserved; no route, spacing key, or cipher experiment introduced")
