"""Download published PDF files and verify exact bytes and PDF structure."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import concurrent.futures,hashlib,json,subprocess
import fitz
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=json.loads((ROOT/'pdfs/publication.json').read_text());out=Path('/tmp/rhetis-element-pdf-downloads');out.mkdir(exist_ok=True)
 def one(row):
  target=out/Path(row['path']).name;subprocess.run(['curl','--fail','--location','--silent','--show-error','--retry','2',row['url'],'--output',str(target)],check=True);assert target.stat().st_size==row['bytes'];assert hashlib.sha256(target.read_bytes()).hexdigest()==row['sha256'];d=fitz.open(target);assert len(d)==row['pages']and not d.is_repaired;assert d.get_toc();d[0].get_pixmap(matrix=fitz.Matrix(.5,.5));d.close();print('Downloaded PDF PASS',row['collection'],row['pages'],'pages',flush=True);return{**row,'downloadVerification':'pass','pdfOpenAndCoverRender':'pass'}
 with concurrent.futures.ThreadPoolExecutor(max_workers=3)as pool:rows=list(pool.map(one,p['pdfs']))
 report={'commit':p['commit'],'verifiedKST':datetime.now(ZoneInfo('Asia/Seoul')).isoformat(),'method':'Actual HTTPS downloads from the immutable source commit; SHA-256, bytes, page count, repair status, bookmarks and cover rendering checked.','pdfs':rows};(ROOT/'pdfs/download-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('VERIFIED',len(rows),'downloaded PDFs;',sum(r['pages']for r in rows),'pages')
if __name__=='__main__':main()
