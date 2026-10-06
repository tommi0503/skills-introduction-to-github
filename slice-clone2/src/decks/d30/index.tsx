import type { DeckDefinition } from '../../ui'
import { Abs, ImagePlaceholder, Slide, cn } from '../../ui'
import { Bug, Check, ChevronRight, CloudRain, Flame, MessagesSquare, MonitorSmartphone, Phone, Store, Sunset, Thermometer } from 'lucide-react'
import { B, BL, Box, FrameSlide, Logo, Tag, Txt } from './components'
import { categories, checks, closing, cook, cover, guide, intro, manners, sets, sites, sleep, toc, types, warm } from './data'
import { t } from './theme'

const Ph = ({ x, y, w, h, label, className }: { x: number; y: number; w: number; h: number; label: string; className?: string }) => (
  <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label={label} className={cn('h-full w-full', className)} /></Abs>
)
const Dot = ({ cx, cy, r = 18, children }: { cx: number; cy: number; r?: number; children: React.ReactNode }) => (
  <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className="flex items-center justify-center rounded-full" style={{ background: t.brown, color: '#fff' }}>{children}</Abs>
)
const BrownPill = ({ x, y, w, h, size, children }: { x: number; y: number; w: number; h: number; size: number; children: string }) => (
  <>
    <Box x={x} y={y} w={w} h={h} r={h / 2} fill={t.brown} border={false} />
    <Txt x={x + w / 2} cy={y + h / 2} size={size} align="center" w={w} d={t.brown} style={{ color: '#fff' }}>{children}</Txt>
  </>
)

function Cover() {
  return (
    <Slide background={t.cream} style={{ color: t.brown }}>
      <Abs x={0} y={640} w={1280} h={80} style={{ background: t.green }} />
      <Ph x={55} y={425} w={330} h={215} label="trees" />
      <Ph x={235} y={560} w={210} h={140} label="camping chair and campfire" />
      <Ph x={880} y={415} w={400} h={265} label="tent and trees" />
      <Ph x={85} y={73} w={105} h={75} label="cloud" className="rounded-[40px]" />
      <Ph x={1048} y={297} w={108} h={60} label="cloud" className="rounded-[30px]" />
      <Box x={152} y={112} w={976} h={216} r={30} style={{ borderWidth: 2 }} />
      <Tag x={400} y={72} w={480} h={65} size={34}>{cover.tag}</Tag>
      <Txt x={640} cy={222} size={102} align="center" d style={{ color: t.brown }}>{cover.title}</Txt>
      <Ph x={420} y={300} w={415} h={420} label="camper character" className="rounded-t-[180px]" />
      <Logo x={1110} cy={41} size={19} />
    </Slide>
  )
}

function Intro() {
  return (
    <Slide background={t.cream} style={{ color: t.brown }}>
      <Abs x={0} y={690} w={1280} h={30} style={{ background: t.green }} />
      <Ph x={0} y={465} w={215} h={255} label="trees" />
      <Ph x={1075} y={445} w={205} h={275} label="trees" />
      <Ph x={200} y={188} w={128} h={75} label="cloud" className="rounded-[40px]" />
      <Ph x={980} y={348} w={118} h={70} label="cloud" className="rounded-[40px]" />
      <Ph x={158} y={337} w={80} h={70} label="bird" />
      <Ph x={988} y={132} w={68} h={58} label="bird" />
      <Tag y={85} h={46}>{intro.tag}</Tag>
      {intro.chars.map((c, i) => {
        const cx = 347 + i * 193
        return (
          <div key={c}>
            <Abs x={cx - 104} y={198} w={208} h={208} className="rounded-full" style={{ background: t.brown, border: `4px solid ${t.cream}` }} />
            <Txt x={cx} cy={302} size={104} align="center" w={200} d={t.brown} style={{ color: '#fff' }}>{c}</Txt>
          </div>
        )
      })}
      <Txt x={640} cy={470} size={46} align="center" d={t.cream} style={{ color: t.brown }}>{intro.question}</Txt>
      <BL x={640} cy0={530} gap={31} size={19} align="center" lines={intro.lines} />
    </Slide>
  )
}

function Toc() {
  return (
    <FrameSlide tag={toc.tag} title={toc.title}>
      {toc.items.map(([title, sub], i) => {
        const x = 85 + (i % 3) * 375
        const y = 266 + Math.floor(i / 3) * 174
        return (
          <div key={title}>
            <Box x={x} y={y} w={360} h={162} r={18} fill={i % 2 ? t.pale : t.cream} />
            <BrownPill x={x + 124} y={y + 14} w={112} h={34} size={24}>{String(i + 1).padStart(2, '0')}</BrownPill>
            <B x={x + 180} cy={y + 86} size={25} align="center" w={360} className="font-bold">{title}</B>
            <B x={x + 180} cy={y + 120} size={18} align="center" w={360}>{sub}</B>
          </div>
        )
      })}
      {[0, 1].flatMap((r) => [0, 1].map((c) => <Dot key={`${r}${c}`} cx={452 + c * 375} cy={348 + r * 174}><ChevronRight size={22} strokeWidth={2.5} /></Dot>))}
    </FrameSlide>
  )
}

function Types() {
  return (
    <FrameSlide tag={types.tag} title={types.title} frameX={53}>
      {types.items.map((it, i) => {
        const cx = 288 + i * 350
        return (
          <div key={it.name}>
            <Ph x={cx - 123} y={245} w={246} h={170} label={`${it.name} photo`} className="rounded-[50%]" />
            <BrownPill x={cx - 118} y={442} w={236} h={38} size={28}>{it.name}</BrownPill>
            <BL x={cx} cy0={508} gap={27} size={17} align="center" w={400} lines={it.points.map((p) => `•  ${p}`)} />
            <Abs x={cx - 200} y={565} w={400} h={30} className="flex justify-center gap-[10px]">
              {it.tags.map((g) => (
                <span key={g} className={cn(t.body, 'flex items-center rounded-full px-[13px] font-medium leading-none')} style={{ border: `1.5px solid ${t.brown}`, fontSize: 14 }}>{g}</span>
              ))}
            </Abs>
          </div>
        )
      })}
    </FrameSlide>
  )
}

function Note({ x, cy, children }: { x: number; cy: number; children: string }) {
  return (
    <>
      <Txt x={x} cy={cy} size={21} className={t.hand}>{children}</Txt>
      <Abs x={x - 4} y={cy + 13} w={170} h={1.5} style={{ background: t.brown }} />
      <Ph x={x + 152} y={cy - 2} w={30} h={24} label="star doodle" />
    </>
  )
}

function Guide() {
  const m = guide.main
  return (
    <FrameSlide tag={guide.tag} title={guide.title}>
      <Box x={117} y={240} w={421} h={368} fill={t.cream} />
      <Ph x={118} y={241} w={419} h={194} label="family auto camping photo" />
      <BrownPill x={135} y={449} w={150} h={36} size={26}>{m.name}</BrownPill>
      <Note x={295} cy={466}>{m.note}</Note>
      {m.points.map((p, i) => (
        <div key={p}>
          {m.bullets.includes(i) && <B x={148} cy={511 + i * 24} size={17}>•</B>}
          <B x={165} cy={511 + i * 24} size={17}>{p}</B>
        </div>
      ))}
      {guide.side.map((s, i) => {
        const y = 240 + i * 191
        return (
          <div key={s.name}>
            <Box x={800} y={y} w={362} h={177} fill={t.cream} />
            <Ph x={555} y={y} w={246} h={177} label={`${s.name} photo`} />
            <BrownPill x={832} y={y + 47} w={123} h={36} size={26}>{s.name}</BrownPill>
            <Note x={967} cy={y + 64}>{s.note}</Note>
            <BL x={840} cy0={y + 107 + i * 12} gap={23} size={17} lines={s.lines} />
          </div>
        )
      })}
    </FrameSlide>
  )
}

function Sites() {
  return (
    <FrameSlide tag={sites.tag} title={sites.title}>
      <Ph x={100} y={238} w={392} h={366} label="autumn campsite photo" />
      {sites.cells.map(([h, a, b], i) => {
        const x = 505 + (i % 2) * 346
        const y = 238 + Math.floor(i / 2) * 189
        return (
          <div key={h}>
            <Box x={x} y={y} w={334} h={178} fill={t.cream} />
            <Box x={x} y={y} w={334} h={66} fill={t.brown} border={false} />
            <Txt x={x + 167} cy={y + 33} size={31} align="center" w={334} d={t.brown} style={{ color: '#fff' }}>{h}</Txt>
            <BL x={x + 167} cy0={y + 107} gap={27} size={18} align="center" w={334} lines={[a, b]} />
          </div>
        )
      })}
    </FrameSlide>
  )
}

const checkIcons = [Thermometer, Sunset, CloudRain, Bug, Flame]
function Checks() {
  return (
    <FrameSlide tag={checks.tag} title={checks.title}>
      {checks.items.map(([h, a, b], i) => {
        const x = [85, 309, 532, 755, 981][i]
        const Icon = checkIcons[i]
        return (
          <div key={h}>
            <Box x={x} y={235} w={213} h={377} fill="#fff" />
            <Box x={x} y={495} w={213} h={117} fill={t.cream} />
            <Box x={x} y={235} w={213} h={65} fill={t.brown} border={false} />
            <Txt x={x + 106} cy={268} size={28} align="center" w={213} d={t.brown} style={{ color: '#fff' }}>{h}</Txt>
            <Abs x={x + 46} y={340}><Icon size={120} strokeWidth={1.3} color={t.brown} /></Abs>
            <BL x={x + 106} cy0={536} gap={32} size={22} align="center" w={213} lines={[a, b]} />
            {i < 4 && (
              <Abs x={[303, 526, 749, 975][i] - 11} y={406} w={22} h={22} className="flex items-center justify-center rounded-full bg-white" style={{ border: `1px solid ${t.brown}` }}>
                <ChevronRight size={14} color={t.brown} />
              </Abs>
            )}
          </div>
        )
      })}
    </FrameSlide>
  )
}

function Categories() {
  return (
    <FrameSlide tag={categories.tag} title={categories.title}>
      <Ph x={455} y={248} w={410} h={407} label="camper character" className="rounded-t-[180px]" />
      {categories.items.map((c, i) => {
        const left = i === 0 || i === 2
        const x = left ? 67 : 833
        const y = i < 2 ? 266 : 455
        const fill = i === 1 || i === 2 ? t.pale : t.cream
        return (
          <div key={c.name}>
            <Box x={x} y={y} w={378} h={160} r={20} fill={fill} />
            <Dot cx={x + 363} cy={y + 5} r={20}><Check size={24} strokeWidth={3} /></Dot>
            <Txt x={x + 189} cy={y + 48} size={33} align="center" w={378} d={fill} style={{ color: t.brown }}>{c.name}</Txt>
            <BL x={x + 189} cy0={y + 95} gap={27} size={18} align="center" w={378} lines={c.lines} />
          </div>
        )
      })}
    </FrameSlide>
  )
}

function Sleep() {
  return (
    <FrameSlide bg={t.green} tag={sleep.tag} title={sleep.title}>
      {sleep.items.map((p, i) => {
        const x = 77 + i * 576
        const [ix, iy, iw, ih] = p.img
        return (
          <div key={p.name}>
            <Abs x={x} y={226} w={553} h={402} className="overflow-hidden rounded-[30px] bg-white" style={{ border: `1.5px solid ${t.brown}` }}>
              <div className="absolute bottom-0 left-0 h-[63px] w-full" style={{ background: t.brown }} />
            </Abs>
            <Ph x={ix} y={iy} w={iw} h={ih} label={p.name} />
            <B x={x + 276} cy={498} size={27} align="center" w={553} className="font-bold">{p.name}</B>
            <B x={x + 276} cy={537} size={17} align="center" w={553} style={{ color: t.muted }}>{p.spec}</B>
            <B x={x + 276} cy={594} size={32} align="center" w={553} className="font-bold" style={{ color: '#fff' }}>{p.price}</B>
          </div>
        )
      })}
    </FrameSlide>
  )
}

function Cook() {
  return (
    <FrameSlide bg={t.green} tag={cook.tag} title={cook.title}>
      {[452, 830].map((x) => <Abs key={x} x={x} y={267} w={1.5} h={333} style={{ background: t.brown }} />)}
      {cook.items.map((p, i) => {
        const cx = [263, 642, 1017][i]
        const [ix, iy, iw, ih] = p.img
        return (
          <div key={p.name}>
            <Ph x={ix} y={iy} w={iw} h={ih} label={p.name} />
            <B x={cx} cy={509} size={26} align="center" w={380} className="font-bold">{p.name}</B>
            <B x={cx} cy={540} size={16} align="center" w={380} style={{ color: t.muted }}>{p.spec}</B>
            <Box x={cx - 168} y={567} w={336} h={32} fill={t.brown} border={false} />
            <B x={cx} cy={583} size={24} align="center" w={336} className="font-semibold" style={{ color: '#fff' }}>{p.price}</B>
          </div>
        )
      })}
    </FrameSlide>
  )
}

function Warm() {
  return (
    <FrameSlide bg={t.green} tag={warm.tag} title={warm.title}>
      {warm.items.map((p, i) => {
        const x = 93 + i * 278.5
        const cx = x + 129
        return (
          <div key={p.name}>
            <Box x={x} y={243} w={258} h={219} r={20} />
            <Ph x={x + 40} y={255} w={178} h={195} label={p.name} />
            <Abs x={cx - 0.75} y={462} w={1.5} h={30} style={{ background: t.brown }} />
            <Box x={cx - 115} y={492} w={230} h={44} r={22} />
            <B x={cx} cy={514} size={24} align="center" w={258} className="font-bold">{p.name}</B>
            <B x={cx} cy={560} size={16} align="center" w={258} style={{ color: t.muted }}>{p.spec}</B>
            <B x={cx} cy={596} size={30} align="center" w={258} className="font-bold">{p.price}</B>
          </div>
        )
      })}
    </FrameSlide>
  )
}

function Sets() {
  return (
    <FrameSlide bg={t.green} tag={sets.tag} title={sets.title}>
      <Abs x={639} y={260} w={1.5} h={355} style={{ background: t.rule }} />
      {sets.items.map((s, i) => {
        const x = 120 + i * 555
        const [ix, iy, iw, ih] = s.img
        return (
          <div key={s.name}>
            <Ph x={ix} y={iy} w={iw} h={ih} label={s.name} />
            <Abs x={x} y={487} w={480} h={1.5} style={{ background: t.rule }} />
            <B x={x} cy={521} size={29} className="font-bold">{s.name}</B>
            <BL x={x} cy0={565} gap={24} size={17} lines={s.spec} style={{ color: t.muted }} />
            <Box x={x + 313} y={538} w={170} h={38} r={19} fill={t.brown} border={false} />
            <B x={x + 398} cy={557} size={28} align="center" w={170} className="font-bold" style={{ color: '#fff' }}>{s.price}</B>
          </div>
        )
      })}
    </FrameSlide>
  )
}

function Manners() {
  return (
    <FrameSlide bg={t.green} tag={manners.tag} title={manners.title}>
      {manners.items.map(([h, a, b], i) => {
        const x = [82, 462, 844][i]
        return (
          <div key={h}>
            <Box x={x} y={245} w={355} h={151} r={16} fill={t.brown} border={false} />
            <B x={x + 177} cy={282} size={25} align="center" w={355} className="font-bold" style={{ color: '#fff' }}>{h}</B>
            <Abs x={x + 20} y={310} w={315} h={1.5} className="bg-white" />
            <BL x={x + 177} cy0={338} gap={21} size={16} align="center" w={355} lines={[a, b]} style={{ color: '#fff' }} />
            <Box x={x} y={400} w={355} h={212} r={16} fill={t.cream} />
            <Ph x={x + 70} y={410} w={215} h={195} label="line illustration" />
          </div>
        )
      })}
    </FrameSlide>
  )
}

const contactIcons = [Store, Phone, MonitorSmartphone, MessagesSquare]
function Closing() {
  return (
    <Slide background={t.cream} style={{ color: t.brown }}>
      <Abs x={0} y={682} w={1280} h={38} style={{ background: t.green }} />
      <Ph x={0} y={565} w={330} h={155} label="trees and campfire" />
      <Ph x={950} y={540} w={330} h={180} label="tent and trees" />
      <Box x={62} y={112} w={1156} h={470} r={60} style={{ borderWidth: 2 }} />
      <Tag x={400} y={72} w={480} h={65}>{''}</Tag>
      <Logo x={543} cy={102} size={22} />
      {closing.title.map((l, i) => <Txt key={l} x={640} cy={222 + i * 90} size={74} align="center" d style={{ color: t.brown }}>{l}</Txt>)}
      <B x={640} cy={400} size={19} align="center">{closing.sub}</B>
      <Abs x={168} y={439} w={944} h={1} style={{ background: t.rule }} />
      {closing.contacts.map(([l, v], i) => {
        const cx = 183 + i * 250
        const Icon = contactIcons[i]
        return (
          <div key={l}>
            <Dot cx={cx} cy={487} r={23}><Icon size={24} strokeWidth={1.8} /></Dot>
            <B x={cx + 42} cy={472} size={19}>{l}</B>
            <B x={cx + 42} cy={502} size={19}>{v}</B>
          </div>
        )
      })}
    </Slide>
  )
}

const deck: DeckDefinition = {
  id: '30',
  title: '연두 미니멀 캠핑생활 안내',
  slides: [Cover, Intro, Toc, Types, Guide, Sites, Checks, Categories, Sleep, Cook, Warm, Sets, Manners, Closing],
}
export default deck
