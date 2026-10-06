import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { theme } from './theme'
import { cover, systems, analysis, layers } from './data'
import { BarRow, Layer, SystemCard } from './components'

function Cover() {
  return (
    <Slide background="#fff" className="font-geist">
      <ImagePlaceholder tone={theme.photo} className="absolute" style={{ left: 0, top: 0, width: 1040, height: 720 }} />
      <Abs x={31} y={38} className="text-[52px] font-medium leading-none text-white">{cover.brand}</Abs>
      <Abs x={31} y={425} className="text-[58px] font-light leading-[63px] text-white">{cover.lines.map((l) => <div key={l}>{l}</div>)}</Abs>
      <Abs x={1185} y={648} className="text-[14px]">{cover.year}</Abs>
    </Slide>
  )
}

function Systems() {
  return (
    <Slide background={theme.grey} className="font-geist">
      <Abs x={35} y={50} className="text-[69px] font-light leading-[62px]">{systems.title.map((l) => <div key={l}>{l}</div>)}</Abs>
      {systems.cards.map((c, i) => <SystemCard key={c} label={c} x={35 + i * 206} />)}
    </Slide>
  )
}

function Analysis() {
  return (
    <Slide background="#fff" className="font-geist">
      <Abs x={0} y={0} w={872} h={720} style={{ background: theme.mid }} />
      {analysis.rows.map(([v, w], i) => <BarRow key={v} value={v} w={w} y={33 + i * 83} />)}
      <Abs x={1053} y={355} w={190} className="text-[12px] leading-[15px]">
        <div className="mb-3 text-[13px] font-semibold">{analysis.heading}</div>
        {analysis.paras.map((p) => <p key={p} className="mb-3" style={{ color: '#444' }}>{p}</p>)}
      </Abs>
    </Slide>
  )
}

function Layers() {
  return (
    <Slide background="#fff" className="font-geist">
      <ImagePlaceholder className="absolute" style={{ left: 455, top: 77, width: 700, height: 565 }} />
      {layers.map((l, i) => <Layer key={l.n} {...l} y={218 + i * 136} />)}
    </Slide>
  )
}

const deck: DeckDefinition = { id: '26', title: 'Architekt', slides: [Cover, Systems, Analysis, Layers] }
export default deck
