import type { CSSProperties, ReactNode } from 'react'
import { ArrowBigLeft, ArrowBigRight, Tent } from 'lucide-react'
import { Abs, Slide, cn } from '../../ui'
import { t } from './theme'

type Align = 'left' | 'center' | 'right'

/** Single text line: `x` is left edge / centre / right edge per `align`, `cy` the vertical centre.
 *  `d` switches to the thin display face; its value is the colour behind the text. */
export function Txt({ x, cy, size, align = 'left', w = 1100, className, style, children, d }: {
  x: number; cy: number; size: number; align?: Align; w?: number; className?: string; style?: CSSProperties; children: ReactNode; d?: string | true
}) {
  if (d) {
    const fs = size * t.dScale
    style = { letterSpacing: t.dTrack, WebkitTextStroke: `${fs * t.dThin}px ${d === true ? '#fff' : d}`, ...style, fontSize: fs }
    className = cn(t.head, className)
  }
  const left = align === 'left' ? x : align === 'center' ? x - w / 2 : x - w
  const justify = align === 'left' ? 'justify-start' : align === 'center' ? 'justify-center' : 'justify-end'
  return (
    <Abs x={left} y={cy - size * 0.7} w={w} h={size * 1.4} className={cn('flex items-center whitespace-nowrap leading-none', justify, className)} style={{ fontSize: size, ...style }}>
      <span>{children}</span>
    </Abs>
  )
}

export function Lines({ lines, cy0, gap, ...rest }: Omit<Parameters<typeof Txt>[0], 'cy' | 'children'> & { lines: readonly string[]; cy0: number; gap: number }) {
  return <>{lines.map((l, i) => <Txt key={i} {...rest} cy={cy0 + i * gap}>{l}</Txt>)}</>
}

/** Body copy in pretendard, brown. */
export const B = (p: Omit<Parameters<typeof Txt>[0], 'd'>) => <Txt {...p} className={cn(t.body, 'font-medium', p.className)} />
export const BL = (p: Omit<Parameters<typeof Lines>[0], 'd'>) => <Lines {...p} className={cn(t.body, 'font-medium', p.className)} />

export const Box = ({ x, y, w, h, r = 0, fill = '#fff', border = true, style, className }: { x: number; y: number; w: number; h: number; r?: number; fill?: string; border?: boolean; style?: CSSProperties; className?: string }) => (
  <Abs x={x} y={y} w={w} h={h} className={className} style={{ background: fill, borderRadius: r, border: border ? `1.5px solid ${t.brown}` : undefined, ...style }} />
)

/** Tag pill with dots at both ends. */
export function Tag({ x = 470, y = 33, w = 340, h = 44, fill = t.green, size = 24, children }: { x?: number; y?: number; w?: number; h?: number; fill?: string; size?: number; children: ReactNode }) {
  return (
    <>
      <Box x={x} y={y} w={w} h={h} r={h / 2} fill={fill} />
      {[x + 20, x + w - 20].map((cx) => <Abs key={cx} x={cx - 3} y={y + h / 2 - 3} w={6} h={6} className="rounded-full" style={{ background: t.brown }} />)}
      <Txt x={x + w / 2} cy={y + h / 2} size={size} align="center" w={w - 50} d={fill} style={{ color: t.brown }}>{children}</Txt>
    </>
  )
}

export function Logo({ x, cy, size = 20 }: { x: number; cy: number; size?: number }) {
  return (
    <Abs x={x} y={cy - size} h={size * 2} className={cn(t.body, 'flex items-center gap-[6px] whitespace-nowrap font-semibold leading-none')} style={{ fontSize: size, color: t.brown }}>
      <Tent size={size * 1.7} strokeWidth={1.4} />MIRICAMP
    </Abs>
  )
}

/** Standard content slide: coloured backdrop, white rounded frame, tag pill, title, footer. */
export function FrameSlide({ bg = t.cream, tag, title, frameX = t.frame.x, children }: { bg?: string; tag: string; title: string; frameX?: number; children: ReactNode }) {
  const f = t.frame
  const tagFill = bg === t.cream ? t.green : t.cream
  return (
    <Slide background={bg} style={{ color: t.brown }}>
      <Box x={frameX} y={f.y} w={f.w} h={f.h} r={f.r} style={{ borderWidth: 2 }} />
      <Tag fill={tagFill}>{tag}</Tag>
      <Txt x={640} cy={163} size={64} align="center" d style={{ color: t.brown }}>{title}</Txt>
      <Abs x={62} y={664}><ArrowBigLeft size={44} strokeWidth={1.3} color={t.brown} /></Abs>
      <Abs x={1172} y={664}><ArrowBigRight size={44} strokeWidth={1.3} color={t.brown} /></Abs>
      <Logo x={567} cy={688} size={19} />
      {children}
    </Slide>
  )
}
