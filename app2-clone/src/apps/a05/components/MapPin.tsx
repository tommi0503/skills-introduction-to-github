import { ImagePlaceholder } from '../../../ui'
import type { MapPinData } from '../data'

/** Round place marker (emoji/photo badge + status dot) with its name/description label. */
export function MapPin({ pin }: { pin: MapPinData }) {
  const r = 15
  return (
    <div className="absolute" style={{ left: pin.x - r, top: pin.y - r }}>
      <div className="relative flex h-[30px] w-[30px] items-center justify-center rounded-full bg-white" style={{ boxShadow: '0 1px 4px rgba(0,0,0,.18)' }}>
        <ImagePlaceholder label={pin.name} tone={pin.avatar ? '#cfd2d6' : '#d6d9dd'} className={pin.avatar ? 'h-[28px] w-[28px] rounded-full' : 'h-[22px] w-[22px] rounded-full'} />
        <span className="absolute -right-[2px] -top-[3px] h-[10px] w-[10px] rounded-full" style={{ background: pin.dot }} />
      </div>
      <div
        className="absolute left-[35px] whitespace-nowrap leading-[12px] text-[#1d1d1f]"
        style={{ top: pin.kicker ? -9 : 3 }}
      >
        {pin.kicker && <p className="text-[9.5px] italic text-[#555]">{pin.kicker}</p>}
        <p className="text-[10px] font-semibold tracking-[-0.2px]">{pin.name}</p>
        {pin.sub.map((s) => (
          <p key={s} className="text-[8.5px] italic text-[#666]">{s}</p>
        ))}
      </div>
    </div>
  )
}
