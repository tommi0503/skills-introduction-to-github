// Renders every slide at 1:1 and writes shots/NN/SS.png (one PNG per slide).
// Usage: node scripts/screenshot.mjs [NN ...]   (all decks when no ids)
import { createServer } from 'vite'
import { chromium } from 'playwright-core'
import { mkdirSync, readdirSync } from 'node:fs'
import { fileURLToPath } from 'node:url'
import path from 'node:path'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
let ids = process.argv.slice(2)
if (!ids.length) ids = readdirSync(path.join(root, 'src/decks')).filter((d) => /^d\d\d$/.test(d)).map((d) => d.slice(1))

const server = await createServer({ root, logLevel: 'error', server: { port: 0, host: '127.0.0.1' } })
await server.listen()
const { port } = server.httpServer.address()
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' })
try {
  const page = await browser.newPage({ viewport: { width: 2720, height: 1600 }, deviceScaleFactor: 1 })
  page.on('pageerror', (e) => console.error('[pageerror]', e.message))
  page.on('console', (m) => m.type() === 'error' && console.error('[console]', m.text()))
  for (const id of ids) {
    await page.goto(`http://127.0.0.1:${port}/#/${id}`, { waitUntil: 'networkidle' })
    await page.evaluate(() => document.fonts.ready)
    await page.waitForTimeout(300)
    const dir = path.join(root, 'shots', id)
    mkdirSync(dir, { recursive: true })
    const slides = page.locator('[data-stage] > section')
    const n = await slides.count()
    for (let i = 0; i < n; i++) await slides.nth(i).screenshot({ path: path.join(dir, `${String(i + 1).padStart(2, '0')}.png`) })
    console.log(`[ok] ${id} (${n} slides)`)
  }
} finally {
  await browser.close()
  await server.close()
}
