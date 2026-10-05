import type { LucideIcon } from 'lucide-react'
import { ArrowLeft } from 'lucide-react'
import { RoundButton } from './RoundButton'

/** Back button · centred condensed title · trailing action. */
export function TopBar({ title, action, top = 67 }: { title: string; action: LucideIcon; top?: number }) {
  return (
    <div className="absolute right-[16px] left-[16px] flex items-center justify-between" style={{ top }}>
      <RoundButton icon={ArrowLeft} size={51} iconSize={21} strokeWidth={2.2} />
      <span className="font-condensed text-[20px] font-bold text-[#111]">{title}</span>
      <RoundButton icon={action} size={51} iconSize={20} strokeWidth={2} />
    </div>
  )
}
