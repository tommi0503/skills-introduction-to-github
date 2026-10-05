import { ImagePlaceholder } from '../../../ui'
import type { Category } from '../data'

/** Horizontal row of 3D category icons (placeholders) with labels. */
export function CategoryRail({ items, className }: { items: Category[]; className?: string }) {
  return (
    <div className={className}>
      <div className="flex" style={{ gap: 0 }}>
        {items.map((c) => (
          <div key={c.key} className="flex w-[53.5px] flex-col items-center">
            <ImagePlaceholder label={`${c.label} icon`} tone="#d3d6da" className="h-[32px] w-[32px] rounded-[9px]" />
            <span className="mt-[10px] text-[12px] font-semibold leading-none text-[#222]">{c.label}</span>
          </div>
        ))}
      </div>
    </div>
  )
}
