import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'

export interface TransitLineProps {
  icon: LucideIcon
  iconColor: string
  lines: readonly string[]
  className?: string
}

/** Icon followed by one or more lines of travel info. */
export function TransitLine({ icon: Icon, iconColor, lines, className }: TransitLineProps) {
  return (
    <div className={cn('flex items-start', className)}>
      <span className="flex h-[25px] w-[53px] shrink-0 items-center justify-center">
        <Icon size={22} color={iconColor} strokeWidth={2.2} />
      </span>
      <div className="text-[14.5px] font-medium leading-[25px] tracking-[-0.3px]">
        {lines.map((l, i) => (
          <p key={i} className="m-0 whitespace-nowrap">
            {l}
          </p>
        ))}
      </div>
    </div>
  )
}
