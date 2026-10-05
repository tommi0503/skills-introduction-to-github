import { Sparkles } from 'lucide-react'
import { overlays } from '../data'
import { colors, fonts, shadows } from '../theme'

/** Fixed UI captured in the first viewport: cookie notice and floating "Ask" button. */
export function Overlays() {
  return (
    <>
      <div
        className={`absolute flex items-center rounded-[14px] border bg-white pl-[19px] pr-[20px] ${fonts.sans}`}
        style={{ left: 1060, top: 756, width: 360, height: 74, borderColor: '#f2f2f2', boxShadow: shadows.popover }}
      >
        <p className="w-[247px] text-[14px] leading-[16.8px]" style={{ color: colors.body }}>
          {overlays.cookie}
        </p>
        <span className="ml-auto flex h-[34px] items-center rounded-full px-[10px] text-[14px] font-medium" style={{ background: colors.border, color: colors.body }}>
          {overlays.okay}
        </span>
      </div>
      <div
        className="absolute flex items-center gap-[10px] rounded-full border bg-white pl-[16px] text-[16px]"
        style={{ left: 1336, top: 838, width: 87, height: 46, borderColor: '#eeeeee', color: '#656973', boxShadow: shadows.tile }}
      >
        {overlays.ask}
        <Sparkles size={18} strokeWidth={1.5} />
      </div>
    </>
  )
}
