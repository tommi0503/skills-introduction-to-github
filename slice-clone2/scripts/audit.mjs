// Layout QA for every slide: reports text that (1) leaves the slide, (2) overflows its own box
// (scrollWidth/Height > client), (3) overlaps another text block, (4) is clipped by an overflow:hidden ancestor.
// Usage: node scripts/audit.mjs [NN ...]   -> prints issues, writes shots/audit.json
import { createServer } from 'vite'
import { chromium } from 'playwright-core'
import { readdirSync, writeFileSync, mkdirSync } from 'node:fs'

let ids = process.argv.slice(2)
if (!ids.length) ids = readdirSync('src/decks').filter((d) => /^d\d\d$/.test(d)).map((d) => d.slice(1))
const server = await createServer({ logLevel: 'error', server: { port: 0, host: '127.0.0.1' } })
await server.listen()
const { port } = server.httpServer.address()
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' })
const page = await browser.newPage({ viewport: { width: 2720, height: 1600 } })
const all = {}
for (const id of ids) {
  await page.goto(`http://127.0.0.1:${port}/#/${id}`, { waitUntil: 'networkidle' })
  await page.evaluate(() => document.fonts.ready)
  await page.waitForTimeout(200)
  const issues = await page.evaluate(() => {
    const out = []
    const slides = [...document.querySelectorAll('[data-stage] > section')]
    slides.forEach((slide, si) => {
      const sr = slide.getBoundingClientRect()
      // text-bearing leaf-ish elements
      const els = [...slide.querySelectorAll('*')].filter((el) =>
        [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim()))
      const boxes = []
      for (const el of els) {
        const cs = getComputedStyle(el)
        if (cs.visibility === 'hidden' || +cs.opacity === 0) continue
        const range = document.createRange(); range.selectNodeContents(el)
        const rects = [...range.getClientRects()].filter((r) => r.width > 0 && r.height > 0)
        if (!rects.length) continue
        const r = { l: Math.min(...rects.map((q) => q.left)), t: Math.min(...rects.map((q) => q.top)), r: Math.max(...rects.map((q) => q.right)), b: Math.max(...rects.map((q) => q.bottom)) }
        const text = el.textContent.trim().slice(0, 40)
        const tol = 2
        if (r.l < sr.left - tol || r.r > sr.right + tol || r.t < sr.top - tol || r.b > sr.bottom + tol)
          out.push({ slide: si, kind: 'off-slide', text })
        if (el.scrollWidth > el.clientWidth + 2 && cs.overflow !== 'visible' && cs.textOverflow !== 'ellipsis')
          out.push({ slide: si, kind: 'clipped-x', text })
        // clipped by an overflow-hidden ancestor (inside slide)
        let a = el.parentElement
        while (a && a !== slide) {
          const acs = getComputedStyle(a)
          if (acs.overflow !== 'visible' || acs.overflowX !== 'visible') {
            const ar = a.getBoundingClientRect()
            if (r.r > ar.right + tol || r.b > ar.bottom + tol || r.l < ar.left - tol || r.t < ar.top - tol) { out.push({ slide: si, kind: 'clipped-by-parent', text }); break }
          }
          a = a.parentElement
        }
        // text spilling out of its nearest box with a background/border
        let p = el.parentElement
        while (p && p !== slide) {
          const pcs = getComputedStyle(p)
          if (pcs.backgroundColor !== 'rgba(0, 0, 0, 0)' || pcs.borderTopWidth !== '0px') {
            const pr = p.getBoundingClientRect()
            if (r.r > pr.right + tol || r.b > pr.bottom + tol || r.l < pr.left - tol || r.t < pr.top - tol) out.push({ slide: si, kind: 'spills-box', text })
            break
          }
          p = p.parentElement
        }
        boxes.push({ ...r, text, el })
      }
      for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) {
        const A = boxes[i], B = boxes[j]
        if (A.el.contains(B.el) || B.el.contains(A.el)) continue
        const ox = Math.min(A.r, B.r) - Math.max(A.l, B.l), oy = Math.min(A.b, B.b) - Math.max(A.t, B.t)
        const mh = Math.min(A.b - A.t, B.b - B.t); if (ox > 3 && oy > 0.3 * mh) out.push({ slide: si, kind: 'overlap', text: `${A.text} ✕ ${B.text}` })
      }
    })
    return out
  })
  all[id] = issues
  const byKind = {}
  issues.forEach((i) => (byKind[i.kind] = (byKind[i.kind] || 0) + 1))
  console.log(id, issues.length, JSON.stringify(byKind))
}
mkdirSync('shots', { recursive: true })
writeFileSync('shots/audit.json', JSON.stringify(all, null, 1))
await browser.close(); await server.close()
