import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'
import { cardShadow, theme } from '../theme'

export interface ScreenHeaderProps {
  title: string
  subtitle: string
  action: LucideIcon
  /** Small red notification dot on the action. */
  dot?: boolean
  className?: string
}

export function ScreenHeader({ title, subtitle, action: Icon, dot, className }: ScreenHeaderProps) {
  return (
    <div className={cn('flex items-start justify-between', className)}>
      <div>
        <h1 className="text-[24px] leading-[30px] tracking-[-0.6px]" style={{ color: theme.ink }}>
          {title}
        </h1>
        <p className="mt-[2px] text-[11.5px] tracking-[-0.1px]" style={{ color: theme.muted }}>
          {subtitle}
        </p>
      </div>
      <span
        className="relative mt-[3px] flex h-[46px] w-[46px] items-center justify-center rounded-full"
        style={{ background: '#f4f4f4', boxShadow: cardShadow }}
      >
        <Icon size={18} strokeWidth={1.6} color="#333" />
        {dot && <span className="absolute top-[13px] right-[14px] h-[5px] w-[5px] rounded-full bg-[#ef3b3b]" />}
      </span>
    </div>
  )
}
