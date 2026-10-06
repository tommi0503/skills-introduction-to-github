import type { DeckDefinition } from '../../ui'
import { Abs, Slide, cn } from '../../ui'
import type { LucideIcon } from 'lucide-react'
import { Backpack, Bug, CalendarClock, CloudRain, Flame, Lamp, MessageCircleMore, Phone, ShoppingCart, Sunset, Tent, Thermometer, UtensilsCrossed } from 'lucide-react'
import { Box, Card, Hand, Lines, Logo, Page, Ph, Polaroid, Txt } from './components'
import { agenda, checks, closing, cook, cover, gear, guide, manners, sets, sites, sleep, types, warm, why } from './data'
import { t } from './theme'

const Leaf = ({ x, y, s = 60 }: { x: number; y: number; s?: number }) => <Ph x={x} y={y} w={s} h={s} label="autumn leaf" className="rounded-[50%_0]" />
const Price = ({ v, size }: { v: string; size: number }) => <>{v}<span style={{ fontSize: size * 0.7 }}>원</span></>
const Orange = 'font-bold'

/** Kraft hang tag with handwritten lines and a doodle (left side of the orange slides). */
function HangTag({ lines }: { lines: readonly string[] }) {
  return (
    <>
      <Box x={75} y={40} w={255} h={428} r={8} fill="#f1dcc0" style={{ clipPath: 'polygon(25% 0,75% 0,100% 12%,100% 100%,0 100%,0 12%)' }} />
      <Box x={118} y={125} w={205} h={1.5} fill={t.ink} />
      <Lines x={120} cy0={160} gap={42} size={30} lines={lines} className={t.hand} />
      <Box x={110} y={292} w={198} h={1.5} fill={t.ink} />
      <Ph x={102} y={302} w={196} h={142} label="camping doodle" className="rounded-t-[100px]" />
    </>
  )
}
const OrangePanel = () => <Box x={300} y={0} w={980} h={720} fill={t.orange} />

function Cover() {
  return (
    <Page>
      <Abs x={40} y={86} w={1200} h={128} className="overflow-visible whitespace-nowrap leading-none">
        <span className={cn(t.serif, 'inline-block origin-left')} style={{ fontSize: 158, color: t.orange, transform: 'scaleX(0.625)', letterSpacing: '-0.02em', lineHeight: '128px' }}>{cover.title}</span>
      </Abs>
      <Box x={35} y={230} w={1210} h={2} fill={t.orange} />
      <Hand x={40} cy={264} size={27}>{cover.sub}</Hand>
      <Ph x={0} y={290} w={1280} h={430} label="autumn mountain campsite photo" />
      <Ph x={860} y={245} w={390} h={360} label="bell tent and chairs" />
    </Page>
  )
}

function Why() {
  return (
    <Page>
      <Ph x={735} y={65} w={490} h={310} label="orange tent photo" />
      <Ph x={820} y={360} w={440} h={340} label="tent interior photo" />
      <Ph x={370} y={400} w={440} h={320} label="riverside sunset photo" />
      <Leaf x={1180} y={270} s={80} /><Leaf x={240} y={490} s={140} /><Leaf x={570} y={385} s={90} />
      <Hand x={60} cy={158} size={58}>{why.title[0]}</Hand>
      <Hand x={60} cy={240} size={64}>{why.title[1]}</Hand>
      <Txt x={60} cy={317} size={23} className="font-bold">{why.lead}</Txt>
      <Lines x={60} cy0={362} gap={30} size={19} lines={why.body} style={{ color: t.text }} />
    </Page>
  )
}

function Pin({ cx, cy, n }: { cx: number; cy: number; n: number }) {
  return (
    <Abs x={cx - 26} y={cy - 26} w={52} h={52} className={cn(t.serif, 'flex items-center justify-center leading-none')} style={{ background: t.orange, borderRadius: '50% 50% 50% 0', transform: undefined, color: t.orange, fontSize: 22 }}>
      <span className="flex h-[36px] w-[36px] items-center justify-center rounded-full" style={{ background: '#fbe6dc' }}>{String(n).padStart(2, '0')}</span>
    </Abs>
  )
}

function Agenda() {
  const pos = [[415, 88], [832, 78], [435, 298], [850, 287], [415, 500], [832, 490]]
  return (
    <Slide background={t.bg} style={{ color: t.ink }}>
      <OrangePanel />
      <HangTag lines={agenda.tag} />
      <Logo x={40} cy={675} />
      {agenda.items.map(([h, s], i) => {
        const [x, y] = pos[i]
        return (
          <div key={h}>
            <Box x={x} y={y} w={385} h={165} r={3} fill={t.bg} />
            <Pin cx={x + 12} cy={y + 2} n={i + 1} />
            <Txt x={x + 46} cy={y + 46} size={26} className="font-bold">{h}</Txt>
            <Box x={x + 46} y={y + 75} w={306} h={1} fill={t.line} />
            <Txt x={x + 44} cy={y + 103} size={21} style={{ color: t.text }}>{s}</Txt>
          </div>
        )
      })}
    </Slide>
  )
}

function Types() {
  return (
    <Page>
      <Hand x={640} cy={133} size={48} align="center" w={1200}>{types.title}</Hand>
      {types.items.map((it, i) => {
        const x = 55 + i * 395
        return (
          <div key={it.name}>
            <Card x={x} y={213} w={380} h={457} />
            <Ph x={x + 17} y={233} w={346} h={230} label={`${it.name} photo`} />
            <Txt x={x + 28} cy={505} size={19} className={Orange} style={{ color: t.orange }}>{it.name}</Txt>
            <Txt x={x + 28} cy={532} size={16} className="font-semibold">{it.desc}</Txt>
            <Abs x={x + 22} y={566} w={350} h={28} className="flex gap-[9px]">
              {it.tags.map((g) => <span key={g} className={cn(t.body, 'flex items-center rounded-[3px] px-[8px] font-semibold leading-none text-white')} style={{ background: t.orange, fontSize: 14 }}>{g}</span>)}
            </Abs>
            <Lines x={x + 22} cy0={614} gap={23} size={16} lines={it.points} style={{ color: t.text }} />
          </div>
        )
      })}
    </Page>
  )
}

function Guide() {
  const m = guide.main
  return (
    <Page>
      <Hand x={640} cy={140} size={50} align="center">{guide.title[0]}</Hand>
      <Hand x={640} cy={215} size={52} align="center">{guide.title[1]}</Hand>
      <Card x={48} y={318} w={625} h={350} />
      <Polaroid x={50} y={315} w={265} h={325} label="family auto camping photo" />
      <Txt x={347} cy={370} size={19} className="font-bold">{m.kicker}</Txt>
      <Txt x={347} cy={400} size={21} className={Orange} style={{ color: t.orange }}>{m.name}</Txt>
      <Lines x={347} cy0={440} gap={25} size={16} lines={m.body} style={{ color: t.text }} />
      <Lines x={347} cy0={533} gap={26.5} size={16} lines={m.points} style={{ color: t.text }} />
      {guide.side.map((s, i) => {
        const y = i ? 487 : 300
        const d = i ? 191 : 0
        return (
          <div key={s.name}>
            <Card x={718} y={y} w={495} h={i ? 180 : 165} />
            <Polaroid x={728} y={y - (i ? 2 : 17)} w={145} h={i ? 170 : 172} pad={6} label={`${s.name} photo`} />
            <Txt x={895} cy={339 + d} size={18} className="font-bold">{s.kicker}</Txt>
            <Txt x={895} cy={367 + d} size={20} className={Orange} style={{ color: t.orange }}>{s.name}</Txt>
            <Box x={895} y={392 + d} w={290} h={1} fill={t.line} />
            <Lines x={895} cy0={415 + d} gap={23} size={16} lines={s.body} style={{ color: t.text }} />
          </div>
        )
      })}
      <Leaf x={605} y={605} s={100} />
    </Page>
  )
}

function Sites() {
  return (
    <Page>
      <Ph x={0} y={80} w={440} h={310} label="tent and chairs photo" />
      <Ph x={62} y={365} w={415} h={330} label="autumn campsite photo" />
      <Leaf x={0} y={590} s={110} /><Leaf x={1100} y={110} s={70} /><Leaf x={1090} y={240} s={150} />
      <Hand x={518} cy={155} size={56}>{sites.title[0]}</Hand>
      <Hand x={518} cy={238} size={56}>{sites.title[1]}</Hand>
      {sites.items.map(([h, a, b], i) => {
        const x = [512, 872][i % 2]
        const y = [310, 495][Math.floor(i / 2)]
        return (
          <div key={h}>
            <Card x={x} y={y} w={340} h={172} />
            <Txt x={x + 28} cy={y + 33} size={17} className={t.serif} style={{ color: t.sub }}>{`0${i + 1}.`}</Txt>
            <Txt x={x + 28} cy={y + 62} size={20} className={Orange} style={{ color: t.orange }}>{h}</Txt>
            <Box x={x + 28} y={y + 86} w={295} h={1} fill={t.line} />
            <Lines x={x + 28} cy0={y + 113} gap={25} size={16} lines={[a, b]} style={{ color: t.text }} />
          </div>
        )
      })}
    </Page>
  )
}

const IconCircle = ({ cx, cy, r, Icon, s }: { cx: number; cy: number; r: number; Icon: LucideIcon; s: number }) => (
  <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className="flex items-center justify-center rounded-full" style={{ background: t.bg }}><Icon size={s} color={t.icon} strokeWidth={1.4} /></Abs>
)

const checkIcons = [Thermometer, Sunset, Bug, Flame, CloudRain, CalendarClock]
function Checks() {
  return (
    <Page>
      <Hand x={640} cy={133} size={50} align="center">{checks.title}</Hand>
      <Polaroid x={68} y={210} w={358} h={455} pad={12} label="campsite photo" />
      {checks.items.map(([h, d], i) => {
        const x = [478, 855][i % 2]
        const y = 222 + Math.floor(i / 2) * 150
        return (
          <div key={h}>
            <Card x={x} y={y} w={358} h={130} />
            <IconCircle cx={x + 68} cy={y + 70} r={45} Icon={checkIcons[i]} s={46} />
            <Txt x={x + 133} cy={y + 43} size={16} style={{ color: t.sub }}>{`CHECK POINT 0${i + 1}`}</Txt>
            <Txt x={x + 133} cy={y + 69} size={19} className={Orange} style={{ color: t.orange }}>{h}</Txt>
            <Txt x={x + 133} cy={y + 98} size={17}>{d}</Txt>
          </div>
        )
      })}
    </Page>
  )
}

const gearIcons = [Tent, UtensilsCrossed, Backpack, Lamp]
function Gear() {
  return (
    <Page>
      <Hand x={640} cy={135} size={48} align="center">{gear.title}</Hand>
      <Polaroid x={460} y={215} w={365} h={475} label="bell tent campsite photo" />
      {gear.items.map(([h, a, b], i) => {
        const x = i < 2 ? 48 : 840
        const y = i % 2 ? 450 : 243
        const Icon = gearIcons[i]
        return (
          <div key={h}>
            <Card x={x} y={y} w={393} h={i % 2 ? 185 : 182} />
            <Abs x={x + 300} y={y + 28}><Icon size={50} color={t.icon} strokeWidth={1.2} /></Abs>
            <Txt x={x + 32} cy={y + 30} size={17} className={t.serif} style={{ color: t.sub }}>{`0${i + 1}.`}</Txt>
            <Txt x={x + 32} cy={y + 62} size={20} className={Orange} style={{ color: t.orange }}>{h}</Txt>
            <Box x={x + 32} y={y + 88} w={335} h={1} fill={t.line} />
            <Lines x={x + 32} cy0={y + 117} gap={25} size={16} lines={[a, b]} style={{ color: t.text }} />
          </div>
        )
      })}
    </Page>
  )
}

function Sleep() {
  return (
    <Page>
      <Hand x={640} cy={138} size={48} align="center">{sleep.title}</Hand>
      <Leaf x={60} y={110} s={70} /><Leaf x={0} y={215} s={80} /><Leaf x={1130} y={550} s={150} />
      {sleep.items.map((p, i) => {
        const x = i ? 655 : 108
        const tx = i ? 690 : 142
        return (
          <div key={p.name}>
            <Card x={x} y={375} w={515} h={295} />
            <Polaroid x={x + 38} y={200} w={445} h={272} pad={6} label={p.name} />
            <Txt x={tx} cy={515} size={21} className={Orange} style={{ color: t.orange }}>{p.name}</Txt>
            <Txt x={tx} cy={548} size={16}>{p.spec}</Txt>
            <Box x={tx + 268} y={505} w={175} h={48} r={3} fill="#f6efe7" />
            <Txt x={tx + 355} cy={530} size={26} align="center" w={175} className="font-bold" style={{ color: t.orange }}><Price v={p.price} size={26} /></Txt>
            <Lines x={tx} cy0={608} gap={25} size={16} lines={p.desc} style={{ color: t.text }} />
          </div>
        )
      })}
    </Page>
  )
}

function OrangeTag({ x, y, w, h, size, children }: { x: number; y: number; w: number; h: number; size: number; children: string }) {
  return (
    <>
      <Box x={x} y={y} w={w} h={h} r={3} fill={t.orange} />
      <Txt x={x + w / 2} cy={y + h / 2} size={size} align="center" w={w} className="font-bold" style={{ color: '#fff' }}><Price v={children} size={size} /></Txt>
    </>
  )
}

function Cook() {
  return (
    <Page>
      <Hand x={640} cy={135} size={48} align="center">{cook.title}</Hand>
      {cook.items.map((p, i) => {
        const x = [82, 460, 845][i]
        return (
          <div key={p.name}>
            <Card x={x} y={410} w={362} h={290} />
            <Polaroid x={x + 22} y={207} w={318} h={256} pad={5} label={p.name} />
            <Txt x={x + 33} cy={504} size={20} className={Orange} style={{ color: t.orange }}>{p.name}</Txt>
            <Txt x={x + 33} cy={534} size={16}>{p.spec}</Txt>
            <Lines x={x + 33} cy0={580} gap={26} size={15.5} lines={p.desc} style={{ color: t.text }} />
            <OrangeTag x={x + 205} y={630} w={165} h={55} size={25}>{p.price}</OrangeTag>
          </div>
        )
      })}
    </Page>
  )
}

function Warm() {
  return (
    <Page>
      <Hand x={640} cy={135} size={48} align="center">{warm.title}</Hand>
      {warm.items.map(([n, s, p], i) => {
        const x = 75 + i * 285
        const cx = x + 136
        return (
          <div key={n}>
            <Card x={x} y={205} w={272} h={450} />
            <Polaroid x={x + 18} y={205} w={240} h={290} pad={8} label={n} />
            <Txt x={cx} cy={527} size={22} align="center" w={272} className={Orange} style={{ color: t.orange }}>{n}</Txt>
            <Txt x={cx} cy={559} size={16} align="center" w={272}>{s}</Txt>
            <Box x={x + 25} y={585} w={222} h={1} fill={t.line} />
            <Txt x={cx} cy={619} size={24} align="center" w={272} className="font-bold" style={{ color: '#6a5a52' }}><Price v={p} size={24} /></Txt>
          </div>
        )
      })}
    </Page>
  )
}

function Sets() {
  return (
    <Page>
      <Hand x={640} cy={135} size={48} align="center">{sets.title}</Hand>
      <Leaf x={1180} y={200} s={100} /><Leaf x={80} y={410} s={80} /><Leaf x={0} y={520} s={70} />
      {sets.items.map((s, i) => {
        const x = i ? 658 : 118
        return (
          <div key={s.name}>
            <Card x={x} y={225} w={505} h={472} />
            <Ph x={x + 17} y={217} w={465} h={300} label={s.name} />
            <OrangeTag x={x + 323} y={479} w={188} h={55} size={25}>{s.price}</OrangeTag>
            <Txt x={x + 30} cy={532} size={23} className={Orange} style={{ color: t.orange }}>{s.name}</Txt>
            <Txt x={x + 30} cy={562} size={16}>{s.spec}</Txt>
            <Box x={x + 30} y={585} w={445} h={1} fill={t.line} />
            <Lines x={x + 30} cy0={608} gap={25} size={16} lines={s.desc} style={{ color: t.text }} />
          </div>
        )
      })}
    </Page>
  )
}

function Manners() {
  return (
    <Page>
      <Polaroid x={50} y={140} w={410} h={520} pad={12} label="friends at campsite photo" />
      <Hand x={505} cy={158} size={50}>{manners.title}</Hand>
      {manners.items.map(([h, a, b], i) => {
        const x = i === 1 ? 520 : 500
        const y = [222, 375, 527][i]
        return (
          <div key={h}>
            <Card x={x} y={y} w={715} h={i === 2 ? 140 : 135} />
            <Ph x={x + 38} y={y + 22} w={110} h={90} label="line illustration" />
            <Txt x={682 + (i === 1 ? 20 : 0)} cy={y + 43} size={20} className={Orange} style={{ color: t.orange }}>{h}</Txt>
            <Lines x={682 + (i === 1 ? 20 : 0)} cy0={y + 76} gap={25} size={16} lines={[a, b]} style={{ color: t.text }} />
          </div>
        )
      })}
    </Page>
  )
}

const contactIcons = [Phone, ShoppingCart, MessageCircleMore]
function Closing() {
  const c = closing
  return (
    <Slide background={t.bg} style={{ color: t.ink }}>
      <OrangePanel />
      <HangTag lines={c.tag} />
      <Logo x={40} cy={675} />
      <Lines x={400} cy0={94} gap={47} size={30} lines={c.head} className="font-medium" style={{ color: '#fff' }} />
      <Box x={390} y={190} w={825} h={272} r={3} fill={t.bg} />
      <Txt x={448} cy={240} size={24}><b className="font-bold" style={{ color: t.orange }}>{c.visit[0]}</b>&nbsp; {c.visit[1]}</Txt>
      <Box x={420} y={275} w={750} h={1} fill={t.line} />
      {[670, 940].map((x) => <Box key={x} x={x} y={300} w={1} h={100} fill={t.line} />)}
      {c.contacts.map(([l, v], i) => {
        const cx = [540, 805, 1075][i]
        const Icon = contactIcons[i]
        return (
          <div key={l}>
            <Abs x={cx - 14} y={302}><Icon size={28} color={t.orange} strokeWidth={2} /></Abs>
            <Txt x={cx} cy={357} size={22} align="center" w={260} className="font-bold" style={{ color: t.orange }}>{l}</Txt>
            <Txt x={cx} cy={387} size={22} align="center" w={260}>{v}</Txt>
          </div>
        )
      })}
      <Polaroid x={340} y={465} w={305} h={225} pad={8} label="campsite photo" />
      <Polaroid x={655} y={455} w={290} h={235} pad={8} label="tent at night photo" />
      <Polaroid x={945} y={475} w={305} h={230} pad={8} label="mountain tent photo" />
    </Slide>
  )
}

const deck: DeckDefinition = {
  id: '34',
  title: '주황색 깔끔 가을캠핑 안내',
  slides: [Cover, Why, Agenda, Types, Guide, Sites, Checks, Gear, Sleep, Cook, Warm, Sets, Manners, Closing],
}
export default deck
