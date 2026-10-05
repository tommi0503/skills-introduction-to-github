import type { Nutrient } from '../data'
import { theme } from '../theme'

const columns = [0, 71.6, 165.3, 242.4]

/** Four nutrient figures with captions, on fixed column offsets. */
export function NutritionRow({ items }: { items: Nutrient[] }) {
  return (
    <div className="relative h-[38px]">
      {items.map((n, i) => (
        <div key={n.label} className="absolute top-0" style={{ left: columns[i] }}>
          <div className="font-poppins text-[16px] leading-[22px] font-semibold" style={{ color: theme.ink }}>
            {n.value}
          </div>
          <div className="font-poppins text-[11.8px] leading-[16px]" style={{ color: theme.muted }}>
            {n.label}
          </div>
        </div>
      ))}
    </div>
  )
}
