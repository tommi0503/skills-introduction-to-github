import { ArrowRight } from 'lucide-react'
import { Abs } from '../../ui'
import { theme } from './theme'
import type { Feature } from './data'

export const Pill = ({ text, x, y, w }: { text: string; x: number; y: number; w: number }) => (
  <Abs x={x} y={y} w={w} h={26} className="flex items-center justify-center rounded-md font-inter text-[11px] font-semibold tracking-wide" style={{ background: theme.pill, color: theme.pillInk }}>{text}</Abs>
)
export function FeatureColumn({ f, x, last }: { f: Feature; x: number; last: boolean }) {
  return (
    <>
      <Abs x={x} y={252} w={62} h={62} className="rounded-xl" style={{ background: f.color }} />
      {!last && <ArrowRight className="absolute" style={{ left: x + 222, top: 274 }} size={22} color={f.color} />}
      <Abs x={x} y={356} w={200} className="font-inter text-[22px] font-bold leading-[28px]">{f.title.split(' ').map((w, i) => <div key={i}>{w}</div>)}</Abs>
      <Abs x={x} y={435} w={235} className="font-inter text-[14px] leading-[24px]" style={{ color: theme.muted }}>
        {f.bullets.map((b, i) => <div key={i} className="mb-3 flex gap-3"><span>•</span><span>{b}</span></div>)}
      </Abs>
    </>
  )
}
