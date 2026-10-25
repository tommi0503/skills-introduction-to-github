"""Verify final render lineage and create the seven intake/review ZIP pairs."""
import argparse,hashlib,io,json,re,zipfile
from pathlib import Path
from PIL import Image
from render_reassembled import dependency_manifest
ROOT=Path(__file__).resolve().parents[1]
SIZES=[(12,6),(12,3),(9,4),(8,6),(6,6),(6,3),(4,4),(4,3),(3,3)]

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def text_values(value):
    if isinstance(value,str):return [value]
    if isinstance(value,dict):return [s for v in value.values()for s in text_values(v)]
    if isinstance(value,list):return [s for v in value for s in text_values(v)]
    return []
def need(value,message):
    if not value:raise ValueError(message)

def expected_fingerprint(cid,leaf,mapped):
    C=ROOT/cid;E=C/'foundation'if leaf=='foundation-panels'else C/'elements'/leaf;files=sorted((E/'fixtures').glob('panel-*.html'if leaf=='foundation-panels'else'*.html'));deps={leaf}
    for f in files:deps.update(re.findall(r'data-el=[\"\']'+re.escape(cid)+r'-([^\"\']+)',f.read_text()))
    inputs=[C/'kit/css/tokens.css',C/'foundation/foundation.css',C/'foundation/foundation.json',ROOT/'contract/palette.json',ROOT/'contract/type-steps.json',ROOT/'fonts/fonts.css',*files]
    inputs +=[C/'elements'/dep/name for dep in sorted(deps)for name in ['element.css','element.json']if(C/'elements'/dep/name).exists()]
    signature=[{k:x.get(k)for k in ['page','bbox','use','fixture']}for x in mapped]
    return hashlib.sha256((''.join(str(f.relative_to(ROOT))+f.read_text()for f in inputs)+json.dumps(signature,sort_keys=True)+sha(ROOT/'tools/element_sheets.py')).encode()).hexdigest()

def verify():
    static=json.loads((ROOT/'static-audit.json').read_text());need(not static['issues'],'Static audit has unresolved issues')
    text=json.loads((ROOT/'fixture-text-audit.json').read_text());need(text['checked']and not text['issues'],'Fixture source text is still present')
    lock=json.loads((ROOT/'replica-lock-audit.json').read_text());need(lock['checked']==203 and not lock['changed'],'Frozen replicas changed')
    for row in json.loads((ROOT/'replica-lock.json').read_text()):
        f=ROOT/'reference/frozen'/Path(row['path']).relative_to('rhetis-enterprise-053-069');need(sha(f)==row['sha256'],'Frozen source mismatch: '+str(f))
    for name,digest in json.loads((ROOT/'font-lock.json').read_text()).items():need(sha(ROOT/name)==digest,'Provided font changed: '+name)
    furniture=json.loads((ROOT/'furniture-audit.json').read_text());need(len(furniture)==190,'Furniture audit incomplete')
    need(not any(x['contrast']or x['outside']or x['overlap']or x['fontErrors']for x in furniture),'Furniture audit has unresolved issues')
    total_states=0;pngs=[];summaries=[]
    for item in json.loads((ROOT/'collections.json').read_text()):
        cid=item['id'];C=ROOT/cid;R=ROOT/(cid+'-review');m=json.loads((R/'map.json').read_text());folders=sorted(p.name for p in(C/'elements').iterdir()if p.is_dir());need(bool(folders),cid+' has no observed designs')
        required_pages={re.search(r'(\d+)\.html$',f.name)[1]for f in(ROOT/'reference/frozen'/(cid+'-review')/'replica').glob('*.html')}
        need({x['page']for x in m['instances']}==required_pages,cid+' map page coverage')
        states=0;observed=0
        for leaf in folders:
            mapped=[x for x in m['instances']if x.get('leaf')==leaf and x.get('use')not in ['unexpressible','furniture','background']]
            observed+=bool(mapped);a=json.loads((R/'audits'/(leaf+'.json')).read_text())
            need(not a.get('quick')and not a.get('staleDuringRender'),cid+'/'+leaf+' is quick/stale')
            need(a.get('sourceSha256')==expected_fingerprint(cid,leaf,mapped),cid+'/'+leaf+' needs a final rerender')
            expected=set()
            for f in(C/'elements'/leaf/'fixtures').glob('*.html'):
                v=re.search(r'<!--\s*min:\s*(\d+)x(\d+)',f.read_text());minimum=(int(v[1]),int(v[2]));sizes=[s for s in SIZES if s[0]>=minimum[0]and s[1]>=minimum[1]]
                if minimum not in sizes:sizes.append(minimum)
                expected.update((f.stem,mode,str(c)+'x'+str(r))for mode in ['light','dark']for c,r in sizes)
            actual={(s['fixture'],s['mode'],s['size'])for s in a['states']};need(actual==expected,cid+'/'+leaf+' missing grid-size states')
            for s in a['states']:
                errors=[k for k in ['overflow','textOverlap','hiddenNameFig','contrastFailures','paintOverflow','chipAlignmentFailures','fontErrors']if s.get(k)]
                need(not errors,cid+'/'+leaf+'/'+s['fixture']+'/'+s['mode']+'/'+s['size']+' '+','.join(errors))
                need([s['canvas']['w'],s['canvas']['h']]==[1280,720],cid+'/'+leaf+' slide size')
                need(s['fontStatus']=='loaded',cid+'/'+leaf+' font loading')
            for rel,digest in a.get('outputs',{}).items():need(sha(R/rel)==digest,cid+'/'+leaf+' PNG modified after audit')
            for source in a.get('replicaReferences',[]):
                need(sha(ROOT/source['path'])==source['sha256'],cid+'/'+leaf+' reference crop input changed')
            need(bool(a.get('outputs')),cid+'/'+leaf+' has no output hashes')
            for mode in ['light','dark']+(['replica']if mapped else[]):
                f=R/'sheets'/(leaf+'-'+mode+'.png');need(f.exists(),str(f)+' missing')
            states+=len(a['states'])
        if m.get('panels'):
            a=json.loads((R/'audits/foundation-panels.json').read_text())
            signature=[{'page':x['page'],'bbox':x['bbox'],'fixture':x.get('fixture')or f'panel-{x["page"]}-{i:02}','use':'furniture'}for i,x in enumerate(m['panels'],1)]
            need(not a.get('quick')and not a.get('staleDuringRender'),cid+' panels quick/stale')
            need(a['sourceSha256']==expected_fingerprint(cid,'foundation-panels',signature),cid+' panels need final rerender')
            for st in a['states']:
                need(not any(st.get(k)for k in ['overflow','textOverlap','hiddenNameFig','contrastFailures','paintOverflow','chipAlignmentFailures','fontErrors']),cid+' panel '+st['fixture']+'/'+st['size']+' has flags')
            for rel,digest in a['outputs'].items():need(sha(R/rel)==digest,cid+' panel output changed')
            states+=len(a['states'])
        preview=json.loads((R/'preview-audit.json').read_text())
        for rel,digest in preview['inputs'].items():need(sha(ROOT/rel)==digest,cid+' preview needs regeneration: '+rel)
        for rel,digest in preview['outputs'].items():need(sha(R/rel)==digest,cid+' preview HTML changed')
        inputs=json.loads((R/'reassembled-dependencies.json').read_text());need(not inputs['staleDuringRender'],cid+' reassembly changed during rendering')
        need(inputs['files']==dependency_manifest(cid),cid+' reassembly inputs changed since render')
        page_audits=json.loads((R/'reassembled-audit.json').read_text());need(len(page_audits)==item['pages'],cid+' page audit count')
        for row in page_audits:
            need(not(row['outside']or row['overlap']or row['errors']or row.get('paintOverflow')or row.get('fontErrors')or row.get('staleDuringRender')),cid+' page '+row['page']+' has layout/font/http flags')
            need(row.get('inputsSHA256')==inputs['sha256'],cid+' page dependency hash differs')
            need(row['fontStatus']=='loaded'and row['pageSize']==[1280,720],cid+' page font/size failure')
            f=R/'reassembled'/('slide_'+row['page']+'.html');need(sha(f)==row['htmlSHA256'],str(f)+' changed since rendering')
            f=f.with_suffix('.png');need(sha(f)==row['pngSHA256'],str(f)+' changed since rendering')
        for f in sorted(R.rglob('*.png')):
            with Image.open(f)as im:
                im.verify()
            with Image.open(f)as im:
                if f.parent.name=='reassembled':need(im.size==(1280,720),str(f)+' page PNG size')
                if f.parent.name=='compare-reassembled':need(im.size==(3840,720),str(f)+' comparison PNG size')
                pngs.append({'path':str(f.relative_to(ROOT)),'width':im.width,'height':im.height,'sha256':sha(f)})
        total_states+=states;summaries.append({'collection':cid,'elements':len(folders),'observedLeaves':observed,'pages':item['pages'],'fixtureStates':states,'unexpressible':sum(x['use']=='unexpressible'for x in m['instances'])})
    visual={x['path']:x for x in json.loads((ROOT/'primary-visual-review.json').read_text())}
    for item in json.loads((ROOT/'collections.json').read_text()):
        r=ROOT/(item['id']+'-review')
        for f in list((r/'sheets').glob('*.png'))+list((r/'compare-reassembled').glob('*.png')):
            key=str(f.relative_to(ROOT));v=visual.get(key,{})
            need(v.get('status')=='pass'and v.get('sha256')==sha(f),'Primary visual review missing/stale: '+key)
    result={'build':'success','round':5,'gitCommandsRun':False,'collections':summaries,'elements':sum(x['elements']for x in summaries),'pages':95,'states':total_states,'pngs':pngs}
    (ROOT/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));return result

def write_pairs(report):
    artifacts=[]
    for item in json.loads((ROOT/'collections.json').read_text()):
        cid=item['id'];C=ROOT/cid;R=ROOT/(cid+'-review');collection_zip=ROOT/(cid+'.zip')
        with zipfile.ZipFile(collection_zip,'w',zipfile.ZIP_DEFLATED,compresslevel=9)as z:
            for f in sorted(C.rglob('*')):
                if f.is_file():
                    need(f.suffix in ['.css','.json','.md','.html'],'Forbidden intake file '+str(f));z.write(f,str(f.relative_to(ROOT)))
        review_zip=ROOT/(cid+'-review.zip')
        with zipfile.ZipFile(review_zip,'w',zipfile.ZIP_DEFLATED,compresslevel=9)as z:
            for f in sorted(R.rglob('*')):
                if not f.is_file()or '__pycache__'in f.parts:continue
                rel=f.relative_to(R)
                if f.suffix=='.html':
                    s=f.read_text()
                    if rel.parts[0]=='reassembled':
                        s=s.replace('../../'+cid+'/', '../styles/'+cid+'/').replace('../../fonts/','../fonts/').replace('../../assets/','../assets/').replace('../../runtime.css','../runtime.css')
                    elif f.name.startswith('preview-'):s=s.replace('../fonts/','fonts/')
                    z.writestr(str(rel),s)
                else:z.write(f,str(rel))
            z.write(ROOT/'runtime.css','runtime.css')
            # Preserve every used font family without shipping unrelated library faces.
            # The canonical 32 supplied font files stay unchanged in source.
            collection_text='\n'.join(s for f in C.rglob('*')if f.is_file()and f.suffix in ['.css','.json']for s in(text_values(json.loads(f.read_text()))if f.suffix=='.json'else[f.read_text()]))
            faces=[]
            for face in re.findall(r'@font-face\s*\{[^}]+\}',(ROOT/'fonts/fonts.css').read_text()):
                family=re.search(r"font-family\s*:\s*['\"]([^'\"]+)",face)[1]
                if re.search(r"['\"]"+re.escape(family)+r"['\"]",collection_text):faces.append(face)
            need(bool(faces),cid+' has no portable font declarations')
            font_paths={ROOT/'fonts'/rel for face in faces for rel in re.findall(r"url\(['\"]?([^\)'\"]+)",face)}
            z.writestr('fonts/fonts.css','\n'.join(faces)+'\n')
            for f in sorted(font_paths):z.write(f,str(f.relative_to(ROOT)))
            for f in sorted((ROOT/'assets').rglob('*')):
                if f.is_file():z.write(f,str(f.relative_to(ROOT)))
            for f in sorted(C.rglob('*.css')):z.write(f,'styles/'+str(f.relative_to(ROOT)))
            z.writestr('verification.json',json.dumps(next(x for x in report['collections']if x['collection']==cid),ensure_ascii=False,indent=2))
        for f in [collection_zip,review_zip]:
            with zipfile.ZipFile(f)as z:
                need(z.testzip()is None,str(f)+' CRC failed')
                if f==collection_zip:need({n.split('/')[0]for n in z.namelist()}=={cid},'Intake ZIP root')
                for n in z.namelist():need(not n.startswith('/')and'..'not in Path(n).parts,'Unsafe ZIP path')
            artifacts.append({'name':f.name,'bytes':f.stat().st_size,'sha256':sha(f)})
    (ROOT/'artifacts.json').write_text(json.dumps(artifacts,ensure_ascii=False,indent=2));(ROOT/'SHA256SUMS').write_text(''.join(x['sha256']+'  '+x['name']+'\n'for x in artifacts));print('Verified and packaged',len(artifacts),'ZIP files')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--verify-only',action='store_true');a=p.parse_args();report=verify()
    if not a.verify_only:write_pairs(report)
