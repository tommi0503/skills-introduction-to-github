"""Record observations only after a final comparison has been opened individually."""
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[1]
file = root / 'review/main-review.json'
report = json.loads(file.read_text())
pages = {f"{p['deck']}-{p['slide']}": p for p in report['pages']}
for item in json.loads(sys.argv[1]):
    deck, slide = item['key'].split('-')
    meta = json.loads((root / f'comparisons/final/{deck}.json').read_text())
    capture = next(s for s in meta['slides'] if s['id'] == slide)
    pair = f'comparisons/final/{deck}-{slide}.jpg'
    pages[item['key']] = {
        'deck': deck, 'slide': slide, 'finalComparisonViewed': True,
        'comparisonFile': pair, 'finalPngSha256': capture['pngSha256'],
        'finalComparisonSha256': hashlib.sha256((root / pair).read_bytes()).hexdigest(),
        'definitionHash': meta['definitionHash'], 'rendererHash': meta['rendererHash'],
        'observations': item['observations'], 'remainingDifferences': item.get('differences', []),
        'automaticFindings': capture['findings'],
        'reviewedAt': datetime.now(timezone.utc).isoformat(),
    }
report['pages'] = [pages[k] for k in sorted(pages)]
report['pagesIndividuallyViewed'] = len(pages)
file.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(f'Individual final comparisons recorded: {len(pages)}/159')
