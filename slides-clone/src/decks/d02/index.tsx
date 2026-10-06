import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { FeatureColumn, Pill } from './components'
import { features, tag, title } from './data'
import { theme } from './theme'

function Features() {
  return (
    <Slide background={theme.bg}>
      <Pill text={tag} x={51} y={34} w={120} />
      <Abs x={51} y={75} className="font-inter text-[34px] font-semibold leading-[46px] whitespace-nowrap">{title.map((t) => <div key={t}>{t}</div>)}</Abs>
      <Abs x={30} y={222} w={1250} h={96} className="rounded-l-2xl bg-white" />
      {features.map((f, i) => <FeatureColumn key={f.title} f={f} x={[58, 340, 622][i]} last={i === 2} />)}
      <Abs x={51} y={672} className="font-inter text-[17px] font-black tracking-wide">CONNVO</Abs>
      <Abs x={1214} y={676} className="font-inter text-[12px] font-semibold">9</Abs>
      <ImagePlaceholder className="absolute rounded-[36px]" style={{ left: 980, top: 28, width: 215, height: 440 }} />
      <ImagePlaceholder className="absolute rounded-[36px]" style={{ left: 840, top: 485, width: 270, height: 300 }} />
    </Slide>
  )
}
const deck: DeckDefinition = { id: '02', title: 'Key features', slides: [Features] }
export default deck
