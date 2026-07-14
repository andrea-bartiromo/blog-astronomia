#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(ROOT.glob("*.html"))
ERRORS: list[str] = []
WARNINGS: list[str] = []

class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: list[str] = []
        self.links: list[tuple[str, str]] = []
        self.images: list[dict[str, str]] = []
        self.ids: set[str] = set()
        self.h1_count = 0
        self.title_count = 0
        self.has_lang = False
        self.has_viewport = False
        self.has_description = False
        self.has_main = False
        self.has_skip_link = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {k: (v or "") for k, v in attrs}
        self.tags.append(tag)
        if tag == "html" and data.get("lang"):
            self.has_lang = True
        if tag == "meta" and data.get("name") == "viewport":
            self.has_viewport = True
        if tag == "meta" and data.get("name") == "description" and data.get("content"):
            self.has_description = True
        if tag == "title":
            self.title_count += 1
        if tag == "h1":
            self.h1_count += 1
        if tag == "main":
            self.has_main = True
        if tag == "a" and "skip-link" in data.get("class", "").split():
            self.has_skip_link = True
        if data.get("id"):
            self.ids.add(data["id"])
        if tag == "a" and data.get("href"):
            self.links.append(("href", data["href"]))
        if tag in {"img", "script", "link", "source"}:
            for attr in ("src", "href", "srcset"):
                if data.get(attr):
                    self.links.append((attr, data[attr]))
        if tag == "img":
            self.images.append(data)

def local_target(page: Path, raw: str) -> tuple[Path | None, str | None]:
    raw = raw.strip()
    if not raw or raw.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return None, None
    if raw.startswith(("http://", "https://", "//")):
        return None, None
    first = raw.split(",", 1)[0].strip().split()[0]
    parts = urlsplit(first)
    path = unquote(parts.path)
    if not path:
        return page, parts.fragment or None
    target = (page.parent / path).resolve()
    return target, parts.fragment or None

for page in HTML_FILES:
    text = page.read_text(encoding="utf-8")
    if "</html>" not in text.lower() or "</body>" not in text.lower():
        ERRORS.append(f"{page.name}: documento probabilmente troncato (manca </body> o </html>)")
    parser = PageParser()
    try:
        parser.feed(text)
    except Exception as exc:
        ERRORS.append(f"{page.name}: errore di parsing HTML: {exc}")
        continue

    if not parser.has_lang:
        ERRORS.append(f"{page.name}: attributo lang mancante su <html>")
    if not parser.has_viewport:
        ERRORS.append(f"{page.name}: meta viewport mancante")
    if parser.title_count != 1:
        ERRORS.append(f"{page.name}: atteso un solo <title>, trovati {parser.title_count}")
    if not parser.has_description:
        WARNINGS.append(f"{page.name}: meta description mancante")
    if parser.h1_count != 1:
        ERRORS.append(f"{page.name}: atteso un solo <h1>, trovati {parser.h1_count}")
    if not parser.has_main:
        ERRORS.append(f"{page.name}: elemento <main> mancante")
    if not parser.has_skip_link:
        WARNINGS.append(f"{page.name}: skip link mancante")

    for image in parser.images:
        if "alt" not in image:
            ERRORS.append(f"{page.name}: immagine senza attributo alt ({image.get('src', 'src sconosciuto')})")
        src = image.get("src", "")
        if src and not src.startswith(("http://", "https://", "//", "data:")):
            target, _ = local_target(page, src)
            if target and not target.exists():
                ERRORS.append(f"{page.name}: immagine locale mancante: {src}")

    for attr, value in parser.links:
        values = [value]
        if attr == "srcset":
            values = [item.strip().split()[0] for item in value.split(",")]
        for candidate in values:
            target, fragment = local_target(page, candidate)
            if target is None:
                continue
            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                ERRORS.append(f"{page.name}: riferimento locale inesistente: {candidate}")
                continue
            if fragment and target.suffix.lower() == ".html":
                target_text = target.read_text(encoding="utf-8")
                if not re.search(rf'\bid=["\']{re.escape(fragment)}["\']', target_text):
                    ERRORS.append(f"{page.name}: ancora inesistente in {target.name}: #{fragment}")

sitemap = ROOT / "sitemap.xml"
if sitemap.exists():
    try:
        tree = ET.parse(sitemap)
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        urls = [el.text.strip() for el in tree.findall(".//sm:loc", ns) if el.text]
        duplicates = sorted({u for u in urls if urls.count(u) > 1})
        if duplicates:
            ERRORS.append("sitemap.xml: URL duplicati: " + ", ".join(duplicates))
        if any(u.endswith("/index.html") for u in urls):
            WARNINGS.append("sitemap.xml: index.html duplica normalmente la homepage canonica")
    except Exception as exc:
        ERRORS.append(f"sitemap.xml: XML non valido: {exc}")

print(f"Controllate {len(HTML_FILES)} pagine HTML.")
for warning in WARNINGS:
    print(f"WARNING: {warning}")
for error in ERRORS:
    print(f"ERROR: {error}")

if ERRORS:
    print(f"\nControllo fallito: {len(ERRORS)} errore/i e {len(WARNINGS)} avviso/i.")
    sys.exit(1)

print(f"\nControllo superato con {len(WARNINGS)} avviso/i.")
