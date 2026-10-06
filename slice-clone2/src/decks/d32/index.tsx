import type { DeckDefinition } from '../../ui'
import { Abs, Slide, cn } from '../../ui'
import { CircleParking, Truck } from 'lucide-react'
import { Box, Lines, Oval, Page, Ph, Txt } from './components'
import { accessories, best, categories, concept, contact, contents, cover, detail, features, lineup, lookbook, promo, section, styling } from './data'
import { t } from './theme'

const L = t.latin
const PHOTO_DARK = '#4a5a47'

/** Background photo + rounded light card with a photo on the right (cover and contact). */
function CardSlide({ children }: { children: React.ReactNode }) {
  return (
    <Slide background={t.bg} style={{ color: t.ink }}>
      <Ph x={0} y={0} w={1280} h={720} label="grass background photo" />
      <Box x={104} y={75} w={1072} h={565} r={16} fill="#f6f6f4" />
      {children}
      <Txt x={1265} cy={698} size={10} align="right" w={300} style={{ color: '#fff' }}>{t.chrome.note}</Txt>
    </Slide>
  )
}

function Cover() {
  return (
    <CardSlide>
      <Ph x={658} y={85} w={510} h={545} label="female golfer photo" tone="#d6d8d3" className="rounded-[12px]" />
      <Oval cx={384} cy={197} w={148} h={50} border={t.ink} size={20}>{cover.season}</Oval>
      <Txt x={384} cy={288} size={80} align="center" w={600} className={cn(L, 'font-semibold tracking-[-0.03em]')} style={{ color: t.green }}>{cover.brand}</Txt>
      <Txt x={392} cy={368} size={96} align="center" w={600} className={t.script} style={{ color: t.green }}>{cover.script}</Txt>
      <Lines x={382} cy0={456} gap={30} size={20} align="center" w={500} lines={cover.lines} />
      <Ph x={336} y={562} w={100} h={38} label="MIRI golf logo" />
      <Abs x={1112} y={110} w={40} h={350} className={cn(t.serif, 'flex flex-col whitespace-nowrap leading-tight')} style={{ writingMode: 'vertical-rl', color: '#fff', fontSize: 15 }}>
        <span>{cover.side[0]}</span>
      </Abs>
      <Abs x={1092} y={110} w={22} h={350} className="flex flex-col whitespace-nowrap leading-tight" style={{ writingMode: 'vertical-rl', color: '#fff', fontSize: 6.5 }}>
        <span>{cover.side[1]}</span><span>{cover.side[2]}</span>
      </Abs>
    </CardSlide>
  )
}

function Contents() {
  return (
    <Slide background={t.bg} style={{ color: t.ink }}>
      <Box x={0} y={0} w={320} h={720} fill="#fff" />
      <Ph x={320} y={606} w={960} h={114} label="golf course photo" />
      <Abs x={45} y={40} w={110} h={540} className="flex items-center whitespace-nowrap leading-none" style={{ writingMode: 'sideways-lr', color: t.green }}>
        <span className={t.script} style={{ fontSize: 150 }}>C</span>
        <span className={cn(L, 'font-semibold tracking-[-0.02em]')} style={{ fontSize: 98 }}>ontents</span>
      </Abs>
      <Txt x={47} cy={636} size={14} className={t.serif} style={{ color: '#555' }}>{contents.blurb.title}</Txt>
      <Lines x={47} cy0={654} gap={11} size={8} lines={contents.blurb.lines} style={{ color: '#c4c4c4' }} />
      {contents.cols.map((c, ci) => {
        const x = 375 + ci * 319
        return (
          <div key={c.no}>
            <Txt x={x} cy={86} size={52} className={cn(t.serif, 'italic')} style={{ color: '#d4d4d2' }}>{c.no}</Txt>
            <Txt x={x} cy={158} size={32} className="font-semibold" style={{ color: t.green }}>{c.title}</Txt>
            {c.items.map(([kr, en], i) => {
              const cy = 239 + i * 58.3
              return (
                <div key={kr}>
                  <Txt x={x} cy={cy} size={19} className="font-semibold">{kr}</Txt>
                  <Txt x={x} cy={cy + 22} size={13.5} className={L} style={{ color: t.muted }}>{en}</Txt>
                  <Box x={x + 142} y={cy} w={45} h={1} fill={t.rule} />
                  <Txt x={x + 220} cy={cy} size={14} align="right" w={60} className={L} style={{ color: t.muted }}>{contents.page}</Txt>
                </div>
              )
            })}
          </div>
        )
      })}
    </Slide>
  )
}

function Concept() {
  return (
    <Page no="01" caption="Season Concept" ink="#fff" rule="rgba(255,255,255,0.25)" under={<Ph x={0} y={0} w={1280} h={720} label="golf ball near hole photo" tone={PHOTO_DARK} />}>
      {concept.words.map((w, i) => (
        <Txt key={w} x={92} cy={397 + i * 90} size={84} className={cn(L, 'font-light tracking-[-0.02em]')} style={{ color: i === 2 ? '#7f9a7a' : '#fff' }}>{w}</Txt>
      ))}
      <Txt x={502} cy={487} size={31} className="font-bold" style={{ color: '#fff' }}>{concept.lead}</Txt>
      <Lines x={502} cy0={542} gap={29.5} size={19} lines={concept.body} style={{ color: '#fff' }} />
    </Page>
  )
}

function Lookbook() {
  return (
    <Page no="02" caption="Season Lookbook" note>
      <Lines x={640} cy0={155} gap={44} size={30} align="center" lines={lookbook.lines} className="font-semibold" />
      {[40, 343, 647, 950].map((x) => <Ph key={x} x={x} y={267} w={290} h={413} label="lookbook photo" className="rounded-[18px]" />)}
    </Page>
  )
}

function Features() {
  return (
    <Page no="03" caption="Collection Features" under={<Ph x={0} y={500} w={1280} h={220} label="golf course photo" />}>
      <Lines x={53} cy0={155} gap={43} size={30} lines={features.lead} className="font-semibold" />
      <Lines x={53} cy0={302} gap={27} size={17} lines={features.body} />
      {features.points.map((p, i) => {
        const x = i % 2 ? 850 : 446
        const y = i < 2 ? 121 : 407
        const dark = i === 0
        return (
          <div key={p.en}>
            <Box x={x} y={y} w={390} h={272} r={16} fill={dark ? t.green : '#fff'} />
            <Oval cx={x + 76} cy={y + 49} w={88} h={30} fill={dark ? undefined : t.green} border={dark ? '#fff' : undefined} color="#fff" size={11}>{`POINT 0${i + 1}`}</Oval>
            <Lines x={x + 33} cy0={y + 141} gap={35} size={26} lines={p.kr} className="font-semibold" style={{ color: dark ? '#fff' : t.ink }} />
            <Txt x={x + 33} cy={y + 220} size={18} className={L} style={{ color: dark ? '#6d886a' : '#c2c2c2' }}>{p.en}</Txt>
          </div>
        )
      })}
    </Page>
  )
}

function Categories() {
  return (
    <Page no="04" caption="Product Categories">
      <Lines x={640} cy0={155} gap={43} size={30} align="center" lines={categories.lead} className="font-semibold" />
      {categories.items.map(([en, kr, d], i) => {
        const x = [40, 444, 850][i % 3]
        const y = i < 3 ? 268 : 480
        const dark = i === 0
        return (
          <div key={en}>
            <Box x={x} y={y} w={390} h={198} r={18} fill={dark ? t.green : t.cardGray} style={dark ? undefined : { background: '#ebebe8' }} />
            <Ph x={x + 245} y={y + 22} w={120} h={176} label={`${en} image`} />
            <Txt x={x + 34} cy={y + 50} size={27} className={cn(L, 'font-semibold')} style={{ color: dark ? '#fff' : t.ink }}>{en}</Txt>
            <Txt x={x + 34} cy={y + 82} size={17} style={{ color: dark ? '#fff' : t.ink }}>{kr}</Txt>
            <Txt x={x + 34} cy={y + 154} size={14} style={{ color: dark ? '#7f9a7a' : t.muted }}>{d}</Txt>
          </div>
        )
      })}
    </Page>
  )
}

function Section() {
  return (
    <Page bg={t.green} ink="#fff" rule={false}>
      <Ph x={40} y={80} w={1200} h={168} label="putting green photo" className="rounded-[18px]" />
      <Txt x={48} cy={556} size={200} className={t.script} style={{ color: '#f3eed0' }}>{section.cap}</Txt>
      <Txt x={196} cy={606} size={84} className={cn(L, 'font-light tracking-[-0.02em]')} style={{ color: '#fff' }}>{section.rest}</Txt>
      {section.items.map(([kr, en], i) => {
        const cy = 375 + i * 58.3
        return (
          <div key={kr}>
            <Txt x={973} cy={cy} size={20} className="font-semibold" style={{ color: '#fff' }}>{kr}</Txt>
            <Txt x={973} cy={cy + 22} size={13} className={L} style={{ color: '#fff' }}>{en}</Txt>
            <Box x={1105} y={cy} w={60} h={1} fill="rgba(255,255,255,0.25)" />
            <Txt x={1200} cy={cy} size={14} align="right" w={60} className={L} style={{ color: '#fff' }}>{section.page}</Txt>
          </div>
        )
      })}
    </Page>
  )
}

function Best() {
  return (
    <Page no="05" caption="Best Sellers" bg="#e3e4df">
      <Txt x={640} cy={155} size={30} align="center" className="font-semibold">{best.lead}</Txt>
      {best.items.map((b, i) => {
        const x = 40 + i * 405
        return (
          <div key={b.en}>
            <Box x={x} y={222} w={390} h={458} r={18} fill="#fff" />
            <Oval cx={x + 70} cy={266} w={88} h={30} fill={t.green} color="#fff" size={11}>{`BEST 0${i + 1}`}</Oval>
            <Ph x={x + 75} y={290} w={240} h={140} label={`${b.en} image`} />
            <Txt x={x + 34} cy={467} size={21} className={cn(L, 'font-semibold')}>{b.en}</Txt>
            <Txt x={x + 34} cy={493} size={15} className="font-medium">{b.kr}</Txt>
            <Txt x={x + 34} cy={530} size={22} className={cn(L, 'font-medium')}>{b.price}</Txt>
            <Box x={x + 34} y={565} w={322} h={1} fill={t.rule} />
            {b.points.map((p, j) => <Txt key={p} x={x + 34} cy={590 + j * 22.5} size={16}>{`•  ${p}`}</Txt>)}
          </div>
        )
      })}
    </Page>
  )
}

function Lineup() {
  const cx = [481, 710, 884, 1027, 1177]
  return (
    <Page no="06" caption="Product Lineup">
      <Txt x={53} cy={182} size={66} className={cn(L, 'font-medium tracking-[-0.02em]')} style={{ color: t.accent }}>{lineup.title[0]}</Txt>
      <Txt x={53} cy={258} size={66} className={cn(L, 'font-semibold tracking-[-0.02em]')}>{lineup.title[1]}</Txt>
      <Lines x={53} cy0={547} gap={26.7} size={17} lines={lineup.body} />
      <Box x={452} y={123} w={784} h={40} r={10} fill="#fff" />
      {lineup.head.map((h, i) => <Txt key={h} x={i ? [0, 667, 884, 1027, 1177][i] : 465} cy={142} size={13.5} align={i ? 'center' : 'left'} w={i ? 200 : 60} className="font-semibold">{h}</Txt>)}
      {lineup.rows.map(([name, play, feat, price], i) => {
        const y = 170 + i * 85.7
        const cy = y + 39
        return (
          <div key={name}>
            <Box x={452} y={y} w={784} h={78} r={10} fill="#e3e3e1" />
            <Ph x={522} y={y + 8} w={52} h={62} label="club image" />
            <Txt x={cx[0]} cy={cy} size={14} align="center" w={30} className={cn(L, 'font-medium')}>{String(i + 1)}</Txt>
            <Txt x={cx[1]} cy={cy} size={15.5} align="center" w={220} className={cn(L, 'font-semibold')}>{name}</Txt>
            <Txt x={cx[2]} cy={cy} size={14} align="center" w={120}>{play}</Txt>
            <Lines x={cx[3]} cy0={cy - 10} gap={20} size={13.5} align="center" w={180} lines={feat} />
            <Txt x={cx[4]} cy={cy} size={15.5} align="center" w={130} className={cn(L, 'font-semibold')}>{price}</Txt>
          </div>
        )
      })}
    </Page>
  )
}

function Detail() {
  const d = detail
  return (
    <Page no="07" caption="Product Detail" bg="#fff">
      <Box x={40} y={121} w={390} h={558} r={16} fill={t.green} />
      <Ph x={40} y={121} w={390} h={310} label="driver photo" className="rounded-t-[16px]" />
      <Lines x={80} cy0={467} gap={45} size={34} lines={d.card.lead} className="font-bold" style={{ color: '#fff' }} />
      <Lines x={80} cy0={570} gap={22.5} size={15} lines={d.card.body} style={{ color: '#fff' }} />
      <Txt x={471} cy={157} size={50} className={cn(L, 'font-semibold tracking-[-0.01em]')}>{d.name}</Txt>
      <Txt x={471} cy={211} size={25} className="font-medium">{d.kr}</Txt>
      <Txt x={1238} cy={174} size={15} align="right" w={120}>{d.priceLabel}</Txt>
      <Txt x={1238} cy={208} size={33} align="right" w={300} className={cn(L, 'font-semibold')}>{d.price}</Txt>
      <Box x={476} y={256} w={760} h={1} fill="#bdbdbd" />
      <Txt x={471} cy={302} size={17} className={cn(L, 'font-semibold')}>{d.key[0]}</Txt>
      <Txt x={471} cy={325} size={13}>{d.key[1]}</Txt>
      {d.features.map(([h, desc], i) => (
        <div key={h}>
          <Oval cx={668} cy={318 + i * 93} w={56} h={32} fill={t.green} color="#fff" size={13}>{`0${i + 1}`}</Oval>
          <Txt x={717} cy={305 + i * 93} size={19} className={cn(L, 'font-medium')}>{h}</Txt>
          <Txt x={717} cy={327 + i * 93} size={13.5} style={{ color: t.muted }}>{desc}</Txt>
          {i < 2 && <Box x={644} y={355 + i * 93} w={592} h={1} fill="#e5e5e5" />}
        </div>
      ))}
      <Lines x={471} cy0={602} gap={22} size={17} lines={d.spec.slice(0, 2)} className={cn(L, 'font-semibold')} />
      <Txt x={471} cy={649} size={13}>{d.spec[2]}</Txt>
      <Box x={640} y={590} w={600} h={92} r={8} fill={t.bg} />
      <Box x={640} y={590} w={600} h={36} r={8} fill="#e8e8e5" />
      {d.specs.map(([k, v], i) => (
        <div key={k}>
          <Txt x={683 + i * 86} cy={607} size={13} align="center" w={86}>{k}</Txt>
          <Txt x={683 + i * 86} cy={654} size={13} align="center" w={86} className={/[가-힣]/.test(v) ? undefined : L}>{v}</Txt>
        </div>
      ))}
    </Page>
  )
}

function Styling() {
  const s = styling
  const imgs: [number, number, number, number, string][] = [
    [520, 190, 120, 80, 'cap'], [525, 305, 85, 125, 'glove'], [525, 475, 135, 60, 'shoes'], [660, 185, 150, 200, 'polo'],
    [690, 400, 155, 140, 'skirt'], [870, 185, 120, 330, 'stand bag'], [1045, 170, 130, 450, 'model'],
  ]
  return (
    <Page no="08" caption="Golf Styling" note>
      <Txt x={53} cy={172} size={50} className={cn(L, 'font-bold tracking-[-0.02em]')} style={{ color: t.accent }}>{s.title[0]}</Txt>
      <Txt x={53} cy={235} size={50} className={cn(L, 'font-bold tracking-[-0.02em]')}>{s.title[1]}</Txt>
      <Lines x={53} cy0={302} gap={27.5} size={17} lines={s.body} />
      {s.list.map(([n, l], i) => (
        <Txt key={n} x={53} cy={516 + i * 23} size={14.5} className={cn(L, 'font-medium')}><span style={{ color: t.accent }}>{n}</span>&nbsp; {l}</Txt>
      ))}
      <Box x={446} y={121} w={794} h={558} r={18} fill="#fff" />
      {imgs.map(([x, y, w, h, l]) => <Ph key={l} x={x} y={y} w={w} h={h} label={`${l} image`} />)}
      <Ph x={627} y={436} w={40} h={40} label="golf ball" className="rounded-full" />
      {s.labels.map(([n, x, y]) => <Txt key={n} x={x} cy={y} size={13} className={cn(L, 'font-semibold')}>{n}</Txt>)}
      <Txt x={522} cy={596} size={12.5} className={L}>{s.outfitYear + s.outfit}</Txt>
      <Lines x={522} cy0={613} gap={11} size={7} lines={s.outfitBody} className={L} style={{ color: '#666' }} />
    </Page>
  )
}

function AccText({ x, y, item, light }: { x: number; y: number; item: { en: string; kr: string; price: string }; light?: boolean }) {
  const c = light ? '#fff' : t.ink
  return (
    <>
      <Txt x={x} cy={y} size={16} className={cn(L, 'font-semibold')} style={{ color: c }}>{item.en}</Txt>
      <Txt x={x} cy={y + 21} size={13.5} style={{ color: c }}>{item.kr}</Txt>
      <Txt x={x} cy={y + 52} size={16} className={cn(L, 'font-semibold')} style={{ color: c }}>{item.price}</Txt>
    </>
  )
}

function Accessories() {
  const a = accessories
  return (
    <Page no="09" caption="Accessories Collection" bg="#fff">
      <Lines x={640} cy0={155} gap={45} size={30} align="center" lines={a.lead} className="font-semibold" />
      <Box x={40} y={266} w={290} h={413} r={16} fill={t.green} />
      <Ph x={155} y={378} w={150} h={290} label="stand bag image" />
      <AccText x={73} y={312} item={a.tall} light />
      {a.top.map((it, i) => {
        const x = 344 + i * 456
        return (
          <div key={it.en}>
            <Box x={x} y={266} w={440} h={197} r={16} fill={t.bg} />
            <Ph x={x + 245} y={290} w={160} h={150} label={`${it.en} image`} />
            <AccText x={x + 32} y={312} item={it} />
          </div>
        )
      })}
      {a.bottom.map((it, i) => {
        const x = 344 + i * 304
        return (
          <div key={it.en}>
            <Box x={x} y={479} w={288} h={200} r={16} fill={t.bg} />
            <Ph x={x + 155} y={565} w={110} h={100} label={`${it.en} image`} />
            <AccText x={x + 32} y={524} item={it} />
          </div>
        )
      })}
    </Page>
  )
}

function Promo() {
  const p = promo
  return (
    <Page no="10" caption="Special Promotion" ink="#fff" rule="rgba(255,255,255,0.25)" under={<>
      <Ph x={0} y={0} w={1280} h={500} label="driver and golf ball photo" tone={PHOTO_DARK} />
      <Box x={0} y={500} w={1280} h={220} fill={t.bg} />
    </>}>
      <Txt x={640} cy={172} size={52} align="center" className={cn(L, 'font-medium')} style={{ color: '#fff' }}>{p.title[0]}<span style={{ color: '#8fae8a' }}>{p.title[1]}</span></Txt>
      <Txt x={640} cy={229} size={30} align="center" className="font-bold" style={{ color: '#fff' }}>{p.sub}</Txt>
      <Txt x={640} cy={289} size={18} align="center" style={{ color: '#fff' }}><b className="font-bold" style={{ fontSize: 16 }}>{p.periodLabel}</b>&nbsp; {p.period}</Txt>
      {p.items.map((lines, i) => {
        const x = 40 + i * 404.5
        const cx = x + 196
        return (
          <div key={i}>
            <Box x={x} y={356} w={392} h={324} r={18} fill="#fff" />
            <Oval cx={cx} cy={527} w={56} h={32} fill={t.green} color="#fff" size={13}>{`0${i + 1}`}</Oval>
            <Lines x={cx} cy0={580} gap={35} size={24} align="center" w={392} lines={lines} className="font-medium" style={{ color: t.ink }} />
          </div>
        )
      })}
      <Abs x={180} y={416} w={106} h={58} className={cn(L, 'flex flex-col items-center justify-center gap-[5px] rounded-[4px] leading-none')} style={{ background: '#6e9a6c', color: '#fff' }}>
        <span className="font-semibold" style={{ fontSize: 8 }}>COUPON</span>
        <span className="font-semibold" style={{ fontSize: 24 }}>30%</span>
      </Abs>
      <Abs x={588} y={398}><Truck size={104} color="#6e9a6c" fill="#cfdccd" strokeWidth={1.4} /></Abs>
      <Abs x={1004} y={404}><CircleParking size={80} color="#6e9a6c" strokeWidth={1.4} /></Abs>
    </Page>
  )
}

function Contact() {
  const c = contact
  return (
    <CardSlide>
      <Ph x={658} y={85} w={510} h={545} label="showroom photo" tone="#d6d8d3" className="rounded-[12px]" />
      <Oval cx={380} cy={182} w={148} h={52} border={t.ink} size={18}>{c.oval}</Oval>
      <Lines x={380} cy0={262} gap={37.5} size={25} align="center" w={500} lines={c.lines} className="font-semibold" />
      <Box x={360} y={437} w={40} h={1} fill="#ccc" />
      <Txt x={380} cy={478} size={16} align="center" w={300} className={cn(L, 'font-semibold')}>{c.label}</Txt>
      <Lines x={380} cy0={510} gap={22.5} size={16} align="center" w={500} lines={c.info} />
    </CardSlide>
  )
}

const deck: DeckDefinition = {
  id: '32',
  title: '초록 깔끔 골프 카탈로그 홍보',
  slides: [Cover, Contents, Concept, Lookbook, Features, Categories, Section, Best, Lineup, Detail, Styling, Accessories, Promo, Contact],
}
export default deck
