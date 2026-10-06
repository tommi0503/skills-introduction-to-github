import { ChessRook, ClipboardCheck, FileSearch, HandCoins, Handshake, Lightbulb, LocateFixed, MonitorCheck, Newspaper, Trophy, UserRoundSearch, Target } from 'lucide-react'
import type { DeckDefinition } from '../../ui'
import { Abs, cn } from '../../ui'
import { CornerLogo, Frame, Lines, Photo, Pill, T, Tab, Title } from './components'
import { compare, contents, cover, keywords, longText, numbers, part, photoCols, process, tabs } from './data'
import { t } from './theme'

function Cover() {
  return (
    <Frame>
      <Tab x={952} lines={tabs.plan} />
      <T x={126} y={236} size={90} className="font-bold" style={{ letterSpacing: '-0.012em' }}>{cover.title[0]}</T>
      <T x={126} y={334} size={90} className="font-bold" style={{ color: t.ink, letterSpacing: '-0.012em' }}>{cover.title[1]}</T>
      <T x={127} y={449} size={27} className="font-semibold" style={{ letterSpacing: '-0.012em' }}>{cover.sub}</T>
      <Lines x={127} y={593} size={18} lh={25} lines={cover.info} className="font-medium" style={{ letterSpacing: '0.025em' }} />
      <CornerLogo />
    </Frame>
  )
}

function Contents() {
  return (
    <Frame>
      <Tab x={79} lines={tabs.plan} />
      <T x={126} y={334} size={53} className="font-bold">{contents.title}</T>
      {contents.items.map((it, i) => {
        const cx = 596 + (i % 3) * 224, y = 182 + Math.floor(i / 3) * 221
        return (
          <div key={it.no}>
            <T x={cx - 100} y={y} w={200} size={16} align="center" style={{ color: t.blue }}>{it.no}</T>
            <Abs x={cx - 93} y={y + 31} w={186} h={1} style={{ background: '#5a5a78' }} />
            <Lines x={cx - 100} y={y + 46} w={200} size={20} lh={26} align="center" lines={it.lines} className="font-semibold" style={{ color: '#000030' }} />
            <Lines x={cx - 82} y={y + 110} size={16.5} lh={30} lines={it.bullets} style={{ color: t.body }} />
          </div>
        )
      })}
      <CornerLogo />
    </Frame>
  )
}

function LongText() {
  return (
    <Frame>
      <Tab x={79} lines={tabs.ch(1)} />
      <Title text={longText.title} cx={364} y={236} size={50} />
      <Lines x={124} y={326} w={482} size={16.5} lh={27} lines={longText.body} justify style={{ color: t.ink }} />
      {longText.pills.map((p, i) => <Pill key={p} x={110 + i * 175} y={552} w={167} h={47} text={p} />)}
      <Photo x={672} y={40} w={534} h={640} />
    </Frame>
  )
}

const kwIcons = [UserRoundSearch, FileSearch, Newspaper, LocateFixed]
function Keywords() {
  return (
    <Frame>
      <Tab x={79} lines={tabs.ch(2)} />
      <Title text={keywords.title} y={140} />
      {keywords.rows.map((r, i) => {
        const y = 240 + i * 102, Icon = kwIcons[i]
        return (
          <div key={i}>
            <Abs x={170} y={y} w={592} h={90} style={{ background: i % 2 ? t.sky : t.pale, borderRadius: '0 45px 45px 0' }} />
            <T x={207} y={y + 28} size={19} className="font-semibold" style={{ color: '#000030' }}>{r.title}</T>
            <T x={207} y={y + 59} size={16} style={{ color: t.body }}>{r.sub}</T>
            <Abs x={685} y={y + 26}><Icon size={38} strokeWidth={1.3} color={t.navy} /></Abs>
            <Abs x={758} y={y + 41} w={8} h={8} className="rounded-full" style={{ background: t.mid }} />
            <Abs x={766} y={y + 45} w={41} h={1} style={{ background: '#777' }} />
          </div>
        )
      })}
      <Abs x={806} y={285} w={1} h={311} style={{ background: '#777' }} />
      <Abs x={806} y={440} w={40} h={1} style={{ background: '#777' }} />
      <Abs x={846} y={311} w={262} h={262} className="flex flex-col items-center rounded-full text-white" style={{ background: t.blue }}>
        <div className="mt-[39px] font-semibold leading-none" style={{ fontSize: 18 }}>{keywords.goal.head}</div>
        <Target size={44} strokeWidth={1.4} className="mt-[22px]" />
        <div className="mt-[18px] text-center font-medium" style={{ fontSize: 17, lineHeight: '27px' }}>{keywords.goal.lines.map((l) => <div key={l}>{l}</div>)}</div>
      </Abs>
    </Frame>
  )
}

function Part() {
  const panel = { x: 44, y: 144, w: 1192, h: 432 }
  return (
    <Frame panel={panel}>
      <Tab x={975} y={133} lines={tabs.plan} />
      <T x={127} y={275} size={50} className="font-bold">{part.no}</T>
      <T x={340} y={271} size={54} style={{ letterSpacing: '-0.01em' }}>{part.lines[0]}</T>
      <T x={340} y={340} size={54} className="font-bold" style={{ letterSpacing: '-0.01em' }}>{part.lines[1]}</T>
      {part.pills.map((p, i) => <Pill key={p} x={341 + i * 196} y={433} w={189} h={51} size={16} text={p} />)}
      <CornerLogo bottom={576} />
    </Frame>
  )
}

function PhotoCols() {
  return (
    <Frame>
      <Tab x={79} lines={tabs.ch(3)} />
      <Title text={photoCols.title} y={140} />
      {photoCols.cols.map((c, i) => {
        const x = 109 + i * 367, cx = x + 169
        return (
          <div key={c.k}>
            <Photo x={x} y={270} w={338} h={191} />
            <Abs x={cx - 37} y={233} w={74} h={74} className="rounded-full bg-white" />
            <T x={cx - 20} y={273} w={40} size={17} align="center" className="font-medium" style={{ color: t.ink }}>{c.k}</T>
            <Abs x={x} y={461} w={338} h={177} style={{ background: t.pale }} />
            <T x={x} y={489} w={338} size={18.5} align="center" className="font-semibold">{c.head}</T>
            <Lines x={x} y={527} w={338} size={16.2} lh={27.5} align="center" lines={c.body} style={{ color: t.body }} />
          </div>
        )
      })}
    </Frame>
  )
}

const numIcons = [Trophy, HandCoins, ChessRook]
const numCols = [{ x: 100, w: 496, bg: t.blue, fg: t.blue }, { x: 596, w: 328, bg: t.mid, fg: t.mid }, { x: 924, w: 270, bg: t.stone, fg: '#9a9a9a' }]
function Numbers() {
  return (
    <Frame>
      <Tab x={79} lines={tabs.ch(4)} />
      <Title text={numbers.title} y={140} />
      <Lines x={140} y={247} w={1000} size={16.9} lh={27} align="center" lines={numbers.intro} style={{ color: t.ink }} />
      {numbers.items.map((it, i) => {
        const c = numCols[i], Icon = numIcons[i]
        return (
          <div key={it.n}>
            <Abs x={c.x} y={384} w={c.w} h={89} className="flex items-center text-white" style={{ background: c.bg }}>
              <span className="ml-[24px] font-bold leading-none" style={{ fontSize: i ? 42 : 52 }}>{it.n}</span>
              <span className="ml-[3px] mt-[14px] font-semibold leading-none" style={{ fontSize: 24 }}>%</span>
              <span className="ml-[22px] font-semibold leading-none" style={{ fontSize: 18 }}>{it.label}</span>
              <Icon size={36} strokeWidth={1.3} className="ml-auto mr-[30px]" />
            </Abs>
            <T x={c.x + 22} y={503} size={18.5} className="font-semibold" style={{ color: c.fg }}>{it.head}</T>
            <Lines x={c.x + 20} y={539} size={16} lh={27} lines={it.body} style={{ color: t.ink }} />
          </div>
        )
      })}
    </Frame>
  )
}

function Compare() {
  return (
    <Frame>
      <Tab x={971} lines={tabs.ch(5)} />
      <Title text={compare.title} y={140} />
      {compare.heads.map((h, i) => <T key={h} x={[253, 827][i]} y={260} w={200} size={16} align="center" style={{ color: t.ink }}>{h}</T>)}
      {compare.rows.map((r, i) => {
        const y = 300 + i * 78
        return (
          <div key={r.key}>
            <Abs x={180} y={y} w={346} h={70} className="flex items-center justify-center" style={{ background: t.grey, borderRadius: '35px 0 0 35px', color: t.ink, fontSize: 17.7 }}>{r.text}</Abs>
            <Abs x={540} y={y + 35} w={52} h={1} style={{ background: '#555' }} />
            <T x={590} y={y + 27} w={100} size={17} align="center" className="font-semibold" style={{ color: '#111' }}>{r.key}</T>
            <Abs x={688} y={y + 35} w={52} h={1} style={{ background: '#555' }} />
            <Abs x={754} y={y} w={346} h={70} className="flex items-center justify-center text-white" style={{ background: t.mid, borderRadius: '0 35px 35px 0', fontSize: 17.7 }}>{r.text}</Abs>
          </div>
        )
      })}
      <Abs x={180} y={558} w={920} h={80} className="flex items-center rounded-full text-white" style={{ background: t.blue }}>
        <span className="ml-[15px] flex h-[38px] w-[125px] items-center justify-center rounded-full bg-white font-semibold" style={{ color: t.navy, fontSize: 16 }}>{compare.insight.tag}</span>
        <span className="ml-[24px] whitespace-nowrap font-semibold" style={{ fontSize: 18.7 }}>{compare.insight.text}</span>
      </Abs>
    </Frame>
  )
}

const procIcons = [Lightbulb, ClipboardCheck, MonitorCheck, Handshake]
const procBg = [t.pale, t.sky, t.pale, t.blue]
function Process() {
  return (
    <Frame>
      <Tab x={79} lines={tabs.ch(6)} />
      <Title text={process.title} y={140} />
      {process.steps.map((s, i) => {
        const x = 106 + i * 271.5, dark = i === 3, Icon = procIcons[i]
        return (
          <div key={s.step} className={cn(dark && 'text-white')} style={{ color: dark ? '#fff' : undefined }}>
            <Abs x={x} y={292} w={252} h={346} style={{ background: procBg[i], borderRadius: '0 0 126px 126px' }} />
            <Abs x={x} y={361} w={252} h={1} style={{ background: dark ? '#fff' : '#fff' }} />
            <T x={x} y={318} w={252} size={15} align="center" className="font-medium" style={{ color: dark ? '#fff' : t.navy }}>{s.step}</T>
            <T x={x} y={393} w={252} size={19} align="center" className="font-semibold" style={{ color: dark ? '#fff' : t.navy }}>{s.head}</T>
            <Lines x={x} y={443} w={252} size={16} lh={24} align="center" lines={s.body} style={{ color: dark ? '#fff' : t.ink }} />
            <Abs x={x + 108} y={553}><Icon size={36} strokeWidth={1.3} color={dark ? '#fff' : t.navy} /></Abs>
          </div>
        )
      })}
    </Frame>
  )
}

const deck: DeckDefinition = { id: '02', title: '파란색의 심플한 비즈니스 기획서', slides: [Cover, Contents, LongText, Keywords, Part, PhotoCols, Numbers, Compare, Process] }
export default deck
