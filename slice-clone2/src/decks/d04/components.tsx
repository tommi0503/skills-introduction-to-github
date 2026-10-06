import type { ReactNode } from 'react'
import { X } from 'lucide-react'
import { Abs, ImagePlaceholder, Slide } from '../../ui'
import { Lines } from '../../ui'
import type { Deco } from './data'
import { t } from './theme'

/** White page between torn-paper strips (texture → placeholder bands) + decorations. */
export function PaperSlide({ deco = [], children }: { deco?: Deco[]; children: ReactNode }) {
  return (
    <Slide background="#fff" className={t.sans} style={{ color: t.text, ['--ly' as string]: '0.07em' }}>
      <Abs x={0} y={0} w={1280} h={92}><ImagePlaceholder label="torn paper strip" className="h-full w-full" tone="#f1f1f3" /></Abs>
      <Abs x={0} y={650} w={1280} h={70}><ImagePlaceholder label="torn paper strip" className="h-full w-full" tone="#f1f1f3" /></Abs>
      {deco.map((d, i) => <DecoItem key={i} d={d} />)}
      {children}
    </Slide>
  )
}

function DecoItem({ d }: { d: Deco }) {
  switch (d.k) {
    case 'dot':
      return <Abs x={d.x} y={d.y} w={d.d} h={d.d} className="rounded-full" style={{ background: d.c }} />
    case 'ring':
      return <Abs x={d.x} y={d.y} w={d.d} h={d.d} className="rounded-full" style={{ border: `${d.b}px solid ${d.c}` }} />
    case 'x':
      return <Abs x={d.x} y={d.y}><X size={d.s} color={d.c} strokeWidth={4} /></Abs>
    case 'shape':
      return <Abs x={d.x} y={d.y} w={d.w} h={d.h}><ImagePlaceholder label="decorative shape" className="h-full w-full" style={{ borderRadius: d.r }} /></Abs>
  }
}

/** Big centred heavy title. */
export const Title = ({ text, cy, size = 66 }: { text: string; cy: number; size?: number }) => (
  <Lines x={640} cy={cy} align="center" size={size} className={t.head} color={t.ink} lines={[text]} />
)

/** Mint wavy rule. */
export function Wave({ x, y, w, color = t.mint }: { x: number; y: number; w: number; color?: string }) {
  const path = 'M0 4 Q4 0 8 4 T16 4'
  return (
    <Abs x={x} y={y - 4} w={w} h={8}>
      <svg width={w} height={8}>
        <defs>
          <pattern id={`wv${x}${y}`} width={16} height={8} patternUnits="userSpaceOnUse"><path d={path} fill="none" stroke={color} strokeWidth={2} /></pattern>
        </defs>
        <rect width={w} height={8} fill={`url(#wv${x}${y})`} />
      </svg>
    </Abs>
  )
}

/** Rounded grey pill with a white circle holding a coloured play triangle. */
export function PlayPill({ x, y, w, h, color, text, size }: { x: number; y: number; w: number; h: number; color: string; text: string; size: number }) {
  const r = h * 0.43
  return (
    <>
      <Abs x={x} y={y} w={w} h={h} className="rounded-full" style={{ background: t.card }} />
      <Abs x={x + h / 2 - r + 6} y={y + h / 2 - r} w={r * 2} h={r * 2} className="rounded-full bg-white" />
      <Abs x={x + h / 2 + 2} y={y + h / 2 - r * 0.28} w={0} h={0} style={{ borderLeft: `${r * 0.42}px solid ${color}`, borderTop: `${r * 0.28}px solid transparent`, borderBottom: `${r * 0.28}px solid transparent` }} />
      <Lines x={x + h + 18} cy={y + h / 2} size={size} color={t.text} lines={[text]} />
    </>
  )
}

/** Small white circle with a down-pointing triangle (card connector). */
export function DownTab({ cx, cy, r, color }: { cx: number; cy: number; r: number; color: string }) {
  return (
    <>
      {r > 0 && <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className="rounded-full bg-white" />}
      <Abs x={cx - 8} y={cy - 4} w={0} h={0} style={{ borderTop: `9px solid ${color}`, borderLeft: '8px solid transparent', borderRight: '8px solid transparent' }} />
    </>
  )
}
