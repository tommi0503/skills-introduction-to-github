"""Source-box constraints only: prohibit collapsing a member's two boundaries."""
import math

def tracks(entries,axis,extent,count):
 weights={0.:1e12,float(extent):1e12};intervals=[]
 for a in entries:
  b=a['bbox'];w=math.sqrt(max(1,b[2]*b[3]));start=float(b[axis]);end=float(b[axis]+b[axis+2]);intervals.append((start,end))
  for x in [start,end]:weights[x]=weights.get(x,0)+w
 nodes=[{'point':v,'weight':w,'values':[v]}for v,w in sorted(weights.items())]
 # Arithmetic-equivalent source endpoints must share a boundary. Retain
 # their original keys so source-to-track lookup remains exact.
 merged=[]
 for node in nodes:
  if merged and node['point']-merged[-1]['point']<=1e-6:
   prev=merged[-1];total=prev['weight']+node['weight']
   prev.update(point=(prev['point']*prev['weight']+node['point']*node['weight'])/total,weight=total,values=prev['values']+node['values'])
  else:merged.append(node)
 nodes=merged
 while len(nodes)>count+1:
  opts=[]
  for k in range(len(nodes)-1):
   a,b=nodes[k:k+2];lo=min(a['values']);hi=max(b['values'])
   if any(lo<=s and e<=hi for s,e in intervals if e>s):continue
   cost=(b['point']-a['point'])**2*a['weight']*b['weight']/(a['weight']+b['weight']);opts.append((cost,k))
  if not opts:raise ValueError('Source intervals require more distinct tracks than the foundation supplies')
  _,k=min(opts);a,b=nodes[k:k+2];w=a['weight']+b['weight'];nodes[k:k+2]=[{'point':(a['point']*a['weight']+b['point']*b['weight'])/w,'weight':w,'values':a['values']+b['values']}]
 points=[x['point']for x in nodes];points[0]=0;points[-1]=extent
 while len(points)<count+1:
  k=max(range(len(points)-1),key=lambda k:points[k+1]-points[k]);points.insert(k+1,(points[k]+points[k+1])/2);nodes.insert(k+1,{'point':points[k+1],'weight':0,'values':[]})
 index={v:k for k,a in enumerate(nodes)for v in a['values']}
 return points,index
