import { ChevronRight, Earth, Handshake, Orbit, Recycle } from 'lucide-react'
import type { DeckDefinition } from '../../ui'
import { Abs, ImagePlaceholder, cn } from '../../ui'
import { Blob, Card, Lines, Page, Pill, T, Title } from './components'
import { cover, delivery, figures, market, mission, philosophy, positioning, problem, team, traction } from './data'
import { t } from './theme'

function Cover() {
  return (
    <Page>
      <Blob x={220} y={0} w={1060} h={700} r="0 0 0 400px" />
      <Abs x={0} y={0} w={787} h={523} style={{ background: t.bg, borderRadius: '0 0 56px 0' }} />
      <Title x={102} y={108} size={69} lh={81} lines={cover.title} />
      <Abs x={102} y={311} w={582} h={1.5} style={{ background: t.ink }} />
      <T x={107} y={355} size={21.9} className="font-medium">{cover.sub}</T>
      <Lines x={105} y={394} size={16.3} lh={23} lines={cover.body} style={{ color: t.body }} />
    </Page>
  )
}

const msIcons = [Handshake, Earth, Orbit, Recycle]
function Mission() {
  return (
    <Page no="02" label="Mission & Values">
      <Blob x={380} y={100} w={900} h={620} r={300} />
      <Title x={116} y={160} size={55} lh={68} lines={mission.title} />
      <Lines x={118} y={324} size={16} lh={23.5} lines={mission.body} style={{ color: t.body }} />
      {mission.cards.map((c, i) => {
        const x = i % 2 ? 852 : 541, y = i < 2 ? 137 : 390, Icon = msIcons[i]
        return (
          <Card key={c.k} x={x} y={y} w={298} h={241}>
            <Abs x={33} y={48}><Icon size={50} strokeWidth={1.2} color={t.ink} /></Abs>
            <T x={33} y={124} size={20} className="font-semibold">{c.k}</T>
            <Lines x={33} y={158} size={15} lh={19.5} lines={c.body} style={{ color: t.body }} />
          </Card>
        )
      })}
    </Page>
  )
}

function Philosophy() {
  return (
    <Page no="03" label="Brand Philosophy">
      <Title x={147} y={128} size={56.5} lines={[philosophy.title]} />
      <T x={694} y={145} size={19} className="font-medium">{philosophy.sub}</T>
      <T x={694} y={179} size={15.5} style={{ color: t.body }}>{philosophy.body}</T>
      {philosophy.circles.map((c, i) => {
        const cx = [373, 641, 908][i]
        return (
          <div key={c.k}>
            <Abs x={cx - 150} y={310} w={300} h={300}><ImagePlaceholder label="green gradient circle" tone={t.blobTone} className="h-full w-full rounded-full" /></Abs>
            <T x={cx - 68} y={426} size={16} className="font-medium text-white">{c.no}</T>
            <T x={cx - 70} y={453} size={25} className="font-semibold text-white">{c.k}</T>
          </div>
        )
      })}
      {philosophy.circles.map((_, i) => <Abs key={i} x={[373, 641, 908][i] - 150} y={310} w={300} h={300} className="rounded-full" style={{ border: '1.5px solid #fff' }} />)}
    </Page>
  )
}

function Problem() {
  return (
    <Page no="04" label="Problem & Solution">
      <Blob x={95} y={145} w={1095} h={475} r={60} />
      <Card x={116} y={169} w={342} h={426} r={24} />
      <Title x={160} y={270} size={54} lh={58} lines={problem.title} />
      <Lines x={160} y={421} size={16} lh={23} lines={problem.body} style={{ color: t.body }} />
      {problem.cards.map((c, i) => {
        const x = [471, 824][i]
        return (
          <div key={c.k}>
            <Card x={x} y={169} w={341} h={426} r={30} />
            <Abs x={x + 15} y={183} w={311} h={398}><ImagePlaceholder label="photo" className="h-full w-full rounded-[22px]" /></Abs>
            <T x={x + 40} y={474} size={21} className="font-semibold">{c.k}</T>
            <Lines x={x + 41} y={502} size={14} lh={17} lines={c.body} style={{ color: '#222', letterSpacing: '-0.01em' }} />
          </div>
        )
      })}
      <Abs x={782} y={345} w={72} h={72} className="flex items-center justify-center rounded-full bg-white"><ChevronRight size={40} strokeWidth={3.5} color={t.ink} /></Abs>
    </Page>
  )
}

function Market() {
  const y = (v: number) => 606 - v * 2.19
  return (
    <Page no="05" label="Green Market Growth">
      <Blob x={460} y={110} w={820} h={610} r={300} />
      <T x={117} y={153} size={19.2} className="font-medium">{market.kicker}</T>
      <Title x={115} y={180} size={56} lh={65} lines={market.title} />
      <Lines x={117} y={347} size={16} lh={23} lines={market.body} style={{ color: t.body }} />
      {market.ticks.map((v) => (
        <div key={v}>
          <Abs x={609} y={y(v)} w={528} h={1} style={{ background: '#cfd8cf' }} />
          <T x={540} y={y(v) - 8} w={60} size={15} align="right" className="font-semibold">{v}</T>
        </div>
      ))}
      {market.values.map((v, i) => {
        const cx = [673, 806, 938, 1071][i]
        return (
          <div key={i}>
            <Abs x={cx - 43} y={y(v)} w={87} h={606 - y(v)} style={{ background: t.card, borderRadius: '6px 6px 0 0' }} />
            <T x={cx - 20} y={617} w={40} size={15} align="center" className="font-semibold">{i + 1}</T>
          </div>
        )
      })}
    </Page>
  )
}

const dvNodes = [
  { k: 'Production', disc: [763, 237], pill: [762, 186, 306], text: [836, 'left'] },
  { k: 'Distribution', disc: [575, 411], pill: [280, 360, 295], text: [502, 'right'] },
  { k: 'Customer', disc: [934, 411], pill: [934, 360, 289], text: [1001, 'left'] },
  { k: 'ESG Feedback', disc: [763, 585], pill: [427, 534, 336], text: [684, 'right'] },
] as const
function Delivery() {
  return (
    <Page no="06" label="Delivery Diagram">
      <Title x={89} y={130} size={56} lines={[delivery.title]} />
      <T x={92} y={215} size={19} className="font-medium">{delivery.sub}</T>
      <T x={92} y={246} size={16} style={{ color: t.body }}>{delivery.body}</T>
      <Abs x={602} y={250} w={322} h={322}><ImagePlaceholder label="green gradient blob" tone={t.blobTone} className="h-full w-full rounded-full" /></Abs>
      <Abs x={602} y={250} w={322} h={322} className="rounded-full" style={{ border: '1.5px solid #fff' }} />
      <T x={663} y={399} w={200} size={24} align="center" className="font-semibold text-white">{delivery.center}</T>
      {dvNodes.map((n, i) => {
        const [px, , pw] = n.pill, py = n.disc[1] - 51
        const lines = i === 3 ? delivery.esgText : delivery.text
        return (
          <div key={n.k}>
            <Abs x={px} y={py} w={pw} h={102} className="rounded-full" style={{ background: t.green }} />
            <Abs x={n.disc[0] - 52} y={n.disc[1] - 52} w={104} h={104} className="flex items-center justify-center rounded-full text-center font-semibold" style={{ background: t.card, fontSize: 14, lineHeight: '17px' }}>
              {n.k === 'ESG Feedback' ? <span>ESG<br />Feedback</span> : n.k}
            </Abs>
            <Lines x={n.text[1] === 'right' ? n.text[0] - 300 : n.text[0]} y={n.disc[1] - 18} w={n.text[1] === 'right' ? 300 : undefined} size={14} lh={17.5} align={n.text[1]} lines={lines} style={{ color: '#2a2a2a' }} />
          </div>
        )
      })}
    </Page>
  )
}

function Positioning() {
  return (
    <Page no="07" label="Market Positioning Map">
      <Blob x={380} y={120} w={640} h={520} r={260} />
      <Title x={89} y={133} size={56} lh={63} lines={positioning.title} />
      <Lines x={89} y={287} size={16} lh={23} lines={positioning.body} style={{ color: t.body }} />
      <Abs x={807} y={245} w={1.5} h={328} className="bg-white" />
      <Abs x={593} y={409} w={426} h={1.5} className="bg-white" />
      {positioning.axes.map((a) => <Pill key={a.text} cx={a.cx} cy={a.cy} w={a.w} h={51} text={a.text} size={20} className="font-medium" />)}
      {positioning.brands.map((b) => (
        <div key={b.k}>
          <Abs x={b.x - 14} y={b.y - 14} w={28} h={28} className="rounded-full" style={{ background: b.ours ? '#a8d5bd' : '#fff' }} />
          <T x={b.x + 28} y={b.y - 10} size={18.5}>{b.k}</T>
        </div>
      ))}
    </Page>
  )
}

function Team() {
  return (
    <Page no="08" label="Our Team">
      <Blob x={30} y={240} w={1220} h={340} r={170} />
      <Title x={140} y={98} w={1000} size={56} align="center" lines={[team.title]} />
      <T x={340} y={170} w={600} size={18} align="center">{team.sub}</T>
      {team.members.map((m, i) => {
        const cx = [165, 515, 857][i]
        return (
          <div key={m.name}>
            <Card x={cx} y={251} w={266} h={217} r={20} />
            <Abs x={cx + 40} y={223} w={186} h={245}><ImagePlaceholder label="portrait photo" className="h-full w-full" /></Abs>
            <T x={m.x} y={497} size={23.4} className={cn(t.serif, 'font-semibold')}>{m.name}</T>
            <Abs x={m.x - 1} y={536} w={252} h={1.5} style={{ background: t.ink }} />
            <T x={m.x} y={550} size={17}>{m.role}</T>
            <Lines x={m.x} y={579} size={14} lh={21} lines={m.bio} className="font-light" style={{ color: '#333', letterSpacing: '-0.02em' }} />
          </div>
        )
      })}
    </Page>
  )
}

function Traction() {
  const y = (v: number) => 531 - v * 4.8375, xs = [616, 833, 1053]
  return (
    <Page no="09" label="Traction">
      <Blob x={420} y={150} w={860} h={570} r={280} />
      <T x={89} y={128} size={19}>{traction.kicker}</T>
      <Title x={88} y={158} size={56} lines={[traction.title]} />
      <Lines x={89} y={246} size={16} lh={23} lines={traction.body} style={{ color: t.body }} />
      {traction.ticks.map((v) => (
        <div key={v}>
          <Abs x={506} y={y(v)} w={658} h={1} style={{ background: '#d9ddd5' }} />
          <T x={456} y={y(v) - 7} w={40} size={14} align="right">{v}</T>
        </div>
      ))}
      <svg className="absolute left-0 top-0" width={1280} height={720}>
        {traction.series.map((s, si) => (
          <g key={si}>
            <polyline points={s.map((v, i) => `${xs[i]},${y(v)}`).join(' ')} fill="none" stroke="#fff" strokeWidth={1.5} />
            {s.map((v, i) => <circle key={i} cx={xs[i]} cy={y(v)} r={3} fill="#fff" />)}
          </g>
        ))}
      </svg>
      {traction.metrics.map((m, i) => {
        const cx = [653, 835, 1023][i]
        return (
          <div key={m.k}>
            <Pill cx={cx} cy={590} w={156} h={33} text={m.k} size={17} />
            <T x={cx - 100} y={623} w={200} size={27} align="center" className="font-medium">{m.v}</T>
          </div>
        )
      })}
    </Page>
  )
}

const fc = { d1: t.green, d2: t.sageDark, d3: t.sage }
const Legend = ({ x, y, items, gap = 15, size = 10 }: { x: number; y: number; items: readonly (readonly [string, string])[]; gap?: number; size?: number }) => (
  <>{items.map(([l, c], i) => (
    <div key={l}>
      <Abs x={x} y={y + i * gap - 4} w={8} h={8} style={{ background: c }} />
      <T x={x + 12} y={y + i * gap - 5} size={size} style={{ color: '#444' }}>{l}</T>
    </div>
  ))}</>
)
function Figures() {
  const f3 = (v: number) => 380 - v * 1.425, f4 = (v: number) => 622 - v * 1.28, f5 = (v: number) => 602 - v * 1.35
  const p3 = [[922, 20], [1015, 40], [1107, 70]] as const
  const p4 = [20, 40, 70, 60, 90, 80, 100].map((v, i) => [162 + i * 52.5, v] as const)
  const s5 = [[20, 40, 60, 50, 40], [30, 50, 70, 40, 60]]
  return (
    <Page no="10" label="Traction">
      <Blob x={60} y={180} w={1160} h={520} r={100} />
      <Title x={89} y={99} size={56} lines={[figures.title]} />
      <T x={336} y={114} size={16} className="font-semibold">{figures.desc[0]}</T>
      <T x={336} y={136} size={15.2} style={{ color: t.body }}>{figures.desc[1]}</T>
      {[[92, 195, 356, 219], [461, 195, 359, 219], [833, 195, 357, 219], [92, 428, 486, 222], [590, 428, 598, 222]].map(([x, y, w, h], i) => (
        <div key={i}>
          <Card x={x} y={y} w={w} h={h} />
          <T x={x + 20} y={y + 20} size={17} className="font-medium">{`Figure ${i + 1}.`}</T>
        </div>
      ))}
      {/* Figure 1 — pie */}
      <Abs x={181} y={239} w={150} h={150} className="rounded-full" style={{ background: `conic-gradient(${fc.d1} 0 33.3%, ${fc.d2} 0 66.6%, ${fc.d3} 0)` }} />
      <Legend x={338} y={297} items={[['DATA 1', fc.d1], ['DATA 2', fc.d2], ['DATA 3', fc.d3]]} />
      {/* Figure 2 — horizontal bars */}
      {[497, 557, 617, 677, 737].map((x) => <Abs key={x} x={x} y={254} w={1} h={133} style={{ background: '#ddd' }} />)}
      {[[272, 556, fc.d1], [306, 616, fc.d3], [339, 706, fc.d2]].map(([y, x1, c]) => <Abs key={y} x={497} y={+y} w={+x1 - 497} h={30} style={{ background: c as string, borderRadius: '0 4px 4px 0' }} />)}
      <Legend x={746} y={308} gap={11} size={8} items={[['DATA 01', fc.d1], ['DATA 02', fc.d3], ['DATA 03', fc.d2]]} />
      {/* Figure 3 — line */}
      {[80, 60, 40, 20, 0].map((v) => (
        <div key={v}>
          <Abs x={877} y={f3(v)} w={276} h={1} style={{ background: '#ddd' }} />
          <T x={850} y={f3(v) - 5} w={22} size={9} align="right">{v}</T>
        </div>
      ))}
      <svg className="absolute left-0 top-0" width={1280} height={720}>
        <polyline points={p3.map(([x, v]) => `${x},${f3(v)}`).join(' ')} fill="none" stroke={t.olive} strokeWidth={1.5} />
        {p3.map(([x, v]) => <circle key={x} cx={x} cy={f3(v)} r={3.5} fill={t.olive} />)}
        <polygon points={`162,622 ${p4.map(([x, v]) => `${x},${f4(v)}`).join(' ')} 477,622`} fill="#e9ebe4" />
        <polyline points={p4.map(([x, v]) => `${x},${f4(v)}`).join(' ')} fill="none" stroke={t.green} strokeWidth={2} />
        {p4.map(([x, v]) => <circle key={x} cx={x} cy={f4(v)} r={3.5} fill={t.green} />)}
      </svg>
      {p3.map(([x, v]) => <T key={x} x={x - 15} y={f3(v) - 18} w={30} size={9} align="center" style={{ color: '#888' }}>{v}</T>)}
      {['DATA 01', 'DATA 02', 'DATA 03'].map((l, i) => <T key={l} x={p3[i][0] - 30} y={383} w={60} size={8.5} align="center">{l}</T>)}
      {/* Figure 4 — area */}
      {[100, 80, 60, 40, 20, 0].map((v) => (
        <div key={v}>
          <Abs x={135} y={f4(v)} w={368} h={1} style={{ background: '#ddd' }} />
          <T x={106} y={f4(v) - 5} w={26} size={9} align="right">{v}</T>
        </div>
      ))}
      {p4.map(([x, v], i) => (
        <div key={x}>
          <T x={x - 15} y={f4(v) - 17} w={30} size={9} align="center" style={{ color: '#bbb' }}>{v}</T>
          <T x={x - 10} y={626} w={20} size={9} align="center">{i + 1}</T>
        </div>
      ))}
      <Abs x={512} y={553} w={8} h={8} className="rounded-full" style={{ background: t.green }} />
      <T x={524} y={552} size={9}>DATA 01</T>
      {/* Figure 5 — grouped bars */}
      {[80, 60, 40, 20, 0].map((v) => (
        <div key={v}>
          <Abs x={640} y={f5(v)} w={503} h={1} style={{ background: '#ddd' }} />
          <T x={614} y={f5(v) - 5} w={22} size={8} align="right">{v}</T>
        </div>
      ))}
      {[691, 791, 891, 991, 1091].map((cx, i) => (
        <div key={cx}>
          {s5.map((s, si) => <Abs key={si} x={cx + (si ? 5 : -31)} y={f5(s[i])} w={30} h={602 - f5(s[i])} style={{ background: si ? fc.d3 : fc.d1 }} />)}
          <T x={cx - 30} y={607} w={60} size={7} align="center">{`DATA 0${i + 1}`}</T>
        </div>
      ))}
      <Abs x={869} y={628} w={7} h={7} style={{ background: fc.d1 }} />
      <T x={879} y={627} size={8}>1</T>
      <Abs x={886} y={628} w={7} h={7} style={{ background: fc.d3 }} />
      <T x={896} y={627} size={8}>2</T>
    </Page>
  )
}

const deck: DeckDefinition = { id: '14', title: '그린 미니멀리스트 사업 계획 프레젠테이션', slides: [Cover, Mission, Philosophy, Problem, Market, Delivery, Positioning, Team, Traction, Figures] }
export default deck
