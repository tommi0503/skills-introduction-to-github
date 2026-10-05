import { AudioLines, MapPin, X } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { CapsuleButton } from '../components/CapsuleButton'
import { TopBar } from '../components/TopBar'
import { planner } from '../data'

function Chip({ label, pin }: { label: string; pin: boolean }) {
  return (
    <span className="flex h-[36px] items-center gap-[7px] rounded-full border border-[#dedede] bg-[#f1f1f1] px-[13px] text-[14px]">
      {pin && <MapPin size={15} strokeWidth={1.7} />}
      {label}
    </span>
  )
}

/** Voice trip-planning sheet presented over a dimmed chat. */
export function PlannerScreen() {
  return (
    <AppScreen className="font-inter" background="#000">
      <TopBar color="#fff" dot />
      <div className="absolute flex items-start gap-[10px] rounded-t-[12px] bg-[#e9e9e9] px-[30px] pt-[1px]" style={{ left: 16, right: 16, top: 56, height: 30 }}>
        <ImagePlaceholder className="h-[12px] w-[24px]" label="thumbnail" />
        <span className="flex-1 text-[15.5px] leading-[15px]">{planner.behindTitle}</span>
        <X size={13} strokeWidth={1.6} />
      </div>
      <div className="absolute inset-x-0 bottom-0 rounded-t-[14px] bg-white" style={{ top: 68 }}>
        <span className="absolute flex h-[29px] w-[29px] items-center justify-center rounded-full bg-[#f2f2f2]" style={{ left: 15, top: 16 }}>
          <X size={15} strokeWidth={1.8} />
        </span>
        <h1 className="absolute text-[28.5px] leading-[36px] font-[650] tracking-[-0.5px]" style={{ left: 24, top: 89, width: 300 }}>
          {planner.title}
        </h1>
        <p className="absolute text-[17px] leading-[21px] text-[#8e8e93]" style={{ left: 24, top: 168, width: 345 }}>
          {planner.intro}
        </p>
        <div className="absolute flex gap-[13px]" style={{ left: 24, top: 257 }}>
          {planner.photos.map((p) => (
            <ImagePlaceholder key={p} className="h-[79px] w-[78px] rounded-[12px]" label={`${p} photo`} />
          ))}
        </div>
        <div className="absolute flex flex-col gap-[9px]" style={{ left: 24, top: 357 }}>
          {planner.chipRows.map((row, i) => (
            <div key={i} className="flex gap-[8px]">
              {row.map((c) => (
                <Chip key={c.key} label={c.label} pin={c.pin} />
              ))}
            </div>
          ))}
        </div>
        <p className="absolute text-[16px] text-[#8e8e93]" style={{ left: 24, top: 457 }}>
          {planner.transcript[0]}
        </p>
        <p className="absolute text-[16px] leading-[19px] text-[#8e8e93]" style={{ left: 24, top: 497, width: 330 }}>
          {planner.transcript[1]}
        </p>
        <span className="absolute flex h-[63px] w-[63px] items-center justify-center rounded-full bg-[#1f1f1f] text-white" style={{ left: 163, top: 558 }}>
          <AudioLines size={22} strokeWidth={1.5} />
        </span>
        <span className="absolute inset-x-0 text-center text-[12.5px] text-[#9a9a9e]" style={{ top: 630 }}>
          {planner.speaking}
        </span>
        <CapsuleButton top={666} className="inset-x-[24px] h-[47px] text-[16.5px]">
          {planner.cta}
        </CapsuleButton>
      </div>
    </AppScreen>
  )
}
