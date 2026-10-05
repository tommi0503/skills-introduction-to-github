import { Camera } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { GalleryTile } from '../data'
import { ig } from '../theme'

function SelectBadge({ order }: { order?: number }) {
  return order ? (
    <span className="absolute top-[5px] right-[5px] flex h-[25px] w-[25px] items-center justify-center rounded-full bg-white text-[14px] font-semibold text-black">
      {order}
    </span>
  ) : (
    <span className="absolute top-[5px] right-[5px] h-[25px] w-[25px] rounded-full border-[1.5px] border-white/80 bg-white/20" />
  )
}

/** 4-column media picker grid with selection-order badges. */
export function GalleryGrid({ tiles }: { tiles: GalleryTile[] }) {
  return (
    <div className="grid grid-cols-4 gap-[1.5px]">
      {tiles.map((t) =>
        t.camera ? (
          <div key={t.key} className="flex aspect-square items-center justify-center bg-[#29282c] text-[#77767a]">
            <Camera size={28} strokeWidth={1.6} fill="currentColor" stroke="#29282c" />
          </div>
        ) : (
          <div key={t.key} className="relative aspect-square">
            <ImagePlaceholder tone={ig.photoOnDark} className="h-full w-full" label={t.key} />
            <SelectBadge order={t.order} />
          </div>
        ),
      )}
    </div>
  )
}
