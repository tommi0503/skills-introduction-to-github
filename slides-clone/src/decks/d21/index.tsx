import { ArrowUp, BarChart3, Brain } from 'lucide-react'
import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { Heading, VeroLogo, vero } from '../d20/parts'
import { results as R } from './data'

export const Results = () => (
  <Slide background="#1c1c1c" className="font-manrope">
    <Abs x={0} y={0} w={526} h={720} style={{ background: 'linear-gradient(180deg,#242424,#141414)' }} />
    <VeroLogo x={50} y={60} size={22} />
    <Abs x={288} y={58} className="text-[12px] text-white/50">{R.section}</Abs>
    <Heading x={51} y={140} size={52} lh={65}>{R.title.map((t) => <div key={t}>{t}</div>)}</Heading>
    <Abs x={51} y={360} className="text-[28px] font-medium leading-[36px] text-white">{R.sub.map((t) => <div key={t}>{t}</div>)}</Abs>
    <Abs x={51} y={645} w={330} className="text-[11px] leading-[15px] text-white/40">{R.note}</Abs>
    <Abs x={526} y={0} w={754} h={292} style={{ background: vero.panel }} />
    <ImagePlaceholder className="absolute" tone="#5b8fd0" style={{ left: 526, top: 292, width: 754, height: 428 }} label="gradient" />
    {R.stats.map((s, i) => {
      const y = i ? 292 : 0
      const Icon = i ? Brain : BarChart3
      return (
        <div key={s.value}>
          <Icon size={38} strokeWidth={1.6} className="absolute text-white" style={{ left: 576, top: y + (i ? 50 : 46) }} />
          <Abs x={1004} y={y + (i ? 36 : 42)} w={250} className="text-[18px] font-medium leading-[24px] text-white">{s.title.map((t) => <div key={t}>{t}</div>)}</Abs>
          <Abs x={1004} y={y + (i ? 96 : 102)} w={260} className="text-[11px] leading-[14px] text-white/60">{s.text.map((t) => <div key={t}>{t}</div>)}</Abs>
          <Abs x={576} y={y + (i ? 190 : 138)} className="flex items-center text-white" style={{ fontSize: i ? 164 : 106 }}>
            <ArrowUp size={i ? 108 : 72} strokeWidth={3} />
            <span className="font-medium leading-none tracking-[-0.03em]" style={{ lineHeight: i ? "180px" : "120px" }}>{s.value}</span>
          </Abs>
        </div>
      )
    })}
  </Slide>
)

const deck: DeckDefinition = { id: '21', title: 'Vero Control Results', slides: [Results] }
export default deck
