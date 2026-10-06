import { Atom, ChevronRight, Clapperboard, HandHeart, Lightbulb, Quote } from 'lucide-react'
import type { DeckDefinition } from '../../ui'
import { Abs, cn } from '../../ui'
import { Blob, Box, PSlide, Ph, Pill, Section, Title, Txt, Wave } from './components'
import { agenda, bars, cards, cover, donuts, features, flow, mindmap, photos, points, table, thanks, toc } from './data'
import { t } from './theme'

const W = '#fff'

function Cover() {
  return (
    <PSlide bg={t.pink}>
      <Blob x={0} y={0} w={276} h={174} />
      <Blob x={0} y={631} w={435} h={89} />
      <Blob x={972} y={123} w={308} h={400} />
      <Blob x={972} y={486} w={308} h={234} />
      <Wave x={0} y={457} w={193} h={51} />
      <Ph x={936} y={436} w={300} h={170} label="dot spray pattern" />
      <Box x={326} y={203} w={614} h={109} bg={W} r={55} />
      <Txt x={638} cy={254} size={62} align="center" w={700} className="font-extrabold tracking-[-0.03em]" style={{ color: t.blue }}>{cover.kicker}</Txt>
      <Txt x={638} cy={392} size={122} align="center" w={900} className="font-extrabold tracking-[-0.04em]" style={{ color: t.coral }}>{cover.title}</Txt>
      <Txt x={638} cy={518} size={20} align="center" w={500} style={{ color: t.blue }}>{cover.sub}</Txt>
    </PSlide>
  )
}

function Toc() {
  return (
    <PSlide>
      <Ph x={0} y={0} w={461} h={720} label="stacked books photo" />
      <Wave x={239} y={91} w={215} h={51} />
      <Blob x={1117} y={26} w={163} h={210} />
      <Txt x={543} cy={93} size={50} className="font-montserrat font-bold tracking-[-0.02em]">{toc.title}</Txt>
      {toc.groups.map((g, i) => {
        const x = 544 + (i % 2) * 322, y = 258 + Math.floor(i / 2) * 218
        return (
          <div key={g.no}>
            <Txt x={x} cy={y} size={34} className="font-montserrat font-semibold" style={{ color: t.blue }}>{g.no}</Txt>
            <Txt x={x} cy={y + 52} size={18} lh={32} style={{ color: t.body }}>{g.lines.join('\n')}</Txt>
          </div>
        )
      })}
    </PSlide>
  )
}

const Section1 = () => (
  <Section bg={t.blue} no="01" items={agenda}>
    <Blob x={203} y={487} w={290} h={233} />
    <Ph x={447} y={104} w={119} h={116} label="coral starburst" className="rounded-full" />
    <Ph x={924} y={284} w={174} h={174} label="outline starburst" />
  </Section>
)
const Section2 = () => (
  <Section bg={t.coral} no="02" items={agenda}>
    <Blob x={0} y={515} w={312} h={145} />
    <Ph x={725} y={112} w={112} h={111} label="orange starburst" className="rounded-full" />
    <Ph x={921} y={373} w={174} h={170} label="outline starburst" />
  </Section>
)

function Photos() {
  return (
    <PSlide>
      <Abs x={0} y={0} w={1280} h={325} style={{ background: t.pink }} />
      <Ph x={1088} y={0} w={170} h={150} label="ring doodle" className="rounded-full" />
      <Title cy={93} />
      {photos.items.map((p, i) => {
        const cx = 245 + i * 394
        return (
          <div key={i}>
            <Ph x={cx - 145} y={192} w={290} h={290} label="circular photo" className="rounded-full" />
            <Pill x={cx - 136} y={496} w={272} h={64} bg={t.blue} size={22}>{p.title}</Pill>
            <Txt x={cx} cy={592} size={17} lh={27} align="center" w={360}>{p.text}</Txt>
          </div>
        )
      })}
    </PSlide>
  )
}

function Cards() {
  const xs = [68, 467, 850]
  return (
    <PSlide bg={t.blue}>
      <Ph x={40} y={20} w={170} h={230} label="dot doodles" />
      <Title color={W} subColor="#e3e8fc" />
      {cards.items.map((c, i) => (
        <Box key={i} x={xs[i]} y={222} w={360} h={455} bg={i === 1 ? t.orange : W} r={14}>
          <Ph x={33} y={39} w={293} h={189} label="photo" className="rounded-[36px]" />
          <Txt x={180} cy={280} size={22} align="center" w={340} className="font-bold">{c.title}</Txt>
          <Txt x={180} cy={330} size={17} lh={30} align="center" w={340}>{c.text}</Txt>
        </Box>
      ))}
    </PSlide>
  )
}

function Features() {
  const icons = [Lightbulb, Clapperboard, HandHeart]
  const colors = [t.coral, t.orange, t.coral]
  return (
    <PSlide>
      <Abs x={0} y={0} w={471} h={720} style={{ background: t.blue }} />
      <Ph x={0} y={461} w={254} h={259} label="arc doodle" />
      <Wave x={196} y={474} w={271} h={53} />
      <Txt x={68} cy={94} size={40} lh={61} className="font-extrabold" style={{ color: W }}>{features.title}</Txt>
      <Txt x={68} cy={210} size={15} lh={28} className="font-light" style={{ color: '#e3e8fc' }}>{features.sub}</Txt>
      {features.items.map((f, i) => {
        const cy = 175 + i * 188
        const I = icons[i]
        return (
          <div key={i}>
            <Abs x={537} y={cy - 72} w={144} h={144} className="flex items-center justify-center rounded-full" style={{ background: colors[i] }}><I size={60} color={W} strokeWidth={1.6} /></Abs>
            <Txt x={725} cy={cy - 45} size={22} className="font-bold" style={{ color: colors[i] }}>{f.title}</Txt>
            <Txt x={725} cy={cy + 4} size={18} lh={31} style={{ color: t.body }}>{f.text}</Txt>
          </div>
        )
      })}
    </PSlide>
  )
}

function Flow() {
  const boxes = [[71, t.blue], [286, t.lav], [819, t.lav], [1032, t.blue]] as const
  return (
    <PSlide>
      <Abs x={0} y={0} w={1280} h={200} style={{ background: t.coral }} />
      <Title color={W} subColor="#ffd9d2" cy={96} />
      {boxes.map(([x, bg], i) => (
        <Box key={i} x={x} y={310} w={x === 1032 ? 179 : 171} h={160} bg={bg} r={10} className="flex items-center justify-center">
          <Txt x={x === 1032 ? 90 : 86} cy={67} size={20} lh={26} align="center" w={170} className="font-bold">{flow.keyword}</Txt>
        </Box>
      ))}
      {[261, 480, 796, 1011].map((x) => <Abs key={x} x={x - 12} y={380}><ChevronRight size={26} color="#9b9b9b" strokeWidth={3} /></Abs>)}
      <Abs x={506} y={245} w={268} h={268} className="rounded-full" style={{ background: t.blue }} />
      <Abs x={613} y={290}><Atom size={56} color={W} strokeWidth={1.5} /></Abs>
      <Txt x={640} cy={415} size={22} lh={36} align="center" w={260} className="font-bold" style={{ color: W }}>{flow.center}</Txt>
      <Box x={145} y={538} w={1008} h={116} bg="#fdeeee" r={58} />
      <Abs x={240} y={574} style={{ transform: 'scaleX(-1)' }}><Quote size={36} fill="#555" color="#555" /></Abs>
      <Abs x={1022} y={578}><Quote size={36} fill="#555" color="#555" /></Abs>
      <Txt x={640} cy={580} size={18} lh={30} align="center" w={700}>{flow.quote}</Txt>
    </PSlide>
  )
}

function Bars() {
  const base = 584, k = 2.17
  return (
    <PSlide>
      <Title />
      <Box x={80} y={218} w={497} h={452} bg="#fdeeee" r={30} />
      {[302, 367, 432, 497].map((y) => <Abs key={y} x={148} y={y} w={348} h={1} style={{ background: '#d9c9c9' }} />)}
      <Abs x={148} y={base} w={348} h={1} style={{ background: '#bdbdbd' }} />
      {bars.series.map(([a, b], i) => {
        const x = 162 + i * 87
        return (
          <div key={i}>
            <Abs x={x} y={base - a * k} w={58} h={a * k} style={{ background: t.orange }} />
            <Abs x={x} y={base - (a + b) * k} w={58} h={b * k} style={{ background: t.blue }} />
            <Txt x={x + 29} cy={base - (a * k) / 2} size={25} align="center" w={60} className="font-bold">{a}</Txt>
            <Txt x={x + 29} cy={base - a * k - (b * k) / 2} size={25} align="center" w={60} className="font-bold">{b}</Txt>
          </div>
        )
      })}
      <Abs x={224} y={618} className="flex items-center gap-2 whitespace-nowrap leading-none" style={{ fontSize: 16 }}>
        {bars.legend.map((l, i) => <span key={l} className="flex items-center gap-1"><span className="inline-block h-[14px] w-[14px] rounded-[3px]" style={{ background: i ? t.blue : t.orange }} />{l}</span>)}
      </Abs>
      {bars.notes.map((n, i) => {
        const y = 220 + i * 266
        return (
          <div key={n.no}>
            <Box x={652} y={y} w={560} h={186} bg={t.lav} r={22} />
            <Abs x={892} y={y - 45} w={80} h={80} className="flex items-center justify-center rounded-full font-montserrat font-bold" style={{ background: t.blue, color: W, fontSize: 26 }}>{n.no}</Abs>
            <Txt x={932} cy={y + 74} size={20} align="center" w={540} className="font-bold">{n.title}</Txt>
            <Txt x={932} cy={y + 115} size={17} lh={29} align="center" w={540} style={{ color: t.body }}>{n.text}</Txt>
          </div>
        )
      })}
    </PSlide>
  )
}

function Donuts() {
  const colors = [t.lavMid, t.blue, t.coral]
  return (
    <PSlide>
      <Abs x={0} y={0} w={1280} h={200} style={{ background: t.pink }} />
      <Ph x={0} y={20} w={360} h={150} label="dot spray pattern" />
      <Title />
      {donuts.items.map((d, i) => {
        const cx = 304 + i * 341, c = colors[i]
        return (
          <div key={i}>
            <Abs x={cx - 140} y={260} w={280} h={280} className="rounded-full" style={{ background: `conic-gradient(${c} 0 ${d.v}%, #e6e6e6 0)` }}>
              <div className="absolute rounded-full bg-white" style={{ inset: 20 }} />
            </Abs>
            <Txt x={cx} cy={363} size={52} align="center" w={260} className="font-montserrat font-bold" style={{ color: c }}>{d.v}%</Txt>
            <Txt x={cx} cy={423} size={20} lh={32} align="center" w={260} className="font-bold" style={{ color: c }}>{d.label}</Txt>
            <Txt x={cx} cy={586} size={18} lh={28} align="center" w={340} style={{ color: t.body }}>{donuts.text}</Txt>
          </div>
        )
      })}
    </PSlide>
  )
}

function Points() {
  return (
    <PSlide bg={t.pink}>
      <Abs x={0} y={0} w={1280} h={299} style={{ background: t.coral }} />
      <Wave x={0} y={60} w={257} h={60} />
      <Ph x={1080} y={0} w={180} h={150} label="dot doodles" />
      <Title color={W} subColor="#ffd9d2" cy={96} />
      <Box x={68} y={197} w={1143} h={471} bg={W} r={50} />
      <Blob x={126} y={248} w={374} h={370} label="organic photo" />
      {points.items.map((p, i) => {
        const y = 255 + i * 212
        return (
          <div key={i}>
            <Pill x={548} y={y} w={537} h={44} bg={i ? t.orange : t.blue} size={22}><span className="w-full pl-[33px]">{p.title}</span></Pill>
            <Txt x={581} cy={y + 80} size={19} lh={31} style={{ color: t.body }}>{p.text}</Txt>
          </div>
        )
      })}
    </PSlide>
  )
}

function Table() {
  const cx = [348, 595, 841, 1088]
  return (
    <PSlide bg={t.pink}>
      <Abs x={0} y={0} w={1280} h={187} style={{ background: t.blue }} />
      <Ph x={1030} y={0} w={250} h={150} label="arc and dots doodle" />
      <Blob x={0} y={630} w={240} h={90} />
      <Title color={W} subColor="#e3e8fc" cy={97} />
      <Box x={48} y={245} w={1182} h={413} bg={W} r={44} />
      <Abs x={94} y={288} w={1088} h={3} style={{ background: t.blue }} />
      <Abs x={94} y={346} w={1088} h={3} style={{ background: t.blue }} />
      {table.cols.map((c, i) => <Txt key={c} x={cx[i]} cy={318} size={19} align="center" w={220} className="font-bold">{c}</Txt>)}
      {table.rows.map((r, ri) => {
        const cy = 380 + ri * 61.5
        return (
          <div key={ri}>
            <Txt x={110} cy={cy} size={15} className="font-bold" style={{ color: t.blue }}>{r}</Txt>
            {ri < 3 && <Abs x={94} y={cy + 32} w={1088} h={1} style={{ background: '#9a9a9a' }} />}
            {cx.map((x, ci) => {
              const hi = table.highlights.some(([a, b]) => a === ri && b === ci)
              return hi
                ? <Pill key={ci} x={x - 129} y={cy - 32} w={258} h={64} bg={t.coral} size={16}>{table.strong}</Pill>
                : <Txt key={ci} x={x} cy={cy} size={16} align="center" w={240} style={{ color: t.body }}>{table.cell}</Txt>
            })}
          </div>
        )
      })}
      <Abs x={94} y={597} w={1088} h={1} style={{ background: '#9a9a9a' }} />
    </PSlide>
  )
}

function MindMap() {
  const look = { lav: [t.lav, '#333', false], peach: [t.peach, '#333', false], blue: [t.blue, W, true], orange: [t.orange, W, true] } as const
  const arrows = [
    ['M 540 318 Q 490 280 432 296', t.coral], ['M 570 480 Q 545 540 490 550', t.coral], ['M 720 300 Q 760 255 815 262', t.coral], ['M 712 480 Q 750 520 800 515', t.coral],
    ['M 210 255 Q 175 235 180 192', t.blue], ['M 262 268 Q 262 230 285 213', t.blue], ['M 1078 498 Q 1110 500 1112 532', t.blue], ['M 870 530 Q 830 545 840 600', t.blue],
    ['M 230 545 Q 190 530 190 490', t.orange], ['M 390 580 Q 385 615 350 623', t.orange], ['M 920 230 Q 912 195 935 168', t.orange], ['M 905 293 Q 895 330 912 355', t.orange],
  ] as const
  return (
    <PSlide>
      <Txt x={640} cy={98} size={50} align="center" w={900} className="font-extrabold tracking-[-0.02em]">제목을 입력해주세요</Txt>
      <Abs x={0} y={0}>
        <svg width={1280} height={720}>
          {arrows.map(([d, c], i) => <path key={i} d={d} fill="none" stroke={c} strokeWidth={2} strokeDasharray="6 6" />)}
        </svg>
      </Abs>
      <Abs x={498} y={245} w={284} h={284} className="rounded-full" style={{ background: '#fde0de' }} />
      <Abs x={528} y={275} w={224} h={224} className="rounded-full" style={{ background: t.coral }} />
      <Txt x={640} cy={378} size={24} lh={36} align="center" w={240} className="font-bold" style={{ color: W }}>{mindmap.center}</Txt>
      {mindmap.pills.map((p, i) => {
        const [bg, color, kw] = look[p.kind]
        const h = kw ? 60 : 44
        return <Pill key={i} x={p.x} y={p.y - h / 2} w={p.w} h={h} bg={bg} color={color} bold={kw} size={kw ? 19 : 16}>{kw ? mindmap.keyword : mindmap.leaf}</Pill>
      })}
    </PSlide>
  )
}

function Blank() {
  return (
    <PSlide bg={t.pink}>
      <Abs x={0} y={0} w={1280} h={221} style={{ background: t.coral }} />
      <Wave x={1090} y={41} w={190} h={55} />
      <Blob x={0} y={537} w={360} h={183} />
      <Title color={W} subColor="#ffd9d2" cy={98} />
      <Box x={68} y={205} w={1145} h={474} bg={W} r={30} />
    </PSlide>
  )
}

function Thanks() {
  return (
    <PSlide bg={t.blue}>
      <Blob x={0} y={0} w={376} h={135} />
      <Blob x={1085} y={157} w={195} h={381} />
      <Blob x={981} y={495} w={299} h={225} />
      <Blob x={33} y={641} w={327} h={79} />
      <Ph x={1000} y={150} w={240} h={130} label="dot spray pattern" />
      <Txt x={640} cy={325} size={106} align="center" w={900} className={cn('font-semibold tracking-[-0.04em]', 'font-pretendard')} style={{ color: W }}>{thanks.title}</Txt>
      <Txt x={640} cy={415} size={26} align="center" w={600} style={{ color: '#eef0ff' }}>{thanks.sub}</Txt>
      <Wave x={441} y={511} w={398} h={49} />
    </PSlide>
  )
}

const deck: DeckDefinition = {
  id: '24',
  title: '파스텔톤의 몽글몽글한 느낌의 프레젠테이션',
  slides: [Cover, Toc, Section1, Photos, Cards, Features, Flow, Section2, Bars, Donuts, Points, Table, MindMap, Blank, Thanks],
}
export default deck
