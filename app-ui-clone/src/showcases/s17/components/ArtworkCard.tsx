import { ImagePlaceholder } from '../../../ui'
import type { Artwork } from '../data'
import { theme } from '../theme'

/** "For You" tile: artwork, title, artist, medium and price. */
export function ArtworkCard({ art }: { art: Artwork }) {
  return (
    <div className="h-[406px] w-[233px] shrink-0 px-[26.5px] pt-[26.5px]" style={{ background: theme.card }}>
      <ImagePlaceholder className="h-[269px] w-[179px]" label={art.title} />
      <div className="mt-[18px] truncate text-[15px] leading-[19px] font-semibold text-[#111]">{art.title}</div>
      <div className="mt-[3px] truncate text-[12.5px]" style={{ color: theme.muted }}>
        {art.artist}
      </div>
      <div className="mt-[2px] truncate text-[7px]" style={{ color: theme.muted }}>
        {art.medium}
      </div>
      <div className="mt-[4px] text-[16px] font-semibold text-[#111]">{art.price}</div>
    </div>
  )
}
