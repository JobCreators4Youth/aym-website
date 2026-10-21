# aym-website

An open-source revamp of the official African Youth Movement (AYM) website. Built to modernize our digital platform, streamline donation channels, and scale programs across education, agritech, and entrepreneurship to empower youth and combat rural poverty.

## Project structure

```
.
├── index.html            # Landing page
├── *.html                # 20 supporting pages (about, focus areas, volunteer, donate, ...)
├── assets/
│   ├── css/styles.css    # Single stylesheet
│   ├── js/main.js        # Progressive enhancements (no dependencies)
│   └── img/              # Page imagery
└── _tools/               # Build and QA scripts (Python 3, standard library only)
```

The site is fully static: no build step is required to view it, and there are no third-party JavaScript or CSS dependencies at runtime — only webfonts are pulled from Google Fonts.

## Development

### Prerequisites

Python 3.9 or newer. The scripts use only the standard library — no `pip install` needed.

### Regenerating the site

`_tools/gen_site.py` is the source of truth for all 21 pages. Running it rewrites every HTML file in the repository root:

```bash
python _tools/gen_site.py
```

The generator is idempotent: a fresh run reproduces the committed HTML byte-for-byte, so `git diff` stays clean unless you have actually changed something.

To build into a different directory instead of overwriting the working tree:

```bash
# macOS / Linux
AYM_SITE_DIR=/tmp/aym-build python _tools/gen_site.py

# Windows PowerShell
$env:AYM_SITE_DIR = "C:\tmp\aym-build"; python _tools/gen_site.py
```

All scripts below honour the same `AYM_SITE_DIR` environment variable and fall back to the repository root when it is unset.

### Running the checks

```bash
python _tools/check.py            # every local href/src resolves to a real file
python _tools/check2.py           # structural sanity: one <main>, header/footer, <title>, CSS brace balance
python _tools/verify_donate.py    # payment-method buttons, panels and CTA on donate.html
python _tools/audit_check.py      # 12 content audits (see below)
```

`audit_check.py` covers donate CTA routing, YouTube links, dead `href="#"` links, "click here" link text, button capitalisation, hero layout, the founder link, volunteer roles and filters, ecotourism imagery, donate area links, store actions, and the multi-step volunteer application form.

Run the checks before opening a pull request — they are the fastest way to catch a broken link or a malformed page.

## Deployment

The site can be served from any static host. Because pages are plain HTML with relative asset paths, the repository root is the publish root. GitHub Pages is the simplest option: enable it on the `main` branch and serve the repository root.
