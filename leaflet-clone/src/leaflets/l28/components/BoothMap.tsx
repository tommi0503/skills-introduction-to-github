import { autumn } from '../../shared-2829/theme'
import { boothMap } from '../data'

/** White card holding the booth layout boxes. */
export function BoothMap() {
  return (
    <div className="relative h-[279px] w-[352px] rounded-[18px]" style={{ background: autumn.card }}>
      {boothMap.booths.map((b, i) => (
        <div
          key={i}
          className={`absolute flex items-center justify-center rounded-[10px] font-gothic-a1 font-bold tracking-[-0.5px]`}
          style={{ left: b.x, top: b.y, width: b.w, height: b.h, background: b.fill, color: b.text, fontSize: b.size }}
        >
          {b.label}
        </div>
      ))}
    </div>
  )
}
