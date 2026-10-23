"""Draw a collection folder as one HTML sheet: every fixture of its foundation and elements, in light or dark, at its
own size. A review aid for an author working outside the Rhetis repository; it admits nothing — the Rhetis intake
(`python -m services.design_library.importer.intake`) does.

    python preview.py <collection folder> <type steps json> [--dark] [--out sheet.html]
                      [--palette contract/palette.json] [--fonts fonts/fonts.css]

Standard library only. The collection folder is laid out as the reference pack's sample:
    kit/kit.json, kit/<tokens css>, foundation/{foundation.css, foundation.json, fixtures/}, elements/<leaf>/{element.css,
    element.json, fixtures/}
The palette and fonts default to the pack's own (`contract/palette.json`, `fonts/fonts.css` beside the type steps'
folder). Colours come only from the palette, drawn with the library's reference style, so a collection is judged by
its design alone. An icon seat (`[data-icon]`) is drawn as a dashed ring the size Rhetis fills with the Lucide icon.
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


def _palette(modes):
    """The reference palette: light values on `.slide`, dark values on `.slide.dark`."""
    return "".join((".slide.dark" if mode == "dark" else ".slide") + " { "
                   + " ".join(f"{name}: {value};" for name, value in values.items()) + " }\n"
                   for mode, values in modes.items())


def sheet(collection, type_steps, palette, dark=False, fonts_href=None):
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
    # The palette comes after the kit's tokens: previews draw every collection on the one reference style.
    style = "".join(registrations.values()) + "".join(css) + tokens + _palette(palette) + preview + _defaults(defaults)
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
             "small{color:#777;margin-left:8px}.frame{width:640px;height:360px;overflow:hidden;border-radius:6px;background:#fff}"
             ".frame>.slide{width:1280px;height:720px;transform:scale(.5);transform-origin:0 0;position:relative}"
             "[data-icon]:empty::after{content:'';display:block;width:100%;height:100%;box-sizing:border-box;"
             "border:1.5px dashed currentColor;border-radius:50%;opacity:.7}")
    link = f'<link rel="stylesheet" href="{html.escape(fonts_href)}">' if fonts_href else ""
    return (f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>{html.escape(kit["label"])} sheet</title>'
            f"{link}<style>{style}</style><style>{frame}</style></head><body>{''.join(cells)}</body></html>")


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("collection")
    parser.add_argument("type_steps")
    parser.add_argument("--dark", action="store_true")
    parser.add_argument("--out", default="sheet.html")
    parser.add_argument("--palette", help="defaults to palette.json beside the type steps")
    parser.add_argument("--fonts", help="defaults to fonts/fonts.css in the pack")
    arguments = parser.parse_args(argv)
    steps_path = Path(arguments.type_steps).resolve()
    steps = json.loads(steps_path.read_text(encoding="utf-8"))
    palette = json.loads(Path(arguments.palette or steps_path.with_name("palette.json")).read_text(encoding="utf-8"))
    fonts = Path(arguments.fonts or steps_path.parent.parent / "fonts" / "fonts.css").resolve()
    Path(arguments.out).write_text(sheet(arguments.collection, steps, palette, dark=arguments.dark, fonts_href=fonts.as_uri()),
                                   encoding="utf-8", newline="\n")
    print(arguments.out)


if __name__ == "__main__":
    main()
