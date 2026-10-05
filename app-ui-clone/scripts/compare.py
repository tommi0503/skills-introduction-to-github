"""Builds comparison images for one showcase.

shots/<id>-side.png   reference | implementation (stacked vertically when wide)
shots/<id>-blend.png  50% overlay — misalignments show as ghosting
shots/<id>-crop.png   (with --crop x,y,w,h) zoomed side-by-side of a region
"""
import sys
from PIL import Image, ImageDraw

sid = sys.argv[1]
crop = None
if '--crop' in sys.argv:
    crop = tuple(int(v) for v in sys.argv[sys.argv.index('--crop') + 1].split(','))

ref = Image.open(f'public/reference/{sid}.jpg').convert('RGB')
impl = Image.open(f'shots/{sid}.png').convert('RGB')
if impl.size != ref.size:
    print(f'[warn] size mismatch ref={ref.size} impl={impl.size}; resizing impl')
    impl = impl.resize(ref.size)

w, h = ref.size
gap = 12
if w > h * 1.4:
    side = Image.new('RGB', (w, h * 2 + gap), 'red')
    side.paste(ref, (0, 0)); side.paste(impl, (0, h + gap))
else:
    side = Image.new('RGB', (w * 2 + gap, h), 'red')
    side.paste(ref, (0, 0)); side.paste(impl, (w + gap, 0))
side.save(f'shots/{sid}-side.png')
Image.blend(ref, impl, 0.5).save(f'shots/{sid}-blend.png')

if crop:
    x, y, cw, ch = crop
    box = (x, y, x + cw, y + ch)
    z = max(1, min(4, 900 // max(cw, 1)))
    a = ref.crop(box).resize((cw * z, ch * z), Image.LANCZOS)
    b = impl.crop(box).resize((cw * z, ch * z), Image.LANCZOS)
    out = Image.new('RGB', (cw * z * 2 + gap, ch * z), 'red')
    out.paste(a, (0, 0)); out.paste(b, (cw * z + gap, 0))
    out.save(f'shots/{sid}-crop.png')
print(f'[ok] {sid}')
