import type { CSSProperties } from 'react'
import { ImagePlaceholder } from '../../../ui'
import type { MascotSpec } from '../data'

/** Character illustration slot — a flat placeholder in the mascot's silhouette box. */
export function Mascot({ spec, style }: { spec: MascotSpec; style?: CSSProperties }) {
  return (
    <ImagePlaceholder
      label="mascot"
      style={{ width: spec.w, height: spec.h, borderRadius: spec.radius, ...style }}
    />
  )
}
