import { ImagePlaceholder, Placed } from '../../../ui'

export interface PhotoBox {
  label: string
  x: number
  y: number
  w: number
  h: number
  /** Arch-topped photo: vertical height of the rounded top (horizontal radius = half the width). */
  archRise?: number
}

/** Photo slot rendered as a flat placeholder, keeping its shape. */
export function Photo({ box }: { box: PhotoBox }) {
  return (
    <Placed x={box.x} y={box.y} width={box.w} height={box.h}>
      <ImagePlaceholder
        label={box.label}
        className="h-full w-full"
        style={box.archRise ? { borderRadius: `${box.w / 2}px ${box.w / 2}px 0 0 / ${box.archRise}px ${box.archRise}px 0 0` } : undefined}
      />
    </Placed>
  )
}
