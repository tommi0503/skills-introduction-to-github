from pathlib import Path
import subprocess,concurrent.futures,hashlib,json,time
P=Path(__file__).parent;Q=P.parent/'qa';C=P/'meridian-deck'
def snapshot():return {str(f.relative_to(C)):hashlib.sha256(f.read_bytes()).hexdigest() for f in C.rglob('*') if f.is_file()}
initial=snapshot();jobs=[('static','audit_css.py',[]),('browser','browser_audit.py',[]),('clip-light','clipping_audit.py',[]),('clip-dark','clipping_dark_audit.py',[]),('contrast-full','contrast_audit.py',[]),('contrast-min','contrast_min_audit.py',[]),('functional-light','functional_audit.py',[]),('functional-dark','functional_audit.py',['--dark']),('alignment','alignment_audit.py',[]),('code-font','code_font_audit.py',[]),('pill','pill_audit.py',[])]
def run(job):
 name,script,args=job;t=time.time();r=subprocess.run(['python',str(Q/script),'meridian-deck',*args],capture_output=True,text=True);print(name,'exit',r.returncode,'seconds',round(time.time()-t,1),r.stdout[-1300:],r.stderr[-600:],flush=True);return {'name':name,'exit':r.returncode,'seconds':round(time.time()-t,1)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(run,jobs))
end=snapshot();out={'sourceUnchanged':initial==end,'sourceFiles':len(initial),'sourceSha256':hashlib.sha256(json.dumps(initial,sort_keys=True).encode()).hexdigest(),'jobs':results};(Q/'meridian-deck-readonly-final-run.json').write_text(json.dumps(out,indent=2));print('READONLY FINAL',out,flush=True)
