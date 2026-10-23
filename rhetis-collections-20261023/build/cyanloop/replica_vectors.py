from pathlib import Path
p=Path('/workspace/work/cyanloop/replicas.py');s=p.read_text()
s=s.replace("paths='<path d=\"M801 247", "defs+='<linearGradient id=\"bottom2\" gradientUnits=\"userSpaceOnUse\" x1=\"801\" y1=\"0\" x2=\"1065\" y2=\"0\"><stop stop-color=\"#001134\"/><stop offset=\"1\" stop-color=\"#00a9ee\"/></linearGradient><linearGradient id=\"right2\" gradientUnits=\"userSpaceOnUse\" x1=\"1050\" y1=\"0\" x2=\"1370\" y2=\"0\"><stop stop-color=\"#0753d6\"/><stop offset=\"1\" stop-color=\"#001134\"/></linearGradient>'\n  paths='<path d=\"M801 247")
a=s.index("  paths='<path d=\"M801 247");b=s.index('\n elif n==3:',a)
s=s[:a]+'''  paths='<path d="M801 247A139 139 0 1 1 1065 160" stroke="url(#teal)" stroke-width="70"/><path d="M1065 160A139 139 0 0 1 801 247" stroke="url(#bottom2)" stroke-width="70"/><circle cx="801" cy="247" r="35" fill="#00eee2"/><path d="M1065 160A139 139 0 1 1 1340 115A139 139 0 0 1 1065 160" stroke="url(#right2)" stroke-width="70"/><circle cx="1065" cy="160" r="35" fill="#0753d6"/>'
'''+s[b:]
s=s.replace(" elif n==3:\n  paths=", " elif n==3:\n  defs+='<linearGradient id=\"blue3\" gradientUnits=\"userSpaceOnUse\" x1=\"95\" y1=\"0\" x2=\"375\" y2=\"0\"><stop stop-color=\"#0753d6\"/><stop offset=\"1\" stop-color=\"#001134\"/></linearGradient>'\n  paths=")
s=s.replace('M95 480A140 140 0 0 0 375 480" stroke="url(#blue)"', 'M95 480A140 140 0 0 0 375 480" stroke="url(#blue3)"')
s=s.replace('cx="95" cy="480" r="39" fill="#0753d6"/>\'','cx="95" cy="480" r="39" fill="#0753d6"/><circle cx="882" cy="278" r="39" fill="#00eee2"/>\'')
s=s.replace('M808 82A125 125', 'M808 82A125 160')
s=s.replace('M1056 296C1018 410 1098 490 1211 494" stroke="url(#reverse)"', 'M1056 296C1018 410 1098 490 1211 494" stroke="url(#low18)"')
s=s.replace(" else:\n  paths='<path d=\"M808", " else:\n  defs+='<linearGradient id=\"low18\" gradientUnits=\"userSpaceOnUse\" x1=\"1056\" y1=\"260\" x2=\"1211\" y2=\"494\"><stop stop-color=\"#001134\"/><stop offset=\"1\" stop-color=\"#00eee2\"/></linearGradient><linearGradient id=\"blue18\" gradientUnits=\"userSpaceOnUse\" x1=\"985\" y1=\"0\" x2=\"1285\" y2=\"0\"><stop stop-color=\"#001134\"/><stop offset=\"1\" stop-color=\"#0753d6\"/></linearGradient>'\n  paths='<path d=\"M808")
s=s.replace('M985 720A150 150 0 0 1 1285 720" stroke="url(#blue)"', 'M985 720A150 150 0 0 1 1285 720" stroke="url(#blue18)"')
s=s.replace('<svg style="position:absolute;left:393px;top:243px" width="450" height="447" viewBox="0 0 450 447"><path', '<svg style="position:absolute;left:393px;top:243px" width="450" height="447" viewBox="0 0 450 447"><defs><linearGradient id="process"><stop stop-color="#00a9ee"/><stop offset=".45" stop-color="#0753d6"/><stop offset=".75" stop-color="#001134"/></linearGradient></defs><path').replace('fill="{blue}"/><circle cx="213"','fill="url(#process)"/><circle cx="213"')
s=s.replace("tx(60,126,'HRD Learning',122", "tx(60,130,'HRD Learning',114").replace("tx(60,249,'Solution',122", "tx(60,249,'Solution',114")
s=s.replace("['book','chart','users'][i]", "['book','chart','users'][i]")
p.write_text(s)
