"""The Mengenlehreuhr (Berlin-Uhr, Europa-Center, Berlin).

Lamp layout, top to bottom:

    seconds   1 lamp   on for even seconds
    row 1     4 lamps  5 hours each
    row 2     4 lamps  1 hour each
    row 3    11 lamps  5 minutes each
    row 4     4 lamps  1 minute each

This is *not* the Urania Weltzeituhr (the 24-sector world clock) whose geometry
is already recorded as a negative result. The BERLINCLOCK crib at positions
63-73 names this clock, and its lamp count is a bounded, parameter-poor
function of the time of day, which makes it a keystream candidate that can be
falsified outright rather than merely scored.
"""

ROWS = (4, 4, 11, 4)
MAX_LIT = sum(ROWS)  # 23


def lamp_rows(minute_of_day):
    """(row1, row2, row3, row4) lit-lamp counts for a minute of the day."""
    h, m = divmod(minute_of_day % 1440, 60)
    return h // 5, h % 5, m // 5, m % 5


def lamps_lit(minute_of_day):
    """Total lit lamps excluding the seconds lamp. Range 0..23."""
    return sum(lamp_rows(minute_of_day))


def lamp_bits(minute_of_day):
    """The 23-lamp on/off vector, rows concatenated top to bottom."""
    r = lamp_rows(minute_of_day)
    return [1] * r[0] + [0] * (ROWS[0] - r[0]) + \
           [1] * r[1] + [0] * (ROWS[1] - r[1]) + \
           [1] * r[2] + [0] * (ROWS[2] - r[2]) + \
           [1] * r[3] + [0] * (ROWS[3] - r[3])


def lit_table():
    return [lamps_lit(m) for m in range(1440)]


READOUTS = {
    # name: (function(minute, i) -> int, inclusive value range)
    "lamps_lit":      (lambda m, i, T: T[m], (0, 23)),
    "lamps_lit_sec":  (lambda m, i, T: T[m] + (i % 2), (0, 24)),
    "minutes_mod26":  (lambda m, i, T: m % 26, (0, 25)),  # control
}
