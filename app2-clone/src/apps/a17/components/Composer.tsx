import type { ReactNode } from 'react'
import { AudioLines, Mic, Plus, Square } from 'lucide-react'
import { cn } from '../../../ui'
import { composer } from '../data'
import { floatShadow } from '../theme'

export interface ComposerProps {
  placeholder: string
  /** 'voice' shows mic + voice mode; 'stop' shows the stop-generation square. */
  trailing: 'voice' | 'stop'
  /** Optional content above the input (e.g. upgrade banner). */
  banner?: ReactNode
  className?: string
}

/** Bottom message composer card. */
export function Composer({ placeholder, trailing, banner, className }: ComposerProps) {
  return (
    <div className={cn('absolute inset-x-[16px] bottom-[32px] rounded-[24px] bg-[#fbfbf9] px-[8px] pt-[8px] pb-[8px]', floatShadow, className)}>
      {banner}
      <p className={cn('px-[5px] text-[17px] text-[#8d8c87]', banner ? 'pt-[19px]' : 'pt-[5px]')}>{placeholder}</p>
      <div className="mt-[16px] flex items-center gap-[8px]">
        <span className="flex size-[35px] items-center justify-center rounded-full bg-[#ecebe7] text-[#262624]">
          <Plus size={18} strokeWidth={1.8} />
        </span>
        <span className="flex h-[34px] items-center gap-[4px] rounded-full bg-[#ecebe7] px-[15px] text-[13px] text-[#262624]">
          {composer.model}
          <span className="text-[#8d8c87]">{composer.effort}</span>
        </span>
        <span className="flex-1" />
        {trailing === 'voice' ? (
          <>
            <span className="flex size-[35px] items-center justify-center rounded-full bg-[#ecebe7] text-[#262624]">
              <Mic size={18} strokeWidth={1.7} />
            </span>
            <span className="flex size-[36px] items-center justify-center rounded-full bg-[#141413] text-white">
              <AudioLines size={19} strokeWidth={2} />
            </span>
          </>
        ) : (
          <span className="flex size-[36px] items-center justify-center text-[#141413]">
            <Square size={15} fill="currentColor" strokeWidth={0} className="rounded-[2px]" />
          </span>
        )}
      </div>
    </div>
  )
}
