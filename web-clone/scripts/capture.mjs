// Captures the live reference page: public/reference/NN.png (full page, 1440 wide) and
// public/flat/NN.png = the first FRAME_H px (the comparison target), plus NN.html/NN.json dumps.
import { chromium } from 'playwright-core'
import { mkdirSync, writeFileSync } from 'node:fs'

export const SITES = {
  '01': 'https://www.cartesia.ai/',
  '02': 'https://aside.com/',
  '03': 'https://www.harvey.ai/',
  '04': 'https://www.cloudflare.com/',
  '05': 'https://www.monologue.to/',
  '06': 'https://x.ai/',
  '07': 'https://mobbin.com/sites/calendly-d3909122-0ee1-4966-b27c-633ea9a7848c/b4d46a46-7aa6-4490-81c3-c1015516082d/preview',
  '08': 'https://calendly.com/',
  '09': 'https://www.cosmos.so/',
  '10': 'https://giga.ai/',
  '11': 'https://useorigin.com/',
  '12': 'https://www.ada.cx/',
  '13': 'https://retool.com/',
  '14': 'https://www.gitbook.com/',
}
const W = 1440, FRAME_H = 4500
const ids = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(SITES)
mkdirSync('public/reference', { recursive: true }); mkdirSync('public/flat', { recursive: true }); mkdirSync('reference-dom', { recursive: true })
const browser = await chromium.launch({
  executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
  headless: process.env.HEADFUL ? false : true,
  args: ['--disable-blink-features=AutomationControlled'],
})
const ctx = await browser.newContext({
  viewport: { width: W, height: 900 }, deviceScaleFactor: 1, ignoreHTTPSErrors: false,
  userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
  locale: 'en-US',
})
for (const id of ids) {
  const page = await ctx.newPage()
  try {
    await page.goto(SITES[id], { waitUntil: 'domcontentloaded', timeout: 60000 })
    await page.waitForTimeout(4000)
    for (let i = 0; i < 12 && /Just a moment/.test(await page.title()); i++) await page.waitForTimeout(2500)
    // scroll through to trigger lazy content / reveal animations, then back to top
    await page.evaluate(async () => {
      for (let y = 0; y < Math.min(document.body.scrollHeight, 12000); y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 250)) }
      window.scrollTo(0, 0); await new Promise(r => setTimeout(r, 1500))
    })
    // freeze animations so the capture is stable
    await page.addStyleTag({ content: '*,*::before,*::after{animation-play-state:paused!important;transition:none!important;caret-color:transparent!important}' })
    const h = await page.evaluate(() => document.documentElement.scrollHeight)
    await page.screenshot({ path: `public/reference/${id}.png`, fullPage: true })
    await page.screenshot({ path: `public/flat/${id}.png`, clip: { x: 0, y: 0, width: W, height: Math.min(FRAME_H, h) }, fullPage: true })
    writeFileSync(`reference-dom/${id}.html`, await page.content())
    // compact computed-style dump of visible text elements in the frame (for exact fonts/sizes/colours)
    const dump = await page.evaluate((FH) => {
      const out = []
      const els = document.querySelectorAll('body *')
      for (const el of els) {
        const r = el.getBoundingClientRect(); const y = r.top + window.scrollY
        if (r.width < 2 || r.height < 2 || y > FH) continue
        const own = [...el.childNodes].filter(n => n.nodeType === 3 && n.textContent.trim()).map(n => n.textContent.trim()).join(' ')
        const cs = getComputedStyle(el)
        const isMedia = ['IMG', 'VIDEO', 'CANVAS', 'SVG', 'svg', 'PICTURE'].includes(el.tagName) || cs.backgroundImage !== 'none'
        if (!own && !isMedia) continue
        out.push({ tag: el.tagName.toLowerCase(), text: own.slice(0, 160), x: Math.round(r.left), y: Math.round(y), w: Math.round(r.width), h: Math.round(r.height),
          font: cs.fontFamily.split(',')[0].replace(/["']/g, ''), size: cs.fontSize, weight: cs.fontWeight, lh: cs.lineHeight, ls: cs.letterSpacing,
          color: cs.color, bg: cs.backgroundColor !== 'rgba(0, 0, 0, 0)' ? cs.backgroundColor : undefined, radius: cs.borderRadius !== '0px' ? cs.borderRadius : undefined,
          media: isMedia ? (el.tagName.toLowerCase() + (cs.backgroundImage !== 'none' ? ':bg' : '')) : undefined })
      }
      return { title: document.title, height: document.documentElement.scrollHeight, bodyBg: getComputedStyle(document.body).backgroundColor, items: out }
    }, FRAME_H)
    writeFileSync(`reference-dom/${id}.json`, JSON.stringify(dump, null, 0))
    console.log(`[ok] ${id} ${SITES[id]} height=${h} title="${dump.title}" items=${dump.items.length}`)
  } catch (e) {
    console.log(`[fail] ${id} ${e.message.split('\n')[0]}`)
  } finally { await page.close() }
}
await browser.close()
