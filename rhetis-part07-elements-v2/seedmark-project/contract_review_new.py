def apply(D):
 D['card']=D['card'].replace('$ .parts:has(>.note:nth-child(2 of .note)){height:min(100%,calc(var(--pad)*9));','$ .parts:has(>.note:nth-child(2 of .note)){height:100%;')
 D['card']=D['card'].replace('grid-template-rows:20px 56px minmax(0,1fr) minmax(0,auto);','grid-template-rows:20px 56px minmax(0,1fr) min(80px,26cqh);')
 D['card']+='\n$ .parts>.note>.icon{display:inline-flex;width:var(--type-16);height:var(--type-16);vertical-align:middle;margin-right:calc(var(--gap-sm)/2);}\n'
 D['person']+='\n$.person>.note:nth-child(2 of .note){height:62px;width:100%;flex:none;text-align:left;color:var(--ink);font-size:var(--type-12);line-height:var(--body-line);}\n$.person>.note:nth-child(2 of .note)>.icon{display:inline-flex;width:var(--type-12);height:var(--type-12);vertical-align:middle;margin-right:calc(var(--gap-sm)/3);}\n'
 D['pricing']=D['pricing'].replace('height:min(100%,calc(var(--pad)*13))','height:min(100%,calc(var(--pad)*16))').replace('grid-template-rows:26px 60px 58px minmax(0,1fr)','grid-template-rows:26px 60px calc(var(--type-40)*var(--name-line) + var(--gap-sm) + var(--stroke)) minmax(0,1fr)')
 D['pricing']+='\n$.plan>.list{align-self:stretch;height:100%;}\n'
 D['versus']+='\n$ .side>.list{flex:1;align-self:stretch;}\n'
 D['matrix']+='\n$.swot .cell>.list{flex:1;align-self:stretch;}\n'
 D['pricing']=D['pricing'].replace('$ .name{','$.plan>.name,$.plans>.plan>.name{')
 D['pricing']+='\n$.plan{grid-template-columns:minmax(0,1fr);justify-content:stretch;}\n'
 D['matrix']=D['matrix'].replace('$ .name{','$ .cell>.name{').replace('$ .note{','$ .cell>.note{')
