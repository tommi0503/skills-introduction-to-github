import { ImagePlaceholder } from '../../../ui'
import type { MediaCardData } from '../data'
import { sp } from '../theme'

export function MediaCard({ item, size = 144 }: { item: MediaCardData; size?: number }) {
  return (
    <div className="shrink-0" style={{ width: size }}>
      <ImagePlaceholder className="rounded-[3px]" style={{ width: size, height: size }} label={`${item.title} cover`} />
      <div className="mt-[10px] truncate text-[11.5px] leading-[16px]" style={{ color: sp.muted }}>
        {item.overline}
      </div>
      <div className="mt-[3px] truncate text-[12px] leading-[16px] font-bold" style={{ color: sp.white }}>
        {item.title}
      </div>
      <div className="mt-[4px] truncate text-[11.5px] leading-[16px]" style={{ color: sp.muted }}>
        {item.subtitle}
      </div>
    </div>
  )
}
