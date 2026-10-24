from pathlib import Path
B=Path('/workspace/work/rebuild-20261024')
for n in ['afterglow','confluence']:
 p=B/n/'collection'/n/'elements/hub/element.css';s=p.read_text();root=f'.hub[data-el="{n}-hub"]';cut=f'{root}>.spoke:nth-child(6){{left:35%;top:0%;}}\n{root}>.spoke:nth-child(7){{left:35%;top:68%;}}'
 replacement='\n'.join([root+'>.core>.icon{position:absolute;left:22.5%;top:22.5%;display:block;width:55%;height:55%;}',root+':has(>.spoke:nth-child(5 of .spoke))>.core{width:26%;padding:3%;}',root+'>.spoke:nth-child(6){left:35%;top:0%;height:18%;text-align:center;align-items:center;}',root+'>.spoke:nth-child(7){left:35%;top:82%;height:18%;text-align:center;align-items:center;}'])
 assert cut in s;s=s.replace(cut,replacement);p.write_text(s)
 p=B/n/'collection'/n/'elements/timeline/fixtures/business-1.html';s=p.read_text();assert '>2027</b>'in s;p.write_text(s.replace('>2027</b>','>2055</b>'))
p=B/'tools/fresh_parent_elements.py';s=p.read_text();s=s.replace("v=d.strip().replace('2055','2027').replace('2060','2027').replace('2080','2027')","v=d.strip()")
# Regenerating this module must retain the same member-count and icon-seat rules.
needle="  s+='@container (max-height:400px){'+r('>.core>.kick,'+root+'>.core>.note','display:none;')"
rep="  s+=r('>.core>.icon','position:absolute;left:22.5%;top:22.5%;display:block;width:55%;height:55%;')+r(':has(>.spoke:nth-child(5 of .spoke))>.core','width:26%;padding:3%;')+r('>.spoke:nth-child(6)','left:35%;top:0%;height:18%;text-align:center;align-items:center;')+r('>.spoke:nth-child(7)','left:35%;top:82%;height:18%;text-align:center;align-items:center;')\n"+needle
assert needle in s;s=s.replace(needle,rep);p.write_text(s)
# Optical review: make the optional fifth/sixth spokes fit the upper/lower bands.
for n in ['afterglow','confluence']:
 p=B/n/'collection'/n/'elements/hub/element.css';s=p.read_text();root=f'.hub[data-el="{n}-hub"]';s+='\n'+root+'>.spoke:nth-child(n+6)>.name{font-size:clamp(var(--type-18),3cqw,var(--type-32));}\n';p.write_text(s)
 p=B/n/'collection'/n/'elements/bullet/fixtures/business-2.html';s=p.read_text().replace('--v:104','--v:94').replace('104%','94%').replace('>44.6</b>','>92%</b>');p.write_text(s)
p=B/'tools/fresh_parent_elements.py';s=p.read_text();needle="  s+='@container (max-height:400px){'+r('>.core>.kick,'+root+'>.core>.note','display:none;')";s=s.replace(needle,"  s+=r('>.spoke:nth-child(n+6)>.name','font-size:clamp(var(--type-18),3cqw,var(--type-32));')\n"+needle);p.write_text(s)
