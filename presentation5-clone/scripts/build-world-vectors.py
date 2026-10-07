"""Project Natural Earth TopoJSON after splitting polygons at the dateline.

Inputs: world-atlas@2 land-110m.json and countries-110m.json (ISC).
The geographic data is public domain. No reference-image pixels are traced.
"""
import argparse, hashlib, json, math, os, pathlib
root=pathlib.Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument('--land',default='/tmp/p5-world-land-110m.json')
p.add_argument('--countries',default='/tmp/p5-world-countries.json')
a=p.parse_args()

def decode(file,name):
    d=json.loads(pathlib.Path(file).read_text());sx,sy=d['transform']['scale'];tx,ty=d['transform']['translate']
    arcs=[]
    for arc in d['arcs']:
        x=y=0;points=[]
        for dx,dy in arc:
            x+=dx;y+=dy;points.append((x*sx+tx,y*sy+ty))
        arcs.append(points)
    result=[]
    for g in d['objects'][name]['geometries']:
        polygons=g['arcs'] if g['type']=='MultiPolygon' else [g['arcs']]
        rings=[]
        for polygon in polygons:
            for ring in polygon:
                points=[]
                for index in ring:
                    arc=arcs[index] if index>=0 else list(reversed(arcs[~index]))
                    points.extend(arc if not points else arc[1:])
                rings.append(points)
        result.append((g,rings))
    return result

def clip(points,boundary,keep_left):
    if not points:return []
    output=[];previous=points[-1]
    inside=lambda point:point[0]<=boundary+1e-8 if keep_left else point[0]>=boundary-1e-8
    for current in points:
        old_in,new_in=inside(previous),inside(current)
        if old_in!=new_in:
            t=(boundary-previous[0])/(current[0]-previous[0])
            output.append((boundary,previous[1]+t*(current[1]-previous[1])))
        if new_in:output.append(current)
        previous=current
    return output

def split(ring):
    if len(ring)<3 or max(y for x,y in ring)<-60:return []
    if ring[-1]==ring[0]:ring=ring[:-1]
    unwrapped=[]
    for x,y in ring:
        if unwrapped:x+=360*round((unwrapped[-1][0]-x)/360)
        unwrapped.append((x,y))
    low,high=min(x for x,y in unwrapped),max(x for x,y in unwrapped)
    pieces=[]
    for shift in range(math.ceil((-180-high)/360),math.floor((180-low)/360)+1):
        piece=clip(clip([(x+shift*360,y) for x,y in unwrapped],-180,False),180,True)
        if len(piece)>=3:pieces.append(piece)
    return pieces

def path(rings):
    pieces=[piece for ring in rings for piece in split(ring)]
    return ''.join('M'+'L'.join(f'{(x+180)*1000/360:.2f},{(85-y)*1000/360:.2f}' for x,y in piece)+'Z' for piece in pieces)

def write_atomic(file,content):
    temporary=file.with_suffix(file.suffix+'.tmp');temporary.write_text(content);os.replace(temporary,file)

land=''.join(path(rings) for geometry,rings in decode(a.land,'land'))
module="import type {CSSProperties} from 'react'\n// Natural Earth public-domain coastlines via world-atlas 2.0.2 (ISC).\n// Rings are unwrapped and clipped at ±180° before projection.\nexport const worldLandPath="+json.dumps(land)+"\nexport function WorldLand({fill='#8da3af',stroke,strokeWidth=0,style}:{fill?:string;stroke?:string;strokeWidth?:number;style?:CSSProperties}){return <svg width=\"100%\" height=\"100%\" viewBox=\"0 0 1000 425\" preserveAspectRatio=\"xMidYMid meet\" style={style} aria-hidden=\"true\"><path d={worldLandPath} fill={fill} fillRule=\"evenodd\" stroke={stroke} strokeWidth={strokeWidth}/></svg>}\n"
write_atomic(root/'src/graphics/world-land.tsx',module)
countries=[{'id':g.get('id'),'name':g.get('properties',{}).get('name'),'path':path(rings)} for g,rings in decode(a.countries,'countries')]
write_atomic(root/'src/graphics/world-countries.ts','// Natural Earth public-domain boundaries via world-atlas (ISC). Dateline-clipped before projection.\nexport const worldCountries = '+json.dumps(countries,ensure_ascii=False)+' as const\n')
report={'method':'Unwrap longitude continuously, split/clip polygons at ±180 degrees, then project; keep separate pieces instead of drawing a line across the globe.',
        'projectionViewBox':[0,0,1000,425],'countries':len(countries),'landPathSha256':hashlib.sha256(land.encode()).hexdigest(),
        'inputSha256':{pathlib.Path(f).name:hashlib.sha256(pathlib.Path(f).read_bytes()).hexdigest() for f in [a.land,a.countries]}}
(root/'review/quality/world-map-correction.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
