import { Heart } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { GridProduct } from '../data'
import { PriceTag } from './PriceTag'
import { SwatchStack } from './SwatchStack'

interface ProductTileProps {
  product: GridProduct
}

/** Grid product: photo with favourite + colour overlays, then name and daily price. */
export function ProductTile({ product }: ProductTileProps) {
  return (
    <div className="w-[164px]">
      <div className="relative h-[179px] overflow-hidden rounded-[6px]">
        <ImagePlaceholder className="h-full w-full" label={product.name} />
        <div className="absolute top-[10px] right-[10px] flex h-[21px] w-[21px] items-center justify-center rounded-full bg-white">
          <Heart size={12} strokeWidth={2.2} className="text-[#111]" />
        </div>
        <div className="absolute right-[6px] bottom-[6px]">
          <SwatchStack colors={product.colors} />
        </div>
      </div>
      <div className="mt-[11px] truncate text-[13px] font-semibold tracking-[-0.1px] text-[#1c1c1c]">{product.name}</div>
      <PriceTag price={product.price} className="mt-[-1px] text-[12px] text-[#7d7d7d]" unitClassName="text-[9.5px]" />
    </div>
  )
}
