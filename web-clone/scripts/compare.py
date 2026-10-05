"""shots/NN-side.png (reference | implementation, each 1440x4500 side by side), NN-blend.png, NN-crop.png (--crop x,y,w,h)."""
import sys
from PIL import Image
sid = sys.argv[1]
crop = tuple(int(v) for v in sys.argv[sys.argv.index('--crop') + 1].split(',')) if '--crop' in sys.argv else None
impl = Image.open(f'shots/{sid}.png').convert('RGB')
ref = Image.open(f'public/flat/{sid}.png').convert('RGB')
if ref.size != impl.size:
    print(f'[warn] size ref={ref.size} impl={impl.size}'); impl = impl.resize(ref.size)
w, h = ref.size
side = Image.new('RGB', (w * 2 + 20, h), 'red'); side.paste(ref, (0, 0)); side.paste(impl, (w + 20, 0))
side.save(f'shots/{sid}-side.png')
Image.blend(ref, impl, 0.5).save(f'shots/{sid}-blend.png')
if crop:
    x, y, cw, ch = crop
    z = max(1, min(3, 1400 // max(cw, 1)))
    a = ref.crop((x, y, x + cw, y + ch)).resize((cw * z, ch * z), Image.LANCZOS)
    b = impl.crop((x, y, x + cw, y + ch)).resize((cw * z, ch * z), Image.LANCZOS)
    o = Image.new('RGB', (cw * z, ch * z * 2 + 12), 'red'); o.paste(a, (0, 0)); o.paste(b, (0, ch * z + 12))
    o.save(f'shots/{sid}-crop.png')
print(f'[ok] {sid}')
