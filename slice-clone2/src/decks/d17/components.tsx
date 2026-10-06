import type { CSSProperties, ReactNode } from 'react'
import { Abs, ImagePlaceholder, Slide, cn } from '../../ui'
import { t, tone, type Tone } from './theme'

export const FOOTER = '2080 MIRI Company Business Presentation'

/** Sky-blue backdrop, bordered white panel, bottom rule + strip and footer caption. */
export function Page({ children }: { children?: ReactNode }) {
  const p = t.panel
  return (
    <Slide background={t.bg} style={{ color: t.text, fontFamily: t.family }}>
      <Abs x={p.x} y={p.y} w={p.w} h={p.h} className="bg-white" style={{ border: `${p.border}px solid ${t.ink}` }}>
        <Abs x={0} y={t.rule.y - p.y - 1} w={p.w - 4} h={p.h - (t.rule.y - p.y) - 3} style={{ background: t.strip }} />
      </Abs>
      <Abs x={t.rule.x} y={t.rule.y} w={t.rule.w} h={2} style={{ background: t.ink }} />
      <Abs x={0} y={677} w={1280} h={14} className="text-center leading-[14px] font-medium" style={{ fontSize: 11, color: t.ink }}>{FOOTER}</Abs>
      {children}
    </Slide>
  )
}

/** Folder glyph (rounded frame with two small squares). */
export function Folder({ x, y }: { x: number; y: number }) {
  return (
    <Abs x={x} y={y} w={54} h={46}>
      <Abs x={0} y={0} w={22} h={10} className="rounded-t-[5px]" style={{ border: `2.5px solid ${t.ink}`, borderBottom: 0 }} />
      <Abs x={0} y={6} w={54} h={40} className="rounded-[6px]" style={{ border: `2.5px solid ${t.ink}`, background: t.blue }} />
      {[14, 28].map((cx) => <Abs key={cx} x={cx} y={20} w={12} h={13} className="rounded-[3px]" style={{ border: `2.5px solid ${t.ink}` }} />)}
    </Abs>
  )
}

/** Folder icon + rule + right-aligned title. `lineEnd` fixes the rule end when there is no title. */
export function Header({ title, lineEnd }: { title?: string; lineEnd?: number }) {
  return (
    <>
      <Folder x={76} y={77} />
      <Abs x={130} y={108} w={(lineEnd ?? (title ? 1190 : 1204)) - 130} h={2} style={{ background: t.ink }} />
      {title && (
        <Abs x={300} y={72} w={902} h={70} className="flex items-center justify-end">
          <span className="whitespace-nowrap bg-white pl-[38px] font-bold leading-none tracking-[-0.02em]" style={{ fontSize: 49 * t.fs, color: t.ink }}>{title}</span>
        </Abs>
      )}
    </>
  )
}

/** Inline markup: [[bold+highlight]], {{highlight}}, **bold**. */
export function Rich({ text }: { text: string }) {
  const parts = text.split(/(\[\[.*?\]\]|\{\{.*?\}\}|\*\*.*?\*\*)/)
  return (
    <>
      {parts.map((s, i) => {
        if (s.startsWith('[[')) return <span key={i} className="font-bold" style={{ background: t.blue, color: t.ink }}>{s.slice(2, -2)}</span>
        if (s.startsWith('{{')) return <span key={i} style={{ background: t.blue }}>{s.slice(2, -2)}</span>
        if (s.startsWith('**')) return <span key={i} className="font-bold" style={{ color: t.ink }}>{s.slice(2, -2)}</span>
        return s
      })}
    </>
  )
}

/** Explicit-line paragraph. `cy` = centre of first line. `justify` stretches all lines but the last. */
export function Lines({ lines, x, cy, pitch, size: s0, w, justify, align = 'left', className, style }: {
  lines: readonly string[]; x: number; cy: number; pitch: number; size: number; w?: number; justify?: boolean
  align?: 'left' | 'center' | 'right'; className?: string; style?: CSSProperties
}) {
  const size = s0 * t.fs
  return (
    <>
      {lines.map((l, i) => (
        <Abs key={i} x={x} y={cy + i * pitch - size * 0.7} w={w} h={size * 1.4}
          className={cn('whitespace-nowrap', className)}
          style={{ fontSize: size, lineHeight: `${size * 1.4}px`, textAlign: align, textAlignLast: justify && i < lines.length - 1 ? 'justify' : align, ...style }}>
          <Rich text={l} />
        </Abs>
      ))}
    </>
  )
}

export function Box({ x, y, w, h, k = 'grey', r = 12, children, className }: { x: number; y: number; w: number; h: number; k?: Tone; r?: number; children?: ReactNode; className?: string }) {
  return <Abs x={x} y={y} w={w} h={h} className={className} style={{ background: tone(k), borderRadius: r }}>{children}</Abs>
}

/** Tinted heading bar with leading vertical stroke. */
export function Bar({ x, y, w, h, k = 'grey', label, size: s0 = 25, inset = 22, r = 6 }: { x: number; y: number; w: number; h: number; k?: Tone; label: string; size?: number; inset?: number; r?: number }) {
  const size = s0 * t.fs
  return (
    <Box x={x} y={y} w={w} h={h} k={k} r={r} className="flex items-center whitespace-nowrap font-bold leading-none">
      <span style={{ marginLeft: inset, width: 2.5, height: size * 1.05, background: t.ink }} />
      <span style={{ marginLeft: size * 0.85, fontSize: size, color: t.ink }}>{label}</span>
    </Box>
  )
}

export function Photo({ x, y, w, h, label = 'photo', r = 0 }: { x: number; y: number; w: number; h: number; label?: string; r?: number }) {
  return (
    <Abs x={x} y={y} w={w} h={h} style={{ border: `2px solid ${t.ink}`, borderRadius: r }} className="overflow-hidden">
      <ImagePlaceholder label={label} className="h-full w-full" />
    </Abs>
  )
}

export function Logo({ x, y, right }: { x: number; y: number; right?: boolean }) {
  return (
    <Abs x={right ? x - 160 : x} y={y} w={160} h={22} className={cn('flex items-center gap-[5px] font-bold leading-none', right && 'justify-end')} style={{ fontSize: 17, color: t.ink }}>
      <ImagePlaceholder label="logo mark" className="h-[15px] w-[20px]" tone="#c9d5de" />MIRI Company
    </Abs>
  )
}

/** Single text line, `cy` = vertical centre. */
export function T({ x, cy, size: s0, children, w, className, align = 'left', style }: { x: number; cy: number; size: number; children: ReactNode; w?: number; className?: string; align?: 'left' | 'center' | 'right'; style?: CSSProperties }) {
  const size = s0 * t.fs
  return (
    <Abs x={x} y={cy - size * 0.7} w={w} h={size * 1.4} className={cn('whitespace-nowrap leading-none flex items-center', align === 'center' && 'justify-center', align === 'right' && 'justify-end', className)} style={{ fontSize: size, ...style }}>
      {children}
    </Abs>
  )
}

/** Full-width tinted note box with a left stroke and centred lines. */
export function NoteBox({ y, h, lines, cy, pitch = 31, size = 19.6 }: { y: number; h: number; lines: readonly string[]; cy: number; pitch?: number; size?: number }) {
  return (
    <>
      <Box x={77} y={y} w={1126} h={h} k="blue" r={8} />
      <Abs x={97} y={y + 16} w={2.5} h={h - 32} style={{ background: t.ink }} />
      <Lines lines={lines} x={0} w={1280} cy={cy} pitch={pitch} size={size} align="center" />
    </>
  )
}

/** Data table: dark header row, shaded first column, ink rules. `cols` are x boundaries. */
export function Table({ cols, y, headH, rowH, head, rows, size = 17 }: { cols: number[]; y: number; headH: number; rowH: number; head: string[]; rows: string[][]; size?: number }) {
  const x0 = cols[0], w = cols[cols.length - 1] - x0
  return (
    <>
      <Abs x={x0} y={y} w={w} h={headH} className="rounded-t-[4px]" style={{ background: t.ink }} />
      <Abs x={x0} y={y + headH} w={cols[1] - x0} h={rowH * rows.length} style={{ background: t.grey }} />
      {head.map((h, i) => <T key={h} x={cols[i]} w={cols[i + 1] - cols[i]} cy={y + headH / 2} size={size} align="center" className="font-bold text-white">{h}</T>)}
      {cols.slice(1, -1).map((cx) => <Abs key={cx} x={cx} y={y + 2} w={1} h={headH + rowH * rows.length - 2} style={{ background: t.ink }} />)}
      {rows.map((r, ri) => (
        <div key={ri}>
          <Abs x={x0} y={y + headH + (ri + 1) * rowH - 1} w={w} h={1} style={{ background: t.ink }} />
          {r.map((c, ci) => (
            <T key={ci} x={cols[ci]} w={cols[ci + 1] - cols[ci]} cy={y + headH + (ri + 0.5) * rowH} size={size - (ci ? 0 : 0.5)} align="center" className={ci ? '' : 'font-bold'} style={ci ? undefined : { color: t.ink }}>{c}</T>
          ))}
        </div>
      ))}
    </>
  )
}

/** Bottom-to-top vertical label (writing-mode, no transform). `cy` = vertical centre. */
export function VText({ x, cy, size, children, bold }: { x: number; cy: number; size: number; children: ReactNode; bold?: boolean }) {
  return (
    <Abs x={x - size * 0.7} y={cy - 60} w={size * 1.4} h={120} className={cn('flex items-center justify-center whitespace-nowrap leading-none', bold && 'font-bold')} style={{ fontSize: size * t.fs, writingMode: 'sideways-lr', color: bold ? t.ink : undefined }}>
      {children}
    </Abs>
  )
}
