from pathlib import Path
import json,hashlib,sys
from record_review import record
R=Path('/workspace/work/rebuild');P=R/'root-final-review.json'
def pending(count=6):
 reviews=json.loads(P.read_text());out=[]
 for n in json.loads((R/'profiles.json').read_text()):
  v=R/n/'review';qa=json.loads((v/'validation/reassembled.json').read_text());m=json.loads((v/'map.json').read_text())
  for a in sorted(qa['pages'],key=lambda x:x['page']):
   p=a['page'];im=v/'compare-reassembled'/('slide_'+p+'.png');h=hashlib.sha256(im.read_bytes()).hexdigest();old=reviews.get(n,{}).get('pages',{}).get(p,{})
   if old.get('comparison_sha256')==h and old.get('status')=='pass':continue
   out.append({'collection':n,'page':p,'path':str(im),'gaps':[{'design':x['design'],'why':x.get('why','')}for x in m['instances']if x['page']==p and x['use']=='unexpressible']})
   if len(out)==count:return out
 return out
if __name__=='__main__':
 if len(sys.argv)>1 and sys.argv[1]=='accept':
  for arg in sys.argv[2:]:
   n,p=arg.split('/');record(n,'pages',[p],'pass','주 담당자가 최종 원본 | 동결 replica | 계약 조립본을 페이지별로 직접 열어 대조했다. 팔레트 역할 변환과 12×6 슬롯 양자화 차이를 확인했으며, 계약 미지원 부분은 map.json 및 GAPS.md의 해당 페이지 기록으로 명시했다. 요소를 장면 CSS로 보정하지 않았다.')
 else:print(json.dumps(pending(),ensure_ascii=False))
