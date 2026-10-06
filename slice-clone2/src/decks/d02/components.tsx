import type { CSSProperties, ReactNode } from 'react'
import { Abs, ImagePlaceholder, Slide, cn } from '../../ui'
import { t } from './theme'

type Box = { x: number; y: number; w: number; h: number }
type Panel = typeof t.panel | Box

/** Light/dark two-band background + white panel. */
export function Frame({ children, panel = t.panel, split = t.bg.split, colors }: { children?: ReactNode; panel?: Panel; split?: number; colors?: { light: string; dark: string } }) {
  const c = colors ?? { light: t.sky, dark: t.blue }
  return (
    <Slide background={c.light} className={t.font} style={{ color: t.navy }}>
      <Abs x={0} y={split} w={1280} h={720 - split} style={{ background: c.dark }} />
      <Abs x={panel.x} y={panel.y} w={panel.w} h={panel.h} style={{ background: '#fff' }} />
      {children}
    </Slide>
  )
}

/** Half-disc tab hanging from the panel top with a two-line white label. */
export function Tab({ x, lines, y = t.tab.y, color = t.blue, size = 17, w = t.tab.w, h = t.tab.h, pt = 27, lh = 21 }: { x: number; lines: readonly string[]; y?: number; color?: string; size?: number; w?: number; h?: number; pt?: number; lh?: number }) {
  return (
    <Abs x={x} y={y} w={w} h={h} className="flex flex-col items-center text-white" style={{ paddingTop: pt, background: color, borderRadius: `0 0 ${w / 2}px ${w / 2}px`, fontSize: size, lineHeight: `${lh}px`, letterSpacing: '0.04em' }}>
      {lines.map((l) => <div key={l}>{l}</div>)}
    </Abs>
  )
}

/** Diagonal corner with logo mark + company name (bottom-right of panel). */
export function CornerLogo({ bottom = 680, right = 1236, name = 'MIRI COMPANY', color = t.blue }: { bottom?: number; right?: number; name?: string; color?: string }) {
  return (
    <>
      <Abs x={right - 136} y={bottom - 136} w={136} h={136} style={{ background: color, clipPath: 'polygon(100% 0, 100% 100%, 0 100%)' }} />
      <Abs x={right - 63} y={bottom - 63} w={30} h={30}><ImagePlaceholder label="company logo mark" className="h-full w-full" tone="#c9d2ef" /></Abs>
      <Abs x={right - 106} y={bottom - 22} w={110} className="whitespace-nowrap text-center leading-none text-white" style={{ fontSize: 12 }}>{name}</Abs>
    </>
  )
}

/** Single-line text; (x,y) = box top-left, leading-none. align uses w. */
export function T({ x, y, w, size, children, className, style, align = 'left' }: { x: number; y: number; w?: number; size: number; children: ReactNode; className?: string; style?: CSSProperties; align?: 'left' | 'center' | 'right' }) {
  return (
    <Abs x={x} y={y} w={w} className={cn('whitespace-nowrap leading-none', className)} style={{ fontSize: size, textAlign: align, ...style }}>
      {children}
    </Abs>
  )
}

/** Multi-line block with explicit lines; `justify` stretches all but the last line. */
export function Lines({ x, y, w, size, lh, lines, className, style, align = 'left', justify }: { x: number; y: number; w?: number; size: number; lh: number; lines: readonly string[]; className?: string; style?: CSSProperties; align?: 'left' | 'center' | 'right'; justify?: boolean }) {
  return (
    <Abs x={x} y={y} w={w} className={cn('whitespace-nowrap', className)} style={{ fontSize: size, lineHeight: `${lh}px`, textAlign: align, ...style }}>
      {lines.map((l, i) => (
        <div key={i} style={justify && i < lines.length - 1 ? { textAlign: 'justify', textAlignLast: 'justify' } : undefined}>{l}</div>
      ))}
    </Abs>
  )
}

/** Centered page title. */
export const Title = ({ text, y = 136, size = 50, cx = 640 }: { text: string; y?: number; size?: number; cx?: number }) => (
  <T x={cx - 500} y={y} w={1000} size={size} align="center" className="font-bold" style={{ color: t.navy, letterSpacing: '-0.01em' }}>{text}</T>
)

/** Rounded keyword pill. */
export const Pill = ({ x, y, w, h = 43, text, size = 15, bg = t.sky, color = t.navy, className }: { x: number; y: number; w: number; h?: number; text: string; size?: number; bg?: string; color?: string; className?: string }) => (
  <Abs x={x} y={y} w={w} h={h} className={cn('flex items-center justify-center whitespace-nowrap rounded-full font-medium', className)} style={{ background: bg, color, fontSize: size }}>{text}</Abs>
)

export const Photo = ({ x, y, w, h, className }: Box & { className?: string }) => (
  <Abs x={x} y={y} w={w} h={h} className={className}><ImagePlaceholder label="photo" className="h-full w-full" /></Abs>
)
