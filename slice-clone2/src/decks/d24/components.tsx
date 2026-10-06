import type { CSSProperties, ReactNode } from 'react'
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

export const Ph = ({ x, y, w, h, label = 'photo', tone, className }: { x: number; y: number; w: number; h: number; label?: string; tone?: string; className?: string }) => (
  <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label={label} tone={tone} className={cn('h-full w-full', className)} /></Abs>
)
/** Organic blob / doodle / wave graphic stand-in. */
export const Blob = (p: { x: number; y: number; w: number; h: number; label?: string; tone?: string }) => <Ph label="organic blob graphic" {...p} className="rounded-[40%]" />
export const Wave = (p: { x: number; y: number; w: number; h: number; tone?: string }) => <Ph label="wavy lines doodle" {...p} />

export function PSlide({ bg = '#fff', children }: { bg?: string; children: ReactNode }) {
  return <Slide background={bg} className={t.font} style={{ color: t.ink }}>{children}</Slide>
}

export const Box = ({ x, y, w, h, bg, r = 24, children, className, style }: { x: number; y: number; w: number; h: number; bg: string; r?: number; children?: ReactNode; className?: string; style?: CSSProperties }) => (
  <Abs x={x} y={y} w={w} h={h} className={className} style={{ background: bg, borderRadius: r, ...style }}>{children}</Abs>
)

/** Centered slide title + one-line description. */
export function Title({ cy = 97, color = t.ink, subColor = '#444', text = '제목을 입력해주세요', sub = '이 텍스트 박스에 현재 페이지와 관련된 내용을 간략하게 입력해주세요.' }: { cy?: number; color?: string; subColor?: string; text?: string; sub?: string }) {
  return (
    <>
      <Txt x={640} cy={cy} size={50} align="center" w={900} className="font-extrabold tracking-[-0.02em]" style={{ color }}>{text}</Txt>
      <Txt x={640} cy={cy + 52} size={17} align="center" w={900} className="font-light" style={{ color: subColor }}>{sub}</Txt>
    </>
  )
}

/** Rounded pill with centered single-line label. */
export const Pill = ({ x, y, w, h, bg, color = '#fff', size = 19, bold = true, children }: { x: number; y: number; w: number; h: number; bg: string; color?: string; size?: number; bold?: boolean; children: ReactNode }) => (
  <Abs x={x} y={y} w={w} h={h} className={cn('flex items-center justify-center whitespace-nowrap rounded-full leading-none', bold && 'font-bold')} style={{ background: bg, color, fontSize: size }}>{children}</Abs>
)

/** Section divider (big number + agenda). */
export function Section({ bg, no, items, children }: { bg: string; no: string; items: string[]; children?: ReactNode }) {
  return (
    <PSlide bg={bg}>
      {children}
      <Txt x={635} cy={222} size={196} lh={196} align="center" w={500} className="font-montserrat font-bold tracking-[-0.03em]" style={{ color: '#fff' }}>{no}</Txt>
      <Wave x={425} y={347} w={428} h={50} />
      {items.map((it, i) => <Txt key={it} x={500} cy={481 + i * 51} size={27.5} style={{ color: t.navy }}>{it}</Txt>)}
    </PSlide>
  )
}
