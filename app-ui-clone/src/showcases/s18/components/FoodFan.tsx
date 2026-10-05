import { ImagePlaceholder } from '../../../ui'

export interface FoodFanProps {
  /** Rotation of each photo in degrees, left to right. */
  angles: number[]
  width?: number
  height?: number
  /** Distance from a card's top to the common pivot below the fan. */
  pivot?: number
}

/** Photos splayed like a hand of cards around a pivot under the centre. */
export function FoodFan({ angles, width = 64, height = 92, pivot = 430 }: FoodFanProps) {
  const mid = (angles.length - 1) / 2
  return (
    <div className="relative" style={{ width, height }}>
      {angles.map((a, i) => (
        <ImagePlaceholder
          key={i}
          className="absolute top-0 left-0 rounded-[12px] border-[1.5px] border-[#5d9bf5]"
          style={{
            width,
            height,
            transformOrigin: `50% ${pivot}px`,
            transform: `rotate(${a}deg)`,
            zIndex: 10 - Math.abs(i - mid),
          }}
          label="dish photo"
        />
      ))}
    </div>
  )
}
