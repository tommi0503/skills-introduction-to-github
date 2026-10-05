import { Heart } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { Product } from '../data'
import { theme } from '../theme'
import { Eyebrow } from './Eyebrow'
import { Price } from './Price'
import { SellerAvatar } from './SellerAvatar'

/** Marketplace tile: photo (+ optional save button) with seller avatar, tag, title and price. */
export function ProductCard({ product, showSave = false }: { product: Product; showSave?: boolean }) {
  return (
    <div className="relative overflow-hidden rounded-[9px]" style={{ height: product.height, background: theme.surface }}>
      <div className="relative" style={{ height: product.imageHeight }}>
        <ImagePlaceholder label={product.id} className="h-full w-full" />
        {showSave && (
          <span
            className="absolute top-[9px] right-[8px] flex h-[29px] w-[29px] items-center justify-center rounded-full"
            style={{ background: 'rgba(205,200,192,0.85)', color: theme.ink }}
          >
            <Heart size={16.5} strokeWidth={1.9} />
          </span>
        )}
        <div className="absolute bottom-[6px] left-[8px]">
          <SellerAvatar size={27} />
        </div>
      </div>
      <div className="px-[11px] pt-[10px]">
        <Eyebrow>{product.tag}</Eyebrow>
        <div className="mt-[4.5px] font-figtree text-[14px] leading-[17px] font-[460] tracking-[-0.005em] whitespace-nowrap" style={{ color: theme.ink }}>
          {product.title.map((l) => (
            <div key={l}>{l}</div>
          ))}
        </div>
        <Price className="mt-[10px] text-[22px] leading-[26px]">{product.price}</Price>
      </div>
    </div>
  )
}
