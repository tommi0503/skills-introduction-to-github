import { Award, Building2, PersonStanding, CalendarDays, ChartPie, Database, FilePlus2, Plus, FilePen, FileCog, Flag, Presentation, Lightbulb, CloudDownload, ChartColumnIncreasing, UserSquare, FolderOpen, Hand, IdCard, ListChecks, MousePointerClick, Settings, TrendingUp, UserRound } from 'lucide-react'
import { Abs, ImagePlaceholder, cn } from '../../ui'
import { Disc, Folder, FolderCard, Heading, Lines, Photo, SerifPill, T } from '../d11/components'
import { ch } from '../d11/slides'
import { t } from '../d11/theme'
import { org, timetable, bars, heatmap, lines, pies, cause, company, growth, part, table, venn, worldMap, gallery, mockup, pyramid, qna, stairs, summaryBoard, vertical, zoom } from './data'

/** Centred kicker + title used by most d15 pages. */
export const CHead = ({ kicker, title, y = 157 }: { kicker: string; title: string; y?: number }) => (
  <Heading kicker={kicker} title={title} y={y} x={49} w={1127} align="center" size={47} />
)

const coIcons = [[Building2, UserRound, CalendarDays, Flag], [FolderOpen, IdCard, Database, ChartPie]]
export function Company() {
  return (
    <Folder chapter={ch(2)}>
      <CHead kicker={company.kicker} title={company.title} />
      {company.paras.map((p, i) => <Lines key={i} x={[118, 630][i]} y={260} size={16} lh={26} lines={p} style={{ color: t.body }} />)}
      {company.cols.map((col, ci) => col.map(([k, v], ri) => {
        const x = [118, 630][ci], cy = 416 + ri * 63, Icon = coIcons[ci][ri]
        return (
          <div key={k}>
            <SerifPill x={x} y={cy - 16} w={113} h={33} radius={0} text="" bg={ci ? '#eeedea' : '#f8ece1'} />
            <T x={x} y={cy - 8} w={113} size={16} align="center" style={{ color: t.ink }}>{k}</T>
            <T x={x + 130} y={cy - 8} size={16} style={{ color: t.ink }}>{v}</T>
            <Abs x={x + 428} y={cy - 14}><Icon size={28} strokeWidth={1} color={t.ink} /></Abs>
            <Abs x={x} y={cy + 24} w={466} h={1} style={{ background: t.rule }} />
          </div>
        )
      }))}
    </Folder>
  )
}

export function Vertical() {
  return (
    <Folder chapter={ch(4)}>
      <CHead kicker={vertical.kicker} title={vertical.title} />
      {vertical.rows.map((r, i) => {
        const y = [247, 462][i]
        return (
          <div key={r.label}>
            <FolderCard x={94} y={y} w={1019} h={198} tab="right" tabW={180} tabH={16} bg={i ? '#f8f2e2' : '#ebebe6'} />
            <T x={148} y={y + 44} size={15.5} className={cn(t.serif, 'font-semibold')} style={{ color: t.ink }}>{r.label}</T>
            <T x={237} y={y + 43} size={18.5} className="font-semibold">{r.head}</T>
            <Lines x={237} y={y + 86} size={15.5} lh={25} lines={r.body} style={{ color: t.body }} />
            <Photo x={667} y={y + 15} w={422} h={168} />
          </div>
        )
      })}
    </Folder>
  )
}

export function Zoom() {
  return (
    <Folder chapter={ch(7)}>
      <Heading kicker={zoom.kicker} title={zoom.title} y={253} size={47} />
      <Lines x={101} y={341} size={17.5} lh={27} lines={zoom.lead} className="font-medium" style={{ color: t.ink }} />
      <Lines x={101} y={423} w={410} size={15.5} lh={25.4} lines={zoom.body} justify style={{ color: t.body }} />
      <FolderCard x={548} y={148} w={589} h={518} tab="none" bg="#f0eee9" />
      <Abs x={1012} y={131} w={125} h={18} style={{ background: '#f0eee9', clipPath: 'polygon(17px 0, 100% 0, 100% 100%, 0 100%)' }} />
      <Abs x={564} y={157} w={560} h={495}><ImagePlaceholder label="dashboard under magnifier" className="h-full w-full" /></Abs>
    </Folder>
  )
}

const qBg = ['#fceee8', '#fbf4e6', '#ebeae7']
export function Qna() {
  return (
    <Folder chapter={ch(8)}>
      <CHead kicker={qna.kicker} title={qna.title} />
      <Abs x={225} y={250} w={772} h={74} className="rounded-full" style={{ background: '#f0ece7' }} />
      <Disc cx={263} cy={287} r={33} bg="#5a5248"><span className={cn(t.serif, 'leading-none text-white')} style={{ fontSize: 30 }}>Q</span></Disc>
      <T x={326} y={277} w={600} size={20} align="center" className="font-medium" style={{ color: t.ink }}>{qna.q}</T>
      {qna.cards.map((c, i) => {
        const x = [87, 442, 796][i], tx = [x + 324, x + 169, x + 14][i]
        return (
          <div key={i}>
            <Abs x={tx - 10} y={356} w={20} h={15} style={{ background: qBg[i], clipPath: 'polygon(50% 0, 100% 100%, 0 100%)' }} />
            <Abs x={x} y={370} w={338} h={283} style={{ background: qBg[i] }} />
            <Abs x={x + 116} y={400} w={106} h={106} className="overflow-hidden rounded-full bg-white"><ImagePlaceholder label="person illustration" className="h-full w-full" /></Abs>
            <Lines x={x} y={532} w={338} size={17} lh={25} align="center" lines={c.lines} style={{ color: t.ink }} />
            <T x={x} y={600} w={338} size={14.5} align="center" style={{ color: t.body }}>{c.who}</T>
          </div>
        )
      })}
    </Folder>
  )
}

export function SummaryBoard() {
  return (
    <Folder chapter={ch(9)}>
      <Heading kicker={summaryBoard.kicker} title={summaryBoard.title} y={157} size={47} />
      {summaryBoard.cards.map((c, i) => {
        const x = [97, 613][i], w = [506, 504][i]
        return (
          <div key={c.k}>
            <FolderCard x={x} y={257} w={w} h={201} tabW={141} tabH={18} bg={i ? '#f6ecea' : '#efede8'} />
            <T x={x + 37} y={258} size={13.5} className={t.serif} style={{ color: t.ink }}>{c.k}</T>
            <T x={x} y={309} w={w} size={18.8} align="center" className="font-medium" style={{ color: t.ink }}>{c.head}</T>
            <Abs x={x + 17} y={350} w={w - 34} h={1} style={{ background: '#d0ccc6' }} />
            <Lines x={x} y={372} w={w} size={15.5} lh={25.5} align="center" lines={c.body} style={{ color: t.body }} />
          </div>
        )
      })}
      <Abs x={97} y={477} w={1020} h={185} style={{ background: '#f8f3e3' }} />
      {summaryBoard.results.map((r, i) => {
        const cy = 512 + i * 53.5
        return (
          <div key={r.k}>
            <SerifPill x={139} y={cy - 16} w={115} h={33} radius={0} text={r.k} bg="#fff" size={13.5} />
            <T x={269} y={cy - 8} size={16} style={{ color: t.ink }}>{r.text}</T>
            <Abs x={139} y={cy + 26} w={536} h={1} style={{ background: '#d8d2c8' }} />
          </div>
        )
      })}
      <Photo x={711} y={491} w={390} h={156} />
    </Folder>
  )
}

const stBox = [
  { x: 87, top: 551, bg: '#ebebe7' }, { x: 338, top: 430, bg: '#fbeee3' }, { x: 589, top: 318, bg: '#fbf3e6' }, { x: 839, top: 197, bg: '#e9e9e7' },
]
const stIcons = [null, Settings, ListChecks, FilePlus2]
export function Stairs() {
  return (
    <Folder chapter={ch(11)}>
      <Heading kicker={stairs.kicker} title={stairs.title} y={190} size={47} />
      <Lines x={101} y={263} size={15.5} lh={24} lines={stairs.intro} style={{ color: t.body }} />
      {[...stairs.steps].reverse().map((s, ri) => {
        const i = 3 - ri, b = stBox[i], Icon = stIcons[i]
        const right = b.x + (i ? 272 : 278)
        return (
          <div key={s.step}>
            <FolderCard x={b.x} y={b.top} w={i === 3 ? 296 : 296} h={658 - b.top} tabW={88} tabH={18} bg={b.bg} />
            <T x={b.x + 25} y={b.top - 15} size={13.5} className={t.serif} style={{ color: t.ink }}>{s.step}</T>
            <T x={b.x + 22} y={b.top + 29} size={17} className="font-semibold">{s.head}</T>
            {i === 0
              ? <T x={b.x + 46} y={b.top + 69} size={15.5} style={{ color: t.body }}>{s.body[0]}</T>
              : <Lines x={right - 300} y={b.top + 75} w={300} size={15} lh={21.5} align="right" lines={s.body} style={{ color: t.body }} />}
            {Icon && <Abs x={[0, 568, 820, 1071][i]} y={598}><Icon size={36} strokeWidth={1} color={t.ink} /></Abs>}
          </div>
        )
      })}
    </Folder>
  )
}

const mkIcons = [MousePointerClick, Hand, TrendingUp]
const mkBg = ['#ebebe6', '#fbf3e6', '#fbeee8']
export function Mockup() {
  return (
    <Folder chapter={ch(12)}>
      <Heading kicker={mockup.kicker} title={mockup.title} y={157} x={112} size={47} />
      <Abs x={109} y={254} w={481} h={386}><ImagePlaceholder label="monitor mockup" className="h-full w-full rounded-[10px]" /></Abs>
      {mockup.items.map((m, i) => {
        const y = 274 + i * 134, Icon = mkIcons[i]
        return (
          <div key={m.k}>
            <FolderCard x={616} y={y} w={185} h={104} tabW={70} tabH={13} bg={mkBg[i]} />
            <Abs x={692} y={y + 21}><Icon size={32} strokeWidth={1} color={t.ink} /></Abs>
            <T x={616} y={y + 65} w={185} size={17.5} align="center" style={{ color: t.ink }}>{m.k}</T>
            <Lines x={825} y={y + 22} size={15.5} lh={25} lines={m.body} style={{ color: t.body }} />
            {i < 2 && <Abs x={816} y={y + 112} w={313} h={1} style={{ background: t.rule }} />}
          </div>
        )
      })}
    </Folder>
  )
}

export function Gallery() {
  return (
    <Folder chapter={ch(13)}>
      <CHead kicker={gallery.kicker} title={gallery.title} />
      {gallery.cells.map((c, i) => {
        const x = 81 + (i % 4) * 266.25, y = i < 4 ? 257 : 457
        if (!c) return <Photo key={i} x={x} y={y} w={266.25} h={200} />
        return (
          <div key={i}>
            <Abs x={x} y={y} w={266.25} h={200} style={{ background: c.bg }} />
            <T x={x} y={y + 42} w={266} size={13.5} align="center" className={t.serif} style={{ color: t.ink }}>{c.k}</T>
            <T x={x} y={y + 82} w={266} size={17.5} align="center" className="font-semibold">{c.head}</T>
            <Lines x={x} y={y + 113} w={266} size={15} lh={24} align="center" lines={gallery.body} style={{ color: t.body }} />
          </div>
        )
      })}
    </Folder>
  )
}

const pyBands = [[227, 300, '#cbc6bf'], [308, 398, '#dcd9d3'], [406, 502, '#fbe9e2'], [509, 657, '#faf2e3']] as const
const pyIcons = [Database, Presentation, FilePen, FileCog]
export function Pyramid() {
  const cx = 626, hw = (y: number) => ((y - 227) / 430) * 247
  return (
    <Folder chapter={ch(14)}>
      <Heading kicker={pyramid.kicker} title={pyramid.title} y={157} x={112} size={47} />
      {pyBands.map(([y0, y1, bg], i) => {
        const Icon = pyIcons[i], l = cx - hw(y1), w = hw(y1) * 2
        const pts = `${cx - hw(y0) - l}px 0, ${cx + hw(y0) - l}px 0, 100% 100%, 0 100%`
        return (
          <div key={i}>
            <Abs x={l} y={y0} w={w} h={y1 - y0} style={{ background: bg, clipPath: `polygon(${pts})` }} />
            <Abs x={cx - 19} y={(y0 + y1) / 2 - (i ? 19 : 8)}><Icon size={38} strokeWidth={1} color={t.ink} /></Abs>
          </div>
        )
      })}
      {pyramid.notes.map((n, i) => {
        const right = n.side === 'r'
        return (
          <div key={i}>
            <T x={right ? n.x : n.x - 400} y={n.cy - 9} w={right ? undefined : 400} size={17.5} align={right ? 'left' : 'right'} className="font-medium" style={{ color: t.ink }}>{n.head}</T>
            <Lines x={right ? n.x : n.x - 400} y={n.cy + 21} w={right ? undefined : 400} size={14.5} lh={22} align={right ? 'left' : 'right'} lines={n.body} style={{ color: t.body }} />
            <Abs x={right ? n.x - 92 : n.x + 15} y={n.cy + 20} w={70} h={1} style={{ background: '#c8c4be' }} />
            <Abs x={right ? n.x - 26 : n.x + 13} y={n.cy + 18} w={5} h={5} className="rounded-full" style={{ background: '#b8b4ae' }} />
          </div>
        )
      })}
    </Folder>
  )
}

const caIcons = [[Lightbulb, ChartColumnIncreasing], [CloudDownload, UserSquare]]
export function Cause() {
  return (
    <Folder chapter={ch(15)}>
      <CHead kicker={cause.kicker} title={cause.title} />
      {cause.rows.map((r, i) => {
        const y = [267, 469][i]
        return (
          <div key={r.k}>
            <FolderCard x={90} y={y} w={466} h={171} tabW={80} tabH={13} bg={i ? '#fbf3e3' : '#efeeeb'} />
            <T x={113} y={y + 2} size={13.5} className={t.serif} style={{ color: t.ink }}>{r.k}</T>
            <Abs x={566} y={y + 45} w={88} h={76} style={{ background: 'linear-gradient(90deg, #f3f2ef, #d6d3ce)', clipPath: 'polygon(0 22%, 60% 22%, 60% 0, 100% 50%, 60% 100%, 60% 78%, 0 78%)' }} />
            <Abs x={666} y={y} w={467} h={171} style={{ background: '#c9c4bd' }} />
            {[r.cause, r.effect].map((side, j) => {
              const x0 = j ? 666 : 90, Icon = caIcons[i][j], fg = j ? '#fff' : t.ink
              return (
                <div key={j}>
                  <Abs x={x0 + 57} y={y + 56}><Icon size={38} strokeWidth={1} color={fg} /></Abs>
                  <T x={x0} y={y + 117} w={152} size={17} align="center" className="font-medium" style={{ color: fg }}>{side.label}</T>
                  <Abs x={x0 + 160} y={y + 31} w={1} h={117} style={{ background: j ? '#e2ded8' : '#d0ccc6' }} />
                  <Lines x={x0 + 203} y={y + 44} size={15.5} lh={21.7} lines={side.body} style={{ color: j ? '#f6f4f0' : t.body }} />
                </div>
              )
            })}
          </div>
        )
      })}
    </Folder>
  )
}

export function Venn() {
  return (
    <Folder chapter={ch(16)}>
      <CHead kicker={venn.kicker} title={venn.title} />
      {venn.circles.map((c, i) => <Disc key={c} cx={247 + i * 182.5} cy={380} r={128} bg="#efede9" />)}
      {venn.circles.map((c, i) => (
        <Disc key={c} cx={247 + i * 182.5} cy={380} r={111} bg="#f8f6f3" style={{ border: '1px solid #ebe7e1' }}>
          <span className="font-medium leading-none" style={{ fontSize: 17.5, color: t.ink }}>{c}</span>
          <div className="mt-[20px] text-center" style={{ fontSize: 15, lineHeight: '25px', color: t.body }}>{venn.detail.map((d, j) => <div key={j}>{d}</div>)}</div>
        </Disc>
      ))}
      {venn.plus.map((c, i) => <Disc key={i} cx={338 + i * 183.5} cy={380} r={10} bg={c}><Plus size={14} color="#fff" strokeWidth={1.5} /></Disc>)}
      <Abs x={132} y={530} w={959} h={112} style={{ background: '#faf3e2' }} />
      <T x={176} y={559} size={16.9} className="font-medium" style={{ color: t.ink }}>{venn.note}</T>
      {venn.items.map((it, i) => (
        <div key={i}>
          <Disc cx={[187, 500, 813][i]} cy={607} r={10} bg={it.c}><Plus size={14} color="#fff" strokeWidth={1.5} /></Disc>
          <T x={[210, 522, 836][i]} y={598} size={16} style={{ color: t.ink }}>{it.text}</T>
        </div>
      ))}
    </Folder>
  )
}

export function Part() {
  return (
    <Folder>
      <Abs x={49} y={22} w={754} h={676} style={{ background: t.beige }} />
      <Abs x={746} y={303} w={114} h={114} className="rounded-full bg-white" />
      {/* one element so the label and the oversized numeral share a text box */}
      <T x={107} y={213} size={24} className={cn(t.serif, 'font-semibold')} style={{ color: t.ink, letterSpacing: '0.33em' }}>
        {part.label}
        <span className="absolute left-[-19px] top-[-25px]" style={{ fontSize: 190, letterSpacing: 0 }}>{part.no}</span>
      </T>
      <Abs x={157} y={375} w={1} h={267} style={{ background: '#a8a29a' }} />
      <T x={182} y={523} size={40} className="font-medium" style={{ color: t.ink }}>{part.title}</T>
      <Lines x={182} y={585} size={16.5} lh={30} lines={part.body} style={{ color: t.body }} />
      {part.toc.map(([c, txt], i) => {
        const cy = 107 + i * 51.8
        return (
          <div key={c}>
            <T x={838} y={cy - 6} size={13} className={t.serif} style={{ color: t.ink }}>{c}</T>
            <T x={919} y={cy - 9} size={17} style={{ color: t.ink }}>{txt}</T>
            <Abs x={838} y={cy + 21} w={299} h={1} style={{ background: t.rule }} />
          </div>
        )
      })}
    </Folder>
  )
}

const grBox = [{ x: 102, top: 318, bg: '#ebe9e6' }, { x: 454, top: 273, bg: '#faf2e2' }, { x: 804, top: 227, bg: '#e9e8e6' }]
export function Growth() {
  return (
    <Folder chapter={ch(17)}>
      <Heading kicker={growth.kicker} title={growth.title} y={157} size={47} />
      <Abs x={272} y={473} w={680} h={109}><ImagePlaceholder label="swoosh arrow graphic" className="h-full w-full rounded-[50px]" /></Abs>
      {growth.cards.map((c, i) => {
        const b = grBox[i]
        return (
          <div key={i}>
            <FolderCard x={b.x} y={b.top} w={316} h={222} tabW={122} tabH={16} bg={b.bg} />
            <T x={b.x} y={b.top + 37} w={316} size={15} align="center" className={cn(t.serif, 'font-medium')} style={{ color: t.ink, fontVariantCaps: 'all-small-caps' }}>{c.date}</T>
            <T x={b.x} y={b.top + 74} w={316} size={17} align="center" className="font-semibold">{c.head}</T>
            <Lines x={b.x} y={b.top + 108} w={316} size={14.5} lh={22.5} align="center" lines={c.body} style={{ color: t.body }} />
          </div>
        )
      })}
      {growth.big.map((n, i) => <T key={i} x={[160, 491, 842][i]} y={[590, 566, 549][i]} w={[200, 240, 240][i]} size={[60, 76, 88][i]} align="center" className={cn(t.serif, 'font-semibold')} style={{ color: t.ink }}>{n}</T>)}
    </Folder>
  )
}

export function Table() {
  const xs = [106, 309, 512, 715, 918, 1120]
  const line = '#dedad4'
  return (
    <Folder chapter={ch(18)}>
      <CHead kicker={table.kicker} title={table.title} />
      <Abs x={106} y={254} w={1014} h={50} style={{ background: '#5c5045' }} />
      <Abs x={106} y={304} w={203} h={349} style={{ background: '#ede9e4' }} />
      {table.head.map((h, i) => <T key={h} x={xs[i]} y={272} w={203} size={15} align="center" className="font-medium text-white">{h}</T>)}
      {xs.slice(2, 5).map((x) => <Abs key={x} x={x} y={304} w={1} h={349} style={{ background: line }} />)}
      <Abs x={309} y={304} w={1} h={349} style={{ background: line }} />
      {table.rows.map((r, ri) => (
        <div key={r[0]}>
          {r.map((c, ci) => <T key={ci} x={xs[ci]} y={322 + ri * 50.5} w={203} size={ci ? 14.5 : 15} align="center" className={ci ? '' : 'font-medium'} style={{ color: t.ink }}>{c}</T>)}
          <Abs x={ri ? 106 : 309} y={355 + ri * 50} w={ri ? 1014 : 811} h={1} style={{ background: line }} />
        </div>
      ))}
      <T x={106} y={522} w={203} size={15} align="center" className="font-medium" style={{ color: t.ink }}>{table.share.label}</T>
      {table.share.values.map((v, i) => {
        const cx = (xs[i + 1] + xs[i + 2]) / 2
        return (
          <div key={i}>
            <T x={cx - 100} y={428} w={200} size={14} align="center" style={{ color: t.body }}>{table.share.note}</T>
            <Disc cx={cx} cy={555} r={66} bg={`conic-gradient(#f2f1ef 0 ${100 - v}%, #c4bfb9 0)`}>
              <Disc cx={66} cy={66} r={41} bg="#fff"><span className="font-semibold" style={{ fontSize: 16, color: t.ink }}>{v}%</span></Disc>
            </Disc>
          </div>
        )
      })}
      <Abs x={106} y={653} w={1014} h={1} style={{ background: '#6a625a' }} />
    </Folder>
  )
}

const mapIcons = [CloudDownload, Award, FilePlus2, Database]
export function WorldMap() {
  return (
    <Folder chapter={ch(19)}>
      <Heading kicker={worldMap.kicker} title={worldMap.title} y={157} size={47} />
      <Lines x={637} y={164} w={500} size={16} lh={24} align="right" lines={worldMap.intro} style={{ color: t.body }} />
      <Abs x={163} y={481} w={892} h={205}><ImagePlaceholder label="world map" className="h-full w-full rounded-t-[200px]" /></Abs>
      <svg className="absolute left-0 top-0" width={1280} height={720}>
        {worldMap.items.map((it) => <polyline key={it.k} points={it.path.map((p) => p.join(',')).join(' ')} fill="none" stroke="#8a847c" strokeWidth={1} />)}
        {worldMap.items.map((it) => { const e = it.path[3]; return <circle key={it.k} cx={e[0]} cy={e[1]} r={2} fill="#5a544c" /> })}
      </svg>
      {worldMap.items.map((it, i) => {
        const cx = it.path[0][0], Icon = mapIcons[i]
        return (
          <div key={it.k}>
            <Disc cx={cx} cy={298} r={48} bg={it.bg}><Icon size={38} strokeWidth={1} color={t.ink} /></Disc>
            <T x={cx - 80} y={360} w={160} size={15.5} align="center" style={{ color: t.ink }}>{it.k}</T>
            <T x={cx - 120} y={388} w={240} size={39} align="center" className="font-semibold" style={{ color: t.ink }}>{it.v}</T>
          </div>
        )
      })}
    </Folder>
  )
}

export function Bars() {
  return (
    <Folder chapter={ch(20)}>
      <CHead kicker={bars.kicker} title={bars.title} />
      <FolderCard x={131} y={257} w={420} h={286} tabW={90} tabH={13} bg="#ebe9e6" />
      <Abs x={675} y={257} w={417} h={286} style={{ background: '#f2f2f4' }} />
      <Abs x={1002} y={244} w={90} h={14} style={{ background: '#f2f2f4', clipPath: 'polygon(13px 0, 100% 0, 100% 100%, 0 100%)' }} />
      {bars.sides.map((sd, i) => (
        <div key={sd}>
          <T x={[158, 699][i]} y={275} w={[365, 366][i]} size={15} align="center" className={t.serif} style={{ color: t.ink }}>{sd}</T>
          <Abs x={[158, 699][i]} y={308} w={[365, 366][i]} h={1} style={{ background: '#d4d0ca' }} />
        </div>
      ))}
      {bars.labels.map((l, i) => {
        const cy = 349 + i * 51.4
        return (
          <div key={l}>
            <Abs x={bars.left[i]} y={cy - 14} w={551 - bars.left[i]} h={28} style={{ background: '#c4bfb9', borderRadius: '14px 0 0 14px' }} />
            <Abs x={675} y={cy - 14} w={bars.right[i] - 675} h={28} style={{ background: '#dde1e5', borderRadius: '0 14px 14px 0' }} />
            <T x={565} y={cy - 8} w={96} size={14.5} align="center" style={{ color: t.ink }}>{l}</T>
            {i < 3 && <Abs x={561} y={cy + 25} w={103} h={1} style={{ background: '#d4d0ca' }} />}
            <T x={165} y={cy - 7} size={13.5} className={t.serif} style={{ color: t.ink }}>{bars.value}</T>
            <T x={1026} y={cy - 7} size={13.5} className={t.serif} style={{ color: t.ink }}>{bars.value}</T>
          </div>
        )
      })}
      <Abs x={131} y={565} w={961} h={89} style={{ background: '#faf4e6' }} />
      <T x={131} y={588} w={961} size={15.5} align="center" className="font-medium" style={{ color: t.ink }}>{bars.note[0]}</T>
      <T x={131} y={614} w={961} size={15} align="center" style={{ color: t.body }}>{bars.note[1]}</T>
    </Folder>
  )
}

export function Pies() {
  const { small, big } = pies
  return (
    <Folder chapter={ch(21)}>
      <Heading kicker={pies.kicker} title={pies.title} y={216} size={47} />
      <Lines x={101} y={288} size={16} lh={25.5} lines={pies.intro} style={{ color: t.body }} />
      <Abs x={554} y={111} w={1} h={549} style={{ background: t.rule }} />
      <Disc cx={222} cy={524} r={119} bg="conic-gradient(#dcd8d2 0 40%, #fbeee6 0)" />
      <Disc cx={222} cy={524} r={36} bg="#fff" />
      {[151, 294].map((x, i) => (
        <div key={x}>
          <Abs x={x - 12} y={480}><PersonStanding size={26} color={i ? '#fff' : '#8a847c'} fill={i ? '#fff' : '#8a847c'} strokeWidth={1} /></Abs>
          <T x={x - 40} y={528} w={80} size={22} align="center" className={cn(t.serif, 'font-medium')} style={{ color: t.ink }}>{small.value}</T>
        </div>
      ))}
      <T x={356} y={519} size={16} className="font-medium" style={{ color: t.ink }}>{small.head}</T>
      <Lines x={356} y={554} size={14.5} lh={23.5} lines={small.body} style={{ color: t.body }} />
      <Disc cx={903} cy={408} r={220} bg="conic-gradient(#c8c3bc 0 70%, #e9ebe8 0 85%, #f8f1e2 0 95%, #f5ece8 0)" />
      <Disc cx={903} cy={408} r={44} bg="#fff" />
      <svg className="absolute left-0 top-0" width={1280} height={720}>
        {pies.keys.map(([, ly, ex, dy]) => <polyline key={ly} points={`662,${ly} ${ex},${ly} ${ex},${dy}`} fill="none" stroke="#c8c4be" strokeWidth={1} />)}
        {pies.keys.map(([, ly, ex, dy]) => <circle key={ly} cx={ex} cy={dy} r={2.5} fill="#b0aaa2" />)}
      </svg>
      {pies.keys.map(([k, ly, , , pct, px, py]) => (
        <div key={k}>
          <T x={555} y={ly - 7} w={100} size={14} align="right" style={{ color: t.ink }}>{k}</T>
          <T x={px - 30} y={py - 10} w={60} size={19} align="center" className={cn(t.serif, 'font-medium')} style={{ color: t.ink }}>{pct}</T>
        </div>
      ))}
      <T x={913} y={354} w={200} size={15} align="center" className="text-white">{big.head}</T>
      <T x={950} y={386} w={130} size={48} align="center" className={cn(t.serif, 'font-medium text-white')}>{big.value}</T>
      <T x={777} y={459} w={300} size={15} align="right" className="font-semibold text-white">{big.key}</T>
      <Lines x={777} y={485} w={300} size={13} lh={23} align="right" lines={big.body} style={{ color: '#f4f2ee' }} />
    </Folder>
  )
}

export function LineCharts() {
  const vy = (v: number) => 465 - v * 1.5375
  return (
    <Folder chapter={ch(22)}>
      <CHead kicker={lines.kicker} title={lines.title} />
      {lines.charts.map((c, ci) => {
        const ox = ci * 516, xs = [242, 364, 486].map((x) => x + ox)
        return (
          <div key={c.head}>
            <FolderCard x={111 + ox} y={249} w={489} h={337} tabW={86} tabH={12} bg="#efede8" />
            <T x={111 + ox} y={274} w={489} size={16} align="center" className="font-medium" style={{ color: t.ink }}>{c.head}</T>
            <Abs x={135 + ox} y={309} w={436} h={196} className="bg-white" />
            {lines.ticks.map((v) => (
              <div key={v}>
                <Abs x={181 + ox} y={vy(v)} w={366} h={1} style={{ background: v ? '#e6e2f0' : '#c8c4d0' }} />
                <T x={150 + ox} y={vy(v) - 6} w={24} size={11.5} align="right" style={{ color: t.body }}>{v}</T>
              </div>
            ))}
            <svg className="absolute left-0 top-0" width={1280} height={720}>
              {c.series.map((s, si) => {
                const pts = s.map((v, i) => `${xs[i]},${vy(v)}`).join(' ')
                return (
                  <g key={si}>
                    <polygon points={`${xs[0]},465 ${pts} ${xs[2]},465`} fill={si ? '#f1e1e1' : '#ece8ea'} opacity={0.8} />
                    <polyline points={pts} fill="none" stroke="#d7bcbc" strokeWidth={1.5} />
                    {s.map((v, i) => <circle key={i} cx={xs[i]} cy={vy(v)} r={2.5} fill="#c8b0b0" />)}
                  </g>
                )
              })}
            </svg>
            {c.series.map((s, si) => s.map((v, i) => <T key={`${si}${i}`} x={xs[i] - 15} y={vy(v) + (c.series.some((o) => o[i] > v) ? 3 : -18)} w={30} size={11} align="center" style={{ color: '#c8b8b8' }}>{v}</T>))}
            {lines.items.map((it, i) => <T key={it} x={xs[i] - 40} y={473} w={80} size={11.5} align="center" style={{ color: t.ink }}>{it}</T>)}
            <Lines x={111 + ox} y={520} w={489} size={15} lh={24} align="center" lines={c.body} style={{ color: t.body }} />
          </div>
        )
      })}
      <Abs x={113} y={602} w={1005} h={57} style={{ background: '#faf4e6' }} />
      <T x={113} y={623} w={1005} size={16} align="center" className="font-medium" style={{ color: t.ink }}>{lines.note}</T>
    </Folder>
  )
}

export function Heatmap() {
  const { zones, axes } = heatmap
  return (
    <Folder chapter={ch(23)}>
      <Abs x={112} y={156} w={468} h={466} className="overflow-hidden" style={{ background: zones[3].bg }}>
        {zones.slice(0, 3).reverse().map((z) => <Abs key={z.k} x={468 - z.r} y={-z.r} w={z.r * 2} h={z.r * 2} className="rounded-full" style={{ background: z.bg }} />)}
      </Abs>
      {zones.map((z, i) => <T key={z.k} x={z.at[0] - 60} y={z.at[1] - 8} w={120} size={15.5} align="center" style={{ color: i === 3 ? '#a8a29a' : t.ink }}>{z.k}</T>)}
      <Abs x={84} y={255} w={22} h={398} style={{ background: '#ebebe8', clipPath: 'polygon(50% 0, 100% 12px, 100% 100%, 0 100%, 0 12px)' }} />
      <Abs x={106} y={631} w={384} h={22} style={{ background: '#ebebe8', clipPath: 'polygon(0 0, calc(100% - 12px) 0, 100% 50%, calc(100% - 12px) 100%, 0 100%)' }} />
      <Abs x={87} y={156} className="whitespace-nowrap leading-none" style={{ writingMode: 'sideways-lr', fontSize: 14, color: t.ink }}>{axes.y}</Abs>
      <T x={497} y={635} size={14} style={{ color: t.ink }}>{axes.x}</T>
      <T x={90} y={635} size={14} style={{ color: t.ink }}>{axes.zero}</T>
      <Heading kicker={heatmap.kicker} title={heatmap.title} x={629} y={207} size={47} />
      <Lines x={629} y={283} size={15.5} lh={24.5} lines={heatmap.body} style={{ color: t.body }} />
      {zones.map((z, i) => {
        const cy = 430 + i * 64.7
        return (
          <div key={z.k}>
            <FolderCard x={629} y={cy - 21} w={124} h={44} tabW={34} tabH={6} bg={z.bg} />
            <T x={629} y={cy - 8} w={124} size={16} align="center" className="font-medium" style={{ color: t.ink }}>{z.k}</T>
            <T x={776} y={cy - 8} size={15.5} style={{ color: t.body }}>{heatmap.text}</T>
            <Abs x={776} y={cy + 24} w={333} h={1} style={{ background: t.rule }} />
          </div>
        )
      })}
    </Folder>
  )
}

export function Timetable() {
  const x0 = 177, cw = 79.25, line = '#e8e6e4'
  return (
    <Folder chapter={ch(24)}>
      <CHead kicker={timetable.kicker} title={timetable.title} />
      <Abs x={x0} y={239} w={951} h={41} style={{ background: '#514d4b' }} />
      {timetable.quarters.map((q, i) => <T key={q} x={x0 + i * 237.75} y={252} w={237.75} size={15} align="center" className="text-white">{q}</T>)}
      {[1, 2, 3].map((i) => <Abs key={i} x={x0 + i * 237.75} y={239} w={1} h={41} className="bg-white" />)}
      <Abs x={x0} y={281} w={951} h={41} style={{ background: '#f3f2f2' }} />
      {timetable.months.map((m, i) => <T key={m} x={x0 + i * cw} y={294} w={cw} size={14.5} align="center" style={{ color: t.ink }}>{m}</T>)}
      {timetable.months.map((_, i) => <Abs key={i} x={x0 + i * cw} y={281} w={1} h={368} style={{ background: line }} />)}
      {timetable.rows.map((r, i) => {
        const y = 322 + i * 65.4
        return (
          <div key={r.k}>
            <Abs x={97} y={y} w={80} h={65.4} style={{ background: r.bg }} />
            <T x={97} y={y + 25} w={80} size={14.5} align="center" style={{ color: t.ink }}>{r.k}</T>
            <Abs x={177} y={y + 65} w={951} h={1} style={{ background: line }} />
            <Abs x={r.bar[0]} y={y + 12} w={r.bar[1] - r.bar[0]} h={40} className="flex items-center justify-center whitespace-nowrap rounded-full" style={{ background: r.barBg, fontSize: 15, color: t.ink }}>{r.text}</Abs>
          </div>
        )
      })}
      <Abs x={97} y={649} w={1031} h={1} style={{ background: '#c8c4be' }} />
    </Folder>
  )
}

export function Org() {
  const line = '#c8c4be'
  return (
    <Folder chapter={ch(25)}>
      <Heading kicker={org.kicker} title={org.title} x={110} y={196} size={47} />
      <FolderCard x={428} y={157} w={370} h={161} tabW={80} tabH={8} bg="#efede8" />
      <Abs x={454} y={174} w={126} h={126} className="overflow-hidden rounded-full"><ImagePlaceholder label="portrait" className="h-full w-full" /></Abs>
      <T x={598} y={201} size={15} className={t.serif} style={{ color: t.ink }}>{org.lead.role}</T>
      <T x={598} y={229} size={20} className="font-medium tracking-[0.12em]" style={{ color: t.ink }}>{org.lead.name}</T>
      <T x={598} y={264} size={15.5} style={{ color: t.body }}>{org.desc}</T>
      <Abs x={609} y={318} w={1} h={26} style={{ background: line }} />
      <Abs x={230} y={344} w={765} h={1} style={{ background: line }} />
      {org.members.map((m, i) => {
        const x = [110, 366, 621, 875][i], cx = x + 120
        return (
          <div key={m.role}>
            <Abs x={cx} y={344} w={1} h={33} style={{ background: line }} />
            <FolderCard x={x} y={377} w={240} h={264} tabW={80} tabH={10} bg={m.bg} />
            <Abs x={cx - 63} y={405} w={126} h={126} className="overflow-hidden rounded-full"><ImagePlaceholder label="portrait" className="h-full w-full" /></Abs>
            <Abs x={x} y={554} w={240} className="flex items-baseline justify-center gap-[10px] whitespace-nowrap leading-none" style={{ color: t.ink }}>
              <span className={t.serif} style={{ fontSize: 15 }}>{m.role}</span>
              <span className="font-medium tracking-[0.12em]" style={{ fontSize: 19 }}>{m.name}</span>
            </Abs>
            <T x={x} y={590} w={240} size={15.5} align="center" style={{ color: t.body }}>{org.desc}</T>
          </div>
        )
      })}
    </Folder>
  )
}
