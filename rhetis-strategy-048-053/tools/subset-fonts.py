from pathlib import Path
from fontTools import subset
p=Path(__file__).resolve().parents[1]
text=''.join(f.read_text() for f in list((p/'src').rglob('*.js'))+list((p/'strategy-blueprint').rglob('*.html')))+''.join(chr(i) for i in range(32,127))
for source,name in [('Regular','NotoSansCJKkr-Regular'),('Bold','NotoSansCJKkr-Bold')]:
 options=subset.Options();options.font_number=1;options.flavor='woff';options.layout_features=['*'];font=subset.load_font('/usr/share/fonts/opentype/noto/NotoSansCJK-'+source+'.ttc',options);s=subset.Subsetter(options=options);s.populate(text=text);s.subset(font);subset.save_font(font,str(p/'public/fonts'/f'{name}.woff'),options)
 print(name,'saved')
