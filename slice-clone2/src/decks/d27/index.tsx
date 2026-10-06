import {
  Backpack, BriefcaseMedical, CircleCheck, CloudMoon, CloudRainWind, CookingPot, Droplets, FireExtinguisher, Flame, Grid3x3, Lamp,
  Lightbulb, SprayCan, Sunset, Tent, Trash2, Usb, Waves, Wind,
} from 'lucide-react'
import type { DeckDefinition } from '../../ui'
import { Abs } from '../../ui'
import { ArrowDot, Card, Leaf, Page, Ph, Rule, Script, TicketSlide, Txt } from './components'
import { checks, contents, cook, cover, gear, guide, rules, sets, sites, sleep, types, warm, welcome, why } from './data'
import { t } from './theme'
import type { Level } from './data'

const W = '#fff'
const levelColor: Record<Level, string> = { 높음: t.hi, 보통: t.mid, 낮음: t.low }
const Framed = ({ x, y, w, h, b = 6 }: { x: number; y: number; w: number; h: number; b?: number }) => (
  <Abs x={x} y={y} w={w} h={h} className="bg-white" style={{ padding: b }}><Ph x={b} y={b} w={w - b * 2} h={h - b * 2} /></Abs>
)

function Cover() {
  return (
    <TicketSlide card={{ x: 109, y: 87, w: 1058, h: 558 }}>
      <Framed x={48} y={391} w={198} h={206} />
      <Framed x={1027} y={210} w={213} h={210} />
      <Leaf x={70} y={205} s={95} />
      <Leaf x={195} y={350} s={85} />
      <Leaf x={1095} y={400} s={95} />
      <Txt x={640} cy={183} size={25} align="center" w={700} className="font-medium">{cover.kicker}</Txt>
      <Txt x={640} cy={278} size={124} lh={120} align="center" w={900} className="font-medium tracking-[-0.03em]" style={{ color: t.forest }}>{cover.title[0]}</Txt>
      <Txt x={640} cy={403} size={124} lh={120} align="center" w={900} className="font-medium tracking-[-0.03em]">{cover.title[1]}</Txt>
      <Script x={640} cy={478} size={110} w={500}>{cover.script}</Script>
      <Abs x={580} y={565} w={136} h={36} className="flex items-center justify-center rounded-full font-bold" style={{ background: '#333', color: W, fontSize: 14 }}>{cover.badge}</Abs>
    </TicketSlide>
  )
}

function Why() {
  return (
    <TicketSlide band={{ h: 106, ...why.band, size: 26, side: 15 }} card={{ x: 181, y: 167, w: 917, h: 497 }}>
      <Leaf x={135} y={340} s={85} />
      <Leaf x={1055} y={395} s={95} />
      <Txt x={640} cy={262} size={74} lh={74} align="center" w={500} className="font-medium">{why.title}</Txt>
      <Script x={640} cy={305} size={46}>{why.script}</Script>
      {[364, 423, 484].map((y) => <Rule key={y} x={258} y={y} w={763} color="#bdb6a6" />)}
      {why.lines.map((l, i) => <Txt key={l} x={640} cy={394 + i * 60} size={21} align="center" w={900}>{l}</Txt>)}
      {why.tags.map((tg, i) => (
        <Abs key={tg} x={276 + i * 252} y={525} w={227} h={63} className="flex items-center justify-center bg-white font-pen" style={{ fontSize: 28, boxShadow: '0 1px 3px rgba(0,0,0,.15)' }}>{tg}</Abs>
      ))}
    </TicketSlide>
  )
}

function Contents() {
  return (
    <Page band={67}>
      <Ph x={0} y={122} w={171} h={138} />
      <Ph x={1082} y={38} w={196} h={159} />
      <Leaf x={140} y={115} s={70} />
      <Txt x={640} cy={164} size={78} lh={80} align="center" w={700} className="font-medium tracking-[-0.01em]">{contents.title}</Txt>
      <Script x={645} cy={219} size={50} color="#8bbf6a">{contents.script}</Script>
      {contents.items.map(([title, sub], i) => {
        const x = 91 + Math.floor(i / 3) * 569, y = 342 + (i % 3) * 115.5
        return (
          <div key={title}>
            <Abs x={x} y={y - 6} w={68} h={44} className="flex items-center justify-center rounded-[50%]" style={{ border: `1px solid ${t.ink}`, fontSize: 16 }}>{`0${i + 1}`}</Abs>
            <Txt x={x + 93} cy={y} size={24} className="font-medium">{title}</Txt>
            <Txt x={x + 93} cy={y + 39} size={16}>{sub}</Txt>
            <Rule x={x} y={y + 74} w={525} color="#a39d8f" />
          </div>
        )
      })}
    </Page>
  )
}

function Types() {
  return (
    <Page no={types.no} title={types.title}>
      {types.items.map((it, i) => {
        const x = 90 + i * 374
        return (
          <Card key={it.name} x={x} y={188} w={351} h={459}>
            <Ph x={0} y={0} w={351} h={196} />
            <Abs x={150} y={181} w={52} h={30} className="flex items-center justify-center rounded-full" style={{ background: t.cream, border: `1px solid ${t.line}`, fontSize: 13 }}>{`0${i + 1}`}</Abs>
            <Script x={175} cy={256} size={36} opacity={0.75}>{it.script}</Script>
            <Txt x={175} cy={238} size={26} align="center" w={340} className="font-medium">{it.name}</Txt>
            <Rule x={20} y={282} w={311} color="#cfc8b8" />
            <Txt x={175} cy={304} size={13.5} align="center" w={340} className="font-semibold">{it.lead}</Txt>
            <Txt x={175} cy={326} size={13.5} lh={22} align="center" w={340}>{it.text}</Txt>
            <Rule x={20} y={382} w={311} color="#cfc8b8" />
            {types.labels.map((l, k) => (
              <div key={l}>
                <Txt x={89 + k * 86} cy={401} size={12} align="center" w={80}>{l}</Txt>
                <Abs x={50 + k * 86} y={414} w={78} h={27} className="flex items-center justify-center rounded-full font-semibold" style={{ background: levelColor[it.levels[k]], fontSize: 13 }}>{it.levels[k]}</Abs>
              </div>
            ))}
          </Card>
        )
      })}
    </Page>
  )
}

function Guide() {
  const m = guide.main
  return (
    <Page no={guide.no} title={guide.title}>
      <Card x={52} y={188} w={577} h={459}>
        <Ph x={0} y={0} w={577} h={322} tone="#6b6f63" label="auto camping photo (dark overlay)" />
        <Txt x={38} cy={64} size={33} lh={51} className="font-medium" style={{ color: W }}>{m.title}</Txt>
        <Script x={38} cy={154} size={36} align="left" color={t.cream}>{m.script}</Script>
        <Txt x={38} cy={277} size={15} style={{ color: W }}>{m.note}</Txt>
        {m.bullets.map((b, i) => <Txt key={b} x={38} cy={362 + i * 27.5} size={15}>{`•  ${b}`}</Txt>)}
      </Card>
      {guide.side.map((s, i) => {
        const y = 188 + i * 240
        return (
          <div key={s.script}>
            <Card x={651} y={y} w={579} h={219}><Ph x={0} y={0} w={207} h={219} /></Card>
            <ArrowDot cx={856} cy={y + 54} />
            <Txt x={900} cy={y + 51} size={21} lh={35} className="font-medium">{s.title}</Txt>
            <Script x={900} cy={y + 111} size={28} align="left" color="#a9b39a">{s.script}</Script>
            <Txt x={900} cy={y + 154} size={14} lh={23}>{s.text}</Txt>
          </div>
        )
      })}
    </Page>
  )
}

function Sites() {
  return (
    <Page no={sites.no} title={sites.title}>
      <Framed x={52} y={188} w={572} h={459} b={11} />
      <Leaf x={40} y={162} s={95} />
      {sites.items.map(([title, text], i) => {
        const y = 188 + i * 117.5
        return (
          <div key={title}>
            <Card x={671} y={y} w={559} h={102} r={6} />
            <ArrowDot cx={671} cy={y + 51} />
            <Txt x={724} cy={y + 37} size={22} className="font-medium">{title}</Txt>
            <Txt x={724} cy={y + 69} size={14}>{text}</Txt>
          </div>
        )
      })}
    </Page>
  )
}

function Checks() {
  const icons = [CloudMoon, Sunset, CloudRainWind, SprayCan, Flame]
  return (
    <Page no={checks.no} title={checks.title} sub={checks.sub}>
      {checks.items.map(([title, script, text], i) => {
        const x = 80 + i * 229.7, I = icons[i]
        return (
          <Card key={title} x={x} y={232} w={211} h={386} r={8}>
            <Abs x={92} y={31}><CircleCheck size={28} fill={t.badge} color={t.cream} strokeWidth={2} /></Abs>
            <Script x={105} cy={128} size={32} w={240} color="#efb79c" opacity={0.85}>{script}</Script>
            <Txt x={105} cy={110} size={28} align="center" w={200} className="font-medium">{title}</Txt>
            <Abs x={75} y={176}><I size={60} color={t.forest} strokeWidth={1.2} /></Abs>
            <Rule x={20} y={276} w={171} color="#cfc8b8" />
            <Txt x={105} cy={313} size={15} lh={25} align="center" w={200}>{text}</Txt>
          </Card>
        )
      })}
    </Page>
  )
}

function Gear() {
  const icons = [Tent, Backpack, CookingPot, Lamp]
  return (
    <Page no={gear.no} title={gear.title}>
      <Abs x={464} y={207} w={351} h={413} className="bg-white" />
      <Ph x={476} y={218} w={327} h={283} />
      <Script x={640} cy={579} size={38} color={t.ink}>{gear.script}</Script>
      {gear.items.map(([title, text], i) => {
        const right = i % 2 === 1, y = 234 + Math.floor(i / 2) * 190, I = icons[i]
        const x = right ? 841 : 64
        return (
          <div key={title}>
            <Card x={x} y={y} w={374} h={165} r={6} />
            <Abs x={(right ? 841 : 438) - 50} y={y + 32} w={100} h={100} className="flex items-center justify-center rounded-full" style={{ background: t.cream, border: `1px solid ${t.line}` }}><I size={46} color={t.ink} strokeWidth={1} /></Abs>
            <Txt x={right ? 911 : 362} cy={y + 52} size={24} align={right ? 'left' : 'right'} w={300} className="font-medium">{title}</Txt>
            <Txt x={right ? 911 : 362} cy={y + 87} size={14} lh={25} align={right ? 'left' : 'right'} w={300}>{text}</Txt>
          </div>
        )
      })}
    </Page>
  )
}

function Sleep() {
  return (
    <Page no={sleep.no} title={sleep.title}>
      {sleep.items.map((it, i) => {
        const x = 84 + i * 564
        return (
          <Card key={it.price} x={x} y={188} w={536} h={449}>
            <Ph x={0} y={0} w={536} h={273} />
            <Txt x={25} cy={317} size={25} lh={39} className="font-medium">{it.name}</Txt>
            <Txt x={25} cy={402} size={23} className="font-bold" style={{ color: t.orange }}>{it.price}</Txt>
            <Txt x={238} cy={317} size={16}>{it.spec}</Txt>
            <Rule x={238} y={337} w={272} color="#cfc8b8" />
            <Txt x={238} cy={361} size={13.5} lh={23.5}>{it.text}</Txt>
          </Card>
        )
      })}
    </Page>
  )
}

function Cook() {
  return (
    <Page no={cook.no} title={cook.title}>
      {cook.items.map((it, i) => {
        const x = 74 + i * 385
        return (
          <Card key={it.name} x={x} y={194} w={361} h={443} r={8}>
            <Ph x={0} y={0} w={361} h={223} />
            <Txt x={180} cy={263} size={25} align="center" w={360} className="font-medium">{it.name}</Txt>
            <Txt x={180} cy={297} size={13} align="center" w={360}>{it.sub}</Txt>
            <Rule x={0} y={334} w={361} color="#cfc8b8" />
            <Txt x={180} cy={367} size={16} align="center" w={360} className="font-medium">{it.spec}</Txt>
            <Txt x={180} cy={406} size={23} align="center" w={360} className="font-bold" style={{ color: t.orange }}>{it.price}</Txt>
          </Card>
        )
      })}
    </Page>
  )
}

function Warm() {
  const icons = [[Waves, Wind], [Grid3x3, Droplets], [Lightbulb, Usb], [FireExtinguisher, BriefcaseMedical]]
  return (
    <Page no={warm.no} title={warm.title}>
      {warm.items.map((it, i) => {
        const x = 54 + i * 298
        return (
          <Card key={it.name} x={x} y={194} w={280} h={442} r={8}>
            <Ph x={0} y={0} w={280} h={184} />
            <Txt x={140} cy={222} size={25} align="center" w={280} className="font-medium">{it.name}</Txt>
            <Rule x={0} y={266} w={280} color="#cfc8b8" />
            <Abs x={140} y={266} w={1} h={100} style={{ background: '#cfc8b8' }} />
            {it.feats.map((f, k) => {
              const I = icons[i][k]
              return (
                <div key={f}>
                  <Abs x={56 + k * 140} y={286}><I size={30} color={t.ink} strokeWidth={1} /></Abs>
                  <Txt x={71 + k * 140} cy={340} size={13} align="center" w={140}>{f}</Txt>
                </div>
              )
            })}
            <Rule x={0} y={366} w={280} color="#cfc8b8" />
            <Txt x={140} cy={403} size={23} align="center" w={280} className="font-bold" style={{ color: t.orange }}>{it.price}</Txt>
          </Card>
        )
      })}
    </Page>
  )
}

function Sets() {
  return (
    <Page no={sets.no} title={sets.title}>
      {sets.items.map((it, i) => {
        const x = 84 + i * 558
        return (
          <Card key={it.no} x={x} y={188} w={536} h={448}>
            <Ph x={0} y={0} w={536} h={271} />
            <Abs x={15} y={14} w={60} h={36} className="flex items-center justify-center rounded-full bg-white" style={{ fontSize: 13 }}>{it.no}</Abs>
            <Txt x={25} cy={311} size={25} className="font-medium">{it.name}</Txt>
            <Txt x={515} cy={311} size={24} align="right" w={300} className="font-bold" style={{ color: t.orange }}>{it.price}</Txt>
            <Rule x={0} y={350} w={536} color="#cfc8b8" />
            <Txt x={25} cy={380} size={17} className="font-medium">{it.items}</Txt>
            <Txt x={25} cy={412} size={13}>{it.text}</Txt>
          </Card>
        )
      })}
    </Page>
  )
}

function Rules() {
  const icons = [FireExtinguisher, Tent, Trash2]
  return (
    <Page no={rules.no} title={rules.title}>
      {rules.items.map((r, i) => {
        const x = 75 + i * 385.5, I = icons[i]
        return (
          <Card key={r.title} x={x} y={193} w={361} h={439}>
            <Abs x={110} y={52}><I size={140} color={t.orange} strokeWidth={0.9} /></Abs>
            <Txt x={180} cy={249} size={30} align="center" w={360} className="font-medium">{r.title}</Txt>
            <Script x={180} cy={276} size={36} w={360} opacity={0.9}>{r.script}</Script>
            <Txt x={32} cy={332} size={17} lh={29.5} w={320}>{r.text}</Txt>
          </Card>
        )
      })}
    </Page>
  )
}

function Welcome() {
  return (
    <TicketSlide band={{ h: 108, ...welcome.band, size: 30, side: 16 }} card={{ x: 180, y: 167, w: 920, h: 500 }}>
      <Leaf x={128} y={218} s={100} />
      <Leaf x={1048} y={372} s={100} />
      <Txt x={640} cy={262} size={84} lh={84} align="center" w={700} className="font-medium tracking-[-0.01em]">{welcome.title}</Txt>
      <Script x={640} cy={304} size={62} w={600}>{welcome.script}</Script>
      {welcome.lines.map((l, i) => <Txt key={l} x={640} cy={399 + i * 47} size={28} align="center" w={900} className="font-medium">{l}</Txt>)}
      {welcome.contacts.map(([k, v], i) => {
        const cx = [338, 552, 762, 960][i]
        return (
          <div key={k}>
            {i > 0 && <Abs x={cx - 105} y={530} w={1} h={72} style={{ background: '#bdb6a6' }} />}
            <Txt x={cx} cy={552} size={20} align="center" w={220} className="font-medium">{k}</Txt>
            <Txt x={cx} cy={583} size={16} align="center" w={220}>{v}</Txt>
          </div>
        )
      })}
    </TicketSlide>
  )
}

const deck: DeckDefinition = {
  id: '27',
  title: '갈색 깔끔 가을캠핑 가이드',
  slides: [Cover, Why, Contents, Types, Guide, Sites, Checks, Gear, Sleep, Cook, Warm, Sets, Rules, Welcome],
}
export default deck
