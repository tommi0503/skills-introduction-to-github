import { Heart, Plus, Sparkles } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { Pick } from '../data'
import { cardTones, theme } from '../theme'

/** "AI pick" product card with dish, price and add-to-order bar. */
export function PickCard({ pick }: { pick: Pick }) {
  return (
    <div className="relative h-[307px] w-[282px] rounded-[23px]" style={{ background: cardTones[pick.tone] }}>
      <div className="absolute top-[14px] left-[16px] flex items-center gap-[5px] text-[13px] text-[#222]">
        <Sparkles size={14} strokeWidth={2} />
        {pick.badge}
      </div>
      <span className="absolute top-[7px] right-[8px] flex h-[37px] w-[37px] items-center justify-center rounded-[11px] bg-white">
        <Heart size={18} fill={theme.heart} color={theme.heart} />
      </span>
      <ImagePlaceholder className="absolute top-[44px] left-[66px] h-[152px] w-[152px] rounded-full" label={pick.title} />
      <div className="absolute top-[208px] right-[11px] left-[9px] flex items-center justify-between font-condensed font-bold text-[#111]">
        <span className="text-[17.5px]">{pick.title}</span>
        <span className="text-[20px]">{pick.price}</span>
      </div>
      <div className="absolute top-[250px] right-[11px] left-[9px] flex h-[47px] items-center justify-center rounded-full bg-black text-[14.5px] text-white">
        {pick.cta}
        <span className="absolute top-[3px] right-[3px] flex h-[41px] w-[41px] items-center justify-center rounded-full bg-white text-black">
          <Plus size={20} strokeWidth={1.8} />
        </span>
      </div>
    </div>
  )
}
