import { Mic, Plus, Send } from 'lucide-react'
import { composerPlaceholder, type NavKey } from '../data'
import { BottomNav } from './BottomNav'

/** White bottom sheet with an optional "Ask anything" composer above the tab bar. */
export function BottomPanel({ active, composer = true, top }: { active: NavKey; composer?: boolean; top: number }) {
  return (
    <div
      className="absolute inset-x-0 bottom-0 rounded-t-[16px] bg-white"
      style={{ top, boxShadow: composer ? '0 -3px 12px rgba(0,0,0,0.05)' : undefined }}
    >
      {composer && (
        <>
          <div className="absolute flex items-center" style={{ left: 24, right: 22, top: 15 }}>
            <span className="flex h-[30px] w-[30px] items-center justify-center rounded-full bg-[#efefef]">
              <Plus size={18} strokeWidth={1.6} />
            </span>
            <span className="ml-[12px] flex-1 text-[16px] text-[#8e8e93]">{composerPlaceholder}</span>
            <span className="flex h-[30px] w-[30px] items-center justify-center rounded-full bg-[#efefef]">
              <Mic size={15} strokeWidth={1.8} />
            </span>
            <Send size={19} strokeWidth={1.5} className="ml-[15px] text-[#8e8e93]" />
          </div>
          <div className="absolute h-px bg-[#e8e8e8]" style={{ left: 22, right: 22, top: 61 }} />
        </>
      )}
      <BottomNav active={active} top={composer ? 69 : 10} />
    </div>
  )
}
