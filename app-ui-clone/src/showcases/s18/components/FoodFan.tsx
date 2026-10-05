import { ImagePlaceholder } from '../../../ui'
import type { FanCard } from '../data'

/** Dish photos splayed like a hand of cards; later entries sit on top. */
export function FoodFan({ cards, width = 390 }: { cards: FanCard[]; width?: number }) {
  return (
    <div className="relative h-[100px]" style={{ width }}>
      {cards.map((c, i) => (
        <ImagePlaceholder
          key={i}
          className="absolute rounded-[12px] border-[2px] border-[#5d9bf5]"
          style={{ left: width / 2 + c.dx - c.w / 2, top: c.top, width: c.w, height: c.h, transform: `rotate(${c.rotate}deg)` }}
          label="dish photo"
        />
      ))}
    </div>
  )
}
