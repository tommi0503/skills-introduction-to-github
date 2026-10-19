import fs from 'node:fs/promises';
for(const name of ['outputs','pdfs'])await fs.cp(name,`dist/${name}`,{recursive:true});
console.log('Copied standalone previews and PDFs into dist.');
