import type { DeckDefinition } from '../../ui'
import { Abs, ImagePlaceholder, cn } from '../../ui'
import { Building2, Check, House, MapPin, TrendingUp, TreeDeciduous } from 'lucide-react'
import { Base, Circle, Hl, Lines, RailSlide, Rich, Title, Txt } from './components'
import { agenda, center, checklist, closing, compare, conditions, courses, cover, faq, growth, managers, photoNote, produce, roadmap, sideLabels, stories } from './data'
import { t } from './theme'

const Ph = ({ x, y, w, h, label, className }: { x: number; y: number; w: number; h: number; label: string; className?: string }) => (
  <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label={label} className={cn('h-full w-full', className)} /></Abs>
)
const Note = ({ cy = 695 }: { cy?: number }) => <Txt x={1257} cy={cy} size={12} align="right" className={t.body} style={{ color: '#8a8a8a' }}>{photoNote}</Txt>

function Cover() {
  return (
    <Base>
      <Circle cx={1334} cy={703} r={774} color={t.green} />
      <Ph x={640} y={100} w={640} h={620} label="vegetable crate photo" />
      <Abs x={90} y={90} w={281} h={95} style={{ background: t.hl }} />
      <Title x={93} cy={136} size={80} lines={[cover.title[0]]} d={t.hl} />
      <Title x={93} cy={240} size={80} lines={[cover.title[1]]} />
      <Lines x={94} cy0={340} gap={35} size={22} lines={cover.sub} className={cn(t.body, 'font-semibold')} />
      <Txt x={94} cy={543} size={20} className={cn(t.body, 'font-bold')}>{cover.org}</Txt>
      <Abs x={94} y={572} w={349} h={2} style={{ background: t.ink }} />
      <Lines x={94} cy0={604} gap={32} size={20} lines={cover.meta} className={cn(t.body, 'font-semibold')} />
    </Base>
  )
}

function Agenda() {
  return (
    <Base>
      <Title x={640} cy={110} size={50} align="center" lines={[agenda.title]} />
      <Abs x={0} y={531} w={1280} h={2} style={{ background: t.ink }} />
      {agenda.items.map((it, i) => {
        const cx = 189 + i * 225
        const [x, y, w, h] = it.img
        return (
          <div key={i}>
            <Ph x={x} y={y} w={w} h={h} label="strawberry growth stage" className="rounded-[40%]" />
            <Txt x={cx} cy={481} size={34} align="center" w={200} d>{String(i + 1).padStart(2, '0')}</Txt>
            <Circle cx={cx} cy={532} r={8} color={t.ink} />
            <Lines x={cx} cy0={578} gap={33} size={20} align="center" w={220} lines={it.lines} className={cn(t.body, 'font-semibold')} />
          </div>
        )
      })}
    </Base>
  )
}

function Growth() {
  return (
    <RailSlide active={0} label={sideLabels[0]}>
      <Title lines={[growth.title]} />
      <Lines x={173} cy0={166} gap={34} size={22.5} lines={growth.sub} className={cn(t.body, 'font-semibold')} />
      {growth.bars.map((b, i) => {
        const x = 368 + i * 288
        return (
          <div key={b.year}>
            <Abs x={x} y={b.top} w={246} h={720 - b.top} style={{ background: b.color, borderRadius: '123px 123px 0 0' }} />
            <Txt x={x + 123} cy={b.labelCy} size={46} align="center" w={246} d={b.color} style={{ color: b.ink }}>
              {b.value}<span style={{ fontSize: 33, WebkitTextStrokeWidth: 0.8 }}>%</span>
            </Txt>
            <Txt x={x + 123} cy={630} size={28} align="center" w={246} d={b.color} style={{ color: b.ink }}>{b.year}</Txt>
          </div>
        )
      })}
      <Abs x={545} y={398}><TrendingUp size={92} color={t.green} strokeWidth={2.6} /></Abs>
      <Abs x={832} y={238}><TrendingUp size={92} color={t.green} strokeWidth={2.6} /></Abs>
    </RailSlide>
  )
}

function Compare() {
  return (
    <RailSlide active={0} label={sideLabels[0]}>
      <Title x={688} cy={122} align="center" lines={[compare.title]} />
      {compare.cols.map((c, ci) => {
        const x = 193 + ci * 559
        return (
          <div key={c.name}>
            <Abs x={x} y={212} w={430} h={408} className="overflow-hidden rounded-[18px] bg-white">
              <div className="h-[100px]" style={{ background: t.green }} />
            </Abs>
            <Txt x={x + 215} cy={246} size={38} align="center" w={430} d={t.green}>{c.name}</Txt>
            <Txt x={x + 215} cy={285} size={20} align="center" w={430} className={cn(t.body, 'font-semibold')}>{c.en}</Txt>
            {c.rows.map((r, ri) => (
              <div key={r}>
                <Txt x={x + 215} cy={364 + ri * 103} size={22} align="center" w={430} className={cn(t.body, 'font-semibold')}>{r}</Txt>
                {ri < 2 && <Abs x={x} y={415 + ri * 103} w={430} h={1} style={{ background: t.line }} />}
              </div>
            ))}
          </div>
        )
      })}
      <Circle cx={688} cy={264} r={45} color={t.beige2} />
      <Txt x={688} cy={266} size={46} align="center" w={100} d={t.beige2}>VS</Txt>
      {compare.keys.map((k, i) => (
        <div key={k}>
          <Txt x={688} cy={364 + i * 103} size={21} align="center" w={120} className={cn(t.body, 'font-semibold')}>{k}</Txt>
          {i < 2 && <Abs x={640} y={415 + i * 103} w={97} h={2} style={{ background: t.ink }} />}
        </div>
      ))}
    </RailSlide>
  )
}

function Roadmap() {
  return (
    <RailSlide active={1} label={sideLabels[1]}>
      <Title lines={[roadmap.title]} />
      <svg className="absolute left-0 top-0" width={1280} height={720}>
        {roadmap.steps.map((_, i) => {
          const cx = 301 + i * 129.3
          const cy = i % 2 ? 452 : 377
          return <polygon key={i} points={`${cx - 112},${cy} ${cx},${cy - 62} ${cx + 112},${cy} ${cx},${cy + 62}`} fill={roadmap.colors[i]} stroke={roadmap.colors[i]} strokeWidth={14} strokeLinejoin="round" />
        })}
        {roadmap.steps.map((_, i) => {
          const cx = 301 + i * 129.3
          const [y1, y2] = i % 2 ? [452, 568] : [265, 377]
          return (
            <g key={i} stroke="#7aa77a" strokeWidth={1.5} fill="#fff">
              <line x1={cx} y1={y1} x2={cx} y2={y2} />
              <circle cx={cx} cy={y1} r={2.5} /><circle cx={cx} cy={y2} r={2.5} />
            </g>
          )
        })}
      </svg>
      <Ph x={955} y={262} w={100} h={205} label="walking farmer" />
      {roadmap.steps.map(([head, sub], i) => {
        const cx = 301 + i * 129.3
        const cy = i % 2 ? 600 : 203
        return (
          <div key={head}>
            <Txt x={cx} cy={cy} size={26} align="center" w={220} d={t.hl}><Hl>{head}</Hl></Txt>
            <Txt x={cx} cy={cy + 32} size={20} align="center" w={220} className={cn(t.body, 'font-semibold')}>{sub}</Txt>
          </div>
        )
      })}
    </RailSlide>
  )
}

function Conditions() {
  const circles = [
    { cx: 1145, cy: 452, r: 200, color: t.green2 },
    { cx: 815, cy: 600, r: 147, color: t.green3 },
    { cx: 940, cy: 177, r: 196, color: t.green },
  ]
  const icons = [
    { Icon: House, x: 940, y: 138, s: 80 },
    { Icon: TreeDeciduous, x: 1128, y: 398, s: 64 },
    { Icon: Building2, x: 814, y: 556, s: 58 },
  ]
  const labels = [
    { x: 940, cy: 220, ls: 40, vcy: 268, vs: 36, bg: t.green },
    { x: 1128, cy: 478, ls: 34, vcy: 519, vs: 30, bg: t.green2 },
    { x: 814, cy: 624, ls: 30, vcy: 658, vs: 24, bg: t.green3 },
  ]
  return (
    <RailSlide active={1} label={sideLabels[1]}>
      {circles.map((c, i) => <Circle key={i} {...c} />)}
      {conditions.stats.map((s, i) => {
        const { Icon, x, y, s: size } = icons[i]
        const l = labels[i]
        return (
          <div key={s.label}>
            <Abs x={x - size / 2} y={y - size / 2}><Icon size={size} color={t.ink} strokeWidth={2.4} /></Abs>
            <Txt x={l.x} cy={l.cy} size={l.ls} align="center" w={300} d={l.bg}>{s.label}</Txt>
            <Txt x={l.x} cy={l.vcy} size={l.vs} align="center" w={300} d={l.bg}>{s.value}</Txt>
          </div>
        )
      })}
      <Title lines={conditions.title} gap={60} />
      <Lines x={173} cy0={226} gap={33} size={22.5} lines={conditions.body} className={cn(t.body, 'font-semibold')} />
      {conditions.pills.map((p, i) => {
        const cy = 425 + i * 85
        const Icon = icons[i].Icon
        return (
          <div key={i}>
            <Abs x={165} y={cy - 32} w={340} h={64} className="rounded-full bg-white" />
            <Circle cx={200} cy={cy} r={32} color={t.green} />
            <Abs x={181} y={cy - 19}><Icon size={38} color={t.ink} strokeWidth={2.2} /></Abs>
            <Lines x={250} cy0={cy - 14} gap={28} size={18} lines={p} className={cn(t.body, 'font-semibold')} />
          </div>
        )
      })}
    </RailSlide>
  )
}

function Produce() {
  return (
    <RailSlide active={1} label={sideLabels[1]}>
      <Title x={686} align="center" lines={[produce.title]} />
      {produce.items.map((p, i) => {
        const cx = 273 + i * 275
        const [x, y, w, h] = p.img
        return (
          <div key={p.name}>
            <Circle cx={cx} cy={297} r={101} color={t.green} />
            <Ph x={x} y={y} w={w} h={h} label={p.name} className="rounded-[30%]" />
            <Txt x={cx} cy={466} size={20} align="center" w={260} className={cn(t.body, 'font-semibold')}>{p.kicker}</Txt>
            <Txt x={cx} cy={501} size={32} align="center" w={260} d={t.hl}><Hl>{p.name}</Hl></Txt>
            <Abs x={cx - 106} y={533} w={212} h={2} style={{ background: t.ink }} />
            <Lines x={cx} cy0={560} gap={25} size={17} align="center" w={270} lines={p.desc} className={cn(t.body, 'font-semibold')} />
          </div>
        )
      })}
    </RailSlide>
  )
}

function Courses() {
  return (
    <RailSlide active={1} label={sideLabels[1]}>
      <Title x={686} align="center" lines={[courses.title]} />
      <Abs x={324} y={511} w={722} h={2} style={{ background: t.ink }} />
      {courses.items.map((c, i) => {
        const cx = 324 + i * 361
        return (
          <div key={c.level}>
            <Abs x={cx - 134} y={208} w={268} h={268} className="rounded-full" style={{
              background: `conic-gradient(transparent 0 ${c.from}deg, ${c.color} ${c.from}deg ${c.to}deg, transparent ${c.to}deg)`,
              mask: 'radial-gradient(circle, transparent 84px, #000 85px)', WebkitMask: 'radial-gradient(circle, transparent 84px, #000 85px)',
            }} />
            <Txt x={cx} cy={333} size={34} align="center" w={200} d>{c.level}</Txt>
            <Circle cx={cx} cy={512} r={9} color={t.ink} />
            <Txt x={cx} cy={550} size={23} align="center" w={300} d={t.hl}><Hl>{c.name}</Hl></Txt>
            <Lines x={cx} cy0={593} gap={28} size={19} align="center" w={340} lines={c.desc} className={cn(t.body, 'font-semibold')} />
          </div>
        )
      })}
    </RailSlide>
  )
}

function Stories() {
  return (
    <RailSlide active={2} label={sideLabels[2]}>
      <Title lines={[stories.title]} />
      {stories.items.map((s, i) => {
        const x = 232 + (i % 2) * 535
        const y = 184 + Math.floor(i / 2) * 250
        return (
          <div key={s.name}>
            <Abs x={x} y={y} w={440} h={216} className="rounded-[20px] bg-white" />
            <Abs x={x - 70} y={y - 14} w={186} h={186} style={{ background: '#95df92', borderRadius: '50% 50% 0 50%' }} />
            <Abs x={x - 57} y={y - 2} w={160} h={160} className="overflow-hidden rounded-full"><ImagePlaceholder label="interviewee photo" className="h-full w-full" /></Abs>
            <Txt x={x + 140} cy={y + 46} size={34} d={t.hl}><Hl>{s.name}</Hl><span style={{ fontSize: 30, WebkitTextStrokeWidth: 0.8 }}> 씨</span></Txt>
            <Txt x={x + 140} cy={y + 89} size={19} className={cn(t.body, 'font-bold')} style={{ color: t.greenText }}>{s.info}</Txt>
            <Lines x={x + 140} cy0={y + 129} gap={25} size={17} lines={s.quote} className={cn(t.body, 'font-semibold')} />
          </div>
        )
      })}
      <Note />
    </RailSlide>
  )
}

function Checklist() {
  return (
    <RailSlide active={3} label={sideLabels[3]}>
      <Title lines={checklist.title} />
      <Ph x={185} y={250} w={315} h={470} label="farmer holding vegetable box" />
      {checklist.items.map((it, i) => {
        const cy = 150 + i * 139.5
        return (
          <div key={i}>
            <Abs x={580} y={cy - 47} w={592} h={94} className="rounded-full bg-white" />
            <Abs x={624} y={cy - 17} w={34} h={34} className="flex items-center justify-center rounded-full" style={{ background: t.green }}>
              <Check size={22} color="#fff" strokeWidth={3.5} />
            </Abs>
            <Lines x={722} cy0={cy - 14} gap={28} size={19} lines={it} className={cn(t.body, 'font-semibold')} />
          </div>
        )
      })}
      <Note />
    </RailSlide>
  )
}

function Managers() {
  return (
    <RailSlide active={3} label={sideLabels[3]}>
      <Note cy={30} />
      <Title x={688} align="center" lines={[managers.title]} />
      {managers.items.map((m, i) => {
        const x = 163 + i * 357
        return (
          <div key={m.name}>
            <Abs x={x} y={186} w={334} h={262} style={{ background: t.green, borderRadius: '167px 167px 0 0' }} />
            <Ph x={x + 67} y={158} w={200} h={290} label="manager portrait" className="rounded-t-[90px]" />
            <Abs x={x} y={448} w={334} h={272} className="bg-white" />
            <Txt x={x + 29} cy={497} size={30} d="#fff">{m.name}<span style={{ fontSize: 25, WebkitTextStrokeWidth: 0.7 }}> {m.rank}</span></Txt>
            <Txt x={x + 29} cy={539} size={19} className={cn(t.body, 'font-semibold')} style={{ color: t.greenText }}>{m.dept}</Txt>
            <Abs x={x + 29} y={571} w={276} h={2} style={{ background: t.ink }} />
            <Txt x={x + 29} cy={605} size={17} className={cn(t.body, 'font-bold')}>{managers.dutyLabel}</Txt>
            <Lines x={x + 29} cy0={630} gap={24} size={17} lines={m.duty} className={cn(t.body, 'font-semibold')} />
          </div>
        )
      })}
    </RailSlide>
  )
}

function Faq() {
  return (
    <RailSlide active={4} label={sideLabels[4]}>
      <Title x={1192} cy={93} gap={69} align="right" size={46} lines={faq.title} />
      {faq.items.map((f) => (
        <div key={f.q}>
          <Txt x={f.x} cy={f.qCy} size={36} d>Q.</Txt>
          <Abs x={f.pill[0]} y={f.qCy - 31} w={f.pill[1]} h={62} className="rounded-full" style={{ background: t.green }} />
          <Txt x={f.pill[0] + 18} cy={f.qCy - 2} size={21} className={cn(t.body, 'font-semibold')}>{f.q}</Txt>
          <Txt x={f.x} cy={f.aCy} size={36} d>A.</Txt>
          <Lines x={f.pill[0] + 5} cy0={f.aCy - 2} gap={30} size={21} lines={f.a} className={cn(t.body, 'font-semibold')} />
        </div>
      ))}
    </RailSlide>
  )
}

function Center() {
  const rows = [369, 417, 466]
  return (
    <RailSlide active={4} label={sideLabels[4]}>
      <Title lines={[center.title]} cy={94} />
      <Ph x={173} y={260} w={479} h={286} label="map" />
      <Abs x={385} y={292}><MapPin size={52} fill={t.green} color={t.green} strokeWidth={1.5} /></Abs>
      <Txt x={420} cy={408} size={17} align="center" w={260} className={cn(t.body, 'font-bold')}><Hl>{center.pin}</Hl></Txt>
      <Txt x={698} cy={277} size={28} d>{center.heading}</Txt>
      <Abs x={698} y={317} w={521} h={2} style={{ background: t.ink }} />
      {[center.phone.label, center.address.label, center.online.label].map((l, i) => (
        <Txt key={l} x={698} cy={rows[i]} size={20} className={cn(t.body, 'font-semibold')}>{l}</Txt>
      ))}
      <Txt x={824} cy={rows[0]} size={22} className={cn(t.body, 'font-semibold')}>{center.phone.value}<span style={{ fontSize: 17 }}>{center.phone.note}</span></Txt>
      <Txt x={824} cy={rows[1]} size={20} className={cn(t.body, 'font-semibold')}>{center.address.value}</Txt>
      <Ph x={824} y={455} w={89} h={89} label="QR code" />
      <Lines x={934} cy0={471} gap={35} size={20} lines={center.online.lines} className={cn(t.body, 'font-semibold')} />
    </RailSlide>
  )
}

function Closing() {
  return (
    <Base>
      <svg className="absolute left-0 top-0" width={1280} height={720}>
        <path id="d29arc" d="M 165 589 A 475 475 0 0 1 1115 589" fill="none" />
        <text className="font-montserrat" fontSize={40} fontWeight={500} fill={t.ink}>
          <textPath href="#d29arc" startOffset="50%" textAnchor="middle">{closing.arc}</textPath>
        </text>
      </svg>
      <Ph x={418} y={220} w={410} h={300} label="vegetable crate photo" />
      <Txt x={640} cy={584} size={21} align="center" className={cn(t.body, 'font-semibold')}>{closing.line}</Txt>
      <Txt x={640} cy={630} size={24} align="center" className={cn(t.body, 'font-bold')}><Rich text={`==${closing.cta}==`} /></Txt>
    </Base>
  )
}

const deck: DeckDefinition = {
  id: '29',
  title: '연두 깔끔 귀농귀촌 안내',
  slides: [Cover, Agenda, Growth, Compare, Roadmap, Conditions, Produce, Courses, Stories, Checklist, Managers, Faq, Center, Closing],
}
export default deck
