import { ImagePlaceholder, cn } from '../../../ui'
import type { MenuItem } from '../data'
import { DiscountBar } from './DiscountBar'

/** Three menu photos side by side (bleeding off-screen) with captions, prices and a discount strip. */
export function MenuStrip({ menus, discount, className }: { menus: MenuItem[]; discount: string; className?: string }) {
  return (
    <div className={cn('overflow-hidden rounded-[8px]', className)}>
      <div className="flex gap-[2px]">
        {menus.map((m) => (
          <div key={m.key} className="relative h-[136px] w-[135px] shrink-0">
            <ImagePlaceholder label="menu photo" tone="#b8bcc2" className="h-full w-full" />
            <div className="absolute inset-x-[8px] bottom-[8px] text-white">
              <p className="truncate text-[11.5px] leading-[16px] tracking-[-0.3px] opacity-90">{m.caption}</p>
              <p className="flex items-baseline gap-[3px] whitespace-nowrap">
                <b className="text-[15.5px] font-bold">{m.price}</b>
                <s className="text-[11px] opacity-80">{m.was}</s>
              </p>
            </div>
          </div>
        ))}
      </div>
      <DiscountBar label={discount} size="md" className="h-[24px]" />
    </div>
  )
}
