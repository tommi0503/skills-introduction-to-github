import { cn } from '../../../ui'

interface SectionHeaderProps {
  title: string
  aside?: string
  className?: string
  titleClassName?: string
}

/** Title on the left, muted counter on the right. */
export function SectionHeader({ title, aside, className, titleClassName }: SectionHeaderProps) {
  return (
    <div className={cn('flex items-center justify-between', className)}>
      <span className={cn('font-semibold', titleClassName)}>{title}</span>
      {aside && <span className="text-[11.5px] font-medium text-[#86868b]">{aside}</span>}
    </div>
  )
}
