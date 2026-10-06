import type { CSSProperties, ReactNode } from 'react'
import { Abs, ImagePlaceholder, Slide, cn } from '../../ui'
import { t } from './theme'

/** Vertical labels on the right folder tab. */
function SideTab({ date = '2025.02', company = 'MIRI COMPANY', foot = 'Simple Template' }) {
  const v: CSSProperties = { writingMode: 'vertical-rl', fontSize: 13.5, color: t.side, lineHeight: 1 }
  return (
    <>
      <Abs x={1205} y={68} className={cn(t.serif, 'font-medium')} style={v}>{date}</Abs>
      <Abs x={1196} y={294} w={37} h={133} className={cn(t.serif, 'flex items-center justify-center rounded-[50%] font-medium')} style={{ ...v, border: `1px solid ${t.side}` }}>{company}</Abs>
      <Abs x={1206} y={589} className={cn(t.serif, 'font-medium')} style={v}>{foot}</Abs>
    </>
  )
}

/**
 * Folder frame. `cover` = beige front sheet with a round notch; otherwise a white sheet
 * with the chapter rule + label on top.
 */
export function Folder({ children, cover, chapter, sheetBg = '#fff' }: { children?: ReactNode; cover?: boolean; chapter?: string; sheetBg?: string }) {
  const s = t.sheet
  return (
    <Slide background={t.page} className={t.ko} style={{ color: t.ink }}>
      <Abs x={26} y={22} w={1229} h={676} style={{ background: t.taupe, borderRadius: '0 20px 20px 0' }} />
      <Abs x={26} y={22} w={23} h={676} style={{ background: t.strip }} />
      {cover ? (
        <>
          <Abs x={1135} y={s.y} w={41} h={s.h} className="bg-white" />
          <Abs x={49} y={22} w={1086} h={676} style={{ background: t.beige }} />
          <Abs x={1078} y={305} w={114} h={114} className="rounded-full bg-white" />
        </>
      ) : (
        <>
          <Abs x={s.x} y={s.y} w={s.w} h={s.h} style={{ background: sheetBg }} />
          {chapter && <ChapterRule label={chapter} />}
        </>
      )}
      <SideTab />
      {children}
    </Slide>
  )
}

export const ChapterRule = ({ label }: { label: string }) => (
  <>
    <Abs x={87} y={79} w={959} h={1} style={{ background: t.rule }} />
    <T x={1070} y={73} size={14} className={cn(t.serif, 'font-medium')} style={{ color: t.ink }}>{label}</T>
  </>
)

/** Single-line text; (x,y) = box top-left. */
export function T({ x, y, w, size, children, className, style, align = 'left' }: { x: number; y: number; w?: number; size: number; children: ReactNode; className?: string; style?: CSSProperties; align?: 'left' | 'center' | 'right' }) {
  return (
    <Abs x={x} y={y} w={w} className={cn('whitespace-nowrap leading-none', className)} style={{ fontSize: size, textAlign: align, ...style }}>{children}</Abs>
  )
}

/** Explicit lines; `justify` stretches every line but the last. */
export function Lines({ x, y, w, size, lh, lines, className, style, align = 'left', justify }: { x: number; y: number; w?: number; size: number; lh: number; lines: readonly string[]; className?: string; style?: CSSProperties; align?: 'left' | 'center' | 'right'; justify?: boolean }) {
  return (
    <Abs x={x} y={y} w={w} className={cn('whitespace-nowrap', className)} style={{ fontSize: size, lineHeight: `${lh}px`, textAlign: align, ...style }}>
      {lines.map((l, i) => <div key={i} style={justify && i < lines.length - 1 ? { textAlign: 'justify', textAlignLast: 'justify' } : undefined}>{l}</div>)}
    </Abs>
  )
}

/** Small serif kicker ("Overview") + Korean page title. */
export function Heading({ kicker, title, x = 101, y, size = 50, align = 'left', w }: { kicker?: string; title: string; x?: number; y: number; size?: number; align?: 'left' | 'center'; w?: number }) {
  return (
    <>
      {kicker && <T x={x} y={y - 38} w={w} size={18.5} align={align} className={t.serif} style={{ color: t.sub }}>{kicker}</T>}
      <T x={x} y={y} w={w} size={size} align={align} className="font-semibold" style={{ color: t.ink, letterSpacing: '-0.01em' }}>{title}</T>
    </>
  )
}

/** Folder-shaped card: rectangle with a slanted tab on top-left (or right side). */
export function FolderCard({ x, y, w, h, bg = t.card, tab = 'top', tabW = 136, tabH = 17, children }: { x: number; y: number; w: number; h: number; bg?: string; tab?: 'top' | 'right' | 'none'; tabW?: number; tabH?: number; children?: ReactNode }) {
  return (
    <>
      {tab === 'top' && <Abs x={x} y={y - tabH} w={tabW} h={tabH + 1} style={{ background: bg, clipPath: `polygon(0 0, ${tabW - tabH - 8}px 0, 100% 100%, 0 100%)` }} />}
      {tab === 'right' && <Abs x={x + w - 1} y={y} w={tabH + 5} h={tabW} style={{ background: bg, clipPath: `polygon(0 0, 60% 0, 100% ${tabH}px, 100% calc(100% - ${tabH}px), 60% 100%, 0 100%)` }} />}
      <Abs x={x} y={y} w={w} h={h} style={{ background: bg }}>{children}</Abs>
    </>
  )
}

export const Photo = ({ x, y, w, h, className }: { x: number; y: number; w: number; h: number; className?: string }) => (
  <Abs x={x} y={y} w={w} h={h} className={className}><ImagePlaceholder label="photo" className="h-full w-full" /></Abs>
)

/** Rounded pill with a serif label. */
export const SerifPill = ({ x, y, w, h = 32, text, bg = t.card, size = 14, radius = h / 2 }: { x: number; y: number; w: number; h?: number; text: string; bg?: string; size?: number; radius?: number }) => (
  <Abs x={x} y={y} w={w} h={h} className={cn(t.serif, 'flex items-center justify-center whitespace-nowrap font-medium')} style={{ background: bg, fontSize: size, color: t.ink, borderRadius: radius }}>{text}</Abs>
)

/** Circle with an optional centred child. */
export const Disc = ({ cx, cy, r, bg, children, className, style }: { cx: number; cy: number; r: number; bg: string; children?: ReactNode; className?: string; style?: CSSProperties }) => (
  <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className={cn('flex flex-col items-center justify-center rounded-full', className)} style={{ background: bg, ...style }}>{children}</Abs>
)
