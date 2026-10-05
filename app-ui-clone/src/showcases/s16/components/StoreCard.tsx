import { ImagePlaceholder } from '../../../ui'
import type { Store } from '../data'
import { theme } from '../theme'

/** Featured-store tile: glyph, name and perk. */
export function StoreCard({ store }: { store: Store }) {
  const Icon = store.icon
  return (
    <div className="h-[127px] rounded-[18px] bg-white px-[15px] pt-[16px]">
      <div className="flex h-[26px] w-[26px] items-center justify-center">
        {Icon ? <Icon size={25} strokeWidth={1.4} /> : <ImagePlaceholder className="h-[24px] w-[24px] rounded-[4px]" label={`${store.name} logo`} />}
      </div>
      <div className="mt-[26px] text-[18px] leading-[22px] font-[450] tracking-[-0.3px]" style={{ color: theme.ink }}>
        {store.name}
      </div>
      <div className="mt-[3px] text-[12px]" style={{ color: '#808080' }}>
        {store.perk}
      </div>
    </div>
  )
}
