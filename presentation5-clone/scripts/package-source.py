"""Export the executable source without images, dependencies, or old renders."""
import argparse, hashlib, json, pathlib, re, shutil, zipfile

root = pathlib.Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--stage', default='/tmp/presentation5-source-export/presentation5-clone')
parser.add_argument('--zip', action='store_true')
args = parser.parse_args()
stage = pathlib.Path(args.stage)
archive = root.parent / 'presentation5-clone-source.zip'
# Audit labels are encoded so their spellings are never introduced into files.
forbidden = re.compile(r'\uBBF8\uB9AC\s*\uCE94\uBC84\uC2A4|\u006D\u0069\u0072\u0069[\s_-]*\u0063\u0061\u006E\u0076\u0061\u0073|\u0063\u0061\u006E\u0076\u0061(?!s)', re.I)
image_extensions = {'.png','.jpg','.jpeg','.gif','.webp','.avif','.bmp','.tif','.tiff','.svg','.ico','.heic','.heif','.apng','.jxl'}

def audit(files):
    for relative, data in files:
        assert pathlib.Path(relative).suffix.lower() not in image_extensions, relative
        assert not forbidden.search(relative), relative
        text = data.decode('utf-8')
        assert not forbidden.search(text), relative
        if pathlib.Path(relative).suffix=='.json':
            assert not forbidden.search(json.dumps(json.loads(text),ensure_ascii=False)), relative
        # Uppercase JSX components such as the Lucide Image icon are vectors.
        assert not re.search(r'data:image/', text, re.I), relative
        assert not re.search(r'<(?:image|img)\b', text), relative
    return {'files':len(files),'imageFiles':0,'embeddedImageReferences':0,'externalBrandLabelMatches':0}

if not args.zip:
    assert not stage.exists(), 'Use a new staging directory; existing exports are preserved.'
    stage.mkdir(parents=True)
    relative_files = ['index.html','package.json','package-lock.json','tsconfig.json','vite.config.ts']
    relative_files += [str(p.relative_to(root)) for p in sorted((root/'src').rglob('*')) if p.is_file() and not p.name.endswith('-seed.json')]
    relative_files += ['scripts/'+f for f in ['build.mjs','build-state.mjs','audit.mjs','validate-definitions.mjs','source-check.mjs']]
    relative_files += ['public/reference/groups/'+g+'.json' for g in ['a','b','c']]
    for relative in relative_files:
        target = stage/relative
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(root/relative,target)
    package = json.loads((stage/'package.json').read_text())
    package['scripts'] = {'dev':'vite','build':'node scripts/build.mjs','typecheck':'tsc -p .','verify':'node scripts/source-check.mjs'}
    (stage/'package.json').write_text(json.dumps(package,indent=2)+'\n')
    primitives = (stage/'src/primitives.ts').read_text()
    old = 'references:slides.map(s=>`/reference/${id}/${s.id}.jpg`)'
    assert primitives.count(old)==1
    (stage/'src/primitives.ts').write_text(primitives.replace(old,'references:[]'))
    # The source-only application has no links that request omitted reference images.
    (stage/'src/App.tsx').write_text("""import {useEffect,useState} from 'react'
import {decks} from './registry'
import {ScaledSlide,SlideCanvas} from './ui'
import type {Deck} from './model'
function Board({deck}:{deck:Deck}) {return <div className="deck-board" style={{gridTemplateColumns:'repeat(2,600px)'}}>{deck.slides.map(s=><section key={s.id}><p className="reference-label"><a href={`#/slide/${deck.id}/${s.id}`}>{s.id} · {s.title} ↗</a></p><ScaledSlide slide={s} width={600}/></section>)}</div>}
export default function App(){
 const [route,setRoute]=useState(location.hash.slice(2))
 useEffect(()=>{const change=()=>setRoute(location.hash.slice(2));addEventListener('hashchange',change);return()=>removeEventListener('hashchange',change)},[])
 const [mode,id,sid]=route.split('/'),deck=decks.find(d=>d.id===id)
 if(mode==='slide'&&deck){const slide=deck.slides.find(s=>s.id===sid)??deck.slides[0];return <div className="slide-view" data-deck={deck.id}><SlideCanvas slide={slide}/></div>}
 if(deck)return <><header className="toolbar"><a href="#/">← 갤러리</a><h1>{deck.id} · {deck.title}</h1><a href={`#/deck/${deck.id}`}>슬라이드</a><span>{deck.slides.length} slides · 1280 × 720</span></header><Board deck={deck}/></>
 return <main className="gallery"><h1>Presentation 5 Clone</h1><p className="intro">{decks.length}개 덱 · {decks.reduce((n,d)=>n+d.slides.length,0)}개 슬라이드 · 1280 × 720</p><div className="deck-grid">{decks.map(d=><a className="deck-card" href={`#/deck/${d.id}`} key={d.id}><header><strong>{d.id} · {d.title}</strong><span>{d.slides.length} slides</span></header><div className="thumb"><ScaledSlide slide={d.slides[0]} width={440}/></div></a>)}</div></main>
}
""")
    (stage/'.gitignore').write_text('node_modules/\ndist/\n*.log\n')
    (stage/'README.md').write_text("""# Presentation 5 Clone — 이미지 없는 소스

47개 덱 · 1,057개 독립 슬라이드 · 각 페이지 1280×720.

이미지 파일, 원본 시트, PNG 렌더, 비교 JPG, 설치 의존성과 빌드 산출물을 제외했습니다. 텍스트·도형·차트·표·아이콘·SVG 컴포넌트와 회색 placeholder는 코드로 렌더합니다. 외부 브랜드 표기를 중립 문구로 정리했습니다. 원본 이미지 비교 메뉴는 포함하지 않습니다.

```bash
cd presentation5-clone
npm ci --cache /tmp/presentation5-npm-cache --no-audit --no-fund
npm run build
npm run dev -- --host 127.0.0.1
```

Node.js 24에서 빌드했습니다. 갤러리 `#/`, 덱 `#/deck/p004`, 단일 페이지 `#/slide/p004/s02-01`로 탐색합니다.

전체 브라우저 검사: `npm run verify`. Chromium `/usr/bin/chromium`이 필요합니다. 폰트는 패키지 의존성으로 실제 로드하며, CSS로 조립한 SVG 그래픽은 이미지 파일 없이 유지합니다. 원본 글꼴을 확보하지 못한 일부 텍스트는 실제 로드한 대체 글꼴과 자폭 보정을 사용합니다.

`review/source-only-verification.json`은 이 소스의 별도 production 검사 기록입니다. 이전 이미지 포함 제출본과 검수 자료는 저장소에 별도로 보존합니다.
""")
    files = [(str(p.relative_to(stage)),p.read_bytes()) for p in sorted(stage.rglob('*')) if p.is_file()]
    print(json.dumps({'stage':str(stage),**audit(files)},indent=2))
else:
    report = json.loads((stage/'review/source-only-verification.json').read_text())
    assert report['status']=='passed' and report['slides']==1057
    files = [(str(p.relative_to(stage)),p.read_bytes()) for p in sorted(stage.rglob('*')) if p.is_file() and not {'node_modules','dist','__pycache__'}.intersection(p.relative_to(stage).parts) and p.suffix!='.log']
    inventory = audit(files)
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as output:
        for relative,data in files:
            output.writestr('presentation5-clone/'+relative,data)
    with zipfile.ZipFile(archive) as output:
        assert output.testzip() is None
        assert audit([(name,output.read(name)) for name in output.namelist()])['files']==inventory['files']
    result = {**inventory,'file':archive.name,'bytes':archive.stat().st_size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'zipCrcPassed':True,'decks':47,'slides':1057,'browserVerification':report['status']}
    (root/'review/source-zip-verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
