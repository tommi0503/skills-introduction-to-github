import fs from 'node:fs/promises';
let css=await fs.readFile('src/style.css','utf8');const faces=[...css.matchAll(/@font-face\{[^}]+\}/g)].map(m=>m[0]);let fonts=faces.join('\n');
for(const file of ['PretendardVariable.woff2','BlackHanSans-Regular.ttf','NotoSansCJKkr-Regular.woff','NotoSansCJKkr-Bold.woff'])fonts=fonts.replaceAll('../public/fonts/'+file,'data:application/octet-stream;base64,'+(await fs.readFile('public/fonts/'+file)).toString('base64'));
for(const file of ['light.html','dark.html']){let html=await fs.readFile(file,'utf8');html=html.replace(/<style data-fonts>[\s\S]*?<\/style>/,'').replace('</head>',`<style data-fonts>${fonts}</style></head>`);await fs.writeFile(file,html);}console.log('Embedded local font files in light/dark preview sheets.');
