import type { DeckDefinition } from '../../ui'
import { Abs, ImagePlaceholder } from '../../ui'
import { CalendarCheck2, Check, MapPin, Network, NotebookPen, Play } from 'lucide-react'
import { Bullets, HeadCard, LabelBand, Lines, NumBox, Page, PageNo, PhotoPoly, Poly, Quote, T, Tick, Title } from './components'
import * as d from './data'
import { geo, t } from './theme'

const G = { color: t.grey } as const
const B = { color: t.blue } as const
const W = { color: '#fff' } as const
const BRIEF = { color: '#c4d2ea' } as const

function Cover() {
  const c = d.cover
  return (
    <Page>
      <Poly pts={[[0, 190], [54, 250], [0, 312]]} c="#b6c4d4" />
      <Poly pts={[[54, 248], [472, 720], [0, 720], [0, 312]]} />
      <PhotoPoly pts={[[0, 0], [600, 0], [222, 428], [54, 248], [0, 190]]} label="skyscraper photo" />
      <Poly pts={[[1213, 0], [1277, 0], [1173, 107], [1109, 107]]} />
      <T x={800} w={363} cy={190} size={22} align="right" className="tracking-[0.06em]" style={G}>{c.kicker}</T>
      <T x={500} w={670} cy={295} size={80} align="right" className="font-light tracking-[-0.02em]">{c.light}</T>
      <T x={500} w={670} cy={405} size={80} align="right" className="font-bold tracking-[-0.02em]">{c.bold}</T>
      <Lines lines={d.brief} x={68} cy={627} pitch={21} size={15} style={BRIEF} />
      <T x={800} w={368} cy={647} size={17} align="right" className="font-semibold">{d.byline}</T>
    </Page>
  )
}

function TocFrame({ photo }: { photo: string }) {
  return (
    <>
      <Poly pts={geo.stripe} />
      <PhotoPoly pts={[[1003, 0], [1280, 0], [1280, 277]]} label={photo} />
      <Poly pts={[[974, 0], [1003, 0], [1280, 277], [1280, 306]]} />
      <Poly pts={[[0, 332], [341, 720], [0, 720]]} />
      <Poly pts={[[1280, 622], [1280, 720], [1184, 720]]} />
      <Lines lines={d.brief3} x={69} cy={611} pitch={21} size={15} style={BRIEF} />
      <T x={124} cy={99} size={14.5} style={{ color: '#b0b0b0' }}>{d.toc.kicker}</T>
      <Lines lines={d.toc.title} x={120} cy={158} pitch={69} size={62} className="font-bold" />
    </>
  )
}

function TocList() {
  return (
    <Page>
      <TocFrame photo="arched corridor photo" />
      {d.toc.items.map((it, i) => {
        const cy = 144 + i * 93.5
        return (
          <div key={it.n}>
            <NumBox x={490} y={cy - 20} n={it.n} w={41} h={40} />
            <T x={556} cy={cy - 9} size={25}>{it.title}</T>
            <T x={556} cy={cy + 21} size={14.5} style={G}>{it.desc}</T>
          </div>
        )
      })}
    </Page>
  )
}

function TocGrid() {
  return (
    <Page>
      <TocFrame photo="glass building photo" />
      {d.toc.items.map((it, i) => {
        const cx = [473, 776, 1078][i % 3], dy = Math.floor(i / 3) * 224
        return (
          <div key={it.n}>
            <NumBox x={cx - 20} y={263 + dy} n={it.n} w={41} h={40} />
            <T x={cx - 150} w={300} cy={338 + dy} size={25} align="center">{it.title}</T>
            <Lines lines={d.toc.gridDesc} x={cx - 150} w={300} cy={380 + dy} pitch={23} size={14.5} align="center" style={G} />
          </div>
        )
      })}
    </Page>
  )
}

function Chapter() {
  const c = d.chapter
  return (
    <Page>
      <PhotoPoly pts={[[0, 0], [529, 0], [529, 720], [0, 720]]} label="business documents photo" />
      <Poly pts={[[715, 0], [780, 0], [676, 107], [611, 107]]} />
      <Poly pts={geo.bottomRight} />
      <T x={602} cy={188} size={22} className="tracking-[0.08em]" style={G}>{c.kicker}</T>
      <T x={600} cy={272} size={77} className="font-medium">{c.title}</T>
      <Lines lines={c.lines} x={609} cy={412} pitch={27.5} size={19.8} style={G} />
    </Page>
  )
}

function Section() {
  const c = d.section
  return (
    <Page>
      <Poly pts={geo.stripeWide} />
      <PhotoPoly pts={geo.photoRightSlant} label="skyscraper photo" />
      <Poly pts={[[847, 0], [1177, 0], [1078, 290]]} />
      <Poly pts={[[0, 465], [224, 720], [0, 720]]} />
      <NumBox x={158} y={148} n={c.n} w={63} h={63} size={30} blue />
      <T x={156} cy={299} size={78} className="font-medium">{c.title}</T>
      <Lines lines={c.lines} x={158} cy={384} pitch={30} size={19.5} style={G} />
    </Page>
  )
}

function Ceo() {
  const c = d.ceo
  return (
    <Page bg="#555">
      <Abs x={0} y={0} w={1280} h={720}><ImagePlaceholder label="dark handshake background" tone="#5a5a5a" className="h-full w-full" /></Abs>
      <Poly pts={geo.stripeWide} />
      <Poly pts={geo.cornerTri} />
      <Poly pts={geo.bottomRight} />
      <Abs x={102} y={136} w={475} h={470}><ImagePlaceholder label="CEO portrait" className="h-full w-full" /></Abs>
      <T x={614} cy={261} size={38} className="font-medium" style={W}>{c.title}</T>
      <Lines lines={c.lines} x={616} cy={341} pitch={26} size={15} style={{ color: '#ddd' }} />
      <T x={616} cy={524} size={15} className="font-bold" style={W}>{c.sign}</T>
      <Abs x={760} y={497} w={165} h={56}><ImagePlaceholder label="signature" tone="#777" className="h-full w-full" /></Abs>
      <T x={102} cy={631} size={10} style={{ color: '#ccc' }}>{c.foot}</T>
    </Page>
  )
}

function Result() {
  const c = d.result
  return (
    <Page>
      <Poly pts={geo.stripe} />
      <Poly pts={[[1040, 0], [1280, 0], [1280, 160]]} />
      <Title kicker={c.kicker} title={c.title} />
      <Abs x={0} y={232} w={1280} h={268}><ImagePlaceholder label="meeting room photo" className="h-full w-full" /></Abs>
      <LabelBand pts={[[571, 197], [1240, 197], [1240, 261], [537, 261]]} text={c.band} x={600} w={605} cy={229} align="right" />
      {c.stats.map(([v, u, l], i) => {
        const cx = [165, 313, 462][i]
        return (
          <div key={l}>
            <Abs x={cx - 11} y={541}><Check size={22} color={t.blue} strokeWidth={1.6} /></Abs>
            <T x={cx - 80} w={160} cy={603} size={42} align="center" className="items-baseline font-bold tracking-[-0.03em]" style={B}>{v}<span style={{ fontSize: 17 }}>{u}</span></T>
            <T x={cx - 80} w={160} cy={642} size={15}>{''}</T>
            <T x={cx - 80} w={160} cy={642} size={15} align="center">{l}</T>
          </div>
        )
      })}
      <T x={577} cy={554} size={15.5} className="font-bold">{c.lead}</T>
      <Lines lines={c.lines} x={577} cy={583} pitch={29} size={15.5} />
      <PageNo n="07" />
    </Page>
  )
}

function StripePhotoTR({ photo }: { photo: string }) {
  return (
    <>
      <Poly pts={geo.stripe} />
      <PhotoPoly pts={[[1004, 0], [1280, 0], [1280, 234]]} label={photo} />
      <Poly pts={[[976, 0], [1004, 0], [1280, 234], [1280, 260]]} />
    </>
  )
}

function Vision() {
  const c = d.vision
  return (
    <Page>
      <StripePhotoTR photo="desk documents photo" />
      <Title kicker={c.kicker} title={c.title} />
      {c.cards.map((k, i) => {
        const x = [143, 499, 851][i]
        return (
          <div key={k.title}>
            <HeadCard x={x} y={233} w={333} h={167} head={52} />
            <T x={x} w={333} cy={259} size={24} align="center">{k.title}</T>
            <Lines lines={k.lines} x={x} w={333} cy={328} pitch={29} size={18.5} align="center" style={G} />
          </div>
        )
      })}
      <Abs x={141} y={434} w={1042} h={213} style={{ border: `1.5px solid ${t.line}` }} />
      <Quote x={197} y={466} />
      <Quote x={1086} y={583} close />
      <Lines lines={c.quote} x={140} w={1046} cy={518} pitch={41} size={23.5} align="center" />
      <PageNo n="08" />
    </Page>
  )
}

function History() {
  const c = d.history
  return (
    <Page>
      <StripePhotoTR photo="desk documents photo" />
      <Title kicker={c.kicker} title={c.title} />
      {c.cols.map((col, i) => {
        const x = 98 + i * 302, cx = 87 + i * 302
        return (
          <div key={col.year}>
            <Abs x={x} y={252} w={190} h={62} className="flex items-center justify-center font-bold" style={{ background: t.pale, border: `1.5px solid ${t.line}`, fontSize: 28 }}>{col.year}</Abs>
            {i < 3 && <Abs x={x + 237} y={271}><Play size={24} fill={t.blue} color={t.blue} /></Abs>}
            <HeadCard x={cx} y={348} w={219} h={292} head={78} />
            <T x={cx} w={219} cy={386} size={26} align="center" className="font-bold">{col.title}</T>
            <Bullets items={col.bullets} x={cx + 37} cy={474} pitch={23} gap={18} size={15} />
          </div>
        )
      })}
      <PageNo n="09" />
    </Page>
  )
}

function Brief10() {
  const c = d.brief10
  return (
    <Page>
      <PhotoPoly pts={[[0, 0], [330, 0], [724, 720], [0, 720]]} label="building photo" />
      <Poly pts={[[330, 0], [671, 0], [473, 258]]} />
      <Poly pts={[[1243, 0], [1278, 0], [1209, 70], [1175, 70]]} />
      <T x={800} w={358} cy={101} size={15} align="right" className="tracking-[0.08em]" style={G}>{c.kicker}</T>
      <T x={600} w={560} cy={157} size={56} align="right" className="font-light">{c.light}</T>
      <T x={600} w={560} cy={233} size={56} align="right" className="font-bold">{c.bold}</T>
      {c.rows.map((r) => (
        <div key={r.year}>
          <Abs x={r.x} y={r.y} w={123} h={43} className="flex items-center justify-center" style={{ background: t.blue, color: '#fff', fontSize: 23 }}>{r.year}</Abs>
          <Bullets items={[r.lines]} x={r.x + 167} cy={r.y + 19} pitch={29} gap={0} size={17.5} />
        </div>
      ))}
      <PageNo n="10" />
    </Page>
  )
}

function Areas() {
  const c = d.areas
  return (
    <Page>
      <Poly pts={geo.stripe} />
      <PhotoPoly pts={geo.photoRight} label="glass facade photo" />
      <Title kicker={c.kicker} title={c.title} />
      {c.cards.map((k, i) => {
        const x = [107, 460, 804][i]
        return (
          <div key={k.title}>
            <Abs x={x} y={226} w={314} h={428} className="bg-white" style={{ border: `1.5px solid ${t.line}` }} />
            <Abs x={x + 12} y={238} w={290} h={255}><ImagePlaceholder label="business photo" className="h-full w-full" /></Abs>
            <T x={x} w={314} cy={532} size={25} align="center"><Check size={22} color={t.blue} strokeWidth={1.8} style={{ marginRight: 14 }} />{k.title}</T>
            <Lines lines={k.lines} x={x} w={314} cy={576} pitch={25} size={15.5} align="center" style={G} />
          </div>
        )
      })}
      <PageNo n="11" color="#fff" />
    </Page>
  )
}

function ItemHead({ x, y, w, n, title, h = 73, size = 25 }: { x: number; y: number; w: number; n: string; title: string; h?: number; size?: number }) {
  return (
    <>
      <Abs x={x} y={y} w={w} h={h} style={{ background: t.pale }} />
      <NumBox x={x - 17} y={y + 14} n={n} />
      <T x={x + 54} cy={y + 35} size={size}>{title}</T>
    </>
  )
}

function Share() {
  const c = d.share
  let acc = 0
  const stops = c.pie.map((s) => `${s.c} ${acc}deg ${(acc += s.v * 3.6)}deg`).join(', ')
  return (
    <Page>
      <Poly pts={geo.stripe} />
      <Poly pts={geo.cornerTri} />
      <Title kicker={c.kicker} title={c.title} />
      <Abs x={125} y={233} w={432} h={407} style={{ background: t.panel }} />
      <Abs x={207} y={285} w={270} h={270} className="rounded-full" style={{ background: `conic-gradient(${stops})` }} />
      {c.pie.map((s) => (
        <div key={s.label} style={{ color: s.white ? '#fff' : t.ink }}>
          <T x={s.x - 60} w={120} cy={s.y} size={19.5} align="center">{s.label}</T>
          <T x={s.x - 60} w={120} cy={s.y + 34} size={19.5} align="center">{`(${s.v}%)`}</T>
        </div>
      ))}
      <T x={125} w={432} cy={601} size={16} align="center">{c.caption}</T>
      {c.items.map((it, i) => (
        <div key={i}>
          <Abs x={660} y={98 + i * 288} w={528} h={256} style={{ border: `1.5px solid ${t.line}` }} />
          <ItemHead x={660} y={98 + i * 288} w={528} n={it.n} title={it.title} />
          <Bullets items={it.bullets} x={717} cy={225 + i * 288} pitch={29} gap={0} size={18} />
        </div>
      ))}
      <PageNo n="12" />
    </Page>
  )
}

function Trend() {
  const c = d.trend
  const y = (v: number) => 539 - v * 2.83
  const pts = c.points.map(([x, v]) => `${x},${y(v)}`).join(' ')
  return (
    <Page>
      <Poly pts={geo.stripe} />
      <PhotoPoly pts={geo.photoRight} label="glass facade photo" />
      <Title kicker={c.kicker} title={c.title} />
      <Abs x={50} y={228} w={1179} h={417} className="bg-white" style={{ border: `1.5px solid ${t.line}` }} />
      <Abs x={98} y={280} w={671} h={315} style={{ background: t.panel }} />
      {c.ticks.map((v) => (
        <div key={v}>
          <T x={112} w={40} cy={y(v)} size={15} align="right">{v}</T>
          <Abs x={160} y={y(v)} w={572} h={1} style={{ background: v ? '#d5dbe3' : '#9aa5b5' }} />
        </div>
      ))}
      <svg className="absolute left-0 top-0" width={1280} height={720}>
        <defs><linearGradient id="d21area" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stopColor="#a9bad6" /><stop offset="1" stopColor="#a9bad6" stopOpacity={0.15} /></linearGradient></defs>
        <polygon points={`${c.points[0][0]},539 ${pts} ${c.points[3][0]},539`} fill="url(#d21area)" />
        <polyline points={pts} fill="none" stroke={t.blue} strokeWidth={1} />
        {c.points.map(([x, v]) => <circle key={x} cx={x} cy={y(v)} r={3.5} fill={t.blue} />)}
      </svg>
      {c.labels.map(([l, x]) => <T key={l} x={x - 50} w={100} cy={555} size={16} align="center">{l}</T>)}
      {c.items.map((it, i) => (
        <div key={i}>
          <NumBox x={826} y={279 + i * 171} n={it.n} />
          <T x={898} cy={300 + i * 171} size={25}>{it.title}</T>
          <Bullets items={it.bullets} x={914} cy={345 + i * 171} pitch={24} gap={0} size={14.5} />
        </div>
      ))}
      <PageNo n="13" color="#fff" />
    </Page>
  )
}

const factorIcons = { calendar: CalendarCheck2, org: Network, doc: NotebookPen }
function Compare() {
  const c = d.compare
  return (
    <Page>
      <Poly pts={geo.stripe} />
      <PhotoPoly pts={geo.photoRightSlant} label="skyscraper photo" />
      <Poly pts={[[841, 0], [1177, 0], [1102, 200]]} />
      <Title kicker={c.kicker} title={c.title} />
      <Abs x={83} y={234} w={432} h={411} style={{ background: t.panel }} />
      <T x={83} w={432} cy={277} size={11} align="center">
        {c.legend.map((l, i) => <span key={l} className="mr-[5px] inline-flex items-center"><span className="mr-[3px] inline-block h-[9px] w-[9px] rounded-[2px]" style={{ background: i ? '#bcc8cf' : '#5578b3' }} />{l}</span>)}
      </T>
      {[305, 364, 424, 485, 545].map((yy) => <Abs key={yy} x={136} y={yy} w={327} h={1} style={{ background: '#d5dbe3' }} />)}
      {c.bars.map(([x, w, top, k]) => <Abs key={x} x={x} y={top} w={w} h={545 - top} style={{ background: k === 'blue' ? '#5578b3' : '#bcc8cf' }} />)}
      <T x={83} w={432} cy={603} size={17} align="center">{c.caption}</T>
      {c.items.map((it, i) => {
        const y = 232 + i * 145, Icon = factorIcons[it.icon]
        return (
          <div key={it.n}>
            <Abs x={579} y={y} w={617} h={124} className="bg-white" style={{ border: `1.5px solid ${t.line}` }} />
            <Abs x={579} y={y} w={154} h={124} style={{ background: t.pale }} />
            <NumBox x={557} y={y + 41} n={it.n} />
            <Abs x={630} y={y + 33}><Icon size={58} color={t.ink} strokeWidth={1.3} /></Abs>
            <T x={769} cy={y + 40} size={21}>{it.title}</T>
            <Lines lines={it.lines} x={769} cy={y + 70} pitch={24} size={14.5} />
          </div>
        )
      })}
      <PageNo n="14" color="#fff" />
    </Page>
  )
}

function Partners() {
  const c = d.partners
  return (
    <Page>
      <Poly pts={geo.stripe} />
      <Poly pts={[[940, 0], [1280, 0], [1280, 350]]} />
      <Title kicker={c.kicker} title={c.title} />
      {c.cards.map((k, i) => {
        const x = [71, 653][i]
        return (
          <div key={k.title}>
            <Abs x={x} y={214} w={556} h={257}><ImagePlaceholder label="business photo" className="h-full w-full" /></Abs>
            <HeadCard x={x} y={496} w={556} h={157} head={58} />
            <T x={x} w={556} cy={524} size={26} align="center">{k.title}</T>
            <Lines lines={k.lines} x={x} w={556} cy={584} pitch={30} size={18} align="center" />
          </div>
        )
      })}
      <PageNo n="15" />
    </Page>
  )
}

function Analysis1() {
  const c = d.analysis
  return (
    <Page>
      <Poly pts={geo.stripe} />
      <PhotoPoly pts={[[1137, 0], [1280, 0], [1280, 720], [933, 720]]} label="desk with glasses photo" />
      <Poly pts={[[0, 228], [575, 228], [271, 720], [0, 720]]} />
      <Title kicker={c.kicker} title={c.title} />
      <LabelBand pts={[[631, 125], [1280, 125], [1280, 188], [598, 188]]} text={c.band} x={640} w={474} cy={156} align="center" />
      <Quote x={120} y={279} color="#fff" />
      <Lines lines={c.quote} x={121} cy={351} pitch={38} size={20} style={W} />
      {c.stepsA.map((s) => (
        <div key={s.n}>
          <Abs x={s.box[0]} y={s.box[1]} w={43} h={43} className="flex items-center justify-center" style={{ background: t.blue, color: '#fff', fontSize: 19 }}>{s.n}</Abs>
          <Lines lines={s.lines} x={s.right - 460} w={460} cy={s.cy} pitch={26.5} size={17} align="right" />
        </div>
      ))}
      <PageNo n="16" color="#fff" />
    </Page>
  )
}

function Analysis2() {
  const c = d.analysis
  return (
    <Page>
      <Poly pts={geo.stripe} />
      <PhotoPoly pts={geo.photoRightSlant} label="desk with calculator photo" />
      <Poly pts={[[994, 0], [1177, 0], [1122, 150]]} />
      <Title kicker={c.kicker} title={c.title} />
      <Abs x={82} y={219} w={1147} h={413} className="bg-white" style={{ border: `1.5px solid ${t.line}` }} />
      <Poly pts={[[838, 219], [1229, 219], [1229, 632], [838, 632], [838, 448], [820, 430], [838, 412]]} />
      <LabelBand pts={[[50, 245], [651, 245], [729, 308], [50, 308]]} text={c.band} x={127} cy={275} />
      {c.stepsB.map((lines, i) => {
        const y = [357, 449, 544][i]
        return (
          <div key={i}>
            <Abs x={136} y={y} w={44} h={45} className="flex items-center justify-center" style={{ background: t.blue, color: '#fff', fontSize: 19 }}>{i + 1}</Abs>
            <Lines lines={lines} x={224} cy={y + 9} pitch={26.5} size={17.5} />
          </div>
        )
      })}
      <Quote x={1014} y={285} color="#fff" size={34} />
      <Quote x={1014} y={562} color="#fff" size={34} close />
      <Lines lines={c.quote} x={838} w={391} cy={368} pitch={38} size={20} align="center" style={W} />
      <PageNo n="17" />
    </Page>
  )
}

function LeftPhotoFrame({ photo }: { photo: string }) {
  return (
    <>
      <PhotoPoly pts={geo.photoLeft} label={photo} />
      <Poly pts={geo.stripeMid} />
      <Poly pts={geo.cornerTri} />
    </>
  )
}

function Perf() {
  const c = d.perf
  return (
    <Page>
      <LeftPhotoFrame photo="laptop and charts photo" />
      <Poly pts={[[0, 560], [140, 720], [0, 720]]} />
      <Title kicker={c.kicker} title={c.title} x={527} />
      <Tick x={524} cy={243} />
      <Lines lines={c.lines} x={571} cy={239} pitch={29} size={20} />
      <Abs x={521} y={319} w={342} h={342} className="rounded-full" style={{ background: '#e6ebf0' }} />
      <Abs x={847} y={385} w={232} h={232} className="rounded-full" style={{ background: t.blue }} />
      <T x={542} w={300} cy={470} size={78} align="center" className="font-medium tracking-[-0.03em]">{c.a[0]}</T>
      <T x={542} w={300} cy={544} size={22} align="center">{c.a[1]}</T>
      <T x={863} w={200} cy={480} size={40} align="center" className="font-medium" style={W}>{c.b[0]}</T>
      <T x={863} w={200} cy={529} size={22} align="center" style={W}>{c.b[1]}</T>
      <PageNo n="18" />
    </Page>
  )
}

function Big({ x, w, cy, v, unit, size }: { x: number; w: number; cy: number; v: string; unit: string; size: number }) {
  return <T x={x} w={w} cy={cy} size={size} align="center" className="items-baseline font-medium tracking-[-0.04em]" style={B}>{v}<span style={{ fontSize: 19, marginLeft: 4 }}>{unit}</span></T>
}

function Kpis() {
  const c = d.kpis, f = c.first
  return (
    <Page>
      <Poly pts={geo.stripe} />
      <PhotoPoly pts={geo.photoRight} label="skyscraper photo" />
      <Title kicker={c.kicker} title={c.title} />
      <Abs x={100} y={241} w={338} h={405} className="bg-white" style={{ border: `1.5px solid ${t.line}` }}><div style={{ height: 210, background: t.pale }} /></Abs>
      <NumBox x={78} y={257} n={f.n} w={44} />
      <T x={100} w={325} cy={293} size={19} align="center">{f.label}</T>
      <Big x={100} w={338} cy={380} v={f.v} unit={f.unit} size={104} />
      <Lines lines={f.lines} x={137} w={266} cy={503} pitch={27.5} size={17} justify />
      {c.rows.map((r, i) => {
        const y = 241 + i * 211
        return (
          <div key={r.n}>
            <Abs x={479} y={y} w={722} h={194} className="bg-white" style={{ border: `1.5px solid ${t.line}` }} />
            <Abs x={479} y={y} w={306} h={194} style={{ background: t.pale }} />
            <NumBox x={465} y={y + 15} n={r.n} w={44} />
            <T x={479} w={306} cy={y + 47} size={19} align="center">{r.label}</T>
            <Big x={479} w={306} cy={y + 120} v={r.v} unit={r.unit} size={94} />
            <Lines lines={r.lines} x={804} cy={y + 55} pitch={27} size={17} />
          </div>
        )
      })}
      <PageNo n="19" color="#fff" />
    </Page>
  )
}

function Conclusion() {
  const c = d.conclusion
  return (
    <Page>
      <LeftPhotoFrame photo="notebook and calculator photo" />
      <Title kicker={c.kicker} title={c.title} x={527} />
      <LabelBand pts={[[359, 233], [1100, 233], [1154, 296], [359, 296]]} text={c.band} x={522} cy={264} />
      {c.items.map((lines, i) => {
        const cy = [355, 462, 558][i]
        return (
          <div key={i}>
            <Tick x={524} cy={cy + 1} />
            <Lines lines={lines} x={571} cy={cy - 1} pitch={28} size={20} />
          </div>
        )
      })}
      <PageNo n="20" />
    </Page>
  )
}

function Team() {
  const c = d.team
  const cols = [[78, 533, 336], [558, 867, 713], [891, 1199, 1045]]
  return (
    <Page>
      <Poly pts={geo.stripe} />
      <PhotoPoly pts={[[940, 0], [1185, 0], [1122, 180]]} label="building photo" />
      <Poly pts={[[1185, 0], [1280, 0], [1280, 720], [933, 720]]} />
      <Title kicker={c.kicker} title={c.title} x={132} cy={168} />
      {c.rows.map((row, ri) => row.map((p, ci) => {
        const [x0, x1, px] = cols[ci], y = 253 + ri * 194
        return (
          <div key={p.name}>
            <Abs x={x0} y={y} w={x1 - x0} h={162} style={{ background: t.pale }} />
            <Abs x={px} y={y} w={x1 - px} h={162}><ImagePlaceholder label="member portrait" tone="#cdd2d8" className="h-full w-full" /></Abs>
            <Lines lines={p.lines} x={x0 + 21} cy={y + 22} pitch={17.5} size={11.5} style={{ color: '#7d8da6' }} />
            <T x={x0 + 21} cy={y + 107} size={11.5} style={{ color: '#5d7cb3' }}>{c.company}</T>
            <T x={x0 + 20} cy={y + 133} size={21} style={B}>{p.name}</T>
          </div>
        )
      }))}
      <T x={78} cy={630} size={9.5} style={{ color: '#aaa' }}>{c.foot}</T>
      <PageNo n="21" color="#fff" />
    </Page>
  )
}

function Info() {
  const c = d.info
  let y = 317
  return (
    <Page>
      <Poly pts={geo.stripe} />
      <PhotoPoly pts={geo.photoRightSlant} label="glass building photo" />
      <Poly pts={[[994, 0], [1177, 0], [1128, 150]]} />
      <Title kicker={c.kicker} title={c.title} cy={158} />
      <Abs x={87} y={236} w={1106} h={406} className="bg-white" style={{ border: `1.5px solid ${t.line}` }} />
      <Abs x={115} y={264} w={488} h={349}><ImagePlaceholder label="map" className="h-full w-full" /></Abs>
      <Abs x={331} y={352}><MapPin size={62} fill={t.blue} color="#fff" strokeWidth={1.4} /></Abs>
      <T x={262} w={200} cy={440} size={12} align="center" style={B}>{c.pin}</T>
      {c.items.map((it) => {
        const y0 = y
        y += 103 + (it.lines.length - 1) * 30
        return (
          <div key={it.head}>
            <Abs x={647} y={y0 - 16}><Check size={30} color={t.ink} strokeWidth={2} /></Abs>
            <Abs x={647} y={y0 - 11} w={26} h={26} style={{ border: '1.5px solid #d0d0d0', borderTop: 0, borderRight: 0 }} />
            <T x={694} cy={y0} size={22}>{it.head}</T>
            <Lines lines={it.lines} x={694} cy={y0 + 31} pitch={31} size={19} />
          </div>
        )
      })}
      <PageNo n="22" color="#fff" />
    </Page>
  )
}

function Closing() {
  const c = d.closing
  return (
    <Page>
      <Poly pts={[[0, 0], [62, 0], [165, 108], [103, 108]]} />
      <Poly pts={[[1280, 184], [1280, 720], [806, 720]]} />
      <PhotoPoly pts={[[806, 0], [1280, 0], [1280, 190], [1105, 375]]} label="applauding people photo" />
      <Poly pts={[[1230, 250], [1280, 215], [1280, 320]]} c="#b6c4d4" />
      <T x={103} cy={271} size={42} className="tracking-[0.04em]" style={{ color: '#999' }}>{c.en}</T>
      <T x={96} cy={385} size={118} className="font-medium tracking-[-0.03em]">{c.kr}</T>
      <T x={96} cy={618} size={18} className="font-semibold">{d.byline}</T>
      <T x={96} cy={647} size={18} className="font-semibold">{c.mail}</T>
      <Lines lines={d.brief} x={900} w={331} cy={627} pitch={21} size={15} align="right" style={BRIEF} />
    </Page>
  )
}

const deck: DeckDefinition = {
  id: '21', title: '파랑과 하늘색의 심플한 기업 보고서',
  slides: [Cover, TocList, TocGrid, Chapter, Section, Ceo, Result, Vision, History, Brief10, Areas, Share, Trend, Compare, Partners, Analysis1, Analysis2, Perf, Kpis, Conclusion, Team, Info, Closing],
}
export default deck
