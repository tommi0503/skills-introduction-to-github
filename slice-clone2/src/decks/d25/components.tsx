import type { CSSProperties, ReactNode } from 'react'
import { Leaf } from 'lucide-react'
import { Abs, ImagePlaceholder, Slide, cn } from '../../ui'
import { t } from './theme'

type Align = 'left' | 'center' | 'right'
/** Text block: `x` = left / centre / right edge per `align`, `cy` = centre of the first line, `lh` = line pitch. */
export function Txt({ x, cy, size, lh, align = 'left', w = 1000, className, style, children }: {
  x: number; cy: number; size: number; lh?: number; align?: Align; w?: number; className?: string; style?: CSSProperties; children: ReactNode
}) {
  const l = lh ?? size * 1.3
  const left = align === 'left' ? x : align === 'center' ? x - w / 2 : x - w
  return (
    <Abs x={left} y={cy - l / 2} w={w} className={cn('whitespace-pre-line', className)} style={{ fontSize: size, lineHeight: `${l}px`, textAlign: align, ...style }}>
      {children}
    </Abs>
  )
}

export const Ph = ({ x, y, w, h, label = 'photo', className }: { x: number; y: number; w: number; h: number; label?: string; className?: string }) => (
  <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label={label} className={cn('h-full w-full', className)} /></Abs>
)
export const Box = ({ x, y, w, h, bg, r = 20, children, style }: { x: number; y: number; w: number; h: number; bg: string; r?: number; children?: ReactNode; style?: CSSProperties }) => (
  <Abs x={x} y={y} w={w} h={h} style={{ background: bg, borderRadius: r, ...style }}>{children}</Abs>
)

/** Text set on an upward arc (SVG textPath), centred at (cx, cy) baseline apex. */
export function ArcText({ cx, cy, r, size, text, color = t.leaf, spacing = 1 }: { cx: number; cy: number; r: number; size: number; text: string; color?: string; spacing?: number }) {
  const id = `arc-${cx}-${cy}-${r}`
  return (
    <Abs x={cx - r - 10} y={cy + r * 0.1}>
      <svg width={r * 2 + 20} height={r} className="overflow-visible">
        <path id={id} d={`M 10 ${r * 0.9} A ${r} ${r} 0 0 1 ${r * 2 + 10} ${r * 0.9}`} fill="none" />
        <text fontSize={size} fill={color} letterSpacing={spacing} textAnchor="middle" fontFamily="Pretendard Variable">
          <textPath href={`#${id}`} startOffset="50%">{text}</textPath>
        </text>
      </svg>
    </Abs>
  )
}

/** Beige textured backdrop: corner blobs stand in as placeholders. */
export function Backdrop({ blobs }: { blobs: [number, number, number, number][] }) {
  return <>{blobs.map(([x, y, w, h], i) => <Ph key={i} x={x} y={y} w={w} h={h} label="organic blob graphic" className="rounded-[45%]" />)}</>
}
const defaultBlobs: [number, number, number, number][] = [[0, 0, 350, 150], [950, 0, 330, 140], [0, 560, 360, 160], [940, 520, 340, 200]]

export const Footer = ({ cy = 684 }: { cy?: number }) => <Txt x={640} cy={cy} size={15} align="center" w={400} style={{ color: '#444' }}>www.miricompany.com</Txt>

export type Layout = { card: { x: number; y: number; w: number; h: number }; tabTop: number; tabR: number; arcR: number; markCy: number; titleCy: number }
const std: Layout = { card: t.card, tabTop: 28, tabR: 50, arcR: 32, markCy: 72, titleCy: 156 }

/** Standard content slide: beige backdrop, white card with chapter tab, display title + subtitle. */
export function CardSlide({ chapter, title, sub = '타이틀에 관한 내용을 입력하세요.', layout = std, children, blobs = defaultBlobs }: {
  chapter?: string; title: string; sub?: string | null; layout?: Layout; children?: ReactNode; blobs?: [number, number, number, number][]
}) {
  const { card, tabTop, tabR, arcR, markCy, titleCy } = layout
  return (
    <Slide background={t.bg} className={t.font} style={{ color: t.ink }}>
      <Backdrop blobs={blobs} />
      <Box x={card.x} y={card.y} w={card.w} h={card.h} bg="#fff" r={44} />
      <Abs x={640 - tabR} y={tabTop} w={tabR * 2} h={tabR * 2} className="rounded-full bg-white" />
      <ArcText cx={640} cy={tabTop + 28} r={arcR} size={12} text="CHAPTER" spacing={1.5} />
      {chapter
        ? <Txt x={640} cy={markCy} size={19} align="center" w={40} className="font-bold italic" style={{ color: t.leaf }}>{chapter}</Txt>
        : <Abs x={626} y={markCy - 14}><Leaf size={28} fill={t.leaf} color={t.leaf} /></Abs>}
      <Txt x={640} cy={titleCy} size={74} align="center" w={1000} className={t.display}>{title}</Txt>
      {sub && <Txt x={640} cy={titleCy + 61} size={18} align="center" w={600}>{sub}</Txt>}
      {children}
      <Footer />
    </Slide>
  )
}
