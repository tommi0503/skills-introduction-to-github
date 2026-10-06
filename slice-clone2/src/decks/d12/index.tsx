import type { DeckDefinition } from '../../ui'
import { Abs, ImagePlaceholder } from '../../ui'
import { ChevronRight, FileStack, Lightbulb, MessageCircleQuestion, Presentation } from 'lucide-react'
import { Box, Lines } from '../../ui'
import { CalendarSlide, Card, Circle, Ticks, TitleBar } from './components'
import { chapter, compare, contents, cover, flow, fourText, keywords, list, photoText, photos } from './data'
import { t } from './theme'

const Photo = ({ x, y, w, h }: { x: number; y: number; w: number; h: number }) => (
  <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label="photo" className="h-full w-full" /></Abs>
)
const ICONS = { idea: Lightbulb, docs: FileStack, present: Presentation }

function Cover() {
  return (
    <CalendarSlide banded light>
      <Lines x={640} cy={285} align="center" size={80} className="tracking-[-0.03em]" color="#95a8a5" lines={[cover.title[0]]} />
      <Lines x={640} cy={388} align="center" size={82} className="font-medium tracking-[-0.03em]" color={t.ink} lines={[cover.title[1]]} />
      <Box x={226} y={455} w={826} h={45} bg="#f2f2f4" />
      <Lines x={640} cy={480} align="center" size={16} color={t.text} lines={[cover.info.join('\u00a0\u00a0\u00a0\u00a0|\u00a0\u00a0\u00a0\u00a0')]} />
      <Lines x={640} cy={641} align="center" size={12} className="font-bold tracking-[0.2em]" color="#999" lines={[cover.site]} />
    </CalendarSlide>
  )
}

function Contents() {
  return (
    <CalendarSlide banded light>
      <Lines x={640} cy={163} align="center" size={44} className={`${t.latin} font-semibold`} color={t.ink} lines={[contents.title]} />
      {contents.items.map((it, i) => {
        const x = i < 3 ? 123 : 654, y = 228 + (i % 3) * 138
        return (
          <div key={it.n}>
            <Card x={x} y={y} w={505} h={117} />
            <Lines x={x + 35} cy={y + 60} size={26} className={t.latin} color={t.sageText} lines={[it.n]} />
            <Lines x={x + 267} cy={y + 42} align="center" w={400} size={18.3} className="font-medium" color={t.ink} lines={[it.title]} />
            <Lines x={x + 267} cy={y + 78} align="center" w={400} size={14} color="#555" lines={[it.sub]} />
          </div>
        )
      })}
      <Ticks pts={[[120, 334], [120, 472], [120, 610], [651, 334], [651, 472], [651, 610]]} />
    </CalendarSlide>
  )
}

function Keywords() {
  return (
    <CalendarSlide>
      <TitleBar n={keywords.n} title={keywords.title} />
      {keywords.items.map((k, i) => {
        const x = 123 + i * 358, cx = x + 159
        const Icon = ICONS[k.icon]
        return (
          <div key={k.name}>
            <Card x={x} y={214} w={318} h={400} />
            <Circle cx={cx} cy={323} r={63}><Icon size={54} strokeWidth={1.2} color="#444" /></Circle>
            <Lines x={cx} cy={428} align="center" w={318} size={23} className={t.latin} color={t.ink} lines={[k.name]} />
            <Box x={x + 29} y={467} w={258} h={0} style={{ borderTop: '1.5px dashed #888' }} />
            <Lines x={cx} cy={500} lh={23} align="center" w={318} size={14} color={t.text} lines={k.desc} />
          </div>
        )
      })}
      <Ticks pts={[[420, 210], [778, 210], [1136, 210], [118, 600], [476, 600], [834, 600]]} />
    </CalendarSlide>
  )
}

function PhotoText() {
  return (
    <CalendarSlide>
      <TitleBar n={photoText.n} title={photoText.title} />
      <Photo x={103} y={212} w={500} h={409} />
      <Card x={634} y={218} w={528} h={111} />
      <Lines x={898} cy={251} align="center" w={528} size={16.5} color={t.sageText} lines={[photoText.kicker]} />
      <Lines x={898} cy={287} align="center" w={528} size={23} color={t.ink} lines={[photoText.lead]} />
      <Lines x={645} cy={372} lh={25.3} size={13.8} className="tracking-[-0.02em]" color={t.text} lines={photoText.body} />
      <Ticks pts={[[1142, 213], [630, 311]]} />
    </CalendarSlide>
  )
}

function FourText() {
  return (
    <CalendarSlide>
      <TitleBar n={fourText.n} title={fourText.title} />
      {fourText.items.map((it, i) => {
        const x = i % 2 ? 657 : 99, y = i < 2 ? 211 : 427, cx = x + 264
        return (
          <div key={i}>
            <Card x={x} y={y} w={527} h={193} />
            <Lines x={cx} cy={y + 50} align="center" w={527} size={16.5} className={t.latin} color={t.sageText} lines={[it.kicker]} />
            <Box x={x + 41} y={y + 70} w={447} h={43} bg="#fff" />
            <Lines x={cx} cy={y + 91} align="center" w={447} size={23} color={t.ink} lines={[it.title]} />
            <Lines x={cx} cy={y + 136} align="center" w={527} size={14.5} color={t.text} lines={[it.desc]} />
          </div>
        )
      })}
      <Ticks pts={[[97, 390], [655, 390], [97, 606], [655, 606]]} />
    </CalendarSlide>
  )
}

function Chapter() {
  return (
    <CalendarSlide banded light>
      <Box x={145} y={237} w={279} h={297} bg={t.card} style={{ border: `1.5px solid ${t.line}` }} />
      <Lines x={284} cy={289} align="center" w={279} size={16.5} color={t.ink} lines={[chapter.kicker]} />
      <Lines x={284} cy={396} align="center" w={279} size={128} className={`${t.latin} font-semibold`} color={t.sageText} lines={[chapter.n]} />
      <Lines x={490} cy={274} size={43} className="font-medium tracking-[-0.02em]" color={t.ink} lines={[chapter.title]} />
      <Box x={461} y={317} w={672} h={2} bg="#ccc" />
      {chapter.items.map((s, i) => {
        const cy = [380, 436, 492][i]
        return (
          <div key={i}>
            <Lines x={471} cy={cy} size={15} color="#777" lines={['\\']} />
            <Lines x={496} cy={cy} size={17.5} color={t.text} lines={[s]} />
            <Box x={466} y={cy + 27} w={669} h={1.5} bg="#bbb" />
          </div>
        )
      })}
    </CalendarSlide>
  )
}

function Flow() {
  return (
    <CalendarSlide>
      <TitleBar n={flow.n} title={flow.title} />
      <Box x={112} y={226} w={1054} h={3} bg="#dde5e5" />
      {flow.steps.map((s, i) => {
        const x = 115 + i * 267, cx = x + 124
        let y = 388
        return (
          <div key={i}>
            <Abs x={cx - 7.5} y={220} w={15} h={15} className="rounded-full" style={{ background: t.sageText }} />
            <Card x={x} y={250} w={248} h={270} />
            <Lines x={cx} cy={287} align="center" w={248} size={16.5} className={t.latin} color={t.sageText} lines={[s.kicker]} />
            <Box x={x + 21} y={314} w={207} h={44} bg="#fff" />
            <Lines x={cx} cy={336} align="center" w={207} size={18} className="font-semibold" color={t.ink} lines={[s.title]} />
            {s.bullets.map((b, j) => {
              const top = y
              y += b.length * 22.5
              return (
                <div key={j}>
                  <Abs x={x + 27} y={top - 2.5} w={5} h={5} className="rounded-full" style={{ background: t.ink }} />
                  <Lines x={x + 42} cy={top} lh={22.5} size={13.5} color={t.text} lines={b} />
                </div>
              )
            })}
          </div>
        )
      })}
      <Ticks pts={[[112, 505], [379, 505], [646, 505], [913, 505]]} />
      <Box x={98} y={557} w={1085} h={63} bg="#eef1f1" style={{ border: `1.5px solid ${t.line}`, borderBottom: '1.5px solid #888' }} />
      <Lines x={640} cy={589} align="center" size={22} className="font-medium tracking-[-0.02em]" color={t.ink} lines={[flow.note]} />
    </CalendarSlide>
  )
}

function Photos() {
  return (
    <CalendarSlide>
      <TitleBar n={photos.n} title={photos.title} />
      {photos.items.map((p, i) => {
        const x = 96 + i * 276, cx = x + 129
        return (
          <div key={p.n}>
            <Card x={x} y={214} w={259} h={408} />
            <Photo x={x + 44} y={248} w={170} h={196} />
            <Circle cx={cx} cy={457} r={32}><span className={t.latin} style={{ fontSize: 26, color: t.sageText }}>{p.n}</span></Circle>
            <Lines x={cx} cy={514} align="center" w={259} size={21} className={t.latin} color={t.ink} lines={[p.name]} />
            <Lines x={cx} cy={553} lh={22.5} align="center" w={259} size={14} color={t.text} lines={p.desc} />
          </div>
        )
      })}
      <Ticks pts={[[300, 240], [576, 240], [852, 240], [1128, 240], [132, 430], [408, 430], [684, 430], [960, 430]]} />
    </CalendarSlide>
  )
}

function ListPage() {
  return (
    <CalendarSlide>
      <TitleBar n={list.n} title={list.title} />
      {list.rows.map((r, i) => {
        const y = 220 + i * 81.6
        return (
          <div key={r.n}>
            <Box x={103} y={y} w={736} h={63} className="rounded-t-[4px]" style={{ border: `1.5px solid ${t.line}` }} />
            <Lines x={147} cy={y + 32} size={26} className={t.latin} color={t.sageText} lines={[r.n]} />
            <Lines x={495} cy={y + 32} align="center" w={600} size={20} color={t.ink} lines={[r.text]} />
          </div>
        )
      })}
      <Box x={860} y={220} w={317} h={114} bg="#f2f2f4" className="rounded-lg" />
      <Abs x={889} y={251}><MessageCircleQuestion size={48} strokeWidth={1.3} color="#444" /></Abs>
      <Lines x={950} cy={253} lh={22.5} size={13.5} color={t.text} lines={list.aside} />
    </CalendarSlide>
  )
}

function Compare() {
  return (
    <CalendarSlide>
      <TitleBar n={compare.n} title={compare.title} />
      {compare.cols.map((c, i) => {
        const x = 108 + i * 559
        return (
          <div key={c.head}>
            <Box x={x} y={222} w={505} h={410} bg={i ? t.mintCard : t.card} className="rounded-t-md" style={{ border: `1.5px solid ${t.line}`, borderBottom: 0 }} />
            <Box x={x + 5} y={631} w={488} h={1.5} bg={t.line} />
            <Lines x={x + 252} cy={291} align="center" w={505} size={29} className={t.latin} color={t.ink} lines={[c.head]} />
            {c.items.map((s, j) => (
              <div key={j}>
                <Lines x={x + 252} cy={373 + j * 59.3} align="center" w={505} size={16.5} color={t.text} lines={[s]} />
                <Box x={x + 33} y={406 + j * 58.2} w={439} h={2} bg="#cfd6d6" />
              </div>
            ))}
          </div>
        )
      })}
      <Circle cx={640} cy={427} r={42} bg="#eaf0f0"><ChevronRight size={40} strokeWidth={1.2} color="#777" /></Circle>
    </CalendarSlide>
  )
}

const deck: DeckDefinition = { id: '12', title: '민트 깔끔 비즈니스 설명', slides: [Cover, Contents, Keywords, PhotoText, FourText, Chapter, Flow, Photos, ListPage, Compare] }
export default deck
