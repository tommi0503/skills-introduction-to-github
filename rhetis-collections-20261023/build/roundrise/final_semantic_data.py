from pathlib import Path
R=Path('/workspace/output/roundrise/elements')
p=R/'treemap/fixtures/treemap-5.html';s=p.read_text();
for a,b in [('58.8','34'),('23.8','26'),('11.9','18'),('3.8','12'),('1.7','10'),('812억','437억'),('231억','234억'),('98억','100억'),('94억','132억'),('71억','99억'),('52억','154억'),('24억','128억')]:s=s.replace(a,b)
p.write_text(s)
p=R/'funnel/element.css';s=p.read_text()+'''\n/* Values determine the filled surface, while labels retain a readable anchor. */
.funnel[data-el="roundrise-funnel"]>.stage{width:100%;min-width:0;padding:var(--gap-sm) var(--pad);background:none;position:relative;isolation:isolate;}
.funnel[data-el="roundrise-funnel"]>.stage::before{content:'';position:absolute;left:50%;top:0;bottom:0;width:calc(var(--v)*1%);transform:translateX(-50%);border-radius:var(--radius-sm);background:var(--a1-1-soft);z-index:-1;}
.funnel[data-el="roundrise-funnel"]>.stage:first-child{background:none;color:var(--ink);}
.funnel[data-el="roundrise-funnel"]>.stage:first-child::before{background:var(--a1);}
.funnel[data-el="roundrise-funnel"]>.stage:first-child:has(.name){color:var(--a1-on);}
''';p.write_text(s)
p=R/'sankey/element.css';p.write_text(p.read_text()+'''\n.sankey[data-el="roundrise-sankey"]>.branch:not(.on):not(.out)::before,.sankey[data-el="roundrise-sankey"]>.branch>.branch:not(.out)::before{background:var(--a1-1-soft);}
''')
