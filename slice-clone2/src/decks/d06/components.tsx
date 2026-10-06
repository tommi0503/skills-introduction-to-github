import type { ReactNode } from 'react'
import { Abs, ImagePlaceholder, Slide, cn } from '../../ui'
import { Lines } from '../../ui'
import { brand, company } from './data'
import { t } from './theme'

/** White print page with brand mark (top-right) and page number (bottom-right). */
export function PrintSlide({ page, brandColor = '#999', pageColor = '#333', showBrand = true, children }: { page?: string; brandColor?: string; pageColor?: string; showBrand?: boolean; children: ReactNode }) {
  return (
    <Slide background="#fff" className={t.sans} style={{ color: t.body }}>
      {children}
      {showBrand && <Lines x={t.right} cy={19} align="right" size={9.5} className="font-bold" color={brandColor} lines={[brand]} />}
      {page && <Lines x={t.right} cy={687} align="right" size={11.5} className="font-bold" color={pageColor} lines={[page]} />}
    </Slide>
  )
}

export const Photo = ({ x, y, w, h, tone, className }: { x: number; y: number; w: number; h: number; tone?: string; className?: string }) => (
  <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label="photo" tone={tone} className={className ?? 'h-full w-full'} /></Abs>
)

/** Latin heading; multi-line headings are one text block (tight leading like the reference). */
export const Heading = ({ x = t.left, cy, lines, size = 44, lh = 50 }: { x?: number; cy: number; lines: readonly string[]; size?: number; lh?: number }) => (
  <Abs x={x} y={cy - lh / 2} className={cn(t.head, 'whitespace-pre')} style={{ fontSize: size, lineHeight: `${lh}px`, color: t.title }}>
    {lines.join('\n')}
  </Abs>
)

export const SubHead = ({ x = t.left, cy, text, size = 19 }: { x?: number; cy: number; text: string; size?: number }) => (
  <Lines x={x} cy={cy} size={size} className="font-medium" color={t.ink} lines={[text]} />
)

export const Body = ({ x = t.left, cy, lines, size = t.bodySize, lh = t.bodyLh, color = t.body }: { x?: number; cy: number; lines: readonly string[]; size?: number; lh?: number; color?: string }) => (
  <Lines x={x} cy={cy} lh={lh} size={size} color={color} lines={lines} />
)

/** "부가범주" small legend block. */
export const Extra = ({ x, cy, extra }: { x: number; cy: number; extra: { title: string; lines: string[] } }) => (
  <>
    <Lines x={x} cy={cy} size={13} className="font-bold" color={t.ink} lines={[extra.title]} />
    <Lines x={x} cy={cy + 21} lh={14} size={10} color="#777" lines={extra.lines} />
  </>
)

/** Text column for chart pages (title / sub / body / extra). */
export function ChartText({ data }: { data: { title: string[]; sub: string; body: string[]; extra: { title: string; lines: string[] } } }) {
  return (
    <>
      <Heading x={214} cy={142} lines={data.title} />
      <SubHead x={214} cy={250} text={data.sub} />
      <Body x={214} cy={291} lines={data.body} />
      <Extra x={214} cy={502} extra={data.extra} />
    </>
  )
}

/** Company address block (bottom right of closing slides). */
export function Company({ color }: { color: string }) {
  return (
    <>
      <Lines x={971} cy={566} size={13} className="font-bold" color={color} lines={[company.name]} />
      <Lines x={971} cy={607} lh={13.6} size={11} color={color} lines={company.lines} />
      <Lines x={971} cy={663} size={11} color={color} lines={[company.copy]} />
    </>
  )
}
