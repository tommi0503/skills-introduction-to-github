import { ImagePlaceholder, cn } from '../../../ui'
import type { StoreBrand } from '../data'

/** Round store logos (placeholders) with promo badges and names; overflows to the right. */
export function BrandRail({ items, className }: { items: StoreBrand[]; className?: string }) {
  return (
    <div className={cn('flex gap-[11px]', className)}>
      {items.map((b) => (
        <div key={b.key} className="relative flex w-[57px] shrink-0 flex-col items-center">
          <ImagePlaceholder label={`${b.label} logo`} className="h-[57px] w-[57px] rounded-full" />
          {b.badge && (
            <span className="absolute -top-[8px] whitespace-nowrap rounded-full border border-[#d9dcf5] bg-white px-[5px] text-[9.5px] leading-[15px] text-[#3b3f9a]">
              {b.badge}
            </span>
          )}
          <span className="mt-[6px] whitespace-nowrap text-[12.5px] leading-none tracking-[-0.3px] text-[#333]">{b.label}</span>
        </div>
      ))}
    </div>
  )
}
