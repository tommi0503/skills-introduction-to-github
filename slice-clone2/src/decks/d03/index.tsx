import type { DeckDefinition } from '../../ui'
import { Abs, ImagePlaceholder, Slide, cn } from '../../ui'
import { Bullets, PageSlide, Paras, SectionHead, Summary } from './components'
import { analysis, background, cause, compare, conclusion, cover, status, table, toc } from './data'
import { Box, Donut, Lines } from '../../ui'
import { t } from './theme'

function Cover() {
  return (
    <Slide background="#fff" className={t.sans}>
      <Abs x={60} y={33} w={134} h={35}><ImagePlaceholder label="institution logo" className="h-full w-full" /></Abs>
      <Lines x={1235} cy={43} align="right" size={15} className={cn(t.latin, 'font-bold')} color={t.navy} lines={[cover.date]} />
      <Box x={0} y={360} w={1280} h={360} bg={t.blue} />
      <Lines x={640} cy={321} align="center" size={70} className={t.head} color={t.navy} lines={[cover.title]} />
      <Lines x={640} cy={408} align="center" size={70} className={t.head} color="#fff" lines={[cover.title2]} />
      <Lines x={640} cy={467} align="center" size={19} className={cn(t.latin, "tracking-[0.03em]")} color="#fff" lines={[cover.sub]} />
      <Lines x={640} cy={648} align="center" size={20} className="font-extrabold" color="#fff" lines={[cover.author]} />
    </Slide>
  )
}

function Toc() {
  return (
    <PageSlide page={1}>
      <SectionHead head={toc.head} />
      {toc.items.map((it, i) => {
        const y = 135 + i * 110.5
        return (
          <div key={i}>
            <Box x={645} y={y} w={4} h={93} bg={t.blue} />
            <Lines x={660} cy={y + 16} size={26} className="font-semibold tracking-[-0.02em]" color={t.navy} lines={[it.title]} />
            <Lines x={963} cy={y + 17} size={22} color="#888" lines={[it.page]} />
            <Lines x={660} cy={y + 61} lh={23} size={16} color="#444" className="tracking-[-0.02em]" lines={it.desc} />
          </div>
        )
      })}
    </PageSlide>
  )
}

function Status() {
  return (
    <PageSlide page={2}>
      <SectionHead head={status.head} />
      <Lines x={t.left} cy={383} size={33} className="font-medium italic" color="#333" lines={[status.lead]} />
      <Paras x={t.left} cy={499} paras={status.paras} gap={18} />
      <Abs x={691} y={134} w={538} h={491}><ImagePlaceholder label="status photo" className="h-full w-full" /></Abs>
      <Box x={691} y={640} w={538} h={25} bg={t.pale} />
      <Lines x={960} cy={653} align="center" size={14} color="#333" lines={[status.caption]} />
    </PageSlide>
  )
}

function Analysis() {
  return (
    <PageSlide page={3}>
      <SectionHead head={analysis.head} />
      <Box x={73} y={257} w={1132} h={166} bg={t.lav} />
      <Lines x={640} cy={313} lh={49} align="center" size={39} color="#222" lines={analysis.summary} />
      {analysis.cards.map((c, i) => {
        const x = 77 + i * 388
        return (
          <div key={c.n}>
            <Box x={x} y={452} w={352} h={227} bg={t.card} />
            <Box x={x} y={452} w={39} h={40} bg={t.badge} />
            <Lines x={x + 19.5} cy={472} align="center" w={39} size={27} className="font-light" color="#fff" lines={[c.n]} />
            <Lines x={x + 49} cy={516} size={17} className="font-bold" color="#222" lines={[c.title]} />
            <Lines x={x + 49} cy={556} lh={25} size={19} color="#333" lines={c.body} />
          </div>
        )
      })}
    </PageSlide>
  )
}

function Table() {
  const xs = [73, 245, 933, 1204]
  const rows = [302, 413, 519, 623]
  return (
    <PageSlide page={4}>
      <SectionHead head={table.head} />
      <Summary text={table.summary} />
      <Box x={73} y={259} w={1131} h={43} bg={t.blue} />
      {table.cols.map((c, i) => (
        <Lines key={c} x={(xs[i] + xs[i + 1]) / 2} cy={281} align="center" w={xs[i + 1] - xs[i]} size={19} color="#fff" lines={[c]} />
      ))}
      <Box x={73} y={302} w={1131} h={321} style={{ border: '1px solid #8a8a8a', borderTop: 0 }} />
      {rows.slice(1, -1).map((y) => <Box key={y} x={73} y={y} w={1131} h={1} bg="#8a8a8a" />)}
      {xs.slice(1, -1).map((x) => <Box key={x} x={x} y={259} w={1} h={364} bg="#8a8a8a" />)}
      {table.rows.map((r, i) => {
        const cy = (rows[i] + rows[i + 1]) / 2
        return (
          <div key={r.label}>
            <Lines x={(xs[0] + xs[1]) / 2} cy={cy} align="center" w={170} size={19} color={t.navy} lines={[r.label]} />
            <Lines x={(xs[1] + xs[2]) / 2} cy={cy - 25} lh={25} align="center" w={680} size={18} color="#555" lines={r.desc} />
            <Lines x={(xs[2] + xs[3]) / 2} cy={cy - 25} lh={25} align="center" w={270} size={18} color="#555" lines={r.note} />
          </div>
        )
      })}
    </PageSlide>
  )
}

function Compare() {
  return (
    <PageSlide page={5}>
      <SectionHead head={compare.head} />
      <Summary text={compare.summary} />
      {compare.cards.map((c, i) => {
        const x = 73 + i * 600
        return (
          <div key={c.title}>
            <Box x={x} y={272} w={534} h={66} bg={t.blue} />
            <Lines x={x + 267} cy={305} align="center" w={534} size={28} className="font-extrabold" color="#fff" lines={[c.title]} />
            <Box x={x} y={338} w={534} h={300} style={{ background: `linear-gradient(${t.pale}, #f1f3fb)` }} />
            <Lines x={x + 267} cy={386} align="center" w={534} size={27} className="font-medium" color="#222" lines={[c.quote]} />
            <Bullets x={x + 41} cy={457} items={c.bullets} gap={7} indent={19} />
          </div>
        )
      })}
    </PageSlide>
  )
}

function Cause() {
  return (
    <PageSlide page={6}>
      <SectionHead head={cause.head} />
      <Summary text={cause.summary} />
      {cause.rows.map((r, i) => {
        const y = 279 + i * 183
        const fg = r.filled ? '#fff' : t.navy
        return (
          <div key={r.ko}>
            <Box x={73} y={y} w={1131} h={165} style={{ border: `2px solid ${t.blue}` }} />
            <Box x={73} y={y} w={209} h={165} bg={r.filled ? t.blue : '#ecf2fb'} style={{ border: `2px solid ${t.blue}` }} />
            <Lines x={177} cy={y + 70} align="center" w={200} size={36} className="font-black" color={fg} lines={[r.ko]} />
            <Lines x={177} cy={y + 107} align="center" w={200} size={20} className={cn(t.latin, 'font-medium')} color={fg} lines={[r.en]} />
            <Bullets x={312} cy={y + 43} items={r.bullets} indent={18} />
          </div>
        )
      })}
    </PageSlide>
  )
}

function Background() {
  const { bars, ticks } = background
  const bx = 95, bw = 366
  const segs1 = [{ v: 25, c: t.blue }, { v: 31, c: t.dark }, { v: 44, c: t.light }]
  const segs2 = [{ v: 12, c: t.blue }, { v: 26, c: t.light }, { v: 62, c: t.dark }]
  return (
    <PageSlide page={7}>
      <Box x={640} y={0} w={640} h={720} bg="#ecf1fb" />
      <SectionHead head={background.head} />
      <Donut cx={154} cy={359} r={82} hole={41} segs={segs1} />
      <Donut cx={337} cy={359} r={82} hole={41} segs={segs2} />
      {background.legend.map((l, i) => {
        const x = [89, 174, 264][i]
        return (
          <div key={l}>
            <Abs x={x - 7} y={471} w={14} h={14} className="rounded-full" style={{ background: [t.blue, '#2a3fc0', t.light][i], opacity: [0.75, 0.85, 0.8][i] }} />
            <Lines x={x + 13} cy={478} size={15} color="#666" lines={[l]} />
          </div>
        )
      })}
      {ticks.map((v) => <Box key={v} x={bx + (bw * v) / 100} y={537} w={1} h={76} bg="#ddd" />)}
      {bars.map((b, i) => (
        <div key={i}>
          <Box x={bx} y={543 + i * 20.3} w={(bw * b.v) / 100} h={8} bg={t.blue} />
          <Lines x={bx - 4} cy={547 + i * 20.3} align="right" w={40} size={9} color="#888" lines={[b.label]} />
        </div>
      ))}
      {ticks.map((v) => <Lines key={v} x={bx + (bw * v) / 100} cy={623} align="center" w={30} size={9} color="#888" lines={[String(v)]} />)}
      <Lines x={98} cy={656} size={15} color="#444" lines={[background.barTitle]} />
      {background.factors.map((f) => (
        <div key={f.title}>
          <Abs x={666} y={f.cy - 6} w={16} h={16} className="rounded-full" style={{ background: t.blue }} />
          <Lines x={695} cy={f.cy} size={33} className="font-medium" color="#222" lines={[f.title]} />
          <Lines x={695} cy={f.cy + 47} lh={25} size={19} color="#333" lines={f.body} />
        </div>
      ))}
    </PageSlide>
  )
}

function Conclusion() {
  return (
    <PageSlide page={8}>
      <SectionHead head={conclusion.head} />
      <Box x={0} y={358} w={1280} h={362} style={{ background: 'linear-gradient(90deg, #d9ddf3, #e3e6f6 50%, #d9ddf3)' }} />
      <Lines x={t.left} cy={443} lh={56} size={46} className="font-medium italic" color="#1d2a5c" lines={conclusion.lead} />
      <Paras x={660} cy={426} paras={conclusion.paras} gap={26} />
    </PageSlide>
  )
}

const deck: DeckDefinition = { id: '03', title: '파랑과 흰색의 심플한 보고서', slides: [Cover, Toc, Status, Analysis, Table, Compare, Cause, Background, Conclusion] }
export default deck
