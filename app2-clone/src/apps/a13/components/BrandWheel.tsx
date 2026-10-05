import { ImagePlaceholder } from '../../../ui'
import type { BrandTile } from '../data'

export interface BrandWheelProps {
  tiles: BrandTile[]
  /** Centre of the top tile (screen coords). */
  cx: number
  cy: number
  radius: number
  stepDeg: number
  size: number
}

/** Brand artwork tiles arranged on a wheel arc, rotated tangentially. */
export function BrandWheel({ tiles, cx, cy, radius, stepDeg, size }: BrandWheelProps) {
  const mid = (tiles.length - 1) / 2
  return (
    <>
      {tiles.map((t, i) => {
        const deg = (i - mid) * stepDeg
        const rad = (deg * Math.PI) / 180
        const x = cx + radius * Math.sin(rad)
        const y = cy + radius * (1 - Math.cos(rad))
        return (
          <ImagePlaceholder
            key={t.key}
            label={t.key}
            tone={t.tone}
            className="absolute rounded-[6px] shadow-[0_4px_10px_rgba(0,0,0,0.12)]"
            style={{ left: x - size / 2, top: y - size / 2, width: size, height: size, transform: `rotate(${deg}deg)` }}
          />
        )
      })}
    </>
  )
}
