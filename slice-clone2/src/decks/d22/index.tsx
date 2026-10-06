import type { DeckDefinition } from '../../ui'
import { Abs, ImagePlaceholder } from '../../ui'
import { House, Mail, MapPin, Phone } from 'lucide-react'
import { Dotted, HLine, Lines, Page, PhotoBg, RunHead, T, Title } from './components'
import * as d from './data'
import { t } from './theme'

const W = { color: '#fff' } as const
const BL = { color: t.blue } as const
const INK = { color: t.ink } as const

function Cover() {
  const c = d.cover
  return (
    <Page dark>
      <PhotoBg label="city riverside night photo" />
      {d.nav.map((lines, i) => {
        const x = 42 + i * 201.5
        return (
          <div key={i}>
            <HLine x={x} y={35} w={188} c={i ? 'rgba(255,255,255,0.45)' : '#fff'} />
            <Lines lines={lines} x={x} cy={49} pitch={19} size={13} style={{ color: i ? '#8a93b8' : '#fff' }} />
          </div>
        )
      })}
      <Lines lines={c.title} x={40} cy={432} pitch={80.5} size={75.5} className="font-extrabold tracking-[-0.01em]" style={W} />
      <T x={42} cy={666} size={19} className="font-light" style={W}>{c.sub}</T>
    </Page>
  )
}

function Toc() {
  const c = d.toc
  const xs = c.xs
  return (
    <Page>
      <RunHead no="00" label={c.label} />
      <T x={42} cy={127} size={33} className="font-extrabold" style={INK}>{c.title[0]}<span style={{ color: t.blue, marginLeft: 9 }}>{c.title[1]}</span></T>
      {c.cols.map((col, i) => {
        const x = xs[i], w = xs[i + 1] - x
        return (
          <div key={col.n}>
            <Abs x={x} y={203} w={w} h={col.bottom - 203} style={{ background: t.grey }} />
            <T x={x + 17} cy={238} size={31} className="font-extrabold" style={BL}>{col.n}</T>
            <Lines lines={col.label} x={x + 19} cy={col.bottom - 46} pitch={19} size={15} className="font-bold" style={INK} />
            <Lines lines={col.body} x={x + 18} cy={col.bottom + 25} pitch={21} size={13.5} style={{ color: t.sub }} />
          </div>
        )
      })}
      {xs.map((x) => <Abs key={x} x={x} y={203} w={0} h={499} style={{ borderLeft: '1.3px dotted #b8bcc8' }} />)}
      <HLine x={36} y={202} w={1206} c={t.ink} h={1.5} />
      {xs.map((x, i) => <Abs key={x} x={x - 4} y={198} w={0} h={0} style={{ borderTop: '5px solid transparent', borderBottom: '5px solid transparent', [i ? 'borderLeft' : 'borderRight']: `7px solid ${t.ink}` }} />)}
    </Page>
  )
}

function Intro() {
  const c = d.intro
  return (
    <Page dark>
      <PhotoBg label="building photo" />
      <RunHead label={c.label} dark />
      <T x={40} cy={596} size={56} className="font-thin" style={W}>{c.no}</T>
      <T x={137} cy={596} size={70} className="font-extrabold tracking-[-0.01em]" style={W}>{c.name}</T>
      <T x={42} cy={661} size={19} className="font-light" style={W}>{c.sub}</T>
    </Page>
  )
}

function Ceo() {
  const c = d.ceo
  return (
    <Page>
      <Abs x={0} y={500} w={975} h={220} style={{ background: t.grey }} />
      <Abs x={975} y={0} w={305} h={720} style={{ background: t.blue }} />
      <Abs x={676} y={86} w={589} h={634}><ImagePlaceholder label="CEO portrait" className="h-full w-full" /></Abs>
      <RunHead no="01" label="Company Introduction" end={953} />
      <Title lead={c.title[0]} tail={c.title[1]} />
      <T x={42} cy={213} size={24} className="font-medium" style={INK}>{c.quote}</T>
      <Lines lines={c.body} x={42} cy={268} pitch={25.2} size={15.5} />
      <T x={44} cy={429} size={14.5} style={INK}><b className="font-bold">{c.sign[0]}</b><span className="mx-[9px] inline-block h-[14px] w-px bg-[#999]" />{c.sign[1]}</T>
      <Abs x={198} y={408} w={84} h={40}><ImagePlaceholder label="signature" className="h-full w-full" /></Abs>
      {c.goals.map((g, i) => {
        const x = [42, 253, 464][i]
        return (
          <div key={g.n}>
            <T x={x} cy={549} size={13} className="font-bold" style={BL}>{g.n}</T>
            <Lines lines={g.head} x={x} cy={569} pitch={19} size={13} className="font-bold" style={BL} />
            <Lines lines={g.body} x={x} cy={621} pitch={19} size={11.5} style={{ color: t.sub }} />
          </div>
        )
      })}
    </Page>
  )
}

function Company() {
  const c = d.company
  return (
    <Page>
      <RunHead no="01" label="Company Introduction" />
      <Title lead={c.title[0]} tail={c.title[1]} />
      {c.rows.map(([k, v], i) => {
        const cy = 359 + i * 42.3
        return (
          <div key={k}>
            <T x={52} cy={cy} size={15} className="font-bold" style={BL}>{k}</T>
            <T x={147} cy={cy} size={15.5} style={INK}>{v}</T>
            <HLine x={42} y={cy + 22} w={464} c="#9aa0b0" />
            <HLine x={126} y={cy + 13} w={1} c="#9aa0b0" h={9} />
          </div>
        )
      })}
      <Abs x={640} y={109} w={598} h={566} style={{ background: t.grey }} />
      <T x={640} w={598} cy={164} size={19} align="center" className="font-bold" style={INK}>{c.quote}</T>
      {c.keywords.map((k, i) => (
        <Abs key={k} x={[751, 939, 1127][i] - 73} y={221} w={146} h={146} className="flex items-center justify-center rounded-full font-bold" style={{ border: `2px solid ${t.blue}`, color: t.ink, fontSize: 15.5 }}>{k}</Abs>
      ))}
      <HLine x={677} y={412} w={526} c="#9aa0b0" />
      <HLine x={677} y={454} w={526} c="#9aa0b0" />
      <T x={640} w={598} cy={433} size={15.5} align="center" style={INK}>{c.philosophy}</T>
      <Lines lines={c.body} x={677} cy={495} pitch={27.4} size={15.5} />
      <T x={677} cy={631} size={15.5}>{c.last}</T>
    </Page>
  )
}

function Sales() {
  const c = d.sales, tb = c.table
  const mark = (cy: number) => <HLine x={42} y={cy - 7} w={1.2} h={14} c={t.sub} />
  return (
    <Page>
      <RunHead no="02" label="Business Performance" />
      <Title lead={c.title[0]} tail={c.title[1]} />
      <T x={40} cy={208} size={19.5} className="items-baseline font-bold" style={INK}>{c.sub}<span className="font-normal" style={{ fontSize: 11, marginLeft: 8 }}>{c.unit}</span></T>
      {mark(270)}
      <T x={49} cy={270} size={14.5} style={INK}>매출 비중</T>
      {c.share.map(([l, x0, x1], i) => <Abs key={l} x={x0} y={257} w={x1 - x0} h={26} className="flex items-center justify-center text-white" style={{ background: i ? t.blue : t.light, fontSize: 13 }}>{l}</Abs>)}
      {c.groups.map((g) => (
        <div key={g.label}>
          {mark(g.cy)}
          <T x={49} cy={g.cy} size={14.5} style={INK}>{g.label}</T>
          {g.rows.map((r, j) => {
            const cy = g.cy + j * 39
            return (
              <div key={r.year}>
                <T x={144} cy={cy} size={13.5} style={INK}>{r.year}</T>
                <Abs x={211} y={cy - 12} w={r.w} h={24} style={{ background: r.light ? t.light : t.blue }} />
                <T x={218 + r.w} cy={cy} size={13} style={{ color: r.light ? t.light : t.blue }}>{r.v}{r.light && <span style={{ fontSize: 12 }}>백만 원</span>}</T>
              </div>
            )
          })}
        </div>
      ))}
      {[[40, 221], [271, 304]].map(([x, w]) => <HLine key={x} x={x} y={510} w={w} c={t.ink} h={2} />)}
      {[[40, 221], [271, 304]].map(([x, w]) => <HLine key={x} x={x} y={549} w={w} c="#b7bac4" />)}
      <T x={44} cy={529} size={13.5} className="font-bold" style={INK}>부문</T>
      <T x={275} cy={529} size={13.5} className="font-bold" style={INK}>주요 제품</T>
      {c.divisions.map(([a, b], i) => {
        const cy = 572 + i * 41.5
        return (
          <div key={a}>
            <T x={44} cy={cy} size={13.5}>{a}</T>
            <T x={141} cy={cy} size={13.5}>{b}</T>
            <T x={275} cy={cy} size={13.5}>{c.product}</T>
            {i < 2 && <><Dotted x={40} y={cy + 21} w={221} /><Dotted x={271} y={cy + 21} w={304} /></>}
          </div>
        )
      })}
      {[[40, 221], [271, 304]].map(([x, w]) => <HLine key={x} x={x} y={696} w={w} c={t.ink} h={1.5} />)}
      <Abs x={639} y={182} w={599} h={82} style={{ background: t.grey }} />
      <HLine x={639} y={182} w={599} c={t.ink} h={2} />
      <HLine x={878} y={222} w={360} c="#b7bac4" />
      <HLine x={639} y={263} w={599} c={t.ink} h={1.5} />
      <Abs x={878} y={182} w={1} h={493} style={{ background: '#b7bac4' }} />
      <T x={639} w={239} cy={222} size={13.5} align="center" className="font-bold" style={INK}>구분</T>
      <T x={878} w={360} cy={201} size={13.5} align="center" className="font-bold" style={INK}>{tb.head}</T>
      {['2020년도', '2039년도'].map((y, i) => <T key={y} x={[878, 1058][i]} w={180} cy={243} size={13.5} align="center" className="font-bold" style={INK}>{y}</T>)}
      {tb.rows.map((r, i) => {
        const cy = 284 + i * 41.3
        return (
          <div key={r[0]}>
            {r.map((cell, j) => <T key={j} x={[639, 878, 1058][j]} w={[239, 180, 180][j]} cy={cy} size={13.5} align="center" style={INK}>{cell}</T>)}
            {i < 8 && <Dotted x={639} y={cy + 20.5} w={599} />}
          </div>
        )
      })}
      <Abs x={639} y={634} w={599} h={41} style={{ background: t.grey }} />
      <HLine x={639} y={634} w={599} c={t.ink} h={1.5} />
      <HLine x={639} y={675} w={599} c={t.ink} h={1.5} />
      {d.sales.table.total.map((cell, j) => <T key={j} x={[639, 878, 1058][j]} w={[239, 180, 180][j]} cy={655} size={13.5} align="center" className={j ? '' : 'font-bold'} style={INK}>{cell}</T>)}
    </Page>
  )
}

function Network() {
  const c = d.network
  const tb = c.table
  const row = (k: string, v: string, cy: number, bold?: boolean) => (
    <div key={k}>
      <T x={45} cy={cy} size={13.5} className={bold ? 'font-bold' : ''} style={INK}>{k}</T>
      <T x={118} w={96} cy={cy} size={13.5} align="right" className={bold ? 'font-bold' : ''} style={INK}>{v}</T>
    </div>
  )
  return (
    <Page>
      <RunHead no="02" label="Business Performance" />
      <Title lead={c.title[0]} tail={c.title[1]} />
      <Abs x={0} y={198} w={1280} h={522} style={{ background: '#f9f9fb' }} />
      <Abs x={294} y={239} w={986} h={436}><ImagePlaceholder label="world map" tone="#e9eaee" className="h-full w-full" /></Abs>
      <Abs x={42} y={250} w={176} h={42} style={{ background: t.grey }} />
      <HLine x={42} y={250} w={176} c={t.ink} h={2} />
      <HLine x={42} y={292} w={176} c={t.ink} h={1.5} />
      {row(tb.head[0], tb.head[1], 271, true)}
      {tb.a.map(([k, v], i) => <div key={k}>{row(k, v, 311 + i * 41)}{i < 4 && <Dotted x={42} y={331 + i * 41} w={176} />}</div>)}
      <HLine x={42} y={498} w={176} c={t.ink} h={1.5} />
      {tb.b.map(([k, v], i) => <div key={k}>{row(k, v, 528 + i * 42)}{i < 3 && <Dotted x={42} y={549 + i * 42} w={176} />}</div>)}
      <HLine x={42} y={676} w={176} c={t.ink} h={2} />
      <svg className="absolute left-0 top-0" width={1280} height={720}>
        {c.regions.map((r) => <polyline key={r.name} points={r.path.map((p) => p.join(',')).join(' ')} fill="none" stroke={t.blue} strokeWidth={1.3} />)}
      </svg>
      {c.pins.map(([x, y], i) => <Abs key={i} x={x - 10} y={y - 22}><MapPin size={20} fill={t.blue} color="#fff" strokeWidth={1.6} /></Abs>)}
      {c.regions.map((r) => (
        <div key={r.name}>
          <T x={r.x} cy={r.cy} size={14.5} className="font-bold" style={INK}>{r.name}</T>
          {c.kinds.map((k, i) => (
            <div key={k} style={{ color: t.sub }}>
              <T x={r.x} cy={r.cy + 29 + i * 22.7} size={13} className="tracking-[0.02em]">{k}</T>
              <T x={r.x + 77} w={30} cy={r.cy + 29 + i * 22.7} size={13} align="right">{String(r.values[i])}</T>
            </div>
          ))}
        </div>
      ))}
    </Page>
  )
}

function Field() {
  const c = d.field
  return (
    <Page>
      <RunHead no="03" label="Performance by field" />
      <Title lead={c.title[0]} tail={c.title[1]} />
      <T x={40} cy={207} size={18.5} className="items-baseline font-bold" style={INK}>{c.sub}<span className="font-normal" style={{ fontSize: 11, marginLeft: 8 }}>{c.unit}</span></T>
      <T x={36} cy={300} size={82} className="font-extrabold tracking-[-0.02em]" style={BL}>{c.big}</T>
      <Lines lines={c.bigDesc} x={46} cy={375} pitch={20.5} size={12.5} />
      {[450, 577].map((y) => <Dotted key={y} x={42} y={y} w={534} />)}
      {c.rows.map((r) => (
        <div key={r.v}>
          <T x={40} cy={r.cy} size={48} className="font-extrabold tracking-[-0.01em]" style={{ color: t.navy }}>{r.v}</T>
          <Lines lines={r.desc} x={346} cy={r.cy - 10} pitch={20} size={12.5} />
        </div>
      ))}
      {c.kpis.map((k) => (
        <div key={k.label}>
          <Abs x={k.x} y={k.y} w={k.w} h={k.label === '총 고객수' ? 142 : 139} style={{ border: '2px solid #dfe3ee' }} />
          <T x={k.x} w={k.w} cy={k.y + 30} size={18} align="center" className="font-bold" style={BL}>{k.label}</T>
          <T x={k.x} w={k.w} cy={k.y + 87} size={64} align="center" className="items-baseline font-extrabold" style={{ color: k.navy ? t.navy : t.blue }}>{k.v}{k.unit && <span style={{ fontSize: 26 }}>{k.unit}</span>}</T>
        </div>
      ))}
    </Page>
  )
}

function Env() {
  const c = d.env, tech = c.tech, s = c.strategy
  const ring = 'radial-gradient(circle, transparent 86px, #000 87px)'
  return (
    <Page>
      <RunHead no="04" label="Environment" />
      <T x={41} cy={125} size={30} className="font-extrabold" style={BL}>{c.title}</T>
      {c.cols.map((col) => (
        <div key={col.head}>
          <T x={col.x} cy={207} size={19.5} className="font-bold" style={INK}>{col.head}</T>
          <Lines lines={col.lines} x={col.x} cy={244} pitch={21.4} size={13.5} />
          {col.note && <T x={col.x} cy={330} size={10.5}>{col.note}</T>}
        </div>
      ))}
      <T x={871} cy={207} size={19.5} className="font-bold" style={INK}>{tech.head}</T>
      <HLine x={871} y={236} w={1.2} h={14} c={t.sub} />
      <T x={881} cy={243} size={14} className="items-baseline font-bold" style={INK}>{tech.sub}<span className="font-normal" style={{ fontSize: 11, marginLeft: 8 }}>{tech.unit}</span></T>
      {tech.bars.map((b) => (
        <div key={b.year}>
          <T x={879} cy={b.cy} size={13} className="font-bold" style={INK}>{b.year}</T>
          <Abs x={935} y={b.cy - 12} w={b.w} h={24} style={{ background: t.light }} />
          <Abs x={935} y={b.cy - 12} w={b.a - 1} h={24} className="flex items-center pl-[4px] text-white" style={{ background: t.blue, fontSize: 11.5 }}>{b.a}</Abs>
          <T x={935} w={b.w - 5} cy={b.cy} size={11.5} align="right" style={W}>{String(b.b)}</T>
        </div>
      ))}
      <T x={42} cy={396} size={19.5} className="font-bold" style={INK}>{s.head}</T>
      <Lines lines={s.p1} x={42} cy={433} pitch={21.4} size={13.5} />
      <Lines lines={s.p2} x={42} cy={603} pitch={21.4} size={13.5} />
      <T x={42} cy={668} size={10.5}>{s.note}</T>
      <Abs x={458} y={384} w={780} h={291} style={{ background: t.grey }} />
      <Abs x={484} y={416} w={228} h={228} className="rounded-full" style={{ background: `conic-gradient(from 20deg, ${t.mid} 0deg 118deg, #fff 118deg 121deg, ${t.pale} 121deg 238deg, #fff 238deg 241deg, ${t.blue} 241deg 357deg, #fff 357deg 360deg)`, mask: ring, WebkitMask: ring }} />
      <Abs x={512} y={444} w={172} h={172} className="rounded-full bg-white" style={{ boxShadow: '0 0 0 6px #e4e6ec' }} />
      <T x={498} w={200} cy={530} size={19} align="center" className="font-bold" style={INK}>{c.ring}</T>
      {c.keywords.map((k, i) => {
        const cy = [423, 510, 598][i]
        return (
          <div key={k.title}>
            <Abs x={789} y={[440, 530, 616][i] - 13} w={26} h={26} className="rounded-full" style={{ background: [t.blue, t.mid, t.pale][i] }} />
            <T x={843} cy={cy} size={15.5} className="font-bold" style={BL}>{k.title}</T>
            <Lines lines={k.lines} x={843} cy={cy + 21} pitch={21} size={13.5} style={INK} />
          </div>
        )
      })}
    </Page>
  )
}

const contactIcons = { mail: Mail, phone: Phone, home: House }
function Contact() {
  const c = d.contact
  return (
    <Page dark>
      <PhotoBg label="corridor photo" />
      <RunHead no="05" label="Contact" dark />
      <T x={40} cy={450} size={98} className="font-extrabold tracking-[-0.02em]" style={W}>{c.title}</T>
      {c.rows.map((r) => {
        const Icon = contactIcons[r.icon]
        return (
          <div key={r.icon}>
            <Abs x={50} y={r.cy - 12}><Icon size={24} fill="#e8eaf2" color={t.dark} strokeWidth={1.5} /></Abs>
            <Lines lines={r.lines} x={96} cy={r.cy} pitch={28} size={19} className="font-light" style={{ color: '#e8eaf2' }} />
          </div>
        )
      })}
    </Page>
  )
}

const deck: DeckDefinition = { id: '22', title: '남색과 하얀색의 심플한 컨셉 기업 경영 보고서', slides: [Cover, Toc, Intro, Ceo, Company, Sales, Network, Field, Env, Contact] }
export default deck
