import { BadgeDollarSign, ChevronsRight, Gem, Headset, House, Leaf, MonitorPlay, Palette, Presentation, Users, UsersRound, Wallet } from 'lucide-react'
import type { DeckDefinition } from '../../ui'
import { Abs, Slide, cn } from '../../ui'
import { ArcText, Backdrop, Box, CardSlide, Footer, Ph, Txt, type Layout } from './components'
import { company, cover, customer, dept, mission, process, sales, service, thanks, toc } from './data'
import { t } from './theme'

const W = '#fff'
const alt = (i: number) => (i % 2 ? t.lime : t.yellow)

function Cover({ data = cover, panel = { x: 199, y: 138, w: 881, h: 464 } }: { data?: typeof cover; panel?: { x: number; y: number; w: number; h: number } }) {
  return (
    <Slide background={t.bg} className={t.font} style={{ color: t.ink }}>
      <Backdrop blobs={[[0, 0, 218, 138], [500, 0, 240, 72], [1000, 0, 280, 203], [0, 435, 355, 285], [928, 507, 352, 213]]} />
      <Ph x={170} y={555} w={130} h={100} label="orange dots" />
      <Box x={panel.x} y={panel.y} w={panel.w} h={panel.h} bg="rgba(255,255,255,0.85)" r={80} />
      <ArcText cx={640} cy={204} r={72} size={19} text={data.arc} spacing={0} />
      <Abs x={628} y={232}><Leaf size={26} fill={t.leaf} color={t.leaf} /></Abs>
      {data.title.map((l, i) => <Txt key={l} x={640} cy={331 + i * 94} size={91} align="center" w={1000} className={t.display}>{l}</Txt>)}
      <Abs x={435} y={509} w={400} h={49} className="flex items-center justify-center whitespace-nowrap rounded-full" style={{ background: t.pink, fontSize: 15 }}>{data.pill}</Abs>
      <Footer cy={668} />
    </Slide>
  )
}

const tocLayout: Layout = { card: { x: 90, y: 99, w: 1099, h: 562 }, tabTop: 26, tabR: 85, arcR: 44, markCy: 96, titleCy: 193 }
function Toc() {
  return (
    <CardSlide title={toc.title} layout={tocLayout} sub={null}>
      <Txt x={640} cy={254} size={18} align="center" w={600}>타이틀에 관한 내용을 입력하세요.</Txt>
      {toc.items.map(([no, label, sub], i) => {
        const col = Math.floor(i / 3), x = 157 + col * 497, y = 347 + (i % 3) * 93
        return (
          <Box key={no} x={x} y={y} w={468} h={75} bg={col ? t.lime : t.yellow} r={38}>
            <Abs x={31} y={0} h={75} className="flex items-center gap-[14px] whitespace-nowrap leading-none">
              <span className="font-montserrat font-medium" style={{ fontSize: 27, color: col ? '#8cbf3a' : '#f5b955' }}>{no}</span>
              <span className="font-montserrat font-bold" style={{ fontSize: 26 }}>{label}</span>
              <span style={{ fontSize: 12 }}>{sub}</span>
            </Abs>
          </Box>
        )
      })}
    </CardSlide>
  )
}

function Company() {
  return (
    <CardSlide chapter="1" title="COMPANY">
      <Ph x={138} y={255} w={406} h={355} label="team photo in orange blob" className="rounded-[45%]" />
      <Txt x={119} cy={632} size={10} style={{ color: '#888' }}>{company.note}</Txt>
      {company.items.map((it, i) => {
        const y = 267 + i * 117
        return (
          <div key={it.no}>
            <Box x={661} y={y} w={474} h={95} bg="#fdefc4" r={6} />
            <Abs x={632} y={y + 18} w={60} h={60} className="flex items-center justify-center rounded-full font-montserrat font-bold italic" style={{ background: t.green, fontSize: 17 }}>{it.no}</Abs>
            <Txt x={714} cy={y + 37} size={13} lh={20} style={{ color: t.body }}>{it.text}</Txt>
          </div>
        )
      })}
    </CardSlide>
  )
}

function Mission() {
  const icons = [Presentation, MonitorPlay, UsersRound]
  return (
    <CardSlide chapter="2" title="OUR MISSION">
      {mission.items.map((m, i) => {
        const x = 144 + i * 340, tag = i === 1 ? '#9cc94a' : t.orange
        const I = icons[i]
        return (
          <div key={m.title}>
            <Box x={x} y={278} w={310} h={322} bg={alt(i)} r={18} />
            <Abs x={x + 81} y={261} w={148} h={44} className="flex items-center justify-center rounded-full font-bold" style={{ background: tag, color: W, fontSize: 16 }}>{m.tag}</Abs>
            <Txt x={x + 155} cy={344} size={34} align="center" w={300} className="font-montserrat font-bold">{m.title}</Txt>
            <Abs x={x + 120} y={391}><I size={72} color={tag} strokeWidth={1.8} /></Abs>
            <Txt x={x + 30} cy={503} size={13} lh={20.5} w={270} style={{ color: t.body }}>{m.text}</Txt>
          </div>
        )
      })}
    </CardSlide>
  )
}

function Dept() {
  const rows = [280, 394, 509]
  const pill = (x: number, y: number, [title, sub]: string[], bg: string) => (
    <Box key={`${x}${y}`} x={x} y={y} w={353} h={92} bg={bg} r={46}>
      <Txt x={176} cy={32} size={22} align="center" w={350} className="font-bold">{title}</Txt>
      <Txt x={176} cy={62} size={15} align="center" w={350} style={{ color: t.body }}>{sub}</Txt>
    </Box>
  )
  return (
    <CardSlide chapter="3" title="DEPARTMENT">
      <Abs x={0} y={0}>
        <svg width={1280} height={720}>
          {rows.map((y) => [[481, 560], [800, 720]].map(([a, b]) => (
            <line key={`${y}${a}`} x1={a} y1={y + 46} x2={b} y2={y + 46 + (442 - y - 46) * 0.35} stroke={t.green} strokeWidth={2} strokeDasharray="2 4" />
          )))}
        </svg>
      </Abs>
      <Abs x={527} y={329} w={226} h={226} className="rounded-full" style={{ background: t.green }} />
      {dept.center.map((l, i) => <Txt key={l} x={640} cy={410 + i * 35} size={30} align="center" w={220} className="font-montserrat font-extrabold">{l}</Txt>)}
      <Txt x={640} cy={480} size={13} align="center" w={200} style={{ color: '#555' }}>{dept.centerSub}</Txt>
      {dept.left.map((d, i) => pill(128, rows[i], d, alt(i)))}
      {dept.right.map((d, i) => pill(797, rows[i], d, alt(i + 1)))}
    </CardSlide>
  )
}

function Service() {
  return (
    <CardSlide chapter="4" title="SERVICE" sub={null}>
      {service.items.map((s, i) => {
        const x = 160 + (i % 3) * 326, y = 220 + Math.floor(i / 3) * 187
        return (
          <Box key={s.title} x={x} y={y} w={307} h={168} bg={alt(i + Math.floor(i / 3))} r={10}>
            <Abs x={45} y={21} w={217} h={39} className="flex items-center justify-center rounded-full bg-white font-bold" style={{ fontSize: 17 }}>{s.title}</Abs>
            <Txt x={30} cy={90} size={11.5} lh={19} w={260} style={{ color: t.body }}>{s.text}</Txt>
          </Box>
        )
      })}
      <Txt x={640} cy={615} size={17} align="center" w={900}>{service.quote}</Txt>
    </CardSlide>
  )
}

function Process() {
  const icons = [Headset, Users, Palette, House]
  return (
    <CardSlide chapter="5" title="PROCESS">
      {process.items.map((p, i) => {
        const x = 110 + i * 277
        const I = icons[i]
        return (
          <div key={p.no}>
            <Box x={x} y={262} w={229} h={330} bg={t.limeSoft} r={60} />
            <Abs x={x + 80} y={262} w={70} h={40} className="flex items-center justify-center font-montserrat font-bold" style={{ background: t.lime, borderRadius: '0 0 14px 14px', fontSize: 20 }}>{p.no}</Abs>
            <Abs x={x + 85} y={345}><I size={60} color={t.ink} fill={i === 3 ? t.ink : 'none'} strokeWidth={2.2} /></Abs>
            <Abs x={x + 34} y={444} w={162} h={36} className="flex items-center justify-center rounded-full font-bold whitespace-nowrap" style={{ background: t.green, fontSize: 17 }}>{p.title}</Abs>
            <Txt x={x + 115} cy={503} size={12.5} lh={19.5} align="center" w={220} style={{ color: t.body }}>{p.text}</Txt>
            {i < 3 && <Abs x={x + 238} y={398}><ChevronsRight size={30} color={t.lime} strokeWidth={3} /></Abs>}
          </div>
        )
      })}
    </CardSlide>
  )
}

function Sales() {
  const base = 574, top = 286, k = (base - top) / 1000
  const icons = [Gem, BadgeDollarSign, Wallet]
  return (
    <CardSlide chapter="6" title="SALES RESULT" sub={null}>
      <Txt x={640} cy={216} size={18} align="center" w={600}>타이틀에 관한 내용을 입력하세요.</Txt>
      <Txt x={142} cy={241} size={10}>{sales.unit}</Txt>
      {sales.ticks.map((v) => (
        <div key={v}>
          <Abs x={199} y={base - v * k} w={430} h={1} style={{ background: '#ddd' }} />
          <Txt x={190} cy={base - v * k} size={14} align="right" w={60}>{v.toLocaleString()}</Txt>
        </div>
      ))}
      <Abs x={199} y={top} w={1} h={base - top} style={{ background: '#ddd' }} />
      {sales.bars.map(([yr, v], i) => {
        const cx = 235 + i * 73
        return (
          <div key={yr}>
            <Abs x={cx - 24} y={base - v * k} w={48} h={v * k} style={{ background: t.green }} />
            <Txt x={cx} cy={base - v * k - 13} size={13} align="center" w={60} style={{ color: t.orange }}>{v}</Txt>
            <Txt x={cx} cy={587} size={14} align="center" w={60}>{yr}</Txt>
          </div>
        )
      })}
      {sales.items.map((s, i) => {
        const y = 261 + i * 120, I = icons[i]
        return (
          <div key={s.title}>
            <Box x={690} y={y} w={442} h={105} bg={alt(i)} r={8} />
            <Abs x={710} y={y + 12} w={82} h={82} className="flex items-center justify-center rounded-full" style={{ background: i === 1 ? t.green : t.orange }}><I size={40} color={W} /></Abs>
            <Txt x={813} cy={y + 29} size={20} className="font-bold">{s.title}</Txt>
            <Txt x={813} cy={y + 57} size={11.5} lh={18} style={{ color: t.body }}>{s.text}</Txt>
          </div>
        )
      })}
    </CardSlide>
  )
}

function Customer() {
  return (
    <CardSlide chapter="7" title="CUSTOMER">
      {customer.notes.map((n, i) => {
        const x = 133 + i * 347.5, bg = i === 1 ? t.lime : '#fdeab0'
        return (
          <div key={i}>
            <Abs x={x} y={285} w={315} h={315} style={{ background: bg, clipPath: 'polygon(0 0,100% 0,100% 83%,85% 100%,0 100%)' }} />
            <Abs x={x + 268} y={548} w={47} h={52} style={{ background: i === 1 ? '#bcd86a' : '#f5d470', clipPath: 'polygon(100% 0,0 100%,0 0)' }} />
            <Abs x={x + 107} y={272} w={100} h={25} style={{ background: i === 1 ? '#f8d58a' : '#c6df86', opacity: 0.9 }} />
            <Txt x={x + 157} cy={350} size={23} lh={35} align="center" w={315} className="font-pen">{n.text}</Txt>
            <Txt x={x + 157} cy={548} size={25} align="center" w={315} className="font-pen font-bold">{n.by}</Txt>
          </div>
        )
      })}
    </CardSlide>
  )
}

function Thanks() {
  return (
    <Slide background={t.bg} className={t.font} style={{ color: t.ink }}>
      <Backdrop blobs={[[0, 0, 320, 190], [518, 0, 290, 82], [918, 0, 362, 250], [0, 490, 330, 230], [1000, 550, 280, 170]]} />
      <Ph x={165} y={535} w={135} h={110} label="orange dots" />
      <Box x={200} y={140} w={880} h={462} bg="rgba(255,255,255,0.85)" r={80} />
      <ArcText cx={640} cy={204} r={72} size={19} text={thanks.arc} spacing={0} />
      <Abs x={628} y={230}><Leaf size={26} fill={t.leaf} color={t.leaf} /></Abs>
      <Txt x={640} cy={342} size={97} align="center" w={1000} className={t.display}>{thanks.title}</Txt>
      <Txt x={640} cy={422} size={15} lh={19} align="center" w={600}>{thanks.sub}</Txt>
      <Abs x={327} y={505} w={626} h={50} className="flex items-center justify-center gap-[34px] whitespace-nowrap rounded-full leading-none" style={{ background: t.pink, fontSize: 17 }}>
        <span className="font-bold">{thanks.contact.team}</span>
        <span><b className={cn('mr-2 font-montserrat')}>E.</b>{thanks.contact.email}</span>
        <span><b className="mr-2 font-montserrat">T.</b>{thanks.contact.tel}</span>
      </Abs>
      <Footer cy={670} />
    </Slide>
  )
}

const deck: DeckDefinition = {
  id: '25',
  title: '노랑과 연두의 아기자기한 봄 보고서',
  slides: [() => <Cover />, Toc, Company, Mission, Dept, Service, Process, Sales, Customer, Thanks],
}
export default deck
