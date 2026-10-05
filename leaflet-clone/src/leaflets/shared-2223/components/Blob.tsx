import type { CSSProperties } from 'react'
import { ImagePlaceholder } from '../../../ui'

export interface BlobShape {
  id: string
  x: number
  y: number
  width: number
  height: number
  /** border-radius for the organic silhouette (default: ellipse). */
  radius?: string
  rotate?: number
  label: string
}

export interface BlobProps {
  shape: BlobShape
  style?: CSSProperties
}

/** Decorative artwork (vegetables, blobs, squiggles) kept as a flat placeholder silhouette. */
export function Blob({ shape, style }: BlobProps) {
  return (
    <ImagePlaceholder
      label={shape.label}
      className="absolute"
      style={{
        left: shape.x,
        top: shape.y,
        width: shape.width,
        height: shape.height,
        borderRadius: shape.radius ?? '50%',
        transform: shape.rotate ? `rotate(${shape.rotate}deg)` : undefined,
        ...style,
      }}
    />
  )
}
