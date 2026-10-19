# QA Report

Environment: Chromium 1.56 via Playwright (headless, Linux), local file rendering, run with qa.py. No external network, no ESP, no Gmail/Outlook/Apple Mail access.

| # | Test | Result | Method / notes |
|---|---|---|---|
| A | Static HTML tag balance | PASS | Python HTMLParser: no unclosed/mismatched tags. Full W3C validation not run (offline); email conditional comments/VML are not valid in strict validators. |
| B | Links and missing destinations | PASS (with placeholders) | 5 hrefs, none empty; no JavaScript or onclick |
| B2 | CTA goes to the real booking page | BLOCKED | URL not in supplied files; REPLACE_WITH_REAL_TOUR_URL placeholder in place. **Not production-ready.** |
| B3 | Logo/footer website opens | BLOCKED | https://www.foreverbeauty.com taken from reference image; no network to test |
| C | Missing images / paths | PASS | 3/3 images resolve and load in preview-local.html |
| C2 | Production image URLs | BLOCKED | Images not yet hosted; placeholder host in index.html |
| D | Image dimensions/ratio/size | PASS | Natural vs displayed ratio within 0.003 on all images; files 9 to 157 KB (total email images about 230 KB). Interior hero is an upscale (see README), not true retina. |
| E | Desktop, 600px container | PASS | Container 600px at 900px viewport; logo 200px, CTA 243x52 |
| F | Mobile 320 / 375 / 390 | PASS | scrollWidth equals viewport at each width (an overflow at 320 was found and fixed) |
| G | Overflow, stretching, CTA, readability | PASS | No stretching; CTA 272 to 342px wide x 52px tall on mobile; body text 16px; previews visually inspected |
| H | Accessibility basics | PASS | Alt text on all images, text contrast 4.73:1 (button) to 14.2:1, descriptive link text, logical order, lang attribute. No screen-reader test. |
| I | CTA URL matches verified URL | BLOCKED | No URL supplied |
| J | ESP merge tags / unsubscribe | BLOCKED | ESP unknown |
| K | Gmail / Outlook / Apple Mail | BLOCKED | No access. Outlook VML button and ghost table are written but untested. |

Clients actually verified: none (Chromium only). Remaining client inputs: tour URL, ESP, mailing address, hosted image location, original high-res interior photo, copy approval, confirmation of website URL.

## Tour page and click-through (added)
| # | Test | Result | Notes |
|---|---|---|---|
| T1 | Email CTA opens tour page | PASS (local) | preview-local.html maps the placeholder to tour.html; Playwright click opened tour.html in a new tab (the CTA uses target=_blank) |
| T2 | Form validation | PASS | Empty submit shows 5 errors and focuses the first; invalid email blocked |
| T3 | Unconfigured form behaves honestly | PASS | Shows a "not connected" message instead of fake success |
| T4 | Successful submission path | PASS (mocked) | Tested against an intercepted fake endpoint only |
| T5 | Real submissions arrive | BLOCKED | No endpoint supplied |
| T6 | Tour page at 320/375/390/900px | PASS | No horizontal overflow, all images load; previews: preview-tour-desktop.png, preview-tour-mobile.png |
| T7 | Hosted production URL works | BLOCKED | Not hosted yet |
