import type { ReactNode } from 'react'
import { Abs, cn } from '../../ui'
import { CornerLogo, Frame, Lines, T, Tab, Title } from '../d02/components'
import { t } from './theme'

export { CornerLogo, Frame, Lines, T, Tab, Title }
export { Photo, Pill } from '../d02/components'

/** Deck-16 tab: narrower, bigger uppercase label. */
export const Tab16 = ({ x, lines, y }: { x: number; lines: readonly string[]; y?: number }) => (
  <Tab x={x} y={y ?? t.tab.y} lines={lines} w={t.tab.w} h={t.tab.h} size={16} pt={22} lh={21} />
)

/** Standard content page: frame + chapter tab (left or right) + centered title + optional intro lines. */
export function Page({ ch, right, title, intro, introY = 216, children, titleY = 132 }: { ch: number; right?: boolean; title?: string; intro?: readonly string[]; introY?: number; titleY?: number; children?: ReactNode }) {
  return (
    <Frame>
      <Tab16 x={right ? 990 : 79} lines={['CHAPTER', String(ch).padStart(2, '0')]} />
      {title && <Title text={title} y={titleY} />}
      {intro && <Lines x={140} y={introY} w={1000} size={16} lh={25} align="center" lines={intro} style={{ color: t.ink }} />}
      {children}
    </Frame>
  )
}

/** Small solid-blue rounded label. */
export const Badge = ({ x, y, w, h = 32, text, size = 15, bg = t.blue, color = '#fff', className }: { x: number; y: number; w: number; h?: number; text: string; size?: number; bg?: string; color?: string; className?: string }) => (
  <Abs x={x} y={y} w={w} h={h} className={cn('flex items-center justify-center whitespace-nowrap rounded-full font-semibold', className)} style={{ background: bg, color, fontSize: size }}>{text}</Abs>
)

/** Circle holding a lucide icon. */
export const IconDisc = ({ cx, cy, r, bg = '#fff', children, className }: { cx: number; cy: number; r: number; bg?: string; children: ReactNode; className?: string }) => (
  <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className={cn('flex items-center justify-center rounded-full', className)} style={{ background: bg }}>{children}</Abs>
)

/** Bullet list with round dots. */
export const Bullets = ({ x, y, items, size = 15, lh = 32, color = t.ink, dot = t.ink }: { x: number; y: number; items: readonly string[]; size?: number; lh?: number; color?: string; dot?: string }) => (
  <Abs x={x} y={y} className="whitespace-nowrap" style={{ fontSize: size, lineHeight: `${lh}px`, color }}>
    {items.map((it, i) => (
      <div key={i} className="flex items-center gap-[9px]"><span className="inline-block h-[5px] w-[5px] shrink-0 rounded-full" style={{ background: dot }} />{it}</div>
    ))}
  </Abs>
)

/** Full-width dark rounded bar with a white "Insight" tag. */
export const InsightBar = ({ y, tag, text, x = 122, w = 1036, h = 66, size = 17.8 }: { y: number; tag: string; text: string; x?: number; w?: number; h?: number; size?: number }) => (
  <Abs x={x} y={y} w={w} h={h} className="flex items-center rounded-full text-white" style={{ background: t.blue }}>
    <span className="ml-[27px] flex h-[30px] w-[88px] shrink-0 items-center justify-center rounded-full bg-white font-semibold" style={{ color: t.navy, fontSize: 15 }}>{tag}</span>
    <span className="ml-[21px] whitespace-nowrap font-medium" style={{ fontSize: size }}>{text}</span>
  </Abs>
)
