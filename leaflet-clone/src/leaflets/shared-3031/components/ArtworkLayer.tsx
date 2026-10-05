import type { CSSProperties } from 'react'
import { ImagePlaceholder, Placed } from '../../../ui'

/** One character illustration / graphic region kept as a flat placeholder. */
export interface Artwork {
  label: string
  x: number
  y: number
  w: number
  h: number
  radius?: CSSProperties['borderRadius']
  clipPath?: string
}

/** Renders illustration regions as flat placeholders preserving their silhouette. */
export function ArtworkLayer({ items }: { items: readonly Artwork[] }) {
  return (
    <>
      {items.map((a) => (
        <Placed key={a.label} x={a.x} y={a.y} width={a.w} height={a.h}>
          <ImagePlaceholder label={a.label} className="h-full w-full" style={{ borderRadius: a.radius, clipPath: a.clipPath }} />
        </Placed>
      ))}
    </>
  )
}
