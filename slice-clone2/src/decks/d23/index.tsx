import { ArrowRight, ChevronDown, Flag, Play } from 'lucide-react'
import type { DeckDefinition } from '../../ui'
import { Abs, cn } from '../../ui'
import { AreaChart, Donut } from './charts'
import { Cross, Dots, GSlide, Grid, Hatch, Header, IconDisc, Ph, Ring, Square, Txt, type Cell } from './components'
import { budget, club, contents, cover, finance, income, market, marketing, overview, partners, thanks, values } from './data'
import { t } from './theme'

const W = '#fff'
const BottomDots = ({ color }: { color?: string }) => <Dots x={1102} y={662} color={color} />

function Cover() {
  return (
    <GSlide>
      <Hatch x={1138} y={0} w={142} h={196} />
      <Hatch x={0} y={570} w={181} h={150} />
      <Ph x={674} y={80} w={414} h={640} label="golfer photo" />
      <Dots x={64} y={57} />
      <Ring cx={157} cy={138} r={25} />
      {cover.title.map((l, i) => (
        <Txt key={l} x={130} cy={258 + i * 80} size={72} className={cn(t.latin, 'font-extrabold tracking-[-0.01em]')} style={{ color: t.green }}>{l}</Txt>
      ))}
      <Txt x={132} cy={484} size={33} className="font-light" style={{ color: t.green }}>{cover.sub}</Txt>
      <Abs x={200} y={538}><Play size={56} color={t.green} strokeWidth={2.2} /></Abs>
      <Square x={1084} y={239} />
      <Cross cx={1222} cy={360} />
      <BottomDots />
    </GSlide>
  )
}

function Overview() {
  const C = (text: string, head = false, colSpan?: number): Cell => ({ text, head, colSpan })
  const rows: Cell[][] = [
    ...overview.wide.map(([k, v]) => [C(k, true), C(v, false, 3)]),
    ...overview.pairs.map(([a, b, c, d]) => [C(a, true), C(b), C(c, true), C(d)]),
  ]
  return (
    <GSlide>
      <Ph x={0} y={0} w={1280} h={277} label="golf course lake photo" />
      <Header title={overview.title} en={overview.en} x={164} y={320} />
      <Hatch x={97} y={557} w={210} h={163} />
      <Grid x={167} y={383} cols={[135, 332, 152, 326]} rowH={39} rows={rows} size={15} />
      <BottomDots />
    </GSlide>
  )
}

function Contents() {
  return (
    <GSlide bg={t.green}>
      <Hatch x={0} y={161} w={170} h={283} tone="#a2c09c" />
      <Dots x={70} y={67} color={W} />
      <Square x={1169} y={80} s={40} color={W} />
      <Cross cx={1160} cy={138} color={W} />
      <Txt x={202} cy={193} size={50} className={cn(t.latin, 'font-extrabold')} style={{ color: W }}>{contents.title}</Txt>
      <Txt x={203} cy={237} size={19} style={{ color: W }}>{contents.sub}</Txt>
      {contents.items.map((it, i) => (
        <div key={it.no}>
          <Txt x={639} cy={198 + i * 110} size={38} className={cn(t.latin, 'font-extrabold')} style={{ color: W }}>{it.no}</Txt>
          <Txt x={709} cy={199 + i * 110} size={22} style={{ color: W }}>{it.name}</Txt>
          <Txt x={709} cy={231 + i * 110} size={14} lh={21} className="font-light" style={{ color: W }}>{it.desc}</Txt>
        </div>
      ))}
      <BottomDots color={W} />
    </GSlide>
  )
}

function Market() {
  const xs = [203, 558, 909]
  return (
    <GSlide>
      <Dots x={64} y={57} />
      <Square x={1161} y={62} s={40} />
      <Cross cx={1149} cy={135} />
      <Header title={market.title} en={market.en} desc={market.desc} />
      {market.charts.map((c, i) => (
        <div key={c.legend}>
          <Txt x={xs[i] - 48} cy={252} size={13} style={{ color: t.green }}>{market.unit}</Txt>
          <AreaChart x={xs[i]} y={304} w={222} h={169} max={c.max} step={c.step} values={c.values} years={market.years} />
          <Abs x={xs[i] + 22} y={528} w={14} h={14} className="rounded-full" style={{ background: t.green }} />
          <Txt x={xs[i] + 40} cy={535} size={16} style={{ color: '#666' }}>{c.legend}</Txt>
        </div>
      ))}
      <Txt x={640} cy={601} size={20} align="center" w={1100} className="font-semibold" style={{ color: t.green }}>{market.note}</Txt>
      <BottomDots />
    </GSlide>
  )
}

function Marketing() {
  return (
    <GSlide>
      <Ph x={0} y={413} w={218} h={307} label="golfer silhouette illustration" />
      <Dots x={64} y={57} />
      <Abs x={1172} y={54} className="flex">{[0, 1, 2].map((i) => <Play key={i} size={18} fill={t.green} color={t.green} />)}</Abs>
      <Square x={1137} y={101} s={38} />
      <Header title={marketing.title} en={marketing.en} desc={marketing.desc} />
      {marketing.steps.map((s, i) => {
        const cx = 252 + i * 253, cy = 355, R = 96
        const top = i % 2 === 0
        return (
          <div key={i}>
            <Abs x={cx - R - 2} y={cy - R - 2}>
              <svg width={R * 2 + 4} height={R * 2 + 4}>
                <path d={`M 2 ${R + 2} A ${R} ${R} 0 0 ${top ? 1 : 0} ${R * 2 + 2} ${R + 2}`} fill="none" stroke={t.green} strokeWidth={4} />
              </svg>
            </Abs>
            {i < 3 && <Abs x={cx + R - 4} y={cy - 18}><ArrowRight size={44} color={t.green} strokeWidth={2.4} /></Abs>}
            <Abs x={cx - 73} y={cy - 73} w={146} h={146} className="rounded-full" style={{ border: '2px solid #c9c9c9' }} />
            <Txt x={cx} cy={cy - 12} size={20} lh={24} align="center" w={140} style={{ color: t.green }}>{s.label}</Txt>
            <Abs x={cx - 14} y={466}><ChevronDown size={28} color={t.green} strokeWidth={2.4} /></Abs>
            <Txt x={cx - 90} cy={523} size={14} lh={21} w={190} className="font-light" style={{ color: '#888' }}>{s.text}</Txt>
          </div>
        )
      })}
      <BottomDots />
    </GSlide>
  )
}

function Values() {
  const cx = 464, cy = 403, R = 225
  const discs = [[642, 255], [686, 402], [642, 547]]
  return (
    <GSlide>
      <Abs x={0} y={0} w={464} h={720} style={{ background: t.green }} />
      <Hatch x={0} y={492} w={155} h={228} tone="#a2c09c" />
      <Abs x={cx - R} y={cy - R} w={R * 2} h={R * 2} className="rounded-full" style={{ border: `3px solid ${W}` }} />
      <Abs x={cx} y={cy - R} w={R + 4} h={R * 2} className="overflow-hidden">
        <div className="absolute rounded-full" style={{ left: -R, top: 0, width: R * 2, height: R * 2, border: `3px solid ${t.green}` }} />
      </Abs>
      <Ph x={cx - 161} y={cy - 161} w={322} h={322} label="golf club and ball photo" className="rounded-full" />
      <Dots x={70} y={67} color={W} />
      <Square x={1161} y={791 - 728} s={40} />
      <Cross cx={1160} cy={138} />
      <Header title={values.title} en={values.en} x={544} y={124} rule={false} />
      {values.items.map((it, i) => {
        const [dx, dy] = discs[i]
        return (
          <div key={it.title}>
            <IconDisc cx={dx} cy={dy} r={48}>
              {i === 0 ? <Flag size={36} color={W} /> : <Ph x={30} y={28} w={36} h={40} label={i === 1 ? 'golf bag icon' : 'golf ball icon'} tone="#cfe0cb" />}
            </IconDisc>
            <Txt x={dx + 66} cy={dy - 34} size={20} className="tracking-[-0.03em]" style={{ color: t.green }}>{it.title}</Txt>
            <Txt x={dx + 98} cy={dy - 6} size={14} lh={21} className="font-light" style={{ color: '#888' }}>{it.text}</Txt>
          </div>
        )
      })}
      <BottomDots />
    </GSlide>
  )
}

function Finance() {
  const H = (s: string, colSpan?: number): Cell => ({ text: s, head: true, colSpan })
  const left: Cell[][] = [
    [H(finance.head[0], 2), H(finance.head[1])],
    ...finance.assets.rows.map(([k, v], i) => [...(i === 0 ? [{ text: finance.assets.group, rowSpan: 5 }] : []), { text: k }, { text: v }]),
    [{ text: finance.assets.total[0], colSpan: 2, strong: true, color: t.green }, { text: finance.assets.total[1], strong: true, color: t.green }],
  ]
  const right: Cell[][] = [
    [H(finance.head[0], 2), H(finance.head[1])],
    ...finance.debts.flatMap((g) => g.rows.map(([k, v], i) => [...(i === 0 ? [{ text: g.group, rowSpan: 3 }] : []), { text: k }, { text: v }])),
    [{ text: finance.debtTotal[0], colSpan: 2, strong: true, color: t.green }, { text: finance.debtTotal[1], strong: true, color: t.green }],
  ]
  return (
    <GSlide>
      <Abs x={0} y={570} w={1280} h={150} style={{ background: t.green }} />
      <Dots x={64} y={57} />
      <Ring cx={1197} cy={84} r={22} />
      <Cross cx={1160} cy={136} />
      <Header title={finance.title} en={finance.en} desc={finance.desc} />
      <Txt x={135} cy={272} size={22} style={{ color: t.green }}>{finance.sub}</Txt>
      <Txt x={1166} cy={272} size={14} align="right" w={200}>{finance.unit}</Txt>
      <Grid x={135} y={302} cols={[75, 215, 203]} rowH={[48, 49, 49, 49, 49, 49, 48]} rows={left} size={17} />
      <Grid x={671} y={297} cols={[74, 216, 203]} rowH={[44, 43, 43, 43, 43, 43, 43, 45]} rows={right} size={17} />
    </GSlide>
  )
}

function Income() {
  const x0 = 215, base = 561, ph = 259
  const H = (s: string, o: Partial<Cell> = {}): Cell => ({ text: s, head: true, ...o })
  const rows: Cell[][] = [
    [H('구분', { rowSpan: 2 }), H('추  정', { colSpan: 2 })],
    [H(income.years[0]), H(income.years[1])],
    ...income.rows.map(([a, b, c], i) => [{ text: a, color: i === 0 ? t.green : undefined }, { text: b }, { text: c }]),
  ]
  return (
    <GSlide>
      <Dots x={64} y={57} />
      <Square x={1161} y={62} s={40} />
      <Cross cx={1160} cy={136} />
      <Header title={income.title} en={income.en} desc={income.desc} />
      {income.ticks.map((v) => (
        <div key={v}>
          <Abs x={x0} y={base - (v / 10000) * ph} w={350} h={1} style={{ background: '#dcdcdc' }} />
          <Txt x={x0 - 12} cy={base - (v / 10000) * ph} size={16} align="right" w={80} style={{ color: '#666' }}>{v.toLocaleString()}</Txt>
        </div>
      ))}
      <Abs x={x0} y={base - ph} w={1} h={ph} style={{ background: '#dcdcdc' }} />
      {income.bars.map(([label, a, b], i) => {
        const gx = 222 + i * 89
        return (
          <div key={label}>
            <Abs x={gx} y={base - (a / 10000) * ph} w={29} h={(a / 10000) * ph} style={{ background: t.green }} />
            <Abs x={gx + 39} y={base - (b / 10000) * ph} w={29} h={(b / 10000) * ph} style={{ background: '#c8c8c8' }} />
            <Txt x={gx + 34} cy={576} size={16} align="center" w={90} style={{ color: '#666' }}>{label}</Txt>
          </div>
        )
      })}
      {income.years.map((y, i) => (
        <Abs key={y} x={296 + i * 66} y={617} className="flex items-center gap-1 leading-none" style={{ fontSize: 16, color: '#666' }}>
          <span className="inline-block h-[13px] w-[13px]" style={{ background: i ? '#c8c8c8' : t.green }} />{y}
        </Abs>
      ))}
      <Txt x={1124} cy={258} size={14} align="right" w={200}>{income.unit}</Txt>
      <Grid x={640} y={278} cols={[165, 159, 164]} rowH={[36, 37, 34, 34, 34, 34, 34, 34, 34, 34]} rows={rows} size={18} border="#cfcfcf" />
    </GSlide>
  )
}

function Club() {
  const cells = [[1038, 0], [800, 239], [1038, 478]]
  return (
    <GSlide>
      <Ph x={0} y={0} w={1038} h={720} label="golf course photo with green overlay" tone="#9fb99a" />
      <Ph x={1038} y={239} w={242} h={239} label="golf ball photo" />
      <Dots x={70} y={67} color={W} />
      {club.title.map((l, i) => (
        <Txt key={l} x={126} cy={237 + i * 50} size={44} className={cn(t.latin, 'font-extrabold')} style={{ color: W }}>{l}</Txt>
      ))}
      <Abs x={128} y={329} w={97} h={4} style={{ background: W }} />
      <Txt x={127} cy={414} size={21} lh={31} className="font-bold" style={{ color: W }}>{club.lead}</Txt>
      <Txt x={127} cy={491} size={17} lh={28.5} className="font-light" style={{ color: W }}>{club.body}</Txt>
      {club.cells.map((c, i) => {
        const [x, y] = cells[i]
        return (
          <div key={c.title}>
            <Abs x={x} y={y} w={i === 1 ? 238 : 242} h={239} style={{ background: t.bg }} />
            <IconDisc cx={x + 120} cy={y + 75} r={45}>
              {i === 0 ? <Flag size={34} color={W} /> : <Ph x={28} y={26} w={34} h={38} label={i === 1 ? 'golf bag icon' : 'golf ball icon'} tone="#cfe0cb" />}
            </IconDisc>
            <Txt x={x + 120} cy={y + 146} size={18} align="center" w={230} className="tracking-[-0.03em]" style={{ color: t.green }}>{c.title}</Txt>
            <Txt x={x + 120} cy={y + 173} size={14} lh={21} align="center" w={230} className="font-light" style={{ color: '#888' }}>{c.text}</Txt>
          </div>
        )
      })}
    </GSlide>
  )
}

function Budget() {
  const H = (s: string, colSpan = 3): Cell => ({ text: s, head: true, colSpan })
  const m = budget.money
  const rows: Cell[][] = [
    [H('수 입'), H('지 출')],
    [{ text: '구 분', colSpan: 2 }, { text: '금 액' }, { text: '구 분', colSpan: 2 }, { text: '금 액' }],
    [{ text: '회비', rowSpan: 3 }, { text: '가입비' }, { text: m }, { text: '운영비', rowSpan: 3 }, { text: '인건비' }, { text: m }],
    [{ text: '월회비' }, { text: m }, { text: '활동비' }, { text: m }],
    [{ text: '소계' }, { text: m }, { text: '소계' }, { text: m }],
    [{ text: '합계', colSpan: 2 }, { text: m }, { text: '합계', colSpan: 2 }, { text: m }],
  ]
  return (
    <GSlide>
      <Abs x={0} y={571} w={1280} h={149} style={{ background: t.green }} />
      <Dots x={1114} y={792 - 728} />
      <Ring cx={1202} cy={115} r={22} />
      <Header title={budget.title} en={budget.en} />
      <Txt x={631} cy={219} size={18} align="center" w={400} className="font-light" style={{ color: t.green }}>{budget.caption}</Txt>
      {budget.donuts.map((v, i) => {
        const cx = [271, 506, 770, 1022][i]
        return (
          <div key={i}>
            <Donut cx={cx} cy={345} r={86} ring={20} value={v} />
            <Txt x={cx} cy={345} size={40} align="center" w={160} className={cn(t.latin, 'font-bold')} style={{ color: t.green }}>{v}%</Txt>
            <Abs x={cx - 47} y={437} className="flex items-center gap-1 leading-none whitespace-nowrap" style={{ fontSize: 11, color: '#666' }}>
              {budget.legend.map((l, j) => <span key={l} className="flex items-center gap-[2px]"><span className="inline-block h-[10px] w-[10px]" style={{ background: j ? '#c8c8c8' : t.green }} />{l}</span>)}
            </Abs>
          </div>
        )
      })}
      <Grid x={129} y={477} cols={[103, 126, 232, 129, 131, 300]} rowH={[29, 30, 30, 30, 30, 30]} rows={rows} size={16} />
    </GSlide>
  )
}

function Partners() {
  const xs = [139, 402, 661, 927]
  return (
    <GSlide>
      <Hatch x={918} y={0} w={212} h={154} />
      <Dots x={70} y={78} />
      <Square x={1158} y={88} s={38} />
      <Header title={partners.title} en={partners.en} desc={partners.desc} y={168} />
      {partners.items.map((p, i) => (
        <div key={p.name}>
          <Ph x={xs[i]} y={271} w={231} h={170} label="partner photo" />
          <Abs x={xs[i]} y={462} w={231} h={35} className="flex items-center justify-center whitespace-nowrap leading-none" style={{ background: t.green, color: W, fontSize: 20 }}>{p.name}</Abs>
          <Txt x={xs[i]} cy={531} size={14} lh={21} w={240} className="font-light" style={{ color: '#888' }}>{p.text}</Txt>
        </div>
      ))}
    </GSlide>
  )
}

function Thanks() {
  return (
    <GSlide>
      <Ph x={167} y={0} w={935} h={231} label="dotted world map" />
      <Abs x={0} y={231} w={1280} h={250} style={{ background: t.green }} />
      <Hatch x={903} y={231} w={254} h={82} tone="#a2c09c" />
      <Hatch x={141} y={481} w={253} h={76} />
      <Dots x={100} y={65} />
      <Cross cx={120} cy={116} />
      <Cross cx={1114} cy={96} />
      <Ring cx={1153} cy={151} r={22} />
      <Txt x={640} cy={360} size={78} align="center" w={800} className={cn(t.latin, 'font-extrabold tracking-[-0.02em]')} style={{ color: W }}>{thanks.title}</Txt>
      <Txt x={931} cy={542} size={16} style={{ color: t.green }}>{thanks.company}</Txt>
      <Txt x={931} cy={567} size={12} style={{ color: t.green }}>{thanks.address}</Txt>
      <Txt x={931} cy={590} size={11} style={{ color: t.green }}>{thanks.copy}</Txt>
      <Dots x={1080} y={660} />
    </GSlide>
  )
}

const deck: DeckDefinition = {
  id: '23',
  title: '그린톤의 비즈골프사업 투자제안서 골프클럽 리조트 사업개요 예산안 기대효과',
  slides: [Cover, Overview, Contents, Market, Marketing, Values, Finance, Income, Club, Budget, Partners, Thanks],
}
export default deck
