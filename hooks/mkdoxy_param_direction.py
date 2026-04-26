"""
mkdocs hooks for the Amplitude Audio SDK documentation.

Responsibilities:

1. Patch mkdoxy's XML parser so Doxygen @param[in/out/inout] directions render
   as Material Design icons in the generated API reference.

     in    -> :material-location-enter:
     out   -> :material-location-exit:
     inout -> :material-arrow-left-right:

   The patch is applied in-place to the installed mkdoxy/xml_parser.py on every
   build. It's idempotent — a sentinel comment is inserted the first time and
   subsequent runs skip.

2. Post-process each page markdown so that:
   - ``__SDK_BRANCH__`` placeholders are replaced with the GitHub branch name
     provided by the ``SDK_BRANCH`` environment variable, defaulting to
     ``develop``. This is a build-time fallback; at runtime
     ``static/versioned-links.js`` detects the active mike version from the URL
     and rewrites source-code links to the correct branch/tag (e.g.
     ``nightly`` -> ``develop``, ``stable`` -> ``main``, ``v1.0.0`` -> ``v1.0.0``).
   - Doxygen simple sections (``@note``, ``@warning``, ``@attention``,
     ``@remark(s)``, ``@tip``) rendered by mkdoxy as ``**Note:**`` bold headers
     are converted into proper mkdocs-material admonitions (``!!! note`` …).
"""

from __future__ import annotations

import logging
import os
import re
from pathlib import Path

log = logging.getLogger("mkdocs.hooks.mkdoxy_param_direction")

SENTINEL = "# __param_direction_patched__"

ORIGINAL = (
    '            elif item.tag == "parameterlist":\n'
    '                parameteritems = item.findall("parameteritem")\n'
    "                lst = MdList([])\n"
    "                for parameteritem in parameteritems:\n"
    '                    name = parameteritem.find("parameternamelist").find("parametername")\n'
    '                    description = parameteritem.find("parameterdescription").findall("para")\n'
    "                    par = MdParagraph([])\n"
    "                    if name is not None and len(name) > 0:\n"
    "                        par.extend(self.paras(name))\n"
    "                    else:\n"
    "                        par.append(Code(name.text))\n"
    '                    par.append(Text(" "))\n'
)

PATCHED = (
    '            elif item.tag == "parameterlist":\n'
    "                " + SENTINEL + "\n"
    '                parameteritems = item.findall("parameteritem")\n'
    "                lst = MdList([])\n"
    "                for parameteritem in parameteritems:\n"
    '                    name = parameteritem.find("parameternamelist").find("parametername")\n'
    '                    description = parameteritem.find("parameterdescription").findall("para")\n'
    "                    par = MdParagraph([])\n"
    "                    _dir = name.get('direction') if name is not None else None\n"
    "                    _dir_icon = {\n"
    "                        'in': ':material-location-enter:',\n"
    "                        'out': ':material-location-exit:',\n"
    "                        'inout': ':material-arrow-left-right:',\n"
    "                    }.get(_dir)\n"
    "                    if _dir_icon:\n"
    "                        par.append(Text(_dir_icon + ' '))\n"
    "                    if name is not None and len(name) > 0:\n"
    "                        par.extend(self.paras(name))\n"
    "                    else:\n"
    "                        par.append(Code(name.text))\n"
    '                    par.append(Text(" "))\n'
)


def _patch_xml_parser() -> None:
    import mkdoxy

    parser_path = Path(mkdoxy.__file__).parent / "xml_parser.py"
    source = parser_path.read_text(encoding="utf-8")

    if SENTINEL in source:
        return

    if ORIGINAL not in source:
        log.warning(
            "mkdoxy_param_direction: could not find the expected parameterlist "
            "block in %s; skipping patch. The mkdoxy version may have changed.",
            parser_path,
        )
        return

    parser_path.write_text(source.replace(ORIGINAL, PATCHED), encoding="utf-8")
    log.info("mkdoxy_param_direction: patched %s", parser_path)


def on_startup(command, dirty, **kwargs):
    _patch_xml_parser()


# ---------------------------------------------------------------------------
# Markdown post-processing
# ---------------------------------------------------------------------------

_SDK_BRANCH = os.environ.get("SDK_BRANCH", "develop")

_ADMONITION_KINDS = {
    "Note": "note",
    "Warning": "warning",
    "Attention": "warning",
    "Remark": "info",
    "Remarks": "info",
    "Tip": "tip",
    "Important": "info",
}

# Match the bold header emitted by mkdoxy for a simplesect, plus the single
# paragraph of body that follows it on the next non-blank line. Body stops at
# the next blank line — which matches how mkdoxy lays out each simplesect.
_ADMON_RE = re.compile(
    r"^(?P<indent>[ \t]*)\*\*(?P<title>Note|Warning|Attention|Remarks?|Tip|Important):\*\*[ \t]*\n"
    r"(?:[ \t]*\n)+"
    r"(?P<body>(?:(?P=indent)[^\n]+\n)+)",
    re.MULTILINE,
)


def _rewrite_admonitions(markdown: str) -> str:
    def _sub(match: re.Match[str]) -> str:
        indent = match.group("indent")
        title = match.group("title")
        kind = _ADMONITION_KINDS.get(title, "note")
        body_lines = match.group("body").splitlines()
        reindented = "\n".join(f"{indent}    {line[len(indent):]}" for line in body_lines if line)
        return f'{indent}!!! {kind} "{title}"\n{reindented}\n'

    return _ADMON_RE.sub(_sub, markdown)


def on_page_markdown(markdown: str, page=None, config=None, files=None, **kwargs) -> str:
    out = markdown.replace("__SDK_BRANCH__", _SDK_BRANCH)
    out = _rewrite_admonitions(out)
    return out
