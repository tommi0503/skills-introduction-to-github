import { Abs, Slide, type DeckDefinition } from '../../ui'
import { Heading, Photo, VeroHeader } from '../d20/parts'
import { team as T } from './data'

export const Team = () => (
  <Slide background="linear-gradient(180deg,#1f1f1f,#0b0b0b)" className="font-manrope">
    <VeroHeader section={T.section} page="Page 01" />
    <Heading x={63} y={132} size={56} lh={69}>{T.title.map((t) => <div key={t}>{t}</div>)}</Heading>
    <Abs x={656} y={132} w={420} className="text-[26px] leading-[31px] text-white">{T.intro}</Abs>
    {T.people.map((p, i) => (
      <div key={p.name}>
        <Photo x={181 + i * 237} y={345} w={217} h={244} />
        <Abs x={181 + i * 237} y={607} className="text-[20px] text-white">{p.name}</Abs>
        <Abs x={181 + i * 237} y={638} className="text-[11px] text-white/50">{p.role}</Abs>
      </div>
    ))}
  </Slide>
)

const deck: DeckDefinition = { id: '22', title: 'Vero Team', slides: [Team] }
export default deck
