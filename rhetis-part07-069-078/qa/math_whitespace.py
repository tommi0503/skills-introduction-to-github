from pathlib import Path
import re,json
R=Path(__file__).resolve().parent.parent
for P in R.glob('*-project'):
 kid=P.name.removesuffix('-project');found=[]
 for p in (P/kid).rglob('*.css'):
  text=p.read_text()
  for m in re.finditer(r'calc\(',text):
   pos=m.end();depth=1;i=pos
   while i<len(text) and depth:
    if text[i]=='(':depth+=1
    elif text[i]==')':depth-=1
    i+=1
   expression=text[pos:i-1];masked=re.sub(r'var\([^)]*\)','V',expression)
   hits=[]
   for op in re.finditer(r'(?<=[\d%V)])(\s*)([+-])(\s*)(?=[\dV.(])',masked):
    if not op.group(1) or not op.group(3):hits.append(op.group())
   if hits:found.append({'file':str(p.relative_to(P)),'expression':expression,'suspectOperators':hits})
 (R/'qa'/(kid+'-math-whitespace.json')).write_text(json.dumps(found,ensure_ascii=False,indent=2))
 print(kid,len(found));
 for x in found[:15]:print(x['file'],x['expression'])
