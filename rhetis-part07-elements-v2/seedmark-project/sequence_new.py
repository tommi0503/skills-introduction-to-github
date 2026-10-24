def apply(D):
 D['steps']=D['steps'].replace('${display:grid;','${container-name:seedmark-steps;display:grid;').replace('35cqh','55cqh')
 D['steps']=D['steps'].replace('@container(max-width:600px)','@container seedmark-steps(max-width:600px)').replace('@container(max-height:180px)','@container seedmark-steps(max-height:130px)')
 D['steps']+='''
$:not(.col):before{content:'';position:absolute;left:0;right:0;top:26%;bottom:0;border:var(--stroke) solid var(--n-3);border-radius:999px;z-index:-1;}
$:not(.col) .step{gap:0;}
$:not(.col) .step>.name{margin-top:calc(var(--gap-sm)*-1.75);}
$:not(.col) .step>.note{margin-top:var(--gap-sm);}
'''
