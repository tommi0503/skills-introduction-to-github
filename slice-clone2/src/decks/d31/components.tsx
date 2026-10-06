import type { CSSProperties, ReactNode } from 'react'
import { Abs, ImagePlaceholder, Slide, cn } from '../../ui'
import { t } from './theme'

type Align = 'left' | 'center' | 'right'
export interface TxtProps { x: number; cy: number; size: number; align?: Align; w?: number; className?: string; style?: CSSProperties; children: ReactNode }

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

/** `**bold**` and `__lime__` inline markup. */
export function Rich({ text }: { text: string }) {
  return (
    <>
      {text.split(/(\*\*.*?\*\*|__.*?__)/).map((s, i) =>
        s.startsWith('**') ? <b key={i} className="font-bold">{s.slice(2, -2)}</b>
          : s.startsWith('__') ? <b key={i} className="font-bold" style={{ color: t.lime }}>{s.slice(2, -2)}</b>
            : s)}
    </>
  )
}

export function Lines({ lines, cy0, gap, ...rest }: Omit<TxtProps, 'cy' | 'children'> & { lines: readonly string[]; cy0: number; gap: number }) {
  return <>{lines.map((l, i) => <Txt key={i} {...rest} cy={cy0 + i * gap}>{l}</Txt>)}</>
}

export const Ph = ({ x, y, w, h, label, tone, className }: { x: number; y: number; w: number; h: number; label: string; tone?: string; className?: string }) => (
  <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label={label} tone={tone} className={cn('h-full w-full', className)} /></Abs>
)
export const Rect = ({ x, y, w, h, fill, className }: { x: number; y: number; w: number; h: number; fill: string; className?: string }) => (
  <Abs x={x} y={y} w={w} h={h} className={className} style={{ background: fill }} />
)

/** Decorative swoosh strokes drawn as SVG paths. */
export function Swoosh({ paths, color }: { paths: readonly (readonly [string, number])[]; color: string }) {
  return (
    <svg className="pointer-events-none absolute left-0 top-0" width={1280} height={720}>
      {paths.map(([d, w], i) => <path key={i} d={d} fill="none" stroke={color} strokeWidth={w} strokeLinecap="round" />)}
    </svg>
  )
}

export const Logo = ({ x = 1117, y = 46, w = 113, h = 17, tone }: { x?: number; y?: number; w?: number; h?: number; tone?: string }) => <Ph x={x} y={y} w={w} h={h} label="MIRI GOLF logo" tone={tone} />

/** Page chrome: KR title left, latin caption centre, logo right, rule, footer captions. */
export function Page({ bg = '#fff', title, caption, ink = t.ink, rule = t.rule, footerLeft = true, footerRight = true, logo = true, logoTone, children, under }: {
  bg?: string; title?: string; caption?: string; ink?: string; rule?: string; footerLeft?: boolean; footerRight?: boolean; logo?: boolean; logoTone?: string; children: ReactNode; under?: ReactNode
}) {
  return (
    <Slide background={bg} style={{ color: ink }}>
      {under}
      {title && <Txt x={48} cy={62} size={25} className="font-bold" style={{ color: ink }}>{title}</Txt>}
      {caption && <Txt x={640} cy={55} size={17} align="center" className={t.latin} style={{ color: ink }}>{caption}</Txt>}
      {title && <Rect x={53} y={96} w={1172} h={1} fill={rule} />}
      {logo && <Logo tone={logoTone} />}
      {children}
      {footerLeft && <Txt x={48} cy={667} size={15} className={t.latin} style={{ color: ink }}>{t.footer.left}</Txt>}
      {footerRight && <Txt x={1232} cy={666} size={15} align="right" style={{ color: ink }}>{t.footer.right}</Txt>}
    </Slide>
  )
}

/** Small filled badge (blue/lime) with centred label. */
export function Badge({ x, y, w, h, fill, color = '#fff', size = 15, children }: { x: number; y: number; w: number; h: number; fill: string; color?: string; size?: number; children: string }) {
  return (
    <Abs x={x} y={y} w={w} h={h} className={cn('flex items-center justify-center font-semibold leading-none', t.latin)} style={{ background: fill, color, fontSize: size }}>{children}</Abs>
  )
}
