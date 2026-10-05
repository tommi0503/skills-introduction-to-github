import { BadgeCheck, Check, Clock3, MapPin } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'

interface TripCardStackProps {
  dates: string
  title: string
  place: string
}

const glass = 'bg-[rgba(70,72,60,0.55)] text-white backdrop-blur-[2px]'

/** Fanned stack of trip photo cards with frosted info overlays. */
export function TripCardStack({ dates, title, place }: TripCardStackProps) {
  return (
    <div className="relative h-[205px] w-[175px]">
      <div className="absolute top-[4px] left-[12px] h-[198px] w-[160px] rotate-[5deg] rounded-[12px] border-[3px] border-white bg-white shadow-[0_4px_12px_rgba(0,0,0,0.10)]">
        <ImagePlaceholder className="h-full w-full rounded-[9px]" tone="#dcdfe3" label="trip photo" />
      </div>
      <div className="absolute top-[3px] left-[9px] h-[198px] w-[161px] -rotate-[5deg] rounded-[12px] border-[3px] border-white bg-white shadow-[0_6px_16px_rgba(0,0,0,0.12)]">
        <div className="relative h-full w-full overflow-hidden rounded-[9px]">
          <ImagePlaceholder className="h-full w-full" label="Bali photo" />
          <div className={`absolute top-[7px] left-[7px] flex h-[22px] items-center gap-[4px] rounded-full px-[7px] text-[9px] ${glass}`}>
            <Clock3 size={10} strokeWidth={2} />
            {dates}
          </div>
          <div className={`absolute top-[8px] right-[8px] flex h-[18px] w-[18px] items-center justify-center rounded-full ${glass}`}>
            <Check size={10} strokeWidth={2.6} />
          </div>
          <div className={`absolute right-[7px] bottom-[11px] left-[11px] rounded-[10px] px-[9px] pt-[8px] pb-[8px] ${glass}`}>
            <div className="flex items-center gap-[4px] text-[11px] font-semibold">
              {title}
              <BadgeCheck size={11} strokeWidth={0} fill="#fff" className="text-white" />
            </div>
            <div className="mt-[6px] flex items-center gap-[5px] text-[9px] text-white/85">
              <MapPin size={9} strokeWidth={2} />
              {place}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
