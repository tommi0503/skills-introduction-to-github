"""Final measured corrections from the first native size-sheet review."""
import re
def apply(D):
 D['chart-bar']=D['chart-bar'].replace('max-width:calc(var(--pad)*5);white-space:normal;','width:calc(var(--pad)*5);max-width:calc(var(--pad)*5);white-space:normal;')
 D['bullet']=D['bullet'].replace('flex-direction:column;gap:var(--gap);','flex-direction:column;gap:var(--gap-sm);').replace('padding:calc(var(--gap-sm)/3) var(--gap-sm) calc(var(--gap-sm)*2);','padding:0 var(--gap-sm) calc(var(--gap-sm)*1.666667);').replace('bottom:var(--gap-sm);height:14px;','bottom:calc(var(--gap-sm)/3);height:10px;').replace('bottom:calc(var(--gap-sm) + 3px);','bottom:calc(var(--gap-sm)/2);').replace('height:8px;background:var(--a1);','height:6px;background:var(--a1);').replace('bottom:calc(var(--gap-sm) - 3px);','bottom:calc(var(--gap-sm)/6);').replace('height:20px;width:2px;','height:14px;width:2px;')
 for key,v in D.items():
  # CSS math tokenization requires whitespace around subtraction; custom-property identifiers are untouched.
  v=re.sub(r'(?<![\w-])(\d+)-(?=\d)', r'\1 - ', v).replace(')-',') - ').replace(')+',') + ')
  v=v.replace('1-var(', '1 - var(').replace('1-max(', '1 - max(').replace('100%-','100% - ')
  D[key]=v
