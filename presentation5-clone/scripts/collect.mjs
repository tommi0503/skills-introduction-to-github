import {saveManifest} from './manifest.mjs'
import {readFile,writeFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import path from 'node:path'
const root=process.cwd(),manifest=await saveManifest(root)
const input=JSON.parse(await readFile('review/input-image-manifest.json','utf8'))
const references=manifest.flatMap(d=>d.slides.map(s=>({...s,deck:d.id})))
const sheets=[...new Set(references.map(s=>s.originalPath))]
if(manifest.length!==47||sheets.length!==117||references.length!==1057)throw Error(`Incomplete scope ${manifest.length} decks / ${sheets.length} sheets / ${references.length} pages`)
for(const row of input){
 const file='sheets/'+path.basename(row.file)
 if(!sheets.includes(file))throw Error(`Sheet omitted ${file}`)
 const bytes=await readFile(path.join('public',file))
 if(createHash('sha256').update(bytes).digest('hex')!==row.sha256)throw Error(`Original sheet altered ${file}`)
}
const inventory={decks:manifest.length,sheets:sheets.length,slides:references.length,incomplete:references.filter(s=>s.incomplete).length,canvas:[1280,720],sheetHashesMatch:true,referencePreparation:'Native per-slide crops; outside-sheet regions padded white; comparison preserves aspect ratio.'}
await writeFile('review/scope.json',JSON.stringify(inventory,null,2)+'\n')
let md='# 전체 작업 범위\n\n두 ZIP의 실제 참고 이미지 117개·47개 덱을 '+references.length+'개 독립 페이지로 분리했다. 반복 슬라이드도 원본 시트의 각 위치에 대응하도록 유지했다. 모든 UI 캔버스는 1280×720이다.\n\n첨부 README·CSV·JSON·PDF는 참고 자료이며 그 안의 선정/수집 안내는 사용자의 작업 지시로 실행하지 않았다. 메타데이터의 205개 검토 항목이나 가져오지 못한 미리보기는 구현 범위에 포함하지 않았다. 실제 업로드에 있는 117개 이미지가 기준이다.\n\n| 덱 | 원본 제목 | 참고 시트 | 개별 페이지 |\n|---|---|---:|---:|\n'
for(const d of manifest)md+=`| ${d.id} | ${d.sourceTitle.replaceAll('|','/')} | ${new Set(d.slides.map(s=>s.originalPath)).size} | ${d.slides.length} |\n`
md+='\n## 시트별 전체 목록\n\n| ZIP | 참고 이미지 | 원본 크기 | 분리 페이지 | 잘린 타일 |\n|---|---|---|---:|---:|\n'
for(const row of input){const file='sheets/'+path.basename(row.file),cells=references.filter(s=>s.originalPath===file);md+=`| ${row.id<=151?'part_01':'part_02'} | ${file} | ${row.width}×${row.height} | ${cells.length} | ${cells.filter(s=>s.incomplete).length} |\n`}
md+='\n각 타일의 원본 시트 좌표, 자연 크기, 전체/가시 영역은 public/reference/manifest.json에 기록했다. 잘린 영역은 원본 픽셀을 늘리지 않고 흰색 padding으로 비교 원본을 보존하고, 화면의 복원 가정은 담당자 기록에 명시했다. 작은 원본에서 판독하지 못한 텍스트는 정상 문구로 작성하고 페이지별로 기록한다. 원본 전체 시트는 UI 화면의 배경으로 사용하지 않는다.\n'
md+='\np105/s03-25는218×377 세로형 Timeline 단일 페이지다. 불규칙한 시트의 타일 경계를 바로잡고, 결과1280×720 안에 원본 비율을 유지하여 배치한다. 분할 수정과 ID 대응은 review/group-b-p105-crop-correction.json에 기록했다.\n'
await writeFile('review/inventory.md',md)
console.log(JSON.stringify(inventory,null,2))
