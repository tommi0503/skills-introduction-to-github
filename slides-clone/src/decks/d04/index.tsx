import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { StepColumn } from './components'
import { legend, steps, tag } from './data'
import { theme } from './theme'

const xs = [38, 335, 632, 930]
function HowItWorks() {
  return (
    <Slide background={theme.bg}>
      <Abs x={38} y={40} w={162} h={26} className="flex items-center justify-center rounded-md font-inter text-[11px] font-semibold" style={{ background: theme.pill, color: theme.pillInk }}>{tag}</Abs>
      <Abs x={38} y={78} className="font-inter text-[34px] font-semibold leading-[46px] whitespace-nowrap">Low commitment, easy-to-use core feature to engage<br />users repeatedly <span className="text-[14px] font-normal">(think Wordle, but for language practice)</span></Abs>
      <Abs x={50} y={266} w={1180} h={2} style={{ background: '#d4dbe8' }} />
      {steps.map((s, i) => <StepColumn key={s.label} s={s} x={xs[i]} />)}
      <Abs x={0} y={602} w={1220} h={54} className="rounded-r-xl bg-white shadow-[0_4px_20px_rgba(60,90,160,0.08)]" />
      {legend.map((l, i) => (
        <Abs key={l.text} x={[588, 805, 1000][i]} y={614} className="flex items-center gap-3 font-inter text-[12px] italic">
          <div className="h-[22px] w-[22px] rounded-md" style={{ background: l.color }} />{l.text}
        </Abs>
      ))}
      <ImagePlaceholder className="absolute rounded-[40px]" style={{ left: 200, top: 492, width: 340, height: 300 }} />
      <Abs x={38} y={686} className="font-inter text-[16px] font-black">CONNVO</Abs>
      <Abs x={1210} y={688} className="font-inter text-[12px] font-semibold">6</Abs>
    </Slide>
  )
}
const deck: DeckDefinition = { id: '04', title: 'How it works', slides: [HowItWorks] }
export default deck
