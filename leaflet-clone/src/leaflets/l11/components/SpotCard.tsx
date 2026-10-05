import { ImagePlaceholder, Placed } from '../../../ui'
import { Lines } from '../../shared-0812'
import type { Spot } from '../data'
import { theme } from '../theme'

const CARD = { top: 213, height: 657, photo: 242, tabWidth: 283, tabHeight: 43 }

/** Big number, photo with a lime tag tab, description and info rows with a mascot icon. */
export function SpotCard({ spot }: { spot: Spot }) {
  return (
    <>
      <Placed x={spot.x + 4} y={96} className="font-poppins text-[124px] leading-[124px] font-black" style={{ color: theme.lime }}>
        {spot.number}
      </Placed>
      <Placed x={spot.x} y={CARD.top} width={spot.width} height={CARD.height} style={{ background: theme.card, color: theme.ink }}>
        <ImagePlaceholder className="w-full" style={{ height: CARD.photo }} label={`${spot.tag} photo`} />
        <div
          className="absolute left-0 flex items-center pl-[30px] text-[20px] font-bold"
          style={{ top: CARD.photo - CARD.tabHeight, width: CARD.tabWidth, height: CARD.tabHeight, background: theme.card }}
        >
          {spot.tag}
        </div>
        <div className="absolute left-[30px] top-[288px] text-[22.5px] leading-[30px] text-[#4d4d38]">{spot.desc}</div>
        <ImagePlaceholder className="absolute left-[28px] top-[422px] h-[75px] w-[60px] rounded-[45%]" label="clover mascot" />
        <div className="absolute left-[105px] top-[419px] text-[22px] leading-[32px] text-[#4d4d38]">
          <Lines lines={spot.info} />
          <Lines lines={spot.address} className="mt-[20px] tracking-[-0.6px]" />
        </div>
      </Placed>
    </>
  )
}
