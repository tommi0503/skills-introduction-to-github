def apply(D):
 D['card']+='''
$ .parts:has(>.mark):has(>.kick){padding-left:min(calc(var(--pad)*3.9),11.8cqw);padding-right:min(calc(var(--pad)*3.9),9.55cqw);gap:0;}
$ .parts:has(>.mark):has(>.kick)>.kick{font-size:clamp(var(--type-12),min(3.65cqw,4.1cqh),var(--type-24));}
$ .parts:has(>.mark):has(>.kick)>.note{margin-top:8.5cqh;font-size:clamp(var(--type-16),min(4.78cqw,5.36cqh),var(--type-28));}
'''
 D['tag']=D['tag'].replace('align-self:center;justify-self:center;','align-self:start;justify-self:start;')
 D['concentric']+='\n${width:100%;height:100%;max-width:476px;max-height:476px;align-self:end;justify-self:start;}'
