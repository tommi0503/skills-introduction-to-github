import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const prior=path.resolve(root,'../eonu-ir-20261021-v2');
function load(folder){const c={window:{}};vm.createContext(c);for(const file of ['components.js','slides.js'])vm.runInContext(fs.readFileSync(path.join(folder,'src',file),'utf8'),c);return c.window.EONU;}
const before=load(prior),after=load(root);
const count=html=>html.replace(/<[^>]*>/g,'').replace(/\s/g,'').length;
const pages=after.slides.map((s,i)=>({id:s.id,v2Characters:count(before.renderSlide(before.slides[i])),v3Characters:count(after.renderSlide(s)),talkUnchanged:s.talk===before.slides[i].talk}));
const total2=pages.reduce((n,p)=>n+p.v2Characters,0),total3=pages.reduce((n,p)=>n+p.v3Characters,0);
const report={measurement:'Text in slide markup, excluding HTML tags and whitespace; notes excluded.',v2Characters:total2,v3Characters:total3,reductionPercent:Math.round((1-total3/total2)*1000)/10,talksUnchanged:pages.every(p=>p.talkUnchanged),pages};
fs.writeFileSync(path.join(root,'review/content-density.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report,null,2));
