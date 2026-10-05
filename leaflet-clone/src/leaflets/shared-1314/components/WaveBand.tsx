import { ImagePlaceholder } from '../../../ui'

export interface WaveBandProps {
  x: number
  y: number
  width: number
  height: number
  /** Optional solid strip drawn on top of the pattern (flat band edge). */
  strip?: { color: string; height: number }
  /** Scalloped top edge: diameter of each scallop and its horizontal period. */
  scallop?: { size: number; period: number; offset?: number }
}

/** Wave/scale pattern band along the bottom — the pattern itself is artwork, so it is a placeholder. */
export function WaveBand({ x, y, width, height, strip, scallop }: WaveBandProps) {
  const top = strip?.height ?? (scallop ? scallop.size / 2 : 0)
  const count = scallop ? Math.ceil((width + scallop.size) / scallop.period) + 1 : 0
  return (
    <div className="absolute overflow-hidden" style={{ left: x, top: y, width, height }}>
      <ImagePlaceholder className="absolute inset-x-0 bottom-0" style={{ top }} label="wave pattern" />
      {scallop &&
        Array.from({ length: count }, (_, i) => (
          <ImagePlaceholder
            key={i}
            className="absolute rounded-full"
            style={{ left: (scallop.offset ?? 0) + i * scallop.period - scallop.size / 2, top: 0, width: scallop.size, height: scallop.size }}
          />
        ))}
      {strip && <div className="absolute inset-x-0 top-0" style={{ height: strip.height, background: strip.color }} />}
    </div>
  )
}
