import { ArrowRight } from 'lucide-react'
import { cn } from '../../../ui'
import { theme } from '../theme'

export function DestinationInput({ placeholder, className }: { placeholder: string; className?: string }) {
  return (
    <div
      className={cn('flex h-[56px] items-center rounded-full border pr-[18px] pl-[21px] font-pretendard', className)}
      style={{ background: theme.inputBg, borderColor: theme.inputBorder }}
    >
      <span className="h-[7px] w-[7px]" style={{ background: theme.navy }} />
      <span className="ml-[13px] flex-1 text-[15px] tracking-[-0.2px]" style={{ color: theme.muted }}>
        {placeholder}
      </span>
      <ArrowRight size={22} strokeWidth={1.6} color="#555a6e" />
    </div>
  )
}
