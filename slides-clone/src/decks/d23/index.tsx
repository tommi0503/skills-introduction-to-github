import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { theme } from './theme'
import { cover } from './data'
import { Brand, Pill } from './components'

function Cover() {
  return (
    <Slide background={theme.bg} className="font-manrope">
      <Abs x={0} y={0} w={530} h={720} style={{ background: theme.panel }} />
      <ImagePlaceholder className="absolute" style={{ left: 530, top: 0, width: 750, height: 720 }} tone={theme.photo} />
      <Abs x={50} y={52}><Brand name={cover.brand} /></Abs>
      <Abs x={278} y={50} className="text-[13px]" style={{ color: theme.muted }}>{cover.nav}</Abs>
      <Abs x={1192} y={50} className="text-[13px]" style={{ color: theme.muted }}>{cover.page}</Abs>
      <Abs x={50} y={125} className="text-[60px] font-semibold leading-[72px] text-white">
        {cover.title.map((l) => <div key={l}>{l}</div>)}
      </Abs>
      <Abs x={50} y={620} className="text-[20px] leading-[28px] text-white">
        {cover.contact.map((l) => <div key={l}>{l}</div>)}
      </Abs>
      {cover.pills.map((p) => <Pill key={p.label} {...p} />)}
    </Slide>
  )
}

const deck: DeckDefinition = { id: '23', title: 'Vero AI', slides: [Cover] }
export default deck
