import type { ReactNode } from 'react'
import { Abs, Slide } from '../../ui'
import { Box, Lines } from '../../ui'
import { band } from './data'
import { t } from './theme'

const RINGS = [122, 176, 230, 284, 338, 942, 996, 1050, 1104, 1158]
const stroke = `1.5px solid ${t.line}`

/** Desk-calendar page: rounded card with spiral rings, optional sage title band. */
export function CalendarSlide({ banded = false, light = false, children }: { banded?: boolean; light?: boolean; children: ReactNode }) {
  return (
    <Slide background={light ? t.bgLight : t.bg} className={t.sans} style={{ color: t.ink, ['--ly' as string]: '0.06em' }}>
      <Box x={50} y={36} w={1181} h={650} bg="#fdffff" className="rounded-[10px]" style={{ border: stroke }} />
      {banded && (
        <>
          <Box x={51} y={37} w={1179} h={55} bg={t.sage} className="rounded-t-[9px]" style={{ borderBottom: stroke }} />
          <Lines x={640} cy={63} align="center" size={16} className="tracking-[0.1em]" color="#f4fbfb" lines={[band]} />
        </>
      )}
      {RINGS.map((x) => <Box key={x} x={x - 6} y={16} w={12} h={44} bg="#dfe7e8" className="rounded-full" style={{ border: stroke }} />)}
      {children}
    </Slide>
  )
}

/** Numbered title bar: sage slanted tab + outlined box. */
export function TitleBar({ n, title }: { n: string; title: string }) {
  return (
    <>
      <Box x={98} y={103} w={1085} h={70} className="rounded-md" style={{ border: stroke }} />
      <Box x={98} y={103} w={98} h={70} bg={t.sage} style={{ clipPath: 'polygon(0 0, 100% 0, 68% 100%, 0 100%)' }} />
      <svg className="absolute left-0 top-0" width={1280} height={720}><line x1={196} y1={103} x2={165} y2={173} stroke={t.line} strokeWidth={1.5} /></svg>
      <Lines x={116} cy={137} size={34} className={t.latin} color="#fff" lines={[n]} />
      <Lines x={670} cy={138} align="center" size={42} className="font-medium tracking-[-0.02em]" color={t.ink} lines={[title]} />
    </>
  )
}

/** Small diagonal ticks at a card's corners (decorative). */
export function Ticks({ pts }: { pts: readonly (readonly [number, number])[] }) {
  return (
    <svg className="absolute left-0 top-0" width={1280} height={720}>
      {pts.map(([x, y], i) => <line key={i} x1={x} y1={y} x2={x + 16} y2={y + 15} stroke="#777" strokeWidth={1} />)}
    </svg>
  )
}

export const Card = ({ x, y, w, h, bg = t.card, children }: { x: number; y: number; w: number; h: number; bg?: string; children?: ReactNode }) => (
  <Box x={x} y={y} w={w} h={h} bg={bg}>{children}</Box>
)

export const Circle = ({ cx, cy, r, bg = '#fff', children }: { cx: number; cy: number; r: number; bg?: string; children?: ReactNode }) => (
  <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className="flex items-center justify-center rounded-full" style={{ background: bg, border: stroke }}>{children}</Abs>
)
