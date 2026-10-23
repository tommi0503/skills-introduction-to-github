from pathlib import Path
p=Path(__file__).with_name('refine_fidelity.py');s=p.read_text()
needle="css('legend','''"
insert="""# Fig-only source content uses flexible card.parts, not metric's named figure structure.
mp=C/'elements/metric/element.css';ms=mp.read_text().split(MARK,1)[1].replace('[data-el="vectorbox-metric"]','[data-el="vectorbox-card"]').replace('.stat.on.quiet','.quiet.on.line').replace('.stat.on','.quiet.on').replace('.stat.quiet','.quiet')
ms=ms.replace('[data-el="vectorbox-card"].quiet.on{','[data-el="vectorbox-card"].quiet.on{display:flex;justify-content:flex-start;').replace('[data-el="vectorbox-card"].quiet.on .parts{','[data-el="vectorbox-card"].quiet.on .parts{display:flex;flex-direction:column;align-items:center;height:auto;')
ms+='[data-el="vectorbox-card"].quiet:has(.parts>.fig>.icon){display:flex;justify-content:center;align-items:center;background:none;padding:0}[data-el="vectorbox-card"].quiet:has(.parts>.fig>.icon) .parts{height:auto;display:block}[data-el="vectorbox-card"].quiet:has(.parts>.fig>.icon) .fig{margin:0}'
cp=C/'elements/card/element.css';cp.write_text(cp.read_text()+'\\n'+ms+'\\n');css('metric','')
"""
s=s.replace(needle,insert+needle)
s=s.replace("el('metric','stat on '+quiet+' '+tone", "el('card','card quiet on '+('line' if quiet else '')+' '+tone")
s=s.replace("el('metric','stat quiet','<div class=\"parts\"><b class=\"fig\">'+ic('database')", "el('card','card quiet','<div class=\"parts\"><b class=\"fig\">'+ic('database')")
p.write_text(s)
p=p.parent/'add_fidelity_fixtures.py';s=p.read_text();s=s.replace("write('elements/metric','source-burst-pair.html',group(document(4).xpath('//*[@data-el=\"vectorbox-metric\"]')),'6x3')", "write('elements/card','source-burst-pair.html',group(document(4).xpath('//*[@data-el=\"vectorbox-card\" and contains(concat(\" \",@class,\" \"),\" on \")]')),'6x3')\nwrite('elements/card','source-icon-figure.html',standalone(document(10).xpath('//*[@data-el=\"vectorbox-card\" and contains(concat(\" \",@class,\" \"),\" quiet \")]')[0]),'3x3')")
# Budget card is now second card; caption fixture excludes the independent burst cards.
s=s.replace("root(10,'card')),'5x5'", "root(10,'card',1)),'5x5'").replace("group(document(4).xpath('//*[@data-el=\"vectorbox-card\"]')),'6x4'", "group(document(4).xpath('//*[@data-el=\"vectorbox-card\" and not(contains(concat(\" \",@class,\" \"),\" on \"))]')),'6x4'")
p.write_text(s)
