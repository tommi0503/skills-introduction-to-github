"""Side-by-side helper: python3 scripts/view.py NN [slideIndex]
Writes shots/NN-view.png = reference image (left, scaled to 1100 wide) and the rendered slide(s) (right)."""
import sys
from PIL import Image
sid = sys.argv[1]
ref = Image.open(f'public/reference/{sid}.jpg').convert('RGB')
impl = Image.open(f'shots/{sid}.png').convert('RGB')
if len(sys.argv) > 2:
    i = int(sys.argv[2]); cols = 2; x = 40 + (i % cols) * 1320; y = 40 + (i // cols) * 760
    impl = impl.crop((x, y, x + 1280, y + 720))
def fit(im, w): return im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
a, b = fit(ref, 1100), fit(impl, 1100)
out = Image.new('RGB', (2220, max(a.height, b.height)), 'red'); out.paste(a, (0, 0)); out.paste(b, (1120, 0))
out.save(f'shots/{sid}-view.png'); print(f'[ok] shots/{sid}-view.png')
