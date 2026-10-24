from pathlib import Path
import json
B=Path('/workspace/work/rebuild-20261024');REF=Path('/workspace/work/reference')
P={
'nocturne':{'--page':'#030508','--ink':'#ffffff','--a1':'#399fee','--a1-on':'#030508','--a1-7':'#399fee','--a1-2-soft':'#123047','--n-1':'#141b21','--n-2':'#1c232c','--n-3':'#334151','--n-4':'#546b77','--n-5':'#748190','--n-6':'#aab3c1','--n-7':'#cbd2dc','--n-8':'#dfe8f2','--n-9':'#ffffff'},
'inflexion':{'--page':'#f7fbff','--ink':'#2d2f30','--a1':'#2245ed','--a1-on':'#ffffff','--a1-7':'#2245ed','--a2':'#8fb8ff','--a3':'#d5daea','--n-1':'#f2f3f8','--n-2':'#e9edf6','--n-3':'#d5daea','--n-4':'#bec8e5','--n-5':'#9ca7bf','--n-6':'#7a869c','--n-7':'#60656a','--n-8':'#444950','--n-9':'#2d2f30'},
'diecut':{'--page':'#f6f6f6','--ink':'#050505','--a1-2-soft':'#deff3c','--a1':'#deff3c','--a1-on':'#050505','--n-1':'#ffffff','--n-2':'#dedede','--n-3':'#e6e6e6','--n-4':'#bfbfbf','--n-5':'#a7a7a7','--n-6':'#969696','--n-7':'#777777','--n-8':'#333333','--n-9':'#000000'},
'afterglow':{'--page':'#000000','--ink':'#ffffff','--a1':'#307efa','--a1-on':'#ffffff','--a1-2':'#307efa','--a1-8':'#307efa','--a1-7':'#307efa','--n-1':'#010204','--n-2':'#122b55','--n-3':'#e9e9e9','--n-4':'#bbbbbb','--n-5':'#a2a2a2','--n-6':'#969696','--n-7':'#dadada','--n-8':'#eeeeee','--n-9':'#ffffff'},
'dockside':{'--page':'#f8f8f8','--ink':'#333333','--a1':'#3198fa','--a1-on':'#ffffff','--a1-7':'#3198fa','--a1-4':'#7fc1ff','--a1-2-soft':'#d7eefa','--a2':'#e6ff91','--n-1':'#ffffff','--n-2':'#ececec','--n-3':'#dddddd','--n-4':'#cccccc','--n-5':'#aaaaaa','--n-6':'#888888','--n-7':'#777777','--n-8':'#555555','--n-9':'#333333'},
'confluence':{'--a1-1':'#308d9e','--a2-2':'#3858e3','--page':'#ffffff','--ink':'#070707','--a1':'#44cde5','--a1-on':'#ffffff','--a1-8':'#44cde5','--a1-9':'#308d9e','--a1-1-soft':'#effafd','--a2':'#3858e3','--a2-on':'#44cde5','--a2-1-soft':'#eff2fc','--n-1':'#ffffff','--n-2':'#eef2f5','--n-3':'#d5ddea','--n-4':'#c9d0db','--n-5':'#b7bec9','--n-6':'#a7aeb8','--n-7':'#979fa4','--n-8':'#626262','--n-9':'#505050'}}
for n,over in P.items():
 base=json.loads((REF/'contract/palette.json').read_text())['light']
 for k in range(1,5):
  accent=over.get('--a'+str(k),over['--a1'])
  for depth in range(1,10):
   for suffix in ['', '-soft','-muted']:
    base['--a'+str(k)+'-'+str(depth)+suffix]=('color-mix(in srgb,'+accent+' '+str(5+depth*7)+'%,'+over['--page']+')') if depth<=4 else accent
  base['--a'+str(k)]=accent;base['--a'+str(k)+'-on']=over.get('--a'+str(k)+'-on',over.get('--a1-on','#ffffff'))
 base.update(over);(B/n/'review/source-palette.json').write_text(json.dumps({'light':base,'dark':base},indent=2))
print('six host palettes; collection CSS contains roles only')
