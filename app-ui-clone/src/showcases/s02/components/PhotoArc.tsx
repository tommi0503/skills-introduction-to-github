import { ImagePlaceholder } from '../../../ui'

interface ArcPhoto {
  x: number
  y: number
  d: number
}

interface PhotoArcProps {
  photos: ArcPhoto[]
  /** Dome that the photos fan around. */
  dome: { cx: number; top: number; r: number }
}

/** Fan of destination photo bubbles around a soft white dome (absolute, logical coords). */
export function PhotoArc({ photos, dome }: PhotoArcProps) {
  return (
    <>
      {photos.map((p, i) => (
        <ImagePlaceholder
          key={i}
          className="absolute rounded-full ring-[2px] ring-white"
          style={{ left: p.x - p.d / 2, top: p.y - p.d / 2, width: p.d, height: p.d }}
          label="destination photo"
        />
      ))}
      <div
        className="absolute rounded-full bg-[#f4f4f6] shadow-[0_-2px_10px_rgba(0,0,0,0.04)]"
        style={{ left: dome.cx - dome.r, top: dome.top, width: dome.r * 2, height: dome.r * 2 }}
      />
    </>
  )
}
