import re

def normalize(text,name):
 def fix_first(m):
  a=m.group();found=re.search(r'style="([^"]*)"',a);data=[]
  if found:data=[x.strip() for x in found.group(1).split(';') if x.strip().startswith('--')]
  style='grid-column:1 / span 12;grid-row:1 / span 6'+(';'+';'.join(data)if data else'')
  if found:a=a[:found.start()]+'style="'+style+'"'+a[found.end():]
  else:a=a[:-1]+' style="'+style+'">'
  if 'class="prose"'in a and 'data-el='not in a:a=a[:-1]+' data-el="'+name+'-prose">'
  return a
 text=re.sub(r'<(?![!/?])[^>]+>',fix_first,text,count=1)
 def scope(m):
  a=m.group();cl=re.search(r'class="([^"]*)"',a)
  if cl and 'data-el='not in a:
   classes=cl.group(1).split();leaf=next((x for x in ['list','tag','prose']if x in classes),None)
   if not leaf and 'hl'in classes:leaf='tag'
   if leaf:a=a[:-1]+' data-el="'+name+'-'+leaf+'">'
  return a
 text=re.sub(r'<(?:ul|ol|span|b|div)\b[^>]*>',scope,text)
 def item(m):
  attrs,body=m.groups();cl=re.search(r'class="([^"]*)"',attrs)
  if not cl:attrs+=' class="item"'
  elif 'item'not in cl.group(1).split():attrs=attrs[:cl.start(1)]+cl.group(1)+' item'+attrs[cl.end(1):]
  if not re.search(r'class="[^"]*\bname\b',body):body='<span class="name">'+body+'</span>'
  return '<li'+attrs+'>'+body+'</li>'
 return re.sub(r'<li\b([^>]*)>(.*?)</li>',item,text,flags=re.S)
