import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { quote } from '../d17/data'
import { Glow, Logo, Mono } from '../d17/parts'

const Quote = () => (
  <Slide className="font-montalt">
    <Glow x={-90} y={170} w={340} h={300} c="#ece9f8" />
    <Logo x={632} y={228} size={36} color="#050507" />
    <Abs x={632} y={310} w={640} className="text-[40px] font-medium leading-[44px] tracking-[-0.02em] text-[#9a9a9f]">
      {quote.lead}<span className="text-[#050507]">{quote.strong}</span>{quote.rest}
    </Abs>
    <ImagePlaceholder className="absolute" tone="#2a2a30" style={{ left: 22, top: 515, width: 105, height: 105 }} label="portrait" />
    <Abs x={142} y={560} className="text-[13px] font-semibold">{quote.author.name}</Abs>
    <Mono x={142} y={588} className="text-[11px] leading-[17px] text-[#666]">{quote.author.role.map((r) => <div key={r}>{r}</div>)}</Mono>
  </Slide>
)

const deck: DeckDefinition = { id: '18', title: 'Elabor.rate Quote', slides: [Quote] }
export default deck
