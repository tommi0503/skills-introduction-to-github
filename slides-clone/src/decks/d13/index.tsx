import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { GradText, SynthHeader } from '../d12/shared'
import { roadmap as R } from './data'

// The title runs across both slides; slide 2 continues it after the 1280px slide plus the
// ~66px gap that separates the two slides in the reference (letters falling in the gap are hidden).
const OFFSET = 1280 + 66

function Title({ dx, dark }: { dx: number; dark?: boolean }) {
  return (
    <>
      <Abs x={619 + dx} y={47} className="whitespace-nowrap font-grotesk text-[155px] leading-[219px]" style={{ color: dark ? '#fff' : '#000' }}>
        {R.titleLine1[0]}<GradText>{R.titleLine1[1]}</GradText>{R.titleLine1[2]}
      </Abs>
      <Abs x={357 + dx} y={266} className="whitespace-nowrap font-grotesk text-[155px] leading-[219px]" style={{ color: dark ? '#fff' : '#000' }}>
        {R.titleLine2}
      </Abs>
    </>
  )
}

function Milestone({ i, x, y, dark, last }: { i: number; x: number; y: number; dark?: boolean; last?: boolean }) {
  const m = R.years[i]
  const c = dark ? '#fff' : '#000'
  return (
    <>
      <Abs x={x} y={y} className="font-grotesk text-[42px] leading-none" style={{ color: c }}>{m.year}</Abs>
      <Abs x={x + 80} y={y + 22} w={Math.max(120, 1280 - x - 80)} className="h-px" style={{ background: 'linear-gradient(90deg,#1fd3a4,transparent)', display: last ? 'none' : undefined }} />
      <Abs x={x + 75} y={y + 12} w={110} className="h-px" style={{ background: '#1fd3a4', display: last ? 'block' : 'none' }} />
      <Abs x={x} y={y + 80} className="font-grotesk text-[14px] leading-[17px]" style={{ color: c }}>
        {m.label.map((l) => <div key={l}>{l}</div>)}
      </Abs>
    </>
  )
}

const Intro = () => (
  <Slide background="#000">
    <SynthHeader section={R.section} dark />
    <Title dx={0} dark />
    <Abs x={53} y={358} className="font-grotesk text-[15px] leading-[19px] text-white">{R.intro.map((l) => <div key={l}>{l}</div>)}</Abs>
    <Abs x={349} y={603} w={240} className="font-grotesk text-[11px] leading-[14px] text-white">{R.body}</Abs>
    <Milestone i={0} x={944} y={518} dark />
  </Slide>
)

const Years = () => (
  <Slide>
    <SynthHeader section={R.section} />
    <Title dx={-OFFSET} />
    <ImagePlaceholder className="absolute rounded-bl-[24px]" style={{ left: 632, top: 0, width: 648, height: 336 }} />
    <Milestone i={1} x={51} y={518} />
    <Milestone i={2} x={496} y={518} />
    <Milestone i={3} x={941} y={518} last />
  </Slide>
)

const deck: DeckDefinition = { id: '13', title: 'SYNTH Roadmap', slides: [Intro, Years] }
export default deck
