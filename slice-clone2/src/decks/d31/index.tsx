import type { DeckDefinition } from '../../ui'
import { Abs, Slide, cn } from '../../ui'
import { Feather, Gem, Move, Route } from 'lucide-react'
import { Badge, Lines, Logo, Page, Ph, Rect, Swoosh, Txt } from './components'
import { accessories, best, categories, concept, contact, contents, cover, detail, features, lineup, lookbook, promo, section, styling } from './data'
import { t } from './theme'

const L = t.latin
const DARK = '#4b5563'

function Cover() {
  return (
    <Slide background={t.blue} style={{ color: '#fff' }}>
      <Swoosh color={t.lime} paths={[['M -30 665 C 250 390, 650 260, 1000 285 S 1260 360, 1300 395', 30]]} />
      <Ph x={745} y={95} w={285} h={625} label="golfer photo" className="rounded-t-[140px]" />
      <Logo x={1098} y={47} w={132} h={18} />
      <Txt x={42} cy={88} size={104} className={cn(L, 'font-medium tracking-[-0.03em]')}>{cover.title[0]}</Txt>
      <Txt x={42} cy={186} size={104} className={cn(L, 'font-bold tracking-[-0.04em]')} style={{ color: t.lime }}>{cover.title[1]}</Txt>
      <Txt x={48} cy={252} size={24} className={cn(L, 'font-light')} style={{ color: t.lime }}>{cover.year}</Txt>
      <Txt x={673} cy={253} size={24} align="right" className={cn(L, 'font-light')} style={{ color: t.lime }}>{cover.tagline}</Txt>
      <Txt x={48} cy={660} size={20} style={{ color: t.lime }}>{cover.bottom}</Txt>
      <Lines x={1233} cy0={628} gap={33} size={21} align="right" lines={cover.right} style={{ color: t.lime }} />
    </Slide>
  )
}

function Contents() {
  return (
    <Slide background="#fff" style={{ color: t.ink }}>
      <Rect x={0} y={0} w={417} h={720} fill={t.blue} />
      <svg className="absolute left-0 top-0" width={417} height={720}>
        <path d="M 100 730 C 150 520, 260 330, 425 235" fill="none" stroke={t.lime} strokeWidth={22} />
      </svg>
      <Txt x={46} cy={70} size={58} className={cn(L, 'font-bold tracking-[-0.02em]')} style={{ color: t.lime }}>{contents.title}</Txt>
      <Txt x={48} cy={131} size={46} className="font-bold" style={{ color: '#fff' }}>{contents.kr}</Txt>
      <Abs x={45} y={380} w={20} h={292} className={cn(L, 'flex items-center justify-start whitespace-nowrap leading-none')} style={{ fontSize: 13, color: '#fff', writingMode: 'sideways-lr' }}>
        {contents.side[0]}<b className="font-bold">{contents.side[1]}</b>
      </Abs>
      <Logo x={1098} y={45} w={132} h={18} />
      <Rect x={470} y={49} w={598} h={1} fill="#c5cbe0" />
      {[225, 354, 540].map((y) => <Rect key={y} x={470} y={y} w={762} h={2} fill="#3d5bbc" />)}
      <Rect x={470} y={672} w={762} h={1} fill="#c5cbe0" />
      {contents.groups.map((g) => (
        <div key={g.no}>
          <Txt x={492} cy={g.cy} size={25} className={cn(L, 'font-semibold')} style={{ color: t.blue }}>{g.no}</Txt>
          <Txt x={549} cy={g.cy} size={24} className={cn(L, 'font-semibold tracking-[-0.02em]')}>{g.en}</Txt>
          <Txt x={549} cy={g.cy + 34} size={21}>{g.kr}</Txt>
          {g.items.map(([kr, en], i) => (
            <div key={kr}>
              <Txt x={858} cy={g.cy - 1 + i * 27} size={15}>{kr}</Txt>
              <Txt x={997} cy={g.cy - 1 + i * 28.5} size={17} className={cn(L, 'font-light')} style={{ color: '#9a9a9a' }}>{en}</Txt>
            </div>
          ))}
        </div>
      ))}
    </Slide>
  )
}

function Concept() {
  return (
    <Page bg={DARK} ink="#fff" rule="rgba(255,255,255,0.8)" title={concept.title} caption={concept.caption}
      under={<Ph x={0} y={0} w={1280} h={720} label="aerial golf course photo" tone={DARK} />}>
      {[[908, 8, 75, '#fff'], [0, 235, 75, t.lime], [1215, 392, 77, t.lime], [1141, 311, 77, '#fff'], [917, 680, 75, t.lime]].map(([cx, cy, r, c], i) => (
        <Abs key={i} x={(cx as number) - (r as number)} y={(cy as number) - (r as number)} w={(r as number) * 2} h={(r as number) * 2} className="rounded-full" style={{ background: c as string }} />
      ))}
      {concept.big.map((w, i) => (
        <Txt key={w} x={76} cy={362 + i * 77} size={84} className={cn(L, i === 2 ? 'font-bold' : 'font-light', 'tracking-[-0.03em]')} style={{ color: i === 2 ? t.lime : '#fff' }}>{w}</Txt>
      ))}
      <Txt x={494} cy={430} size={27} className="font-bold">{concept.lead}</Txt>
      <Lines x={494} cy0={475} gap={31} size={19} lines={concept.body} />
    </Page>
  )
}

function Lookbook() {
  return (
    <Page bg="#000" ink="#fff" rule="rgba(255,255,255,0.6)" title={lookbook.title} caption={lookbook.caption}>
      <Ph x={0} y={253} w={630} h={467} label="golf bags photo" tone={DARK} />
      <Ph x={640} y={253} w={312} h={467} label="female golfer photo" tone={DARK} />
      <Ph x={965} y={253} w={315} h={467} label="male golfer photo" tone={DARK} />
      <Swoosh color={t.lime} paths={[['M 1290 148 C 1130 170, 990 280, 955 420', 9], ['M 628 585 C 700 640, 760 690, 785 730', 9]]} />
      <Txt x={640} cy={143} size={28} align="center" className={L}><span className="font-semibold" style={{ color: t.lime }}>NEW</span> COLLECTION</Txt>
      <Lines x={640} cy0={182} gap={26} size={18} align="center" lines={lookbook.lines} />
    </Page>
  )
}

const featureIcons = [Route, Move, Feather, Gem]
function Features() {
  return (
    <Page title={features.title} caption={features.caption}>
      <Ph x={650} y={100} w={630} h={620} label="golfer swing photo" className="rounded-t-[200px]" />
      <Swoosh color={t.blue} paths={[['M 845 -10 C 760 200, 670 450, 680 730', 26], ['M 1290 315 C 1240 420, 1180 520, 1135 595', 22]]} />
      <Lines x={48} cy0={147} gap={39} size={25} lines={features.lead} className="font-medium tracking-[-0.02em]" />
      <Lines x={48} cy0={232} gap={31} size={18} lines={features.body} />
      {features.items.map((f, i) => {
        const cx = [97, 240, 387, 532][i]
        const Icon = featureIcons[i]
        return (
          <div key={f.en[0]}>
            <Abs x={cx - 47} y={424} w={94} h={94} className="flex items-center justify-center rounded-full" style={{ background: '#e8e9ff' }}>
              <Icon size={46} color={t.blue} strokeWidth={1.4} />
            </Abs>
            <Lines x={cx} cy0={544} gap={21} size={16} align="center" w={160} lines={f.en} className={cn(L, 'font-medium')} />
            <Lines x={cx} cy0={593} gap={23} size={14.5} align="center" w={170} lines={f.kr} />
          </div>
        )
      })}
    </Page>
  )
}

function Categories() {
  return (
    <Page title={categories.title} caption={categories.caption}>
      <Txt x={48} cy={146} size={26} className="font-medium tracking-[-0.02em]">{categories.lead}</Txt>
      {categories.items.map(([en, kr, d], i) => {
        const x = 48 + i * 198.8
        return (
          <div key={en}>
            <Rect x={x} y={187} w={190} h={310} fill={t.gray} />
            <Ph x={i < 4 ? x + 20 : x} y={i < 4 ? 250 : 187} w={i < 4 ? 150 : 190} h={i < 4 ? 247 : 310} label={`${en} image`} />
            <Badge x={x} y={187} w={42} h={32} fill={t.blue}>{String(i + 1).padStart(2, '0')}</Badge>
            <Txt x={x} cy={524} size={18} className={L}>{en}</Txt>
            <Txt x={x} cy={549} size={16} className="font-medium">{kr}</Txt>
            <Rect x={x} y={572} w={190} h={1} fill={t.rule} />
            <Txt x={x} cy={597} size={15}>{d}</Txt>
          </div>
        )
      })}
    </Page>
  )
}

function Section() {
  return (
    <Slide background={t.blue} style={{ color: '#fff' }}>
      <Swoosh color={t.lime} paths={[['M 1290 300 C 1100 210, 900 125, 620 125 C 380 128, 320 260, 470 410 C 620 560, 860 650, 1000 735', 34]]} />
      <Ph x={680} y={140} w={520} h={305} label="floating golf course island" />
      <Txt x={48} cy={54} size={15} className={L}>{section.kicker[0]}<b className="font-bold">{section.kicker[1]}</b></Txt>
      <Logo x={1098} y={47} w={132} h={18} />
      <Txt x={46} cy={369} size={66} className={cn(L, 'font-bold')} style={{ color: t.lime }}>{section.no}</Txt>
      <Txt x={46} cy={498} size={64} className={cn(L, 'font-light tracking-[-0.03em]')}>{section.title[0]}</Txt>
      <Txt x={46} cy={563} size={64} className={cn(L, 'font-bold tracking-[-0.03em]')} style={{ color: t.lime }}>{section.title[1]}</Txt>
      <Txt x={46} cy={630} size={58} className="font-bold tracking-[-0.03em]">{section.title[2]}</Txt>
    </Slide>
  )
}

function Best() {
  return (
    <Page title={best.title} caption={best.caption}>
      <Txt x={48} cy={148} size={26} className="font-medium tracking-[-0.02em]">{best.lead}</Txt>
      {best.items.map((b, i) => {
        const x = 48 + i * 400
        return (
          <div key={b.name}>
            <Rect x={x} y={185} w={385} h={320} fill={t.gray} />
            <Ph x={x + 85} y={215} w={215} h={290} label="product image" />
            <Badge x={x} y={185} w={84} h={30} fill={t.blue} size={13}>{`BEST 0${i + 1}`}</Badge>
            <Txt x={x} cy={502} size={17} className="font-semibold tracking-[-0.02em]">{b.name}</Txt>
            <Txt x={x + 385} cy={502} size={18} align="right" w={150} className={cn(L, 'font-medium')}>{b.price}</Txt>
            <Txt x={x} cy={529} size={17} style={{ color: t.muted }}>{b.sub}</Txt>
            <Rect x={x} y={553} w={382} h={1} fill={t.rule} />
            <Lines x={x} cy0={576} gap={24} size={15} lines={b.points} />
          </div>
        )
      })}
    </Page>
  )
}

function Lineup() {
  const cols = [571, 780, 960, 1160]
  const rowsCy = [295, 353, 412, 476, 539, 598]
  return (
    <Page title={lineup.title} caption={lineup.caption}>
      <Txt x={48} cy={155} size={62} className={L}><b className="font-bold">PRO</b> X SERIES</Txt>
      {[0, 1, 2, 3, 4, 5].map((i) => {
        const x = 48 + (i % 3) * 132
        const y = 208 + Math.floor(i / 3) * 215
        return (
          <div key={i}>
            <Rect x={x} y={y} w={120} h={205} fill={t.gray} />
            <Ph x={x + 8} y={y + 40} w={104} h={165} label="club image" />
            <Txt x={x + 8} cy={y + 18} size={15} className={cn(L, 'font-semibold')}>{`${i + 1}.`}</Txt>
          </div>
        )
      })}
      <Lines x={473} cy0={139} gap={31} size={18} lines={lineup.intro} />
      <Rect x={473} y={207} w={759} h={1.5} fill="#999" />
      {lineup.head.map((h, i) => <Txt key={h} x={cols[i]} cy={237} size={16} align="center" w={200} className="font-medium" style={{ color: t.blue }}>{h}</Txt>)}
      {lineup.rows.map((r, i) => (
        <div key={r[0]}>
          {i % 2 === 0 && <Rect x={473} y={rowsCy[i] - 28} w={759} h={56} fill={t.gray} />}
          <Txt x={505} cy={rowsCy[i]} size={16} className={L}>{String(i + 1)}</Txt>
          <Txt x={551} cy={rowsCy[i]} size={16} className={cn(L, 'tracking-[-0.03em]')}>{r[0]}</Txt>
          {r.slice(1).map((c, j) => <Txt key={j} x={cols[j + 1]} cy={rowsCy[i]} size={16} align="center" w={260} className={j === 2 ? L : undefined}>{c}</Txt>)}
        </div>
      ))}
      <Rect x={473} y={628} w={759} h={1.5} fill="#999" />
    </Page>
  )
}

function Detail() {
  return (
    <Page title={detail.title} caption={detail.caption} under={<>
      <Rect x={0} y={0} w={472} h={720} fill={t.gray} />
      <Ph x={110} y={140} w={300} h={580} label="driver image" />
      <svg className="absolute left-0 top-0" width={472} height={720}><path d="M -10 440 C 120 300, 280 225, 480 212" fill="none" stroke={t.blue} strokeWidth={30} /></svg>
    </>}>
      <Txt x={48} cy={495} size={30} className={cn(L, 'font-bold tracking-[-0.02em]')}>{detail.name[0]}</Txt>
      <Txt x={48} cy={534} size={30}>{detail.name[1]}</Txt>
      <Txt x={48} cy={581} size={17}><span className={cn(L, 'font-medium')} style={{ fontSize: 16 }}>PRICE</span> 소비자가</Txt>
      <Txt x={46} cy={616} size={30} className={cn(L, 'font-semibold')}>{detail.price}</Txt>
      <Txt x={520} cy={146} size={28} className="font-bold tracking-[-0.03em]">{detail.lead}</Txt>
      <Lines x={520} cy0={187} gap={31} size={19} lines={detail.body} />
      <Txt x={520} cy={273} size={17}><span className={cn(L, 'font-medium')} style={{ fontSize: 16 }}>KEY FEATURES</span> 핵심 특징</Txt>
      <Rect x={725} y={273} w={242} h={1} fill={t.rule} />
      {detail.features.map(([h, a, b], i) => {
        const cy = 313 + i * 117
        return (
          <div key={h}>
            <Badge x={520} y={cy - 12} w={36} h={36} fill={t.blue} size={17}>{`0${i + 1}`}</Badge>
            <Txt x={574} cy={cy} size={17} className={cn(L, 'font-semibold')}>{h}</Txt>
            <Lines x={574} cy0={cy + 26} gap={23} size={15.5} lines={[a, b]} />
            <Rect x={520} y={cy + 82} w={447} h={1.5} fill={t.rule} />
          </div>
        )
      })}
      <Txt x={1003} cy={277} size={13} className={L}>PRODUCT SPECIFICATIONS</Txt>
      <Txt x={1227} cy={277} size={13} align="right" w={80}>제품 사양</Txt>
      <Rect x={1003} y={297} w={229} h={1.5} fill="#999" />
      {detail.specs.map(([k, v], i) => {
        const cy = i === 0 ? 318 : 355 + (i - 1) * 36.5
        return (
          <div key={k}>
            <Rect x={1003} y={cy - 17} w={95} h={34} fill={t.gray} />
            {i === 0 && <Rect x={1100} y={cy - 17} w={132} h={34} fill={t.gray} />}
            <Txt x={1051} cy={cy} size={14} align="center" w={95} className={i === 0 ? 'font-medium' : undefined}>{k}</Txt>
            <Txt x={1167} cy={cy} size={14} align="center" w={130} className={cn(i === 0 ? 'font-medium' : L, 'tracking-[-0.02em]')}>{v}</Txt>
          </div>
        )
      })}
      <Rect x={1003} y={628} w={229} h={1.5} fill="#999" />
    </Page>
  )
}

function Styling() {
  return (
    <Page title={styling.title} caption={styling.caption}>
      <Swoosh color={t.lime} paths={[['M -20 290 C 300 280, 600 420, 760 660', 32]]} />
      <Rect x={542} y={135} w={258} h={493} fill={t.gray} />
      <Ph x={575} y={170} w={190} h={420} label="stand bag image" />
      <Rect x={288} y={477} w={245} h={150} fill={t.gray} />
      <Ph x={250} y={500} w={265} h={125} label="golf shoes image" />
      <Ph x={745} y={135} w={535} h={585} label="women golfers photo" />
      <Txt x={48} cy={158} size={60} className={L}><b className="font-bold">WOMEN'S</b> LOOK</Txt>
      <Lines x={48} cy0={216} gap={31} size={18} lines={styling.body} />
      <Txt x={48} cy={490} size={19} className={cn(L, 'font-bold')}>STYLING POINT</Txt>
      <Lines x={48} cy0={520} gap={31} size={19} lines={styling.point} />
      <Lines x={1232} cy0={143} gap={21.2} size={14.5} align="right" lines={styling.list} className={L} />
      {styling.badges.map(([x, y], i) => <Badge key={i} x={x} y={y} w={36} h={30} fill={t.lime} color={t.ink} size={15}>{`0${i + 1}`}</Badge>)}
    </Page>
  )
}

function AccCard({ x, y, w, h, n, item, wide }: { x: number; y: number; w: number; h: number; n: number; item: { name: string; price: string; desc: readonly string[]; en: string }; wide?: boolean }) {
  const r = x + w - 13
  return (
    <>
      <Rect x={x} y={y} w={w} h={h} fill={t.gray} />
      <Txt x={x + 12} cy={y + 23} size={17} className={cn(L, 'font-medium')}>{`${n}.`}</Txt>
      <Txt x={r} cy={y + 23} size={17} align="right" w={300} className="font-medium">{item.name}</Txt>
      <Txt x={r} cy={y + 47} size={18} align="right" w={300} className={L}>{item.price}</Txt>
      {wide
        ? <Lines x={r} cy0={y + 88} gap={19.5} size={12.5} align="right" w={360} lines={item.desc} />
        : <Lines x={x + (n === 6 ? 16 : 12)} cy0={n === 6 ? 541 : y + 211} gap={18.5} size={12.5} w={w - 14} lines={item.desc} />}
      <Txt x={x + (n === 6 ? 16 : 12)} cy={wide || n === 6 ? 605 : y + 277} size={15} className={L}>{item.en}</Txt>
    </>
  )
}

function Accessories() {
  const a = accessories
  return (
    <Page title={a.title} caption={a.caption}>
      <Swoosh color={t.lime} paths={[['M 755 400 C 860 210, 1050 80, 1290 10', 40], ['M -20 290 C 150 330, 300 420, 380 520', 26], ['M 430 640 C 470 680, 500 700, 520 730', 26], ['M 600 730 C 610 690, 620 660, 630 640', 10]]} />
      {a.small.map((it, i) => {
        const x = 50 + i * 238.5
        return (
          <div key={it.en}>
            <AccCard x={x} y={192} w={226} h={295} n={i + 1} item={it} />
            <Ph x={x + 10} y={285} w={140} h={105} label={it.en} />
          </div>
        )
      })}
      {a.wide.map((it, i) => {
        const x = 50 + i * 477
        return (
          <div key={it.en}>
            <AccCard x={x} y={500} w={i ? 463 : 465} h={129} n={i + 4} item={it} wide />
            <Ph x={x + (i ? 45 : 45)} y={512} w={i ? 150 : 75} h={i ? 65 : 75} label={it.en} />
          </div>
        )
      })}
      <AccCard x={1002} y={192} w={230} h={437} n={6} item={a.tall} />
      <Ph x={1025} y={262} w={150} h={260} label={a.tall.en} />
      <Txt x={48} cy={146} size={26} className="font-medium tracking-[-0.02em]">{a.lead}</Txt>
    </Page>
  )
}

function Promo() {
  const p = promo
  return (
    <Page bg={t.gray} title={p.title} caption={p.caption} under={<Rect x={0} y={372} w={1280} h={348} fill="#fff" />}>
      <Swoosh color={t.blue} paths={[['M 968 -10 C 870 70, 820 150, 806 210', 7], ['M 405 182 C 450 188, 495 205, 520 232', 3.5], ['M 570 330 C 574 345, 576 360, 575 372', 9]]} />
      <Ph x={450} y={140} w={455} h={200} label="golf shoe image" className="rounded-[60px]" />
      <Txt x={48} cy={140} size={19} className={L}>{p.kicker}</Txt>
      <Lines x={48} cy0={182} gap={39} size={28} lines={p.lines} className="tracking-[-0.02em]" />
      <Txt x={48} cy={305} size={22} className={L}>{p.date}</Txt>
      <Txt x={1000} cy={162} size={78} className={cn(L, 'font-semibold tracking-[-0.03em]')}>{p.pct}</Txt>
      <Badge x={1103} y={133} w={66} h={20} fill={t.blue} size={18}>{p.upTo}</Badge>
      <Txt x={1103} cy={176} size={32} className={cn(L, 'font-bold')}>%</Txt>
      <Lines x={1001} cy0={224} gap={44} size={19} lines={p.perks} />
      {[247, 290].map((y) => <Rect key={y} x={1001} y={y} w={231} h={1} fill={t.rule} />)}
      {[50, 350, 648, 948].map((x, i) => (
        <div key={x}>
          <Rect x={x} y={408} w={285} h={220} fill={t.gray} />
          <Ph x={x + 40} y={430} w={205} h={180} label={['cap', 'gloves', 'polo shirt', 'skirt'][i]} />
        </div>
      ))}
    </Page>
  )
}

function Contact() {
  const c = contact
  return (
    <Page bg={t.gray} footerLeft={false} logo={false} under={<Ph x={640} y={48} w={592} h={608} label="golfer on course photo" tone={DARK} />}>
      <Swoosh color={t.blue} paths={[['M 505 735 C 700 420, 950 270, 1295 185', 28]]} />
      <Ph x={790} y={656} w={330} h={64} label="golfer photo (overflow)" tone={DARK} />
      <Txt x={48} cy={62} size={25} className="font-bold">{c.title}</Txt>
      <Lines x={48} cy0={110} gap={31} size={19} lines={c.body} />
      <Abs x={1190} y={82} w={20} h={240} className={cn(L, 'flex items-center whitespace-nowrap leading-none')} style={{ fontSize: 14, color: '#fff', writingMode: 'vertical-rl' }}>{c.side}</Abs>
      <Logo x={50} y={438} w={210} h={26} />
      {c.rows.map((r) => (
        <div key={r.label}>
          <Txt x={48} cy={r.cy} size={15} className={cn(L, 'font-semibold')}>{r.label}</Txt>
          {r.values.map(([v, cy]) => <Txt key={v} x={210} cy={cy as number} size={15.5} className={(v as string).match(/^[A-Z]/) ? L : undefined}>{v as string}</Txt>)}
        </div>
      ))}
    </Page>
  )
}

const deck: DeckDefinition = {
  id: '31',
  title: '파랑 모던 골프 홍보',
  slides: [Cover, Contents, Concept, Lookbook, Features, Categories, Section, Best, Lineup, Detail, Styling, Accessories, Promo, Contact],
}
export default deck
