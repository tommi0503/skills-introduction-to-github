import { cn } from '../../../ui'
import { theme } from '../theme'

export interface SectionHeaderProps {
  title: string
  action?: string
  className?: string
  titleClassName?: string
}

/** "Title ........ See all" row. */
export function SectionHeader({ title, action, className, titleClassName }: SectionHeaderProps) {
  return (
    <div className={cn('flex items-center justify-between', className)}>
      <span className={cn('text-[18px] tracking-[-0.2px]', titleClassName)} style={{ color: theme.ink }}>
        {title}
      </span>
      {action && (
        <span className="text-[12px]" style={{ color: '#8a8a8a' }}>
          {action}
        </span>
      )}
    </div>
  )
}
