#!/usr/bin/env python3
"""Assemble the single-file Damus dashboard: python3 tools/build.py  ->  index.html"""
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
read = lambda p: (root / p).read_text(encoding="utf-8")
app = read("src/app.js")
ljs = read("vendor/leaflet.js").rstrip("\n")
# Embedded apps: each apps/*.html file ships unmodified inside the page and opens in its own frame.
import json
apps = json.dumps({p.stem: p.read_text(encoding="utf-8") for p in sorted((root / "apps").glob("*.html"))},
                  ensure_ascii=False).replace("<", "\\u003c")
assert "</script" not in app.lower() and "</script" not in ljs.lower()
# The tab icon is embedded so a lone copy of index.html still shows it.
from urllib.parse import quote
favicon = "data:image/svg+xml," + quote(read("icons/favicon.svg").strip(), safe="/:=,;()!*'~ ")
out = (read("src/shell.html")
       .replace("__FAVICON_DATA__", favicon.replace(" ", "%20"))
       .replace("/*__LEAFLET_CSS__*/", read("vendor/leaflet.css").rstrip("\n"))
       .replace("/*__LEAFLET_JS__*/", ljs)
       .replace("/*__LAND__*/[]", read("data/land.json").strip())
       .replace("/*__APPS__*/{}", apps)
       .replace("/*__APP_JS__*/", app))
(root / "index.html").write_text(out, encoding="utf-8")
print("index.html", len(out), "bytes")
