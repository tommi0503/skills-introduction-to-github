"""Fresh inferred spatial elements from 078 circles, paper bays and capsule captions.
Only these six element folders are written. Shared design files are never changed.
"""
from write_elements import write
import sys

def matrix(nine=False):
 k='matrix-nine' if nine else 'matrix';root='grid9' if nine else 'matrix';n=3 if nine else 2
 css='''/* Source18:12px round neutral bays,24px copy insets and thin rules; source16:open ruled lists. */
ROOT{container-type:size;container-name:od-matrix;position:relative;box-sizing:border-box;display:grid;grid-template-columns:repeat(N,minmax(0,1fr));grid-template-rows:repeat(N,minmax(0,1fr));gap:var(--gap-sm);padding:var(--gap-lg) 0 var(--gap-lg) calc(var(--gap-lg)*1.5);min-width:0;min-height:0;color:var(--ink)}
ROOT>.cell{box-sizing:border-box;container-type:size;display:flex;flex-direction:column;justify-content:center;gap:calc(var(--gap-sm)/2);padding:var(--gap-sm);border-radius:var(--radius);background:var(--n-1);min-width:0;min-height:0}
ROOT>.cell.on{background:var(--a1-1-soft);outline:var(--stroke) solid var(--a1-4-soft);outline-offset:calc(var(--stroke)*-1)}
ROOT>.cell>.name{margin:0;font-size:var(--type-18);font-weight:var(--name-weight);line-height:var(--name-line);letter-spacing:var(--name-track);overflow-wrap:anywhere}
ROOT>.cell>.note{margin:0;font-size:var(--type-14);font-weight:var(--body-weight);line-height:var(--label-line);letter-spacing:var(--body-track);color:var(--n-7);overflow-wrap:anywhere}
ROOT>.axis-x{position:absolute;left:calc(var(--gap-lg)*1.5);right:0;bottom:0;display:flex;justify-content:space-between;gap:var(--gap-sm)}
ROOT>.axis-y{position:absolute;left:0;top:var(--gap-lg);bottom:var(--gap-lg);width:var(--gap-lg);display:flex;flex-direction:column;justify-content:space-between;gap:var(--gap-sm)}
ROOT>.axis-x>span,ROOT>.axis-y>span{font-size:var(--type-12);font-weight:var(--body-weight);line-height:var(--label-line);letter-spacing:var(--body-track);color:var(--n-7);overflow-wrap:anywhere}
@container od-matrix(max-height:400px){ROOT>.cell{padding:calc(var(--gap-sm)/2)}ROOT>.cell>.name{font-size:var(--type-16)}ROOT>.cell>.note{font-size:var(--type-12)}}
'''.replace('repeat(N,',f'repeat({n},')
 if nine:
  css+='ROOT>.cell>.name{font-size:var(--type-16)}ROOT>.cell>.note{font-size:var(--type-12)}'
 else:
  css+='''ROOT.swot{padding:0}ROOT.swot>.cell{gap:calc(var(--gap-sm)/2);justify-content:center}ROOT.swot>.cell>.kick{margin:0;font-size:var(--type-28);font-weight:var(--figure-weight);line-height:var(--figure-line);letter-spacing:var(--figure-track);color:var(--a1-7)}ROOT.swot>.cell>.list{inline-size:100%;block-size:43cqh;flex:none;align-self:stretch;justify-self:stretch}'''
 labels=['승인 우선','책임 합의','보완 검토','위험 점검','실행 확대','운영 유지','예외 분류','현장 대조','후속 협의']
 notes=['근거가 충분한 요청부터 처리해요.','담당 조직의 이관 범위를 맞춰요.','누락된 변경 사유를 보완해요.','반복 발생 위험을 다시 살펴요.','승인 조건에 맞춰 적용을 넓혀요.','검토한 기준을 지속 점검해요.','특별한 처리 사유를 분류해요.','상담 기록과 조치 결과를 대조해요.','개선 항목의 담당자를 정해요.']
 def row(alt=False):
  if alt and not nine:
   pairs=[('공유된 접수 기준',['문의 분류표 정리','책임 조직의 합의']),('분산된 이관 이력',['기록 보관처 통합','검토 대장의 정비']),('점검 자동화 확대',['알림 규칙의 시험','중복 등록의 제거']),('승인 지연의 재발',['누락 사유의 추적','대기 건수의 확인'])]
   return '<div class="matrix swot" DATA>'+''.join('<div class="cell'+(' on' if i==0 else '')+'"><p class="kick">'+c+'</p><p class="name">'+name+'</p><div class="list divided" data-el="onboard-docket-list">'+''.join('<div class="item"><p class="name">'+t+'</p></div>' for t in rows)+'</div></div>' for i,(c,(name,rows)) in enumerate(zip('SWOT',pairs)))+'</div>'
  return '<div class="'+root+'" DATA><div class="axis-x">'+''.join('<span>'+v+'</span>' for v in (['낮은 영향','보통 영향','높은 영향'] if nine else ['낮은 영향','높은 영향']))+'</div><div class="axis-y">'+''.join('<span>'+v+'</span>' for v in (['높은 위험','보통 위험','낮은 위험'] if nine else ['높은 위험','낮은 위험']))+'</div>'+''.join('<div class="cell'+(' on' if i==(4 if nine else 0) else '')+'"><p class="name">'+(('여러 부서의 예외 승인 협의') if alt and i==1 else labels[(i+(2 if alt else 0))%len(labels)])+'</p><p class="note">'+notes[i]+'</p></div>' for i in range(n*n))+'</div>'
 write(k,root,css,'Rounded neutral paper bays extend the reference’s divided explanation panels into an axis comparison. A pale accent bay denotes priority; separate names and short notes retain the measured Noto hierarchy. The SWOT form uses real nested list elements and independent list slots.', [('risk-priority','6x4' if nine else '4x3',row()),('review-options','6x6' if nine else '8x6',row(True))])

def concentric():
 css='''/* Source06:248px open circular boundary; source14:paired short captions; source17:bare figures. */
ROOT{container-type:size;container-name:od-orbit;position:relative;min-width:0;min-height:0;color:var(--ink);--od-rings:3}
ROOT:has(>.ring:nth-child(2):last-child){--od-rings:2}ROOT:has(>.ring:nth-child(4):last-child){--od-rings:4}
ROOT>.ring{box-sizing:border-box;container-type:size;position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:calc(min(88cqw,88cqh)*(var(--od-rings) - var(--od-order) + 1)/var(--od-rings));aspect-ratio:1;border-radius:50%;border:2px solid var(--n-4);display:grid;grid-template-columns:max-content max-content;column-gap:calc(var(--gap-sm)/2);align-content:start;justify-content:center;align-items:baseline;background:none;padding-top:calc(min(88cqw,88cqh)/(4*var(--od-rings)) - var(--type-22)*var(--figure-line)/2);--od-order:1}
ROOT>.ring:nth-child(2){--od-order:2}ROOT>.ring:nth-child(3){--od-order:3}ROOT>.ring:nth-child(4){--od-order:4}ROOT>.ring:last-child{padding-top:calc(min(88cqw,88cqh)/(2*var(--od-rings)) - var(--type-22)*var(--figure-line)/2)}
ROOT>.ring.on{border-color:var(--a1-7)}ROOT>.ring>.name{margin:0;font-size:var(--type-14);font-weight:var(--name-weight);line-height:var(--label-line);letter-spacing:var(--name-track);white-space:nowrap}
ROOT>.ring>.fig{margin:0;font-size:var(--type-22);font-weight:var(--figure-weight);line-height:var(--figure-line);letter-spacing:var(--figure-track);white-space:nowrap}
ROOT>.ring>.note{grid-column:1/-1;margin:0;font-size:var(--type-12);font-weight:var(--body-weight);line-height:var(--label-line);letter-spacing:var(--body-track);text-align:center;color:var(--n-7)}
ROOT>.ring:has(>.note){padding-top:calc(min(88cqw,88cqh)/(4*var(--od-rings)) - (var(--type-22)*var(--figure-line) + var(--type-12)*var(--label-line))/2)}
@container od-orbit(max-height:360px){ROOT>.ring{padding-top:calc(min(88cqw,88cqh)/(4*var(--od-rings)) - var(--type-16)*var(--figure-line)/2)}ROOT>.ring:last-child{padding-top:calc(min(88cqw,88cqh)/(2*var(--od-rings)) - var(--type-16)*var(--figure-line)/2)}ROOT>.ring:has(>.note){padding-top:calc(min(88cqw,88cqh)/(4*var(--od-rings)) - (var(--type-16)*var(--figure-line) + var(--type-12)*var(--label-line))/2)}ROOT>.ring>.fig{font-size:var(--type-16)}ROOT>.ring>.name{font-size:var(--type-12)}}
'''
 def row(n):
  return '<div class="orbit" DATA>'+''.join('<div class="ring'+(' on' if i==n-1 else '')+'"><p class="name">'+name+'</p><p class="fig">'+str(v)+'</p>'+('<p class="note">전사 접수 합계</p>' if n==3 and i==0 else '')+'</div>' for i,(name,v) in enumerate([('전체 요청',287),('검토 대상',162),('승인',94),('예외',12)][:n]))+'</div>'
 write('concentric','orbit',css,'Open concentric outlines communicate inclusion without opaque layers. Each name and figure share one baseline on the upper annulus, calculated from the actual ring count; the innermost subset is centred. The small optional note remains visible.', [('three-subsets','5x4',row(3)),('four-subsets','6x4',row(4))])

def venn():
 css='''/* Inferred plain-set comparison: source08 circular material and source14 translucent overlaps. */
ROOT{container-type:size;container-name:od-venn;position:relative;isolation:isolate;min-width:0;min-height:0;color:var(--ink)}
ROOT>.set{box-sizing:border-box;container-type:size;position:absolute;width:min(62cqw,82cqh);aspect-ratio:1;left:calc(50% - min(62cqw,82cqh)*.8);top:calc(50% - min(62cqw,82cqh)*.5);border:2px solid var(--n-4);border-radius:50%}
ROOT>.set::before{content:"";position:absolute;inset:0;border-radius:50%;background:var(--n-1);opacity:.55;z-index:0}ROOT>.set:nth-child(2){left:calc(50% - min(62cqw,82cqh)*.2)}ROOT>.set.on{border-color:var(--a1-7)}ROOT>.set.on::before{background:var(--a1-1-soft)}
ROOT>.set>.name{position:absolute;top:40%;left:10%;right:50%;margin:0;font-size:clamp(var(--type-14),9cqw,var(--type-22));font-weight:var(--name-weight);line-height:var(--name-line);letter-spacing:var(--name-track);text-align:center;overflow-wrap:anywhere;z-index:2}
ROOT>.set:nth-child(2)>.name{left:50%;right:10%}
ROOT:has(>.set:nth-child(3))>.set{width:min(57cqw,60cqh);left:calc(50% - min(57cqw,60cqh)*.8);top:calc(50% - min(57cqw,60cqh)*.73)}ROOT:has(>.set:nth-child(3))>.set:nth-child(2){left:calc(50% - min(57cqw,60cqh)*.2)}ROOT:has(>.set:nth-child(3))>.set:nth-child(3){left:calc(50% - min(57cqw,60cqh)*.5);top:calc(50% - min(57cqw,60cqh)*.27)}
ROOT:has(>.set:nth-child(3))>.set>.name{top:23%}ROOT:has(>.set:nth-child(3))>.set:nth-child(3)>.name{left:25%;right:25%;top:70%}
ROOT>.core{box-sizing:border-box;position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);max-width:25%;padding:calc(var(--gap-sm)/2);border-radius:999px;background:var(--page);text-align:center;font-size:var(--type-14);font-weight:var(--body-weight);line-height:var(--label-line);letter-spacing:var(--body-track);z-index:3}
@container od-venn(max-width:600px){ROOT>.core{font-size:var(--type-12)}}
'''
 def row(n):return '<div class="venn" DATA>'+''.join('<div class="set'+(' on' if i==0 else '')+'"><p class="name">'+name+'</p></div>' for i,name in enumerate((['접수 기준','승인 근거'] if n==2 else ['접수 내용 대조','승인 근거','후속 점검'])))+'<div class="core">합의된 기준</div></div>'
 write('venn','venn',css,'Plain named sets overlap through translucent paper fields, separately from the source’s icon-circle illustration. Names sit on exposed outer arcs and remain above every field; a compact paper capsule identifies the shared intersection.', [('two-sets','5x3',row(2)),('three-sets','6x4',row(3))])

def network():
 css='''/* Source06:101×30px centred capsules and1px relationship rules; source09 organization connectors. */
ROOT{container-type:size;container-name:od-network;position:relative;isolation:isolate;min-width:0;min-height:0;color:var(--ink)}
ROOT>.node,ROOT>.link{--od-nx:min(16cqw,calc(var(--gap-lg)*3));--od-ny:min(20cqh,calc(var(--gap-lg)*2))}
ROOT>.node{box-sizing:border-box;position:absolute;left:calc(var(--od-nx) + (100cqw - 2*var(--od-nx))*var(--x)/100);top:calc(var(--od-ny) + (100cqh - 2*var(--od-ny))*var(--y)/100);transform:translate(-50%,-50%);width:min(27cqw,calc(var(--gap-lg)*5));min-height:min(16cqh,calc(var(--gap-lg)*1.25));display:flex;align-items:center;justify-content:center;padding:calc(var(--gap-sm)/2);border-radius:999px;background:var(--n-1);border:var(--stroke) solid var(--n-4);font-size:var(--type-14);font-weight:var(--name-weight);line-height:var(--name-line);letter-spacing:var(--name-track);text-align:center;overflow-wrap:anywhere}
ROOT>.node>.name{margin:0;font:inherit;letter-spacing:inherit}ROOT>.node.on{background:var(--a1-7);color:var(--page);border-color:var(--a1-7)}ROOT>.node.tone-2{background:var(--a2-1-soft)}ROOT>.node.tone-3{background:var(--a3-1-soft)}
ROOT>.link{position:absolute;left:calc(var(--od-nx) + (100cqw - 2*var(--od-nx))*var(--x1)/100);top:calc(var(--od-ny) + (100cqh - 2*var(--od-ny))*var(--y1)/100);height:var(--stroke);width:hypot(calc((100cqw - 2*var(--od-nx))*(var(--x2) - var(--x1))/100),calc((100cqh - 2*var(--od-ny))*(var(--y2) - var(--y1))/100));rotate:atan2(calc((100cqh - 2*var(--od-ny))*(var(--y2) - var(--y1))/100),calc((100cqw - 2*var(--od-nx))*(var(--x2) - var(--x1))/100));transform-origin:0 50%;background:var(--n-4);z-index:-1}ROOT>.link.strong{height:calc(var(--stroke)*2);background:var(--a1-7)}
'''
 def row(extra=False):
  pts=[('상담 접수',12,18),('승인 책임',82,16),('운영 지원',30,80),('품질 점검',85,70)]+([('지역별 승인 책임자',48,45)] if extra else [])
  links=[(0,1),(0,2),(1,3),(2,3)]+([(0,4),(1,4),(2,4),(3,4)] if extra else [])
  return '<div class="network" DATA>'+''.join('<div class="node'+(' on' if i==1 else ' tone-2' if i==2 else '')+'" style="--x:'+str(x)+';--y:'+str(y)+'"><p class="name">'+name+'</p></div>' for i,(name,x,y) in enumerate(pts))+''.join('<div class="link'+(' strong' if a==1 else '')+'" style="--x1:'+str(pts[a][1])+';--y1:'+str(pts[a][2])+';--x2:'+str(pts[b][1])+';--y2:'+str(pts[b][2])+'"></div>' for a,b in links)+'</div>'
 write('network','network',css,'Thin coordinate-based links connect quiet capsule nodes. Euclidean distance and atan2 calculate every link from its two public endpoints, with the same reserved margins as the nodes. Labels remain above links and one relationship uses a stronger accent rule.', [('four-organizations','5x3',row()),('five-organizations','6x4',row(True))])

def positioning():
 css='''/* Source06 capsule captions and source17 quiet comparison fields; no reference chart layout is imported. */
ROOT{container-type:size;container-name:od-posmap;position:relative;isolation:isolate;min-width:0;min-height:0;color:var(--ink)}ROOT::before{content:"";position:absolute;left:10%;right:10%;top:50%;height:var(--stroke);background:var(--n-4)}ROOT::after{content:"";position:absolute;left:50%;top:8%;bottom:8%;width:var(--stroke);background:var(--n-4)}
ROOT>.axis-x{position:absolute;left:0;right:0;top:calc(50% + var(--gap-sm)/3);display:flex;justify-content:space-between}ROOT>.axis-y{position:absolute;left:calc(50% + var(--gap-sm)/2);top:0;bottom:0;display:flex;flex-direction:column;justify-content:space-between}
ROOT>.axis-x>span,ROOT>.axis-y>span{font-size:var(--type-12);font-weight:var(--body-weight);line-height:var(--label-line);letter-spacing:var(--body-track);color:var(--n-7);max-width:calc(var(--gap-lg)*2.5);overflow-wrap:anywhere}
ROOT>.mark{box-sizing:border-box;position:absolute;left:calc(18cqw + 64cqw*var(--x)/100);top:calc(84cqh - 68cqh*var(--y)/100);transform:translate(-50%,-50%);width:min(24cqw,calc(var(--gap-lg)*5));min-height:min(16cqh,calc(var(--gap-lg)*1.25));display:flex;align-items:center;justify-content:center;padding:calc(var(--gap-sm)/2);border-radius:999px;background:var(--n-1);border:var(--stroke) solid var(--n-4);font-size:var(--type-14);font-weight:var(--name-weight);line-height:var(--name-line);letter-spacing:var(--name-track);text-align:center;overflow-wrap:anywhere;z-index:1}ROOT>.mark>.name{margin:0}ROOT>.mark.on{background:var(--a1-7);color:var(--page);border-color:var(--a1-7)}ROOT>.mark>.seat{width:min(12cqw,12cqh);height:min(12cqw,12cqh);aspect-ratio:1;border-radius:var(--radius-sm)}
'''
 def row(logos=False):return '<div class="posmap" DATA><div class="axis-x"><span>낮은 자동화</span><span>높은 자동화</span></div><div class="axis-y"><span>높은 응답 품질</span><span>낮은 응답 품질</span></div>'+''.join('<div class="mark'+(' on' if i==2 else '')+'" style="--x:'+str(x)+';--y:'+str(y)+'">'+('<div class="seat logo" data-ph="'+str(i+1)+'"></div>' if logos else '<p class="name">'+name+'</p>')+'</div>' for i,(name,x,y) in enumerate([('상담 채널',15,18),('메일 이관',75,28),('공유 승인',25,77),('현장 협의',82,85)]))+'</div>'
 write('positioning','posmap',css,'Two fine crossing axes locate capsule alternatives on explicit x/y coordinates. Labels use quiet neutral material, one accent capsule indicates the focal option, and optional logo seats preserve a square image area within the same mark contract.', [('four-channels','5x3',row()),('four-partners','6x4',row(True))])

def author(k):
 if k in ['matrix','matrix-nine']:matrix(k=='matrix-nine')
 elif k=='concentric':concentric()
 elif k=='venn':venn()
 elif k=='network':network()
 elif k=='positioning':positioning()
 else:raise SystemExit(k)
if __name__=='__main__':author(sys.argv[1])
