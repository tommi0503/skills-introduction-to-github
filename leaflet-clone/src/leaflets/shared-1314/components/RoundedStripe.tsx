import type { CSSProperties } from 'react'

export interface StripeLayer {
  color: string
  /** Thickness of this ring in px. */
  width: number
}

export interface RoundedStripeProps {
  /** Outer box of the stripe (panel coordinates). The left end runs off the panel edge. */
  x: number
  y: number
  width: number
  height: number
  /** Rings from the outside in; the remaining interior is painted with `fill`. */
  layers: StripeLayer[]
  fill: string
  style?: CSSProperties
}

/**
 * Concentric capsule made of nested rounded strokes — the ornamental "stripes" ornament.
 * Each ring is a nested box with a fully rounded right side.
 */
export function RoundedStripe({ x, y, width, height, layers, fill, style }: RoundedStripeProps) {
  const rings = [...layers.map((l) => l.color), fill]
  let inset = 0
  const boxes = rings.map((color, i) => {
    const box = { color, inset }
    inset += layers[i]?.width ?? 0
    return box
  })
  return (
    <div className="absolute" style={{ left: x, top: y, width, height, ...style }}>
      {boxes.map(({ color, inset: d }, i) => (
        <div
          key={i}
          className="absolute"
          style={{
            left: -d - 40,
            top: d,
            right: d,
            bottom: d,
            background: color,
            borderRadius: `0 ${height}px ${height}px 0`,
          }}
        />
      ))}
    </div>
  )
}
