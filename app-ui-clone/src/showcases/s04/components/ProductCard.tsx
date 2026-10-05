import { Plus } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { Product } from '../data'
import { theme } from '../theme'

export function ProductCard({ product }: { product: Product }) {
  return (
    <div className="w-[166px] rounded-[9px] border border-[#ececec] bg-white p-[4px]">
      <div className="relative h-[101px]">
        <ImagePlaceholder label={`${product.name} photo`} className="h-full w-full rounded-[6px]" />
        <span className="absolute right-[7px] bottom-[7px] flex h-[26px] w-[26px] items-center justify-center rounded-full bg-white/35 text-white">
          <Plus size={18} strokeWidth={2} />
        </span>
      </div>
      <p className="px-[7px] pt-[9px] text-[14.5px] text-[#1c1c1c]">{product.name}</p>
      <p className="flex items-baseline gap-[5px] px-[7px] pt-[1px] pb-[6px]">
        <span className="text-[15.5px]" style={{ color: theme.accent }}>
          {product.price}
        </span>
        {product.oldPrice && <s className="text-[13.5px] text-[#9a9a9a]">{product.oldPrice}</s>}
      </p>
    </div>
  )
}
