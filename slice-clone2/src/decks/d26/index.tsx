import { CircleCheck, MapPin, MousePointer2, Phone, Sprout, Star } from 'lucide-react'
import type { DeckDefinition } from '../../ui'
import { Abs } from '../../ui'
import { Caption, CreamSlide, FieldSlide, Frame, Ph, Pill, SideTitle, Txt } from './components'
import { center, checklist, compare, courses, cover, faq, managers, products, roadmap, stories, thanks, toc, trend, venn } from './data'
import { t } from './theme'

const W = '#fff'

/** Shared layout for the cover and the closing slide. */
function Hero({ top, footer, pill, children }: { top: string; footer: string; pill: string; children: React.ReactNode }) {
  return (
    <FieldSlide>
      <Txt x={640} cy={67} size={17} align="center" w={600} className="font-bold" style={{ color: W }}>{top}</Txt>
      {children}
      <Pill cx={638} cy={526} w={509} h={69} bg={t.orange} size={21} className="font-semibold" >{pill}</Pill>
      <Txt x={640} cy={655} size={17} align="center" w={600} className="font-semibold" style={{ color: W }}>{footer}</Txt>
    </FieldSlide>
  )
}

function Cover() {
  return (
    <Hero top={cover.top} footer={cover.footer} pill={cover.pill}>
      <Ph x={0} y={0} w={330} h={560} label="farmers and apple tree illustration" />
      <Ph x={940} y={30} w={340} h={640} label="greenhouse, farmers and cow illustration" />
      <Frame x={294} y={193} w={691} h={330} border={t.green} r={18} />
      <Txt x={386} cy={350} size={158} lh={100} className="font-jua" style={{ color: t.brown }}>{cover.title[0]}</Txt>
      <Txt x={652} cy={340} size={158} lh={100} className="font-jua" style={{ color: t.greenText }}>{cover.title[1]}</Txt>
      <Txt x={632} cy={423} size={35} lh={40} className="font-medium" style={{ color: t.brown }}>{cover.sub}</Txt>
    </Hero>
  )
}

function Toc() {
  return (
    <CreamSlide>
      <SideTitle part={toc.part} lines={toc.lines} />
      <Ph x={0} y={309} w={403} h={326} label="farmer with vegetables illustration" />
      {toc.items.map((it, i) => (
        <Frame key={it} x={621} y={135 + i * 101} w={565} h={83}>
          <Abs x={50} y={22} w={36} h={36} className="flex items-center justify-center rounded-full font-semibold" style={{ background: t.green, color: W, fontSize: 14 }}>{i + 1}</Abs>
          <Txt x={104} cy={39} size={21} className="font-medium">{it}</Txt>
        </Frame>
      ))}
    </CreamSlide>
  )
}

function Cylinder({ x, top, base, w, body, cap }: { x: number; top: number; base: number; w: number; body: string; cap: string }) {
  const eh = 64
  return (
    <>
      <Abs x={x} y={top + eh / 2} w={w} h={base - top - eh / 2} style={{ background: body }} />
      <Abs x={x} y={base - eh / 2} w={w} h={eh} className="rounded-[50%]" style={{ background: body }} />
      <Abs x={x} y={top} w={w} h={eh} className="rounded-[50%]" style={{ background: cap }} />
    </>
  )
}

function Trend() {
  return (
    <CreamSlide>
      <SideTitle part={trend.part} lines={trend.lines} />
      <Ph x={113} y={386} w={76} h={89} label="chicken illustration" />
      <Frame x={91} y={461} w={286} h={167}>
        {trend.note.map((l, i) => <Txt key={l} x={25} cy={39 + i * 27.5} size={17} className={i === 3 ? 'font-bold' : ''}>{l}</Txt>)}
      </Frame>
      <Caption x={464} cy={148}>{trend.caption}</Caption>
      <Ph x={445} y={575} w={766} h={70} label="grass ground" className="rounded-[50%]" />
      {trend.bars.map((b, i) => {
        const x = 480 + i * 240, last = i === 2
        return (
          <div key={b.v}>
            <Cylinder x={x} top={b.top} base={600} w={212} body={last ? t.orange : t.green} cap={last ? '#f6a062' : '#a2cc77'} />
            <Ph x={x + 56} y={b.top - 160} w={100} h={190} label="farmer illustration" />
            <Txt x={x + 106} cy={[536, 513, 452][i]} size={36} align="center" w={200} className="font-bold" style={{ color: W }}>{b.v}</Txt>
            <Txt x={x + 106} cy={[570, 547, 490][i]} size={14} align="center" w={200} style={{ color: W }}>{b.y}</Txt>
          </div>
        )
      })}
    </CreamSlide>
  )
}

function Compare() {
  const xs = [463, 760, 893], ws = [297, 133, 296]
  return (
    <CreamSlide>
      <SideTitle part={compare.part} lines={compare.lines} />
      <Ph x={90} y={480} w={290} h={150} label="farmer with basket illustration" />
      <Caption x={464} cy={148}>{compare.caption}</Caption>
      {[0, 2].map((c) => (
        <Abs key={c} x={xs[c]} y={209} w={ws[c]} h={64} className="flex items-center justify-center font-bold" style={{ background: t.green, color: W, fontSize: 21, borderRadius: '22px 22px 0 0' }}>{compare.heads[c]}</Abs>
      ))}
      <Txt x={827} cy={241} size={22} align="center" w={120} className="font-bold" style={{ color: t.brown }}>{compare.heads[1]}</Txt>
      <Abs x={760} y={273} w={133} h={357} style={{ background: t.brownCell }} />
      {compare.rows.map((r, ri) => (
        <div key={ri}>
          <Abs x={463} y={273 + ri * 71.4} w={726} h={71.4} style={{ background: 'transparent', borderBottom: '2px solid #e4e4dc' }} />
          {r.map((c, ci) => (
            <Txt key={ci} x={xs[ci] + ws[ci] / 2} cy={309 + ri * 71.4} size={ci === 1 ? 17 : 16} align="center" w={ws[ci]} className={ci === 1 ? 'font-bold' : ''} style={{ color: ci === 1 ? W : '#444' }}>{c}</Txt>
          ))}
        </div>
      ))}
    </CreamSlide>
  )
}

function Roadmap() {
  return (
    <CreamSlide>
      <SideTitle part={roadmap.part} lines={roadmap.lines} cy={177} size={56} lh={58} />
      <Ph x={756} y={108} w={460} h={196} label="farmer with wheelbarrow illustration" />
      <Ph x={0} y={370} w={170} h={40} label="dashed road" />
      <Ph x={1130} y={530} w={150} h={70} label="dashed road" />
      {roadmap.steps.map(([title, text], i) => {
        const cx = 174 + i * 155, low = i % 2 === 0, cy = low ? 490 : 442, last = i === 6
        const ring = last ? t.orange : low ? t.green : t.line
        const tc = last ? t.orange : low ? t.brown : t.greenText
        return (
          <div key={title}>
            <Abs x={cx - 83} y={cy - 83} w={166} h={166} className="rounded-full bg-white" style={{ border: `6px solid ${ring}` }} />
            <Abs x={cx - 19} y={cy - 102} w={38} h={38} className="flex items-center justify-center rounded-full font-semibold" style={{ background: ring, color: W, fontSize: 13 }}>{`0${i + 1}`}</Abs>
            <Txt x={cx} cy={cy - 24} size={22} align="center" w={150} className="font-black" style={{ color: tc }}>{title}</Txt>
            <Txt x={cx} cy={cy + 10} size={15} lh={20} align="center" w={150}>{text}</Txt>
          </div>
        )
      })}
    </CreamSlide>
  )
}

function Venn() {
  return (
    <CreamSlide>
      <SideTitle part={venn.part} lines={venn.lines} cy={181} size={52} lh={56.5} />
      <Ph x={400} y={420} w={160} h={160} label="chicken illustration" />
      <Ph x={1058} y={130} w={130} h={115} label="cow illustration" />
      <Frame x={91} y={439} w={286} h={189}>
        {venn.note.map((l, i) => <Txt key={l} x={25} cy={40 + i * 27.3} size={17}>{l}</Txt>)}
      </Frame>
      {venn.sets.map((s) => <Abs key={s.tag} x={s.cx - 151} y={s.cy - 151} w={302} h={302} className="rounded-full" style={{ background: 'rgba(196,220,165,0.55)', border: `2px solid ${t.band}` }} />)}
      {venn.sets.map((s, i) => (
        <div key={s.tag}>
          <Pill cx={s.cx} cy={s.vy - 44} w={90} h={30} bg={t.orange} size={12}>{s.tag}</Pill>
          <Txt x={s.cx} cy={s.vy} size={34} align="center" w={200} className="font-black" style={{ color: t.brown }}>{s.v}</Txt>
          <Txt x={s.cx} cy={s.vy + 38} size={14.5} lh={20} align="center" w={260} style={{ color: t.text }}>{s.text}</Txt>
          {i === 0 && null}
        </div>
      ))}
      <Abs x={755} y={319} w={160} h={160} className="rounded-full bg-white" style={{ border: `5px solid ${t.green}` }} />
      <Abs x={821} y={337}><Sprout size={28} color={t.green} strokeWidth={2.6} /></Abs>
      <Txt x={835} cy={393} size={22} align="center" w={150} className="font-black" style={{ color: t.greenText }}>{venn.center[0]}</Txt>
      <Txt x={835} cy={421} size={14} lh={19} align="center" w={150}>{venn.center[1]}</Txt>
    </CreamSlide>
  )
}

function Products() {
  return (
    <CreamSlide>
      <SideTitle part={products.part} lines={products.lines} cy={178} size={52} lh={57} />
      <Ph x={0} y={420} w={400} h={225} label="farmer holding basket illustration" />
      {products.items.map((p, i) => {
        const x = 464 + (i % 2) * 373, y = 135 + Math.floor(i / 2) * 257
        return (
          <Frame key={p.title} x={x} y={y} w={351} h={236} r={12}>
            <Txt x={32} cy={45} size={24} className="font-black" style={{ color: t.brown }}>{p.title}</Txt>
            <Pill cx={113} cy={88} w={161} h={32} size={12}>{p.tag}</Pill>
            <Txt x={32} cy={142} size={15} lh={24}>{p.text}</Txt>
            <Ph x={243} y={20} w={78} h={100} label="fruit illustration" />
          </Frame>
        )
      })}
    </CreamSlide>
  )
}

function Courses() {
  return (
    <CreamSlide>
      <SideTitle part={courses.part} lines={courses.lines} cy={178} size={52} lh={57} />
      <Ph x={90} y={430} w={220} h={200} label="farmers illustration" />
      <Abs x={26} y={623} w={1226} h={5} style={{ background: t.line }} />
      {courses.items.map((c, i) => {
        const x = 409 + i * 267, cx = x + 122
        return (
          <div key={c.title}>
            <Abs x={cx - 2} y={567} w={4} h={58} style={{ background: t.green }} />
            <Abs x={cx - 8} y={617} w={16} h={16} className="rounded-full" style={{ background: t.green }} />
            <Frame x={x} y={132} w={245} h={435} r={10}>
              <Ph x={0} y={0} w={239} h={172} label="education photo" className="rounded-t-[8px]" />
              <Txt x={26} cy={203} size={21} className="font-black" style={{ color: t.brown }}>{c.title}</Txt>
              <Txt x={26} cy={240} size={14.5} lh={23}>{c.text}</Txt>
              <Pill cx={120} cy={386} w={186} h={32} bg={t.soft} color={t.text} size={12}>{c.hours}</Pill>
            </Frame>
            <Pill cx={cx} cy={133} w={72} h={30} size={12}>{c.level}</Pill>
          </div>
        )
      })}
      <Txt x={1189} cy={653} size={9} align="right" w={300} style={{ color: '#888' }}>{courses.note}</Txt>
    </CreamSlide>
  )
}

function Stories() {
  return (
    <FieldSlide>
      <SideTitle part={stories.part} lines={stories.lines} cy={135} size={52} lh={57} light />
      <Ph x={0} y={320} w={370} h={320} label="farmers illustration" />
      {stories.items.map((s, i) => {
        const x = 416 + (i % 2) * 394, y = 84 + Math.floor(i / 2) * 289
        return (
          <Frame key={s.name} x={x} y={y} w={377} h={264} border={t.green}>
            <Txt x={35} cy={46} size={22} className="font-black" style={{ color: t.brown }}>{s.name}</Txt>
            <Abs x={35} y={66} className="flex gap-[2px]">{[0, 1, 2, 3, 4].map((k) => <Star key={k} size={13} fill={t.orange} color={t.orange} />)}</Abs>
            <Ph x={225} y={14} w={128} h={128} label="portrait photo" className="rounded-full" />
            <Pill cx={122} cy={133} w={175} h={32} bg={t.soft} color={t.text} size={11}>{s.tag}</Pill>
            <Txt x={35} cy={173} size={15} lh={24}>{s.text}</Txt>
          </Frame>
        )
      })}
      <Txt x={1189} cy={655} size={9} align="right" w={300} style={{ color: W }}>{courses.note}</Txt>
    </FieldSlide>
  )
}

function Checklist() {
  return (
    <FieldSlide>
      <SideTitle part={checklist.part} lines={checklist.lines} cy={135} size={52} lh={57} light />
      <Ph x={0} y={330} w={370} h={340} label="cow and farmer illustration" />
      {checklist.items.map((c, i) => (
        <Frame key={c} x={410} y={84 + i * 113} w={775} h={90} border={t.green}>
          <Abs x={51} y={30}><CircleCheck size={26} fill={t.orange} color={W} strokeWidth={2.4} /></Abs>
          <Txt x={90} cy={42} size={21} className="font-medium">{c}</Txt>
        </Frame>
      ))}
    </FieldSlide>
  )
}

function Managers() {
  return (
    <CreamSlide>
      <SideTitle part={managers.part} lines={managers.lines} cy={178} size={52} lh={57} />
      <Ph x={90} y={420} w={260} h={220} label="farmer with mushrooms illustration" />
      {managers.items.map((m, i) => {
        const x = 409 + i * 267, cx = x + 122
        return (
          <div key={m.name}>
            <Frame x={x} y={193} w={245} h={435} r={12} border={t.band} />
            <Abs x={cx - 75} y={137} w={150} h={150} className="overflow-hidden rounded-full" style={{ border: `4px solid ${t.green}` }}><Ph x={0} y={0} w={142} h={142} label="portrait photo" /></Abs>
            <Pill cx={cx} cy={336} w={116} h={32} size={12}>{m.tag}</Pill>
            <Txt x={cx} cy={376} size={22} align="center" w={240} className="font-black" style={{ color: t.brown }}>{m.name}</Txt>
            <Txt x={cx} cy={403} size={14} align="center" w={240}>{m.dept}</Txt>
            <Abs x={x + 32} y={435} w={181} h={2} style={{ background: t.soft }} />
            <Abs x={x + 30} y={464} w={200} className="flex flex-col gap-0" style={{ fontSize: 15, lineHeight: '23px' }}>
              {m.bullets.map((b) => <div key={b} className="relative whitespace-pre-line pl-[18px]"><span className="absolute left-[2px] top-[9px] h-[6px] w-[6px] rounded-full" style={{ background: t.text }} />{b}</div>)}
            </Abs>
          </div>
        )
      })}
      <Txt x={1189} cy={653} size={9} align="right" w={300} style={{ color: '#888' }}>{courses.note}</Txt>
    </CreamSlide>
  )
}

function Faq() {
  return (
    <CreamSlide>
      <SideTitle part={faq.part} lines={faq.lines} cy={178} size={52} lh={57} />
      <Txt x={88} cy={509} size={82} className="font-montserrat font-black tracking-[-0.03em]" style={{ color: t.greenText }}>QNA</Txt>
      <Ph x={0} y={600} w={370} h={70} label="grass ground" className="rounded-[50%]" />
      {faq.items.map((f, i) => (
        <Frame key={f.q} x={410} y={136 + i * 169} w={776} h={145}>
          <Abs x={46} y={34} w={30} h={30} className="flex items-center justify-center rounded-full font-black" style={{ background: t.orange, color: W, fontSize: 16 }}>Q</Abs>
          <Txt x={86} cy={49} size={22} className="font-black tracking-[-0.02em]" style={{ color: t.brown }}>{f.q}</Txt>
          <Txt x={43} cy={90} size={15} lh={23}>{f.a}</Txt>
        </Frame>
      ))}
    </CreamSlide>
  )
}

function Center() {
  const icons = [Phone, MapPin, MousePointer2]
  return (
    <FieldSlide>
      <SideTitle part={center.part} lines={center.lines} cy={137} size={52} lh={57.5} light />
      <Ph x={0} y={300} w={530} h={340} label="farmer, chickens and tree illustration" />
      <Abs x={538} y={100} w={652} h={387} className="overflow-hidden" style={{ border: `4px solid ${W}`, borderRadius: 18 }}><Ph x={0} y={0} w={644} h={379} label="street map illustration" /></Abs>
      <Abs x={893} y={270}><MapPin size={44} fill={t.orange} color={W} strokeWidth={1.6} /></Abs>
      <Pill cx={915} cy={349} w={172} h={38} size={14} className="font-semibold">{center.pin}</Pill>
      {center.contacts.map((c, i) => {
        const I = icons[i]
        return (
          <div key={c}>
            <Abs x={537} y={523 + i * 43} w={30} h={30} className="flex items-center justify-center rounded-full" style={{ background: t.orange }}><I size={16} color={W} fill={i === 2 ? W : 'none'} /></Abs>
            <Txt x={578} cy={538 + i * 43} size={19} className="font-semibold" style={{ color: W }}>{c}</Txt>
          </div>
        )
      })}
      <Abs x={1072} y={523} w={117} h={117} className="rounded-[8px] bg-white p-[14px]"><Ph x={14} y={14} w={89} h={89} label="QR code" /></Abs>
    </FieldSlide>
  )
}

function Thanks() {
  return (
    <Hero top={thanks.top} footer={thanks.footer} pill={thanks.pill}>
      <Ph x={110} y={110} w={250} h={520} label="chicken and farmer illustration" />
      <Ph x={960} y={120} w={290} h={590} label="farmers and chickens illustration" />
      <Frame x={312} y={172} w={656} h={325} border={t.green} r={18} />
      <Txt x={630} cy={284} size={158} lh={120} align="center" w={600} className="font-jua" style={{ color: t.brown }}>{thanks.title[0]}</Txt>
      <Txt x={566} cy={395} size={150} lh={100} align="center" w={300} className="font-jua" style={{ color: t.greenText }}>{thanks.title[1]}</Txt>
      <Txt x={710} cy={378} size={27} lh={35} className="font-medium" style={{ color: t.brown }}>{thanks.side}</Txt>
    </Hero>
  )
}

const deck: DeckDefinition = {
  id: '26',
  title: '초록 심플 귀농귀촌 안내',
  slides: [Cover, Toc, Trend, Compare, Roadmap, Venn, Products, Courses, Stories, Checklist, Managers, Faq, Center, Thanks],
}
export default deck
