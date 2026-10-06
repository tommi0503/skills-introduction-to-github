import { Check, X } from 'lucide-react'
import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { differentiators as D, problem as P } from './data'
import { GradText, SynthHeader, synth } from './shared'

function List({ items, color, x, y, w }: { items: string[]; color: string; x: number; y: number; w: number }) {
  return (
    <Abs x={x} y={y} w={w} className="flex flex-col font-grotesk text-[17px] leading-[1.15] uppercase" style={{ color, gap: 17 }}>
      {items.map((t) => <div key={t}>{t}</div>)}
    </Abs>
  )
}

const Differentiators = () => (
  <Slide background={synth.paper} className="font-grotesk">
    <SynthHeader section={D.section} />
    <Abs x={56} y={116} className="text-[64px] leading-[56px] text-[#0a0a0a]">
      <div>{D.title[0]}<GradText>{D.title[1]}</GradText></div>
      <div>{D.title[2]}</div>
    </Abs>
    <Abs x={619} y={176} w={253} h={133} className="rounded-[22px] border border-[#dfe5ec] bg-white">
      <ImagePlaceholder className="absolute left-[78px] top-[48px] h-[34px] w-[64px]" />
    </Abs>
    <Abs x={227} y={312} w={392} h={408} className="rounded-t-[22px] bg-white">
      <Check size={38} color="#1fd3a4" strokeWidth={1.5} className="absolute left-[318px] top-[34px]" />
    </Abs>
    <List items={D.ours} color={synth.ink} x={253} y={512} w={190} />
    <Abs x={648} y={376} w={392} h={344} className="rounded-t-[22px]" style={{ background: synth.gradV }}>
      <X size={38} color="#fff" strokeWidth={1.5} className="absolute left-[318px] top-[22px]" />
    </Abs>
    <List items={D.theirs} color="#fff" x={675} y={530} w={220} />
  </Slide>
)

const Problem = () => (
  <Slide background={synth.paper} className="font-grotesk">
    <SynthHeader section={P.section} />
    <Abs x={51} y={78} className="text-[56px] leading-[53px] text-[#0a0a0a]">
      <div>{P.title[0]}<GradText>{P.title[1]}</GradText>{P.title[2]}</div>
      <div>{P.title[3]}</div>
    </Abs>
    <Abs x={51} y={222} w={300} className="text-[11px] leading-[14px] text-[#222]">{P.body}</Abs>
    <Abs x={318} y={268} className="text-[400px] font-medium leading-[400px] tracking-[-0.03em] text-[#0a0a0a]">{P.big}</Abs>
    <Abs x={904} y={420} w={260} className="text-[20px] leading-[26px]">{P.caption}</Abs>
    <ImagePlaceholder className="absolute" style={{ left: 856, top: 517, width: 125, height: 140 }} />
  </Slide>
)

const deck: DeckDefinition = { id: '12', title: 'SYNTH Differentiators', slides: [Differentiators, Problem] }
export default deck
