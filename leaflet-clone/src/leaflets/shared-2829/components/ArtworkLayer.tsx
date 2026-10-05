import type { CSSProperties } from 'react'
import { ImagePlaceholder, Placed } from '../../../ui'

/** One illustration / graphic region that must stay a flat placeholder. */
export interface Artwork {
  label: string
  x: number
  y: number
  w: number
  h: number
  radius?: CSSProperties['borderRadius']
  clipPath?: string
  rotate?: number
  tone?: string
}

export interface ArtworkLayerProps {
  items: readonly Artwork[]
}

/** Renders artwork regions (leaves, hills, people…) as flat placeholders keeping their silhouette. */
export function ArtworkLayer({ items }: ArtworkLayerProps) {
  return (
    <>
      {items.map((a) => (
        <Placed key={a.label} x={a.x} y={a.y} width={a.w} height={a.h}>
          <ImagePlaceholder
            label={a.label}
            tone={a.tone}
            className="h-full w-full"
            style={{
              borderRadius: a.radius,
              clipPath: a.clipPath,
              transform: a.rotate ? `rotate(${a.rotate}deg)` : undefined,
            }}
          />
        </Placed>
      ))}
    </>
  )
}

/** Builds a polygon-shaped artwork region from absolute (sheet/panel) points. */
export function polygonArtwork(label: string, points: ReadonlyArray<readonly [number, number]>): Artwork {
  const xs = points.map((p) => p[0])
  const ys = points.map((p) => p[1])
  const x = Math.min(...xs)
  const y = Math.min(...ys)
  return {
    label,
    x,
    y,
    w: Math.max(...xs) - x,
    h: Math.max(...ys) - y,
    clipPath: `polygon(${points.map(([px, py]) => `${px - x}px ${py - y}px`).join(', ')})`,
  }
}
