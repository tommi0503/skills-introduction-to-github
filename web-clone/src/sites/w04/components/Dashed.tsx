import type { CSSProperties } from 'react'
import { theme } from '../theme'

const dash = (dir: 'to bottom' | 'to right') =>
  `repeating-linear-gradient(${dir}, ${theme.color.line} 0 16px, transparent 16px 32px)`

/** 1px dashed guide line (16px dash, 16px gap) positioned absolutely. */
export function DashedLine({ vertical, style }: { vertical?: boolean; style: CSSProperties }) {
  return (
    <div
      aria-hidden
      className="absolute"
      style={{ background: dash(vertical ? 'to bottom' : 'to right'), ...(vertical ? { width: 1 } : { height: 1 }), ...style }}
    />
  )
}

/** Small square handle drawn on the corners of bordered panels. */
export function Corner({ x, y }: { x: number; y: number }) {
  return (
    <div
      aria-hidden
      className="absolute size-[9px] rounded-[2px] border bg-white"
      style={{ left: x - 4, top: y - 4, borderColor: theme.color.border }}
    />
  )
}

/** Four corner handles for a box. */
export function Corners({ x, y, w, h }: { x: number; y: number; w: number; h: number }) {
  return (
    <>
      <Corner x={x} y={y} />
      <Corner x={x + w} y={y} />
      <Corner x={x} y={y + h} />
      <Corner x={x + w} y={y + h} />
    </>
  )
}
