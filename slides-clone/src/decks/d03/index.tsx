import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { Bullet, PerkCard } from './components'
import { bullets, lead, perks, tag, title } from './data'
import { theme } from './theme'

function Usp() {
  return (
    <Slide background={theme.bg}>
      <Abs x={45} y={46} w={222} h={26} className="flex items-center justify-center rounded-md font-inter text-[11px] font-semibold" style={{ background: theme.pill, color: theme.pillInk }}>{tag}</Abs>
      <Abs x={45} y={86} className="font-inter text-[33px] font-semibold leading-[44px] whitespace-nowrap">{title.map((t) => <div key={t}>{t}</div>)}</Abs>
      <Abs x={45} y={288} className="font-inter text-[22px] font-semibold leading-[25px]">{lead.map((t) => <div key={t}>{t}</div>)}</Abs>
      {[404, 468, 533].map((y, i) => <Bullet key={i} y={y} b={bullets[i]} last={i === 2} />)}
      <ImagePlaceholder className="absolute rounded-[44px]" style={{ left: 549, top: 208, width: 301, height: 560 }} />
      {perks.map((p) => <PerkCard key={p.label} p={p} />)}
      <Abs x={45} y={690} className="font-inter text-[16px] font-black">CONNVO</Abs>
      <Abs x={1214} y={692} className="font-inter text-[12px] font-semibold">5</Abs>
    </Slide>
  )
}
const deck: DeckDefinition = { id: '03', title: 'Unique selling proposition', slides: [Usp] }
export default deck
