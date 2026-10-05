import type { CSSProperties } from 'react'
import { ImagePlaceholder, Placed } from '../../ui'

/** A positioned artwork region (mascot, photo, graphic) rendered as a flat placeholder. */
export interface ShapeSpec {
  x: number
  y: number
  w: number
  h: number
  /** CSS border-radius (e.g. '50%', 16, '999px 999px 0 0'). */
  radius?: CSSProperties['borderRadius']
  /** CSS clip-path for non-rectangular silhouettes. */
  clip?: string
  tone?: string
  label?: string
}

export function Shape({ x, y, w, h, radius, clip, tone, label }: ShapeSpec) {
  return (
    <Placed x={x} y={y} width={w} height={h}>
      <ImagePlaceholder
        className="h-full w-full"
        tone={tone}
        label={label}
        style={{ borderRadius: radius, clipPath: clip }}
      />
    </Placed>
  )
}

export function Shapes({ items }: { items: readonly ShapeSpec[] }) {
  return (
    <>
      {items.map((s, i) => (
        <Shape key={i} {...s} />
      ))}
    </>
  )
}
