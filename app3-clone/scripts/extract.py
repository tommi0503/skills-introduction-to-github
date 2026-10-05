"""Cuts every phone screen out of a reference image and normalises it to SCREEN size.

Usage:  python3 scripts/extract.py NN            (auto-detect, then saves scripts/boxes/NN.json)
        python3 scripts/extract.py NN --boxes "x,y,w,h x,y,w,h ..."   (manual override, saved)
        python3 scripts/extract.py NN --from-json                     (re-use saved boxes)
Outputs public/flat/NN.png — the screens side by side at 390x844 with GAP px between,
exactly the layout the implementation renders, so they can be compared 1:1.
Boxes must be the screen's outer edge (the rounded white/coloured phone shape).
"""
import json, os, sys
import numpy as np
from PIL import Image

SW, SH, GAP, PAD = 390, 844, 40, 40
PITCH = 293.6

def runs(mask, minlen):
    out, s = [], None
    for i, v in enumerate(list(mask) + [False]):
        if v and s is None: s = i
        if not v and s is not None:
            if i - s >= minlen: out.append((s, i))
            s = None
    return out

def auto(img):
    a = np.asarray(img.convert('L')).astype(int)
    h, w = a.shape
    bg = np.median(np.concatenate([a[:, :3].ravel(), a[:, -3:].ravel()]))
    diff = np.abs(a - bg) > 14
    segs = [s for s in runs(diff.mean(0) > 0.5, 200) if 255 <= s[1] - s[0] <= 285]
    pw = int(round(np.median([b - a_ for a_, b in segs]))) if segs else 270
    x0 = segs[0][0] - round((segs[0][0] - 0) // PITCH) * PITCH if segs else 5
    n = int(round((w - x0 - pw) / PITCH)) + 1
    tops, bots = [], []
    for a_, b in segs:
        r = runs(diff[:, a_ + 20:b - 20].mean(1) > 0.5, 400)
        if r and r[-1][1] - r[0][0] > 540: tops.append(r[0][0]); bots.append(r[-1][1])
    top = int(np.median(tops)) if tops else 12
    bot = int(np.median(bots)) if bots else min(h, top + int(pw * 844 / 390))
    return [(int(round(x0 + i * PITCH)), top, pw, bot - top) for i in range(n)]

def main():
    sid = sys.argv[1]
    img = Image.open(f'public/reference/{sid}.jpg').convert('RGB')
    os.makedirs('scripts/boxes', exist_ok=True)
    jp = f'scripts/boxes/{sid}.json'
    if '--boxes' in sys.argv:
        boxes = [tuple(int(v) for v in t.split(',')) for t in sys.argv[sys.argv.index('--boxes') + 1].split()]
    elif '--from-json' in sys.argv:
        boxes = [tuple(b) for b in json.load(open(jp))]
    else:
        boxes = auto(img)
    json.dump(boxes, open(jp, 'w'))
    n = len(boxes)
    out = Image.new('RGB', (PAD * 2 + n * SW + (n - 1) * GAP, PAD * 2 + SH), (17, 17, 17))
    for i, (x, y, w, h) in enumerate(boxes):
        crop = img.crop((x, y, x + w, y + h)).resize((SW, SH), Image.LANCZOS)
        out.paste(crop, (PAD + i * (SW + GAP), PAD))
    os.makedirs('public/flat', exist_ok=True)
    out.save(f'public/flat/{sid}.png')
    print(f'[ok] {sid} boxes={boxes} -> public/flat/{sid}.png {out.size}')

main()
