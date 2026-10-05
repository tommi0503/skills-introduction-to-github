import { Crown, Heart } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'
import type { Product } from '../data'
import { theme } from '../theme'
import { TagPill } from './TagPill'

export interface ProductCardProps {
  product: Product
  width: number
  imageHeight: number
  /** Typographic scale: compact for carousels, regular for grids. */
  size?: 'compact' | 'regular'
  textInset?: number
  className?: string
}

export function ProductCard({ product: p, width, imageHeight, size = 'compact', textInset = 0, className }: ProductCardProps) {
  const big = size === 'regular'
  return (
    <div className={cn('shrink-0', className)} style={{ width }}>
      <div className="relative" style={{ height: imageHeight }}>
        <ImagePlaceholder label="product photo" className="absolute inset-0" />
        <Heart
          className="absolute"
          style={{ right: big ? 12 : 9, bottom: big ? 10 : 8 }}
          size={big ? 24 : 21}
          strokeWidth={1.6}
          color={p.liked ? theme.up : '#fff'}
          fill={p.liked ? theme.up : 'transparent'}
        />
        {p.express && (
          <span className="absolute bottom-0 left-0 flex h-[25px] items-center px-[6px] text-[10.5px] font-semibold text-white" style={{ background: theme.express }}>
            직진배송
          </span>
        )}
      </div>
      <div style={{ paddingLeft: textInset, paddingRight: textInset }}>
        <div className={cn('flex items-center gap-[4px] font-semibold text-[#222]', big ? 'mt-[11px] text-[13.5px] leading-[18px]' : 'mt-[9px] text-[12.5px] leading-[17px]')}>
          {p.store}
          {p.crown && <Crown size={11} fill="#f5c542" color="#f5c542" />}
          {p.ad && <span className="rounded-[3px] border border-[#e5e5e5] px-[3px] text-[8.5px] leading-[12px] text-[#bbb]">AD</span>}
        </div>
        <div className={cn('truncate text-[#444]', big ? 'mt-[5px] text-[13.5px] leading-[18px]' : 'mt-[4px] text-[12.5px] leading-[17px]')}>{p.name}</div>
        <div className={cn('flex items-baseline gap-[4px] font-bold whitespace-nowrap', big ? 'mt-[3px] text-[17px] leading-[24px]' : 'mt-[2px] text-[15px] leading-[22px]')}>
          {p.discount && <span style={{ color: theme.pink }}>{p.discount}</span>}
          <span className="text-[#111]">{p.price}</span>
        </div>
        {p.tags && (
          <div className={cn('flex gap-[4px]', big ? 'mt-[5px]' : 'mt-[3px]')}>
            {p.tags.map((t) => (
              <TagPill key={t.label} tag={t} compact={!big} />
            ))}
          </div>
        )}
        {p.colors && (
          <div className="mt-[7px] flex items-center gap-[4px]">
            {p.colors.map((c) => (
              <span key={c} className="h-[8px] w-[8px] rounded-full border border-[#e5e5e5]" style={{ background: c }} />
            ))}
            {p.moreColors && <span className="text-[10px] text-[#888]">+{p.moreColors}</span>}
          </div>
        )}
        {p.meta && <div className="mt-[6px] text-[11px] text-[#b0b0b4]">{p.meta}</div>}
      </div>
    </div>
  )
}
