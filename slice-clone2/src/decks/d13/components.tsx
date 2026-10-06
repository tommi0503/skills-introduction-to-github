import type { ReactNode } from 'react'
import { Abs, Slide } from '../../ui'
import { Box, Lines } from '../../ui'
import { total } from './data'
import { t, tone, type Tone } from './theme'

const TABS = [t.tan, t.pink, t.blue, t.green]

/** Notebook page: grey shadow, 4 coloured index tabs, ring binding on the left, page sticker. */
export function NoteSlide({ page, fill = '#fffeff', children }: { page?: number; fill?: string; children: ReactNode }) {
  return (
    <Slide background={t.bg} className={t.sans} style={{ color: t.text, ['--ly' as string]: '0.04em' }}>
      <Box x={33} y={45} w={1213} h={641} bg={t.shadow} className="rounded-lg" />
      {TABS.map((c, i) => <Box key={c} x={53 + i * 293.5} y={30} w={293} h={40} bg={c} className="rounded-t-lg" />)}
      <Box x={53} y={65} w={1174} h={3} bg="rgba(0,0,0,0.12)" />
      <Box x={53} y={67} w={1174} h={600} bg={fill} />
      {Array.from({ length: 14 }, (_, i) => (
        <div key={i}>
          <Box x={53} y={95 + i * 41.7} w={14} h={2} bg="#888" />
          <Abs x={67} y={89 + i * 41.7} w={14} h={14} className="rounded-full" style={{ background: '#a8a6a4' }} />
        </div>
      ))}
      {children}
      {page !== undefined && <Sticker top={String(page)} bottom={total} />}
    </Slide>
  )
}

/** Round pink sticker with dashed inner ring (page number / date). */
export function Sticker({ top, bottom, big = false }: { top: string; bottom: string; big?: boolean }) {
  const cx = big ? 1137 : 1150, cy = big ? 155 : 137, r = big ? 60 : 45
  return (
    <>
      <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className="rounded-full" style={{ background: t.pink }} />
      <Abs x={cx - r + 4} y={cy - r + 4} w={r * 2 - 8} h={r * 2 - 8} className="rounded-full" style={{ border: '1.5px dashed #fbd7df' }} />
      {big ? (
        <>
          <Lines x={cx} cy={cy - 18} align="center" w={100} size={19} className="font-semibold" color="#fff" lines={[top]} />
          <Lines x={cx} cy={cy + 10} align="center" w={100} size={30} className="font-semibold" color="#fff" lines={[bottom]} />
        </>
      ) : (
        <>
          <Lines x={cx - 12} cy={cy - 10} align="center" w={60} size={23} className="font-semibold" color="#fff" lines={[top]} />
          <Lines x={cx + 13} cy={cy + 10} align="center" w={60} size={14} color="#f8c9d4" lines={[bottom]} />
        </>
      )}
    </>
  )
}

/** Centred page title with a short green rule underneath. */
export function Title({ text, cy = 145 }: { text: string; cy?: number }) {
  return (
    <>
      <Lines x={656} cy={cy} align="center" size={60} className="font-medium tracking-[-0.01em]" color={t.ink} lines={[text]} />
      <Box x={639} y={cy + 57} w={36} h={3} bg={t.green} />
    </>
  )
}

export const Sub = ({ x, cy, text, align = "left", size = 31.5 }: { x: number; cy: number; text: string | readonly string[]; align?: 'left' | 'center'; size?: number }) => (
  <Lines x={x} cy={cy} lh={size * 1.38} align={align} size={size} color={t.green} lines={typeof text === 'string' ? [text] : text} />
)

export const Text = ({ x, cy, lines, align = 'left', size = 17.5, lh = 29, w = 1400 }: { x: number; cy: number; lines: readonly string[]; align?: 'left' | 'center'; size?: number; lh?: number; w?: number }) => (
  <Lines x={x} cy={cy} lh={lh} align={align} w={w} size={size} color={t.text} lines={lines} />
)

/** Outlined pale card in a tone. */
export function ToneCard({ x, y, w, h, c, r = 6, children, className }: { x: number; y: number; w: number; h: number; c: Tone; r?: number; children?: ReactNode; className?: string }) {
  return <Box x={x} y={y} w={w} h={h} bg={tone[c].bg} className={className} style={{ border: `2px solid ${tone[c].fg}`, borderRadius: r }}>{children}</Box>
}

/** Solid tab / pill with spaced latin label. */
export function Tag({ x, y, w, h, c, text, size = 19, className }: { x: number; y: number; w: number; h: number; c: Tone; text: string; size?: number; className?: string }) {
  return (
    <>
      <Box x={x} y={y} w={w} h={h} bg={tone[c].fg} className={className} />
      <Lines x={x + w / 2} cy={y + h / 2} align="center" w={w} size={size} className="tracking-[0.08em]" color="#fff" lines={[text]} />
    </>
  )
}

/** Bulleted lines; each item may wrap to several lines with hanging indent. */
export function Bullets({ x, cy, items, lh = 27.5, gap = 6, size = 17 }: { x: number; cy: number; items: readonly (readonly string[])[]; lh?: number; gap?: number; size?: number }) {
  let y = cy
  return (
    <>
      {items.map((p, i) => {
        const top = y
        y += p.length * lh + gap
        return (
          <div key={i}>
            <Abs x={x} y={top - 3} w={6} h={6} className="rounded-full" style={{ background: t.ink }} />
            <Lines x={x + 18} cy={top} lh={lh} size={size} color={t.text} lines={p} />
          </div>
        )
      })}
    </>
  )
}

