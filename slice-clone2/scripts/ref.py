"""Stack reference slides vertically at full size: python3 scripts/ref.py NN S [S ...] -> shots/NN-ref.png"""
import sys, os
from PIL import Image
sid, sel = sys.argv[1], [int(s) for s in sys.argv[2:]]
os.makedirs('shots', exist_ok=True)
ims = [Image.open(f'public/reference/{sid}/{i:02d}.webp').convert('RGB') for i in sel]
out = Image.new('RGB', (1280, len(ims) * 728 - 8), 'red')
for k, im in enumerate(ims): out.paste(im, (0, k * 728))
out.save(f'shots/{sid}-ref.png'); print('[ok]', f'shots/{sid}-ref.png')
