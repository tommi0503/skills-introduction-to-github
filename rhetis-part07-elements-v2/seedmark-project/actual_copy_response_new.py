def apply(D):
 # The measured base contains three display lines. Bound its type by its actual own height.
 D['headline']+='\n$ h2{font-size:clamp(var(--type-28),min(7.9cqw,22.5cqh),var(--type-44));}\n'
 D['card']+='''
@container(min-aspect-ratio:2/1){$ .parts:has(>.mark):not(:has(>.kick,>.fig)){height:100%;grid-template-columns:54px minmax(0,1fr);grid-template-rows:auto auto;padding:var(--gap-sm);gap:calc(var(--gap-sm)/2) var(--gap-sm);align-content:center;}$ .parts:has(>.mark):not(:has(>.kick,>.fig))>.mark{grid-column:1;grid-row:1/span 2;align-self:center;}$ .parts:has(>.mark):not(:has(>.kick,>.fig))>.name{grid-column:2;grid-row:1;align-self:start;font-size:var(--type-22);}$ .parts:has(>.mark):not(:has(>.kick,>.fig))>.note{grid-column:2;grid-row:2;align-self:start;font-size:var(--type-16);}}
'''
 D['list']=D['list'].replace('gap:calc(var(--gap-sm)/2);padding:calc(var(--gap-sm)/2);counter-reset:item;','gap:calc(var(--gap-sm)/3);padding:calc(var(--gap-sm)/3);counter-reset:item;')
 D['list']+='''
@container(max-height:75px){$ .item{font-size:var(--type-12);gap:calc(var(--gap-sm)/6);padding-top:0;padding-bottom:0;}$ .name{font-size:var(--type-12);line-height:var(--label-line);}$ .note{font-size:var(--type-10);line-height:var(--label-line);}}
'''
 D['prose']+='\n@container(max-height:250px){$ p:has(>br:nth-of-type(6)){margin-bottom:auto;font-size:var(--type-14);}}\n'
