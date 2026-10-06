import type { CSSProperties, ReactNode } from 'react'
import { Abs, Slide, cn } from '../../ui'
import { t, tabOrder, type Chapter } from './theme'

const clip = (pts: [number, number][]) => `polygon(${pts.map(([x, y]) => `${x}px ${y}px`).join(',')})`

/** Stack of slanted folder tabs (the chapters after `current`, cyclic). */
function Tabs({ current, x, w, y0, side }: { current: Chapter; x: number; w: number; y0: number; side: 'l' | 'r' }) {
  const i0 = tabOrder.indexOf(current)
  const rest = [1, 2, 3, 4].map((k) => tabOrder[(i0 + k) % 5])
  return (
    <>
      {rest.map((c, k) => {
        const y = y0 + k * 80, s = 44
        const pts: [number, number][] = side === 'r' ? [[0, s], [w, 0], [w, 80], [0, 80 + s]] : [[0, 0], [w, s], [w, 80 + s], [0, 80]]
        return <Abs key={c} x={x} y={y} w={w} h={80 + s} style={{ background: t[c], clipPath: clip(pts), zIndex: 4 - k }} />
      })}
    </>
  )
}

/** Coloured folder page with tab notch on the right and a vertical CHAPTER label. */
export function FolderPage({ color, chapter, children }: { color: Chapter; chapter?: string; children?: ReactNode }) {
  const e = t.edge
  return (
    <Slide background="#fff" className={t.body} style={{ color: t.text }}>
      <Tabs current={color} x={e - 4} w={1280 - e + 4} y0={238} side="r" />
      <Abs x={0} y={0} w={1280} h={720} style={{ background: t[color], clipPath: clip([[0, 0], [1280, 0], [1280, 200], [e, 276], [e, 720], [0, 720]]), zIndex: 5 }} />
      <div className="relative" style={{ zIndex: 6 }}>
        {chapter && (
          <Abs x={1238} y={42} w={24} h={120} className="flex items-start justify-center font-extrabold leading-none" style={{ writingMode: 'vertical-rl', fontSize: 16, color: t.navy, letterSpacing: '0.02em' }}>{chapter}</Abs>
        )}
        {children}
      </div>
    </Slide>
  )
}

/** Cover / closing page: navy spine on the left with tabs, pink folder. */
export function CoverPage({ children }: { children?: ReactNode }) {
  const e = t.edge
  return (
    <Slide background="#fff" className={t.body} style={{ color: t.text }}>
      <Abs x={0} y={0} w={16} h={720} style={{ background: t.navy }} />
      <Abs x={0} y={44} w={57} h={250} className="rounded-tr-[14px]" style={{ background: t.navy }} />
      <Tabs current="pink" x={12} w={30} y0={262} side="l" />
      <Abs x={14} y={0} w={1266} h={720} style={{ background: t.pink, clipPath: clip([[44, 0], [1266, 0], [1266, 190], [e - 14, 270], [e - 14, 720], [0, 720], [0, 600], [26, 560], [26, 290], [44, 260]]), zIndex: 5 }} />
      <Abs x={14} y={0} w={44} h={720} style={{ background: t.pink, clipPath: clip([[0, 0], [44, 0], [44, 44], [0, 44]]), zIndex: 5 }} />
      <div className="relative" style={{ zIndex: 6 }}>{children}</div>
    </Slide>
  )
}

/** Single line, `cy` = vertical centre. */
export function T({ x, cy, size, children, w, className, align = 'left', style }: { x: number; cy: number; size: number; children: ReactNode; w?: number; className?: string; align?: 'left' | 'center' | 'right'; style?: CSSProperties }) {
  return (
    <Abs x={x} y={cy - size * 0.75} w={w} h={size * 1.5} className={cn('flex items-center whitespace-nowrap leading-none', align === 'center' && 'justify-center', align === 'right' && 'justify-end', className)} style={{ fontSize: size, ...style }}>
      {children}
    </Abs>
  )
}

export function Lines({ lines, x, cy, pitch, size, w, align = 'left', className, style }: { lines: readonly string[]; x: number; cy: number; pitch: number; size: number; w?: number; align?: 'left' | 'center' | 'right'; className?: string; style?: CSSProperties }) {
  return <>{lines.map((l, i) => <T key={i} x={x} cy={cy + i * pitch} size={size} w={w} align={align} className={className} style={style}>{l}</T>)}</>
}

/** Heavy rounded display title with gap line + offset shadow. */
export function Title({ text, cy, size = 70, cx = t.cx, bg, light }: { text: string; cy: number; size?: number; cx?: number; bg: string; light?: boolean }) {
  return (
    <T x={cx - 600} w={1200} cy={cy} size={size} align="center" className={t.display}
      style={{ color: light ? '#fff' : t.navy, textShadow: light ? `-2px -2px 0 ${t.navy}, 2px -2px 0 ${t.navy}, -2px 2px 0 ${t.navy}, 2px 2px 0 ${t.navy}, 5px 5px 0 ${t.navy}` : `2px 2px 0 ${bg}, 5px 5px 0 ${t.navy}`, letterSpacing: '-0.02em' }}>
      {text}
    </T>
  )
}

/** "~ WORD ~" spaced red subtitle. */
export function Kicker({ word, cy, size = 32, cx = t.cx }: { word: string; cy: number; size?: number; cx?: number }) {
  return <T x={cx - 400} w={800} cy={cy} size={size} align="center" className="font-extrabold" style={{ color: t.red, letterSpacing: '0.16em' }}>{`~ ${word} ~`}</T>
}

/** White card with navy border and optional navy header band. */
export function Card({ x, y, w, h, head = 0, label, r = 12, labelSize = 16.5 }: { x: number; y: number; w: number; h: number; head?: number; label?: string; r?: number; labelSize?: number }) {
  return (
    <>
      <Abs x={x} y={y} w={w} h={h} className="overflow-hidden bg-white" style={{ border: `2px solid ${t.navy}`, borderRadius: r }}>
        {head > 0 && <div className="flex items-center justify-center text-white" style={{ height: head - 2, background: t.navy, fontSize: labelSize }}>{label}</div>}
      </Abs>
    </>
  )
}

/** "③조" team badge + student line. */
export function Team({ cy, cy2, size = 20, team }: { cy: number; cy2: number; size?: number; team: { no: string; suffix: string; line: string } }) {
  return (
    <>
      <T x={t.cx - 100} w={200} cy={cy} size={28} align="center" className="font-bold" style={{ color: t.navy }}>
        <span className="mr-[2px] inline-flex h-[32px] w-[32px] items-center justify-center rounded-full text-white" style={{ background: t.navy, fontSize: 22 }}>{team.no}</span>{team.suffix}
      </T>
      <T x={t.cx - 300} w={600} cy={cy2} size={size} align="center" className="font-extrabold" style={{ color: t.navy }}>{team.line}</T>
    </>
  )
}
