# /// script
# requires-python = ">=3.11"
# dependencies = ["markdown-it-py[linkify]>=3"]
# ///
"""Build one PDF from all Markdown files in the repo.

Run from anywhere:  uv run tools/build_pdf.py [-o out.pdf]
Needs Google Chrome (or Chromium). Set CHROME=/path/to/chrome to use another one.
"""

import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT = ROOT / "build" / f"{ROOT.name}.pdf"
SKIP_DIRS = {".git", "build", "node_modules"}
# Show only the newest sections of these files on the contents page.
TOC_LIMIT = {"CHANGELOG.md": 5}
# Emoji next to each file on the contents page. Unknown files get 📄.
TOC_ICON = {
    "README.md": "🚗",
    "CHANGELOG.md": "📜",
    "MAINTENANCE.md": "🛢️",
    "ROADMAP.md": "🗺️",
    "brakes/README.md": "💿",
    "drivetrain/README.md": "⚙️",
    "electrical/README.md": "⚡",
    "electrical/tunes/README.md": "💾",
    "engine/README.md": "🔥",
    "fuel/README.md": "⛽",
    "interior/README.md": "💺",
    "suspension/README.md": "🔩",
    "wheels/README.md": "🛞",
}

CSS = """
@page { size: 158mm 210mm; margin: 9mm 8mm 10mm 8mm; }
* { box-sizing: border-box; }
body { font: 10.5pt/1.4 -apple-system, "Helvetica Neue", Helvetica, Arial, sans-serif; color: #000; margin: 0; }
h1 { font-size: 18pt; margin: 0 0 8pt; border-bottom: 1.5pt solid #000; padding-bottom: 3pt; }
h2 { font-size: 13.5pt; margin: 14pt 0 5pt; break-after: avoid; }
h3 { font-size: 11.5pt; margin: 10pt 0 4pt; break-after: avoid; }
a { color: #000; }
a.internal { text-decoration: none; border-bottom: 1pt dotted #000; }
p, ul, ol { margin: 0 0 6pt; }
ul, ol { padding-left: 16pt; }
table { border-collapse: collapse; margin: 0 0 8pt; font-size: 9pt; width: 100%; }
th, td { border: 0.75pt solid #000; padding: 2pt 4pt; text-align: left; vertical-align: top; }
th { background: #e6e6e6; }
tr { break-inside: avoid; }
code { font: 9pt Menlo, monospace; }
pre { font: 7.3pt/1.25 Menlo, monospace; border: 0.75pt solid #000; padding: 4pt; white-space: pre-wrap; break-inside: avoid; }
pre code { font: inherit; }
img { max-width: 100%; max-height: 170mm; display: block; margin: 4pt auto; }
.file { break-before: page; }
.imgpage { position: relative; height: 182mm; }
.imgpage img { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); max-height: 100%; margin: 0; }
.imgpage img.wide { max-width: 180mm; max-height: 140mm; transform: translate(-50%, -50%) rotate(90deg); }
.path { font: 8pt Menlo, monospace; color: #444; margin-bottom: 2pt; display: flex; justify-content: space-between; }
.path a { text-decoration: none; }
.toc ul { list-style: none; padding-left: 0; }
.toc h1 { font-size: 17pt; margin-bottom: 6pt; }
.toc > ul > li { margin: 0 0 5pt; font-size: 12.5pt; font-weight: 600; line-height: 1.3; }
.toc .icon { display: inline-block; width: 18pt; }
.toc li li { font-size: 10.5pt; font-weight: 400; display: inline; }
.toc li li + li::before { content: " · "; }
.toc ul ul { margin: 1pt 0 0 18pt; }
"""


# Turn wide images sideways so they fill the tall page.
ROTATE_JS = """<script>
for (const img of document.querySelectorAll(".imgpage img")) {
  const set = () => img.classList.toggle("wide", img.naturalWidth > img.naturalHeight);
  img.complete ? set() : img.addEventListener("load", set);
}
</script>"""


def find_md_files():
    files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = sorted(
            d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")
        )
        files += [Path(dirpath, f) for f in filenames if f.lower().endswith(".md")]
    rel = [f.relative_to(ROOT) for f in files]
    # README first, then other top-level files, then folders.
    return sorted(
        rel, key=lambda p: (p != Path("README.md"), len(p.parts) > 1, str(p).lower())
    )


def file_id(rel):
    return "f-" + re.sub(r"[^a-z0-9]+", "-", str(rel).lower()).strip("-")


def slugify(text):
    text = re.sub(r"<[^>]+>", "", html.unescape(text)).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def add_heading_ids(body, fid):
    """Give headings GitHub-style ids, prefixed by the file id. Return html and heading list."""
    seen = {}
    headings = []

    def repl(m):
        level, inner = m.group(1), m.group(2)
        slug = slugify(inner)
        n = seen.get(slug, 0)
        seen[slug] = n + 1
        if n:
            slug = f"{slug}-{n}"
        hid = f"{fid}--{slug}"
        headings.append((int(level), re.sub(r"<[^>]+>", "", inner), hid))
        return f'<h{level} id="{hid}">{inner}</h{level}>'

    return re.sub(r"<h([1-6])>(.*?)</h\1>", repl, body), headings


IMAGE_EXT = {".jpg", ".jpeg", ".png", ".gif", ".webp"}


def fix_links(body, rel, md_ids, images):
    base = (ROOT / rel).parent

    def repl(m):
        href, text = m.group(1), m.group(2)
        if re.match(r"^[a-z]+:", href):
            return m.group(0)
        path_part, _, anchor = href.partition("#")
        if not path_part:
            target = rel
        else:
            target = (base / path_part).resolve()
            try:
                target = target.relative_to(ROOT)
            except ValueError:
                return text
        if target in md_ids:
            fid = md_ids[target]
            dest = f"{fid}--{anchor}" if anchor else fid
            return f'<a class="internal" href="#{dest}">{text}</a>'
        if target.suffix.lower() in IMAGE_EXT and (ROOT / target).is_file():
            images.setdefault(target, file_id(target))
            return f'<a class="internal" href="#{images[target]}">{text}</a>'
        # Not in the PDF (folder, html tool): keep the text, drop the link.
        return text

    return re.sub(r'<a href="([^"]*)"[^>]*>(.*?)</a>', repl, body)


def fix_images(body, rel):
    base = (ROOT / rel).parent

    def repl(m):
        src = m.group(2)
        if re.match(r"^[a-z]+:", src):
            return m.group(0)
        return f"{m.group(1)}{(base / src).resolve().as_uri()}{m.group(3)}"

    return re.sub(r'(<img src=")([^"]+)(")', repl, body)


def task_boxes(body):
    body = re.sub(r"<li>\[ \]\s*", "<li>☐ ", body)
    return re.sub(r"<li>\[[xX]\]\s*", "<li>☑ ", body)


def build_html(files):
    md = MarkdownIt("commonmark", {"html": True, "linkify": True}).enable(
        ["table", "strikethrough", "linkify"]
    )
    md_ids = {f: file_id(f) for f in files}
    sections, toc, images = [], [], {}
    for rel in files:
        fid = md_ids[rel]
        body = md.render((ROOT / rel).read_text(encoding="utf-8"))
        body, headings = add_heading_ids(body, fid)
        body = fix_links(body, rel, md_ids, images)
        body = fix_images(body, rel)
        body = task_boxes(body)
        title = next((t for lvl, t, _ in headings if lvl == 1), str(rel))
        h2 = [(t, hid) for lvl, t, hid in headings if lvl == 2]
        limit = TOC_LIMIT.get(str(rel), len(h2))
        subs = "".join(
            f'<li><a href="#{hid}">{html.escape(t)}</a></li>' for t, hid in h2[:limit]
        )
        if len(h2) > limit:
            subs += f'<li><a href="#{fid}">all {len(h2)} entries…</a></li>'
        toc.append(
            f'<li><span class="icon">{TOC_ICON.get(rel.as_posix(), "📄")}</span>'
            f'<a href="#{fid}">{html.escape(title)}</a>'
            f"{f'<ul>{subs}</ul>' if subs else ''}</li>"
        )
        sections.append(
            f'<section class="file" id="{fid}">'
            f'<div class="path"><span>{html.escape(str(rel))}</span><a href="#contents">↑ Contents</a></div>'
            f"{body}</section>"
        )
    if images:
        toc.append(
            f'<li><span class="icon">🖼️</span>'
            f'<a href="#{next(iter(images.values()))}">Images</a></li>'
        )
        for target, iid in images.items():
            sections.append(
                f'<section class="file" id="{iid}">'
                f'<div class="path"><span>{html.escape(str(target))}</span><a href="#contents">↑ Contents</a></div>'
                f'<div class="imgpage"><img src="{(ROOT / target).as_uri()}"></div></section>'
            )
    return (
        f'<!doctype html><html><head><meta charset="utf-8"><title>{ROOT.name}</title>'
        f"<style>{CSS}</style></head><body>"
        f'<section class="toc" id="contents"><h1>{ROOT.name}: Contents</h1><ul>{"".join(toc)}</ul></section>'
        f"{''.join(sections)}{ROTATE_JS}</body></html>"
    )


def find_chrome():
    candidates = [
        os.environ.get("CHROME"),
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
    ]
    for c in candidates:
        if c and Path(c).exists():
            return c
    sys.exit("Chrome not found. Install Google Chrome or set CHROME=/path/to/chrome.")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("-o", "--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument(
        "--html", action="store_true", help="also save the HTML next to the PDF"
    )
    args = parser.parse_args()

    files = find_md_files()
    page = build_html(files)
    out = args.out.resolve()
    out.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        html_path = Path(tmp, "repo.html")
        html_path.write_text(page, encoding="utf-8")
        if args.html:
            shutil.copy(html_path, out.with_suffix(".html"))
        subprocess.run(
            [
                find_chrome(),
                "--headless",
                "--disable-gpu",
                "--no-pdf-header-footer",
                "--generate-pdf-document-outline",
                f"--print-to-pdf={out}",
                html_path.as_uri(),
            ],
            check=True,
            capture_output=True,
        )
    print(f"{len(files)} files -> {out}")


if __name__ == "__main__":
    main()
