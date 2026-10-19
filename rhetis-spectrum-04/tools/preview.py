"""Draw a collection folder as one HTML sheet: every fixture of its foundation and elements, in light or dark, at its
own size. A review aid for an author working outside the Rhetis repository; it admits nothing — the Rhetis intake
(`python -m services.design_library.importer.intake`) does.

    python preview.py <collection folder> <type steps json> [--dark] [--out sheet.html]

Standard library only. The collection folder is laid out as the reference pack's sample:
    kit/kit.json, kit/<tokens css>, foundation/{foundation.css, foundation.json, fixtures/}, elements/<leaf>/{element.css,
    element.json, fixtures/}
"""
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

_MIN = re.compile(r"\A<!--\s*min:\s*([^>]*?)\s*-->\n")


def _defaults(values):
    return (".slide { " + " ".join(f"{name}: {value};" for name, value in sorted(values.items())) + " }\n") if values else ""


def sheet(collection, type_steps, dark=False):
    collection = Path(collection)
    kit = json.loads((collection / "kit" / "kit.json").read_text(encoding="utf-8"))
    tokens = (collection / "kit" / kit["tokens"]).read_text(encoding="utf-8")
    sources = [("foundation", collection / "foundation", "foundation")]
    sources += [(path.name, path, "element") for path in sorted((collection / "elements").iterdir()) if path.is_dir()]
    css, registrations, defaults, pages = [], {}, {}, []
    for name, folder, kind in sources:
        source = json.loads((folder / f"{kind}.json").read_text(encoding="utf-8"))
        registrations.update(source["registrations"])
        defaults.update(source["tokenDefaults"])
        css.append(f"/* {name} */\n" + (folder / f"{kind}.css").read_text(encoding="utf-8"))
        for fixture in sorted((folder / "fixtures").glob("*.html")):
            text = fixture.read_text(encoding="utf-8")
            found = _MIN.match(text)
            pages.append((f"{name} / {fixture.stem}", found.group(1) if found else "", text[found.end() if found else 0:]))
    # Neutral preview sizes: every element size token at its own size, the large radius at the kit's radius.
    preview = ".slide { " + " ".join(f"--type-{step:g}: {step:g}px;" for step in type_steps) + " --radius-lg: var(--radius); }\n"
    style = "".join(registrations.values()) + "".join(css) + tokens + preview + _defaults(defaults)
    mode = " dark" if dark else ""
    cells = []
    for title, minimum, body in pages:
        cover = re.search(r'<section\b[^>]*class="slide\b', body)
        slide = (re.sub(r'class="slide', f'class="slide{mode}', body, count=1) if cover
                 else f'<section class="slide{mode}"><div class="page"><div class="body">{body}</div></div></section>')
        label = html.escape(title) + (f" <small>min {html.escape(minimum)}</small>" if minimum else "")
        cells.append(f'<article><h2>{label}</h2><div class="frame">{slide}</div></article>')
    frame = ("body{margin:0;padding:24px;background:#e8e8ec;font:14px system-ui;display:grid;gap:24px;"
             "grid-template-columns:repeat(auto-fill,640px)}h2{font-size:13px;font-weight:500;margin:0 0 8px}"
             "small{color:#777;margin-left:8px}article>.frame{width:640px;height:360px;overflow:hidden;border-radius:6px;background:#fff}"
             "article>.frame>.slide{width:1280px;height:720px;transform:scale(.5);transform-origin:0 0;position:relative}")
    return (f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{html.escape(kit["label"])} sheet</title>'
            f"<style>{style}</style><style>{frame}</style></head><body>{''.join(cells)}</body></html>")


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("collection")
    parser.add_argument("type_steps")
    parser.add_argument("--dark", action="store_true")
    parser.add_argument("--out", default="sheet.html")
    arguments = parser.parse_args(argv)
    steps = json.loads(Path(arguments.type_steps).read_text(encoding="utf-8"))
    Path(arguments.out).write_text(sheet(arguments.collection, steps, dark=arguments.dark), encoding="utf-8", newline="\n")
    print(arguments.out)


if __name__ == "__main__":
    main()
