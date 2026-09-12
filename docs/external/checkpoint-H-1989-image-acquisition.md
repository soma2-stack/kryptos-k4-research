# Checkpoint H — 4 Nov 1989 image acquisition handoff

Date: 2026-09-12
Prepared outside Claude's restricted-web environment.

## Branch state checked first
Latest pushed Checkpoint H commit before this handoff: `c08aa49261021a76ce81c5caa6e331050604f890`.

Claude requested these exact target-era picture-alliance frames:

- `16008401`
- `16008415`

Both are confirmed by picture-alliance as **04.11.1989** Alexanderplatz demonstration photographs with the Weltzeituhr in the foreground.

Picture-alliance collection page:
https://www.picture-alliance.com/webseries/weltzeituhr-in-berlin-w194131

Direct public image endpoints exposed by the picture-alliance page:

- https://img.picturealliance.sodatech.com/KARE/public/16008401.jpg
- https://img.picturealliance.sodatech.com/KARE/public/16008415.jpg

The image CDN returns HTTP 403 to automated direct fetching in this environment, so no JPEG bytes were committed here.

## Visual usefulness check

### 16008401
Image-search preview confirms this is a wide, elevated view of the 4 Nov 1989 demonstration with the Weltzeituhr relatively small in frame. It is target-era and archive-identified, but appears low-value for line-by-line panel transcription because the clock occupies a small fraction of the image.

### 16008415
Picture-alliance confirms it is another 4 Nov 1989 demonstration frame with the Weltzeituhr in front. Automated search did not expose a directly downloadable binary here, so this image still needs to be saved manually from the source page or image endpoint and uploaded to Claude as a session file.

## Publicly mirrored same-day close view

A separate public page from HanisauLand (bpb) displays a **4 November 1989** black-and-white close/elevated view of the Weltzeituhr surrounded by demonstrators. The clock is much larger in frame than in 16008401, and several city panels are visibly legible in the public preview.

Page:
https://www.hanisauland.de/wissen/spezial/geschichte/deutsche-einheit/mauerfall-2009-kapitel-4.html

Direct image URL exposed by search:
https://www.hanisauland.de/system/files/153695.jpg

The page credits the image to **picture alliance / akg** and captions it as the 4 November 1989 East Berlin demonstration.

This is not asserted here to be picture-alliance ID 16008415; treat it as an independent same-day image unless source metadata proves identity.

Because it is a same-day target-era close view with a much larger clock image, it may be more useful for CET-face transcription than 16008401 even if it is a different frame.

## Recommended acquisition order

1. Save/upload picture-alliance `16008415` at maximum accessible resolution.
2. Save/upload the HanisauLand 4 Nov 1989 image (`153695.jpg`) because its public preview shows much more panel detail.
3. Save/upload picture-alliance `16008401` only as corroborating target-era geometry/context unless the original file resolution makes the panel text unexpectedly legible.

## Handling rule

Claude should inspect actual uploaded image pixels and should not promote any transcription from this text handoff itself. This file establishes identity/date/source and acquisition priority only.

EXP-024 remains frozen until Claude's existing Tier-1 rule is independently satisfied from target-era evidence.
