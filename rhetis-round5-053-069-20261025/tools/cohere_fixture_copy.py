"""Replace unrelated demo contexts with a coherent cold-chain operation; preserve golden fixtures."""
import hashlib,json
from pathlib import Path
from static_audit import GOLDEN
ROOT=Path(__file__).resolve().parents[1]
REPLACEMENTS={
 '실내농장 급수량을 조절합니다.':'냉장물류 배차량을 조절합니다.',
 '도서관 좌석 배정을 정비합니다.':'배송점 적재 순서를 정비합니다.',
 '원예 작물의 수분을 관찰합니다.':'냉장 화물의 온도를 관찰합니다.',
 '공항 수하물 동선을 점검합니다.':'창고 출입구 동선을 점검합니다.',
 '양조 설비의 온도를 기록합니다.':'운송 장비의 온도를 기록합니다.',
 '지역 박람회 접수를 준비합니다.':'지역 배송점 인수를 준비합니다.',
 '공방 자재의 낭비를 줄입니다.':'포장 자재의 낭비를 줄입니다.',
 '재배 설비 점검':'냉장 설비 점검',
 '예약 좌석 배분':'운송 물량 배분',
 '공방 자재 절약':'포장 자재 절약',
 '현장 소음 관찰':'현장 온도 관찰',
 '전시 출입 관리':'창고 출입 관리',
 '항공 화물 배정':'운송 화물 배정',
 '전시 현장 조정자':'물류 현장 조정자'}
if __name__=='__main__':
 rows=[]
 for c in json.loads((ROOT/'collections.json').read_text()):
  for f in (ROOT/c['id']/'elements').glob('*/fixtures/*.html'):
   leaf=f.parents[1].name
   if leaf in GOLDEN and f.stem in GOLDEN[leaf][1]:continue
   if c['id']=='cinder-pulse'and leaf in ['card','callout']:continue
   before=f.read_text();after=before
   for a,b in REPLACEMENTS.items():
    assert len(a)==len(b),(a,b)
    after=after.replace(a,b)
   if after!=before:
    f.write_text(after);rows.append({'path':str(f.relative_to(ROOT)),'beforeSHA256':hashlib.sha256(before.encode()).hexdigest(),'afterSHA256':hashlib.sha256(after.encode()).hexdigest()})
 (ROOT/'fixture-copy-revision.json').write_text(json.dumps({'purpose':'Coherent cold-chain operations; equal character counts and unchanged markup, values, breaks and emphasis. Golden fixture data excluded. Cinder card/callout handled separately.','files':rows},ensure_ascii=False,indent=2));print(len(rows),'fixtures revised')
