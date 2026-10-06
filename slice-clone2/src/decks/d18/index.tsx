import type { DeckDefinition } from '../../ui'
import { Abs, ImagePlaceholder } from '../../ui'
import { Blend, Handshake, PencilLine, Waypoints } from 'lucide-react'
import { Card, CoverPage, FolderPage, Kicker, Lines, T, Team, Title } from './components'
import * as d from './data'
import { t } from './theme'

const N = { color: t.navy } as const

function Cover() {
  return (
    <CoverPage>
      {d.cover.title.map((l, i) => <Title key={l} text={l} cy={[193, 296][i]} size={100} bg={t.pink} cx={628} />)}
      <Kicker word={d.cover.kicker} cy={420} size={33} cx={625} />
      <Team cy={578} cy2={633} team={d.team} />
    </CoverPage>
  )
}

const tocIcons = { pen: PencilLine, net: Waypoints, rings: Blend, hands: Handshake }
function Toc() {
  const c = d.toc
  return (
    <FolderPage color="brown" chapter={c.chapter}>
      <Title text={c.title} cy={96} size={69} bg={t.brown} />
      <Abs x={45} y={641} w={1121} h={2} style={{ background: t.navy }} />
      {c.items.map((it, i) => {
        const x = 71 + i * 276.3, cx = x + 120.5, Icon = tocIcons[it.icon]
        return (
          <div key={it.label}>
            <Card x={x} y={206} w={241} h={374} head={42} r={14} />
            <Abs x={cx - 20} y={287}><Icon size={40} color={t.navy} strokeWidth={1.6} /></Abs>
            <T x={x} w={241} cy={360} size={20} align="center" className="font-bold" style={N}>{it.label}</T>
            <Lines lines={it.lines} x={x} w={241} cy={407} pitch={25.3} size={15} align="center" />
            <Abs x={cx - 1} y={580} w={2} h={58} style={{ background: t.navy }} />
            <Abs x={cx - 7} y={622} w={14} h={14} style={{ borderRight: `2px solid ${t.navy}`, borderBottom: `2px solid ${t.navy}`, transform: 'translateY(-8px) rotate(45deg)', transformOrigin: 'center' }} />
            <Abs x={cx - 6} y={636} w={12} h={12} className="rounded-full" style={{ background: t.navy }} />
          </div>
        )
      })}
    </FolderPage>
  )
}

const knobColor = { navy: t.navy, pink: t.pink, white: '#fff' }
function Swot() {
  const c = d.swot
  return (
    <FolderPage color="brown" chapter={c.chapter}>
      <Title text={c.title} cy={97} size={74} bg={t.brown} />
      <Abs x={113} y={171} w={1019} h={488} className="bg-white" style={{ border: `2px solid ${t.navy}` }} />
      <Abs x={621} y={171} w={2} h={488} style={{ background: t.navy }} />
      <Abs x={113} y={414} w={1019} h={2} style={{ background: t.navy }} />
      {c.pieces.map((p) => <Abs key={p.ch} x={p.x} y={p.y} w={112} h={113} style={{ background: knobColor[p.k] }} />)}
      {c.knobs.map(([x, y, k], i) => <Abs key={i} x={x - 13} y={y - 13} w={26} h={26} className="rounded-full" style={{ background: knobColor[k] }} />)}
      <Abs x={602} y={394} w={40} h={40} className="rounded-full bg-white" />
      {c.pieces.map((p) => <T key={p.ch} x={p.x} w={112} cy={p.y + 56} size={30} align="center" className="font-bold" style={{ color: p.k === 'navy' ? '#fff' : t.navy }}>{p.ch}</T>)}
      {c.quads.map((q) => (
        <div key={q.label}>
          <T x={q.right ? 141 : 802} w={300} cy={q.cy} size={22} align={q.right ? 'right' : 'left'} className="font-extrabold" style={{ color: t.red, letterSpacing: '0.04em' }}>{q.label}</T>
          <Lines lines={q.lines} x={q.right ? 141 : 802} w={300} cy={q.cy + 33} pitch={22.6} size={15} align={q.right ? 'right' : 'left'} />
        </div>
      ))}
    </FolderPage>
  )
}

function Head({ title, kicker, bg, wide }: { title: string; kicker: string; bg: string; wide?: boolean }) {
  return (
    <>
      <Title text={title} cy={96} size={wide ? 72 : 72} bg={bg} />
      <Kicker word={kicker} cy={175} />
    </>
  )
}

/** Polyline area chart in slide coords. */
function AreaChart({ pts, base, color, fill, hollow, labelColor }: { pts: [number, number, number][]; base: number; color: string; fill: string; hollow?: boolean; labelColor: string }) {
  const p = pts.map(([x, y]) => `${x},${y}`).join(' ')
  return (
    <>
      <svg className="absolute left-0 top-0" width={1280} height={720}>
        <defs>
          <linearGradient id={`g${color.slice(1)}`} x1="0" y1="0" x2="0" y2="1"><stop offset="0" stopColor={fill} /><stop offset="1" stopColor={fill} stopOpacity={0} /></linearGradient>
        </defs>
        <polygon points={`${pts[0][0]},${base} ${p} ${pts[pts.length - 1][0]},${base}`} fill={`url(#g${color.slice(1)})`} />
        <polyline points={p} fill="none" stroke={color} strokeWidth={1.2} />
        {pts.map(([x, y]) => hollow ? <circle key={x} cx={x} cy={y} r={6} fill="#fff" stroke={color} strokeWidth={2} /> : <circle key={x} cx={x} cy={y} r={4.5} fill={color} />)}
      </svg>
      {pts.map(([x, y, v]) => <T key={x} x={x - 20} w={40} cy={y - 20} size={12.5} align="center" style={{ color: labelColor }}>{v}</T>)}
    </>
  )
}

function Strength() {
  const c = d.strength
  return (
    <FolderPage color="beige" chapter={c.chapter}>
      <Head title={c.title} kicker={c.kicker} bg={t.beige} />
      <Card x={100} y={219} w={1029} h={451} head={52} />
      {c.notes.map((n) => (
        <div key={n.label}>
          <T x={n.x} cy={299} size={21} className="font-extrabold" style={N}>{n.label}</T>
          <Lines lines={n.lines} x={n.tx} cy={296} pitch={25} size={16} />
        </div>
      ))}
      <AreaChart pts={c.points} base={600} color="#eea29b" fill="#fbdcd8" hollow labelColor="#eea29b" />
      <T x={785} w={300} cy={638} size={20} align="right" style={{ color: '#e8958d' }}>{c.caption}</T>
    </FolderPage>
  )
}

function Weakness() {
  const c = d.weakness
  const teal = '#a6cbc8'
  return (
    <FolderPage color="beige" chapter={c.chapter}>
      <Head title={c.title} kicker={c.kicker} bg={t.beige} />
      <Card x={100} y={219} w={1029} h={451} head={52} label={c.head} />
      <AreaChart pts={c.points} base={628} color={teal} fill="#e3efee" labelColor={teal} />
      <Abs x={159} y={627} w={553} h={2} style={{ background: t.navy }} />
      <Abs x={571} y={360} w={1.5} h={85} style={{ background: teal }} />
      <Abs x={512} y={326} w={119} h={34} className="flex items-center justify-center rounded-[4px] font-bold text-white" style={{ background: teal, fontSize: 13 }}>{c.tag}</Abs>
      {c.blocks.map((b) => (
        <div key={b.label}>
          <T x={754} cy={b.cy} size={21} className="font-extrabold" style={N}>{b.label}</T>
          <Lines lines={b.lines} x={754} cy={b.cy + 42} pitch={23.8} size={15.5} />
        </div>
      ))}
    </FolderPage>
  )
}

function Opportunity() {
  const c = d.opportunity
  const colors = { orange: t.orange, pink: t.pink, teal: t.teal, navy: t.navy }
  return (
    <FolderPage color="beige" chapter={c.chapter}>
      <Head title={c.title} kicker={c.kicker} bg={t.beige} wide />
      <Card x={100} y={227} w={498} h={424} head={48} label={c.heads[0]} />
      <Card x={632} y={227} w={498} h={424} head={48} label={c.heads[1]} />
      {[314, 410, 505].map((y) => <Abs key={y} x={141} y={y} w={419} h={1} style={{ background: '#dcdcdc' }} />)}
      <Lines lines={c.note} x={141} cy={337} pitch={20} size={12.5} style={{ color: '#666' }} />
      {c.bars.map((b, i) => {
        const x = 158 + i * 100.7
        return (
          <div key={b.label}>
            <Abs x={x} y={b.top} w={84} h={607 - b.top} style={{ background: colors[b.c], borderRadius: '42px 42px 0 0' }} />
            <T x={x} w={84} cy={b.top - 14} size={12.5} align="center" className="font-bold" style={{ color: colors[b.c] }}>{b.v}</T>
            <T x={x - 10} w={104} cy={622} size={14.5} align="center" className={i === 3 ? 'font-extrabold' : ''} style={i === 3 ? N : { color: '#666' }}>{b.label}</T>
          </div>
        )
      })}
      <Abs x={132} y={606} w={437} h={2.5} style={{ background: t.navy }} />
      <T x={632} w={498} cy={329} size={21} align="center" className="font-extrabold" style={N}>{c.heading}</T>
      <Lines lines={c.lines} x={632} w={498} cy={396} pitch={28.2} size={17} align="center" />
    </FolderPage>
  )
}

function Threat() {
  const c = d.threat
  const cols = [162, 248, 413, 580, 746], ys = [317, 381, 446, 510, 574]
  const dc = { navy: t.navy, pink: '#f2a7a0', teal: t.teal }
  let acc = 0
  const stops = c.donut.map((s) => `${dc[s.c]} ${acc}deg ${(acc += s.deg)}deg`).join(', ')
  return (
    <FolderPage color="beige" chapter={c.chapter}>
      <Head title={c.title} kicker={c.kicker} bg={t.beige} />
      <Abs x={104} y={220} w={1022} h={451} className="overflow-hidden rounded-[12px] bg-white" style={{ border: `2px solid ${t.navy}` }}>
        <div className="absolute bottom-0 left-0 right-0 flex items-center justify-center whitespace-pre text-white" style={{ height: 50, background: t.navy, fontSize: 22 }}>
          {c.banner[0]}<b className="font-extrabold">{c.banner[1]}</b>{c.banner[2]}
        </div>
      </Abs>
      <Abs x={162} y={273} w={584} h={44} style={{ background: t.teal }} />
      {c.rows.map((_, r) => (
        <div key={r}>
          <Abs x={162} y={ys[r]} w={86} h={ys[r + 1] - ys[r]} style={{ background: t.beige }} />
          {r % 2 === 1 && <Abs x={248} y={ys[r]} w={498} h={ys[r + 1] - ys[r]} style={{ background: t.cream }} />}
        </div>
      ))}
      {cols.slice(1, -1).map((x) => <Abs key={x} x={x} y={273} w={1.5} h={301} style={{ background: t.teal }} />)}
      <Abs x={162} y={316} w={584} h={2} style={{ background: t.navy }} />
      <Abs x={162} y={573} w={584} h={2} style={{ background: t.navy }} />
      {c.cols.map((h, i) => <T key={i} x={cols[i]} w={cols[i + 1] - cols[i]} cy={295} size={14.5} align="center" style={N}>{h}</T>)}
      {c.rows.map((row, r) => row.map((cell, i) => (
        <T key={`${r}${i}`} x={cols[i]} w={cols[i + 1] - cols[i]} cy={(ys[r] + ys[r + 1]) / 2} size={14.5} align="center" style={i ? undefined : N}>{cell}</T>
      )))}
      <Abs x={782} y={286} w={284} h={284} className="rounded-full" style={{ background: `conic-gradient(${stops})`, mask: 'radial-gradient(circle, transparent 123px, #000 124px)', WebkitMask: 'radial-gradient(circle, transparent 123px, #000 124px)' }} />
      {c.donut.map((s, i) => (
        <T key={s.label} x={852} cy={[389, 425, 462][i]} size={17.5} className="font-extrabold" style={{ color: dc[s.c] }}>
          <span className="mr-[8px] inline-block h-[13px] w-[13px]" style={{ background: dc[s.c] }} />{s.label}
        </T>
      ))}
    </FolderPage>
  )
}

function Label() {
  return <Abs x={437} y={157} w={362} h={46} className="flex items-center justify-center bg-white font-black leading-none" style={{ zIndex: 2, color: t.red, fontSize: 32 }}>{d.fourP.label}</Abs>
}

function FourP1() {
  const c = d.fourP
  return (
    <FolderPage color="teal" chapter={c.chapter}>
      <Title text={c.title} cy={96} size={70} bg={t.teal} light />
      <Abs x={162} y={179} w={955} h={478}><ImagePlaceholder label="coffee pour-over photo" className="h-full w-full" /></Abs>
      <Abs x={642} y={179} w={475} h={478} style={{ background: '#1b2a39', opacity: 0.93 }} />
      <Label />
      {c.blocks.map((b, i) => (
        <div key={i}>
          <T x={700} w={350} cy={b.cy} size={21} align="right" className="font-extrabold" style={{ color: '#dde9e8' }}>{b.head}</T>
          <Lines lines={b.lines} x={650} w={400} cy={b.cy + 47} pitch={26.5} size={16.5} align="right" className="text-white" />
        </div>
      ))}
    </FolderPage>
  )
}

function FourP2() {
  const c = d.fourP
  return (
    <FolderPage color="teal" chapter={c.chapter}>
      <Title text={c.title} cy={96} size={70} bg={t.teal} light />
      {[122, 648].map((x) => (
        <div key={x}>
          <Abs x={x} y={176} w={509} h={395}><ImagePlaceholder label="cafe photo" className="h-full w-full" /></Abs>
          <Lines lines={c.caption} x={x - 20} w={549} cy={613} pitch={21} size={15} align="center" />
        </div>
      ))}
      <Label />
    </FolderPage>
  )
}

function References() {
  const c = d.references
  const col = [0, 22, 150, 218, 530]
  return (
    <FolderPage color="orange" chapter={c.chapter}>
      <Head title={c.title} kicker={c.kicker} bg={t.orange} />
      {c.tables.map((tb, ti) => {
        const x0 = [98, 652][ti]
        return (
          <div key={tb.heading}>
            <T x={x0} w={530} cy={247} size={22} align="center" className="font-extrabold" style={N}>{tb.heading}</T>
            <Abs x={x0} y={279} w={530} h={36} style={{ background: t.navy }} />
            {[1, 2, 3].map((k) => <Abs key={k} x={x0 + col[k]} y={279} w={1} h={36} style={{ background: 'rgba(255,255,255,0.5)' }} />)}
            {c.head.map((h, k) => <T key={h} x={x0 + col[k + 1]} w={col[k + 2] - col[k + 1]} cy={297} size={12.5} align="center" className="font-bold text-white">{h}</T>)}
            {tb.rows.map((r, ri) => {
              const y = 315 + ri * 46.3, cy = y + 23
              return (
                <div key={ri}>
                  {ri < 6 && <Abs x={x0} y={y + 45.3} w={530} h={2} className="bg-white" />}
                  <T x={x0 + 4} w={14} cy={cy} size={12.5} align="center" style={{ color: t.red }}>{ri + 1}</T>
                  <T x={x0 + col[1]} w={128} cy={cy} size={12.5} align="center" className="font-bold" style={N}>{r.item}</T>
                  <Lines lines={r.kind.split('\n')} x={x0 + col[2]} w={68} cy={cy - (r.kind.includes('\n') ? 7 : 0)} pitch={14} size={12.5} align="center" />
                  <Lines lines={r.ref.split('\n')} x={x0 + col[3]} w={312} cy={cy - (r.ref.includes('\n') ? 7 : 0)} pitch={14} size={12.5} align="center" />
                </div>
              )
            })}
            <Abs x={x0} y={638} w={530} h={2.5} style={{ background: t.navy }} />
          </div>
        )
      })}
    </FolderPage>
  )
}

function Closing() {
  return (
    <CoverPage>
      <Title text={d.closing.title} cy={329} size={100} bg={t.pink} cx={640} />
      <Kicker word={d.closing.kicker} cy={420} size={34} cx={625} />
      <Team cy={577} cy2={633} size={21} team={d.team} />
    </CoverPage>
  )
}

const deck: DeckDefinition = { id: '18', title: '폴더링프레젠테이션', slides: [Cover, Toc, Swot, Strength, Weakness, Opportunity, Threat, FourP1, FourP2, References, Closing] }
export default deck
