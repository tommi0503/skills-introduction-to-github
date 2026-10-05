"""Flattens a (photographed / angled) leaflet reference into the flat sheet geometry.

Usage:
  python3 scripts/rectify.py NN --top x,y x,y ... --bottom x,y x,y ...
Give the leaflet's TOP edge points (left corner, each fold, right corner) and the
matching BOTTOM edge points, in reference pixel coordinates. N panels need N+1 points
on each edge. Each panel quad is perspective-warped to PANEL size (480x1018), so folds
and perspective are removed. Output: public/flat/NN.png (+ points saved to
scripts/corners/NN.json so the flattening is reproducible).
"""
import json, os, sys
import numpy as np
from PIL import Image

PW, PH = 480, 1018

def coeffs(src, dst):
    # solve perspective transform mapping dst(output) -> src(input) for PIL
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); B.append(u)
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); B.append(v)
    return np.linalg.solve(np.array(A, float), np.array(B, float)).tolist()

def parse(tokens):
    return [tuple(float(v) for v in t.split(',')) for t in tokens]

def main():
    sid = sys.argv[1]
    args = sys.argv[2:]
    if '--top' in args:
        ti, bi = args.index('--top'), args.index('--bottom')
        top = parse(args[ti + 1:bi]) if ti < bi else parse(args[ti + 1:])
        bottom = parse(args[bi + 1:ti]) if bi < ti else parse(args[bi + 1:])
        os.makedirs('scripts/corners', exist_ok=True)
        json.dump({'top': top, 'bottom': bottom}, open(f'scripts/corners/{sid}.json', 'w'))
    else:
        d = json.load(open(f'scripts/corners/{sid}.json'))
        top, bottom = [tuple(p) for p in d['top']], [tuple(p) for p in d['bottom']]
    assert len(top) == len(bottom) >= 2
    n = len(top) - 1
    ref = Image.open(f'public/reference/{sid}.jpg').convert('RGB')
    out = Image.new('RGB', (PW * n, PH), 'white')
    for i in range(n):
        src = [top[i], top[i + 1], bottom[i + 1], bottom[i]]
        dst = [(0, 0), (PW, 0), (PW, PH), (0, PH)]
        panel = ref.transform((PW, PH), Image.PERSPECTIVE, coeffs(src, dst), Image.BICUBIC)
        out.paste(panel, (PW * i, 0))
    os.makedirs('public/flat', exist_ok=True)
    out.save(f'public/flat/{sid}.png')
    print(f'[ok] public/flat/{sid}.png {out.size}')

main()
