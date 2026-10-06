import { Briefcase, ChessRook, Crosshair, FileSearch, FileText, Files, HandCoins, Handshake, Lightbulb, ClipboardCheck, Settings, Monitor, ChevronRight, ChevronDown, ChevronLeft, ChevronUp, ArrowUp, ChartColumnBig, UserRoundCheck, ChartColumn, MapPin, SearchCheck, MonitorCheck, Newspaper, Presentation, Puzzle, Rocket, Target, Trophy,  UserRound, UserRoundPlus, UsersRound } from 'lucide-react'
import type { DeckDefinition } from '../../ui'
import { Abs, ImagePlaceholder } from '../../ui'
import { Badge, Bullets, CornerLogo, InsightBar, Frame, IconDisc, Lines, Page, Photo, Pill, T, Tab, Tab16 } from './components'
import { contents, cover, horizontal, keywords4, listRows, longText, overview, photo3, plan, process, pyramid, quote, sites, stats, visual, compare, part, mindmap, formula, timeline, swot, cycle, mockup, qna, numbers, lineChart, table, pies, gantt, org, thanks } from './data'
import { t } from './theme'

function Cover() {
  return (
    <Frame>
      <Tab x={1025} y={30} w={182} h={92} pt={22} lines={plan} size={18} />
      <T x={104} y={238} size={86} style={{ color: t.blue, letterSpacing: '-0.01em' }}>{cover.title[0]}</T>
      <T x={104} y={342} size={86} className="font-bold" style={{ letterSpacing: '-0.01em' }}>{cover.title[1]}</T>
      <T x={105} y={451} size={25}>{cover.sub}</T>
      <Lines x={105} y={593} size={18} lh={26} lines={cover.info} style={{ color: t.ink, letterSpacing: '0.02em' }} />
      <CornerLogo />
    </Frame>
  )
}

function Contents() {
  return (
    <Frame>
      <Tab16 x={79} lines={plan} />
      <T x={122} y={334} size={54} className="font-bold">{contents.title}</T>
      {contents.items.map((it, i) => {
        const cx = 598 + (i % 3) * 225, y = 181 + Math.floor(i / 3) * 225
        return (
          <div key={it.no}>
            <T x={cx - 100} y={y} w={200} size={17} align="center" style={{ color: t.blue }}>{it.no}</T>
            <Abs x={cx - 87} y={y + 32} w={174} h={1} style={{ background: '#88809f' }} />
            <Lines x={cx - 100} y={y + 47} w={200} size={20} lh={27} align="center" lines={it.lines} className="font-semibold" style={{ color: '#000030' }} />
            <Lines x={cx - 100} y={y + 112} w={200} size={16} lh={30} align="center" lines={it.bullets} style={{ color: t.grey6 }} />
          </div>
        )
      })}
      <CornerLogo />
    </Frame>
  )
}

function LongText() {
  return (
    <Page ch={1}>
      <T x={164} y={217} w={400} size={49} align="center" className="font-bold">{longText.title}</T>
      <Lines x={124} y={306} w={482} size={16.5} lh={27} lines={longText.body} justify style={{ color: '#444' }} />
      {longText.pills.map((p, i) => <Pill key={p} x={112 + i * 175} y={534} w={167} h={44} text={p} />)}
      <Photo x={723} y={75} w={474} h={573} />
    </Page>
  )
}

const ovIcons = [Briefcase, FileText, Handshake]
function Overview() {
  return (
    <Page ch={2} title={overview.title} intro={overview.intro}>
      <Abs x={44} y={310} w={1192} h={370} style={{ background: t.soft }} />
      {overview.cards.map((c, i) => {
        const x = 79 + i * 224.5, Icon = ovIcons[i]
        return (
          <div key={c.tag}>
            <Abs x={x} y={357} w={216} h={278} className="bg-white" />
            <Badge x={x + 48} y={380} w={120} h={33} text={c.tag} />
            <IconDisc cx={x + 108} cy={491} r={52} bg={t.soft}><Icon size={38} strokeWidth={1.3} color={t.blue} /></IconDisc>
            <T x={x} y={576} w={216} size={17} align="center" style={{ color: t.ink }}>{c.value}</T>
          </div>
        )
      })}
      {overview.rows.map((r, i) => {
        const y = 357 + i * 71.5
        return (
          <div key={r.k}>
            <Abs x={756} y={y} w={444} h={65} style={{ background: t.sky }} />
            <Badge x={771} y={y + 16} w={85} h={33} text={r.k} bg="#fff" color={t.navy} size={14} />
            <T x={878} y={y + 24} size={17} style={{ color: '#203040' }}>{r.v}</T>
          </div>
        )
      })}
    </Page>
  )
}

const hzIcons = [Puzzle, ChessRook]
function Horizontal() {
  return (
    <Page ch={3} title={horizontal.title} intro={horizontal.intro}>
      {horizontal.cards.map((c, i) => {
        const x = 96 + i * 554, Icon = hzIcons[i]
        return (
          <div key={c.tag}>
            <Abs x={x} y={311} w={534} h={336} style={{ background: t.soft }} />
            <Badge x={x + 31} y={337} w={99} h={33} text={c.tag} />
            <T x={x + 37} y={397} size={19.5} className="font-semibold" style={{ color: t.navy }}>{c.head}</T>
            <Lines x={x + 31} y={446} size={16} lh={24} lines={c.body} style={{ color: '#485060' }} />
            <Bullets x={x + 37} y={558} items={c.bullets} size={15.5} lh={32} color="#485060" />
            <IconDisc cx={x + 477} cy={588} r={41}><Icon size={36} strokeWidth={1.2} color={t.blue} /></IconDisc>
          </div>
        )
      })}
    </Page>
  )
}

const lsIcons = [Crosshair, FileSearch, Files, UserRoundPlus]
function ListRows() {
  return (
    <Page ch={4} title={listRows.title} intro={listRows.intro}>
      {listRows.rows.map((r, i) => {
        const y = 281 + i * 93.7, Icon = lsIcons[i]
        return (
          <div key={r.k}>
            <Abs x={160} y={y} w={990} h={76} className="rounded-full" style={{ background: t.soft }} />
            <Abs x={160} y={y} w={394} h={76} style={{ background: i % 2 ? t.rowB : t.rowA, borderRadius: '38px 0 0 38px' }} />
            <IconDisc cx={198} cy={y + 38} r={30}><Icon size={26} strokeWidth={1.3} color={t.blue} /></IconDisc>
            <T x={247} y={y + 29} size={18} className="font-semibold text-white">{r.k}</T>
            <T x={576} y={y + 30} size={15.7} style={{ color: t.ink }}>{r.v}</T>
          </div>
        )
      })}
    </Page>
  )
}

function Photo3() {
  return (
    <Page ch={5} title={photo3.title}>
      {photo3.cols.map((c, i) => {
        const x = 109 + i * 366.5, dark = i === 2, fg = dark ? '#fff' : t.navy
        return (
          <div key={c.k}>
            <Photo x={x} y={247} w={338} h={207} />
            <Abs x={x + 132} y={210} w={74} h={74} className="rounded-full bg-white" />
            <T x={x + 149} y={255} w={40} size={17} align="center" style={{ color: t.blue }}>{c.k}</T>
            <Abs x={x} y={454} w={338} h={181} style={{ background: dark ? t.blue : t.soft }} />
            <T x={x} y={481} w={338} size={18.5} align="center" className="font-semibold" style={{ color: fg }}>{c.head}</T>
            <Lines x={x} y={525} w={338} size={15.5} lh={24} align="center" lines={c.body} style={{ color: dark ? '#fff' : '#485060' }} />
          </div>
        )
      })}
    </Page>
  )
}

const statIcons = [Target, Presentation, Puzzle, HandCoins, UserRound]
function Stats() {
  return (
    <Page ch={6} title={stats.title}>
      <Photo x={136} y={240} w={273} h={153} />
      <Photo x={435} y={240} w={274} h={153} />
      <T x={736} y={252} size={19.6} className="font-semibold" style={{ color: t.navy }}>{stats.head}</T>
      <Lines x={736} y={306} size={16.8} lh={25} lines={stats.body} style={{ color: '#485060' }} />
      {stats.items.map((s, i) => {
        const cx = [181, 410, 639, 865, 1099][i], Icon = statIcons[i]
        return (
          <div key={i}>
            {i > 0 && <Abs x={[294, 522, 752, 981][i - 1]} y={468} w={1} h={166} style={{ background: '#d5d8e8' }} />}
            <IconDisc cx={cx} cy={484} r={34} bg={t.soft}><Icon size={30} strokeWidth={1.2} color={t.blue} /></IconDisc>
            <Abs x={cx - 120} y={530} w={240} className="flex items-baseline justify-center whitespace-nowrap font-bold leading-none" style={{ color: t.rowA }}>
              <span style={{ fontSize: 52 }}>{s.n}</span><span style={{ fontSize: 28 }}>%</span>
            </Abs>
            <T x={cx - 100} y={606} w={200} size={16} align="center" style={{ color: t.ink }}>{s.label}</T>
          </div>
        )
      })}
    </Page>
  )
}

function Keywords4() {
  const line = '#d0d0d8'
  return (
    <Page ch={7} title={keywords4.title}>
      {keywords4.rows.map((r, i) => {
        const y = 239 + i * 101.5
        return (
          <div key={i}>
            <Abs x={143} y={y} w={613} h={92} style={{ background: i % 2 ? t.sky : t.pale, borderRadius: '0 46px 46px 0', boxShadow: '0 2px 8px rgba(80,100,180,0.12)' }} />
            <T x={178} y={y + 28} size={17.8} className="font-semibold" style={{ color: t.navy }}>{r.title}</T>
            <Bullets x={183} y={y + 54} items={[r.sub]} size={15.5} lh={32} color="#485060" dot={t.navy} />
            <Abs x={762} y={y + 46} w={43} h={1} style={{ background: line }} />
          </div>
        )
      })}
      <Abs x={805} y={285} w={1} h={305} style={{ background: line }} />
      <Abs x={805} y={441} w={30} h={1} style={{ background: line }} />
      <Abs x={835} y={283} w={316} h={316} className="rounded-full" style={{ background: t.pale }} />
      <Abs x={851} y={299} w={284} h={284} className="rounded-full" style={{ background: t.rowB }} />
      <Abs x={863} y={311} w={260} h={260} className="flex flex-col items-center rounded-full text-white" style={{ background: t.blue }}>
        <div className="mt-[42px] font-semibold leading-none" style={{ fontSize: 19 }}>{keywords4.goal.head}</div>
        <Target size={44} strokeWidth={1.4} className="mt-[22px]" />
        <div className="mt-[21px] text-center font-medium" style={{ fontSize: 18.5, lineHeight: '27px' }}>{keywords4.goal.lines.map((l) => <div key={l}>{l}</div>)}</div>
      </Abs>
    </Page>
  )
}

const pyrIcons = [Target, UsersRound, Newspaper, Rocket, Lightbulb]
const pyrBg = [t.rowA, '#c9cdee', '#e8eaf7', t.sky, t.pale]
const sqBg = [t.rowB, t.pale, '#e8eaf7', t.pale, '#f2f5ff']
function Pyramid() {
  return (
    <Page ch={8}>
      <T x={100} y={210} size={49} className="font-bold">{pyramid.title}</T>
      <Lines x={100} y={295} size={16.7} lh={25} lines={pyramid.body} style={{ color: '#485060' }} />
      <Abs x={1146} y={74} w={3} h={74} style={{ background: t.rowB }} />
      <Abs x={1093} y={76} w={54} h={42} style={{ background: t.rowA, clipPath: 'polygon(100% 0, 100% 100%, 0 50%)' }} />
      {pyramid.rows.map((r, i) => {
        const y = [189, 282, 375, 469, 561][i], x = [707, 598, 490, 379, 270][i], Icon = pyrIcons[i], dark = i === 0
        const sq = [148, 240, 333, 427, 519][i]
        return (
          <div key={r.k}>
            <Abs x={1053} y={y - (i % 3 === 0 ? 40 : 10)} w={41} h={i % 3 === 0 ? 40 : 10} style={{ background: '#9aa0b8', clipPath: 'polygon(0 0, 100% 100%, 0 100%)' }} />
            <Abs x={x} y={y} w={1094 - x} h={79} style={{ background: pyrBg[i], borderRadius: '40px 0 0 40px' }} />
            <Badge x={x + 30} y={y + 24} w={80} h={31} text={r.k} bg="#fff" color={t.navy} size={15} />
            <T x={x + 128} y={y + 30} size={17.8} style={{ color: dark ? '#fff' : t.ink }}>{r.v}</T>
            <Abs x={1094} y={sq} w={86} h={81} className="flex items-center justify-center" style={{ background: sqBg[i] }}><Icon size={38} strokeWidth={1.2} color={t.blue} /></Abs>
          </div>
        )
      })}
    </Page>
  )
}

function QuotePage() {
  return (
    <Frame panel={{ x: 55, y: 53, w: 1192, h: 640 }}>
      <Abs x={55} y={53} w={448} h={437} style={{ borderRadius: '0 0 100% 0', overflow: 'hidden' }}><Photo x={0} y={0} w={448} h={437} /></Abs>
      <Tab16 x={990} y={29} lines={['CHAPTER', '09']} />
      <Abs x={808} y={226}>
        <svg width={48} height={31} viewBox="0 0 48 31" fill={t.ink}>
          {[0, 26].map((dx) => <path key={dx} transform={`translate(${dx} 0)`} d="M11 31a11 11 0 0 1-11-11C0 10 6 2 15 0l2 4c-5 2-8 5-8 7a10 10 0 0 1 13 9 11 11 0 0 1-11 11z" />)}
        </svg>
      </Abs>
      <Lines x={431} y={281} w={800} size={33.5} lh={48} align="center" lines={quote.lines} className="font-semibold" style={{ color: t.ink }} />
      <Lines x={531} y={402} w={600} size={15.5} lh={20} align="center" lines={quote.en} className="font-poppins" style={{ color: t.ink }} />
      <Abs x={831} y={477} w={1} h={67} style={{ background: '#707070' }} />
      <Lines x={431} y={560} w={800} size={14.3} lh={20} align="center" lines={quote.note} style={{ color: '#555' }} />
    </Frame>
  )
}

const procIcons = [Lightbulb, ClipboardCheck, Settings, Monitor, ChevronRight, ChevronDown, ChevronLeft, ChevronUp, ArrowUp, ChartColumnBig, UserRoundCheck, ChartColumn, MapPin, SearchCheck, MonitorCheck, Handshake]
function Process() {
  return (
    <Page ch={10} title={process.title} intro={process.intro}>
      {process.steps.map((s, i) => {
        const x = 104 + i * 272, dark = i === 3, Icon = procIcons[i]
        return (
          <div key={s.step}>
            <Abs x={x} y={311} w={254} h={348} style={{ background: dark ? t.rowA : t.pale, borderRadius: '0 0 127px 127px' }} />
            <Badge x={x + 83} y={339} w={89} h={26} text={s.step} bg="#fff" color={t.blue} size={13} />
            <T x={x} y={391} w={254} size={18.5} align="center" className="font-semibold" style={{ color: dark ? '#fff' : t.navy }}>{s.head}</T>
            <Lines x={x} y={432} w={254} size={16} lh={24} align="center" lines={s.body} style={{ color: dark ? '#fff' : '#485060' }} />
            <Abs x={x + 107} y={560}><Icon size={40} strokeWidth={1.2} color={dark ? '#fff' : t.blue} /></Abs>
          </div>
        )
      })}
    </Page>
  )
}

function Visual() {
  return (
    <Page ch={11}>
      <T x={100} y={282} size={49} className="font-bold">{visual.title}</T>
      <Lines x={100} y={361} size={16.8} lh={25.5} lines={visual.body} style={{ color: '#485060' }} />
      {visual.items.map((v, i) => {
        const x = i % 2 ? 853 : 485, y = i < 2 ? 76 : 375
        return (
          <div key={v.k}>
            <Photo x={x} y={y} w={348} h={232} />
            <Abs x={x} y={y + 232} w={348} h={50} className="flex items-center justify-center" style={{ background: t.pale, color: t.ink, fontSize: 16 }}>{v.cap}</Abs>
            <IconDisc cx={x + 39} cy={y + 11} r={26}><span className="font-semibold" style={{ fontSize: 15, color: t.navy }}>{v.k}</span></IconDisc>
          </div>
        )
      })}
    </Page>
  )
}

const siteIcons = [SearchCheck, ChartColumn]
function Sites() {
  return (
    <Page ch={12}>
      <T x={100} y={183} size={49} className="font-bold">{sites.title}</T>
      <Lines x={100} y={255} size={16.8} lh={26} lines={sites.body} style={{ color: '#485060' }} />
      {sites.cards.map((c, i) => {
        const x = 100 + i * 301, Icon = siteIcons[i]
        return (
          <div key={i}>
            <Abs x={x} y={336} w={284} h={303} style={{ background: i ? '#f2f2f4' : '#e2ebff' }} />
            <Badge x={x + 92} y={360} w={100} h={31} text={c.tag} bg={t.rowA} size={15} />
            <Abs x={x + 124} y={421}><Icon size={36} strokeWidth={1.2} color={t.blue} /></Abs>
            <T x={x} y={486} w={284} size={17.5} align="center" className="font-semibold" style={{ color: t.navy }}>{c.head}</T>
            <Bullets x={x + 39} y={533} items={c.bullets} size={15.8} lh={27.5} color="#485060" />
          </div>
        )
      })}
      <Abs x={705} y={212} w={481} h={419}><ImagePlaceholder label="district map" className="h-full w-full rounded-[40px]" /></Abs>
      {sites.pins.map(([label, lx, py], i) => {
        const ly = 168 + i * 26
        return (
          <div key={i}>
            <Abs x={lx} y={ly} w={1130 - lx} h={1} style={{ background: '#9a9a9a' }} />
            <Abs x={lx} y={ly} w={1} h={py - ly} style={{ background: '#9a9a9a' }} />
            <Abs x={lx - 14} y={py - 22}><MapPin size={28} fill={t.blue} color="#fff" strokeWidth={1.6} /></Abs>
            <T x={1137} y={ly - 7} size={14} style={{ color: t.ink }}>{label}</T>
          </div>
        )
      })}
    </Page>
  )
}

function Compare() {
  return (
    <Page ch={13} title={compare.title} intro={compare.intro}>
      {compare.heads.map((h, i) => <T key={h} x={[251, 827][i]} y={272} w={200} size={17.5} align="center" style={{ color: t.ink }}>{h}</T>)}
      {compare.rows.map((r, i) => {
        const y = 305 + i * 83.5
        return (
          <div key={r.key}>
            <Abs x={177} y={y} w={347} h={70} className="flex items-center justify-center" style={{ background: t.grey, borderRadius: '35px 0 0 35px', color: t.ink, fontSize: 17 }}>{r.text}</Abs>
            <Abs x={540} y={y + 35} w={52} h={1} style={{ background: '#555' }} />
            <T x={590} y={y + 27} w={100} size={17} align="center" className="font-semibold" style={{ color: '#111' }}>{r.key}</T>
            <Abs x={688} y={y + 35} w={52} h={1} style={{ background: '#555' }} />
            <Abs x={753} y={y} w={347} h={70} className="flex items-center justify-center text-white" style={{ background: t.rowB, borderRadius: '0 35px 35px 0', fontSize: 17 }}>{r.text}</Abs>
          </div>
        )
      })}
      <InsightBar y={579} tag={compare.insight.tag} text={compare.insight.text} />
    </Page>
  )
}

function Part() {
  return (
    <Frame panel={{ x: 44, y: 64, w: 1192, h: 512 }}>
      <Tab x={1006} y={46} lines={plan} size={16} pt={27} />
      <T x={215} y={247} size={50} className="font-bold" style={{ color: t.blue }}>{part.no}</T>
      <T x={422} y={241} size={54}>{part.lines[0]}</T>
      <T x={422} y={316} size={54} className="font-bold">{part.lines[1]}</T>
      {part.pills.map((p, i) => <Pill key={p} x={424 + i * 195} y={410} w={188} h={50} size={17} text={p} bg={t.pale} className="shadow-[0_2px_6px_rgba(80,100,180,0.15)]" />)}
      <CornerLogo bottom={576} />
    </Frame>
  )
}

const mmIcons = [Puzzle, Newspaper, Presentation, Lightbulb]
function Mindmap() {
  const { nodes, labels } = mindmap
  const line = '#c9cdee'
  return (
    <Page ch={14} title={mindmap.title}>
      <svg className="absolute left-0 top-0" width={1280} height={720}>
        <path d="M 450 655 A 190 190 0 0 1 830 655" fill="none" stroke={line} strokeWidth={2} />
        {nodes.map((n, i) => <polyline key={i} points={`${n.cx},${n.cy} ${n.cx},${n.cy + (i % 3 ? 54 : 56)} ${n.dot[0]},${n.dot[1]}`} fill="none" stroke={line} strokeWidth={1.5} />)}
        {labels.map((l, i) => { const n = nodes[l.node]; return <line key={i} x1={l.cx} y1={l.cy} x2={n.cx} y2={n.cy} stroke="#b8bcd8" strokeWidth={1} strokeDasharray="2 2" /> })}
      </svg>
      <Abs x={0} y={0} w={1280} h={655} className="overflow-hidden">
        <Abs x={477} y={492} w={326} h={326} className="rounded-full" style={{ background: t.rowA }} />
        <Abs x={501} y={516} w={278} h={278} className="rounded-full" style={{ background: t.blue }} />
      </Abs>
      <Abs x={622} y={556}><Target size={38} strokeWidth={1.4} color="#fff" /></Abs>
      <T x={540} y={611} w={200} size={20} align="center" className="font-semibold text-white">{mindmap.center}</T>
      {nodes.map((n, i) => {
        const Icon = mmIcons[i]
        return (
          <div key={i}>
            <Abs x={n.dot[0] - 5} y={n.dot[1] - 5} w={10} h={10} className="rounded-full" style={{ background: t.rowB, border: '2px solid #e2e5f6' }} />
            <IconDisc cx={n.cx} cy={n.cy} r={58} bg={n.dark ? t.rowA : t.rowB}><Icon size={38} strokeWidth={1.2} color="#fff" /></IconDisc>
          </div>
        )
      })}
      {labels.map((l) => <Badge key={l.text} x={l.cx - 56} y={l.cy - 17} w={112} h={35} text={l.text} bg={l.dark ? t.rowA : t.rowB} size={16} className="font-medium" />)}
      <Lines x={43} y={601} w={400} size={16.9} lh={26} align="center" lines={mindmap.left} style={{ color: t.ink }} />
      <Lines x={883} y={590} size={16.8} lh={26} lines={mindmap.right} style={{ color: t.ink }} />
    </Page>
  )
}

function Formula() {
  return (
    <Page ch={15} title={formula.title}>
      <Abs x={185} y={228} w={910} h={292} className="rounded-full" style={{ background: t.pale }} />
      <Abs x={560} y={520} w={160} h={49} style={{ background: t.sky, clipPath: 'polygon(0 0, 100% 0, 50% 100%)' }} />
      {formula.points.map((p, i) => {
        const cx = 332 + i * 308
        return (
          <div key={p.tag}>
            <Abs x={cx - 127} y={248} w={254} h={254} className="rounded-full" style={{ background: i === 1 ? t.blue : t.rowA }} />
            <Badge x={cx - 46} y={292} w={92} h={28} text={p.tag} bg={t.rowB} size={14} className="font-medium" />
            <T x={cx - 120} y={349} w={240} size={19} align="center" className="font-semibold text-white">{p.head}</T>
            <Lines x={cx - 120} y={391} w={240} size={15.5} lh={24} align="center" lines={p.body} style={{ color: '#dfe3f7' }} />
            {i > 0 && <T x={cx - 154 - 20} y={355} w={40} size={40} align="center" className="font-extralight" style={{ color: t.rowA }}>+</T>}
          </div>
        )
      })}
      <InsightBar y={578} tag={formula.insight.tag} text={formula.insight.text} />
    </Page>
  )
}

const tlIcons = [Settings, Trophy, ClipboardCheck]
const tlBlocks = [{ x: 82, y: 350, bg: t.pale }, { x: 447, y: 309, bg: t.sky }, { x: 815, y: 267, bg: t.rowB }]
function Timeline() {
  return (
    <Page ch={16} right>
      <T x={104} y={133} size={49} className="font-bold">{timeline.title}</T>
      <Lines x={104} y={202} size={16.5} lh={25} lines={timeline.intro} style={{ color: '#485060' }} />
      {timeline.steps.map((st, i) => {
        const b = tlBlocks[i], last = i === 2, Icon = tlIcons[i]
        return (
          <div key={st.tag}>
            <Abs x={b.x} y={b.y} w={i === 2 ? 367 : 365 + (i ? 3 : 0)} h={616 - b.y} style={{ background: b.bg }} />
            <Badge x={b.x + 21} y={b.y + 21} w={98} h={31} text={st.tag} size={14.5} className="font-medium" />
            <T x={b.x + (last ? 29 : 21)} y={b.y + (last ? 73 : 76)} size={18} className="font-semibold" style={{ color: last ? '#fff' : t.navy }}>{st.head}</T>
            <Lines x={b.x + (last ? 29 : 21)} y={b.y + (last ? 119 : 109)} size={15.5} lh={last ? 24.5 : 24} lines={st.body} style={{ color: last ? '#f0f2fb' : '#485060' }} />
            <IconDisc cx={[388, 757, 1111][i]} cy={565} r={34}><Icon size={30} strokeWidth={1.2} color={t.blue} /></IconDisc>
          </div>
        )
      })}
      <Abs x={86} y={616} w={1113} h={40} style={{ background: `linear-gradient(90deg, #c9cdee, ${t.rowA} 60%, ${t.blue})`, clipPath: 'polygon(0 0, calc(100% - 16px) 0, 100% 50%, calc(100% - 16px) 100%, 0 100%)' }} />
      {timeline.dates.map((d) => <T key={d.x} x={d.x} y={628} size={16} className="font-semibold text-white">{d.text}</T>)}
    </Page>
  )
}

const swotFill = [t.rowA, t.rowB, t.rowB, t.rowA]
function Swot() {
  return (
    <Page ch={17} right title={swot.title}>
      {swot.items.map((it, i) => {
        const right = i % 2 === 1, x = right ? 644 : 136, y = i < 2 ? 214 : 436
        const ax = right ? 'right' : 'left', tx = right ? x + 28 : x + 27
        return (
          <div key={it.k}>
            <Abs x={x} y={y} w={499} h={215} style={{ background: i === 0 || i === 3 ? t.sky : t.pale }} />
            <Badge x={right ? x + 335 : x + 25} y={y + 30} w={136} h={33} text={it.tag} size={16} className="font-medium" />
            <T x={tx} y={y + 98} w={444} size={18.5} align={ax} className="font-semibold" style={{ color: t.navy }}>{it.head}</T>
            <Lines x={tx} y={y + 135} w={444} size={15.5} lh={24} align={ax} lines={it.body} style={{ color: '#485060' }} />
          </div>
        )
      })}
      <Abs x={525} y={317} w={230} h={230} className="rounded-full bg-white" />
      {swot.items.map((it, i) => {
        const r = 104, right = i % 2 === 1, bottom = i > 1
        return (
          <Abs key={it.k} x={right ? 644 : 640 - r} y={bottom ? 436 : 432 - r} w={r - 4} h={r - 4} className="flex items-center justify-center font-bold text-white"
            style={{ background: swotFill[i], fontSize: 38, borderRadius: right ? (bottom ? '0 0 100% 0' : '0 100% 0 0') : bottom ? '0 0 0 100%' : '100% 0 0 0' }}>
            <span style={{ transform: 'none', margin: right ? (bottom ? '0 20px 22px 0' : '22px 20px 0 0') : bottom ? '0 0 22px 20px' : '22px 0 0 20px' }}>{it.k}</span>
          </Abs>
        )
      })}
      <Abs x={608} y={400} w={64} h={64} className="rounded-full bg-white" />
    </Page>
  )
}

const cyIcons = [Lightbulb, Newspaper, UsersRound, Monitor]
const cyPos = [[449, 318], [829, 318], [449, 558], [829, 558]] as const
function Cycle() {
  const ch = '#9aa0c8'
  return (
    <Page ch={18} right title={cycle.title}>
      <Abs x={434} y={224} w={412} h={412} className="rounded-full" style={{ border: `1.5px dashed ${t.rowB}`, background: '#f7f9ff' }} />
      <Abs x={480} y={270} w={320} h={320} className="rounded-full" style={{ background: t.pale }} />
      <Abs x={499} y={289} w={282} h={282} className="rounded-full" style={{ background: '#c9cdee' }} />
      <Abs x={511} y={301} w={258} h={258} className="rounded-full" style={{ background: t.blue }} />
      <T x={520} y={398} w={240} size={19} align="center" className="font-semibold text-white">{cycle.center.head}</T>
      <Lines x={520} y={430} w={240} size={15} lh={24} align="center" lines={cycle.center.body} style={{ color: '#dfe3f7' }} />
      <Abs x={632} y={216}><ChevronRight size={16} color={ch} /></Abs>
      <Abs x={838} y={422}><ChevronDown size={16} color={ch} /></Abs>
      <Abs x={632} y={629}><ChevronLeft size={16} color={ch} /></Abs>
      <Abs x={426} y={422}><ChevronUp size={16} color={ch} /></Abs>
      {cycle.items.map((it, i) => {
        const [cx, cy] = cyPos[i], right = i % 2 === 1, Icon = cyIcons[i]
        const ty = i < 2 ? 279 : 520
        return (
          <div key={it.head}>
            <IconDisc cx={cx} cy={cy} r={50} bg={t.rowB}><Icon size={38} strokeWidth={1.2} color="#fff" /></IconDisc>
            {right
              ? <><T x={[0, 892, 0, 898][i]} y={ty} size={18} className="font-semibold" style={{ color: t.navy }}>{it.head}</T>
                  <Lines x={[0, 892, 0, 898][i]} y={ty + 32} size={15.5} lh={24} lines={it.body} style={{ color: '#485060' }} /></>
              : <><T x={80} y={ty} w={300} size={18} align="right" className="font-semibold" style={{ color: t.navy }}>{it.head}</T>
                  <Lines x={80} y={ty + 32} w={300} size={15.5} lh={24} align="right" lines={it.body} style={{ color: '#485060' }} /></>}
          </div>
        )
      })}
    </Page>
  )
}

function Mockup() {
  return (
    <Page ch={19}>
      <T x={109} y={254} size={49} className="font-bold">{mockup.title}</T>
      <Lines x={109} y={347} size={16.5} lh={25.3} lines={mockup.body} style={{ color: '#485060' }} />
      <Bullets x={115} y={470} items={mockup.bullets} size={16} lh={32.5} color="#485060" />
      {mockup.shots.map((c, i) => (
        <div key={c}>
          <Abs x={528 + i * 349} y={151} w={308} h={513}><ImagePlaceholder label="smartphone mockup" className="h-full w-full rounded-t-[40px]" /></Abs>
          <T x={581 + i * 349} y={643} w={200} size={15} align="center" className="font-semibold" style={{ color: t.ink }}>{c}</T>
        </div>
      ))}
    </Page>
  )
}

function Qna() {
  return (
    <Page ch={20}>
      <T x={100} y={301} size={49} className="font-bold">{qna.title}</T>
      <Lines x={100} y={379} size={16.5} lh={25} lines={qna.body} style={{ color: '#485060' }} />
      {qna.items.map((it, i) => {
        const cy = 157 + i * 141.3
        const av = it.q ? 588 : 1138
        return (
          <div key={i}>
            {it.q
              ? <Abs x={609} y={cy - 52} w={592} h={105} style={{ background: t.blue, borderRadius: '0 53px 53px 0' }} />
              : <Abs x={524} y={cy - 53} w={618} h={106} style={{ background: t.pale, borderRadius: '53px 0 0 53px' }} />}
            <Abs x={av - 63} y={cy - 63} w={126} h={126} className="overflow-hidden rounded-full bg-white" style={{ border: `2px solid ${t.blue}` }}>
              <ImagePlaceholder label="avatar illustration" className="h-full w-full" />
            </Abs>
            <Abs x={it.q ? 667 : 588} y={cy - 24} className="whitespace-nowrap" style={{ fontSize: 16, lineHeight: '25px', color: it.q ? '#fff' : t.navy }}>
              <div><b className="font-semibold">{it.q ? 'Q' : 'A'} :</b> {it.lines[0]}</div>
              <div style={{ paddingLeft: 26 }}>{it.lines[1]}</div>
            </Abs>
          </div>
        )
      })}
    </Page>
  )
}

const numCols = [{ x: 92, w: 498, bg: t.blue, fg: t.blue }, { x: 590, w: 327, bg: t.rowB, fg: t.rowB }, { x: 917, w: 269, bg: t.stone, fg: '#8a8a8a' }]
const numIcons = [Trophy, HandCoins, ChessRook]
function Numbers() {
  return (
    <Page ch={21}>
      <T x={92} y={195} size={49} className="font-bold">{numbers.title}</T>
      <Lines x={92} y={284} size={16.5} lh={25} lines={numbers.body} style={{ color: '#485060' }} />
      <Photo x={727} y={161} w={459} h={223} />
      {numbers.items.map((it, i) => {
        const c = numCols[i], Icon = numIcons[i]
        return (
          <div key={it.n}>
            <Abs x={c.x} y={424} w={c.w} h={90} className="flex items-center text-white" style={{ background: c.bg }}>
              <span className="ml-[26px] font-bold leading-none" style={{ fontSize: i ? 42 : 52 }}>{it.n}</span>
              <span className="ml-[3px] mt-[14px] font-semibold leading-none" style={{ fontSize: 26 }}>%</span>
              <span className="ml-[14px] mt-[8px] font-semibold leading-none" style={{ fontSize: 19 }}>{it.label}</span>
              <Icon size={34} strokeWidth={1.3} className="ml-auto mr-[26px]" />
            </Abs>
            <Bullets x={c.x + 13} y={537} items={[it.head]} size={18} lh={32} color={c.fg} dot={c.fg} />
            <Lines x={c.x + 28} y={579} size={15.5} lh={24} lines={it.body} style={{ color: '#485060' }} />
          </div>
        )
      })}
    </Page>
  )
}

function LineChart() {
  const { points } = lineChart
  const path = points.map(([x, y]) => `${x},${y}`).join(' ')
  return (
    <Page ch={22}>
      <T x={106} y={170} size={49} className="font-bold">{lineChart.title}</T>
      {lineChart.cards.map((c, i) => {
        const y = 249 + i * 149
        return (
          <div key={c.head}>
            <Abs x={106} y={y} w={563} h={135} style={{ background: t.pale, borderRadius: '0 68px 68px 0' }} />
            <Bullets x={128} y={y + 27} items={[c.head]} size={19} lh={32} color={t.navy} dot={t.navy} />
            <Lines x={126} y={y + 66} size={16} lh={24.5} lines={c.body} style={{ color: '#485060' }} />
            <Abs x={c.up ? 518 : 500} y={y + 63} className="flex items-center whitespace-nowrap font-bold leading-none" style={{ fontSize: 48, color: t.blue }}>
              {c.big}{c.up && <ArrowUp size={40} strokeWidth={2.5} className="-ml-1" />}
            </Abs>
          </div>
        )
      })}
      <svg className="absolute left-0 top-0" width={1280} height={720}>
        <polygon points={`452,640 ${path} 1196,640`} fill="#eef1fb" />
        <polyline points={path} fill="none" stroke="#a8b0e0" strokeWidth={2} />
        {points.map(([x, y]) => <circle key={x} cx={x} cy={y} r={3} fill="#a8b0e0" />)}
        <line x1={435} y1={646} x2={1203} y2={646} stroke="#555" strokeWidth={1} />
      </svg>
      <Abs x={762} y={288} w={272} h={120}><ImagePlaceholder label="swoosh arrow graphic" className="h-full w-full rounded-[60px]" /></Abs>
      {points.map(([x, y, v]) => <T key={x} x={x - 30} y={y - 24} w={60} size={12} align="center" style={{ color: '#a8b0e0' }}>{v}</T>)}
      {lineChart.weeks.map((w, i) => <T key={w} x={461 + i * 102 - 40} y={658} w={80} size={12} align="center" style={{ color: t.ink }}>{w}</T>)}
      <T x={884} y={607} w={300} size={16.5} align="right" className="font-semibold" style={{ color: t.ink }}>{lineChart.caption}</T>
      <IconDisc cx={1127} cy={239} r={55} bg={t.blue}><span className="font-bold text-white" style={{ fontSize: 36 }}>{lineChart.badge}</span></IconDisc>
    </Page>
  )
}

function Table() {
  const xs = [249, 408, 568, 727, 887], rowY = [304, 360, 416, 472, 528]
  return (
    <Page ch={23} title={table.title}>
      <Abs x={249} y={247} w={638} h={1} style={{ background: '#c8c8d0' }} />
      <Abs x={249} y={304} w={638} h={334} style={{ background: t.pale }} />
      {xs.slice(1, 4).map((x) => <Abs key={x} x={x} y={247} w={1} h={281} style={{ background: '#e4e8f8' }} />)}
      {table.cols.map((c, i) => <Badge key={c} x={(xs[i] + xs[i + 1]) / 2 - 68} y={260} w={137} h={33} text={c} size={16} className="font-medium" />)}
      {[...table.rows.map((r) => r.k), table.note.k].map((k, i) => {
        const y = rowY[i], h = i === 4 ? 110 : 56
        return (
          <div key={k}>
            <Abs x={91} y={y + h - 1} w={796} h={1} style={{ background: i === 4 ? '#d8d8e0' : '#fff' }} />
            <Abs x={91} y={y + h - 1} w={158} h={1} style={{ background: '#d8d8e0' }} />
            <Badge x={100} y={y + h / 2 - 16} w={138} h={33} text={k} bg={i < 2 ? t.rowA : '#8e96d4'} size={15} className="font-medium" />
          </div>
        )
      })}
      {table.rows.map((r, i) => r.v.map((v, j) => <T key={`${i}-${j}`} x={xs[j]} y={rowY[i] + 20} w={xs[j + 1] - xs[j]} size={15} align="center" style={{ color: t.ink }}>{v}</T>))}
      <Bullets x={280} y={549} items={table.note.bullets} size={16} lh={24} color={t.ink} />
      <Photo x={906} y={249} w={307} h={401} />
    </Page>
  )
}

function Pies() {
  return (
    <Page ch={24} right title={pies.title}>
      {pies.charts.map((c, i) => {
        const x = 140 + i * 520, cx = 493 + i * 519, cy = 362
        let acc = 0
        const grad = c.segs.map((s) => { const a = acc; acc += s.v; return `${s.c} ${a}% ${acc}%` }).join(', ')
        const Icon = i ? UserRoundCheck : ChartColumnBig
        return (
          <div key={c.tag}>
            <Abs x={x} y={237} w={478} h={407} style={{ background: `linear-gradient(180deg, ${t.pale}, #f7f9ff)` }} />
            <Badge x={x + 24} y={260} w={137} h={33} text={c.tag} size={16} className="font-medium" />
            <Abs x={cx - 124} y={cy - 124} w={248} h={248} className="rounded-full" style={{ background: '#f3f5fd' }} />
            <Abs x={cx - 114} y={cy - 114} w={228} h={228} className="rounded-full" style={{ background: `conic-gradient(${grad})` }} />
            <IconDisc cx={cx} cy={cy} r={46}><Icon size={30} strokeWidth={1.2} color={t.blue} /></IconDisc>
            {c.labels.map(([l, lx, ly, light]) => <T key={l} x={lx - 30} y={ly - 8} w={60} size={15.5} align="center" className="font-semibold" style={{ color: light ? '#fff' : t.rowA }}>{l}</T>)}
            {c.legend.map(([l, col], j) => (
              <div key={l}>
                <Abs x={x + 24 + i * 20} y={c.legendY + j * 25.5 - 6} w={27} h={12} className="rounded-full" style={{ background: col }} />
                <T x={x + 58 + i * 20} y={c.legendY + j * 25.5 - 7} size={13} style={{ color: t.ink }}>{l}</T>
              </div>
            ))}
            <Bullets x={x + 27} y={523} items={c.bullets} size={16} lh={29} color={t.ink} />
          </div>
        )
      })}
    </Page>
  )
}

function Gantt() {
  const x0 = 222, cw = 78.33, navy = '#000849'
  return (
    <Page ch={25} right title={gantt.title}>
      <Abs x={x0} y={223} w={940} h={38} style={{ background: navy }} />
      {gantt.months.map((m, i) => <T key={m} x={x0 + i * cw} y={235} w={cw} size={14.5} align="center" className="text-white">{m}</T>)}
      {gantt.rows.map((r, i) => {
        const y = 262 + i * 61.3
        return (
          <div key={i}>
            <Abs x={116} y={y} w={1046} h={61} style={{ background: i % 2 ? t.pale : t.sky, borderRadius: '31px 0 0 31px' }} />
            <Lines x={116} y={y + 30 - r.label.length * 9} w={134} size={15} lh={19} align="center" lines={r.label} style={{ color: t.ink }} />
            <Abs x={r.x0} y={y + 16} w={r.x1 - r.x0} h={28} className="flex items-center justify-center bg-white" style={{ clipPath: 'polygon(0 0, calc(100% - 12px) 0, 100% 50%, calc(100% - 12px) 100%, 0 100%)', fontSize: 14, color: t.ink }}>{gantt.task}</Abs>
          </div>
        )
      })}
      {Array.from({ length: 12 }, (_, i) => <Abs key={i} x={x0 + i * cw} y={223} w={1} h={i ? 345 : 345} style={{ background: i ? 'rgba(255,255,255,0.7)' : '#fff' }} />)}
      <InsightBar y={592} x={116} w={1048} tag={gantt.insight.tag} text={gantt.insight.text} />
    </Page>
  )
}

function Org() {
  const navy = '#000849', line = '#a0a4b8'
  const card = (i: number) => [94, 275, 457, 658, 840, 1022][i]
  return (
    <Page ch={26} right title={org.title} intro={org.intro} introY={216}>
      <Abs x={528} y={262} w={224} h={54} className="flex items-center rounded-full text-white" style={{ background: navy }}>
        <span className="ml-[9px] flex h-[38px] w-[38px] items-center justify-center rounded-full bg-white"><UserRound size={26} fill={navy} color={navy} strokeWidth={1} /></span>
        <span className="ml-[10px]" style={{ fontSize: 15 }}>{org.lead.role}</span>
        <span className="ml-[30px] font-bold tracking-[0.06em]" style={{ fontSize: 18.5 }}>{org.lead.name}</span>
      </Abs>
      <Abs x={640} y={316} w={1} h={16} style={{ background: line }} />
      <Abs x={348} y={332} w={583} h={1} style={{ background: line }} />
      {org.teams.map((tm, ti) => {
        const tx = ti ? 841 : 276, tcx = tx + 81, Icon = ti ? Settings : Puzzle
        return (
          <div key={tm.name}>
            <Abs x={ti ? 930 : 348} y={332} w={1} h={26} style={{ background: line }} />
            <Abs x={tx} y={358} w={162} h={53} className="flex items-center rounded-full text-white" style={{ background: t.blue }}>
              <span className="ml-[10px] flex h-[38px] w-[38px] items-center justify-center rounded-full bg-white"><Icon size={22} strokeWidth={1.3} color={t.blue} /></span>
              <span className="ml-[22px] font-semibold" style={{ fontSize: 18 }}>{tm.name}</span>
            </Abs>
            <Abs x={tcx} y={411} w={1} h={15} style={{ background: line }} />
            <Abs x={ti ? 741 : 176} y={426} w={364} h={1} style={{ background: line }} />
            {tm.members.map(([role, name], mi) => {
              const x = card(ti * 3 + mi)
              return (
                <div key={name}>
                  <Abs x={x + 82} y={426} w={1} h={19} style={{ background: line }} />
                  <Abs x={x} y={445} w={164} h={208} style={{ background: t.rowA }} />
                  <IconDisc cx={x + 82} cy={490} r={18}><UserRound size={22} fill={t.rowB} color={t.rowB} strokeWidth={1} /></IconDisc>
                  <T x={x} y={524} w={164} size={13} align="center" style={{ color: '#e8eaf8' }}>{role}</T>
                  <T x={x} y={551} w={164} size={18} align="center" className="font-bold tracking-[0.08em] text-white">{name}</T>
                  <Bullets x={x + 33} y={591} items={org.duties} size={14} lh={23} color="#fff" dot="#fff" />
                </div>
              )
            })}
          </div>
        )
      })}
    </Page>
  )
}

function Thanks() {
  return (
    <Frame>
      <Tab x={976} lines={plan} size={17} pt={27} />
      <Abs x={92} y={145} w={432} h={432} className="overflow-hidden rounded-full"><ImagePlaceholder label="photo" className="h-full w-full" /></Abs>
      <T x={588} y={262} size={90} className="font-poppins font-medium" style={{ color: t.navy, letterSpacing: '-0.01em' }}>{thanks.title}</T>
      <T x={592} y={378} size={17.6} style={{ color: '#485060' }}>{thanks.sub}</T>
      {thanks.contacts.map(([k, v], i) => (
        <div key={k}>
          <Badge x={589} y={507 + i * 44.5} w={116} h={32} text={k} bg={t.rowA} size={14.5} className="font-poppins font-medium" />
          <T x={726} y={514 + i * 44.5} size={16.5} className="font-poppins" style={{ color: t.ink }}>{v}</T>
        </div>
      ))}
      <CornerLogo />
    </Frame>
  )
}

const deck: DeckDefinition = { id: '16', title: '하늘색 깔끔 비즈니스 기획', slides: [Cover, Contents, LongText, Overview, Horizontal, ListRows, Photo3, Stats, Keywords4, Pyramid, QuotePage, Process, Visual, Sites, Compare, Part, Mindmap, Formula, Timeline, Swot, Cycle, Mockup, Qna, Numbers, LineChart, Table, Pies, Gantt, Org, Thanks] }
export default deck
