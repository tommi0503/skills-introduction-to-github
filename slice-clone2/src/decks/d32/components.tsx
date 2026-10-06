import type { CSSProperties, ReactNode } from 'react'
import { Abs, ImagePlaceholder, Slide, cn } from '../../ui'
import { t } from './theme'

type Align = 'left' | 'center' | 'right'
export interface TxtProps { x: number; cy: number; size: number; align?: Align; w?: number; className?: string; style?: CSSProperties; children: ReactNode }

/** `==accent==` and `**bold**` inline markup. */
export function Rich({ text }: { text: string }) {
  return (
    <>
      {text.split(/(==.*?==|\*\*.*?\*\*)/).map((s, i) =>
        s.startsWith('==') ? <span key={i} style={{ color: t.accent }}>{s.slice(2, -2)}</span>
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

/** Serif label inside an ellipse (page number, POINT 01, BEST 01, CONTACT...). */
export function Oval({ cx, cy, w, h, children, fill, color = t.ink, border, size = 12 }: { cx: number; cy: number; w: number; h: number; children: string; fill?: string; color?: string; border?: string; size?: number }) {
  return (
    <Abs x={cx - w / 2} y={cy - h / 2} w={w} h={h} className={cn(t.serif, 'flex items-center justify-center rounded-[50%] leading-none')}
      style={{ background: fill, color, border: border ? `1px solid ${border}` : undefined, fontSize: size }}>{children}</Abs>
  )
}

/** Standard page: number oval, centred caption, right label, hairline rule. */
export function Page({ no, caption, bg = t.bg, ink = t.ink, rule = t.rule, note, under, children }: {
  no?: string; caption?: string; bg?: string; ink?: string; rule?: string | false; note?: boolean; under?: ReactNode; children: ReactNode
}) {
  return (
    <Slide background={bg} style={{ color: ink }}>
      {under}
      {no && <Oval cx={64} cy={46} w={50} h={28} border={ink} color={ink}>{no}</Oval>}
      {caption && <Txt x={640} cy={46} size={16} align="center" className={cn(t.latin, 'font-medium')} style={{ color: ink }}>{caption}</Txt>}
      <Txt x={1240} cy={46} size={13} align="right" w={300} style={{ color: ink }}>{t.chrome.right}</Txt>
      {rule && <Box x={40} y={80} w={1190} h={1} fill={rule} />}
      {children}
      {note && <Txt x={1265} cy={698} size={10} align="right" w={300} style={{ color: '#b5b5b5' }}>{t.chrome.note}</Txt>}
    </Slide>
  )
}
