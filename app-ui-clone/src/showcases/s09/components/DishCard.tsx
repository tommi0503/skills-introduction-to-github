import { ImagePlaceholder } from '../../../ui'
import type { Dish } from '../data'
import { theme } from '../theme'

/** Recommended dish tile: round bowl photo, two-line name and price. */
export function DishCard({ dish, height = 200 }: { dish: Dish; height?: number }) {
  return (
    <div className="relative rounded-[13px] bg-white" style={{ height }}>
      <ImagePlaceholder label={dish.key} className="absolute top-[14px] left-1/2 h-[122px] w-[122px] -translate-x-1/2 rounded-full" />
      <div className="absolute inset-x-[14px] top-[152px] flex items-end justify-between font-poppins text-[13px] leading-[18px] font-medium" style={{ color: theme.ink }}>
        <div>
          {dish.name.map((l) => (
            <div key={l}>{l}</div>
          ))}
        </div>
        <span>{dish.price}</span>
      </div>
    </div>
  )
}
