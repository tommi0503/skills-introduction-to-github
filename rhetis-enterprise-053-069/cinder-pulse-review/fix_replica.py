from pathlib import Path
p=Path(__file__).parent/'build_replica.py';s=p.read_text()
s=s.replace("+f'\">{txt}</div>'", "+f'\">{txt}</div>'")
s=s.replace('{txt}</div>\'\ndef arrow','<div style="text-align:center">{txt}</div></div>\'\ndef arrow')
s=s.replace("s=caps([(-17,137,440),(103,214,440),(223,57,440),(343,151,440),(1054,-222,440),(1174,-128,440)],color='#484847')", "s=caps([(-17,137,440),(103,214,440),(223,57,440),(343,151,440),(1054,-222,440),(1174,-128,440)],color='#484847').replace('#ff3e0c','#484847')")
s=s.replace("text(533,307,700,'Thank you',88", "text(533,293,700,'Thank you',88")
# Remove placeholder icon characters and draw geometry, not character symbols.
s=s.replace("'◎'", "'<svg viewBox=\"0 0 24 24\" width=\"32\" height=\"32\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1\"><circle cx=\"12\" cy=\"12\" r=\"9\"/><circle cx=\"12\" cy=\"12\" r=\"6\"/><circle cx=\"12\" cy=\"12\" r=\"3\"/><path d=\"M12 12L22 2M16 2H22V8\"/></svg>'")
s=s.replace("'<span style=\"font-size:24px\">◇</span><br>'+stepls[i][0]", "'<svg viewBox=\"0 0 24 24\" width=\"28\" height=\"28\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1\"><rect x=\"4\" y=\"3\" width=\"16\" height=\"18\" rx=\"2\"/><path d=\"M8 8H16M8 12H16M8 16H13\"/></svg><br>'+stepls[i][0]")
s=s.replace("'◇','#c4c4c4'", "'<svg viewBox=\"0 0 24 24\" width=\"48\" height=\"48\" fill=\"none\" stroke=\"currentColor\" stroke-width=\".7\"><circle cx=\"12\" cy=\"12\" r=\"10\"/><ellipse cx=\"12\" cy=\"12\" rx=\"4\" ry=\"10\"/><path d=\"M2 12H22M4 6H20M4 18H20\"/></svg>','#c4c4c4'")
# repair financial table neutral subheader and uniform rows; keep stripe selection.
s=s.replace("(OUT/f'slide_{i:02}.html').write_text", "\n if i==6:s+='<style>table thead th{background:#f5f5f5}table td{height:51px}table:nth-child(1) td:last-child{background:inherit}</style>'\n if i==10:s+='<style>table td{height:42px}table th{font-size:20px}table tbody tr:nth-child(even){background:#f0f0f0}</style>'\n (OUT/f'slide_{i:02}.html').write_text")
p.write_text(s)
