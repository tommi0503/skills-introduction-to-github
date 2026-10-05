import type { Challenge } from '../data'
import { Mascot } from './Mascot'

/** Pastel challenge card with its mascot and duration meta. */
export function ChallengeTile({ challenge }: { challenge: Challenge }) {
  const { mascot } = challenge
  return (
    <div className="relative h-[182px] rounded-[22px]" style={{ background: challenge.bg }}>
      <Mascot spec={mascot} style={{ position: 'absolute', left: mascot.x, top: mascot.y }} />
      <div className="absolute inset-x-[16.5px] top-[127px]">
        <div className="whitespace-nowrap text-[15.9px] leading-[18px] font-bold tracking-[-0.2px]">{challenge.title}</div>
        <div className="mt-[5px] text-[11px] font-semibold text-[#5a5a60]">{challenge.meta}</div>
      </div>
    </div>
  )
}
