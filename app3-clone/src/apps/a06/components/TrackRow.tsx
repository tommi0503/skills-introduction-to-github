import { Ellipsis, SquarePlay } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { Track } from '../data'
import { sp } from '../theme'

export function TrackRow({ track, index }: { track: Track; index: number }) {
  return (
    <div className="flex h-[63.5px] items-center pr-[18px]">
      <span className="w-[41px] pl-[19px] text-[12px]" style={{ color: sp.white }}>
        {index}
      </span>
      <ImagePlaceholder className="h-[48px] w-[48px] rounded-[3px]" label={`${track.title} cover`} />
      <div className="ml-[12px] flex-1">
        <div className="text-[15px] leading-[19px]" style={{ color: sp.white }}>
          {track.title}
        </div>
        <div className="mt-[4px] flex items-center gap-[4px] text-[12.5px]" style={{ color: sp.muted }}>
          {track.video && (
            <>
              <SquarePlay size={11} strokeWidth={2} /> Video ·
            </>
          )}
          {track.plays}
        </div>
      </div>
      <Ellipsis size={18} color={sp.muted} />
    </div>
  )
}
