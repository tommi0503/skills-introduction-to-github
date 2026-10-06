"""Reference vs render: python3 scripts/view.py NN [S ...] [--half]
Writes shots/NN-view.png: for each slide, the reference (top) above the render (bottom).
With --half every pair is half size and pairs are tiled 2 per row (overview)."""
import sys, os
from PIL import Image
args = [a for a in sys.argv[1:] if not a.startswith('--')]; half = '--half' in sys.argv
sid, sel = args[0], args[1:]
refdir = f'public/reference/{sid}'
n = len([f for f in os.listdir(refdir) if f.endswith('.webp')])
sel = [int(s) for s in sel] or list(range(1, n + 1))
def pair(i):
    ref = Image.open(f'{refdir}/{i:02d}.webp').convert('RGB')
    p = f'shots/{sid}/{i:02d}.png'
    imp = Image.open(p).convert('RGB') if os.path.exists(p) else Image.new('RGB', (1280, 720), 'red')
    im = Image.new('RGB', (1280, 1448), 'red'); im.paste(ref, (0, 0)); im.paste(imp, (0, 728))
    return im.resize((640, 724)) if half else im
ims = [pair(i) for i in sel]
cols = 2 if half and len(ims) > 1 else 1
w, h = ims[0].size
out = Image.new('RGB', (cols * w + (cols - 1) * 12, ((len(ims) + cols - 1) // cols) * (h + 12)), 'black')
for k, im in enumerate(ims): out.paste(im, ((k % cols) * (w + 12), (k // cols) * (h + 12)))
out.save(f'shots/{sid}-view.png'); print(f'[ok] shots/{sid}-view.png', out.size)
