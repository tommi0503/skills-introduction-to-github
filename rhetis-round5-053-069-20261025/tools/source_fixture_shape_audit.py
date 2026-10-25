"""Read-only audit of supported source map markup against its designated replica fixture.

Definite findings concern missing source fixtures, explicit variants, repeated member
counts and manual line breaks. Text-length differences are review candidates: equal
character counts do not prove equal glyph widths, and contract normalization can
change harmless wrappers. No fixture, map or collection files are modified.
"""
from pathlib import Path
from collections import Counter
import argparse,hashlib,json,re,time
from lxml import html,etree
ROOT=Path(__file__).resolve().parents[1]
EXCLUDED_CARDS={'current-fold','halo-field','corner-signal','scanline-rise'}
VARIANT=re.compile(r'^(?:on|quiet|line|tone-\d+)$')
MEMBERS={'item','step','stop','node','spoke','ring','layer','cell','row','pt','bar','slice','branch','leaf','card','plan','tier','stage','seg','chunk','entry','person'}
SLOTS={'name','kick','fig','note','key','chip'}
def classes(e):return e.get('class','').split()
def content(e):return re.sub(r'[\t\r\n]+',' ',e.text_content()).strip()
def signature(e):
 text=content(e)
 return {'chars':len(text),'spaces':text.count(' '),'br':len(e.xpath('.//br')),'text':text[:160]}
def parse(markup):
 markup=re.sub(r'<!--.*?-->','',markup,flags=re.S).strip()
 nodes=html.fragments_fromstring(markup)
 return next(e for e in nodes if isinstance(e,etree._Element))
def tokens(e):return [x for x in classes(e)if VARIANT.fullmatch(x)]
def figure_units(fig):
 explicit=fig.xpath('.//small')
 if explicit:return [{'mode':'explicit-small',**signature(e)}for e in explicit]
 text=content(fig);match=re.match(r'^[+−-]?\d[\d,.]*(.*)$',text)
 if match and match.group(1).strip():
  unit=match.group(1).strip();return [{'mode':'inline-numeric-suffix','chars':len(unit),'spaces':unit.count(' '),'br':0,'text':unit}]
 return []
def brief(v):return v[:160]if isinstance(v,str)else v
def shape(root):
 def metric(e):
  d=signature(e);return [d['chars'],d['spaces'],d['br']]
 out={'variants':sorted(tokens(root)),'members':dict(Counter(c for e in root.iter()for c in classes(e)if c in MEMBERS)),'slots':{slot:[metric(e)for e in root.iter()if slot in classes(e)]for slot in sorted(SLOTS)}}
 if not any(out['slots'].values()):out['plainText']=metric(root)
 if 'prose'in classes(root):out['paragraphs']=[metric(e)for e in root.xpath('./p')]
 out['figureUnits']=[{k:u[k]for k in ['mode','chars','spaces','br']}for f in root.iter()if 'fig'in classes(f)for u in figure_units(f)]
 return out
def audit_instance(cid,inst,cache):
 leaf=inst['leaf'];fixture=inst.get('fixture');record={'collection':cid,'page':inst.get('page'),'leaf':leaf,'fixture':fixture,'instance_id':inst.get('instance_id',inst.get('id',inst.get('instance'))),'bbox':inst.get('bbox'),'use':inst.get('use'),'source_html':inst.get('source',{}).get('html'),'source_selector':inst.get('source',{}).get('selector',inst.get('source',{}).get('selectors')),'definite':[],'review':[]}
 def finding(kind,source,target,certainty='review',**extra):record[certainty].append({'kind':kind,'source':source,'fixture':target,**extra})
 if not fixture:
  finding('missing-fixture-reference',True,None,'definite');return record
 stem=Path(fixture).stem
 if not stem.startswith('replica-'):
  record['skipped']='designated fixture is not a source replica';return record
 f=ROOT/cid/'elements'/leaf/'fixtures'/(stem+'.html');record['fixture_path']=str(f.relative_to(ROOT))
 if not f.exists():finding('missing-fixture-file',True,False,'definite');return record
 raw=f.read_text();cache[str(f.relative_to(ROOT))]=hashlib.sha256(raw.encode()).hexdigest()
 try:a=parse(inst.get('markup',''));b=parse(raw)
 except Exception as e:finding('parse-error','source/fixture',str(e),'definite');return record
 # Select actual contract root when a fixture has an incidental wrapper.
 expected=cid+'-'+leaf
 for name,root in [('source',a),('fixture',b)]:
  if root.get('data-el')!=expected:
   found=root.xpath('.//*[@data-el=$id]',id=expected)
   if found:
    if name=='source':a=found[0]
    else:b=found[0]
 record['sourceShape']=shape(a);record['fixtureShape']=shape(b)
 if a.tag!=b.tag:finding('root-tag',a.tag,b.tag)
 if sorted(tokens(a))!=sorted(tokens(b)):finding('root-contract-variant',tokens(a),tokens(b),'definite')
 # Classless spans, wrappers and optional typography are not relationship members.
 ac=Counter(c for e in a if isinstance(e.tag,str)for c in classes(e)if c in MEMBERS)
 bc=Counter(c for e in b if isinstance(e.tag,str)for c in classes(e)if c in MEMBERS)
 if ac!=bc:finding('direct-member-count',dict(ac),dict(bc),'definite')
 ad=Counter(c for e in a.iter()for c in classes(e)if c in MEMBERS)
 bd=Counter(c for e in b.iter()for c in classes(e)if c in MEMBERS)
 if ad!=bd:finding('descendant-member-count',dict(ad),dict(bd),'definite')
 av=Counter(c for e in a.iter()for c in tokens(e));bv=Counter(c for e in b.iter()for c in tokens(e))
 if av!=bv:finding('member-contract-variant-count',dict(av),dict(bv),'definite')
 for role in sorted(MEMBERS):
  am=[e for e in a.iter()if role in classes(e)];bm=[e for e in b.iter()if role in classes(e)]
  if len(am)==len(bm)and am:
   aa=[sorted(tokens(e))for e in am];bb=[sorted(tokens(e))for e in bm]
   if aa!=bb:finding('member-contract-variant-order:'+role,aa,bb,'definite')
 def slots(root,slot):return [e for e in root.iter()if slot in classes(e)]
 for slot in sorted(SLOTS):
  aa=slots(a,slot);bb=slots(b,slot)
  if len(aa)!=len(bb):finding('slot-count:'+slot,len(aa),len(bb),'definite')
  for i,(s,t)in enumerate(zip(aa,bb),1):
   ss=signature(s);tt=signature(t)
   if ss['br']!=tt['br']:finding('manual-br:'+slot,ss,tt,'definite',slot_index=i)
   if (ss['chars'],ss['spaces'])!=(tt['chars'],tt['spaces']):finding('text-length:'+slot,ss,tt,slot_index=i)
   if slot=='fig':
    su=figure_units(s);tu=figure_units(t)
    if len(su)!=len(tu):finding('figure-unit-count',su,tu,'definite',slot_index=i)
    for j,(u,v)in enumerate(zip(su,tu),1):
     if (u['chars'],u['spaces'],u['br'])!=(v['chars'],v['spaces'],v['br']):finding('figure-unit-length',u,v,'definite',slot_index=i,unit_index=j)
 # Prose and plain root labels are meaningful source shapes even without slot classes.
 if leaf=='prose':
  aa=a.xpath('./p');bb=b.xpath('./p')
  if len(aa)!=len(bb):finding('prose-paragraph-count',len(aa),len(bb),'definite')
  for i,(s,t)in enumerate(zip(aa,bb),1):
   sa=signature(s);ta=signature(t)
   if sa['br']!=ta['br']:finding('prose-manual-br',sa,ta,'definite',paragraph=i)
   seg=lambda e:[re.sub('<[^>]+>','',x)for x in re.split(r'<br\s*/?>',html.tostring(e,encoding='unicode',method='html'))]
   for j,(u,v)in enumerate(zip(seg(s),seg(t)),1):
    u=html.fromstring('<span>'+u+'</span>').text_content();v=html.fromstring('<span>'+v+'</span>').text_content()
    if (len(u),u.count(' '))!=(len(v),v.count(' ')):finding('prose-segment-length',{'chars':len(u),'spaces':u.count(' '),'text':u[:160]},{'chars':len(v),'spaces':v.count(' '),'text':v[:160]},paragraph=i,segment=j)
 elif not any(slots(a,s)for s in SLOTS) and leaf in {'tag','pill','badge','headline','callout','quote'}:
  sa=signature(a);ta=signature(b)
  if sa['br']!=ta['br']:finding('plain-root-manual-br',sa,ta,'definite')
  if (sa['chars'],sa['spaces'])!=(ta['chars'],ta['spaces']):finding('plain-root-text-length',sa,ta)
 return record
def manual_classify(r):
 key=(r['collection'],r['page'],r['leaf'])
 result=None
 if r['definite'] and key==('cinder-pulse','18','list'):
  result={'category':'map-normalization-error','severity':'high','reason':'Actual source HTML and page PNG show three bullet lines in the case-study panel. Map concatenates them into one item/name with two BRs. Three-item fixture count is not itself an error; normalize the source list before judging its per-item fixture text.','actual_source_shape':'3 bullet items, no long explanatory notes'}
 elif r['definite'] and key==('scanline-rise','06','list'):
  result={'category':'map-normalization-error','severity':'high','reason':'Actual HTML/PNG show three logical columns, each containing three bullet members. The map splits all nine members into independent one-item roots. A three-item fixture is appropriate for each complete column, not for each fragmented root.','actual_source_shape':'3 lists × 3 items'}
 elif r['definite'] and key==('scanline-rise','12','list'):
  result={'category':'map-normalization-error-plus-fixture-count-review','severity':'high','reason':'Each pale upper explanation region contains two hyphen-prefixed bullet lines. Map merges both into one name with BR, while the designated fixture has three full items. Normalize each actual two-item list, then supply a two-member source fixture.','actual_source_shape':'2 items in each pale explanation region'}
 elif r['definite'] and key==('current-fold','12','list'):
  result={'category':'fixture-error','severity':'high','reason':'Frozen source has four check-list items with genuinely empty notes. The replica fixture adds substantial two-line notes to each item. These belong in a separate stress fixture, not a source-shape fixture.','actual_source_shape':'4 names; 4 empty notes'}
 elif r['definite'] and key==('scanline-rise','02','agenda'):
  result={'category':'equivalent-line-wrapper-plus-map-normalization-review','severity':'medium','reason':'Source sublists have 3/4/3/4/3 lines. Map uses BR separators and fixture uses the same number of block spans. Literal BR difference is not a missing line. Existing CSS paints bullets only on note > span, so source map normalization should preserve semantic subitems. Text lengths still differ.','actual_source_shape':'5 entries; notes have 3/4/3/4/3 subitems'}
 elif r['definite'] and key==('halo-field','14','person') and r['definite']:
  result={'category':'nested-instance-scope','severity':'high','reason':'Actual source has a people wrapper containing three individual person cards. The wrapper fixture contains all three correctly; the nested individual source instances point at that same three-person fixture. Do not count contained children as three new top-level scenes. For individual-instance fixture verification, provide single-person source fixtures or explicitly audit each corresponding fixture member.','actual_source_shape':'1 wrapper × 3 people; contained individual instances'}
 elif r['definite'] and key==('corner-signal','03','prose') and r['definite']:
  result={'category':'fixture-error','severity':'high','reason':'Actual source contains two separately placed paragraphs: the first has four manual lines and the second two. The same four-line fixture is assigned to both. The short second paragraph needs its own source-shaped fixture.','actual_source_shape':'separate 4-line and 2-line paragraphs'}
 elif r['definite'] and key==('corner-signal','19','person'):
  result={'category':'map-role-normalization-error-plus-copy-review','severity':'high','reason':'Actual source separates a large role label from the four-line bio. Map prepends role text and BR to note; fixture uses a semantic small role followed by three BRs in the bio. Total visible line count can be equivalent, so literal BR count alone is not a fixture failure. Normalize the source role into the actual role slot, then compare its source-specific English/Korean width and bio lengths.','actual_source_shape':'separate role label + 4 bio lines'}
 if result:
  result['evidence']='Manually read frozen source HTML and individually viewed the corresponding reference/replica-html-render page PNG.'
  r['manualClassification']=result
 if r['definite'] and key==('scanline-rise','04','card'):
  r['manualClassification']={'category':'equivalent-line-wrapper-plus-map-normalization-review','severity':'medium','reason':'Fixture uses block spans as bullet subitems; source map uses BRs. Actual source has 2/3/3 lines. The visible line count is equivalent, but card CSS adds bullets only to note > span; source-map normalization should preserve those semantic subitems.'}
 if r['definite'] and key==('corner-signal','05','card'):
  r['manualClassification']={'category':'map-contract-variant-normalization-review','severity':'high','reason':'Designated source fixtures explicitly use on/quiet but map markup lacks that root variant. Check source emphasis and use-field semantics before correcting the canonical root markup; this is not a reason to drop the real source fixture variation.'}
 if r['definite'] and not result and 'manualClassification'not in r:r['manualClassification']={'category':'requires-source-review','severity':'high','reason':'Observed structural difference; not yet adjudicated against actual source.'}
 severe=[]
 for f in r['review']:
  a=f.get('source');b=f.get('fixture')
  if isinstance(a,dict)and isinstance(b,dict)and 'chars'in a and 'chars'in b:
   delta=b['chars']-a['chars']
   if (a['chars']>=25 and abs(delta)>=10)or(a['chars']>=15 and b['chars']>=a['chars']*1.75):severe.append({'kind':f['kind'],'sourceChars':a['chars'],'fixtureChars':b['chars'],'delta':delta,'slot_index':f.get('slot_index'),'paragraph':f.get('paragraph'),'segment':f.get('segment')})
 if severe:r['longTextShapeRisks']=severe
 return r
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--out',default='source-fixture-shape-audit.json');parser.add_argument('--exclude-concurrent-cards',action='store_true');args=parser.parse_args();records=[];cache={};excluded=[];maphash={}
 for item in json.loads((ROOT/'collections.json').read_text()):
  cid=item['id'];p=ROOT/(cid+'-review')/'map.json';raw=p.read_text();maphash[str(p.relative_to(ROOT))]=hashlib.sha256(raw.encode()).hexdigest();data=json.loads(raw)
  for inst in data['instances']:
   if inst.get('use')in {'unexpressible','furniture','background'}or not inst.get('leaf'):continue
   if args.exclude_concurrent_cards and inst['leaf']=='card'and cid in EXCLUDED_CARDS:excluded.append({'collection':cid,'page':inst.get('page'),'leaf':'card','reason':'concurrent owner correction; explicitly excluded for this run'});continue
   records.append(manual_classify(audit_instance(cid,inst,cache)))
 active=[r for r in records if not r.get('skipped')]
 reuse={}
 for r in active:
  if 'sourceShape'in r:reuse.setdefault((r['collection'],r['leaf'],r['fixture']),[]).append(r)
 reusegroups=[]
 for (cid,leaf,fixture),rs in reuse.items():
  distinct={json.dumps(r['sourceShape'],sort_keys=True)for r in rs}
  if len(distinct)>1:reusegroups.append({'collection':cid,'leaf':leaf,'fixture':fixture,'sourceShapeCount':len(distinct),'instances':[{'page':r['page'],'bbox':r['bbox'],'sourceShape':r['sourceShape']}for r in rs]})
 flagged=[r for r in active if r['definite']or r['review']]
 def summary(kind):return dict(Counter(f['kind']for r in active for f in r[kind]))
 changed=[str(p)for p,h in {**maphash,**cache}.items()if not(ROOT/p).exists()or hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h]
 report={'schema':'rhetis.source-fixture-shape-audit/1','createdUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'policy':'Read-only. Definite = structural/explicit variant/manual BR discrepancy; review = text-length discrepancy, not proof of unequal pixel width. Contract normalization may require human review. This report does not imply source support for excluded/GAP scenes.','summary':{'mappedInstancesVisited':len(records),'sourceReplicaInstancesAudited':len(active),'skippedNonReplica':len(records)-len(active),'concurrentCardsExcluded':len(excluded),'instancesWithDefinite':sum(bool(r['definite'])for r in active),'instancesWithReview':sum(bool(r['review'])for r in active),'definiteFindings':summary('definite'),'reviewFindings':summary('review'),'sourceFigureSlotsChecked':sum(len(r.get('sourceShape',{}).get('slots',{}).get('fig',[]))for r in active),'sourceFigureUnitSlotsChecked':sum(len(r.get('sourceShape',{}).get('figureUnits',[]))for r in active),'explicitVariantMismatchInstances':sum(any('variant'in f['kind']for f in r['definite'])for r in active)},'byCollection':{cid:{'audited':sum(r['collection']==cid for r in active),'flagged':sum(r['collection']==cid for r in flagged)}for cid in [x['id']for x in json.loads((ROOT/'collections.json').read_text())]},'manualClassificationSummary':dict(Counter(r['manualClassification']['category']for r in active if r.get('manualClassification'))),'highSeverityLongTextInstances':[{'collection':r['collection'],'page':r['page'],'leaf':r['leaf'],'fixture':r['fixture'],'risks':r['longTextShapeRisks']}for r in active if r.get('longTextShapeRisks')],'sameFixtureDistinctSourceShapes':reusegroups,'excluded':excluded,'changedDuringAudit':changed,'mapSha256':maphash,'fixtureSha256':cache,'findings':flagged,'matchingInstances':[{k:r.get(k)for k in ['collection','page','leaf','fixture']}for r in active if not r['definite']and not r['review']]}
 out=ROOT/args.out;out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report['summary'],ensure_ascii=False,indent=2));print('changedDuringAudit',len(changed));print('output',out)
if __name__=='__main__':main()
