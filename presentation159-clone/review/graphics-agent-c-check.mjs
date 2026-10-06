// Live browser audit and page records; no second agent PNG/comparison capture.
import {createServer} from 'vite'
import {chromium} from 'playwright-core'
import {readFile,writeFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import {auditSlide} from '../scripts/browser-audit.mjs'
const assignment=JSON.parse(await readFile(new URL('./assignment-c.json',import.meta.url),'utf8'))
const old=JSON.parse(await readFile(new URL('./agent-c.json',import.meta.url),'utf8')).pages
const after=new Set(['d38-s010','d39-s001','d43-s003','d43-s007','d45-s001','d47-s011','d48-s003','d48-s004','d50-s001','d50-s006','d50-s008','d50-s009','d53-s005','d53-s010'])
const restored={
 'd38-s010':['큰 추상 잎 3개를 SVG 곡선과 푸른 회색→주황 그라데이션으로 복원. 하단 잎은 1차 비교 뒤 transparent fade로 보정.'],
 'd39-s001':['teal→밝은 청록색 배경과 하단 검정·분홍 흐림을 CSS radial/linear gradient로 복원. 원본에 독립적인 기업 격자 장식은 없어 추가하지 않음.'],
 'd41-s001':['크림색 종이 바탕·불규칙 얼룩·grain을 SVG/CSS로 복원.','빈티지 가로등·책 더미·꽃 가지·검은 장식 무늬를 분리된 SVG 컴포넌트로 복원.'],
 'd43-s001':['머리 윤곽·분홍 뇌·보라색 체크보드·꽃/잎 가지·두 모서리 꽃을 SVG path로 복원.','대학 로고의 책과 Ψ를 SVG로 복원.'],
 'd43-s003':['사진의 유기적 곡선 마스크 유지. 1차 비교 뒤 얇은 검정 곡선 경계선도 별도 SVG path로 복원.'],
 'd43-s007':['분홍 머리·보라색 하트·Ψ·꽃/잎 가지를 SVG로 복원. 사진의 둥근 경계선은 1차 비교 뒤 SVG arc로 복원.'],
 'd43-s008':['머리 윤곽·분홍 원형 미로·열쇠·열쇠구멍·보라색 잎 가지를 SVG path로 복원.'],
 'd44-s008':['왼쪽의 푸른 회색 soft 배경을 CSS radial/linear gradient로 복원.'],
 'd45-s001':['회색 큰 배경 영역을 제거하고 붉은 흐림 곡선 두 갈래를 SVG path+CSS blur로 복원.','아래쪽 연분홍 radial fade와 procedural grain을 복원. 1차 비교 뒤 grain 농도를 보정.'],
 'd47-s007':['양쪽 cream색 X 장식을 둥근 SVG stroke로 복원.'],
 'd47-s010':['cream색 X 장식 2개를 둥근 SVG stroke로 복원.'],
 'd47-s011':['cream색 8갈래 꽃 장식을 SVG로 복원. 1차 비교 뒤 직선 살 대신 부드러운 유기적 곡선으로 보정.'],
 'd48-s003':['사진 아래의 종이 테이프를 SVG로 보존하고 1차 비교 뒤 양 끝의 찢긴 윤곽을 구현.'],
 'd48-s004':['사진 위의 종이 테이프를 SVG로 보존하고 1차 비교 뒤 양 끝의 찢긴 윤곽을 구현.'],
 'd49-s006':['62.5%/25%/12.5% 원형 차트를 기존 벡터로 유지하고 개별 비교 확인.'],
 'd50-s001':['배경의 반복 곡면과 transparent fade를 CSS gradient로 복원.','연두색 하프톤을 SVG circles로 복원하고 검정 별 장식을 SVG stroke로 복원.','1차 비교 뒤 큰 마블링 영역도 회색에서 SVG turbulence/displacement 기반 procedural marble로 복원.'],
 'd50-s006':['반복 곡면과 transparent fade를 CSS gradient로 복원. 우측 녹색 하프톤을 SVG circles로 복원.'],
 'd50-s008':['반복 곡면과 transparent fade를 CSS gradient로 복원. 하단 녹색 하프톤을 SVG circles로 복원.'],
 'd50-s009':['반복 곡면과 transparent fade를 CSS gradient로 복원. 우측/하단 녹색 하프톤을 SVG circles로 복원.'],
 'd50-s010':['왼쪽 상단과 오른쪽 하단의 작은 반복 곡면, transparent fade를 CSS gradient로 복원.'],
 'd50-s011':['오른쪽 반복 곡면과 transparent fade를 CSS gradient로 복원. 연두색 둥근 8갈래 별을 SVG stroke로 복원.'],
 'd52-s002':['사진 아래 작은 카드의 아래쪽 밝음→위쪽 transparent fade를 복원.'],
 'd52-s005':['좌상단 카드의 왼쪽 밝음→오른쪽 transparent fade, 하단 카드의 아래쪽 밝음→위쪽 transparent fade를 복원.'],
 'd52-s006':['중앙 카드의 위쪽 밝음→아래쪽 transparent fade를 복원.'],
 'd52-s009':['좌상단 카드의 위쪽 밝음→아래쪽 transparent fade를 복원.'],
 'd52-s010':['좌하단 카드의 왼쪽 밝음→오른쪽 transparent fade와 우측 카드의 아래쪽 밝음→위쪽 transparent fade를 복원.'],
 'd53-s002':['오른쪽 위 큰 흰 물결의 U 곡선을 SVG Bezier로 재현.'],
 'd53-s005':['오른쪽 아래 흰 물결을 SVG Bezier로 재현. 1차 비교 뒤 별도의 작은 물결 geometry로 크기와 상단 위치를 보정.'],
 'd53-s007':['왼쪽 흰 물결의 끝단과 안쪽 곡선을 SVG Bezier로 재현.'],
 'd53-s010':['오른쪽 아래 노란 물결을 SVG Bezier로 재현. 1차 비교 뒤 내부 골의 높이를 보정.'],
 'd53-s011':['기존 벡터 리본 장식을 유지하고 개별 비교 확인.'],
 'd53-s014':['기존 벡터 리본 장식을 유지하고 개별 비교 확인.']
}
const commonRestored={d40:['기존 격자선·둥근 프레임·chip 구현을 유지하고 원본/결과에서 개별 확인.'],d42:['기존 선·카드 테두리와 Lucide 로고 구현을 유지하고 개별 확인.'],d46:['기존 라임색 강조 바를 유지하고 개별 확인.'],d47:['기존 원형 pill 장식을 유지하고 개별 확인.'],d49:['기존 헤더/푸터의 얇은 선과 텍스트 구현을 유지하고 개별 확인.']}
const differences={
 d38:['잎 곡선의 접점과 그라데이션 위치는 벡터 근사이며 원본의 부드러운 grain과 완전히 같지는 않음.'],
 d39:['전체 흐림 배경의 밝기 분포는 CSS 근사. League Spartan은 원본 폰트 추정이며 글리프 폭이 조금 다름.'],
 d40:['제목과 본문 글리프 폭은 실제 로드된 추정 글꼴 사용으로 소폭 차이가 남음. 사진 위 밝은 글자는 회색 사진 placeholder에서 대비가 낮음.'],
 d41:['종이 얼룩, 꽃, 가로등, 책, 빈티지 무늬는 재사용 SVG 근사로 원본의 세밀한 텍스처와 불규칙성이 남음. Bodoni Moda 제목 글리프도 추정.'],
 d42:['로고는 Lucide 근사이며 Barlow/DM Sans/Roboto Condensed를 실제 로드. 작은 본문 글리프 폭은 소폭 차이.'],
 d43:['뇌/꽃/잎/미로 선화는 SVG로 근사하여 세밀한 손그림 선의 굴곡과 꽃잎 모양이 다름. Forum/Comic Neue 실제 폰트를 사용하며 원본 글리프와 일부 차이.'],
 d44:['왼쪽 배경의 푸른 회색 밝기 분포는 CSS 근사.'],
 d45:['흐림 곡선의 굴곡·grain 텍스처·색 농도는 SVG/CSS 근사. 로고는 Lucide 근사.'],
 d46:['글꼴 폭과 줄간격의 미세 차이가 남음. 배경 사진 위 흰 글자는 회색 placeholder에서 대비가 낮음.'],
 d47:['원본 좁은 제목 글꼴을 실제 로드된 Bebas Neue로 추정해 글리프 모양·폭에 차이. 크림 장식의 곡률은 SVG 근사.'],
 d48:['테이프의 찢긴 윤곽은 procedural SVG 근사이며 원본 투명 종이의 표면 질감은 생략.'],
 d49:['원본 serif 제목을 실제 로드된 Tinos로 추정해 일부 글리프와 폭이 다름. 작은 본문은 원본과 소폭 줄바꿈 차이.'],
 d50:['반복 곡면의 투명도·하프톤 점 배열은 SVG/CSS 근사. 재현된 글꼴 폭에도 소폭 차이.'],
 d51:['회색 placeholder는 원본 빈티지 기기·사진의 형태와 질감을 단순화함. 원본 기울어진 사진 구도를 펴서 페이지 자체는 왜곡하지 않음.'],
 d52:['카드의 transparent fade와 Lucide 로고는 근사. 일부 제목 글리프 폭·크기에 소폭 차이.'],
 d53:['물결과 리본은 SVG 곡선 근사. 원본 제목 폰트 추정에 따른 글리프/폭 차이가 남음.']
}
const server=await createServer({server:{host:'127.0.0.1',port:0},logLevel:'error'})
await server.listen()
const browser=await chromium.launch({executablePath:'/usr/bin/chromium'})
const page=await browser.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1})
const url='http://127.0.0.1:'+server.httpServer.address().port,rows=[],audits=[]
try {
 await page.goto(url,{waitUntil:'networkidle'})
 const definitions=await page.evaluate(async()=>{const m=await import('/src/registry.ts');return m.decks})
 for(const item of assignment){
  const deck=definitions.find(d=>d.id===item.id),definitionHash=createHash('sha256').update(JSON.stringify(deck)).digest('hex')
  const capture=JSON.parse(await readFile(new URL('../comparisons/graphics-agent-c/'+deck.id+'.json',import.meta.url),'utf8'))
  for(const source of item.slides){
   const slide=deck.slides.find(s=>s.id===source.id),key=deck.id+'-'+slide.id,previous=old.find(p=>p.deck===deck.id&&p.slide===slide.id)
   await page.goto(url+'/#/slide/'+deck.id+'/'+slide.id,{waitUntil:'networkidle'})
   const audit=await auditSlide(page);audits.push({deck:deck.id,slide:slide.id,definitionHash,...audit})
   const photos=slide.elements.filter(e=>e.kind==='image').map(e=>e.text??e.label??'photographic content')
   const reasons=photos.map(label=>({label,reason:'원본의 촬영 사진·복잡한 회화 사진 또는 기기 화면 영역으로 확인하여 연한 회색 단색 placeholder를 유지. 단순 도형/장식과 분리함.'}))
   const diff=[...(differences[deck.id]??[])]
   if(key==='d50-s001')diff.push('마블링은 1차 비교 이후 공통 marble SVG로 복원. 원본의 액체 결 방향·세부 무늬는 난수 기반 근사이며 주 에이전트 최종 2차 확인 필요.')
   if(deck.id==='d43'&&(slide.id==='s003'||slide.id==='s007'))diff[0]='사진의 SVG 곡선 경계선은 1차 비교 뒤 추가. Comic Neue/Forum 실제 폰트의 일부 글리프 폭 차이가 남음.'
   rows.push({deck:deck.id,slide:slide.id,originalViewed:true,comparisonViewed:true,originalPath:'public/reference/'+deck.id+'/'+slide.id+'.jpg',comparisonImage:'comparisons/graphics-agent-c/'+key+'.jpg',graphicsRestored:restored[key]??commonRestored[deck.id]??[],remainingPlaceholderReasons:reasons,remainingDifferences:diff,finalRecaptureRequired:after.has(key),unreadableReplacements:previous?.unreadableReplacements??[],textChangesInThisRevision:[],observedOriginalLayout:previous?.observedOriginalLayout,automaticFindingsAtAgentCapture:capture.slides.find(s=>s.id===slide.id).findings.filter(f=>!f.expectedClip).length,automaticFindingsAfterLastCorrection:audit.issues.filter(f=>!f.expectedClip).length,definitionHash})
  }
  console.log(deck.id,rows.filter(r=>r.deck===deck.id).length,'pages;',audits.filter(r=>r.deck===deck.id).reduce((n,r)=>n+r.issues.filter(i=>!i.expectedClip).length,0),'findings')
 }
 const findings=audits.reduce((n,r)=>n+r.issues.filter(i=>!i.expectedClip).length,0)
 await writeFile(new URL('./graphics-agent-c.json',import.meta.url),JSON.stringify({agent:'decks_c',scope:'d38–d53 / 53 slides',originalsIndividuallyViewed:53,comparisonsIndividuallyViewed:53,comparisonRound:'graphics-agent-c',reviewMethod:'53개 원본과 53개 원본/결과 비교 이미지를 각각 tools.view_image로 개별 열람. 연락처 시트 검수로 대체하지 않음.',cycleLimit:'그래픽 개선 에이전트 1차 캡처/비교 후 최소 보정. 주 에이전트 2차 최종 캡처/개별 검수 필요.',lastCorrectionAutomaticAudit:'review/graphics-agent-c-audit.json; live browser 자동 검사만 수행하며 추가 PNG/비교 캡처 없음.',originalPolicyChange:'새 사용자 기준에 따라 gradients, transparent fade, SVG 재현 가능 장식을 복원. 사진·복잡한 회화 사진·기기 화면만 회색.',sourceFiles:['src/decks/c-graphics.ts','src/decks/c-38-45.ts','src/decks/c-46-49.ts','src/decks/c-50-53.ts'],checkedAt:new Date().toISOString(),unexpectedFindings:findings,pages:rows},null,2)+'\n')
 await writeFile(new URL('./graphics-agent-c-audit.json',import.meta.url),JSON.stringify({checkedAt:new Date().toISOString(),verification:'Live browser automatic check after the single graphics agent comparison capture. No extra PNG captured; primary final second capture remains required.',pages:audits.length,unexpectedFindings:findings,rows:audits},null,2)+'\n')
 if(rows.length!==53||findings)process.exitCode=1
} finally {await browser.close();await server.close()}
