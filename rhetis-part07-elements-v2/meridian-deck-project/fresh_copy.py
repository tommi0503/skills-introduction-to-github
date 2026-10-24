import itertools
seed=[0]
# Every candidate is a complete business noun phrase or sentence; never truncate a word.
subjects=['금형 담당자는','야간반 관리자는','보전 책임자는','발주 담당자는','계정 관리자는','상근 운영자는','조달 실무자는','창고 관리자는','납기 조정반은','현장 정비반은']
objects=['예비 자재를 점검해','공용 계정을 정리해','금형 수명을 추적해','작업 교대를 조정해','설비 이력을 대조해','조달 조건을 검증해','납기 지연을 분류해','안전 재고를 보충해','단기 차입을 줄여','검수 서식을 통합해']
ends=['긴급 작업을 준비합니다.','고정 지출을 억제합니다.','가동 중단을 예방합니다.','오류 재발을 방지합니다.','인계 공백을 축소합니다.','보전 일정을 확정합니다.','자금 소요를 줄입니다.','점검 시간을 단축합니다.','담당 구역을 재편합니다.','유휴 자산을 매각합니다.']
phrases=['안전','보전비','금형정비','교대 운영','수주처 정비','공정별 원가','설비 이력 대조','야간반 교대 조정','고정 지출의 재분류','예비 자재의 구매 기준','현장별 금형 수명 점검','예비 자재 검수 체계 정비','납기 지연의 원인별 후속 조치','공용 계정 정리와 검수 서식 통합','상근 정비반의 긴급 작업 대응 정비','단기 차입 축소를 위한 자금 소요 조정']
qualifiers=['','분기별 ','상시 ','신규 ','전사 ','지역별 ','핵심 ','우선 ','주요 ','중기 ','야간 ','통합 ','기본 ','공동 ']
valid=lambda t:not any(normalize(t)[i:i+6] in banned for i in range(max(0,len(normalize(t))-5)))
bylen={}
def add(t):
 if valid(t):bylen.setdefault(len(t),[]).append(t)
for a,b,c in itertools.product(subjects,objects,ends):add(a+' '+b+' '+c)
for a,b in itertools.product(qualifiers,phrases):add(a+b)
# Optional neutral modifiers allow exact short-length matches without clipped syllables.
for a,b,c in itertools.product(['수주','조달','금형','검수','회수','계정','예비','야간'],[' ',' 및 ','별 ',' 중심 '],['통제','정비','진단','운용','점검','대조','추적','재편']):add(a+b+c)
for a,b,c in itertools.product(['분기','상시','공동','전사','중기','지역'],[' 운영 ',' 검수 ',' 정비 ',' 자재 '],['방침','체계','표준','계획','절차','조건']):add(a+b+c)
for sub,obj,end,adv in itertools.product(['정비반은','검수반은','조달반은','각 담당자는','현장 반장은'],['자재를 비축해','이력을 대조해','교대를 정비해','장비를 점검해','오차를 줄여'],['납기를 지킵니다.','비용을 아낍니다.','장애를 막습니다.','공백을 줄입니다.'],['','매일 ','우선 ','주기적으로 ','월별로 ','모든 현장에서 ','검수 일정을 대조한 뒤 ']):
 add(sub+' '+adv+obj+' '+end)
for sub,obj,end,adv in itertools.product(subjects,objects,ends,['매월 ','정기적으로 ','협력 공장별로 ','검수 일정을 대조한 뒤 ']):
 add(sub+' '+adv+obj+' '+end)
for n in range(2,25):
 if n not in bylen:
  # A grammatical nominal phrase of the target length, assembled from complete modifiers.
  for k in range(1,5):
   for pref in itertools.product(['상시 ','공동 ','전사 ','주요 ','분기별 '],repeat=k):
    for end in ['검수','정비','자재','담당자','재고량','보전비','운영 체계','현장 점검']:
     t=''.join(pref)+end
     if len(t)==n:add(t)
    if n in bylen:break
   if n in bylen:break

def composed(n):
 if n in bylen:return bylen[n][seed[0]%len(bylen[n])]
 # Compose complete sentences in a readable paragraph, preserving exact character count.
 lens=sorted(k for k in bylen if any(t.endswith('.') for t in bylen[k]))
 for a in lens:
  b=n-a-1
  if b in bylen and any(t.endswith('.') for t in bylen[b]):
   aa=[t for t in bylen[a] if t.endswith('.')];bb=[t for t in bylen[b] if t.endswith('.')];t=aa[seed[0]%len(aa)]+' '+bb[(seed[0]+3)%len(bb)]
   if valid(t):return t
 for a in lens:
  if n-a-1>=50:
   try:
    aa=[t for t in bylen[a] if t.endswith('.')];t=aa[seed[0]%len(aa)]+' '+composed(n-a-1)
   except ValueError:continue
   if valid(t):return t
 raise ValueError(('No complete fresh phrase at length',n))
def fresh(src):
 seed[0]+=1;t=src.strip()
 if not t:return ''
 if re.fullmatch(r'[\d.,%+−–/: QxX년월분기]+',t):return html.escape(t)
 if len(t)<=1:return html.escape(t)
 return html.escape(composed(len(t)))
