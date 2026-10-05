import { Globe, Heart, ChevronRight, Star } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { Store } from '../data'
import { ue } from '../theme'
import { Tag } from './Tag'

export function StoreCard({ store, width }: { store: Store; width: number }) {
  return (
    <div className="shrink-0" style={{ width }}>
      <div className="relative">
        <ImagePlaceholder className="h-[132px] w-full rounded-[10px]" label={`${store.name} photo`} />
        {store.promo && (
          <Tag className="absolute top-[9px] left-[9px] h-[20px] text-[11.5px] text-white" style={{ background: ue.red }}>
            {store.promo}
          </Tag>
        )}
      </div>
      <div className="mt-[10px] flex items-center justify-between">
        <span className="text-[15.5px] leading-[20px] font-semibold tracking-[-0.2px]">{store.name}</span>
        {!store.promo && <Heart size={18} strokeWidth={1.4} color="#555" />}
      </div>
      <div className="mt-[1px] flex items-center gap-[3px] text-[11.5px] tracking-[-0.1px] whitespace-nowrap">
        <Globe size={12} strokeWidth={2.2} color={ue.teal} />
        <span style={{ color: ue.teal }}>{store.perk}</span>
        {store.eta && <span style={{ color: ue.muted }}>· {store.eta}</span>}
      </div>
      <div className="mt-[1px] flex items-center gap-[2px] text-[11.5px] tracking-[-0.1px] whitespace-nowrap">
        <span>{store.rating}</span>
        <Star size={12} fill={store.starColor} color={store.starColor} />
        <span style={{ color: ue.muted }}>{store.reviews}</span>
        <Tag className="ml-[5px] h-[19px] gap-[6px] font-medium" style={{ background: ue.greenBg, color: ue.green }}>
          {store.rank}
          <ChevronRight size={11} strokeWidth={2.4} />
        </Tag>
      </div>
    </div>
  )
}
