# Forever Beauty Salon Suites: McDonough Announcement Email

## Files
index.html (production template) · preview-local.html (same email, local image paths, for previews) · assets/ · originals/ (untouched supplied files) · style-guide.md · email-plain-text.txt · preview-desktop.png · preview-mobile.png · QA-REPORT.md · qa.py (test script)

## Placeholders to replace before sending (search index.html for REPLACE)
| Placeholder | Where | Needed |
|---|---|---|
| REPLACE_WITH_REAL_TOUR_URL | CTA (2x: VML for Outlook + standard anchor), plain text | The https URL where tour.html is hosted (or the client's own booking page, if they have one). No booking URL exists in the supplied files, so none was invented. |
| REPLACE_WITH_FORM_ENDPOINT | `<form action>` in tour.html | A form-handling endpoint (for example from Formspree, Getform, or the client's web host) that emails or stores submissions. Until set, the form shows an honest "not connected" message. |
| https://REPLACE_WITH_IMAGE_HOST/ | 3 image srcs | HTTPS location of the files in assets/ (upload to ESP image library, then paste the URLs) |
| REPLACE_WITH_ESP_UNSUBSCRIBE_TAG | Footer link, plain text | The ESP's own unsubscribe merge tag. ESP is unknown, so no syntax is guessed. |
| [REPLACE WITH PHYSICAL MAILING ADDRESS] | Footer (highlighted) | Required by CAN-SPAM; not supplied |

## Link audit
| Element | Destination | Status |
|---|---|---|
| Logo | https://www.foreverbeauty.com | Read from the client's reference newsletter; not tested live (no external network) and the https scheme is assumed. Confirm. |
| SCHEDULE A TOUR | REPLACE_WITH_REAL_TOUR_URL (opens tour.html once hosted) | Works end to end locally (preview-local.html opens tour.html); needs the hosted URL |
| tour.html logo / footer | https://www.foreverbeauty.com | Same as above |
| Footer website | https://www.foreverbeauty.com | Same as logo |
| Unsubscribe | REPLACE_WITH_ESP_UNSUBSCRIBE_TAG | Blocked: ESP needed |

## ESP import
1. Upload assets/ images and copy their HTTPS URLs. 2. Replace the image host placeholder (find and replace `https://REPLACE_WITH_IMAGE_HOST/` with your folder URL, keeping filenames). 3. Replace the other placeholders. 4. Paste index.html into a custom-HTML block; set the plain-text part from email-plain-text.txt. 5. Send test messages to Gmail, Outlook and Apple Mail before launch.

## Image caveat
The supplied interior photo is only 364x480 px. It is upscaled 1.65x for the 600px hero, so it will look a little soft, and a true 2x version is not possible. For best results send the original full-resolution photo (at least 1200px wide); then export 600px and 1200px JPGs at quality ~80. The supplied exterior photo supports near-2x (1160px) and is used as the retina source.

## Copy needing client approval
"A New Beauty Destination in McDonough, Georgia", the invitation paragraph and "We would love to show you around." The copy deliberately avoids "Now Open", dates and availability claims. The footer line about why recipients get the email is generic; adjust to the actual list.

## Tour page (tour.html)
A separate single-page companion that the email button opens: logo, interior photo, "Schedule a Tour" headline, a request form (name, email, phone, profession, optional preferred time and message), storefront photo and footer. No invented address, phone, hours or availability. Validation, error messages and a spam honeypot are built in.
Setup: 1) upload tour.html and the assets/ folder to the client's web host (keep the folder name), 2) set `action` on the form to a real endpoint, 3) put the page's final https URL in the email CTA, 4) submit a real test request and confirm it arrives.
