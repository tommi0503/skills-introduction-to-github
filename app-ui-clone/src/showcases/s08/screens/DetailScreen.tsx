import { ChevronLeft, ChevronRight, Heart, Share2, Star } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { Box } from '../../shared-canvas/Box'
import { Eyebrow } from '../components/Eyebrow'
import { OverlayButton } from '../components/OverlayButton'
import { Price } from '../components/Price'
import { SellerAvatar } from '../components/SellerAvatar'
import { SpecTile } from '../components/SpecTile'
import { listing } from '../data'
import { theme } from '../theme'

function PageDots({ count, active }: { count: number; active: number }) {
  return (
    <div className="flex gap-[5px]">
      {Array.from({ length: count }, (_, i) => (
        <span key={i} className="h-[6px] w-[6px] rounded-full" style={{ background: i === active ? '#fff' : 'rgba(255,255,255,0.5)' }} />
      ))}
    </div>
  )
}

function SellerRow() {
  const { seller } = listing
  return (
    <div className="flex h-full items-center rounded-[10px] border bg-[#fbf8ef] pr-[18px] pl-[13px]" style={{ borderColor: theme.hairline }}>
      <SellerAvatar size={43} ring={0} badgeSide="right" />
      <div className="ml-[11px] flex-1">
        <div className="font-dm text-[16.5px] leading-[20px] font-medium" style={{ color: theme.ink }}>
          {seller.name}
        </div>
        <div className="mt-[2px] flex items-center gap-[8px] font-dm text-[13px] leading-[16px]" style={{ color: theme.muted }}>
          <Star size={12} fill="#f2b632" stroke="#f2b632" />
          <span>{seller.rating}</span>
          <span>•</span>
          <span>{seller.sales}</span>
        </div>
      </div>
      <ChevronRight size={16} strokeWidth={2} color={theme.muted} />
    </div>
  )
}

/** Listing detail. */
export function DetailScreen() {
  return (
    <div className="absolute inset-0" style={{ background: theme.bg }}>
      <Box rect={{ x: 0, y: 0, w: 375, h: 407 }}>
        <ImagePlaceholder label="teak sideboard" className="h-full w-full" />
      </Box>
      <Box rect={{ x: 13, y: 13.5, w: 38.5, h: 38.5 }}>
        <OverlayButton icon={ChevronLeft} size={38.5} iconSize={20} />
      </Box>
      <Box rect={{ x: 277, y: 13.5, w: 85, h: 38.5 }} className="flex gap-[6px]">
        <OverlayButton icon={Share2} size={38.5} iconSize={18} />
        <OverlayButton icon={Heart} size={38.5} iconSize={19} />
      </Box>
      <Box rect={{ x: 178, y: 386, w: 30, h: 6 }}>
        <PageDots count={listing.photos} active={0} />
      </Box>

      <Box rect={{ x: 21, y: 432, w: 330, h: 12 }}>
        <Eyebrow>{listing.tag}</Eyebrow>
      </Box>
      <Box rect={{ x: 21, y: 453, w: 340, h: 28 }} className="font-dm text-[22.6px] leading-[28px] font-medium tracking-[-0.01em]">
        <span style={{ color: theme.ink }}>{listing.title}</span>
      </Box>
      <Box rect={{ x: 21, y: 494, w: 340, h: 44 }} className="flex items-end gap-[9px]">
        <Price className="text-[39px] leading-[44px]">{listing.price}</Price>
        <span className="pb-[4.5px] font-dm text-[13px]" style={{ color: theme.muted }}>
          {listing.pickup}
        </span>
      </Box>

      <Box rect={{ x: 21, y: 555, w: 332, h: 91 }} className="flex gap-[15px]">
        {listing.specs.map((s) => (
          <SpecTile key={s.label} label={s.label} value={s.value} />
        ))}
      </Box>

      <Box rect={{ x: 23, y: 677.5, w: 330, h: 74 }}>
        <SellerRow />
      </Box>

      <Box rect={{ x: 0, y: 734, w: 375, h: 90 }} className="flex gap-[12px] border-t px-[14px] pt-[16px]" style={{ background: theme.bg, borderColor: theme.hairline }}>
        <span className="flex h-[52px] w-[111px] items-center justify-center rounded-[6px] font-dm text-[15px] font-medium" style={{ background: '#e8e4d9', color: theme.ink }}>
          {listing.actions.secondary}
        </span>
        <span className="flex h-[52px] flex-1 items-center justify-center rounded-[6px] font-dm text-[15px] font-medium text-white" style={{ background: theme.accent }}>
          {listing.actions.primary}
        </span>
      </Box>
    </div>
  )
}
