"""Download immutable GitHub ZIPs, then verify CRC, hashes, PNGs and inventory."""
import argparse, concurrent.futures, datetime, hashlib, json, pathlib, re, struct, subprocess, zipfile

root=pathlib.Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument('commit')
p.add_argument('--prefix',default='presentation5-clone-quality-v2')
p.add_argument('--download-dir',default='/tmp/presentation5-quality-v2-github-download')
a=p.parse_args()
assert re.fullmatch('[0-9a-f]{40}',a.commit)
delivery=json.loads((root.parent/f'{a.prefix}-downloads.json').read_text())
slides=json.loads((root/'review/delivery-manifest.json').read_text())
expected={f'presentation5-clone/renders/final/{s["deck"]}-{s["slide"]}.png':s['pngSha256'] for s in slides}
download=pathlib.Path(a.download_dir);download.mkdir(parents=True,exist_ok=True)
def fetch(row):
    url=f'https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/{a.commit}/{row["file"]}'
    subprocess.run(['curl','--fail','--location','--retry','2','--max-time','240',url,'--output',str(download/row['file'])],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    return url
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    urls=list(pool.map(fetch,delivery['archives']))
seen,files,archives=set(),set(),[]
for row,url in zip(delivery['archives'],urls):
    path=download/row['file'];digest=hashlib.sha256(path.read_bytes()).hexdigest()
    assert digest==row['sha256'] and path.stat().st_size==row['bytes']
    with zipfile.ZipFile(path) as z:
        assert z.testzip() is None
        for name in z.namelist():
            if name=='DELIVERY.txt':continue
            assert name not in files,f'Duplicate payload: {name}'
            files.add(name)
            if name in expected:
                content=z.read(name)
                assert hashlib.sha256(content).hexdigest()==expected[name]
                assert content[:8]==b'\x89PNG\r\n\x1a\n' and struct.unpack('>II',content[16:24])==(1280,720)
                seen.add(name)
    archives.append({**row,'downloadedSha256':digest,'downloadedBytes':path.stat().st_size,'downloadMatchesCommittedArchive':True,'remoteZipCrcPassed':True,'downloadUrl':url})
sheets=sum(n.startswith('presentation5-clone/public/sheets/') for n in files)
refs=sum(n.startswith('presentation5-clone/public/reference/') and n.endswith('.jpg') and '/groups/' not in n for n in files)
pairs=sum(n.startswith('presentation5-clone/comparisons/final/') and n.endswith('.jpg') and not n.endswith('-contact.jpg') for n in files)
previews=sum(n.startswith('presentation5-clone/review/preview-pages/') and n.endswith('.jpg') for n in files)
assert len(seen)==1057 and (sheets,refs,pairs,previews)==(117,1057,1057,53)
assert 'presentation5-clone/preview.html' in files
report={'status':'passed','qualityRevision':'2026-10-07-v2','artifactCommit':a.commit,
    'verifiedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'downloadedViaHTTPS':True,'localArchiveFilesWereNotCopied':True,
    'zipParts':len(archives),'sourceSheets':sheets,'nativeReferences':refs,'comparisonPairs':pairs,'previewPages':previews,
    'pngCount':len(seen),'allPngSize':[1280,720],'allRemotePngHashesMatch':True,'allRemoteZipHashesAndCrcMatch':True,'archives':archives}
(root/'review/github-download-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='archives'},ensure_ascii=False,indent=2))
