import type { DeckDefinition } from '../../ui'
import { Abs, ImagePlaceholder, Slide, cn } from '../../ui'
import { ChevronRight, FilePenLine, Laptop, Lightbulb, UsersRound } from 'lucide-react'
import { Display, HLine, Hatched, Header, Lines, Marker, Page, Photo, T } from './components'
import * as d from './data'
import { t } from './theme'

const W = { color: '#fff' } as const

function Cover() {
  const c = d.cover
  return (
    <Slide background="#fff" className={t.kr}>
      <Abs x={36} y={33} w={1208} h={655} className="overflow-hidden rounded-[30px]"><ImagePlaceholder label="taupe light-streak background" tone="#aaa293" className="h-full w-full" /></Abs>
      <HLine y={247} x={36} w={1208} c="#fff" h={2} />
      <HLine y={469} x={36} w={1208} c="#fff" h={2} />
      <T x={106} cy={69} size={17} className={cn(t.en, 'font-bold')} style={W}>{c.kicker}</T>
      <T x={104} cy={326} size={106} className={cn(t.en, 'font-bold tracking-[-0.03em]')} style={W}>{c.title[0]}</T>
      <T x={104} cy={426} size={106} className={cn(t.en, 'font-light tracking-[-0.03em]')} style={W}>{c.title[1]}</T>
      {(['v', 'h', 'd'] as const).map((k, i) => <Marker key={k} cx={1152} cy={[149, 359, 582][i]} kind={k} color="#fff" />)}
      <Photo x={106} y={585} w={186} h={36} label="MIRI.DIH logo" tone="#c9c2b5" />
      <T x={106} cy={639} size={14} style={W}>{c.info}</T>
    </Slide>
  )
}

function Toc() {
  return (
    <Page>
      {[50, 255, 460, 664].map((y) => <HLine key={y} y={y} />)}
      {d.toc.map((r, i) => {
        const cy = [144, 352, 555][i]
        return (
          <div key={r.desc}>
            <Marker cx={189} cy={cy} kind={r.kind} />
            <T x={258} cy={cy} size={19} style={{ color: t.grey }}>{r.items.join('    |    ')}</T>
            <T x={640} w={566} cy={cy} size={16} align="center" style={{ color: t.grey }}>{r.desc}</T>
          </div>
        )
      })}
    </Page>
  )
}

function Vision() {
  const c = d.vision
  const v = c.venn
  const disc = (cx: number, cy: number, r: number, bg: string) => <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className="rounded-full" style={{ background: bg }} />
  return (
    <Page>
      <Header kind="v" label={c.label} page={c.page} />
      <Lines lines={c.head} x={67} cy={146} pitch={45} size={38} style={{ color: t.head, letterSpacing: 0 }} />
      <Lines lines={c.body} x={67} cy={300} pitch={26.5} size={16.5} />
      <Hatched cx={940} cy={233} r={160} ring={174} color="#bdb9b0" />
      {disc(939, 192, 122, 'rgba(232,120,96,0.62)')}
      {disc(901, 266, 122, 'rgba(232,120,96,0.62)')}
      {disc(977, 266, 122, 'rgba(232,120,96,0.62)')}
      {disc(939, 248, 85, 'rgba(214,80,52,0.65)')}
      <T x={892} w={100} cy={108} size={16} align="center" style={W}>{v.top}</T>
      <T x={777} w={100} cy={294} size={16} align="center" style={W}>{v.left}</T>
      <T x={997} w={100} cy={292} size={16} align="center" style={W}>{v.right}</T>
      <Lines lines={v.center} x={894} w={100} cy={234} pitch={17} size={16} align="center" style={W} />
      <Abs x={0} y={436} w={1280} h={200} style={{ background: t.taupe }} />
      {[433, 851].map((x) => <Abs key={x} x={x} y={459} w={1.5} h={152} className="bg-white" />)}
      {c.cols.map((col, i) => (
        <div key={col.title}>
          <T x={[69, 489, 909][i]} w={310} cy={486} size={17} align="center" className={cn(t.en, 'font-bold')} style={W}>{col.title}</T>
          <Lines lines={col.lines} x={[69, 489, 909][i]} cy={520} pitch={23} size={16} />
        </div>
      ))}
      <HLine y={696} />
    </Page>
  )
}

function Greeting() {
  const c = d.greeting
  return (
    <Page>
      <Photo x={785} y={0} w={495} h={720} label="smiling man portrait" />
      <Header kind="v" label={c.label} page={c.page} pageColor="#fff" />
      <Lines lines={c.head} x={67} cy={149} pitch={45} size={38} style={{ color: t.head, letterSpacing: 0 }} />
      <Abs x={0} y={288} w={785} h={219} style={{ background: t.taupe }} />
      <Lines lines={c.p1} x={67} cy={320} pitch={26.6} size={16} />
      <Lines lines={c.p2} x={67} cy={452} pitch={27} size={16} />
      <Lines lines={c.p3} x={67} cy={532} pitch={27} size={16} />
      <T x={423} w={200} cy={611} size={16} align="right" className="font-bold" style={{ color: t.ink }}>{c.sign}</T>
      <Photo x={626} y={596} w={105} h={66} label="signature" />
    </Page>
  )
}

function Band({ y, h, title, side, sideY }: { y: number; h: number; title: string[]; side: string[]; sideY: number }) {
  return (
    <>
      <HLine y={y - 7} />
      <Abs x={0} y={y} w={1280} h={h} style={{ background: t.taupe }} />
      <HLine y={y + h + 8} />
      <Display lines={title} cy={y + 54} pitch={61} />
      <Lines lines={side} x={736} cy={sideY} pitch={26} size={16} />
    </>
  )
}

function Perf() {
  const c = d.perf
  const y = (v: number) => 656 - v * 0.119
  return (
    <Page>
      <HLine y={21} />
      <Header kind="v" label={c.label} page={c.page} cy={75} />
      <Band y={116} h={198} title={c.title} side={c.side} sideY={152} />
      <Lines lines={c.p1} x={65} w={480} cy={367} pitch={26.5} size={16} justify />
      <Lines lines={c.p2} x={65} w={480} cy={499} pitch={26.5} size={16} justify />
      {c.charts.map((ch) => (
        <div key={ch.title}>
          <T x={ch.axis - 30} cy={368} size={13} className="font-bold" style={{ color: t.ink }}>{ch.title} <span className="font-normal" style={{ fontSize: 11, color: '#777' }}>{c.unit}</span></T>
          {[2000, 1500, 1000, 500, 0].map((v) => (
            <div key={v}>
              <T x={ch.axis - 50} w={50} cy={y(v)} size={11} align="right" className={t.en} style={{ color: '#555' }}>{v.toLocaleString()}</T>
              <Abs x={ch.axis + 5} y={y(v)} w={128} h={0} style={{ borderTop: v ? '1.3px dashed #444' : '1.5px solid #333' }} />
            </div>
          ))}
          {ch.values.map((v, i) => {
            const x = ch.axis + 16 + i * 28, last = i === 3
            return (
              <div key={i}>
                <Abs x={x} y={y(v)} w={22} h={656 - y(v)} style={{ background: last ? t.red : t.bar }} />
                <T x={x - 15} w={52} cy={y(v) - 10} size={10.5} align="center" className={t.en} style={{ color: last ? t.red : '#aaa' }}>{v.toLocaleString()}</T>
              </div>
            )
          })}
        </div>
      ))}
      <HLine y={696} />
    </Page>
  )
}

function Market() {
  const c = d.market, f1 = c.fig1, f2 = c.fig2
  let acc = 0
  const stops = f2.segs.map(([deg, col]) => `${col} ${acc}deg ${(acc += deg)}deg`).join(', ')
  const ringMask = 'radial-gradient(circle, transparent 90px, #000 91px)'
  return (
    <Page>
      <Header kind="h" label={c.label} page={c.page} cy={55} labelX={131} />
      <Band y={102} h={199} title={c.title} side={c.side} sideY={139} />
      <T x={72} cy={343} size={14}>{f1.label}</T>
      <Abs x={150} y={423} w={336} h={166} style={{ background: 'linear-gradient(90deg, #e98a73, rgba(240,190,175,0.15))', clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0 100%)', borderRadius: '0 0 0 0' }} />
      <Hatched cx={486} cy={506} r={100} ring={112} fill="#b8b3a2" />
      <Abs x={67} y={423} w={166} h={166} className="rounded-full" style={{ background: t.red }} />
      <T x={67} w={166} cy={469} size={19} align="center" className={t.en} style={{ color: '#f5d5cc' }}>{f1.from[0]}</T>
      <HLine x={100} w={100} y={490} c="#f5d5cc" h={1} />
      <T x={67} w={166} cy={528} size={46} align="center" className={cn(t.en, 'font-light')} style={W}>{f1.from[1]}</T>
      <T x={240} w={120} cy={508} size={21} align="center" className="font-bold" style={{ color: t.ink }}>{f1.growth}</T>
      <T x={386} w={200} cy={456} size={25} align="center" className={cn(t.en, 'font-light')} style={W}>{f1.to[0]}</T>
      <HLine x={416} w={140} y={481} c="#fff" h={1} />
      <T x={386} w={200} cy={531} size={58} align="center" className={cn(t.en, 'font-light')} style={W}>{f1.to[1]}</T>
      <T x={656} cy={343} size={14}>{f2.label}</T>
      <Hatched cx={961} cy={495} r={118} ring={131} color="#c6c2b8" />
      <Abs x={846} y={380} w={230} h={230} className="rounded-full" style={{ background: `conic-gradient(${stops})`, mask: ringMask, WebkitMask: ringMask }} />
      <Lines lines={f2.center} x={861} w={200} cy={483} pitch={26} size={20} align="center" className={t.en} style={{ color: '#555' }} />
      <svg className="absolute left-0 top-0" width={1280} height={720}>
        {f2.callouts.map((co) => <polyline key={co.v} points={co.path.map((p) => p.join(',')).join(' ')} fill="none" stroke="#999" strokeWidth={1} />)}
        {f2.callouts.map((co) => { const [x, y] = co.path[co.path.length - 1]; return <circle key={co.v} cx={x} cy={y} r={3.5} fill="#999" /> })}
      </svg>
      {f2.callouts.map((co) => (
        <div key={co.v}>
          <T x={co.vx ?? co.x} w={150} cy={co.cy} size={co.red ? 38 : 28} className={cn(t.en, 'font-light')} style={{ color: co.red ? t.red : '#b5b09e', marginLeft: co.red ? 8 : 0 }}>{co.v}</T>
          <Lines lines={co.desc} x={co.x} cy={co.cy + (co.red ? 35 : 32)} pitch={17} size={13.5} />
        </div>
      ))}
      <HLine y={696} />
    </Page>
  )
}

const stepIcons = { bulb: Lightbulb, laptop: Laptop, pen: FilePenLine, people: UsersRound }
function Roadmap() {
  const c = d.roadmap
  const xs = [220, 498, 770, 1044], tx = [113, 382, 664, 957]
  return (
    <Page>
      <Header kind="h" label={c.label} page={c.page} cy={55} labelX={131} />
      {c.steps.map((s, i) => {
        const Icon = stepIcons[s.icon]
        return (
          <div key={s.en}>
            <Hatched cx={xs[i]} cy={220} r={92} ring={101} color="#bdb9b0" />
            <Abs x={xs[i] - 36} y={162}><Icon size={72} color={t.red} strokeWidth={1.6} /></Abs>
            <T x={xs[i] - 90} w={180} cy={257} size={13} align="center" className={cn(t.en, 'font-extrabold')} style={{ color: t.red }}>{s.en}</T>
            <T x={xs[i] - 90} w={180} cy={275} size={14} align="center" style={{ color: t.red }}>{s.kr}</T>
            {i < 3 && <Abs x={[336, 612, 884][i]} y={198}><ChevronRight size={46} color="#b5b09e" strokeWidth={2.2} /></Abs>}
            <T x={tx[i]} cy={345} size={16.5} style={{ color: '#aaa' }}>{s.title}</T>
            <Lines lines={s.lines} x={tx[i] + 2} w={226} cy={375} pitch={22} size={15.5} justify />
          </div>
        )
      })}
      <Abs x={0} y={472} w={1280} h={199} style={{ background: t.taupe }} />
      <Lines lines={c.head} x={67} cy={520} pitch={45} size={38} style={{ ...W, letterSpacing: 0 }} />
      <Lines lines={c.side} x={687} cy={511} pitch={27} size={16} />
      <HLine y={696} />
    </Page>
  )
}

function Finance() {
  const c = d.finance
  const y = (v: number) => 653 - v * 0.0565
  const colX = [751, 833, 917, 1002, 1086, 1169]
  const rowY = [215, 260, 302, 345, 389, 438, 486, 534, 584, 632]
  return (
    <Page>
      <Abs x={640} y={0} w={640} h={720} style={{ background: t.paper }} />
      <Header kind="d" label={c.label} page={c.page} />
      <Display lines={c.title} cy={184} color={t.head} />
      {c.charts.map((ch) => {
        const pts = ch.values.map((v, i) => `${ch.xs[i]},${y(v)}`).join(' ')
        return (
          <div key={ch.title}>
            <T x={ch.x} cy={348} size={13} className="font-bold" style={{ color: t.ink }}>{ch.title}<span className="font-normal" style={{ fontSize: 11, color: '#666' }}>{ch.unit}</span></T>
            {[4000, 3000, 2000, 1000, 0].map((v) => <T key={v} x={ch.axis - 50} w={50} cy={y(v)} size={11} align="right" className={t.en} style={{ color: '#555' }}>{v.toLocaleString()}</T>)}
            {[404, 491, 576].map((yy) => <Abs key={yy} x={ch.axis - 6} y={yy} w={182} h={0} style={{ borderTop: '1.3px dashed #555' }} />)}
            <svg className="absolute left-0 top-0" width={1280} height={720}>
              <polygon points={`${ch.xs[0]},663 ${pts} ${ch.xs[3]},663`} fill={ch.fill} />
              <polyline points={pts} fill="none" stroke={ch.line} strokeWidth={1.2} />
              {ch.values.map((v, i) => <circle key={i} cx={ch.xs[i]} cy={y(v)} r={3.5} fill={ch.line} />)}
              <line x1={ch.axis - 10} y1={663} x2={ch.axis + 176} y2={663} stroke="#333" strokeWidth={1.2} />
            </svg>
            {ch.values.map((v, i) => <T key={i} x={ch.xs[i] - 30} w={60} cy={y(v) - 13} size={11} align="center" className={t.en} style={{ color: ch.label }}>{v.toLocaleString()}</T>)}
            {c.years.map((yr, i) => <T key={yr} x={ch.xs[i] - 25} w={50} cy={663} size={11} align="center" className={t.en} style={{ color: '#555' }}>{yr}</T>)}
          </div>
        )
      })}
      <T x={900} w={315} cy={143} size={13} align="right" className="font-bold" style={{ color: t.ink }}>{c.tableTitle[0]}<span className="font-normal" style={{ fontSize: 11 }}>{c.tableTitle[1]}</span></T>
      <HLine x={709} w={501} y={162} c="#888" h={2} />
      <HLine x={709} w={501} y={189} c="#888" h={2} />
      {c.head.map((h, i) => <T key={h} x={colX[i] - 45} w={90} cy={176} size={16} align="center" className={i ? t.en : ''} style={{ color: t.ink }}>{h}</T>)}
      {c.rows.map((r, ri) => (
        <div key={r[0]}>
          {ri < 9 && <HLine x={709} w={501} y={(rowY[ri] + rowY[ri + 1]) / 2} c="#ddd" h={1} />}
          {r.map((cell, ci) => <T key={ci} x={colX[ci] - 45} w={90} cy={rowY[ri]} size={ci ? 15.5 : 15} align="center" className={ci ? t.en : 'font-bold'} style={{ color: ci ? '#666' : t.ink }}>{cell}</T>)}
        </div>
      ))}
      {c.circled.map(([r, ci]) => <Abs key={`${r}${ci}`} x={colX[ci] - 41} y={rowY[r] - 19} w={82} h={38} className="rounded-[50%]" style={{ border: `1.5px solid ${t.red}` }} />)}
      <HLine x={709} w={501} y={656} c="#999" h={3} />
    </Page>
  )
}

function Org() {
  const c = d.org
  const rows = [294, 376, 461, 545, 629]
  return (
    <Page bg={t.paper}>
      <Header kind="d" label={c.label} page={c.page} />
      <Display lines={c.title} cy={168} pitch={62} color={t.head} />
      {c.people.map(([n, r], i) => {
        const cx = [165, 337][i]
        return (
          <Hatched key={n} cx={cx} cy={413} r={64} ring={75} color={t.red}>
            <T x={cx - 70} w={140} cy={398} size={24} align="center" style={{ color: '#888' }}>{n}</T>
            <T x={cx - 70} w={140} cy={428} size={18} align="center" style={{ color: t.red }}>{r}</T>
          </Hatched>
        )
      })}
      <Lines lines={c.body} x={98} w={310} cy={518} pitch={26.3} size={16} justify />
      <Abs x={468} y={294} w={87} h={335} style={{ borderLeft: '1.2px solid #c44', borderTop: '1.2px solid #c44', borderBottom: '1.2px solid #c44' }} />
      {c.depts.map(([dept, ...teams], i) => (
        <div key={dept}>
          <Abs x={555} y={rows[i] - 25} w={153} h={50} className="flex items-center justify-center rounded-full font-bold text-white" style={{ background: t.bar, fontSize: 17 }}>{dept}</Abs>
          {teams.map((tm, j) => (
            <Abs key={tm} x={722 + j * 162.5} y={rows[i] - 25} w={155} h={50} className="flex items-center justify-center rounded-full" style={{ border: '1.5px solid #f0c0b2', color: '#888', fontSize: 17 }}>{tm}</Abs>
          ))}
        </div>
      ))}
    </Page>
  )
}

function History() {
  const c = d.history
  return (
    <Page>
      <Header kind="d" label={c.label} page={c.page} cy={68} color={t.bar} />
      <T x={70} cy={170} size={67} className="font-inter font-extrabold" style={{ color: t.head }}>{c.title}</T>
      {c.photos.map((p) => (
        <div key={p.cx}>
          {p.label && <Hatched cx={p.cx} cy={326} r={61} ring={75} color="#cfcac0" />}
          <Abs x={p.cx - 61} y={265} w={122} h={122} className="overflow-hidden rounded-full"><ImagePlaceholder label="history photo" tone="#9b9184" className="h-full w-full" /></Abs>
          {p.label && <Lines lines={p.label} x={p.cx - 70} w={140} cy={314} pitch={24} size={18} align="center" className="font-bold" style={W} />}
        </div>
      ))}
      <HLine y={428} c={t.red} h={1.2} />
      {c.cols.map((col) => (
        <div key={col.year}>
          <Abs x={col.dot - 8} y={420} w={16} h={16} className="rounded-full bg-white" style={{ border: `3px solid ${t.red}` }} />
          <T x={col.x} cy={468} size={17} className="font-bold" style={{ color: t.red }}>{col.title}</T>
          <T x={col.x} cy={503} size={38} className={cn(t.en, 'items-baseline font-light')} style={{ color: t.red }}>{col.year}<span style={{ fontSize: 22, color: '#999' }}>{col.from}</span></T>
          <Lines lines={col.lines} x={col.x} cy={542} pitch={25} size={14.5} style={{ color: '#a9a49a' }} />
        </div>
      ))}
    </Page>
  )
}

function Closing() {
  return (
    <Slide background="#fff">
      <Abs x={30} y={29} w={1220} h={661} className="overflow-hidden rounded-[34px]">
        {[0, 221, 442].map((y, i) => (
          <Abs key={y} x={0} y={y} w={1220} h={219}><ImagePlaceholder label="city photo band" tone={['#6f6257', '#55524f', '#46433b'][i]} className="h-full w-full" /></Abs>
        ))}
      </Abs>
      {d.closing.map((l, i) => <T key={l} x={0} w={1280} cy={[138, 359, 580][i]} size={18} align="center" className="font-semibold" style={{ ...W, fontFamily: "'Open Sans', 'Inter Variable', sans-serif" }}>{l}</T>)}
    </Slide>
  )
}

const deck: DeckDefinition = { id: '20', title: '브라운 레드 느낌의 비즈니스 제안서', slides: [Cover, Toc, Vision, Greeting, Perf, Market, Roadmap, Finance, Org, History, Closing] }
export default deck
