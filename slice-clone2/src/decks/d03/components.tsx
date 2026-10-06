import type { ReactNode } from 'react'
import { Abs, Slide, cn } from '../../ui'
import { Lines } from '../../ui'
import { t } from './theme'

/** Content slide: thin blue top bar + page number. */
export function PageSlide({ page, children }: { page: number; children: ReactNode }) {
  return (
    <Slide background="#fff" className={t.sans} style={{ color: t.ink }}>
      {children}
      <Abs x={0} y={0} w={1280} h={t.topBar} style={{ background: t.blue }} />
      <Lines x={1258} cy={30} align="right" w={60} size={13} className={cn(t.latin, 'font-bold')} color={t.navy} lines={[String(page)]} />
    </Slide>
  )
}

/** Korean title + small latin subtitle at the top-left. */
export function SectionHead({ head }: { head: readonly [string, string] }) {
  return (
    <>
      <Lines x={t.left - 1} cy={166} size={56} className={t.head} color={t.navy} lines={[head[0]]} />
      <Lines x={t.left} cy={213} size={18} className={cn(t.latin, 'font-medium')} color={t.navy} lines={[head[1]]} />
    </>
  )
}

/** Italic one-line summary aligned to the right margin. */
export const Summary = ({ text, cy = 165 }: { text: string; cy?: number }) => (
  <Lines x={t.right} cy={cy} align="right" size={34} className="font-medium italic" color="#222" lines={[text]} />
)

/** Paragraph groups with a blank gap between groups. */
export function Paras({ x, cy, paras, lh = 25, gap = 18, size = 19, color = '#333' }: { x: number; cy: number; paras: readonly (readonly string[])[]; lh?: number; gap?: number; size?: number; color?: string }) {
  let y = cy
  return (
    <>
      {paras.map((p, i) => {
        const el = <Lines key={i} x={x} cy={y} lh={lh} size={size} color={color} lines={p} />
        y += p.length * lh + gap
        return el
      })}
    </>
  )
}

/** Bulleted paragraphs (bullet + hanging indent). */
export function Bullets({ x, cy, items, lh = 25, size = 19, indent = 18, color = '#222', gap = 0 }: { x: number; cy: number; items: readonly (readonly string[])[]; lh?: number; size?: number; indent?: number; color?: string; gap?: number }) {
  let y = cy
  return (
    <>
      {items.map((p, i) => {
        const top = y
        y += p.length * lh + gap
        return (
          <div key={i}>
            <Abs x={x} y={top - 3} w={6} h={6} className="rounded-full" style={{ background: color }} />
            <Lines x={x + indent} cy={top} lh={lh} size={size} color={color} lines={p} />
          </div>
        )
      })}
    </>
  )
}
