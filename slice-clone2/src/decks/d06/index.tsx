import type { DeckDefinition } from '../../ui'
import { Abs } from '../../ui'
import { Box, Lines } from '../../ui'
import { Body, ChartText, Company, Heading, Photo, PrintSlide, SubHead } from './components'
import { about, cover, line, mission, pie, product, qna, quote, team, timeline } from './data'
import { t } from './theme'

function Cover() {
  return (
    <PrintSlide brandColor="#111">
      <Heading x={112} cy={260} lines={cover.title} size={56} lh={52} />
      <Lines x={112} cy={375} size={23} color={t.title} lines={[cover.sub]} />
      <Lines x={t.right} cy={688} align="right" size={12.5} className="font-bold" color={t.ink} lines={[cover.date]} />
    </PrintSlide>
  )
}

function About() {
  return (
    <PrintSlide page={about.page} brandColor="#ccc" pageColor="#fff">
      <Photo x={642} y={0} w={625} h={720} tone="#6b7280" />
      <Abs x={650} y={556} h={158} className="whitespace-nowrap" style={{ writingMode: 'vertical-rl', fontSize: 8, color: '#eee' }}>{about.note}</Abs>
      <Heading cy={111} lines={[about.title]} />
      <SubHead cy={219} text={about.sub} />
      <Body cy={259} lines={about.body} />
    </PrintSlide>
  )
}

function Mission() {
  return (
    <PrintSlide page={mission.page} pageColor="#fff">
      <Heading cy={111} lines={[mission.title]} />
      <SubHead cy={218} text={mission.sub} />
      {mission.cols.map((c, i) => <Body key={i} x={60 + i * 418} cy={259} lines={c} />)}
      <Photo x={0} y={455} w={1280} h={265} tone="#6b7280" />
    </PrintSlide>
  )
}

function Timeline() {
  return (
    <PrintSlide page={timeline.page}>
      <Heading cy={111} lines={[timeline.title]} />
      <Body x={772} cy={89} lines={timeline.intro} />
      <Box x={106} y={634} w={1071} h={3} bg="#111" />
      {timeline.years.map((y) => (
        <div key={y.year}>
          <Box x={y.x} y={292} w={2} h={343} bg="#111" />
          <Lines x={y.x} cy={654} align="center" w={80} size={14} className="font-bold" color={t.ink} lines={[y.year]} />
          {y.entries.map((e, i) => (
            <div key={i}>
              <Lines x={y.x + 25} cy={e.cy} size={12.5} className="font-bold" color={t.ink} lines={[e.title]} />
              <Lines x={y.x + 25} cy={e.cy + 22} lh={14.7} size={10} color={t.body} lines={e.desc} />
            </div>
          ))}
        </div>
      ))}
    </PrintSlide>
  )
}

function Product() {
  return (
    <PrintSlide page={product.page}>
      <Photo x={109} y={34} w={531} h={686} />
      <Heading x={747} cy={142} lines={[product.title]} />
      <Body x={747} cy={209} lines={product.intro} />
      {product.items.map((it, i) => {
        const y = 371 + i * 158
        return (
          <div key={i}>
            <Photo x={746} y={y} w={121} h={114} />
            <SubHead x={883} cy={y + 12} text={it.title} />
            <Body x={883} cy={y + 53} lh={21.5} lines={it.desc} />
          </div>
        )
      })}
    </PrintSlide>
  )
}

function Pie() {
  const cx = 906, cy = 383, r = 196
  /** one wedge; a 0.5° gap on each side leaves a white seam between slices */
  const grad = (from: number, to: number, c: string) => `conic-gradient(transparent 0deg ${from + 0.5}deg, ${c} ${from + 0.5}deg ${to - 0.5}deg, transparent ${to - 0.5}deg)`
  return (
    <PrintSlide page={pie.page}>
      <ChartText data={pie} />
      <Lines x={915} cy={124} align="center" w={400} size={19} className="font-medium" color={t.ink} lines={[pie.chartTitle]} />
      {pie.slices.map((s, i) => {
        const dx = i === 0 ? 15 : 0, dy = i === 0 ? -2 : 0
        return <Abs key={i} x={cx - r + dx} y={cy - r + dy} w={r * 2} h={r * 2} className="rounded-full" style={{ background: grad(s.from, s.to, s.c) }} />
      })}
      {pie.bigLabels.map((l) => (
        <div key={l.cy}>
          <Lines x={l.x} cy={l.cy} align="center" w={160} size={25} color="#fff" lines={[l.v]} />
          <Lines x={l.x} cy={l.cy + 31} lh={12.5} align="center" w={160} size={9.5} color="#eee" lines={l.d} />
        </div>
      ))}
      {pie.smallLabels.map((l) => (
        <div key={l.cy}>
          <Lines x={l.x} cy={l.cy} align="center" w={80} size={13} color={l.c} lines={[l.v]} />
          <Lines x={l.x} cy={l.cy + 19} align="center" w={80} size={7.5} color={l.c} lines={[l.d]} />
        </div>
      ))}
      <Abs x={860} y={181} w={28} h={1} style={{ background: '#666' }} />
      <Abs x={888} y={181} w={1} h={1} />
      <Lines x={915} cy={618} align="center" w={400} size={12.5} color="#555" lines={[pie.caption]} />
    </PrintSlide>
  )
}

function LineGraph() {
  const x0 = 696, x1 = 1167, y = (v: number) => 600 - v * 1.0175
  return (
    <PrintSlide page={line.page}>
      <ChartText data={line} />
      <Lines x={915} cy={125} align="center" w={400} size={19} className="font-medium" color={t.ink} lines={[line.chartTitle]} />
      {line.ticks.map((v) => (
        <div key={v}>
          {v > 0 && <Box x={x0} y={y(v)} w={x1 - x0} h={1} bg="#ddd" />}
          <Lines x={689} cy={y(v)} align="right" w={60} size={14} color="#333" lines={[String(v)]} />
        </div>
      ))}
      <Box x={x0} y={y(400)} w={1} h={y(0) - y(400)} bg="#999" />
      <Box x={x0} y={y(0)} w={x1 - x0} h={1} bg="#999" />
      <svg className="absolute left-0 top-0" width={1280} height={720}>
        {line.series.map((s) => (
          <g key={s.c}>
            <polyline points={s.values.map((v, i) => `${line.xs[i]},${y(v)}`).join(' ')} fill="none" stroke={s.c} strokeWidth={1.5} />
            {s.values.map((v, i) => <circle key={i} cx={line.xs[i]} cy={y(v)} r={3.5} fill={s.c} />)}
          </g>
        ))}
      </svg>
      {line.series.map((s, si) => s.values.map((v, i) => (si === 1 && i < 2 ? null : (
        <Lines key={`${si}-${i}`} x={line.xs[i] - (si === 0 && i === 3 ? 0 : 0)} cy={y(v) - 18} align="center" w={60} size={14} color={s.labelC} lines={[String(v)]} />
      ))))}
      {line.years.map((yr, i) => <Lines key={yr} x={line.xs[i]} cy={617} align="center" w={70} size={14} color="#333" lines={[yr]} />)}
      <Abs x={1104} y={240} w={0} h={0} style={{ borderBottom: '42px solid #555', borderLeft: '30px solid transparent', borderRight: '30px solid transparent' }} />
      <Box x={1118} y={281} w={32} h={52} bg="#555" />
      <Abs x={890} y={651} w={14} h={14} className="rounded-full" style={{ background: '#c4c4c4' }} />
      <Abs x={919} y={651} w={14} h={14} className="rounded-full" style={{ background: '#555' }} />
    </PrintSlide>
  )
}

function Team() {
  return (
    <PrintSlide showBrand={false}>
      <Abs x={44} y={30} h={62} className="font-bold whitespace-nowrap" style={{ writingMode: 'sideways-lr', fontSize: 9.5, color: '#111' } }>MIRICANVAS</Abs>
      <Heading x={214} cy={142} lines={team.title} />
      {team.members.map((m) => (
        <div key={m.name}>
          <Photo x={m.x - 68} y={276} w={136} h={136} className="h-full w-full rounded-full" />
          <Lines x={m.x} cy={438} align="center" w={200} size={19} className="font-bold" color={t.ink} lines={[m.name]} />
          <Lines x={m.x} cy={465} align="center" w={200} size={13} className="font-bold" color={t.ink} lines={[m.role]} />
          <Lines x={m.x} cy={487} align="center" w={200} size={12.5} className="font-montserrat" color={t.ink} lines={[m.en]} />
          <Lines x={m.x} cy={519} lh={16.3} align="center" w={200} size={12.5} color="#444" lines={[...m.duties, '“', ...m.motto, '”'].slice(0)} />
        </div>
      ))}
      <Box x={679} y={120} w={1.5} h={538} bg="#333" />
      {team.rows.map((r) => (
        <div key={r.dept}>
          <Lines x={718} cy={r.cy} size={13.5} className="font-bold" color={t.ink} lines={[r.dept]} />
          <Lines x={718} cy={r.cy + 32} lh={14.5} size={11.5} className="font-montserrat" color={t.ink} lines={r.en} />
          <Lines x={863} cy={r.cy} size={13.5} className="font-bold" color={t.ink} lines={[r.lead]} />
          {team.staff.map((s, i) => <Lines key={i} x={986 + i * 58.7} cy={r.cy + 2} align="center" w={60} size={12} className="font-medium" color={t.ink} lines={[s]} />)}
          <Lines x={863} cy={r.cy + 33} lh={14.5} size={11} color="#444" lines={r.desc} />
        </div>
      ))}
      {team.dividers.map((y) => <Box key={y} x={718} y={y} w={459} h={1} bg="#333" />)}
      <Lines x={45} cy={687} size={11.5} className="font-bold" color="#333" lines={[team.page]} />
      <Lines x={596} cy={687} align="center" w={300} size={9} color={t.muted} lines={[team.note]} />
    </PrintSlide>
  )
}

function QnA() {
  return (
    <PrintSlide showBrand={false}>
      <Photo x={0} y={0} w={1280} h={720} />
      <Lines x={640} cy={369} align="center" size={40} className="font-bold" color="#111" lines={[qna.title]} />
      <Company color="#111" />
    </PrintSlide>
  )
}

function Quote() {
  return (
    <PrintSlide showBrand={false}>
      <Photo x={0} y={0} w={1280} h={720} tone="#4b4b4b" />
      <Lines x={636} cy={298} align="center" w={40} size={20} color="#fff" lines={['“']} />
      <Lines x={636} cy={343} lh={40} align="center" size={27} color="#fff" lines={quote.lines} />
      <Lines x={636} cy={435} align="center" w={40} size={20} color="#fff" lines={['”']} />
      <Lines x={640} cy={476} align="center" size={22} className="font-greatvibes" color="#fff" lines={[quote.author]} />
      <Company color="#fff" />
    </PrintSlide>
  )
}

const deck: DeckDefinition = { id: '06', title: '검정과 흰색의 모던한 인쇄용 보고서', slides: [Cover, About, Mission, Timeline, Product, Pie, LineGraph, Team, QnA, Quote] }
export default deck
