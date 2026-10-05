import { Bookmark, Check, ChevronDown } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { place } from '../data'
import { theme } from '../theme'
import { RoundToggle } from './RoundToggle'

/** Name, saves badge, tags, rank and opening hours of a place. */
export function PlaceHeader() {
  return (
    <div className="relative h-[136px]">
      <div className="absolute left-[7px] top-[20px] flex items-center gap-[3px]">
        <ImagePlaceholder label="croissant" tone="#e9cf9e" className="h-[22px] w-[22px] rounded-full" />
        <h1 className="a05-wide text-[19px] font-extrabold uppercase leading-none tracking-[-0.9px]" style={{ color: theme.ink, fontStretch: '108%' }}>
          {place.name}
        </h1>
      </div>
      <div className="absolute right-[18px] top-[12px] flex gap-[8px]">
        <RoundToggle label="to try" icon={Bookmark} />
        <RoundToggle label="been" icon={Check} />
      </div>
      <div className="absolute left-[7px] top-[52px] flex items-center gap-[8px]">
        <span
          className="rounded-[4px] px-[7px] py-[2px] text-[12.5px] font-medium leading-[15px]"
          style={{ background: theme.pink, border: `1.5px solid ${theme.pinkBorder}`, color: theme.pinkText }}
        >
          {place.saves}
        </span>
        <span className="text-[15px] text-[#5a5a5e]">
          {place.tags[0]} <span className="text-[#bbb]">•</span> {place.tags[1]}
        </span>
      </div>
      <div className="absolute left-[10px] top-[80px] flex items-center gap-[5px] text-[13.5px]">
        <span className="h-[7px] w-[7px] rounded-full" style={{ background: '#f3a6d0' }} />
        <span className="text-[12px] font-semibold text-[#222]">{place.rank.label}</span>
        <span className="text-[#9a9a9e]">· {place.rank.detail}</span>
      </div>
      <div className="absolute left-[7px] top-[107px] flex items-center gap-[6px] text-[14.5px]">
        <span className="font-medium" style={{ color: theme.openGreen }}>{place.hours.state}</span>
        <span className="text-[#5a5a5e]">{place.hours.range}</span>
        <ChevronDown size={15} strokeWidth={1.6} color="#999" className="ml-[4px]" />
      </div>
    </div>
  )
}
