import { Star } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { StoreCart } from '../data'

export function StoreHeader({ store }: { store: StoreCart }) {
  return (
    <div className="flex items-center gap-[8px]">
      <ImagePlaceholder className="h-[43px] w-[43px] rounded-[8px]" tone={store.logoTone} label={`${store.name} logo`} />
      <div className="text-[#111]">
        <p className="text-[14.5px] leading-[18px] font-medium">{store.name}</p>
        <p className="flex items-center gap-[2px] text-[11.5px] leading-[15px]">
          {store.rating}
          <Star size={11.5} fill="currentColor" strokeWidth={0} />
          {store.reviews}
        </p>
      </div>
    </div>
  )
}
