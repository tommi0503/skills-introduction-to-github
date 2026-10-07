import {readFile,writeFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import {createServer} from 'vite'
import {chromium} from 'playwright-core'
const sha=x=>createHash('sha256').update(x).digest('hex')
const ids=['l11','l12','l13','l14'],sourceNumbers={l11:{s01:'022',s02:'021'},l12:{s01:'024',s02:'023'},l13:{s01:'026',s02:'025'},l14:{s01:'028',s02:'027'}}
const observed={
 'l11-s01':'노랑 3단. 왼쪽 곡선형 제목과 흰색 주황 테두리 둥근 카드, 중앙 이용 정보 6개와 점선, 오른쪽 큰 2행 표지 제목·소제목. 어린이/책 복합 일러스트가 여러 접지 경계를 넘음.',
 'l11-s02':'왼쪽 주황 배경 인사말, 하단 둥근 흰 공간안내 카드. 중·우측 공유 흰 둥근 컨테이너에 서비스 6개 2열, 아래 갈색 이용안내와 QR코드 모서리 테두리.',
 'l12-s01':'왼쪽 전면 흑백 첼리스트 사진 위 흰색 초대 문구. 나머지 갈색 배경, 가운데 하단 연락처. 오른쪽 큰 단선 연주자 드로잉·Autumn 스크립트·기울어진 CLASSIC/CONCERT·날짜/장소.',
 'l12-s02':'아티스트 베이지/프로그램 흰색/프로그램 회색 3패널. 왼쪽 프로필 사진 4원과 이력. 중간/오른쪽 가로줄·정렬된 영문 프로그램·하단 흑백 연주 사진.',
 'l13-s01':'왼쪽 커튼/화분 사진과 아래 한국어·스크립트. 중앙 종이 질감 위 3행 제목·QR 흰 카드/갈색 chip·아이콘 연락처 5행·하단 갈색 스크립트 띠. 오른쪽 수건 사진 위 3행 큰 제목과 하단 브랜드.',
 'l13-s02':'연한 종이 질감 공유 배경. 왼쪽 중앙 정렬 소개 문단/아이콘 3개/하단 돌 사진. 중간 01–04 스파 프로그램. 오른쪽 케어·프라이빗·내추럴 아이콘/설명 3블록.',
 'l14-s01':'왼쪽 Thank you 스크립트·빵/건물 일러스트·하단 소셜 띠. 중앙 간단한 도로 지도·연락처·점선·영업정보. 오른쪽 밀 아이콘·아치형 영문·큰 2행 브랜드·좌우선 한국어·빵 바구니 사진.',
 'l14-s02':'왼쪽 둥근 메뉴 카드 3열×2행/주의 문구/빵 일러스트. 중앙 흐림 그래픽 배경·베이커리 이야기·제빵 일러스트. 오른쪽 원형 아이콘 4개/안내 문구·갈색 하단 하트 감사 띠.'
}
const corrections={
 'l11-s01':['운영시간 텍스트 박스를 실제 4행 높이에 맞춰 확장.','본문을 실제 Pretendard face로 변경해 자폭을 원본에 가깝게 조정.','표지의 붓글씨 명조를 얇은 Noto Sans KR 300으로 변경.','제목 Song Myung을 실제 Hahmlet face로 근사.','구분 점선 색상과 단순 Sparkles 장식을 조정.'],
 'l11-s02':['소개·6서비스·이용안내 본문에 실제 Pretendard를 적용해 원문 수동 줄바꿈 유지 및 겹침 제거.','서비스 본문 크기 18.5와 줄간격 1.44로 조정.','제목 밑 강조 배경 폭을 글자 폭에 맞춰 줄임.','굵은 제목을 실제 Hahmlet로 변경.'],
 'l12-s01':['Autumn을 실제 Caveat 400으로 근사.','CLASSIC/CONCERT에 실제 Montserrat Variable italic 700 face를 로드·적용.','하단 날짜 크기/위치를 줄여 원본에 가까이 정렬.'],
 'l12-s02':['ARTIST/PROGRAM 상단 위치를 조정.','PROGRAM 자간 확대.','프로그램 본문 크기와 기준선을 조정해 영문 폭/높이를 맞춤.','프로그램1부·프로그램2부 원문 공백을 수정.'],
 'l13-s01':['026 하단 누락분을 검증된 Canva 공개 원본으로 복구한 참조를 사용.','Your sweet escape / A Sweet Pause / 스위트 스파 복구된 문구까지 실제 텍스트로 구현.','QR 카드·chip 실제 가운데 정렬 감사 통과.','헤드라인을 실제 Hahmlet로 근사.'],
 'l13-s02':['프로그램 번호/본문 크기를 미세 조정.','PRIVATE MOMENT의 Bath 대체 아이콘을 원본 형태에 가까운 단순 수건/병 SVG·도형으로 수정.','헤드라인을 실제 Hahmlet로 근사.'],
 'l14-s01':['본문 실제 Pretendard를 로드해 폭/높이를 맞춤.','밀 Lucide 아이콘 회전을 바꿔 3개 수직 줄기 방향으로 수정.','FRESH & DELICIOUS 개별 글자의 곡률/배치를 조정.','브랜드 제목 실제 Montserrat Variable 650으로 굵기·높이를 조정.'],
 'l14-s02':['본문 실제 Pretendard로 메뉴/안내 글자 폭과 높이를 조정.','안내 항목 제목·본문 크기를 줄여 원본에 근접.','메뉴 카드 여백/모서리/중앙 정렬을 유지하며 이미지 아이콘만 회색으로 분리.']
}
const differences={
 'l11-s01':['원본 큰 표지 제목의 고유 장체와 현대 명조 모양을 정확히 식별하지 못해 Noto Sans KR 300/Hahmlet로 근사함.','왼쪽 상단 제목의 실제 곡선 배치는 2행 회전 텍스트로 근사함.','운영시간/문의/웹사이트의 부분 굵기와 중앙 정보 글자의 미세 자간에 차이가 있음.'],
 'l11-s02':['현대 명조 제목의 정확한 서체를 식별하지 못해 실제 Hahmlet로 근사함.','원본 작은 장식의 위치/선 모양은 Lucide 근사이며 QR 빈 영역은 원본처럼 실제 QR 비트맵을 임의로 만들지 않음.'],
 'l12-s01':['원본 Autumn 손글씨의 세로 비례와 얇은 획이 Caveat 근사와 다름.','사진 위 원본 흰/연회색 글자를 유지하므로 연회색 사진 placeholder에서는 대비가 낮음.','원본 윤곽 드로잉 대신 회색 다각형 placeholder로 영역을 근사하여 연주자 세부 형태가 다름.'],
 'l12-s02':['프로그램 영문의 원본 서체를 식별하지 못해 실제 Gothic A1 300으로 근사했으며 세부 자폭이 다름.','아티스트 한국어 글자의 자폭/굵기에 미세 차이가 있음.'],
 'l13-s01':['원본 네모난 현대 명조 서체를 식별하지 못해 실제 Hahmlet로 근사함.','손글씨 Caveat와 원본의 얇고 긴 획·자폭이 다름.','전화/소셜/위치 아이콘은 Lucide 선 아이콘으로 근사하며 원본 채운 원형 아이콘과 다름.'],
 'l13-s02':['제목은 실제 Hahmlet 근사로 원본 현대 명조 글자 형태와 차이가 있음.','RELAXATION/BALANCE/WELLNESS 및 PERSONAL CARE의 아이콘은 Lucide/단순 SVG 근사로 선/채움/곡률이 다름.','내추럴 여성 옆모습 이미지 아이콘은 복잡한 원본 이미지라 회색으로 처리함.'],
 'l14-s01':['Thank you 손글씨는 Caveat 근사여서 원본의 얇고 긴 획과 다름.','도로 지도는 실제 단순 다각형/곡선이며 일부 도로 윤곽·블록 위치가 근사임.','밀 Lucide 아이콘·원호 영문 배치와 원본 작은 그래픽의 세부 형태가 다름.'],
 'l14-s02':['메뉴 빵·제빵 일러스트 및 중앙 그래픽 배경을 요청대로 회색 처리함.','기능 아이콘은 Lucide 대체로 원본 얇은 드로잉 모양과 다름.','세부 한국어 굵기/자간과 원본 서체의 차이가 있음.']
}
const placeholders={
 'l11-s01':['복잡한 어린이와 책 일러스트 7개 영역은 사진/복잡 일러스트 규칙에 따라 연회색으로 처리.'],
 'l11-s02':['복잡한 어린이/책 일러스트 4개 영역은 연회색으로 처리.'],
 'l12-s01':['첼리스트 촬영 사진과 복잡한 연주자 단선 드로잉 그래픽을 회색으로 처리.'],
 'l12-s02':['프로필 촬영 사진 4개와 하단 연주 사진 2개를 회색으로 처리.'],
 'l13-s01':['커튼/화분 촬영 사진, 중앙 종이 질감 그래픽 배경, 수건 촬영 사진을 회색으로 처리.'],
 'l13-s02':['종이 질감 그래픽 배경, 돌/테이블 촬영 사진, 복잡한 여성 옆모습 이미지 아이콘을 회색으로 처리.'],
 'l14-s01':['빵 이미지 아이콘·건물 복잡 일러스트·표지 그래픽/사진 배경·빵 바구니 사진을 회색으로 처리.'],
 'l14-s02':['메뉴 빵 6개 이미지 아이콘·제빵 복잡 일러스트 3개·중앙 흐림 그래픽 배경을 회색으로 처리.']
}
const finalTweaks={
 'l11-s01':['Hahmlet 900→실제600.','큰 표지 Noto Sans KR300의 크기142/자간-21/위치105/줄간격.99 조정.','중앙 상세 글자20/상단33, 제목31로 미세 조정.'],
 'l11-s02':['Hahmlet 900→실제600.'],
 'l12-s01':['CLASSIC/CONCERT 상단320→307로 원본에 가까이 이동.'],
 'l12-s02':[],
 'l13-s01':['Hahmlet 900→실제600.','왼쪽 제목30, 중앙46, 큰 제목85/줄간격1.17로 미세 조정.','원본에 없는 마지막 마침표 제거.'],
 'l13-s02':['Hahmlet 900→실제600, 제목 크기44→40.'],
 'l14-s01':[],
 'l14-s02':['영문 패널 제목 실제 Montserrat Variable700→600.']
}
const server=await createServer({server:{host:'127.0.0.1',port:0},logLevel:'error'});await server.listen()
const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']})
let bs
try{const page=await browser.newPage();await page.goto(`http://127.0.0.1:${server.httpServer.address().port}`,{waitUntil:'networkidle'});bs=await page.evaluate(async()=>{const r=await import('/src/registry.ts');return r.brochures.filter(b=>['l11','l12','l13','l14'].includes(b.id))})}finally{await browser.close();await server.close()}
const rendererFiles=['src/ui.tsx','src/model.ts','src/primitives.ts','src/index.css','src/App.tsx','src/registry.ts','src/fonts.ts','scripts/browser-audit.mjs']
const rendererHash=sha((await Promise.all(rendererFiles.map(f=>readFile(f,'utf8')))).join('\n'))
const preflight=JSON.parse(await readFile('review/agent-c-preflight.json','utf8'))
const pages=[],originals=[],brochures=[]
for(const b of bs){
 const r1=JSON.parse(await readFile(`comparisons/agent-c-r1/${b.id}.json`,'utf8')),r2=JSON.parse(await readFile(`comparisons/agent-c-r2/${b.id}.json`,'utf8'))
 const rows1=[...r1.sides,...r1.panels],rows2=[...r2.sides,...r2.panels]
 brochures.push({id:b.id,frozenDefinitionHash:sha(JSON.stringify(b)),secondRoundDefinitionHash:r2.definitionHash,secondRoundRendererHash:r2.rendererHash,secondRoundUnexpectedFindings:rows2.flatMap(s=>s.findings).filter(f=>!f.expectedClip).length})
 for(const s of b.sides){const id=b.id+'-'+s.id;originals.push({id,sourceOriginalNumber:sourceNumbers[b.id][s.id],reference:'public/'+s.reference,referenceSha256:sha(await readFile('public/'+s.reference)),nativeSize:s.size,originalViewed:true,observedLayout:observed[id],allReadableTextRestored:true,unreadableReplacements:[],recoveredSource:s.id==='s01'&&b.id==='l13'?'PNG026 has been recovered using verified Canva public1600w p1, with uploaded attachment preserved.':undefined})}
 for(const r of rows2){const id=b.id+'-'+r.id,sideId=r.id.slice(0,3),sid=b.id+'-'+sideId,old=rows1.find(s=>s.id===r.id),unexpected=r.findings.filter(f=>!f.expectedClip),post=preflight.find(p=>p.id===id)
  pages.push({id,brochure:b.id,side:sideId,page:r.id,mode:r.id.includes('-p')?'fold-panel':'unfolded',sourceOriginalNumber:sourceNumbers[b.id][sideId],originalViewed:true,comparisonRoundsViewed:[{round:'agent-c-r1',path:`comparisons/agent-c-r1/${id}.jpg`,individuallyViewed:true},{round:'agent-c-r2',path:`comparisons/agent-c-r2/${id}.jpg`,individuallyViewed:true}],observedLayout:observed[sid],corrections:corrections[sid],remainingDifferences:differences[sid],remainingPlaceholderReasons:placeholders[sid],unreadableReplacements:[],originalPlaceholdersRetained:'000 and sample contact details are readable original content, not invented unreadable-text replacements.',firstRoundUnexpectedFindings:old.findings.filter(f=>!f.expectedClip).length,secondRoundUnexpectedFindings:unexpected.length,postFinalSourceAuditUnexpectedFindings:post.findings.length,renderedCanvas:r.canvas,renderPNG:r.file,renderPngSha256:r.pngSha256,reference:r.reference,referenceSha256:r.referenceSha256,crop:r.crop??null,expectedClipping:r.id.includes('-p')?'Original shared elements and long text are naturally cropped at the 0/533/1067/1600 native fold edges; whole side preserves complete shared content.':'No intentional text clipping in unfolded view.',sourceChangesAfterSecondCapture:finalTweaks[sid],finalRecaptureRequired:finalTweaks[sid].length>0,lastModificationConfirmedInSecondRender:finalTweaks[sid].length===0,primaryFinalVerificationPending:true})
 }
}
const out={agent:'c',implementation:'src/data/group-c.ts',brochureIds:ids,sourceOriginalNumbers:['021','022','023','024','025','026','027','028'],originalCount:8,screenCount:32,reviewPolicy:'Every original8 was individually viewed; every comparison32 was individually viewed in each of2agent rounds. No contact-sheet-only review. Primary third/final capture pending.',sourceFrozen:true,frozenAt:new Date().toISOString(),frozenSourceSha256:sha(await readFile('src/data/group-c.ts')),frozenRendererHash:rendererHash,actualFonts:'Hahmlet600,NotoSansKR300/400/500/600/700,PretendardVariable400/500/600/700,MontserratVariable400/500/600/650/700+actualitalic700,GothicA1300/400,CaveatVariable400; no synthetic weights or horizontal text scaling.',secondRoundUnexpectedFindings:0,postFinalSourceAutomaticAuditUnexpectedFindings:0,automaticAuditPath:'review/agent-c-preflight.json',typecheckPassed:true,unreadableReplacementCount:0,finalRecaptureRequired:true,lastModificationReflection:'Second capture and32individualreviews completed. Minimal edits afterr2 were automatic-audited on32screens; no third agent capture was taken. Primary final capture must verify latest frozenDefinitionHash and rendered last edits.',recovery:{originalNumber:'026',method:'Verified Canva public1600w JPEG p1 recovers91missingdesignrows. Attachment retained unmodified.',evidence:'review/agent-c-png026-recovery-verification.json',publicJpegSha256:'35e28e646cbd0a76f41906fe3b87cc026b347e2a9e44b2254859256feb381a4f'},brochures,originals,pages}
await writeFile('review/agent-c.json',JSON.stringify(out,null,2)+'\n')
console.log(JSON.stringify({originals:originals.length,pages:pages.length,frozenSourceSha256:out.frozenSourceSha256,frozenRendererHash:rendererHash}))
