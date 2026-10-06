import { AlarmClock, Check, Headset, House, Image, MapPin, Star } from 'lucide-react'
import type { DeckDefinition } from '../../ui'
import { Abs, Slide } from '../../ui'
import { Dashed, Page, Ph, Pill, Txt } from './components'
import { checklist, concepts, contact, cover, curriculum, ending, faq, guide, interview, managers, roadmap, specialties, toc, trends } from './data'
import { t } from './theme'

const W = '#fff'

function Cover() {
  return (
    <Slide background="#bfe3f3" className={t.font} style={{ color: t.ink }}>
      <Ph x={0} y={0} w={1280} h={720} label="mountain village and rapeseed field illustration" />
      <Txt x={1241} cy={39} size={14} align="right" w={400} style={{ color: '#444' }}>{t.org}</Txt>
      <Abs x={490} y={84}>
        <svg width={320} height={80} className="overflow-visible">
          <path id="d28arc" d="M 10 70 Q 160 -10 310 70" fill="none" />
          <text fontSize={21} fill={t.deep} fontFamily="Poppins" fontWeight={500} textAnchor="middle"><textPath href="#d28arc" startOffset="50%">{cover.arc}</textPath></text>
        </svg>
      </Abs>
      <Txt x={640} cy={203} size={94} align="center" w={1000} className="font-bold tracking-[-0.03em]" style={{ color: t.deep }}>{cover.title}</Txt>
      <Abs x={448} y={283} w={382} h={41} className="flex items-center justify-center gap-[10px] whitespace-nowrap rounded-full font-semibold leading-none" style={{ background: t.yellow, fontSize: 22 }}>
        {cover.pill[0]}<span style={{ fontSize: 16 }}>×</span>{cover.pill[1]}
      </Abs>
    </Slide>
  )
}

function Toc() {
  return (
    <Page tag={toc.tag} title={toc.title} panel={false}>
      <Ph x={145} y={309} w={261} h={283} label="farmer planting illustration" />
      <Ph x={855} y={476} w={189} h={131} label="puppy and fence illustration" />
      {toc.items.map((it, i) => (
        <div key={it}>
          <Pill cx={475} cy={293 + i * 65} w={65} h={29} size={17}>{`0${i + 1}`}</Pill>
          <Txt x={521} cy={293 + i * 65} size={21} className="font-medium">{it}</Txt>
          <Dashed x={442} y={325 + i * 65} w={370} />
        </div>
      ))}
    </Page>
  )
}

function Cylinder({ x, top, base, w, color, cap }: { x: number; top: number; base: number; w: number; color: string; cap: string }) {
  const eh = 44
  return (
    <>
      <Abs x={x} y={base - eh / 2} w={w} h={eh} className="rounded-[50%]" style={{ background: color, filter: 'brightness(0.9)' }} />
      <Abs x={x} y={top + eh / 2} w={w} h={base - top - eh / 2} style={{ background: color }} />
      <Abs x={x} y={top} w={w} h={eh} className="rounded-[50%]" style={{ background: cap }} />
    </>
  )
}

function Trends() {
  const geo = [{ x: 190, top: 412, base: 496 }, { x: 489, top: 357, base: 493 }, { x: 802, top: 313, base: 487 }]
  const cols = [[t.beige, '#e6d9cc'], [t.lime, '#c3dd96'], [t.moss, '#6d985a']]
  const vy = [463, 435, 427]
  return (
    <Page tag={trends.tag} title={trends.title}>
      <Txt x={640} cy={273} size={20} align="center" w={400} className="font-bold" style={{ color: t.deep }}>{trends.caption}</Txt>
      <Ph x={392} y={300} w={95} h={75} label="curved arrow" />
      <Ph x={705} y={262} w={95} h={75} label="curved arrow with note" />
      <Ph x={1010} y={350} w={95} h={160} label="farmer illustration" />
      {trends.bars.map((b, i) => (
        <div key={b.v}>
          <Cylinder {...geo[i]} w={215} color={cols[i][0]} cap={cols[i][1]} />
          {b.now && <Txt x={geo[i].x + 107} cy={381} size={20} align="center" w={200} style={{ color: W }}>{b.now}</Txt>}
          <Abs x={geo[i].x} y={vy[i] - 26} w={215} h={52} className="flex items-baseline justify-center gap-[3px] font-medium leading-none" style={{ color: W }}>
            <span style={{ fontSize: i === 2 ? 50 : 36 }}>{b.v}</span><span style={{ fontSize: i === 2 ? 26 : 18 }}>%</span>
          </Abs>
          <Txt x={geo[i].x + 107} cy={522} size={14} align="center" w={200}>{b.y}</Txt>
        </div>
      ))}
      <Abs x={138} y={559} w={1008} h={1} style={{ background: '#e2dccf' }} />
      <Txt x={640} cy={597} size={16} align="center" w={1000}>{trends.note[0]}<b style={{ color: t.deep }}>{trends.note[1]}</b></Txt>
    </Page>
  )
}

function Concepts() {
  const cx = [312, 639, 966]
  return (
    <Page tag={concepts.tag} title={concepts.title}>
      <Abs x={528} y={252} w={222} h={370} className="rounded-[16px]" style={{ background: '#8eb79e' }} />
      {concepts.heads.map((h, i) => <Txt key={h} x={cx[i]} cy={304} size={24} lh={37} align="center" w={360} className="font-medium" style={{ color: i === 1 ? W : t.deep }}>{h}</Txt>)}
      {[376, 443, 511, 579].map((y) => [128, 550, 783].map((x, k) => <Dashed key={`${x}${y}`} x={x} y={y} w={k === 1 ? 178 : 367} />))}
      {concepts.rows.map((r, ri) => r.map((c, ci) => (
        <Txt key={`${ri}${ci}`} x={cx[ci]} cy={410 + ri * 67.5} size={18} align="center" w={360} className={ci === 1 ? 'font-bold' : ''} style={{ color: ci === 1 ? W : t.ink }}>{c}</Txt>
      )))}
    </Page>
  )
}

function Roadmap() {
  return (
    <Page tag={roadmap.tag} title={roadmap.title}>
      <Abs x={0} y={0}>
        <svg width={1280} height={720}><path d="M 190 381 H 1080 A 88 88 0 0 1 1080 558 H 300" fill="none" stroke={t.road} strokeWidth={30} strokeLinecap="round" /></svg>
      </Abs>
      {roadmap.steps.map((s) => (
        <div key={s.n}>
          <Pill cx={s.x + 36} cy={s.cy} w={72} h={27} size={15}>{s.n}</Pill>
          <Txt x={s.x + 84} cy={s.cy} size={18} className="font-medium">{s.label}</Txt>
          <Ph x={s.x + 45} y={s.cy + 35} w={130} h={s.cy > 400 ? 105 : 95} label="farmer step illustration" />
        </div>
      ))}
    </Page>
  )
}

function Guide() {
  const disc = [t.beige, t.lime, t.moss]
  const venn = [{ cx: 922, cy: 348, c: 'rgba(205,191,177,0.85)' }, { cx: 838, cy: 497, c: 'rgba(160,197,110,0.85)' }, { cx: 1000, cy: 497, c: 'rgba(95,127,87,0.88)' }]
  const icons = [House, Image, MapPin]
  return (
    <Page tag={guide.tag} title={guide.title}>
      {guide.items.map(([title, text], i) => {
        const cy = 332 + i * 106, I = icons[i]
        return (
          <div key={title}>
            <Abs x={152} y={cy - 29} w={58} h={58} className="flex items-center justify-center rounded-full" style={{ background: disc[i] }}><I size={26} color={W} strokeWidth={1.6} /></Abs>
            <Txt x={222} cy={cy - 16} size={25} className="font-medium">{title}</Txt>
            <Txt x={222} cy={cy + 20} size={15}>{text}</Txt>
          </div>
        )
      })}
      {venn.map((v, i) => {
        const I = icons[i]
        return (
          <div key={i}>
            <Abs x={v.cx - 113} y={v.cy - 113} w={226} h={226} className="rounded-full" style={{ background: v.c }} />
            <Abs x={v.cx - (i ? 0 : 0) - 28 + (i === 1 ? -8 : i === 2 ? -6 : 0)} y={v.cy - 40 + (i ? 0 : -10)}><I size={52} color={W} strokeWidth={1.4} /></Abs>
          </div>
        )
      })}
      {guide.venn.map((l, i) => <Txt key={l} x={[922, 832, 1000][i]} cy={[372, 513, 513][i]} size={12} align="center" w={120} style={{ color: W }}>{l}</Txt>)}
    </Page>
  )
}

function Specialties() {
  return (
    <Page tag={specialties.tag} title={specialties.title} tagW={194}>
      {[362, 641, 921].map((x) => <Dashed key={x} x={x} y={263} vertical h={355} />)}
      {specialties.items.map((s, i) => {
        const cx = [225, 505, 780, 1058][i]
        return (
          <div key={s.no}>
            <Abs x={cx - 77} y={268} h={30} className="flex items-center gap-[10px] whitespace-nowrap leading-none">
              <span className="flex h-[27px] w-[52px] items-center justify-center rounded-full" style={{ background: t.green, color: W, fontSize: 17 }}>{s.no}</span>
              <span className="font-medium" style={{ fontSize: 23 }}>{s.name}</span>
            </Abs>
            <Ph x={cx - 75} y={325} w={150} h={142} label="fruit basket illustration" />
            <Txt x={cx} cy={496} size={21} align="center" w={260} className="font-bold" style={{ color: t.deep }}>{s.head}</Txt>
            <Txt x={cx} cy={531} size={13.5} lh={23} align="center" w={270}>{s.text}</Txt>
          </div>
        )
      })}
    </Page>
  )
}

function Curriculum() {
  return (
    <Page tag={curriculum.tag} title={curriculum.title} tagW={194}>
      {[467, 821].map((x) => <Dashed key={x} x={x} y={265} vertical h={355} />)}
      {curriculum.items.map(([lvl, name, sub, hours], i) => {
        const x = [128, 482, 838][i], cx = [290, 645, 1000][i]
        return (
          <div key={name}>
            <Abs x={x} y={275} w={329} h={66} style={{ background: t.green, clipPath: 'polygon(0 0, 91% 0, 100% 50%, 91% 100%, 0 100%)', borderRadius: '10px 0 0 10px' }} />
            <Abs x={x + 18} y={295} h={28} className="flex items-center gap-[10px] whitespace-nowrap leading-none" style={{ color: W }}>
              <span className="flex h-[26px] w-[54px] items-center justify-center rounded-full" style={{ background: t.deep, fontSize: 14 }}>{lvl}</span>
              <span className="font-medium" style={{ fontSize: 23 }}>{name}</span>
            </Abs>
            <Txt x={cx} cy={375} size={20} lh={32} align="center" w={320} className="font-medium">{sub}</Txt>
            <Ph x={cx - 133} y={441} w={266} h={84} label="training photo" />
            <Abs x={cx - 106} y={548} h={38} className="flex items-center gap-[10px] whitespace-nowrap font-bold leading-none" style={{ fontSize: 23, color: t.deep }}>
              <AlarmClock size={34} color="#e8823a" strokeWidth={1.8} />{hours}
            </Abs>
          </div>
        )
      })}
      <Txt x={1198} cy={661} size={9} align="right" w={300} style={{ color: '#999' }}>{curriculum.note}</Txt>
    </Page>
  )
}

function Interview() {
  return (
    <Page tag={interview.tag} title={interview.title} tagW={194}>
      {interview.items.map((p, i) => {
        const x = 139 + (i % 2) * 537, y = 290 + Math.floor(i / 2) * 193
        return (
          <div key={p.name}>
            <Abs x={x} y={y} w={488} h={142} className="rounded-[10px] bg-white" />
            <Abs x={x - 20} y={y - 33} w={325} h={79} style={{ background: t.green, clipPath: 'polygon(0 0, 88% 0, 100% 50%, 88% 100%, 0 100%)', borderRadius: '8px 0 0 8px' }} />
            <Txt x={x + 12} cy={y - 7} size={21} className="font-bold" style={{ color: W }}>{p.name}</Txt>
            <Txt x={x + 12} cy={y + 22} size={15} style={{ color: W }}>{p.info}</Txt>
            <Ph x={x + 347} y={y - 6} w={98} h={98} label="portrait photo" className="rounded-full" />
            <Txt x={x + 31} cy={y + 80} size={13} lh={22}>{p.text}</Txt>
            <Abs x={x + 357} y={y + 104} className="flex gap-[1px]">
              {[0, 1, 2, 3, 4].map((k) => <Star key={k} size={15} fill={k < p.stars ? '#f2c240' : '#c8c8c8'} color={k < p.stars ? '#f2c240' : '#c8c8c8'} />)}
            </Abs>
          </div>
        )
      })}
      <Txt x={1198} cy={663} size={9} align="right" w={300} style={{ color: '#999' }}>{interview.note}</Txt>
    </Page>
  )
}

function Checklist() {
  return (
    <Page tag={checklist.tag} title={checklist.title}>
      <Txt x={131} cy={291} size={26} className="font-bold" style={{ color: t.deep }}>{checklist.head}</Txt>
      <Txt x={132} cy={335} size={14} lh={22.5}>{checklist.desc}</Txt>
      <Ph x={130} y={461} w={218} h={159} label="farmer gardening illustration" />
      {checklist.items.map((c, i) => {
        const y = 277 + i * 84
        return (
          <div key={c}>
            <Abs x={399} y={y} w={758} h={73} className="bg-white" />
            <Abs x={432} y={y + 23} w={28} h={28} style={{ background: '#ececec' }} />
            {i === 0 && <Abs x={430} y={y + 10}><Check size={36} color={t.green} strokeWidth={3} /></Abs>}
            <Txt x={471} cy={y + 37} size={20}>{c}</Txt>
          </div>
        )
      })}
    </Page>
  )
}

function Managers() {
  return (
    <Page tag={managers.tag} title={managers.title}>
      {[457, 824].map((x) => <Dashed key={x} x={x} y={263} vertical h={355} />)}
      {managers.items.map((m, i) => {
        const x = [128, 489, 858][i]
        return (
          <div key={m.name}>
            <Pill cx={x + 52} cy={293} w={104} h={27} size={15}>{m.tag}</Pill>
            <Abs x={x} y={320} h={32} className="flex items-baseline gap-[8px] whitespace-nowrap leading-none">
              <span className="font-bold" style={{ fontSize: 24, color: t.deep }}>{m.name}</span>
              <span style={{ fontSize: 14 }}>{m.dept}</span>
            </Abs>
            <Txt x={x} cy={383} size={14} className="font-bold">담당 업무</Txt>
            <Txt x={x} cy={409} size={13.5} lh={23}>{m.duty}</Txt>
            {m.tags.map((tg, k) => <Abs key={tg} x={x + 4} y={518 + k * 31} h={28} className="flex items-center whitespace-nowrap rounded-full bg-white px-[14px] leading-none" style={{ fontSize: 13, color: t.green }}>{tg}</Abs>)}
            <Ph x={x + 178} y={430} w={130} h={167} label="manager illustration" />
          </div>
        )
      })}
    </Page>
  )
}

function Faq() {
  return (
    <Page tag={faq.tag} title={faq.title}>
      {faq.items.map((f, i) => {
        const x = [129, 480, 834][i]
        return (
          <div key={f.a}>
            <Abs x={x} y={268} w={46} h={46} className="flex items-center justify-center rounded-full" style={{ background: t.green, color: W, fontSize: 18 }}>{`Q${i + 1}`}</Abs>
            <Txt x={x + 60} cy={277} size={18} lh={27} className="font-medium">{f.q}</Txt>
            <Abs x={x} y={346} w={318} h={259} className="rounded-[10px] bg-white" />
            <Abs x={x + 16} y={366} w={30} h={30} className="flex items-center justify-center rounded-full font-bold" style={{ background: t.deep, color: W, fontSize: 16 }}>A</Abs>
            <Txt x={x + 58} cy={381} size={17} className="font-bold" style={{ color: t.deep }}>{f.a}</Txt>
            <Abs x={x + 16} y={412} w={286} h={1} style={{ background: '#e4e4e4' }} />
            <Txt x={x + 18} cy={439} size={13.5} lh={23}>{f.text}</Txt>
            <Ph x={x + 205} y={520} w={95} h={80} label="farmer illustration" />
          </div>
        )
      })}
    </Page>
  )
}

function Contact() {
  return (
    <Page tag={contact.tag} title={contact.title} tagW={194}>
      <Abs x={139} y={275} w={50} h={50} className="flex items-center justify-center rounded-full" style={{ background: t.sage }}><Headset size={28} color={W} strokeWidth={1.6} /></Abs>
      <Txt x={206} cy={298} size={28} className="font-bold" style={{ color: t.deep }}>{contact.head}</Txt>
      {[338, 405, 472].map((y) => <Dashed key={y} x={140} y={y} w={527} />)}
      {contact.rows.map(([k, v], i) => (
        <div key={k}>
          <Txt x={142} cy={370 + i * 67} size={21} className="font-bold" style={{ color: t.deep }}>{k}</Txt>
          <Txt x={255} cy={370 + i * 67} size={21}>{v}</Txt>
        </div>
      ))}
      <Abs x={140} y={489} w={104} h={104} className="bg-white p-[8px]"><Ph x={8} y={8} w={88} h={88} label="QR code" /></Abs>
      <Txt x={255} cy={545} size={20} lh={31}>{contact.qr}</Txt>
      <Ph x={697} y={294} w={451} h={305} label="simple street map" />
      <Abs x={928} y={384}><MapPin size={46} fill={t.deep} color={W} strokeWidth={1.4} /></Abs>
      <Txt x={950} cy={446} size={15} align="center" w={200} className="font-bold" style={{ color: t.deep }}>{contact.pin}</Txt>
      {([['농협', 809, 434, 457], ['마을버스\n정류장', 930, 513, 537], ['행복복지센터', 1083, 499, 523]] as const).map(([l, x, dy, ty]) => (
        <div key={l}>
          <Abs x={x - 5} y={dy - 5} w={10} h={10} className="rounded-full" style={{ background: t.sage }} />
          <Txt x={l === '농협' ? x : l.length > 6 ? x : x} cy={ty} size={14} lh={21} align={l.includes('정류장') ? 'left' : 'center'} w={l.includes('정류장') ? 100 : 120} style={{ color: '#555', marginLeft: l.includes('정류장') ? -6 : 0 }}>{l}</Txt>
        </div>
      ))}
    </Page>
  )
}

function Ending() {
  return (
    <Page tag={ending.tag} title="">
      <Txt x={640} cy={175} size={60} align="center" w={800} className="font-medium tracking-[-0.01em]" style={{ color: t.title }}>{ending.title}</Txt>
      {ending.lines.map((l, i) => <Txt key={l} x={197} cy={337 + i * 55} size={40} className="font-bold tracking-[-0.02em]" style={{ color: t.deep }}>{l}</Txt>)}
      <Txt x={197} cy={437} size={15} lh={23}>{ending.desc}</Txt>
      <Abs x={198} y={518} w={375} h={50} className="flex items-center whitespace-nowrap rounded-full pl-[32px] font-medium leading-none" style={{ background: t.green, color: W, fontSize: 24 }}>{ending.pill}</Abs>
      <Ph x={725} y={292} w={365} h={310} label="farmers family illustration" />
    </Page>
  )
}

const deck: DeckDefinition = {
  id: '28',
  title: '노랑 심플 귀농귀촌 가이드북',
  slides: [Cover, Toc, Trends, Concepts, Roadmap, Guide, Specialties, Curriculum, Interview, Checklist, Managers, Faq, Contact, Ending],
}
export default deck
