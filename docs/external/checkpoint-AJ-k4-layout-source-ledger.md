# Checkpoint AJ source ledger — K4 ciphertext-side layout

Date: 2026-09-13

Scope: institutional/public artifact imagery and existing repository evidence only. No
solution-focused site, alleged plaintext, private K5 material, auction-secret material, or
post-hoc geometric extraction was used.

## Image inventory

| Rank | Source / identifier | Photographer / date | Native file inspected | Angle and K4 visibility | Row starts / ends | Measurement suitability |
|---:|---|---|---|---|---|---|
| 1 | Library of Congress, Carol M. Highsmith Archive, `LC-DIG-highsm-13337`, `LC-HS503-2081` | Carol M. Highsmith; catalog date `[between 1980 and 2006]` | 3384×4283 master derivative, SHA-256 `302fb88dee8db7f484a85d9d7f9bbd39f69de37cbf7bb25ae5a2e35bf8b8cf52` | Oblique interior/back view across curved screen. Physical rows starting `ECDM`, `UOX`, `TWT`, `VTT` are legible after a horizontal mirror for reading only | starts visible; terminal ends outside/foreshortened | HIGH for row identity and adjacency; unsuitable for exact counts, pitch, gap size, or terminal geometry |
| 2 | CIA `kryptos_sculpture_lg.jpg` | not stated; not stated | 980×1305 JPEG, SHA-256 `31013cb7c25557174afb228879c654c81b192867661b7c0f477cb31d9c02420a` | Extreme upward oblique detail | neither complete K4 start nor end set | unsuitable for K4 geometry |
| 3 | GSA Fine Arts Collection, artwork 23717, media 36111 | page credits Jim Sanborn; date not stated | 500×330 JPEG preview, SHA-256 `59b6367a8fa3fd1fdc71c2e965a5afda1da73f0e9632ef0887e9451a9cee3913` | Front/context view of full screen | edges geometrically present but letters below reliable reading resolution | context only; no center coordinates or exact counts |
| 4 | GSA Fine Arts Collection, artwork 23717, media 36112 | page credits Jim Sanborn; date not stated | 500×336 JPEG preview, SHA-256 `70d76617f3bb696a470af40cb63c2ff0a4706ef35ac0727ec16372893a04b7db` | Wide courtyard context | no usable K4 rows | unsuitable |

Institutional records:

- LOC: <https://www.loc.gov/pictures/item/2011631531/>
- LOC inspected master derivative:
  <https://cdn.loc.gov/master/pnp/highsm/13300/13337u.tif>
- CIA artifact page and textual panels:
  <https://www.cia.gov/legacy/headquarters/kryptos-sculpture>
- GSA artwork record: <https://art.gsa.gov/objects/23717/kryptos>

The CIA `Kryptos Encoded Text` PNG is a graphic rendering of the institutional text version,
not an independent photograph. It is evidence for **published textual layout**, not physical
x-coordinates.

## Narrow image handling

For visual reading, the LOC master was cropped to the ciphertext-bearing lower area and mirrored
horizontally because the cut-through text is viewed from the reverse. Mirroring changes only
read direction; no planar or curved-surface rectification was applied. No coordinates were
measured from the crop.

A single global homography would be physically inappropriate: the copper visibly curves, depth
changes continuously across the rows, and the far ends are foreshortened or outside the frame.
There are no surveyed control points, known distances, or calibration target. Consequently no
pixel coordinate is promoted into an artifact coordinate.

## What is directly visible

- Four consecutive physical rows begin `ECDM…`, `UOX…`, `TWT…`, and `VTT…`.
- There is no separate engraved row between the `ECDM…` row and the `UOX…` row. Thus the
  inherited image of `OBKR` as its own physical row is false.
- The LOC frame does not show the terminal `?OBKR` of the `ECDM…` row clearly enough to verify
  those glyphs or their spacing independently.
- It does not show both endpoints of any K4-bearing row in a geometry suitable for exact
  character counting.
- Horizontal row baselines, cut-through stencil forms, and curvature are visible.

## Fabrication control

Checkpoint R's first-person Sanborn fabrication account remains the best control: long
horizontal row lines were scribed, while individual metal stencils were located, traced,
drilled, jigsaw-cut, and hand-filed. This predicts horizontal rows plus handcrafted horizontal
placement; it does not predict equal pitch or a shared vertical lattice. The available K4 view
does not establish a departure from that ordinary fabrication practice.

No adequate Smithsonian or archival orthographic K4 close-up is present in the repository.
Folder 8 was already found negative for usable orthographic/restoration geometry and contains a
quarantined solution-adjacent portion; it was not revisited. Folder 10 was already negative for
an x-coordinate layout or fabrication drawing.
