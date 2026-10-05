import type { LucideIcon } from 'lucide-react'
import { Floating } from './Floating'

/** Labelled circular action ("to try" / "been"). */
export function RoundToggle({ label, icon: Icon }: { label: string; icon: LucideIcon }) {
  return (
    <div className="flex flex-col items-center gap-[6px]">
      <span className="text-[11px] leading-none text-[#8a8a8e]">{label}</span>
      <Floating className="h-[36px] w-[36px]" style={{ boxShadow: '0 2px 6px rgba(0,0,0,.16)' }}>
        <Icon size={19} strokeWidth={1.6} color="#333" />
      </Floating>
    </div>
  )
}
