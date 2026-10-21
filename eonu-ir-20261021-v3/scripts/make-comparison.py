"""Build a side-by-side comparison when the preserved v2 folder is available."""
from pathlib import Path
import io
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
OLD = ROOT.parent / 'eonu-ir-20261021-v2'
if not OLD.exists():
    raise SystemExit('Comparison requires sibling eonu-ir-20261021-v2 from the repository.')
font = TTFont(ROOT / 'assets/fonts/PretendardVariable.woff2')
font.flavor = None
buf = io.BytesIO()
font.save(buf)
title = ImageFont.truetype(io.BytesIO(buf.getvalue()), 28)
label = ImageFont.truetype(io.BytesIO(buf.getvalue()), 20)
sheet = Image.new('RGB', (1376, 1352), '#edf0f4')
draw = ImageDraw.Draw(sheet)
draw.text((32, 24), 'EONU  /  v2 → v3', font=title, fill='#202532')
draw.text((32, 80), '이전 v2', font=label, fill='#777e8e')
draw.text((704, 80), '개선 v3', font=label, fill='#477cff')
for row, (page, heading) in enumerate([('02', '문제 · 두 장면으로'), ('06', '데모 · 확인 화면에 집중'), ('11', '투자 · 한 숫자와 세 목적')]):
    y = 128 + row * 408
    for x, source in [(32, OLD), (704, ROOT)]:
        image = Image.open(source / 'previews/design' / (page + '.png')).convert('RGB')
        image = image.resize((640, 360), Image.Resampling.LANCZOS)
        sheet.paste(image, (x, y))
    draw.text((704, y + 372), page + '  ' + heading, font=label, fill='#777e8e')
sheet.save(ROOT / 'previews/eonu-v2-v3-comparison.jpg', quality=94)
print('Created eonu-v2-v3-comparison.jpg with bundled Pretendard labels.')
