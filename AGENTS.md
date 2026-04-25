# AGENTS.md — Amplitude Audio SDK Documentation

This file provides everything an AI coding agent needs to work effectively in this repository.

## Project Overview

This repository builds the public documentation website for the **Amplitude Audio SDK**, a cross-platform C++ audio engine for games. The live site is hosted at https://docs.amplitudeaudiosdk.com.

The documentation is a static site built with **MkDocs** (via the `properdocs` wrapper), the **Material for MkDocs** theme, and the **mkdoxy** plugin for auto-generating C++ API reference pages from Doxygen comments.

**Key repositories**
- Documentation (this repo): `https://github.com/AmplitudeAudio/doc-api-reference`
- SDK source code: `https://github.com/AmplitudeAudio/sdk`

## Technology Stack

| Layer | Technology |
|-------|------------|
| Site generator | [ProperDocs](https://github.com/timothycrosley/properdocs) 1.6.7 (MkDocs-compatible wrapper) |
| Theme | [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 9.7.6 |
| Markdown extensions | PyMdown Extensions, Admonition, attr_list, def_list, md_in_html, TOC, MathJax, Mermaid |
| API generation | [mkdoxy](https://github.com/JakubAndrysek/MkDoxy) 1.2.8 (wraps Doxygen) |
| Versioning | [mike](https://github.com/jimporter/mike) 2.2.0 |
| Templating | Jinja2 (MkDocs/Material + custom mkdoxy templates) |
| Language | Python 3 (virtual environment in `.venv/`) |

## Repository Layout

```
.
├── properdocs.yaml           # Main MkDocs-style configuration (site name, theme, plugins, nav)
├── requirements.txt          # Python dependencies (pinned versions)
├── docs/                     # All source markdown and static assets
│   ├── index.md              # Homepage (grid cards linking to sections)
│   ├── SUMMARY.md            # Navigation tree for mkdocs-literate-nav
│   ├── getting-started/      # SDK overview, concepts, installation, quick start
│   ├── integration/          # Step-by-step C++ integration guide
│   ├── project/              # Amplitude project file format reference
│   ├── tutorials/            # Custom effect, codec, driver, fader tutorials
│   ├── api/                  # API reference landing page (auto-generated pages land in .mkdoxy/)
│   └── static/               # CSS, JS, images, logos, favicons
├── overrides/                # Material theme template overrides
│   ├── main.html             # Microsoft Clarity script + outdated-version banner
│   ├── redirect.html         # Meta-redirect template for section index pages
│   └── partials/
│       ├── copyright.html    # Footer with Doxide + Material attribution
│       └── integrations/     # (reserved for integration partials)
├── templates/                # Custom Jinja2 templates for mkdoxy API output
│   ├── member.jinja2         # Top-level class/namespace/file page layout
│   └── memDef.jinja2         # Collapsible admonition for each member (function, variable, etc.)
├── hooks/                    # MkDocs build hooks
│   └── mkdoxy_param_direction.py
├── site/                     # Build output (gitignored, produced by `properdocs build`)
└── .mkdoxy/                  # Cached/generated API markdown (gitignored)
```

## Build, Serve, and Deploy Commands

All commands assume the virtual environment is activated:

```bash
# Activate the existing venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate        # Windows

# Install / update dependencies
pip install -r requirements.txt

# Development server with hot reload
properdocs serve
# Site available at http://127.0.0.1:8000

# Build static site (outputs to site/)
properdocs build

# Strict build (fails on warnings)
properdocs build --strict

# Deploy a versioned release (uses mike)
mike deploy <version> <alias> --push
mike set-default <version> --push
mike list
```

> **Note:** `properdocs` is used instead of `mkdocs` because the project relies on the `properdocs` wrapper package. The configuration file is named `properdocs.yaml`.

## API Reference Generation

The C++ API reference is **auto-generated** and should never be edited by hand.

**Prerequisites:** The SDK repository must be cloned adjacent to this documentation repository:

```
parent-directory/
├── sdk/                      # SDK source code (https://github.com/AmplitudeAudio/sdk)
│   └── include/              # C++ headers parsed by Doxygen
└── doc-api-reference/        # This repository
```

**How it works**
1. `properdocs build` / `properdocs serve` triggers the `mkdoxy` plugin.
2. mkdoxy runs Doxygen over `../sdk/include` (only `*.h*` files, recursively).
3. Doxygen XML is transformed into Markdown via the custom templates in `templates/`.
4. Generated Markdown is written to `.mkdoxy/api/` and then included in the site build.

**Key Doxygen settings** (from `properdocs.yaml`):
- `FILE_PATTERNS: "*.h*"`
- `RECURSIVE: True`
- `SHOW_NAMESPACES: NO`
- `PREDEFINED`: expands `AM_INLINE`, `AM_API_PUBLIC`, `AM_API_PRIVATE`, and platform macros (`AM_PLATFORM_ANDROID`, `AM_PLATFORM_IOS`)
- `STRIP_FROM_PATH: ../sdk`
- `CLANG_ASSISTED_PARSING: YES`

**API groups** (Doxygen `@defgroup` tags) — documented in `docs/api/index.md`:
Assets, Core, DSP, Engine, IO, Math, Memory, Mixer.

## Build Hooks

`hooks/mkdoxy_param_direction.py` performs two post-processing tasks on every build:

1. **Patch mkdoxy's XML parser** (`on_startup`) — injects Material Design icons for Doxygen `@param[in]`, `@param[out]`, `@param[inout]` directions:
   - `in` → `:material-location-enter:`
   - `out` → `:material-location-exit:`
   - `inout` → `:material-arrow-left-right:`
   The patch is idempotent (guarded by a sentinel comment).

2. **Markdown post-processing** (`on_page_markdown`):
   - Replaces `__SDK_BRANCH__` placeholders with the value of the `SDK_BRANCH` environment variable (defaults to `develop`). This ensures source-code links in API docs point to the correct GitHub branch.
   - Converts Doxygen simple-section bold headers (`**Note:**`, `**Warning:**`, `**Tip:**`, etc.) emitted by mkdoxy into proper Material admonitions (`!!! note`, `!!! warning`, `!!! tip`, etc.).

## Navigation

The site navigation is **not** defined inside `properdocs.yaml`. Instead, it lives in `docs/SUMMARY.md` and is consumed by the `mkdocs-literate-nav` plugin. Editing `SUMMARY.md` is the correct way to add, remove, or reorder pages.

Section index pages (e.g., `getting-started/index.md`) use the `redirect.html` template with `url: <subpage>/` to forward readers to the first meaningful content page.

## Content Style Guidelines

### File naming
- Use **lowercase with hyphens** (kebab-case), e.g., `cmake-setup.md`, `sound-bank.md`.
- Keep filenames consistent with the resulting URL slugs.

### Markdown conventions
- **Front matter** is used for `title`, `description`, and occasionally `template` or `social.cards`.
- **Admonitions** use the Material syntax:
  ```markdown
  !!! note "Title"
      Body indented with 4 spaces.
  ```
- **Tabbed content** uses PyMdown tabbed syntax:
  ```markdown
  === "Tab 1"
      Content here.
  === "Tab 2"
      Other content.
  ```
- **Code blocks** should specify the language for syntax highlighting. The project enables line numbers and language classes.
- **Icons** from Material Design and FontAwesome are referenced with `:material-...:` and `:fontawesome-...:` shortcodes.
- **Internal links** use relative Markdown paths (e.g., `[Getting Started](./getting-started/introduction.md)`).
- **Mermaid diagrams** and **MathJax** expressions are supported via fenced code blocks and `pymdownx.arithmatex`.

### Static assets
- Place images, CSS, and JS in `docs/static/`.
- Custom styles: `docs/static/doxide.css` (defines admonition icons for API member kinds: variable, function, concept, define, typedef, enum).
- Custom scripts: `docs/static/consent.js` (handles Microsoft Clarity cookie consent logic).
- Logos: `docs/static/logo_white.svg`, `docs/static/favicon.svg`.

## Theme Customization

The project uses a heavily customized Material for MkDocs setup:

- **Primary color:** Cyan. **Accent:** Red.
- **Fonts:** DM Sans (text), JetBrains Mono (code).
- **Features enabled:** `navigation.tabs`, `navigation.path`, `navigation.footer`, `navigation.top`, `content.code.copy`, `search.highlight`, `search.suggest`, `toc.follow`, `announce.dismiss`, `navigation.indexes`.
- **Cookie consent** banner is configured for Google Analytics and Microsoft Clarity.
- **Social cards** are auto-generated by the `social` plugin into `docs/static/cards/`.

Template overrides in `overrides/`:
- `main.html` injects the Clarity tracking script and overrides the "outdated version" banner block.
- `partials/copyright.html` replaces the default footer credit with "Made with Doxide and Material for MkDocs".

## Testing Strategy

There are **no automated tests** in this repository. Quality assurance is manual:

1. Run `properdocs serve` and visually verify pages locally.
2. Run `properdocs build --strict` to catch broken internal links, missing files, and Markdown warnings.
3. Verify API reference pages render correctly when the adjacent SDK repository is present.
4. Check that `mike` version aliases and redirects work as expected before pushing deployments.

## Deployment

The site is deployed to **GitHub Pages** using `mike` for multi-version support:

- `nightly` alias tracks the `develop` branch of the SDK.
- `stable` alias tracks the latest release.
- The canonical version is set to `nightly` in the mkdoxy/mike configuration.
- Social cards, analytics, and cookie consent are active in production.

## Security and Privacy Considerations

- **Microsoft Clarity** and **Google Analytics** scripts are present in `overrides/main.html` and `properdocs.yaml`. These are gated by the Material cookie-consent banner.
- `consent.js` explicitly calls `window.clarity('consent')` only when the user has consented; otherwise it calls `window.clarity('consent', false)`.
- No user secrets or API keys are stored in this repository.

## Working with the Adjacent SDK Repository

Several features depend on `../sdk` being present:

| Feature | Dependency |
|---------|------------|
| API reference pages | `../sdk/include/` |
| Source-code links in API docs | GitHub repo (`AmplitudeAudio/sdk`) with branch matching the active mike version. Build-time fallback uses the `SDK_BRANCH` env var (default `develop`); at runtime `static/versioned-links.js` rewrites links based on the URL version prefix (`nightly` → `develop`, `stable` → `main`, `vN.x` → `vN.x`). Minor/patch tags (`v1.0.0`, etc.) do not have separate doc sites. |

If the SDK repository is missing, `mkdoxy` will fail to generate API pages. For local work that does not touch API docs, you can temporarily disable the `mkdoxy` plugin in `properdocs.yaml`, but **do not commit that change**.

## Common Tasks for Agents

- **Add a new documentation page:** Create the `.md` file in the appropriate `docs/<section>/` folder, then add it to `docs/SUMMARY.md`.
- **Update API templates:** Edit `templates/member.jinja2` or `templates/memDef.jinja2`. These are Jinja2 templates consumed by mkdoxy.
- **Change theme styling:** Edit `docs/static/doxide.css` or add CSS files and list them under `extra_css` in `properdocs.yaml`.
- **Add a build-time transformation:** Extend `hooks/mkdoxy_param_direction.py` and register the new hook under the `hooks:` key in `properdocs.yaml`.
- **Bump a dependency:** Update `requirements.txt`, run `pip install -r requirements.txt`, and verify the build still passes.
