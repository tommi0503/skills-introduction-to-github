import type { DeckDefinition } from '../../ui'
import { Abs, Slide } from '../../ui'
import { CircleCheck, Crosshair, Feather, Flag, ShieldCheck, Trophy } from 'lucide-react'
import { Barred, Box, Display, Lines, Pill, Ph, Txt } from './components'
import { accessories, best, categories, concept, contents, cover, detail, features, lineup, lookbook, promo, season, section, styling } from './data'
import { t } from './theme'

const Note = ({ x = 1235, cy = 692, color = '#9a9a9a' }: { x?: number; cy?: number; color?: string }) => (
  <Txt x={x} cy={cy} size={11} align="right" w={300} style={{ color }}>{t.note}</Txt>
)
const SeasonPill = ({ y = 59 }: { y?: number }) => <Pill x={35} y={y} w={246} h={44} size={24}>{season}</Pill>

/** White page with the left title column (season pill, two-tone display, subtitle, barred blurb). */
function TitlePage({ title, sub, body, children, size = 82, pill = true, top = 0 }: { title: readonly [string, string]; sub: string; body?: readonly string[]; children: React.ReactNode; size?: number; pill?: boolean; top?: number }) {
  return (
    <Slide background="#fff" style={{ color: t.ink }}>
      <Abs x={0} y={0} w={560} h={720} style={{ background: 'linear-gradient(90deg,#f4f4f2,#fff)' }} />
      {pill && <SeasonPill y={59 + top} />}
      <Display x={40} cy={162 + top} size={size} gap={84} words={title} sub={sub} subCy={318 + top} />
      {body && <Barred x={35} cy0={624} lines={body} size={20} gap={31} />}
      {children}
    </Slide>
  )
}

function Cover() {
  return (
    <Slide background="#fff" style={{ color: t.ink }}>
      <Txt x={34} cy={113} size={124} className={t.display}>{cover.title}</Txt>
      <SeasonPill y={209} />
      <Txt x={343} cy={235} size={26} className="font-semibold" style={{ color: t.green }}>{cover.sub}</Txt>
      <Ph x={35} y={286} w={1210} h={388} label="golf course photo" className="rounded-br-[180px]" />
      <Ph x={1022} y={556} w={142} h={142} label="golf ball" className="rounded-full" />
      <Txt x={35} cy={692} size={12} style={{ color: '#9a9a9a' }}>{t.note}</Txt>
    </Slide>
  )
}

function Contents() {
  return (
    <Slide background="#fff" style={{ color: t.ink }}>
      <Ph x={150} y={520} w={1130} h={200} label="golf course photo" className="rounded-tl-[600px_200px]" />
      <Txt x={47} cy={91} size={92} className={t.display}>{contents.title}</Txt>
      <Pill x={460} y={81} w={132} h={47} size={22}>{contents.tag}</Pill>
      {contents.cols.map((c, ci) => {
        const x = 48 + ci * 356
        return (
          <div key={c.no}>
            <Txt x={x} cy={245} size={80} className={t.display} style={{ color: t.green }}>{c.no}</Txt>
            <Txt x={x + 103} cy={229} size={24} className="font-bold tracking-[-0.02em]" style={{ color: t.green }}>{c.en}</Txt>
            <Txt x={x + 103} cy={259} size={21}>{c.kr}</Txt>
            <Box x={x} y={291} w={306} h={1.5} fill={t.light} />
            {c.items.map((it, i) => {
              const n = [0, 3, 8][ci] + i + 1
              return (
                <div key={it}>
                  <Txt x={x + (n > 9 ? -2 : 3)} cy={322 + i * 33.5} size={20} style={{ color: t.light }}>{String(n)}</Txt>
                  <Txt x={x + 40} cy={322 + i * 33.5} size={21}>{it}</Txt>
                </div>
              )
            })}
          </div>
        )
      })}
      <Note x={1240} cy={694} color="#fff" />
    </Slide>
  )
}

function Concept() {
  return (
    <Slide background={t.photoDark} style={{ color: '#fff' }}>
      <Ph x={0} y={0} w={1280} h={720} label="aerial golf course photo" tone={t.photoDark} />
      <Abs x={60} y={65} w={352} h={46} className="flex items-center justify-center rounded-full leading-none" style={{ border: `1.5px solid ${t.light}`, color: t.light, fontSize: 22 }}>{concept.tag}</Abs>
      {concept.title.map((l, i) => <Txt key={l} x={58} cy={222 + i * 95} size={88} className={t.display} style={{ color: '#fff' }}>{l}</Txt>)}
      <Txt x={59} cy={473} size={28} className="font-semibold" style={{ color: t.light }}>{concept.lead}</Txt>
      <Lines x={59} cy0={535} gap={29.5} size={20} lines={concept.body} style={{ color: '#fff' }} />
      {concept.tags.map((g, i) => (
        <div key={g}>
          <Txt x={1223} cy={340 + i * 40} size={20} align="right" w={200} style={{ color: '#bdbdbd' }}>{g}</Txt>
          <Abs x={1235} y={335 + i * 40} w={10} h={10} className="rounded-full" style={{ background: '#bdbdbd' }} />
        </div>
      ))}
    </Slide>
  )
}

function Lookbook() {
  const cells: [number, number, number, number][] = [[552, 58, 217, 405], [777, 58, 217, 199], [1001, 58, 217, 199], [777, 264, 217, 199], [1001, 264, 217, 199], [552, 470, 217, 199], [777, 470, 217, 199], [1001, 470, 217, 199]]
  return (
    <TitlePage title={lookbook.title} sub={lookbook.sub} body={lookbook.body}>
      {cells.map(([x, y, w, h], i) => <Ph key={i} x={x} y={y} w={w} h={h} label="lookbook photo" />)}
      <Note x={1218} cy={685} />
    </TitlePage>
  )
}

const featureIcons = [Flag, Crosshair, Feather, ShieldCheck]
function Features() {
  return (
    <Slide background={t.photoDark} style={{ color: '#fff' }}>
      <Ph x={0} y={0} w={1280} h={720} label="dark golf course photo" tone="#1c211a" />
      <Txt x={73} cy={104} size={86} className={t.display} style={{ color: '#fff' }}>{features.title}</Txt>
      <Txt x={74} cy={183} size={27} className="font-semibold" style={{ color: t.light }}>{features.sub}</Txt>
      <Lines x={74} cy0={235} gap={30} size={19} lines={features.body} style={{ color: '#fff' }} />
      {features.items.map((f, i) => {
        const x = 75 + i * 290.5
        const Icon = featureIcons[i]
        return (
          <div key={f.en}>
            <Abs x={x} y={320} w={258} h={364} className="rounded-[10px]" style={{ border: `1.5px solid ${t.light}`, background: 'rgba(255,255,255,0.04)' }} />
            <Abs x={x + 60} y={346} w={138} h={138} className="flex items-center justify-center rounded-full" style={{ border: `1.5px solid ${t.light}` }}>
              <Icon size={64} color={t.light} strokeWidth={1.3} />
            </Abs>
            <Txt x={x + 16} cy={527} size={17} className="font-semibold" style={{ color: t.light }}>{`Point ${i + 1}.`}</Txt>
            <Txt x={x + 16} cy={565} size={20} className="font-medium tracking-[0.01em]" style={{ color: '#fff' }}>{f.en}</Txt>
            <Box x={x + 16} y={592} w={226} h={1} fill="rgba(255,255,255,0.4)" />
            <Lines x={x + 16} cy0={621} gap={23} size={18} lines={f.kr} style={{ color: '#fff' }} />
          </div>
        )
      })}
    </Slide>
  )
}

function Categories() {
  return (
    <TitlePage title={categories.title} sub={categories.sub} body={categories.body}>
      {categories.items.map(([en, kr, d], i) => {
        const x = 495 + (i % 3) * 254
        const y = i < 3 ? 83 : 396
        return (
          <div key={en}>
            <Box x={x} y={y} w={229} h={285} r={8} fill="#fff" style={{ boxShadow: '0 1px 4px rgba(0,0,0,0.06)' }} />
            <Ph x={x} y={y} w={229} h={200} label={`${en} photo`} className="rounded-t-[8px]" />
            <Txt x={x + 12} cy={y + 222} size={18} className="font-bold" style={{ color: t.green }}>{en}<span className="px-[8px] font-normal" style={{ color: '#ccc' }}>|</span>{kr}</Txt>
            <Txt x={x + 12} cy={y + 252} size={15}>{d}</Txt>
          </div>
        )
      })}
    </TitlePage>
  )
}

function Section() {
  return (
    <Slide background="#111" style={{ color: '#fff' }}>
      <Ph x={0} y={0} w={1280} h={720} label="iron and golf ball photo" tone="#2a2d24" />
      <Txt x={42} cy={180} size={170} className={t.display} style={{ color: t.green }}>{section.no}</Txt>
      <Txt x={46} cy={308} size={92} className={t.display} style={{ color: '#fff' }}>{section.title}</Txt>
      <Txt x={48} cy={400} size={28} className="font-semibold" style={{ color: t.light }}>{section.sub}</Txt>
      {section.items.map(([n, en, kr], i) => {
        const x = [48, 262, 477, 691, 906][i]
        return (
          <div key={n}>
            {i > 0 && <Box x={x - 18} y={598} w={1.5} h={95} fill={t.green} />}
            <Txt x={x} cy={609} size={21} className="font-semibold" style={{ color: t.green }}>{n}</Txt>
            <Txt x={x} cy={642} size={21} className="font-medium" style={{ color: t.light }}>{en}</Txt>
            <Txt x={x} cy={677} size={21} style={{ color: '#fff' }}>{kr}</Txt>
          </div>
        )
      })}
    </Slide>
  )
}

function Best() {
  const rows = [
    { y: 0, img: [387, 0, 288, 240], tx: 698, px: 1052, by: 0 },
    { y: 240, img: [992, 240, 288, 240], tx: 412, px: 752, by: 240 },
    { y: 480, img: [387, 480, 288, 240], tx: 698, px: 1052, by: 480 },
  ]
  return (
    <TitlePage title={best.title} sub={best.sub} body={best.body}>
      <Box x={387} y={240} w={893} h={240} fill="#fff" />
      {[240, 480].map((y) => <Box key={y} x={387} y={y} w={893} h={1.5} fill={t.light} />)}
      {best.items.map((b, i) => {
        const r = rows[i]
        const [ix, iy, iw, ih] = r.img
        return (
          <div key={b.name}>
            <Ph x={ix} y={iy} w={iw} h={ih} label="product photo" />
            <Pill x={r.tx} y={r.by + 31} w={160} h={34} size={17}><Trophy size={20} className="mr-[8px]" />{`BEST 0${i + 1}`}</Pill>
            <Txt x={r.tx} cy={r.by + 101 - (i === 1 ? 0 : 0)} size={18} className="font-bold">{b.name}</Txt>
            <Lines x={r.tx} cy0={r.by + 134} gap={20} size={15.5} lines={b.desc} style={{ color: t.muted }} />
            <Txt x={r.tx} cy={r.by + 191} size={25} className="font-bold" style={{ color: t.green }}>{b.price}</Txt>
            <Box x={r.px - 26} y={r.by + 92} w={1} h={110} fill="#ccc" />
            {(() => {
              let k = 0
              return b.points.map((p, j) => {
                const cy = r.by + (i === 1 ? 108 : 104) + k * 20 + j * 10
                k += p.length
                return (
                  <div key={j}>
                    <Txt x={r.px} cy={cy} size={15}>•</Txt>
                    <Lines x={r.px + 16} cy0={cy} gap={20} size={15.5} lines={p} />
                  </div>
                )
              })
            })()}
          </div>
        )
      })}
    </TitlePage>
  )
}

function Lineup() {
  const cx = [648, 788, 969, 1164]
  return (
    <TitlePage title={lineup.title} sub={lineup.sub} top={-728 + 728 - 0}>
      <Barred x={35} cy0={523} lines={lineup.body} head={lineup.head} size={20} gap={30.5} bar={7} />
      {[728, 1090].map((x) => <Box key={x} x={x} y={124} w={x === 728 ? 122 : 148} h={566} fill={t.pale} />)}
      <Box x={438} y={65} w={800} h={2} fill="#2e3326" />
      {lineup.cols.map((c, i) => <Txt key={c} x={cx[i]} cy={95} size={17} align="center" w={200} className="font-medium" style={{ color: t.green }}>{c}</Txt>)}
      <Box x={438} y={124} w={800} h={1.5} fill="#ccc" />
      {lineup.rows.map(([name, play, feat, price], i) => {
        const cy = 170 + i * 94
        return (
          <div key={i}>
            <Ph x={462} y={cy - 38} w={84} h={76} label="club image" />
            <Lines x={cx[0]} cy0={cy - (name.length - 1) * 13} gap={26} size={18} align="center" w={180} lines={name} />
            <Txt x={cx[1]} cy={cy} size={17} align="center" w={120}>{play}</Txt>
            <Txt x={cx[2]} cy={cy} size={17} align="center" w={240}>{feat}</Txt>
            <Txt x={cx[3]} cy={cy} size={18} align="center" w={148} className="font-bold">{price}</Txt>
            {i < 5 && <Box x={438} y={cy + 46} w={800} h={1} fill="#ccc" />}
          </div>
        )
      })}
      <Box x={438} y={689} w={800} h={2} fill="#2e3326" />
    </TitlePage>
  )
}

function Detail() {
  const d = detail
  return (
    <Slide background="#fff" style={{ color: t.ink }}>
      <Ph x={757} y={0} w={523} h={720} label="driver on tee photo" />
      {[306, 438, 570].map((y) => <Ph key={y} x={1128} y={y} w={116} h={116} label="driver head detail" tone="#f3f3f3" className="rounded-[6px]" />)}
      <Display x={35} cy={88} size={86} words={d.title} inline sub={d.sub} subCy={165} />
      <Abs x={35} y={212} w={400} h={44} className="flex items-center whitespace-nowrap px-[8px] font-bold leading-none" style={{ background: `linear-gradient(90deg, ${t.green} 55%, #fff)`, color: '#fff', fontSize: 18 }}>{d.band}</Abs>
      <Lines x={35} cy0={285} gap={29} size={17} lines={d.body} />
      <Box x={475} y={212} w={252} h={110} r={12} fill={t.green} />
      <Txt x={601} cy={242} size={17} align="center" w={252} style={{ color: '#a9c08c' }}>{d.priceLabel}</Txt>
      <Txt x={601} cy={285} size={38} align="center" w={252} className="font-bold" style={{ color: '#fff' }}>{d.price}</Txt>
      <Abs x={35} y={346} w={620} h={42} className="flex items-center whitespace-nowrap px-[8px] font-bold leading-none" style={{ background: `linear-gradient(90deg, ${t.green} 50%, #fff)`, color: '#fff', fontSize: 18 }}>{d.key}</Abs>
      {d.features.map(([h, ...ls], i) => {
        const cx = 139 + i * 242
        return (
          <div key={h}>
            {i > 0 && <Box x={cx - 121} y={406} w={1} h={120} fill="#ddd" />}
            <Abs x={cx - 11} y={407} w={22} h={22} className="flex items-center justify-center rounded-full font-bold leading-none" style={{ background: t.green, color: '#fff', fontSize: 14 }}>{String(i + 1)}</Abs>
            <Txt x={cx} cy={448} size={15} align="center" w={240} className="font-bold" style={{ color: t.green }}>{h}</Txt>
            <Lines x={cx} cy0={477} gap={19.5} size={14.5} align="center" w={240} lines={ls} />
          </div>
        )
      })}
      {d.specs.map((col, ci) => {
        const x = 35 + ci * 357
        return (
          <div key={ci}>
            <Box x={x} y={548} w={335} h={140} fill="#fff" />
            <Box x={x} y={548} w={167} h={140} fill={t.pale} />
            {col.map(([k, v], i) => (
              <div key={k}>
                <Box x={x} y={548 + i * 35} w={335} h={1} fill="#c9c9c9" />
                <Txt x={x + 84} cy={565 + i * 34.5} size={14.5} align="center" w={160}>{k}</Txt>
                <Txt x={x + 251} cy={565 + i * 34.5} size={14.5} align="center" w={160}>{v}</Txt>
              </div>
            ))}
            <Box x={x + 167} y={548} w={1} h={140} fill="#c9c9c9" />
            <Box x={x} y={687} w={335} h={1} fill="#c9c9c9" />
          </div>
        )
      })}
    </Slide>
  )
}

function Styling() {
  const s = styling
  return (
    <Slide background="#fff" style={{ color: t.ink }}>
      <Abs x={0} y={0} w={560} h={720} style={{ background: 'linear-gradient(90deg,#f4f4f2,#fff)' }} />
      <Display x={35} cy={90} size={86} words={s.title} inline sub={s.sub} subCy={166} />
      <Lines x={35} cy0={220} gap={30.5} size={20} lines={s.body} />
      <Barred x={35} cy0={385} lines={s.point.lines} head={s.point.head} size={20} gap={31} bar={7} />
      <Barred x={35} cy0={541} lines={s.tip.lines} head={s.tip.head} size={20} gap={33} bar={7} />
      <Ph x={505} y={80} w={200} h={590} label="female golfer model" />
      {s.items.map(([n, kr, en, price], i) => {
        const x = 723 + (i % 2) * 262
        const y = 85 + Math.floor(i / 2) * 200
        return (
          <div key={n}>
            <Box x={x} y={y} w={248} h={188} r={6} fill="#fff" style={{ border: '1px solid #f0f0f0' }} />
            <Ph x={x + 120} y={y + 20} w={115} h={115} label={`${en.join(' ')} image`} />
            <Txt x={x + 21} cy={y + 27} size={20} className="font-bold" style={{ color: t.green }}>{n}</Txt>
            <Txt x={x + 21} cy={y + 51} size={16} className="font-semibold" style={{ color: t.green }}>{kr}</Txt>
            <Lines x={x + 21} cy0={y + 84} gap={20} size={16} lines={en} style={{ color: '#9a9a9a' }} />
            <Txt x={x + 21} cy={y + 157} size={20} className="font-bold" style={{ color: t.green }}>{price}</Txt>
          </div>
        )
      })}
      <Note x={1235} cy={688} />
    </Slide>
  )
}

function Accessories() {
  return (
    <TitlePage title={accessories.title} sub={accessories.sub} body={accessories.body}>
      {accessories.items.map(([n, name, desc, price], i) => {
        const x = 558 + (i % 2) * 352
        const y = 69 + Math.floor(i / 2) * 209
        return (
          <div key={n}>
            <Box x={x} y={y} w={337} h={200} r={4} fill="#fff" style={{ border: '1px solid #eee' }} />
            <Ph x={x} y={y} w={140} h={200} label={`${name[0]} photo`} />
            <Txt x={x + 155} cy={y + 25} size={17} className="font-bold" style={{ color: t.green }}>{n}</Txt>
            <Lines x={x + 155} cy0={y + 52} gap={20} size={16} lines={name} className="font-bold" style={{ color: t.green }} />
            <Lines x={x + 155} cy0={y + 103} gap={15} size={12} lines={desc} style={{ color: t.muted }} />
            <Txt x={x + 155} cy={y + 174} size={18} className="font-bold" style={{ color: t.green }}>{price}</Txt>
          </div>
        )
      })}
    </TitlePage>
  )
}

function Promo() {
  const p = promo
  return (
    <Slide background="#eef0ea" style={{ color: t.ink }}>
      <Ph x={0} y={300} w={1280} h={420} label="golf course background" tone="#dfe4d5" />
      <Ph x={60} y={420} w={500} h={290} label="cap, gloves and golf balls" />
      <Display x={35} cy={100} size={86} gap={84} words={p.title} sub={p.sub} subCy={258} />
      <Barred x={37} cy0={342} lines={p.event} size={19} gap={30} bar={7} />
      <Box x={640} y={66} w={501} h={584} r={18} fill={t.green} />
      <Txt x={700} cy={121} size={30} className="font-semibold" style={{ color: '#fff' }}>{p.kicker}</Txt>
      <Txt x={694} cy={240} size={196} className={t.display} style={{ color: '#fff', letterSpacing: '-0.08em' }}>{p.pct}</Txt>
      <Txt x={940} cy={180} size={74} className={t.display} style={{ color: '#fff' }}>{p.unit[0]}</Txt>
      <Txt x={938} cy={270} size={70} className="font-extrabold tracking-[-0.04em]" style={{ color: '#fff' }}>{p.unit[1]}</Txt>
      <Box x={669} y={344} w={443} h={2} fill="#a9c08c" />
      {p.perks.map((k, i) => (
        <div key={k}>
          <Abs x={700} y={371 + i * 58}><CircleCheck size={40} color={t.green} fill="#a9c08c" strokeWidth={2.4} /></Abs>
          <Txt x={754} cy={391 + i * 58} size={24} style={{ color: '#fff' }}>{k}</Txt>
        </div>
      ))}
      <Abs x={670} y={554} w={445} h={73} className="flex items-center justify-center rounded-full bg-white font-semibold leading-none" style={{ color: t.green, fontSize: 30 }}>{p.period}</Abs>
      <Ph x={1088} y={522} w={162} h={162} label="golf ball" className="rounded-full" />
    </Slide>
  )
}

const deck: DeckDefinition = {
  id: '33',
  title: '초록 심플 골프 시즌 카탈로그',
  slides: [Cover, Contents, Concept, Lookbook, Features, Categories, Section, Best, Lineup, Detail, Styling, Accessories, Promo],
}
export default deck
