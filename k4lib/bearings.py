"""Compass-bearing routes over a grid.

Motivation, not decoration: `EASTNORTHEAST` is a compass bearing, the Kryptos
courtyard contains a compass rose, and Sanborn confirmed in November 2025 that
`BERLINCLOCK` is the Weltzeituhr, which stands on a compass-rose mosaic. Both
confirmed cribs therefore point at the same object: a rose of directions.

The natural operation an artist performs with a bearing and a grid of letters is
to read the grid along that bearing. On a lattice a 16-point rose becomes sixteen
integer step vectors, given below as (dcol, drow) with row increasing southward.
ENE - the bearing named by the crib - is two east for one north.

A route steps repeatedly by (dcol, drow) on the torus, collecting unvisited cells;
when an orbit closes it resumes at the next unvisited cell in reading order. That
always yields a full permutation, for any grid and any step.
"""

ROSE_16 = {
    "N":   (0, -1),  "NNE": (1, -2),  "NE":  (1, -1),  "ENE": (2, -1),
    "E":   (1, 0),   "ESE": (2, 1),   "SE":  (1, 1),   "SSE": (1, 2),
    "S":   (0, 1),   "SSW": (-1, 2),  "SW":  (-1, 1),  "WSW": (-2, 1),
    "W":   (-1, 0),  "WNW": (-2, -1), "NW":  (-1, -1), "NNW": (-1, -2),
}


def bearing_route(w, h, dcol, drow, start=0, ncells=None):
    """Cell visiting order for a w x h torus stepping by (dcol, drow).

    Returns a list of cell indices (row-major) of length w*h, or the first
    `ncells` of it. Always a permutation of the cells it covers.
    """
    total = w * h
    seen = [False] * total
    order = []
    nxt = start % total
    while len(order) < total:
        if seen[nxt]:
            nxt = next((c for c in range(total) if not seen[c]), None)
            if nxt is None:
                break
        r, c = divmod(nxt, w)
        while not seen[r * w + c]:
            seen[r * w + c] = True
            order.append(r * w + c)
            c = (c + dcol) % w
            r = (r + drow) % h
        nxt = 0
    return order[:ncells] if ncells else order


def grid_permutation(w, h, name, start, nletters=97, blank_last=True):
    """A permutation of 0..nletters-1 induced by a bearing route over a w x h grid.

    Letters are laid into the grid in reading order; a grid with more cells than
    letters leaves the surplus blank at the end (matching the reported K4 layout,
    which is 7 x 14 with one blank in the final row). Cells beyond the letter count
    are skipped by the route rather than renumbering it.
    """
    dcol, drow = ROSE_16[name]
    order = bearing_route(w, h, dcol, drow, start)
    kept = [c for c in order if c < nletters] if blank_last else order
    return kept if len(kept) == nletters else None
