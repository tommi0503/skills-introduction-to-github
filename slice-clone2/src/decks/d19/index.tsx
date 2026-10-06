import type { DeckDefinition } from '../../ui'
import { Abs, ImagePlaceholder, Slide } from '../../ui'
import { Badge, Dot, Lines, Page, PhotoSlot, Sub, T } from './components'
import * as d from './data'
import { t } from './theme'

function Author({ x, cy, dept, name, second, size = 20 }: { x: number; cy: number; dept: string; name: string; second: string; size?: number }) {
  return (
    <>
      <T x={x} cy={cy} size={size}>{dept} <b className="font-bold tracking-[0.01em]">{name}</b></T>
      <T x={x} cy={cy + 34} size={size}>{second}</T>
    </>
  )
}

function Cover() {
  const c = d.cover
  return (
    <Slide background="#fff" className={t.font} style={{ color: t.ink, letterSpacing: '0.05em' }}>
      <Abs x={0} y={0} w={232} h={720} style={{ background: t.side }} />
      <Abs x={216} y={134} w={17} h={143} style={{ background: t.red }} />
      <Lines lines={c.title} x={281} cy={169} pitch={70} size={58} className="font-bold tracking-[0.01em]" />
      <Lines lines={c.sub} x={285} cy={332} pitch={31} size={20.8} />
      <Abs x={1189} y={38}><ImagePlaceholder label="logo" tone="#444" className="h-[44px] w-[44px] rounded-full" /></Abs>
      <Abs x={981} y={577} w={6} h={63} style={{ background: t.red }} />
      <Author x={999} cy={589} dept={c.dept} name={c.name} second={c.date} />
    </Slide>
  )
}

function Contents({ v }: { v: 'a' | 'b' }) {
  const c = d.contents
  const a = v === 'a'
  const x0 = a ? 92 : 232
  return (
    <Slide background={a ? '#c4c4c4' : '#a3a3a3'} className={t.font} style={{ letterSpacing: '0.05em' }}>
      <Abs x={0} y={0} w={x0} h={720} style={{ background: a ? '#a5a5a5' : '#c4c4c4' }} />
      <T x={a ? 124 : 281} cy={38} size={24} className="font-bold tracking-[0.01em]" style={{ color: a ? '#111' : '#fff' }}>{c.label}</T>
      <Abs x={1189} y={38}><ImagePlaceholder label="logo" tone="#e8e8e8" className="h-[44px] w-[44px] rounded-full" /></Abs>
      <Abs x={x0 - 17} y={a ? 128 : 127} w={17} h={a ? 50 : 62} style={{ background: a ? t.red : '#555' }} />
      <T x={a ? 127 : 274} cy={a ? 152 : 158} size={43} className="font-bold tracking-[0.01em]" style={{ color: a ? '#555' : '#fff' }}>{c.first}</T>
      <Lines lines={a ? c.a : c.b} x={a ? 169 : 327} cy={a ? 202 : 209} pitch={41.6} size={26} style={{ color: a ? '#a9a9a9' : '#c6c6c6' }} />
      {!a && (
        <>
          <T x={919} cy={417} size={26} style={{ color: '#c6c6c6' }}>{c.bTail[0]}</T>
          <T x={259} cy={457} size={26} style={{ color: '#c6c6c6' }}>{c.bTail[1]}</T>
        </>
      )}
    </Slide>
  )
}

function Intro1() {
  const c = d.intro
  return (
    <Page title={c.title} page={c.page}>
      <Sub>{c.sub}</Sub>
      <Lines lines={c.body} x={207} cy={186} pitch={31} size={20} />
      <PhotoSlot x={387} y={288} w={505} h={351} />
    </Page>
  )
}

function Intro2() {
  const c = d.intro
  return (
    <Page title={c.title} page={c.page}>
      {c.subWrapped.map((l, i) => <Sub key={l} cy={136 + i * 36}>{l}</Sub>)}
      <Lines lines={c.bodyNarrow} x={207} cy={243} pitch={31.3} size={20} />
      <PhotoSlot x={578} y={118} w={655} h={554} />
    </Page>
  )
}

function Legend({ cx, cy, label, round }: { cx: number; cy: number; label: string; round?: boolean }) {
  return (
    <T x={cx - 200} w={400} cy={cy} size={15} align="center">
      <span className={round ? 'rounded-full' : 'rounded-[3px]'} style={{ display: 'inline-block', width: 14, height: 14, background: round ? '#555' : '#000', marginRight: 4 }} />{label}
    </T>
  )
}

function Revenue() {
  const c = d.revenue
  const y = (v: number) => 529 - v * 0.102
  const xs = [359, 445, 531, 616, 702, 787, 873, 957, 1042]
  return (
    <Page title={c.title} page={c.page}>
      <Sub>{c.sub}</Sub>
      {c.ticks.map((v) => (
        <div key={v}>
          <T x={208} w={100} cy={y(v)} size={14.5} align="right">{`${v.toLocaleString()}억`}</T>
          <Abs x={317} y={y(v)} w={769} h={1} style={{ background: v ? '#ddd' : '#bbb' }} />
        </div>
      ))}
      {c.bars.map(([yr, v], i) => {
        const last = i === c.bars.length - 1
        return (
          <div key={yr}>
            <Abs x={xs[i] - 28.5} y={y(v)} w={57} h={529 - y(v)} style={{ background: last ? t.red : '#000' }} />
            <T x={xs[i] - 50} w={100} cy={y(v) - (last ? 28 : 16)} size={last ? 26 : 14.5} align="center" className={last ? 'font-bold tracking-[0.01em]' : ''}>{`${v.toLocaleString()}억`}</T>
            <T x={xs[i] - 40} w={80} cy={545} size={14.5} align="center">{yr}</T>
          </div>
        )
      })}
      <Legend cx={670} cy={592} label={c.legend} />
    </Page>
  )
}

function Profit() {
  const c = d.profit
  const y = (v: number) => 545 - v * 0.198
  const xs = [341, 418, 495, 571, 648, 726, 803, 880, 957, 1035]
  const pts = c.points.map(([, v], i) => `${xs[i]},${y(v)}`).join(' ')
  return (
    <Page title={c.title} page={c.page}>
      <Sub>{c.sub}</Sub>
      <Lines lines={c.note} x={997} cy={169} pitch={22} size={14.5} />
      {c.ticks.map((v) => (
        <div key={v}>
          <T x={194} w={100} cy={y(v)} size={14.5} align="right">{v.toLocaleString()}</T>
          <Abs x={301} y={y(v)} w={773} h={1} style={{ background: v ? '#ddd' : '#bbb' }} />
        </div>
      ))}
      <svg className="absolute left-0 top-0" width={1280} height={720}><polyline points={pts} fill="none" stroke="#999" strokeWidth={1} /></svg>
      {c.points.map(([yr, v], i) => (
        <div key={yr}>
          <Dot cx={xs[i]} cy={y(v)} r={6} bg={i === c.points.length - 1 ? t.red : '#555'} />
          <T x={xs[i] - 40} w={80} cy={y(v) - 20} size={14.5} align="center" style={{ color: '#666' }}>{v.toLocaleString()}</T>
          <T x={xs[i] - 40} w={80} cy={560} size={14.5} align="center">{yr}</T>
        </div>
      ))}
      <Legend cx={665} cy={603} label={c.legend} round />
    </Page>
  )
}

const pieColor = { A: '#b3b3b3', B: '#555', C: '#000', D: t.red }
function Pies() {
  const c = d.pies
  return (
    <Page title={c.title} page={c.page}>
      {c.charts.map((ch) => {
        const total = ch.values.reduce((a, b) => a + b, 0)
        let acc = 0
        const stops = ch.values.map((v, i) => `${pieColor[c.keys[i]]} ${acc}deg ${(acc += (v / total) * 360)}deg`).join(', ')
        return (
          <div key={ch.title}>
            <T x={ch.cx - 200} w={400} cy={156} size={26} align="center" className="font-bold tracking-[0.01em]" style={{ color: t.sub }}>{ch.title}</T>
            <Abs x={ch.cx - ch.r} y={ch.cy - ch.r} w={ch.r * 2} h={ch.r * 2} className="rounded-full" style={{ background: `conic-gradient(${stops})` }} />
            {ch.values.map((v, i) => <T key={i} x={ch.labels[i][0] - 30} w={60} cy={ch.labels[i][1]} size={15} align="center" className="text-white" style={i === 0 ? { textShadow: '0 0 1px #555, 0 0 1px #555' } : undefined}>{v}</T>)}
            {[c.keys.slice(0, 3), c.keys.slice(3)].map((row, ri) => (
              <T key={ri} x={ch.legend.x} cy={ch.legend.y + ri * 25} size={16}>
                {row.map((k) => <span key={k} className="mr-[6px] inline-flex items-center"><span className="mr-[3px] inline-block h-[15px] w-[15px] rounded-[3px]" style={{ background: pieColor[k] }} />제품 {k}</span>)}
              </T>
            ))}
          </div>
        )
      })}
      <Lines lines={c.note} x={509} w={300} cy={242} pitch={15} size={14} align="right" />
    </Page>
  )
}

function Demo() {
  const c = d.demo
  return (
    <Page title={c.title} page={c.page}>
      <Sub>{c.sub}</Sub>
      <Abs x={364} y={225} w={563} h={356}><ImagePlaceholder label="laptop mockup" className="h-full w-full rounded-[10px]" /></Abs>
      <Abs x={979} y={236} w={142} h={299}><ImagePlaceholder label="phone mockup" className="h-full w-full rounded-[14px]" /></Abs>
    </Page>
  )
}

function Clients() {
  const c = d.clients
  const xs = [236, 363, 489, 615, 742, 868, 994, 1121], ys = [181, 313, 441, 574]
  return (
    <Page title={c.title} page={c.page}>
      {ys.map((y) => xs.map((x) => <Abs key={`${x}${y}`} x={x - 40} y={y - 40}><ImagePlaceholder label="client logo" className="h-[80px] w-[80px] rounded-[10px]" /></Abs>))}
    </Page>
  )
}

function Outlook() {
  const c = d.outlook
  return (
    <Page title={c.title} page={c.page}>
      {c.items.map(([h, ...ls], i) => {
        const cy = [160, 311, 467][i]
        return (
          <div key={h}>
            <T x={150} cy={cy} size={26} className="font-bold tracking-[0.01em]" style={{ color: t.sub }}>{h}</T>
            <Lines lines={ls} x={150} cy={cy + 38} pitch={35} size={22} style={{ color: t.sub }} />
          </div>
        )
      })}
      <PhotoSlot x={755} y={141} w={480} h={542} />
    </Page>
  )
}

function Qna() {
  const c = d.qna
  return (
    <Slide background="#fff" className={t.font} style={{ color: t.ink, letterSpacing: '0.05em' }}>
      <Abs x={0} y={0} w={t.rail} h={720} style={{ background: t.side }} />
      <Abs x={92} y={0} w={1188} h={720}><ImagePlaceholder label="smiling woman photo" tone="#8a8a8a" className="h-full w-full" /></Abs>
      <Abs x={75} y={27} w={17} h={50} style={{ background: t.red }} />
      <T x={124} cy={51} size={42} className="font-bold tracking-[0.01em]" style={{ color: '#e6e6e6' }}>{c.title}</T>
      <Badge n={c.page} dark />
      <T x={207} cy={136} size={25} className="font-bold tracking-[0.01em] text-white">{c.sub}</T>
      <Author x={949} cy={652} dept={c.dept} name={c.name} second={c.mail} size={21} />
      <T x={107} cy={706} size={9} style={{ color: '#ddd' }}>{c.foot}</T>
    </Slide>
  )
}

const deck: DeckDefinition = {
  id: '19', title: '흑백의 단순한 구성의 서비스 실적과 전략 예측 보고서',
  slides: [Cover, () => <Contents v="a" />, () => <Contents v="b" />, Intro1, Intro2, Revenue, Profit, Pies, Demo, Clients, Outlook, Qna],
}
export default deck
