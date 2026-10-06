import type { DeckDefinition } from '../../ui'
import { Abs, ImagePlaceholder } from '../../ui'
import { ChevronRight, Heart } from 'lucide-react'
import { Box, Lines } from '../../ui'
import { Display, Ellipse, Kicker, KitschSlide } from './components'
import { closing, cover, highlight, keywords, photos, process, table, toc, twoCol } from './data'
import { t } from './theme'

function Cover() {
  return (
    <KitschSlide bg={t.cream} deco={cover.deco} under={<Box x={0} y={109} w={1280} h={500} bg={t.white} />}>
      <Kicker x={640} cy={213} text={cover.kicker} size={27} />
      <Display x={640} cy={326} lines={[cover.title[0]]} size={115} color={t.tan} />
      <Display x={640} cy={457} lines={[cover.title[1]]} size={115} />
      <Lines x={640} cy={650} align="center" size={15} className="font-montserrat font-semibold tracking-[0.18em]" color="#999" lines={[cover.site]} />
    </KitschSlide>
  )
}

function Toc() {
  const r = 311
  return (
    <KitschSlide bg={t.cream} page={toc.page} under={<>
      <Box x={0} y={0} w={1280} h={320} bg={t.orange} />
      {[174, 642, 1110].map((cx) => <Abs key={cx} x={cx - r} y={184} w={r * 2} h={r * 2} className="rounded-full" style={{ background: t.cream }} />)}
    </>} deco={toc.deco}>
      <Display x={640} cy={101} lines={[toc.title]} size={70} color="#fff" />
      {toc.items.map((it, i) => {
        const x = i < 3 ? 145 : 667, y = 355 + (i % 3) * 99
        return (
          <div key={it.n}>
            <Box x={x} y={y} w={466} h={65} bg="#fff" className="rounded-full" />
            <Lines x={x + 37} cy={y + 33} size={26} className={t.latin} color={t.green} lines={[it.n]} />
            <Lines x={x + 92} cy={y + 33} size={27} color={t.ink} lines={[it.text]} />
          </div>
        )
      })}
    </KitschSlide>
  )
}

function Highlight() {
  return (
    <KitschSlide bg={t.yellow} page={highlight.page} pageRight under={<Ellipse x={361} y={181} w={852} h={479} c={t.cream} />} deco={highlight.deco}>
      <Kicker x={87} cy={114} align="left" text={highlight.kicker} />
      <Display x={82} cy={189} lh={87} align="left" lines={highlight.title} size={72} />
      <Lines x={783} cy={352} lh={55} align="center" size={33} color={t.ink} lines={highlight.body} />
    </KitschSlide>
  )
}

function Keywords() {
  return (
    <KitschSlide bg={t.cream} page={keywords.page} pageRight deco={keywords.deco}>
      <Kicker x={640} cy={121} text={keywords.kicker} />
      <Display x={640} cy={196} lines={[keywords.title]} size={74} />
      {keywords.items.map((k, i) => (
        <div key={k.name}>
          {i === 3 ? (
            <Abs x={k.cx - 68} y={318}><Heart size={136} fill="#ffa3bd" color="#ffa3bd" strokeWidth={1} /></Abs>
          ) : (
            <Abs x={k.cx - 66} y={321} w={132} h={131}><ImagePlaceholder label="keyword shape" className="h-full w-full" style={{ borderRadius: keywords.shapes[i] }} /></Abs>
          )}
          <Display x={k.cx} cy={504} lines={[k.name]} size={33} />
          <Lines x={k.cx} cy={561} lh={33} align="center" w={260} size={21} color={t.ink} lines={k.desc} />
        </div>
      ))}
    </KitschSlide>
  )
}

function TwoCol() {
  const r = 237
  return (
    <KitschSlide bg={t.yellow} page={twoCol.page} deco={twoCol.deco} under={<>
      <Box x={648} y={0} w={359} h={720} bg={t.cream} />
      {[0, 360, 720].flatMap((cy) => [648, 1007].map((cx) => <Abs key={`${cx}-${cy}`} x={cx - r} y={cy - r} w={r * 2} h={r * 2} className="rounded-full" style={{ background: t.cream }} />))}
    </>}>
      <Kicker x={91} cy={114} align="left" text={twoCol.kicker} />
      <Display x={82} cy={189} lh={87} align="left" lines={twoCol.title} size={72} />
      {twoCol.blocks.map((b) => (
        <div key={b.cy}>
          <Display x={596} cy={b.cy} align="left" lines={[b.head]} size={33} />
          <Lines x={596} cy={b.cy + 44} lh={35.9} size={21} color={t.ink} lines={b.lines} />
        </div>
      ))}
    </KitschSlide>
  )
}

function Photos() {
  return (
    <KitschSlide bg={t.cream} page={photos.page} pageRight deco={photos.deco}>
      <Abs x={1135} y={202}><ChevronRight size={60} color={t.yellow} strokeWidth={4} /></Abs>
      <Kicker x={640} cy={120} text={photos.kicker} />
      <Display x={640} cy={193} lines={[photos.title]} size={74} />
      {photos.items.map((p) => (
        <div key={p.cx}>
          <Abs x={p.cx - 132} y={292} w={264} h={183}><ImagePlaceholder label="photo" className="h-full w-full" style={{ borderRadius: '132px 132px 0 0' }} /></Abs>
          <Display x={p.cx} cy={514} lines={[p.head]} size={33} />
          <Lines x={p.cx} cy={558} lh={27.5} align="center" w={340} size={19} color={t.ink} lines={p.desc} />
        </div>
      ))}
    </KitschSlide>
  )
}

function Process() {
  return (
    <KitschSlide bg={t.cream} page={process.page} pageRight deco={process.deco} under={<>
      <Ellipse x={-571} y={71} w={2422} h={1800} c={t.yellow} />
      <Ellipse x={-253} y={332} w={1786} h={1400} c={t.orange} />
    </>}>
      {process.steps.map((s) => (
        <div key={s.head}>
          <Display x={s.cx} cy={s.cy} lines={[s.head]} size={30} />
          <Lines x={s.cx} cy={s.cy + 44} lh={32} align="center" w={260} size={20.5} color={t.ink} lines={s.desc} />
          <Abs x={s.cx - 1} y={s.cy + 128} w={0} h={s.dot - s.cy - 138} style={{ borderLeft: `2px dotted ${t.green}` }} />
          <Abs x={s.cx - 11} y={s.dot - 11} w={22} h={22} className="rounded-full bg-white" style={{ border: `5px solid ${t.green}` }} />
        </div>
      ))}
      <Kicker x={640} cy={437} text={process.kicker} size={21} />
      <Display x={640} cy={524} lh={89} lines={process.title} size={74} color="#fff" />
    </KitschSlide>
  )
}

function Table() {
  const x0 = 611, cw = 140.5
  const rowBg = ['#f9f8f4', t.creamDark, '#f9f8f4']
  return (
    <KitschSlide bg={t.cream} page={table.page} deco={table.deco}>
      <Kicker x={88} cy={254} align="left" text={table.kicker} />
      <Display x={84} cy={331} lh={101} align="left" lines={table.title} size={82} />
      <Box x={x0} y={210} w={cw * 4} h={74} bg={t.green} />
      {table.cols.map((c, i) => (
        <div key={c}>
          {i > 0 && <Box x={x0 + i * cw} y={210} w={1} h={74} bg="#1d7a60" />}
          <Lines x={x0 + cw * (i + 0.5)} cy={248} align="center" w={cw} size={22} className={t.latin} color="#fff" lines={[c]} />
        </div>
      ))}
      {table.rows.map((row, r) => (
        <div key={r}>
          <Box x={x0} y={284 + r * 74} w={cw * 4} h={74} bg={rowBg[r]} />
          {row.map((cell, i) => <Lines key={i} x={x0 + cw * (i + 0.5) - 3} cy={322 + r * 74} align="center" w={cw} size={19} color="#333" lines={[cell]} />)}
        </div>
      ))}
      <Box x={x0} y={505} w={cw * 4} h={2} bg={t.green} />
      <Lines x={890} cy={537} lh={31} align="center" w={562} size={18} color="#333" lines={table.caption} />
    </KitschSlide>
  )
}

function Closing() {
  return (
    <KitschSlide bg="#015d49" deco={closing.deco}>
      <Kicker x={640} cy={212} text={closing.kicker} size={27} color={t.yellow} />
      <Display x={640} cy={326} lh={130} lines={closing.title} size={112} color="#fff" />
    </KitschSlide>
  )
}

const deck: DeckDefinition = { id: '07', title: '주황색과 노랑의 키치한 기본 레이아웃 발표자료', slides: [Cover, Toc, Highlight, Keywords, TwoCol, Photos, Process, Table, Closing] }
export default deck
