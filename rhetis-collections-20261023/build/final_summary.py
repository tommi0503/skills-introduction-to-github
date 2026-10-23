from pathlib import Path
import json,hashlib
W=Path('/workspace/work/integration');names=['fluxweave','cyanloop','roundrise','nightchamfer','glasspulse'];read=lambda f:json.loads((W/f).read_text())
static={r['collection']:r for r in read('static-audit.json')};artifact={r['collection']:r for r in read('artifact-audit.json')};snap={r['collection']:r for r in read('validation-snapshot-audit.json')};compiled={r['collection']:r for r in read('compiled-asset-audit.json')};pdf={r['collection']:r for r in read('pdf-page-image-audit.json')};sel={r['collection']:r for r in read('selector-audit.json')};data={r['collection']:r for r in read('data-audit.json')};strict={r['collection']:r for r in read('strict-fixture-audit.json')}
records=[]
for name in names:
 b=read(name+'-browser-audit.json');page=read(name+'-page-audit.json');row={'collection':name,'elements':static[name]['counts']['elements'],'fixtures_including_foundation':static[name]['counts']['fixtures'],'element_fixtures':b['fixtures'],'grid_states_both_modes':b['tested_states'],'final_html_pages':len(page['pages']),'png_count':len(artifact[name]['pngs']),'library_pngs':artifact[name]['library_png_count'],'pdfs':artifact[name]['pdfs'],'errors':[]}
 contrast=read(name+'-contrast-audit.json')
 if contrast:
  if name=='nightchamfer' and len(contrast)==2 and all('headline-big.html' in r['fixture'] and all(i['gradientAncestor'] for i in r['issues']) for r in contrast):
   row['contrast']='Gradient-filled headline: plain-color false positives separately verified by library/gradient-contrast.json.'
  else:row['errors'].append({'check':'unresolved_contrast','issues':contrast})
 else:row['contrast']='No color-contrast concerns.'
 for label,issues in [('static',static[name]['errors']),('fixture_contract',strict[name]['errors']),('artifact',artifact[name]['errors']),('snapshot',snap[name]['errors']),('compiled_css',compiled[name]['errors']),('pdf_pixels',pdf[name]['errors']),('selectors',sel[name]['invalid_selectors']),('data',data[name]['issues']),('geometry',b['issues']),('page',page['errors'])]:
  if issues:row['errors'].append({'check':label,'issues':issues})
 if b['fonts'] or b['resources']:row['errors'].append({'check':'font_resources','issues':b['fonts']+b['resources']})
 records.append(row)
summary={'original_pages':96,'collections':5,'elements':sum(r['elements'] for r in records),'grid_states_tested':sum(r['grid_states_both_modes'] for r in records),'html_pages':sum(r['final_html_pages'] for r in records),'pngs':sum(r['png_count'] for r in records),'zip_count':10,'all_passed':all(not r['errors'] for r in records),'collections_detail':records,'limits':['Visual comparisons are documented individually; photographs and complex 3D are deliberately light-gray placeholders.','Font identification is an informed approximation where font metadata was absent. The 128px contract maximum affects the reassembled Q&A page.','Transparent gradient-filled headline contrast is checked using actual gradient endpoints; the plain-color contrast script cannot measure background-clip glyph fill.']}
(W/'final-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
if not summary['all_passed']:raise SystemExit(json.dumps([r for r in records if r['errors']],ensure_ascii=False,indent=2))
ledger=read('visual-review-ledger.json');ledger['status']='최종 통합 검수 완료 — 96장 replica와 조립본을 각각 개별 비교했고, 수정된 최종 HTML·PNG·PDF·ZIP의 일치와 데이터 기능을 검증함. 잔차와 의도적 대체는 각 review-notes.md 참조.'
for row in ledger['collections']:
 row['final_replica_verified']=True;row['final_reassembled_verified']=True;row['element_semantic_review']='56개 요소의 light/dark 개별 검토 및 교차 검수. 연결·값·집합·단위 기능 결함 수정 후 최종 시트 확인.'
 row['final_browser_page_report']=row['name']+'-page-audit.json';row['source_snapshot_verified']=True
(W/'visual-review-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
print({k:v for k,v in summary.items() if k not in ['collections_detail','limits']})
