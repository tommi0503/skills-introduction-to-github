import { Plus } from 'lucide-react'
import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { GradText, SynthHeader } from '../d12/shared'
import { features as F, forecast as G } from './data'

const Forecast = () => (
  <Slide background="linear-gradient(180deg,#14dfa8 0%,#4fc0c8 50%,#7b9cf0 100%)" className="font-grotesk">
    <SynthHeader section={G.section} dark />
    <Abs x={53} y={82} className="text-[46px] leading-[53px] text-white">{G.title.map((t) => <div key={t}>{t}</div>)}</Abs>
    {G.cols.map((c, i) => {
      const x = 67 + i * 293
      const size = [72, 64, 58, 52][i]
      return (
        <div key={c.year}>
          {i > 0 && <Abs x={x - 12} y={240} w={1} h={480} className="bg-white/50" />}
          <Abs x={x} y={256} w={235} className="text-[11px] leading-[14px] text-white">{c.text}</Abs>
          <Abs x={x + 13} y={667 - c.h} w={248} h={c.h} className="rounded-[14px] bg-white">
            <div className="absolute left-4 top-4 text-[11px]">{c.year}</div>
            <div className="absolute right-4 top-3 text-[28px] leading-none">{c.pct}</div>
            <div className="absolute bottom-3 left-4 leading-none" style={{ fontSize: size }}><GradText>{c.amount}</GradText></div>
          </Abs>
        </div>
      )
    })}
  </Slide>
)

const Features = () => (
  <Slide background="radial-gradient(ellipse at 45% 60%,#0f2a26 0%,#000 65%)" className="font-grotesk">
    <SynthHeader section={F.section} dark />
    <Abs x={51} y={78} className="text-[46px] leading-[53px] text-white">
      <div>{F.title[0]}</div><div><GradText>{F.title[1]}</GradText></div>
    </Abs>
    {F.items.map((it, i) => {
      const x = i % 2 ? 691 : 51
      const y = i < 2 ? 261 : 518
      const w = i % 2 ? 480 : 480
      return (
        <div key={it.n}>
          <Abs x={x} y={y} className="text-[135px] font-medium leading-[135px] tracking-[-0.03em]">
            {i === 0 ? <GradText>{it.n}</GradText> : <span className="text-white">{it.n}</span>}
          </Abs>
          {it.icon === 'plus'
            ? <Plus size={22} color="#1fd3a4" className="absolute" style={{ left: x + (i === 2 ? 188 : 175), top: y + 118 }} />
            : <ImagePlaceholder className="absolute" tone="#1d2b2a" style={{ left: x + (i === 0 ? 188 : 175), top: y + 105, width: 28, height: 28 }} />}
          <Abs x={x + 255} y={y + 22} w={w - 255} className="text-[16px] leading-[16px] text-white">{it.title.map((t) => <div key={t}>{t}</div>)}</Abs>
          <Abs x={x + 255} y={y + 70} w={220} className="text-[11px] leading-[14px] text-white">{it.body}</Abs>
        </div>
      )
    })}
  </Slide>
)

const deck: DeckDefinition = { id: '14', title: 'SYNTH Forecast & Features', slides: [Forecast, Features] }
export default deck
