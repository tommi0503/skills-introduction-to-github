import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'
import { hutech, hutechType } from '../theme'

export interface ServiceIntroProps {
  icon: LucideIcon
  label: string
  headline: string
  className?: string
}

/** Large icon + "SERVICE 0N" + two-line headline that opens each inside panel. */
export function ServiceIntro({ icon: Icon, label, headline, className }: ServiceIntroProps) {
  return (
    <div className={cn('flex flex-col', className)}>
      <Icon size={176} strokeWidth={1.9} color={hutech.navy} className="-ml-3" />
      <h2 className={cn('m-0 mt-[34px] text-[44px] leading-none', hutechType.display)} style={{ color: hutech.accent }}>
        {label}
      </h2>
      <p className="m-0 mt-[26px] whitespace-pre-line text-[29px] leading-[38px]" style={{ color: hutech.inkSoft }}>
        {headline}
      </p>
    </div>
  )
}
