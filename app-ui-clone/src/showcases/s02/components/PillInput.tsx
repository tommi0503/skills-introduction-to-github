import type { ReactNode } from 'react'
import { Mic } from 'lucide-react'

interface PillInputProps {
  leading: ReactNode
  placeholder: string
  /** Width of the leading slot (up to the hairline divider). */
  leadingWidth: number
  /** Left inset of the leading content; centred when omitted. */
  leadingInset?: number
}

/** Rounded input capsule: leading slot | divider | placeholder | mic. */
export function PillInput({ leading, placeholder, leadingWidth, leadingInset }: PillInputProps) {
  return (
    <div className="flex h-[45px] items-center rounded-full bg-white pr-[16px] shadow-[0_4px_14px_rgba(0,0,0,0.06),0_0_0_1px_rgba(0,0,0,0.025)]">
      <div
        className="flex h-full shrink-0 items-center"
        style={{ width: leadingWidth, paddingLeft: leadingInset, justifyContent: leadingInset === undefined ? 'center' : 'flex-start' }}
      >
        {leading}
      </div>
      <span className="h-[18px] w-px bg-[#ececec]" />
      <span className="ml-[12px] flex-1 text-[13px] text-[#9b9b9b]">{placeholder}</span>
      <Mic size={20} strokeWidth={1.6} className="text-[#3a3a3a]" />
    </div>
  )
}
