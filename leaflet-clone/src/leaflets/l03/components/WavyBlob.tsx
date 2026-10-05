import { ImagePlaceholder } from '../../../ui'

interface WavyBlobProps {
  width: number
  height: number
  /** Approximate scallop length along the edges (px). */
  step: number
  /** Inset of the scallop chord line from the bounding box (≈ bulge depth). */
  depth: number
  label?: string
}

/** Builds a clockwise rectangle outline whose edges are made of outward-bulging arcs. */
export function scallopPath(w: number, h: number, step: number, depth: number): string {
  const d = depth
  const corners: Array<[number, number]> = [
    [d, d],
    [w - d, d],
    [w - d, h - d],
    [d, h - d],
  ]
  let path = `M ${d} ${d}`
  for (let i = 0; i < 4; i++) {
    const [x0, y0] = corners[i]
    const [x1, y1] = corners[(i + 1) % 4]
    const len = Math.hypot(x1 - x0, y1 - y0)
    const n = Math.max(1, Math.round(len / step))
    const half = len / n / 2
    const angle = (Math.atan2(y1 - y0, x1 - x0) * 180) / Math.PI
    for (let k = 1; k <= n; k++) {
      const x = x0 + ((x1 - x0) * k) / n
      const y = y0 + ((y1 - y0) * k) / n
      path += ` A ${half.toFixed(1)} ${d} ${angle.toFixed(0)} 0 1 ${x.toFixed(1)} ${y.toFixed(1)}`
    }
  }
  return path + ' Z'
}

/** Wavy cream "cloud" shape — artwork, so rendered as a flat placeholder clipped to its silhouette. */
export function WavyBlob({ width, height, step, depth, label = 'wavy blob' }: WavyBlobProps) {
  return (
    <ImagePlaceholder
      label={label}
      style={{ width, height, clipPath: `path('${scallopPath(width, height, step, depth)}')` }}
    />
  )
}
