// Renders showcases at 1:1 and writes shots/<id>.png plus comparison images.
// Usage: node scripts/screenshot.mjs 01 02 ...            (all when no ids)
//        node scripts/screenshot.mjs 01 --crop x,y,w,h     (zoomed region compare)
import { createServer } from 'vite'
import { chromium } from 'playwright-core'
import { execFileSync } from 'node:child_process'
import { mkdirSync, readdirSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import path from 'node:path'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const args = process.argv.slice(2)
const cropIdx = args.indexOf('--crop')
const crop = cropIdx >= 0 ? args.splice(cropIdx, 2)[1] : null
let ids = args
if (ids.length === 0) {
  ids = readdirSync(path.join(root, 'src/decks'))
    .filter((d) => /^d\d\d$/.test(d))
    .map((d) => d.slice(1))
}

mkdirSync(path.join(root, 'shots'), { recursive: true })
const server = await createServer({ root, logLevel: 'error', server: { port: 0, host: '127.0.0.1' } })
await server.listen()
const { port } = server.httpServer.address()
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' }).catch(() =>
  chromium.launch(),
)

try {
  const page = await browser.newPage({ viewport: { width: 2720, height: 1600 }, deviceScaleFactor: 1 })
  page.on('pageerror', (e) => console.error('[pageerror]', e.message))
  page.on('console', (m) => m.type() === 'error' && console.error('[console]', m.text()))
  for (const id of ids) {
    await page.goto(`http://127.0.0.1:${port}/#/${id}`, { waitUntil: 'networkidle' })
    await page.evaluate(() => document.fonts.ready)
    await page.waitForTimeout(300)
    const stage = page.locator('[data-stage]').first()
    const out = path.join(root, 'shots', `${id}.png`)
    await stage.screenshot({ path: out })
    const pyArgs = [path.join(root, 'scripts/compare.py'), id]
    if (crop) pyArgs.push('--crop', crop)
    console.log('[ok] ' + id)
  }
} finally {
  await browser.close()
  await server.close()
}
