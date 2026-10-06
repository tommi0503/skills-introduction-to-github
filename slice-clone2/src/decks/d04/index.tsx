import type { DeckDefinition } from '../../ui'
import { Abs, ImagePlaceholder } from '../../ui'
import { BookOpen, ClipboardList, Microscope, MonitorCheck } from 'lucide-react'
import { Box, Lines } from '../../ui'
import { DownTab, PaperSlide, PlayPill, Title, Wave } from './components'
import { closing, compare, core, cover, four, points, praise, summary, toc } from './data'
import { t } from './theme'

function Cover() {
  return (
    <PaperSlide deco={cover.deco}>
      <Lines x={67} cy={59} size={19} color={t.text} lines={[cover.kicker]} />
      <Lines x={640} cy={277} lh={128} align="center" size={104} className={t.head} color={t.ink} lines={cover.title} />
      <Lines x={640} cy={516} align="center" size={28} color={t.text} lines={[cover.author]} />
    </PaperSlide>
  )
}

function Toc() {
  return (
    <PaperSlide deco={toc.deco}>
      <Title text={toc.title} cy={177} size={64} />
      {toc.items.map((it, i) => {
        const col = i % 2, row = Math.floor(i / 2)
        const cy = [308, 423, 558][row]
        const x = col ? 663 : 188
        return (
          <div key={it.n}>
            <Lines x={x} cy={cy} size={66} className="font-black tracking-[-0.04em]" color={t.mint} lines={[it.n]} />
            <Lines x={x + 101} cy={cy} size={29} className="font-medium" color={t.text} lines={[it.text]} />
          </div>
        )
      })}
      {[358, 491].map((y) => <Wave key={y} x={182} y={y} w={888} />)}
    </PaperSlide>
  )
}

function Praise() {
  return (
    <PaperSlide deco={praise.deco}>
      <Title text={praise.title} cy={162} size={66} />
      {praise.cards.map((c, i) => {
        const x = 98 + i * 367, cx = x + 173
        return (
          <div key={c.quote}>
            <Box x={x} y={245} w={346} h={364} bg={t.card} className="rounded-2xl" />
            <Abs x={cx - 120} y={232} w={240} h={240}><ImagePlaceholder label="child photo" className="h-full w-full rounded-full" /></Abs>
            <Abs x={cx - 145} y={226} w={66} h={66}><ImagePlaceholder label="star burst" className="h-full w-full rounded-full" tone="#f3f0d9" /></Abs>
            <Abs x={cx + 70} y={396} w={56} h={56}><ImagePlaceholder label="star burst" className="h-full w-full rounded-full" tone="#f3f0d9" /></Abs>
            <Lines x={cx} cy={509} align="center" w={346} size={31} className="font-medium" color={t.text} lines={[c.quote]} />
            <Lines x={cx} cy={555} lh={25} align="center" w={346} size={17.5} color={t.sub} lines={c.desc} />
          </div>
        )
      })}
      <Lines x={1170} cy={628} align="right" size={8} color={t.sub} lines={[praise.note]} />
    </PaperSlide>
  )
}

function Compare() {
  return (
    <PaperSlide deco={compare.deco}>
      <Title text={compare.title} cy={155} size={66} />
      {compare.cards.map((c, i) => {
        const x = 127 + i * 524, cx = x + 251
        return (
          <div key={i}>
            <Box x={x} y={226} w={502} h={402} bg={t.card} className="rounded-xl" />
            <Abs x={x} y={226} w={502} h={235}><ImagePlaceholder label="topic photo" className="h-full w-full rounded-xl" /></Abs>
            <DownTab cx={cx - 1} cy={459} r={30} color={t.peach} />
            <Lines x={cx} cy={527} align="center" w={502} size={30} className="font-medium" color={t.text} lines={[c.topic]} />
            <Lines x={cx} cy={567} lh={24} align="center" w={502} size={15.5} color={t.sub} lines={c.desc} />
          </div>
        )
      })}
    </PaperSlide>
  )
}

function Four() {
  return (
    <PaperSlide deco={four.deco}>
      <Title text={four.title} cy={153} size={66} />
      {four.items.map((it, i) => {
        const x = [135, 641][i % 2], y = [222, 432][Math.floor(i / 2)], cx = x + 242
        return (
          <div key={it.n}>
            <Box x={x} y={y} w={485} h={195} bg={t.card} className="rounded-xl" />
            <Lines x={cx} cy={y + 51} align="center" w={485} size={35} className="font-medium" color={t.text} lines={[<><span style={{ color: t.mint }}>{it.n}</span>&nbsp;{it.label}</>]} />
            <Wave x={cx - 115} y={y + 81} w={230} />
            <Lines x={cx} cy={y + 115} lh={27} align="center" w={485} size={18.5} color={t.sub} lines={it.desc} />
          </div>
        )
      })}
    </PaperSlide>
  )
}

function Points() {
  return (
    <PaperSlide deco={points.deco}>
      <Title text={points.title} cy={155} size={66} />
      {points.rows.map((r, i) => {
        const y = 223 + i * 81.6
        return (
          <div key={i}>
            <Abs x={94} y={y + 6} w={52} h={42}><ImagePlaceholder label="tab shape" className="h-full w-full rounded-md" tone="#cfe9d9" /></Abs>
            <Box x={134} y={y} w={207} h={74} bg={t.mintPale} />
            <Lines x={237} cy={y + 37} align="center" w={207} size={25} className="font-bold" color="#333" lines={[r.key]} />
            <Box x={346} y={y} w={839} h={74} bg={t.card} />
            <Lines x={374} cy={y + 37} size={21} color={t.text} lines={[r.text]} />
          </div>
        )
      })}
    </PaperSlide>
  )
}

const ICONS = { microscope: Microscope, checklist: ClipboardList, book: BookOpen, monitor: MonitorCheck }

function Core() {
  return (
    <PaperSlide deco={core.deco}>
      <Title text={core.title} cy={150} size={66} />
      {core.cols.map((c, i) => {
        const x = 107 + i * 269, cx = x + 130
        const Icon = ICONS[c.icon]
        return (
          <div key={i}>
            <Box x={x} y={218} w={260} h={79} bg={t.mintPale} />
            <Lines x={cx} cy={256} align="center" w={260} size={26} className="font-medium" color="#333" lines={[c.key]} />
            <Box x={x} y={308} w={260} h={236} bg={t.card} />
            <DownTab cx={cx} cy={306} r={0} color={t.mint} />
            <Abs x={cx - 58} y={340}><Icon size={116} strokeWidth={1.1} color="#4a4a4a" /></Abs>
            <Lines x={cx} cy={487} lh={24} align="center" w={260} size={16.5} color={t.sub} lines={c.desc} />
          </div>
        )
      })}
      <Box x={107} y={555} w={1066} h={77} bg="#eef7fb" />
      <Lines x={640} cy={592} align="center" size={25} className="font-medium" color="#333" lines={[core.result]} />
    </PaperSlide>
  )
}

function Summary() {
  return (
    <PaperSlide deco={summary.deco}>
      <Title text={summary.title} cy={153} size={66} />
      {summary.rows.map((r, i) => (
        <PlayPill key={i} x={139} y={223 + i * 100.6} w={1010} h={87} color={r.c} text={r.text} size={24} />
      ))}
    </PaperSlide>
  )
}

function Closing() {
  return (
    <PaperSlide deco={closing.deco}>
      <Lines x={640} cy={230} lh={123} align="center" size={104} className={t.head} color={t.ink} lines={closing.title} />
      <Lines x={640} cy={468} align="center" size={31} className="font-black" color={t.ink} lines={[closing.question]} />
      <PlayPill x={312} y={500} w={656} h={58} color="#94d6ae" text={closing.pill} size={22} />
    </PaperSlide>
  )
}

const deck: DeckDefinition = { id: '04', title: '노랑과 초록의 기본적인 학교 수업자료', slides: [Cover, Toc, Praise, Compare, Four, Points, Core, Summary, Closing] }
export default deck
