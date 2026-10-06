import {execFileSync} from 'node:child_process'
import {writeFile} from 'node:fs/promises'
import {buildState} from './build-state.mjs'
const before=await buildState()
execFileSync('npm',['run','typecheck'],{stdio:'inherit'})
execFileSync('node',['node_modules/vite/bin/vite.js','build'],{stdio:'inherit'})
const after=await buildState()
const stamp={...after,builtAt:new Date().toISOString(),sourceStableDuringBuild:before.sourceHash===after.sourceHash,rendererStableDuringBuild:before.rendererHash===after.rendererHash}
await writeFile('dist/build-state.json',JSON.stringify(stamp,null,2)+'\n')
console.log(`Build source snapshot: ${stamp.sourceStableDuringBuild?'stable':'changed during build; rebuild after edits finish'}`)
