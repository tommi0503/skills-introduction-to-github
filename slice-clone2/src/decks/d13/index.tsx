import type { DeckDefinition } from '../../ui'
import { Abs, ImagePlaceholder } from '../../ui'
import { Atom, ChartLine, ChartPie, Cog, Crosshair, FileText, Globe, Handshake, MapPinned, PencilLine, Presentation, Puzzle, SearchCheck } from 'lucide-react'
import { Box, Donut, Lines } from '../../ui'
import { Bullets, NoteSlide, Sticker, Sub, Tag, Text, Title, ToneCard } from './components'
import { bars, chapter, cover, donut, iconsGrid, iconsList, mainImage, process, threeCol, threeImages, threeRow, toc, twoImages } from './data'
import { t, tone } from './theme'

const ICONS = { handshake: Handshake, doc: FileText, puzzle: Puzzle, map: MapPinned, globe: Globe, search: SearchCheck, board: Presentation, pie: ChartPie, trend: ChartLine, target: Crosshair, cog: Cog, pencil: PencilLine, atom: Atom }
const Photo = ({ x, y, w, h, r }: { x: number; y: number; w: number; h: number; r?: string }) => (
  <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label="photo" className="h-full w-full" style={{ borderRadius: r }} /></Abs>
)

function Cover() {
  return (
    <NoteSlide>
      <Abs x={121} y={98} w={26} h={18}><ImagePlaceholder label="logo mark" className="h-full w-full" /></Abs>
      <Lines x={156} cy={107} size={15.5} className="font-bold tracking-[0.12em]" color={t.ink} lines={[cover.brand]} />
      <Sticker top={cover.year} bottom={cover.month} big />
      <Lines x={656} cy={260} align="center" size={86} className="font-medium tracking-[-0.03em]" color="#8a8a8a" lines={[cover.title[0]]} />
      <Lines x={656} cy={378} align="center" size={104} className="font-bold tracking-[-0.02em]" color={t.green} lines={[cover.title[1]]} />
      <Lines x={656} cy={479} align="center" size={16} className="tracking-[0.42em]" color="#888" lines={[cover.sub]} />
      <Box x={146} y={569} w={1018} h={56} bg="#fcf1ee" className="rounded" style={{ border: `1.5px solid ${t.green}` }} />
      <Lines x={179} cy={597} size={21} className="font-medium" color={t.green} lines={[<>{cover.org}&nbsp;<b className="text-[#111]">{cover.name}</b></>]} />
      <Lines x={676} cy={598} size={20} color={t.text} lines={[<><b style={{ color: t.green }}>T.</b>&nbsp;{cover.tel}</>]} />
      <Lines x={891} cy={598} size={20} color={t.text} lines={[<><b style={{ color: t.green }}>E.</b>&nbsp;{cover.mail}</>]} />
    </NoteSlide>
  )
}

function Toc() {
  return (
    <NoteSlide page={2}>
      <Title text={toc.title} />
      {toc.items.map((it, i) => {
        const x = 153 + (i % 3) * 344.5, y = 288 + Math.floor(i / 3) * 190
        return (
          <div key={i}>
            <Tag x={x} y={y - 33} w={180} h={42} c={it.c} text={it.chapter} size={15.5} className="rounded-t-xl" />
            <ToneCard x={x} y={y} w={319} h={136} c={it.c} />
            <Lines x={x + 38} cy={y + 41} size={29} color={tone[it.c].fg} lines={[it.title]} />
            <Bullets x={x + 41} cy={y + 81} lh={21.5} gap={0} size={15} items={it.bullets.map((b) => [b])} />
          </div>
        )
      })}
    </NoteSlide>
  )
}

function Chapter() {
  return (
    <NoteSlide fill={t.green}>
      <Lines x={146} cy={407} size={98} className="font-bold tracking-[-0.02em]" color="#fff" lines={[chapter.title]} />
      {[497, 551, 605].map((y) => <Box key={y} x={149} y={y} w={1014} h={1.5} bg="#d8e5dc" />)}
      {chapter.lines.map((l, i) => <Lines key={i} x={149} cy={525 + i * 54} size={27} color="#fff" lines={[l]} />)}
    </NoteSlide>
  )
}

function ThreeCol() {
  return (
    <NoteSlide page={4}>
      <Title text={threeCol.title} />
      <Box x={152} y={242} w={1007} h={79} bg={t.soft} className="rounded-xl" />
      <Sub x={656} cy={282} align="center" text={threeCol.sub} />
      {threeCol.items.map((k, i) => {
        const x = 152 + i * 344.5
        return (
          <div key={k.key}>
            <Tag x={x} y={354} w={204} h={50} c={k.c} text={k.key} className="rounded-t-lg" />
            <ToneCard x={x} y={403} w={317} h={214} c={k.c} />
            <Bullets x={x + 32} cy={448} items={k.bullets} />
          </div>
        )
      })}
    </NoteSlide>
  )
}

function ThreeRow() {
  return (
    <NoteSlide page={5}>
      <Title text={threeRow.title} />
      <Sub x={656} cy={258} align="center" text={threeRow.sub} />
      {threeRow.items.map((k, i) => {
        const y = 311 + i * 105.5
        return (
          <div key={k.key}>
            <Tag x={152} y={y + 11} w={210} h={68} c={k.c} text={k.key} className="rounded-l-lg" />
            <ToneCard x={354} y={y} w={803} h={92} c={k.c} />
            <Bullets x={407} cy={y + 30} lh={30} items={k.bullets.map((b) => [b])} gap={0} />
          </div>
        )
      })}
    </NoteSlide>
  )
}

function MainImage() {
  return (
    <NoteSlide page={6}>
      <Title text={mainImage.title} />
      <Photo x={152} y={234} w={463} h={340} />
      <Sub x={665} cy={272} text={mainImage.sub} />
      <Text x={665} cy={318} lines={mainImage.desc} />
      <Tag x={665} y={418} w={204} h={50} c="green" text={mainImage.key} className="rounded-t-lg" />
      <Box x={665} y={467} w={496} h={95} bg="#fcf2ef" className="rounded" style={{ border: `2px solid ${t.green}` }} />
      <Lines x={904} cy={515} align="center" w={496} size={17.5} color={t.text} lines={[mainImage.keyText]} />
    </NoteSlide>
  )
}

function TwoImages() {
  return (
    <NoteSlide page={7}>
      <Title text={twoImages.title} />
      <Sub x={150} cy={299} text={twoImages.sub} />
      <Text x={150} cy={491} lines={twoImages.desc} size={17.5} lh={30} />
      {twoImages.items.map((k, i) => {
        const x = 458 + i * 360, cx = x + 169
        return (
          <div key={k.key}>
            <ToneCard x={x} y={265} w={339} h={350} c={k.c} r={8} />
            <Photo x={x + 2} y={267} w={335} h={200} r="6px 6px 0 0" />
            <Box x={x + 2} y={467} w={335} h={2} bg={tone[k.c].fg} />
            <Tag x={cx - 98} y={490} w={196} h={36} c={k.c} text={k.key} className="rounded-md" />
            <Text x={cx} cy={552} align="center" w={339} lh={28} lines={k.desc} />
          </div>
        )
      })}
    </NoteSlide>
  )
}

function ThreeImages() {
  return (
    <NoteSlide page={8}>
      <Title text={threeImages.title} />
      <Box x={152} y={237} w={1007} h={105} bg={t.soft} className="rounded-xl" />
      <Sub x={209} cy={290} text={threeImages.sub} />
      <Text x={622} cy={274} lines={threeImages.desc} />
      {threeImages.items.map((k, i) => {
        const x = 152 + i * 341.5, cx = x + 160
        return (
          <div key={k.key}>
            <Photo x={x} y={362} w={320} h={148} r="6px 6px 0 0" />
            <Tag x={x} y={510} w={320} h={43} c={k.c} text={k.key} className="rounded-b-md" />
            <Text x={cx} cy={580} align="center" w={340} lh={28} lines={k.desc} />
          </div>
        )
      })}
    </NoteSlide>
  )
}

function Bars() {
  const y0 = 546, unit = 3.62, xs = [298, 417, 536]
  return (
    <NoteSlide page={9}>
      <Title text={bars.title} />
      <Box x={153} y={265} w={504} h={354} bg="#fbeeee" className="rounded-lg" style={{ border: `2px solid ${t.green}` }} />
      {bars.ticks.map((v) => (
        <div key={v}>
          <Box x={238} y={y0 - v * unit} w={357} h={1} bg={v ? '#ddd' : '#999'} />
          <Lines x={232} cy={y0 - v * unit} align="right" w={40} size={15} color={t.text} lines={[String(v)]} />
        </div>
      ))}
      <Box x={238} y={y0 - 60 * unit} w={1} h={60 * unit} bg="#999" />
      {bars.data.map((b, i) => (
        <div key={b.label}>
          <Box x={xs[i] - 27} y={y0 - b.v * unit} w={54} h={b.v * unit} bg={t.green} />
          <Lines x={xs[i]} cy={y0 - b.v * unit - 19} align="center" w={60} size={15} color={t.green} lines={[String(b.v)]} />
          <Lines x={xs[i]} cy={y0 + 16} align="center" w={80} size={15} className="font-medium" color={t.text} lines={[b.label]} />
        </div>
      ))}
      <Sub x={726} cy={287} text={bars.sub} />
      <Text x={726} cy={331} lines={bars.desc} />
      <Box x={696} y={461} w={463} h={157} bg={t.soft} className="rounded-xl" />
      <Bullets x={742} cy={496} lh={34.5} gap={0} size={17.5} items={bars.bullets.map((b) => [b])} />
    </NoteSlide>
  )
}

function DonutPage() {
  const cx = 845, cy = 327, r = 158
  const segs = donut.segs.map((s) => ({ v: (s.v / 120) * 100, c: tone[s.c].fg }))
  const labels = [{ x: 900, y: 227, v: '20' }, { x: 941, y: 378, v: '40' }, { x: 735, y: 323, v: '60' }]
  return (
    <NoteSlide page={10}>
      <Box x={593} y={120} w={580} h={493} bg={t.soft} className="rounded-xl" />
      <Lines x={151} cy={172} lh={75} size={60} className="font-medium tracking-[-0.01em]" color={t.ink} lines={donut.title} />
      <Sub x={150} cy={466} text={donut.sub} />
      <Text x={150} cy={521} lines={donut.desc} />
      <Donut cx={cx} cy={cy} r={r} hole={63} segs={segs} holeBg={t.soft} />
      {labels.map((l) => <Lines key={l.v} x={l.x} cy={l.y} align="center" w={40} size={16} className="font-bold" color={t.ink} lines={[l.v]} />)}
      {donut.segs.map((s, i) => (
        <div key={s.label}>
          <Box x={1025} y={290 + i * 27} w={16} h={16} bg={tone[s.c].fg} className="rounded-sm" />
          <Lines x={1048} cy={298 + i * 27} size={16.5} color={t.text} lines={[s.label]} />
        </div>
      ))}
      <Bullets x={700} cy={526} lh={31} gap={0} size={17.5} items={donut.bullets.map((b) => [b])} />
    </NoteSlide>
  )
}

function IconsGrid() {
  return (
    <NoteSlide page={11}>
      <Title text={iconsGrid.title} />
      <Sub x={656} cy={250} align="center" text={iconsGrid.sub} />
      <Text x={656} cy={290} align="center" lines={[iconsGrid.desc]} size={17.5} />
      {iconsGrid.items.map((k, i) => {
        const x = 153 + i * 204, cx = x + 94
        const Icon = ICONS[k.icon]
        return (
          <div key={k.key}>
            <Tag x={x + 8} y={329} w={172} h={45} c={k.c} text={k.key} size={18} className="rounded-t-xl" />
            <ToneCard x={x} y={369} w={188} h={233} c={k.c} r={10} />
            <Abs x={cx - 38} y={392}><Icon size={76} strokeWidth={1.2} color="#222" /></Abs>
            <Text x={cx} cy={502} align="center" w={188} lh={28} lines={k.desc} />
          </div>
        )
      })}
    </NoteSlide>
  )
}

function IconsList() {
  return (
    <NoteSlide page={12}>
      {iconsList.items.map((k, i) => {
        const cy = 115 + i * 102.3
        const Icon = ICONS[k.icon]
        return (
          <div key={k.key}>
            <ToneCard x={193} y={cy - 37} w={541} h={74} c={k.c} r={4} />
            <Abs x={194 - 42} y={cy - 42} w={84} h={84} className="rounded-full" style={{ background: tone[k.c].fg }} />
            <Abs x={194 - 23} y={cy - 23}><Icon size={46} strokeWidth={1.6} color="#fff" /></Abs>
            <Lines x={274} cy={cy - 13} size={18} className="tracking-[0.08em]" color={tone[k.c].fg} lines={[k.key]} />
            <Lines x={274} cy={cy + 12} size={17.5} color={t.text} lines={[k.text]} />
          </div>
        )
      })}
      <Lines x={800} cy={170} lh={75} size={60} className="font-medium tracking-[-0.01em]" color={t.ink} lines={iconsList.title} />
      <Sub x={801} cy={455} text={iconsList.sub} />
      <Text x={801} cy={504} lines={iconsList.desc} size={17} lh={30} />
    </NoteSlide>
  )
}

function Process() {
  return (
    <NoteSlide page={13}>
      <Title text={process.title} />
      <Box x={153} y={239} w={432} h={66} bg={t.green} className="rounded-t-2xl" />
      <Lines x={369} cy={271} align="center" w={432} size={31} color="#fff" lines={[process.sub]} />
      <Lines x={618} cy={274} size={17.5} color={t.text} lines={[process.note]} />
      <Box x={153} y={303} w={1005} h={313} bg="#fbeeee" className="rounded-lg" style={{ border: `2.5px solid ${t.green}` }} />
      <Box x={300} y={474} w={720} h={1.5} bg="#e7a9b8" />
      {process.items.map((k, i) => {
        const cx = 304 + i * 234.5
        const Icon = ICONS[k.icon]
        return (
          <div key={k.key}>
            <Abs x={cx - 44} y={344}><Icon size={88} strokeWidth={1.3} color={t.green} /></Abs>
            <Tag x={cx - 88} y={453} w={176} h={44} c="pink" text={k.key} size={18.5} className="rounded-full" />
            <Text x={cx} cy={525} align="center" w={240} lh={29} lines={k.desc} />
          </div>
        )
      })}
    </NoteSlide>
  )
}

const deck: DeckDefinition = { id: '13', title: '베이지 심플 프레젠테이션 소개', slides: [Cover, Toc, Chapter, ThreeCol, ThreeRow, MainImage, TwoImages, ThreeImages, Bars, DonutPage, IconsGrid, IconsList, Process] }
export default deck
