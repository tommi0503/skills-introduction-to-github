import { ImagePlaceholder, Placed } from '../../../ui'
import { ground, library } from '../theme'

/** A piece of artwork (hill, bush, building, character) standing on / over the ground band. */
export interface ArtShape {
  key: string
  x: number
  y: number
  w: number
  h: number
  /** CSS border-radius to keep the silhouette (e.g. '60px 60px 0 0'). */
  radius?: string
  /** Paint above other sheet content. */
  front?: boolean
}

interface GroundBandProps {
  sheetWidth: number
  sheetHeight: number
  shapes: ArtShape[]
}

/** Sheet-wide green ground with its outlined top edge; hills/buildings are flat placeholders. */
export function GroundBand({ sheetWidth, sheetHeight, shapes }: GroundBandProps) {
  return (
    <>
      <Placed
        x={0}
        y={ground.top}
        width={sheetWidth}
        height={sheetHeight - ground.top}
        style={{ background: library.green, borderTop: `${ground.line}px solid ${library.ink}` }}
      />
      {shapes
        .filter((s) => !s.front)
        .map((s) => (
          <ArtPlaceholder key={s.key} shape={s} />
        ))}
    </>
  )
}

export function ArtPlaceholder({ shape }: { shape: ArtShape }) {
  return (
    <Placed x={shape.x} y={shape.y} width={shape.w} height={shape.h}>
      <ImagePlaceholder label={shape.key} className="h-full w-full" style={{ borderRadius: shape.radius }} />
    </Placed>
  )
}
