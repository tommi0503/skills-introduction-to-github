import { ChevronRight } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { topUp } from '../data'
import { theme } from '../theme'

/** Selected recipient / funding card summary. */
export function RecipientRow({ recipient }: { recipient: typeof topUp.recipient }) {
  return (
    <div className="flex h-[61px] items-center rounded-full pl-[9px] pr-[22px]" style={{ background: theme.translucent }}>
      <ImagePlaceholder label="Anne Smith avatar" className="h-[43px] w-[43px] rounded-full" />
      <div className="ml-[12px] flex-1">
        <div className="text-[16px] font-semibold leading-[20px]">{recipient.name}</div>
        <div className="mt-[1px] flex items-center gap-[5px] text-[11px] text-[#9a9aa0]">
          <ImagePlaceholder label="Card network logo" className="h-[11px] w-[22px] rounded-full" />
          {recipient.card}
        </div>
      </div>
      <ChevronRight size={20} strokeWidth={1.8} className="text-[#55555a]" />
    </div>
  )
}
