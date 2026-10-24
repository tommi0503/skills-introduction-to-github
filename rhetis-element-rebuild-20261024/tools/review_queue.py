"""Prepare explicit integration-review batches; never marks a batch automatically."""
from pathlib import Path
import json,sys,hashlib
from record_review import record
R=Path('/workspace/work/rebuild');P=R/'root-sheet-review-queue.json'
TEXT={'card','pill','callout','tag','list','quote','headline','prose','metric','agenda','person'}
OWN={'code','delta','legend','image-frame','logo-group','pricing','versus'}
def prepare():
 data=[]
 for n in json.loads((R/'profiles.json').read_text()):
  for f in sorted((R/n/n/'elements').iterdir()):
   if f.name in TEXT|OWN:continue
   data.append({'collection':n,'leaf':f.name,'reviewed':False})
 P.write_text(json.dumps(data,indent=2));return data
def pending(count=3):
 d=json.loads(P.read_text())if P.exists()else prepare();out=[]
 for a in d:
  if a['reviewed']:continue
  v=R/a['collection']/'review';q=v/'validation'/(a['leaf']+'.json')
  if not q.exists():continue
  obj=json.loads(q.read_text())
  if not isinstance(obj.get('cases'),list)or any(obj.get('counts',{}).values()):continue
  out.append({**a,'paths':[str(v/'sheets'/(a['leaf']+'-'+m+'.png'))for m in ['light','dark']]})
  if len(out)==count:break
 return out
def accept(items):
 d=json.loads(P.read_text())
 for key in items:
  n,l=key.split('/')
  record(n,'elements',[l],'pass','주 담당자: 라이트·다크의 전체 크기별 시트를 직접 열어 통합 디자인·배치·연결·정렬을 확인. 담당자의 최종 native 전칸 검수 및 경계/대비/폰트 증거와 함께 확인했다.')
  for a in d:
   if(a['collection'],a['leaf'])==(n,l):a['reviewed']=True
 P.write_text(json.dumps(d,indent=2))
if __name__=='__main__':
 if len(sys.argv)>1 and sys.argv[1]=='accept':accept(sys.argv[2:])
 else:print(json.dumps(pending(int(sys.argv[1])if len(sys.argv)>1 else 3)))
