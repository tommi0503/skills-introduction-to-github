import type { CSSProperties, ReactNode } from 'react'
import { Tent } from 'lucide-react'
import { Abs, ImagePlaceholder, Slide, cn } from '../../ui'
import { t } from './theme'

type Align = 'left' | 'center' | 'right'
export interface TxtProps { x: number; cy: number; size: number; align?: Align; w?: number; className?: string; style?: CSSProperties; children: ReactNode }

/** `==orange==` and `**bold**` inline markup. */
export function Rich({ text }: { text: string }) {
  return (
    <>
      {text.split(/(==.*?==|\*\*.*?\*\*)/).map((s, i) =>
        s.startsWith('==') ? <span key={i} style={{ color: t.orange }}>{s.slice(2, -2)}</span>
          : s.startsWith('**') ? <b key={i} className="font-bold">{s.slice(2, -2)}</b> : s)}
    </>
  )
}

/** Single text line: `x` is left edge / centre / right edge per `align`, `cy` the vertical centre. */
export function Txt({ x, cy, size, align = 'left', w = 1100, className, style, children }: TxtProps) {
  const left = align === 'left' ? x : align === 'center' ? x - w / 2 : x - w
  const justify = align === 'left' ? 'justify-start' : align === 'center' ? 'justify-center' : 'justify-end'
  return (
    <Abs x={left} y={cy - size * 0.7} w={w} h={size * 1.4} className={cn('flex items-center whitespace-nowrap leading-none', justify, t.body)} style={{ fontSize: size, ...style }}>
      <span className={className}>{typeof children === 'string' ? <Rich text={children} /> : children}</span>
    </Abs>
  )
}

export function Lines({ lines, cy0, gap, ...rest }: Omit<TxtProps, 'cy' | 'children'> & { lines: readonly string[]; cy0: number; gap: number }) {
  return <>{lines.map((l, i) => <Txt key={i} {...rest} cy={cy0 + i * gap}>{l}</Txt>)}</>
}

export const Ph = ({ x, y, w, h, label, tone, className }: { x: number; y: number; w: number; h: number; label: string; tone?: string; className?: string }) => (
  <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label={label} tone={tone} className={cn('h-full w-full', className)} /></Abs>
)
export const Box = ({ x, y, w, h, fill, r = 0, style }: { x: number; y: number; w: number; h: number; fill: string; r?: number; style?: CSSProperties }) => (
  <Abs x={x} y={y} w={w} h={h} style={{ background: fill, borderRadius: r, ...style }} />
)

/** White paper card with soft shadow. */
export const Card = ({ x, y, w, h }: { x: number; y: number; w: number; h: number }) => (
  <Box x={x} y={y} w={w} h={h} r={3} fill="#fff" style={{ boxShadow: '0 2px 6px rgba(80,60,40,0.10)' }} />
)

/** Photo pinned as a polaroid: white frame + photo placeholder. */
export function Polaroid({ x, y, w, h, pad = 10, label = 'photo' }: { x: number; y: number; w: number; h: number; pad?: number; label?: string }) {
  return (
    <>
      <Card x={x} y={y} w={w} h={h} />
      <Ph x={x + pad} y={y + pad} w={w - pad * 2} h={h - pad * 2} label={label} />
    </>
  )
}

/** Handwritten heading (dark + orange via ==markup==). */
export const Hand = (p: Omit<TxtProps, 'className'>) => <Txt {...p} size={p.size * 1.12} className={t.hand} style={{ color: t.ink, ...p.style }} />

export function Logo({ x = 45, cy = 44 }: { x?: number; cy?: number }) {
  return (
    <Abs x={x} y={cy - 12} h={24} className={cn(t.body, 'flex items-center gap-[4px] whitespace-nowrap font-bold leading-none')} style={{ fontSize: 17, color: t.orange }}>
      <Tent size={15} strokeWidth={2.4} />{t.header.left}
    </Abs>
  )
}

/** Standard page with the header strip (logo · 2080 · AUTUMN EDITION + rule). */
export function Page({ children, header = true, bg = t.bg }: { children: ReactNode; header?: boolean; bg?: string }) {
  return (
    <Slide background={bg} style={{ color: t.ink }}>
      {header && (
        <>
          <Logo />
          <Txt x={640} cy={44} size={17} align="center" w={200} className="font-bold" style={{ color: t.orange }}>{t.header.center}</Txt>
          <Txt x={1238} cy={44} size={17} align="right" w={300} className="font-bold" style={{ color: t.orange }}>{t.header.right}</Txt>
          <Box x={35} y={70} w={1210} h={2} fill={t.orange} />
        </>
      )}
      {children}
    </Slide>
  )
}
