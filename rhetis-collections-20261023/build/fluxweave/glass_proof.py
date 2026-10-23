import sys,json
from pathlib import Path
sys.path.insert(0,'/workspace/work/reference/tools')
from preview import sheet
C='/workspace/output/glasspulse'
s=sheet(C,json.loads(Path('/workspace/work/reference/contract/type-steps.json').read_text()),json.loads(Path('/workspace/work/reference/contract/palette.json').read_text()),fonts_href='/fonts/fonts.css')
Path('/workspace/work/integration/public/glass-contract-proof.html').write_text(s)
