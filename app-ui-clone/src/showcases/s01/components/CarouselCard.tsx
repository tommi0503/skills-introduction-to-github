import { ImagePlaceholder } from '../../../ui'
import type { CarouselProduct } from '../data'
import { PriceTag } from './PriceTag'
import { SwatchDot } from './SwatchDot'

interface CarouselCardProps {
  product: CarouselProduct
}

/** Home "new arrivals" card: photo, name, price, size chips and colour dots. */
export function CarouselCard({ product }: CarouselCardProps) {
  return (
    <div
      className="h-[271px] w-[186px] shrink-0 rounded-[8px] px-[6px] pt-[8px]"
      style={{ background: 'linear-gradient(to bottom, #faf7f2 0%, #f3f0ea 60%, #ecebe8 100%)' }}
    >
      <ImagePlaceholder className="h-[161px] w-full rounded-[4px]" label={product.name} />
      <div className="px-[10px] pt-[13px] text-[#1c1c1c]">
        <div className="truncate text-[13px] font-medium tracking-[-0.1px] text-[#111]">{product.name}</div>
        <PriceTag price={product.price} className="mt-[0px] text-[12px] font-bold" unitClassName="text-[9.5px] text-[#8f8f8f]" />
        <div className="mt-[11px] flex items-center gap-[5px] text-[8.5px] text-[#a3a3a3]">
          <span className="mr-[1px]">Sizes -</span>
          {product.sizes.map((s) => (
            <span key={s} className="rounded-[3px] bg-[#f6f6f6] px-[5px] py-[2px] leading-none">
              {s}
            </span>
          ))}
        </div>
        <div className="mt-[6px] flex items-center gap-[4px] text-[8.5px] text-[#a3a3a3]">
          <span className="mr-[2px]">Color -</span>
          {product.colors.map((c) => (
            <SwatchDot key={c.color} swatch={c} size={8} />
          ))}
        </div>
      </div>
    </div>
  )
}
