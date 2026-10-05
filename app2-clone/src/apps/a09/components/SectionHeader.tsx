import { cn } from '../../../ui'

export function SectionHeader({ title, action, className }: { title: string; action?: string; className?: string }) {
  return (
    <div className={cn('flex items-baseline justify-between px-[16px]', className)}>
      <h2 className="text-[20.5px] leading-[26px] font-medium text-[#222325]">{title}</h2>
      {action && <span className="text-[14.5px] font-medium text-[#222325] underline underline-offset-[3px]">{action}</span>}
    </div>
  )
}
