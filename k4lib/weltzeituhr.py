"""Physically meaningful readings of the Weltzeituhr as an object.

The clock is represented as 24 sectors, each with an UPPER and a LOWER band of
place names, matching the three-part cylinder: names on the upper aluminium disk,
the rotating hour ring between, names on the lower disk.

    clock = {"sectors": [{"upper": [...], "lower": [...]}, ... 24 of them],
             "utc_offset": [...]}          # optional, sector -> UTC offset

These reading procedures are PREREGISTERED while the real name list is still
unavailable (see data/weltzeituhr.json). That is the cleanest possible
preregistration: they cannot have been tuned to data that does not exist here.
Each is motivated by the object, not by a crib score:

  * a person walks around a cylinder, so readings are clockwise or anticlockwise;
  * names sit in two bands, so a reader takes upper-then-lower, lower-then-upper,
    or alternates;
  * a reader may circle the whole upper band first, then the whole lower;
  * a Berlin visitor naturally starts at the Berlin sector;
  * the object is also indexed by time zone, so reading in UTC order is natural;
  * a compass rose sits underneath, so a bearing could choose the start sector -
    but that needs the cylinder's orientation, which is UNKNOWN.
"""

import re

BANDS = ("upper", "lower")


def normalise(name):
    """Letters only, uppercase - the form a hand-copied tape would take."""
    return re.sub(r"[^A-Z]", "", name.upper())


def _sector_letters(sector, band_order):
    out = []
    for b in band_order:
        for nm in sector.get(b, []):
            out.append(normalise(nm))
    return "".join(out)


def read(clock, *, direction=1, start=0, band_order=("upper", "lower"),
         whole_band_first=False, by_utc=False):
    """Return the letter tape produced by one reading procedure."""
    sectors = clock["sectors"]
    n = len(sectors)
    if by_utc and "utc_offset" in clock:
        order = sorted(range(n), key=lambda i: clock["utc_offset"][i])
    else:
        order = [(start + direction * k) % n for k in range(n)]
    if whole_band_first:
        parts = []
        for b in band_order:
            for i in order:
                parts.append(_sector_letters(sectors[i], (b,)))
        return "".join(parts)
    return "".join(_sector_letters(sectors[i], band_order) for i in order)


def alternating(clock, *, direction=1, start=0, first="upper"):
    """Alternate bands sector by sector: upper, lower, upper, ..."""
    sectors = clock["sectors"]
    n = len(sectors)
    out = []
    for k in range(n):
        i = (start + direction * k) % n
        b = first if k % 2 == 0 else ("lower" if first == "upper" else "upper")
        out.append(_sector_letters(sectors[i], (b,)))
    return "".join(out)


def procedures(clock, berlin_sector=None):
    """All preregistered readings. Returns {label: tape}."""
    out = {}
    for direction, dname in ((1, "cw"), (-1, "ccw")):
        for band_order in (("upper", "lower"), ("lower", "upper")):
            bo = band_order[0][0] + band_order[1][0]
            out[f"{dname}/start0/{bo}"] = read(clock, direction=direction,
                                               start=0, band_order=band_order)
            out[f"{dname}/start0/{bo}/wholeband"] = read(
                clock, direction=direction, start=0,
                band_order=band_order, whole_band_first=True)
            if berlin_sector is not None:
                out[f"{dname}/berlin/{bo}"] = read(clock, direction=direction,
                                                   start=berlin_sector,
                                                   band_order=band_order)
        for first in ("upper", "lower"):
            out[f"{dname}/start0/alt-{first}"] = alternating(
                clock, direction=direction, start=0, first=first)
            if berlin_sector is not None:
                out[f"{dname}/berlin/alt-{first}"] = alternating(
                    clock, direction=direction, start=berlin_sector, first=first)
    if "utc_offset" in clock:
        for band_order in (("upper", "lower"), ("lower", "upper")):
            bo = band_order[0][0] + band_order[1][0]
            out[f"utc-order/{bo}"] = read(clock, band_order=band_order, by_utc=True)
    return out


def synthetic_clock(seed=0, names_per_band=3):
    """A structurally faithful FAKE clock, for validating the code only.

    It has the right shape - 24 sectors, two bands - and deliberately fake names,
    so the reading machinery can be tested without inventing historical data.
    """
    import random
    rng = random.Random(seed)
    syll = ["BER", "LIN", "MOS", "KAU", "TOK", "YO", "LIM", "CAI", "RO", "OSL",
            "DEL", "HI", "PEK", "ING", "RIO", "NAI", "BI", "PER", "TH", "SYD"]
    sectors = []
    for _ in range(24):
        s = {}
        for b in BANDS:
            s[b] = ["".join(rng.choice(syll) for _ in range(2))
                    for _ in range(rng.randint(1, names_per_band))]
        sectors.append(s)
    return {"sectors": sectors, "utc_offset": [((i + 12) % 24) - 11 for i in range(24)]}
