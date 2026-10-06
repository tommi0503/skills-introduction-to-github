import type { ReactNode } from 'react'
import { Sparkle } from 'lucide-react'
import { Abs, ImagePlaceholder, Slide } from '../../ui'
import { Box, Lines } from '../../ui'
import { brand, bubble } from './data'
import { t } from './theme'

const gridBg = `repeating-linear-gradient(90deg, transparent 0 35px, ${t.grid} 35px 38px, transparent 38px 71px), repeating-linear-gradient(0deg, transparent 0 35px, ${t.grid} 35px 38px, transparent 38px 71px)`

/** Sky grid paper. */
export function GridSlide({ children }: { children: ReactNode }) {
  return (
    <Slide background={t.sky} className={t.sans} style={{ color: t.navy, backgroundImage: gridBg, ['--ly' as string]: '0.06em' }}>
      {children}
    </Slide>
  )
}

/** White card with navy outline and an offset outline "shadow". */
export function Card({ x, y, w, h, bg = '#fff', offset = 6, children }: { x: number; y: number; w: number; h: number; bg?: string; offset?: number; children?: ReactNode }) {
  return (
    <>
      <Box x={x + offset} y={y + offset} w={w} h={h} bg={t.sky} style={{ border: `1.5px solid ${t.navy}` }} />
      <Box x={x} y={y} w={w} h={h} bg={bg} style={{ border: `2px solid ${t.navy}` }}>{children}</Box>
    </>
  )
}

/** Content page: card with header bar (brand + page no.) and a paperclip. */
export function PageCard({ page, clip = true, children }: { page: string; clip?: boolean; children: ReactNode }) {
  return (
    <GridSlide>
      <Card x={34} y={32} w={1212} h={651} />
      <Box x={34} y={101} w={1212} h={2} bg={t.navy} />
      <Lines x={60} cy={66} size={24.5} className="font-medium" color={t.navy} lines={[brand]} />
      <Lines x={1222} cy={66} align="right" size={24} className="font-medium" color={t.navy} lines={[page]} />
      {clip && <Placeholder x={1099} y={0} w={49} h={123} r="0 0 25px 25px" label="paperclip" />}
      {children}
    </GridSlide>
  )
}

export const Placeholder = ({ x, y, w, h, r, label = 'illustration' }: { x: number; y: number; w: number; h: number; r?: string; label?: string }) => (
  <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label={label} className="h-full w-full" style={{ borderRadius: r }} /></Abs>
)

/** Smiley character → round placeholder. */
export const Character = ({ cx, cy, r }: { cx: number; cy: number; r: number }) => <Placeholder x={cx - r} y={cy - r} w={r * 2} h={r * 2} r="50%" label="smiley character" />

export const Star = ({ cx, cy, size, fill }: { cx: number; cy: number; size: number; fill: string }) => (
  <Abs x={cx - size / 2} y={cy - size / 2}><Sparkle size={size} fill={fill} color={t.navy} strokeWidth={1} /></Abs>
)

export const Ring = ({ cx, cy, r = 8 }: { cx: number; cy: number; r?: number }) => (
  <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className="rounded-full bg-white" style={{ border: `2px solid ${t.navy}` }} />
)

/** "MIRI BRAND" speech bubble (ellipse). */
export function Bubble({ cx, cy }: { cx: number; cy: number }) {
  return (
    <>
      <Abs x={cx - 80} y={cy - 57} w={161} h={114} className="rounded-[50%]" style={{ background: t.lemon, border: `2px solid ${t.navy}` }} />
      <Lines x={cx} cy={cy - 16} lh={31} align="center" w={160} size={27} className={t.latin} color={t.navy} lines={bubble} />
    </>
  )
}

export const Title = ({ text, cy, size = 92 }: { text: ReactNode; cy: number; size?: number }) => (
  <Lines x={640} cy={cy} align="center" size={size} className={t.display} color={t.navy} lines={[text]} />
)
