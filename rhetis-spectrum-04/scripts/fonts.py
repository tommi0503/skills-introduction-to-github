from pathlib import Path
import re,shutil
root=Path(__file__).resolve().parent.parent;out=root/'public/fonts';css=[]
for pkg in sorted((root/'node_modules/@fontsource').iterdir()):
 if pkg.name not in ['anton','bebas-neue','jua','roboto-condensed']:continue
 dest=out/pkg.name;dest.mkdir(exist_ok=True)
 for w in ([300,400,800] if pkg.name=='roboto-condensed' else [400]):
  source=pkg/f'{w}.css'
  if not source.exists():continue
  text=source.read_text()
  for rel in re.findall(r'url\(([^)]+)\)',text):
   if (pkg/rel).exists():
    target=dest/Path(rel).name;shutil.copy2(pkg/rel,target)
   text=text.replace(rel,f'./{pkg.name}/{Path(rel).name}')
  css.append(text)
pkg=root/'node_modules/@fontsource-variable/bodoni-moda';dest=out/'bodoni-moda';dest.mkdir(exist_ok=True)
text=(pkg/'index.css').read_text()
for rel in re.findall(r'url\(([^)]+)\)',text):
 shutil.copy2(pkg/rel,dest/Path(rel).name);text=text.replace(rel,f'./bodoni-moda/{Path(rel).name}')
css.append(text.replace('Bodoni Moda Variable','Bodoni Moda'))
src=root/'node_modules/pretendard/dist/web/variable/woff2/PretendardVariable.woff2';shutil.copy2(src,out/src.name)
css.append("@font-face{font-family:Pretendard;src:url('./PretendardVariable.woff2') format('woff2');font-weight:100 900;font-display:block}")
for w in [400,700,800]:
 if (out/f'NanumSquareRound/{w}.woff2').exists():css.append(f"@font-face{{font-family:NanumSquareRound;src:url('./NanumSquareRound/{w}.woff2');font-weight:{w};font-display:block}}")
(out/'fonts.css').write_text('\n'.join(css))
shutil.copy2(root/'node_modules/lucide/dist/umd/lucide.js',root/'public/lucide.js')
