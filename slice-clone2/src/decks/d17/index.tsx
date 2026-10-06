import type { DeckDefinition } from '../../ui'
import { Abs, ImagePlaceholder, cn } from '../../ui'
import { ChevronRight, Crosshair, Laptop, Lightbulb, BadgeDollarSign, ChartColumnIncreasing, ChartNoAxesCombined, CircleDollarSign, Files, FileSearch, Handshake, Mail, MonitorSmartphone, Search, Users } from 'lucide-react'
import { Bar, Box, Header, Lines, Logo, NoteBox, Page, Photo, T, Table, VText } from './components'
import * as d from './data'
import { t, tone } from './theme'

const B = { color: t.ink } as const

function Cover() {
  const c = d.cover
  return (
    <Page>
      <Logo x={72} y={71} />
      <T x={1100} w={108} cy={82} size={17} align="right" className="font-bold" style={B}>{c.year}</T>
      <Abs x={361} y={220} w={580} h={60} className="flex items-center overflow-hidden rounded-full" style={{ border: `2.5px solid ${t.ink}` }}>
        <span style={{ marginLeft: 32, width: 2.5, height: 26, background: t.ink }} />
        <span className="ml-[48px] font-bold leading-none whitespace-nowrap" style={{ fontSize: 34, color: t.ink }}>{c.search}</span>
        <span className="ml-auto flex h-full w-[68px] items-center justify-center" style={{ background: '#94b3c8', borderLeft: `2.5px solid ${t.ink}` }}><Search size={26} color="#fff" strokeWidth={3} /></span>
      </Abs>
      <T x={0} w={1280} cy={359} size={96} align="center" className="font-black tracking-[-0.03em]" style={B}>
        {c.title[0]}<span style={{ color: t.light, marginLeft: 28 }}>{c.title[1]}</span>
      </T>
      <Lines lines={c.desc} x={0} w={1280} cy={486} pitch={34} size={20} align="center" />
    </Page>
  )
}

function Toc() {
  const c = d.toc
  return (
    <Page>
      <T x={80} cy={104} size={21}>{c.sub}</T>
      <T x={76} cy={176} size={88} className="font-extrabold tracking-[-0.01em]" style={B}>{c.title}</T>
      <Logo x={1202} y={74} right />
      {c.items.map((it, i) => {
        const cy = 285 + i * 73.5
        return (
          <div key={it.no}>
            <T x={76} cy={cy} size={34} className="font-bold" style={B}>{it.no}</T>
            <Bar x={141} y={cy - 25} w={371} h={50} k={it.k} label={it.label} size={22} inset={14} r={4} />
            <T x={533} cy={cy} size={19}>{it.desc}</T>
            <Abs x={523} y={cy + 24} w={685} h={1.5} style={{ background: t.ink }} />
          </div>
        )
      })}
    </Page>
  )
}

function About() {
  const c = d.about
  return (
    <Page>
      <Header />
      <Lines lines={c.title} x={78} cy={182} pitch={67} size={50} className="font-bold tracking-[-0.02em]" style={B} />
      <Lines lines={c.body} x={80} cy={316} pitch={30} size={17.8} />
      <Box x={77} y={418} w={744} h={194} r={16} />
      {c.cols.map((col, ci) => (
        <div key={ci}>
          <Abs x={[104, 447][ci]} y={443} w={2} h={147} style={{ background: t.ink }} />
          {col.map(([k, v], i) => (
            <div key={k}>
              <T x={[115, 462][ci]} cy={451 + i * 32} size={16.5} className="font-bold" style={B}>{k}</T>
              <T x={[210, 556][ci]} cy={451 + i * 32} size={16.5}>{v}</T>
            </div>
          ))}
        </div>
      ))}
      <Photo x={846} y={160} w={354} h={452} label="building photo" />
    </Page>
  )
}

function Section() {
  const c = d.section
  return (
    <Page>
      <Logo x={1202} y={80} right />
      <T x={98} cy={240} size={116} className="font-extrabold tracking-[-0.03em]" style={B}>{c.no}</T>
      <Bar x={106} y={324} w={1069} h={79} label={c.sub} size={40} inset={19} r={8} />
      <Lines lines={c.body} x={112} cy={444} pitch={32.5} size={18.3} />
    </Page>
  )
}

function Bracket({ x, y, h, side }: { x: number; y: number; h: number; side: 'l' | 'r' }) {
  const b = `2px solid ${t.ink}`
  return <Abs x={x} y={y} w={12} h={h} style={side === 'l' ? { borderLeft: b, borderTop: b, borderBottom: b } : { borderRight: b, borderTop: b, borderBottom: b }} />
}

function Essay() {
  const c = d.essay
  return (
    <Page>
      <Header title={c.title} />
      <Lines lines={c.body} x={140} w={998} cy={199} pitch={35} size={17.3} justify />
      <Bracket x={103} y={443} h={151} side="l" />
      <Bracket x={1164} y={443} h={151} side="r" />
      <Lines lines={c.quote} x={0} w={1280} cy={458} pitch={40} size={20} align="center" className="font-semibold" style={B} />
    </Page>
  )
}

function TwoCol() {
  const c = d.twoCol
  return (
    <Page>
      <Header title={c.title} />
      {c.cols.map((col, i) => {
        const x = [112, 660][i]
        return (
          <div key={col.label}>
            <Bar x={x} y={230} w={508} h={77} k={col.k} label={col.label} size={25} />
            <Lines lines={col.lines} x={x} w={508} cy={352} pitch={35} size={17.3} justify />
          </div>
        )
      })}
    </Page>
  )
}

function RowsSlide() {
  const c = d.rows
  return (
    <Page>
      <Header title={c.title} />
      {c.items.map((it, i) => {
        const y = 181 + i * 156
        return (
          <div key={i}>
            <Box x={77} y={y} w={326} h={117} k={it.k} r={8} />
            <Abs x={100} y={y + 18} w={2.5} h={81} style={{ background: t.ink }} />
            <Lines lines={it.label} x={120} cy={y + 40} pitch={37} size={24} className="font-bold" style={B} />
            <Lines lines={it.lines} x={431} w={771} cy={y + 10} pitch={31.5} size={16.9} justify />
          </div>
        )
      })}
    </Page>
  )
}

function Grid4() {
  const c = d.grid4
  return (
    <Page>
      <Header title={c.title} />
      {c.items.map((it, i) => {
        const x = [77, 650][i % 2], y = [180, 403][Math.floor(i / 2)]
        return (
          <div key={it.label}>
            <Box x={x} y={y} w={553} h={205} k={it.k} r={16} />
            <Abs x={x + 36} y={y + 33} w={2.5} h={25} style={{ background: t.ink }} />
            <T x={x + 52} cy={y + 46} size={24} className="font-bold" style={B}>{it.label}</T>
            <Lines lines={it.lines} x={x + 36} w={481} cy={y + 91} pitch={28} size={16} justify />
          </div>
        )
      })}
    </Page>
  )
}

function Conclusion() {
  const c = d.conclusion
  return (
    <Page>
      <Header title={c.title} />
      {c.items.map((lines, i) => {
        const col = i % 2, row = Math.floor(i / 2)
        const x = [77, 651][col], y = 180 + row * 88
        return (
          <div key={i}>
            <Box x={x} y={y} w={552} h={75} k={(row + col) % 2 ? 'blue' : 'grey'} r={6} />
            <T x={x + 32} cy={y + 37} size={24} className="font-bold" style={B}>{String(i + 1).padStart(2, '0')}</T>
            <Abs x={x + 83} y={y + 23} w={2.5} h={30} style={{ background: t.ink }} />
            <Lines lines={lines} x={x + 108} cy={y + 25} pitch={25.5} size={15.8} />
          </div>
        )
      })}
    </Page>
  )
}

const kpiIcons = { search: FileSearch, dollar: CircleDollarSign, bag: BadgeDollarSign, chart: ChartColumnIncreasing, doc: Files }
function Kpi() {
  const c = d.kpi
  return (
    <Page>
      <Header title={c.title} />
      <T x={80} cy={198} size={17.6}>{c.sub}</T>
      {c.cards.map((k) => {
        const Icon = kpiIcons[k.icon]
        return (
          <div key={k.label}>
            <Box x={k.x} y={k.y} w={k.w} h={k.h} k={k.k} r={16} />
            <T x={k.x + 26} cy={k.y + 36} size={19} className="font-bold" style={B}>{k.label}</T>
            <Abs x={k.x + k.w - 72} y={k.y + 20}><Icon size={52} color={t.ink} strokeWidth={1.4} /></Abs>
            <T x={k.x} w={k.w - 18} cy={k.y + k.h - 50} size={46} align="right" className="items-baseline font-extrabold" style={B}>
              000<span style={{ fontSize: 26, marginLeft: 2 }}>{k.unit}</span>
            </T>
          </div>
        )
      })}
    </Page>
  )
}

function Message() {
  const c = d.message
  return (
    <Page>
      <Header title={c.title} />
      {['“', '”'].map((q, i) => (
        <T key={q} x={[205, 1008][i]} cy={335} size={110} className="font-black" style={{ color: t.faint, fontFamily: 'Noto Sans KR' }}>{q}</T>
      ))}
      <Lines lines={c.lines} x={0} w={1280} cy={253} pitch={69} size={48} align="center" className="font-medium" style={B} />
      <Abs x={319} y={359} w={325} h={64} style={{ background: t.blue }} />
      <T x={0} w={1280} cy={393} size={48} align="center" className="font-bold" style={B}>
        {c.last[0]}<span className="whitespace-pre">{c.last[1]}</span>
      </T>
      <NoteBox y={507} h={102} lines={c.note} cy={543} />
    </Page>
  )
}

function MapSlide() {
  const c = d.map
  return (
    <Page>
      <Header title={c.title} />
      <Abs x={82} y={172} w={761} h={440}><ImagePlaceholder label="dotted world map" className="h-full w-full rounded-[8px]" /></Abs>
      {c.dots.map(([x, y]) => <Abs key={`${x}-${y}`} x={x - 6} y={y - 6} w={12} h={12} className="rounded-full" style={{ background: t.ink }} />)}
      {c.pins.map((p) => (
        <div key={p.label}>
          <Abs x={p.x - 1} y={p.top} w={2} h={p.bottom - p.top} style={{ background: t.ink }} />
          <Abs x={p.x - 6} y={p.bottom - 6} w={12} h={12} className="rounded-full" style={{ background: t.ink }} />
          <T x={p.x + 17} cy={p.ly} size={20} className="font-bold" style={B}>{p.label}</T>
          <T x={p.x + 17} cy={p.ly + 32} size={16}>{p.desc}</T>
        </div>
      ))}
      {c.cards.map((k, i) => {
        const y = 180 + i * 147
        return (
          <div key={k.label}>
            <Box x={877} y={y} w={327} h={136} k={k.k} r={8} />
            <Abs x={904} y={y + 26} w={2.5} h={25} style={{ background: t.ink }} />
            <T x={920} cy={y + 38} size={24} className="font-bold" style={B}>{k.label}</T>
            <Lines lines={k.lines} x={902} cy={y + 78} pitch={28.5} size={16} />
          </div>
        )
      })}
    </Page>
  )
}

/** Flat person pictogram: round head + dome body. `s` = total height. */
function Person({ cx, cy, s, color }: { cx: number; cy: number; s: number; color: string }) {
  const head = s * 0.46, bw = s * 0.82, bh = s * 0.42
  return (
    <>
      <Abs x={cx - head / 2} y={cy - s / 2} w={head} h={head} className="rounded-full" style={{ background: color }} />
      <Abs x={cx - bw / 2} y={cy + s / 2 - bh} w={bw} h={bh} style={{ background: color, borderRadius: `${bw / 2}px ${bw / 2}px 0 0` }} />
    </>
  )
}

function People({ cx, label }: { cx: number; label: string }) {
  return (
    <>
      {[0, 1, 2].map((r) => [0, 1, 2, 3, 4].map((i) => (
        <Person key={`${r}${i}`} cx={cx - 65 + i * 32.5} cy={[239, 280, 319][r]} s={26} color={r === 0 && i < 4 ? t.ink : '#b8c4cc'} />
      )))}
      <T x={cx - 150} w={300} cy={364} size={20} align="center" className="font-bold" style={B}>{label}</T>
    </>
  )
}

function Picto() {
  const c = d.picto
  const icons = [MonitorSmartphone, ChartNoAxesCombined]
  return (
    <Page>
      <Header title={c.title} />
      <Lines lines={c.body} x={77} w={520} cy={190} pitch={30} size={16} justify />
      {c.tiles.map((tl, i) => {
        const x = [76, 350][i], Icon = icons[i]
        return (
          <div key={tl.label}>
            <Box x={x} y={385} w={255} h={224} k={tl.k} r={16} />
            <Abs x={x + 92} y={436}><Icon size={72} color={t.ink} strokeWidth={1.8} /></Abs>
            <T x={x} w={255} cy={565} size={20} align="center" className="font-bold" style={B}>{tl.label}</T>
          </div>
        )
      })}
      <Box x={621} y={182} w={581} h={428} r={16} />
      {c.groups.map((g) => <People key={g.label} {...g} />)}
      <Abs x={888} y={274} w={50} h={50} className="flex items-center justify-center rounded-full font-bold text-white" style={{ background: t.ink, fontSize: 20 }}>VS</Abs>
      <Person cx={721} cy={477} s={92} color={t.ink} />
      <T x={621} w={200} cy={553} size={19} align="center" className="font-bold" style={B}>{c.solution}</T>
      {c.bars.map((b, i) => {
        const y = [437, 474, 510][i]
        return (
          <div key={i}>
            <Abs x={803} y={y - 12} w={339} h={24} className="bg-white" />
            <Abs x={803} y={y - 12} w={b.w} h={24} style={{ background: t.ink }} />
            <T x={1080} w={56} cy={y} size={16} align="right" className="font-bold" style={B}>{b.v}</T>
          </div>
        )
      })}
      <T x={802} cy={552} size={16}>{c.caption}</T>
    </Page>
  )
}

function PhotoText() {
  const c = d.photoText
  return (
    <Page>
      <Header lineEnd={620} />
      <Lines lines={c.title} x={77} cy={183} pitch={67} size={50} className="font-bold tracking-[-0.02em]" style={B} />
      <Photo x={77} y={317} w={543} h={291} label="desk documents photo" />
      <Lines lines={c.p1} x={660} w={542} cy={118} pitch={32} size={16} justify />
      <Lines lines={c.p2} x={660} w={542} cy={342} pitch={32} size={16} justify />
    </Page>
  )
}

function Evidence() {
  const c = d.evidence
  return (
    <Page>
      <Header title={c.title} />
      {c.items.map((it, i) => {
        const y = [180, 407][i]
        return (
          <div key={it.label}>
            <Photo x={77} y={y} w={378} h={203} label="meeting photo" />
            <Bar x={480} y={y} w={724} h={60} k={it.k} label={it.label} />
            <Lines lines={it.lines} x={480} w={724} cy={y + 92} pitch={32.2} size={15.6} justify />
          </div>
        )
      })}
    </Page>
  )
}

function Visual() {
  const c = d.visual
  return (
    <Page>
      <Header title={c.title} />
      {c.cols.map((col, i) => {
        const x = 78 + i * 385.5
        return (
          <div key={col.label}>
            <Photo x={x} y={181} w={354} h={210} label="construction photo" />
            <Bar x={x} y={410} w={354} h={61} k={col.k} label={col.label} />
            <Lines lines={col.lines} x={x - 2} w={358} cy={499} pitch={32} size={16} justify />
          </div>
        )
      })}
    </Page>
  )
}

function Gallery() {
  const c = d.gallery
  return (
    <Page>
      <Header title={c.title} />
      <Bar x={77} y={180} w={443} h={60} label={c.label} />
      <Lines lines={c.lines} x={77} w={443} cy={272} pitch={32.2} size={16} justify />
      {[0, 1, 2, 3].map((i) => <Photo key={i} x={[549, 883][i % 2]} y={[180, 401][i >> 1]} w={321} h={208} label="office photo" />)}
    </Page>
  )
}

const kwIcons = { mail: Mail, users: Users, chart: ChartColumnIncreasing, hand: Handshake }
function Mockup() {
  const c = d.mockup
  return (
    <Page>
      <Header />
      <Lines lines={c.title} x={77} cy={182} pitch={67} size={50} className="font-bold tracking-[-0.02em]" style={B} />
      <Abs x={77} y={311} w={422} h={2} style={{ background: t.ink }} />
      <Lines lines={c.lines} x={77} w={422} cy={354} pitch={30.4} size={16} justify />
      <Abs x={539} y={140} w={229} h={471}><ImagePlaceholder label="phone mockup" className="h-full w-full rounded-[40px]" /></Abs>
      <Lines lines={c.screen} x={539} w={229} cy={362} pitch={25} size={16} align="center" />
      {c.cards.map((k, i) => {
        const x = [801, 1008][i % 2], y = [158, 388][i >> 1], Icon = kwIcons[k.icon]
        return (
          <div key={k.title}>
            <Box x={x} y={y} w={196} h={220} k={k.k} r={14} />
            <Abs x={x + 72} y={y + 43}><Icon size={52} color={t.ink} strokeWidth={2} /></Abs>
            <T x={x} w={196} cy={y + 125} size={21} align="center" className="font-bold" style={B}>{k.title}</T>
            <Lines lines={k.lines} x={x} w={196} cy={y + 159} pitch={25} size={16} align="center" />
          </div>
        )
      })}
    </Page>
  )
}

const slides1 = [Cover, Toc, About, Section, Essay, TwoCol, RowsSlide, Grid4, Conclusion, Kpi, Message, MapSlide, Picto, PhotoText, Evidence, Visual, Gallery, Mockup]


const dot = (cx: number, cy: number, r: number, bg: string) => <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className="rounded-full" style={{ background: bg }} />
const dotted = (x: number, y: number, w: number) => <Abs x={x} y={y} w={w} h={0} style={{ borderTop: `1.5px dotted ${t.text}` }} />

function Radial() {
  const c = d.radial
  const R = 163
  return (
    <Page>
      <Header title={c.title} />
      <Abs x={640 - R} y={394 - R} w={R * 2} h={R * 2} className="rounded-full" style={{ border: '1px solid #8796a2' }} />
      {c.nodes.map((n, i) => {
        const a = (-90 + i * 60) * Math.PI / 180, cx = 640 + R * Math.cos(a), cy = 394 + R * Math.sin(a)
        return (
          <div key={n[0]}>
            {dot(cx, cy, 52, i % 2 ? t.grey : t.blue)}
            <Lines lines={n} x={cx - 52} w={104} cy={cy - 14} pitch={28} size={19.5} align="center" className="font-bold" style={B} />
          </div>
        )
      })}
      {dot(640, 394, 91, t.ink)}
      <T x={540} w={200} cy={383} size={23} align="center" className="font-bold text-white">{c.center[0]}</T>
      <T x={540} w={200} cy={415} size={16} align="center" className="text-white">{c.center[1]}</T>
      {dotted(82, 391, 350)}{dotted(858, 391, 350)}
      {c.left.map((ls, i) => <Lines key={i} lines={ls} x={150} w={247} cy={[271, 456][i]} pitch={30.5} size={16.5} align="right" />)}
      {c.right.map((ls, i) => <Lines key={i} lines={ls} x={885} cy={[271, 456][i]} pitch={30.5} size={16.5} />)}
    </Page>
  )
}

function Venn() {
  const c = d.venn
  return (
    <Page>
      <Header title={c.title} />
      <Bar x={77} y={215} w={342} h={59} label={c.label} />
      <Lines lines={c.lines} x={78} w={341} cy={305} pitch={28.3} size={16} justify />
      {c.bullets.map((b, i) => (
        <div key={b}>
          {dot(86, 494 + i * 28.5, 3, t.ink)}
          <T x={100} cy={494 + i * 28.5} size={16}>{b}</T>
        </div>
      ))}
      {c.circles.map((k) => <Abs key={k.label} x={k.cx - 116} y={k.cy - 116} w={232} h={232} className="rounded-full" style={{ background: k.fill }} />)}
      {c.circles.map((k) => <T key={k.label} x={k.cx - 60} w={120} cy={k.cy - (k.label === '시간' ? 2 : 0)} size={23} align="center" className="font-bold" style={B}>{k.label}</T>)}
      {c.side.map((s) => (
        <div key={s.label}>
          <Abs x={880} y={s.y} w={323} h={59} className="flex items-center rounded-[4px] font-bold leading-none" style={{ background: '#c5d2dc' }}>
            <span style={{ marginLeft: 22, width: 2.5, height: 26, background: t.ink }} />
            <span style={{ marginLeft: 21, fontSize: 25 * t.fs, color: t.ink }}>{s.label}</span>
          </Abs>
          <Lines lines={s.lines} x={883} w={320} cy={s.y + 84} pitch={28.3} size={16} justify />
        </div>
      ))}
    </Page>
  )
}

const stepIcons = { bulb: Lightbulb, target: Crosshair, laptop: Laptop, search: FileSearch }
function Roadmap() {
  const c = d.roadmap
  return (
    <Page>
      <Header title={c.title} />
      {c.steps.map((s, i) => {
        const x = [148, 432, 713, 1000][i], Icon = stepIcons[s.icon]
        return (
          <div key={s.label}>
            <Box x={x} y={177} w={137} h={137} k={i % 2 ? 'blue' : 'grey'} r={10} />
            <Abs x={x + 39} y={216}><Icon size={58} color={t.ink} strokeWidth={1.5} /></Abs>
            {i < 3 && <Abs x={[343, 627, 904][i]} y={237}><ChevronRight size={26} color={t.ink} strokeWidth={1.5} /></Abs>}
            <T x={x - 60} w={257} cy={354} size={25} align="center" className="font-bold" style={B}>{s.label}</T>
            <Lines lines={s.lines} x={x - 60} w={257} cy={397} pitch={28} size={16.3} align="center" />
          </div>
        )
      })}
      <NoteBox y={508} h={100} lines={c.note} cy={542} pitch={31} size={19.5} />
    </Page>
  )
}

function SpecTable() {
  const c = d.specTable
  return (
    <Page>
      <Header title={c.title} />
      <Bar x={76} y={181} w={785} h={61} label={c.label} />
      <Table cols={[77, 202, 367, 531, 694, 860]} y={259} headH={39} rowH={78} head={c.head} rows={c.rows} size={17} />
      <Photo x={885} y={181} w={318} h={428} label="desk still-life photo" />
    </Page>
  )
}

const ganttTone = { light: '#e1e6ea', mid: '#c5cfd5', dark: '#aab7bf', pink: '#f2e9ee' }
function Gantt() {
  const c = d.gantt
  return (
    <Page>
      <Header title={c.title} />
      <Abs x={77} y={178} w={1126} h={41} className="rounded-[6px]" style={{ background: t.ink }} />
      {c.quarters.map((q, i) => <T key={q} x={[336, 584, 832, 1079][i] - 60} w={120} cy={198} size={17} align="center" className="font-bold text-white">{q}</T>)}
      {c.rows.map((r, i) => (
        <div key={r.label}>
          <T x={82} cy={[260, 336, 414, 491, 567][i]} size={16.5} className="font-bold" style={B}>{r.label}</T>
          <Abs x={77} y={[298, 376, 452, 530, 607][i]} w={1126} h={1.5} style={{ background: t.ink }} />
          {r.bars.map(([x1, x2, y, k, label]) => (
            <div key={label + y}>
              <Abs x={x1} y={y - 4} w={x2 - x1} h={8} className="rounded-full" style={{ background: ganttTone[k] }} />
              <T x={x2 + 12} cy={y} size={16.5}>{label}</T>
            </div>
          ))}
        </div>
      ))}
    </Page>
  )
}

function BarChart() {
  const c = d.barChart
  const x0 = 124, k = 93.6 / 400
  return (
    <Page>
      <Header title={c.title} />
      <Bar x={77} y={180} w={543} h={63} label={c.left} />
      <Bar x={660} y={180} w={544} h={63} k="blue" label={c.right} />
      {c.ticks.map((v) => (
        <div key={v}>
          <Abs x={x0 + v * k} y={272} w={1} h={220} style={{ background: v ? '#cfd6dc' : '#9aa6af' }} />
          <T x={x0 + v * k - 40} w={80} cy={507} size={15.5} align="center">{v.toLocaleString()}</T>
        </div>
      ))}
      {c.bars.map(([q, v], i) => (
        <div key={q}>
          <T x={60} w={60} cy={[298, 354, 411, 467][i]} size={15.5} align="right">{q}</T>
          <Abs x={x0 + 1} y={[298, 354, 411, 467][i] - 19.5} w={v * k} h={39} className="rounded-r-[4px]" style={{ background: i === 3 ? t.blue : t.grey }} />
        </div>
      ))}
      <Lines lines={c.caption} x={148} w={400} cy={565} pitch={28} size={16} align="center" />
      <Table cols={[661, 811, 1203]} y={258} headH={39} rowH={75} head={c.head} rows={c.rows} size={16.5} />
      <Lines lines={c.note} x={730} w={400} cy={565} pitch={28} size={16} align="center" />
    </Page>
  )
}

function Pies() {
  const c = d.pies
  return (
    <Page>
      <Header title={c.title} />
      <Bar x={77} y={181} w={451} h={61} label={c.label} />
      <Lines lines={c.lines} x={77} w={451} cy={272} pitch={32} size={15.8} justify />
      <Photo x={77} y={454} w={221} h={155} label="AI chip photo" />
      <Photo x={309} y={454} w={221} h={155} label="business people photo" />
      {c.charts.map((ch) => {
        let acc = 0
        const stops = ch.slices.map(([deg, k]) => `${tone(k)} ${acc}deg ${(acc += deg)}deg`).join(', ')
        return (
          <div key={ch.title}>
            <T x={ch.cx - 150} w={300} cy={194} size={20} align="center" className="font-bold" style={B}>{ch.title}</T>
            <Abs x={ch.cx - 148} y={233} w={296} h={296} className="rounded-full" style={{ background: `conic-gradient(${stops})` }} />
            {ch.labels.map((l) => (
              <div key={l.v} style={{ color: l.white ? '#fff' : t.ink }}>
                <T x={l.x - 60} w={120} cy={l.y} size={l.ks} align="center" className={l.white ? '' : 'opacity-80'}>{l.k}</T>
                <T x={l.x - 60} w={120} cy={l.y + l.vs * 1.25} size={l.vs} align="center" className="font-bold">{l.v}</T>
              </div>
            ))}
            <Lines lines={c.caption} x={ch.cx - 150} w={300} cy={568} pitch={28} size={16} align="center" />
          </div>
        )
      })}
    </Page>
  )
}

function LineChart() {
  const c = d.line
  const xs = [166, 247, 327, 408, 489, 570, 651, 731], y = (v: number) => 583 - v * 0.1455
  const pts = c.values.map((v, i) => `${xs[i]},${y(v)}`).join(' ')
  return (
    <Page>
      <Header title={c.title} />
      <Bar x={77} y={180} w={1126} h={63} label={c.label} />
      {c.ticks.map((v) => (
        <div key={v}>
          <T x={60} w={61} cy={y(v)} size={15.5} align="right">{v.toLocaleString()}</T>
          <Abs x={125} y={y(v)} w={645} h={1} style={{ background: '#cfd6dc' }} />
        </div>
      ))}
      <svg className="absolute left-0 top-0" width={1280} height={720}>
        <polygon points={`${xs[0]},583 ${pts} ${xs[7]},583`} fill="#d3dde5" />
        <polyline points={pts} fill="none" stroke={t.ink} strokeWidth={1.2} />
        {c.values.map((v, i) => <circle key={i} cx={xs[i]} cy={y(v)} r={3.5} fill={t.ink} />)}
      </svg>
      {xs.map((x, i) => <T key={x} x={x - 30} w={60} cy={599} size={15.5} align="center">{`${i + 1}주차`}</T>)}
      <T x={804} cy={291} size={20} className="font-bold" style={B}>{c.heading}</T>
      <Lines lines={c.lines} x={804} w={394} cy={330} pitch={30.4} size={15.8} justify />
      {c.keywords.map((k, i) => (
        <div key={k}>
          {dot([863, 999, 1136][i], 545, 58, i % 2 ? t.blue : t.grey)}
          <T x={[863, 999, 1136][i] - 58} w={116} cy={545} size={20} align="center" className="font-bold" style={B}>{k}</T>
        </div>
      ))}
    </Page>
  )
}

function OrgBox({ cx, y, w, h, k, label }: { cx: number; y: number; w: number; h: number; k: 'grey' | 'blue' | 'dark'; label: string }) {
  return (
    <>
      <Box x={cx - w / 2} y={y} w={w} h={h} k={k} r={5} />
      <T x={cx - w / 2} w={w} cy={y + h / 2} size={20} align="center" className={cn('font-bold', k === 'dark' && 'text-white')} style={k === 'dark' ? undefined : B}>{label}</T>
    </>
  )
}

function Org() {
  const c = d.org
  const ln = { background: '#7b8a96' }
  const cxs = [153, 348, 543, 738, 933, 1128]
  return (
    <Page>
      <Header title={c.title} />
      <Abs x={640} y={222} w={1.5} h={130} style={ln} />
      <Abs x={474} y={299} w={166} h={1.5} style={ln} />
      <Abs x={640} y={272} w={165} h={1.5} style={ln} />
      <Abs x={805} y={227} w={25} h={91} className="rounded-l-[8px]" style={{ border: '1.5px solid #7b8a96', borderRight: 0 }} />
      <Abs x={153} y={352} w={975} h={30} className="rounded-t-[10px]" style={{ border: '1.5px solid #7b8a96', borderBottom: 0 }} />
      <OrgBox cx={639} y={180} w={240} h={42} k="dark" label={c.ceo} />
      <OrgBox cx={950} y={207} w={241} h={42} k="grey" label={c.side[0]} />
      <OrgBox cx={950} y={296} w={241} h={44} k="blue" label={c.side[1]} />
      <OrgBox cx={354} y={278} w={240} h={42} k="blue" label={c.board} />
      {c.teams.map(([name, ...members], i) => (
        <div key={name}>
          <OrgBox cx={cxs[i]} y={380} w={151} h={44} k={i % 2 ? 'blue' : 'grey'} label={name} />
          {[0, 1, 2].map((j) => (
            <div key={j}>
              {members[j] && <T x={cxs[i] - 80} w={160} cy={455 + j * 60.5} size={17.5} align="center">{members[j]}</T>}
              {dotted(cxs[i] - 75, 487 + j * 60, 150)}
            </div>
          ))}
        </div>
      ))}
    </Page>
  )
}

function Cause() {
  const c = d.cause
  return (
    <Page>
      <Header title={c.title} />
      {c.cols.map((col, i) => {
        const x = [77, 696][i]
        return (
          <div key={col.label}>
            <Bar x={x} y={181} w={508} h={61} k={col.k} label={col.label} />
            <Lines lines={col.lines} x={x} w={508} cy={272} pitch={32} size={16} justify />
            <Photo x={x + 1} y={406} w={507} h={200} label="technology photo" />
          </div>
        )
      })}
      <Abs x={609} y={359} w={70} h={87}><ImagePlaceholder label="gradient arrow" className="h-full w-full" style={{ clipPath: 'polygon(0 0, 55% 0, 100% 50%, 55% 100%, 0 100%, 45% 50%)' }} /></Abs>
    </Page>
  )
}

const onDark = (k: string) => (k === 'dark' || k === 'mid' ? '#fff' : t.ink)
function Positioning() {
  const c = d.positioning
  return (
    <Page>
      <Header title={c.title} />
      <Bar x={77} y={180} w={544} h={63} label={c.label} />
      <Abs x={121} y={267} w={1.5} h={316} style={{ background: t.ink }} />
      <Abs x={121} y={582} w={494} h={1.5} style={{ background: t.ink }} />
      <VText x={101} cy={290} size={15.5}>{c.axis.top}</VText>
      <VText x={101} cy={555} size={15.5}>{c.axis.bottom}</VText>
      <T x={122} cy={599} size={15.5}>{c.axis.left}</T>
      <T x={515} w={100} cy={599} size={15.5} align="right">{c.axis.right}</T>
      {c.bubbles.map((b) => (
        <div key={b.label}>
          {dot(b.cx, b.cy, b.r, tone(b.k))}
          <T x={b.cx - b.r} w={b.r * 2} cy={b.cy} size={b.size} align="center" className="font-bold" style={{ color: onDark(b.k) }}>{b.label}</T>
        </div>
      ))}
      {c.items.map((it, i) => {
        const y = [181, 290, 399, 507][i]
        return (
          <div key={it.label}>
            <Box x={660} y={y} w={124} h={103} k={it.k} r={5} />
            <T x={660} w={124} cy={y + 51} size={21} align="center" className="font-bold" style={{ color: onDark(it.k) }}>{it.label}</T>
            <Lines lines={it.lines} x={806} cy={y + 20} pitch={26.7} size={15.8} />
            {i < 3 && <Abs x={796} y={y + 103} w={409} h={1.5} style={{ background: t.ink }} />}
          </div>
        )
      })}
    </Page>
  )
}

function Matrix() {
  const c = d.matrix
  return (
    <Page>
      <Header title={c.title} />
      <Bar x={77} y={180} w={1126} h={63} label={c.label} />
      <Abs x={121} y={269} w={1.5} h={313} style={{ background: t.ink }} />
      <Abs x={121} y={581} w={494} h={1.5} style={{ background: t.ink }} />
      <VText x={101} cy={289} size={15.5}>{c.axis.top}</VText>
      <VText x={101} cy={424} size={16.5} bold>{c.axis.mid}</VText>
      <VText x={101} cy={558} size={15.5}>{c.axis.bottom}</VText>
      <T x={133} cy={599} size={15.5}>{c.axis.left}</T>
      <T x={267} w={200} cy={599} size={16.5} align="center" className="font-bold" style={B}>{c.axis.center}</T>
      <T x={507} w={100} cy={599} size={15.5} align="right">{c.axis.right}</T>
      {c.zones.map((z) => <Box key={z.label} x={z.x} y={z.y} w={z.w} h={z.h} k={z.k} r={14} />)}
      {c.zones.map((z) => (
        <div key={z.label}>
          <T x={z.lx - 80} w={160} cy={z.ly} size={20} align="center" className="font-bold" style={{ color: onDark(z.k) }}>{z.label}</T>
          <Abs x={z.from} y={z.ly} w={758 - z.from} h={1.5} style={{ background: t.ink }} />
        </div>
      ))}
      {c.notes.map((n, i) => <Lines key={i} lines={n} x={783} cy={[308, 393, 501][i]} pitch={27} size={15.8} />)}
    </Page>
  )
}

const slides2 = [Radial, Venn, Roadmap, SpecTable, Gantt, BarChart, Pies, LineChart, Org, Cause, Positioning, Matrix]

const deck: DeckDefinition = { id: '17', title: '하늘색 심플 비즈니스 설명서', slides: [...slides1, ...slides2] }
export default deck
