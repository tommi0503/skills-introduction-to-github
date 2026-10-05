import { ImagePlaceholder } from '../../../ui'
import type { Track } from '../data'
import { palette } from '../theme'

/** White track card: title + two-line description, cover art on the right. */
export function TrackCard({ track }: { track: Track }) {
  return (
    <div className="flex h-[106px] w-[326px] shrink-0 items-center rounded-[19px] bg-white pl-[17px] pr-[4px]">
      <div className="flex-1">
        <div className="text-[19.5px] font-bold leading-[24px] tracking-[-0.3px]" style={{ color: palette.ink }}>
          {track.title}
        </div>
        <div className="mt-[7px] text-[13px] leading-[20.5px]" style={{ color: palette.muted }}>
          {track.descriptionLines.map((l) => (
            <span key={l} className="block">
              {l}
            </span>
          ))}
        </div>
      </div>
      <ImagePlaceholder label={track.artLabel} className="h-[99px] w-[109px] rounded-[16px]" />
    </div>
  )
}
