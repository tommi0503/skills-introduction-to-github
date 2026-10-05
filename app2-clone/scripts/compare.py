"""shots/NN-side.png (extracted ref screens above, implementation below), NN-blend.png, NN-crop.png (--crop x,y,w,h)."""
import sys
from PIL import Image

sid = sys.argv[1]
crop = tuple(int(v) for v in sys.argv[sys.argv.index('--crop') + 1].split(',')) if '--crop' in sys.argv else None
impl = Image.open(f'shots/{sid}.png').convert('RGB')
try:
    ref = Image.open(f'public/flat/{sid}.png').convert('RGB')
except FileNotFoundError:
    print(f'[warn] no public/flat/{sid}.png — run scripts/extract.py first'); sys.exit(0)
if ref.size != impl.size:
    print(f'[warn] size ref={ref.size} impl={impl.size}; resizing ref'); ref = ref.resize(impl.size)
w, h = impl.size
side = Image.new('RGB', (w, h * 2 + 12), 'red'); side.paste(ref, (0, 0)); side.paste(impl, (0, h + 12))
side.save(f'shots/{sid}-side.png')
Image.blend(ref, impl, 0.5).save(f'shots/{sid}-blend.png')
if crop:
    x, y, cw, ch = crop
    z = max(1, min(4, 900 // max(cw, 1)))
    a = ref.crop((x, y, x + cw, y + ch)).resize((cw * z, ch * z), Image.LANCZOS)
    b = impl.crop((x, y, x + cw, y + ch)).resize((cw * z, ch * z), Image.LANCZOS)
    o = Image.new('RGB', (cw * z * 2 + 12, ch * z), 'red'); o.paste(a, (0, 0)); o.paste(b, (cw * z + 12, 0))
    o.save(f'shots/{sid}-crop.png')
print(f'[ok] {sid}')
