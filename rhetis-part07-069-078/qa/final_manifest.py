"""Record immutable collection inputs and whether audit snapshots match current source."""
import json,hashlib,datetime,importlib.util
from audit_css import BASE,REFERENCE,COLLECTIONS
s=importlib.util.spec_from_file_location('pv',REFERENCE/'tools/preview.py');pv=importlib.util.module_from_spec(s);s.loader.exec_module(pv)
manifest={'status':'Per-report source snapshots only; no visual fidelity acceptance is implied','generatedAtUtc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'collections':{}}
for k in COLLECTIONS:
 root=BASE/(k+'-project')/k
 files={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(root.rglob('*')) if p.is_file()}
 tree=hashlib.sha256(json.dumps(files,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 sheets={}
 for dark in [False,True]:
  m=pv.sheet(root,json.loads((REFERENCE/'contract/type-steps.json').read_text()),json.loads((REFERENCE/'contract/palette.json').read_text()),dark=dark,fonts_href=f'/{k}-project/assets/fonts/fonts.css')
  sheets['dark' if dark else 'light']=hashlib.sha256(m.encode()).hexdigest()
 audits={}
 suffixes=['audit','browser-css-audit','alignment-audit','code-font-audit','pill-cover-audit','clipping-audit','functional-audit','functional-dark-audit','clipping-dark-audit','contrast-audit','contrast-min-audit','placeholder-final-audit','source15-final-audit']
 suffixes+=sorted(p.stem[len(k)+1:] for p in (BASE/'qa').glob(f'{k}-functional-*.json') if p.stem[len(k)+1:] not in suffixes)
 for suffix in suffixes:
  path=BASE/'qa'/f'{k}-{suffix}.json'
  if not path.exists():continue
  d=json.loads(path.read_text()); hashval=d.get('sourceSha256') if isinstance(d,dict) else None
  info={'report':path.name,'reportSha256':hashlib.sha256(path.read_bytes()).hexdigest()}
  if suffix=='source15-final-audit':info['matchesCurrentSourceTree']=d.get('collectionSourceTreeSha256')==tree;info['passed']=d.get('passed');info['scope']=d.get('scope')
  if hashval and suffix=='placeholder-final-audit':info['matchesCurrentSourceTree']=hashval==hashlib.sha256(json.dumps(files,sort_keys=True).encode()).hexdigest();info['reportedSourceSha256']=hashval
  elif hashval:info['matchesCurrent'+('Dark' if '-dark-' in suffix else 'Light')+'Sheet']=hashval==sheets['dark' if '-dark-' in suffix else 'light']
  if suffix in ['contrast-audit','contrast-min-audit']:info['matchesCurrentSheet']={mode:x.get('sourceSha256')==sheets[mode] for mode,x in d.items()}
  if suffix.startswith('functional-'):info['counts']=d['counts'];info['testedTypes']=d.get('testedTypes',[])
  if suffix=='audit':info['summary']=d['summary']
  audits[suffix]=info
 manifest['collections'][k]={'sourceTreeSha256':tree,'sourceFiles':files,'sheetSha256':sheets,'audits':audits}
manifest['auditToolSha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((BASE/'qa').glob('*')) if p.suffix in ['.py','.js']}
manifest['manualEvidenceSha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for name in ['crossrail-native-contrast.json','crossrail-bars-annotated-light.png','crossrail-bars-annotated-dark.png','crossrail-pyramid5-min.png','072-pill-stack.png','072-bubble-5.png','073-logos-6.png','078-agenda-3.png','078-three-icon-circles-source.png'] if (p:=BASE/'qa'/name).exists()}
manifest['manualEvidenceSha256'].update({p.name:hashlib.sha256(p.read_bytes()).hexdigest() for pattern in ['crossrail-source15-final.png','crossrail-photo-rule-*.png'] for p in (BASE/'qa').glob(pattern)})
(BASE/'qa/final-source-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
for k,d in manifest['collections'].items():print(k,d['sourceTreeSha256'],{s:i.get('matchesCurrentLightSheet',i.get('matchesCurrentSheet')) for s,i in d['audits'].items() if 'matchesCurrentLightSheet' in i or 'matchesCurrentSheet' in i})
