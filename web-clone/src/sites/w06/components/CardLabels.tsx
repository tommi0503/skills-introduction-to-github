import { ArrowRight } from 'lucide-react'
import { cn } from '../../../ui'

export interface CardLabelsProps {
  title: string
  action: string
  tone?: 'dark' | 'light'
  className?: string
}

/** Bottom row of a product card: name on the left, "Explore →" on the right. */
export function CardLabels({ title, action, tone = 'dark', className }: CardLabelsProps) {
  const light = tone === 'light'
  return (
    <div className={cn('absolute inset-x-4 bottom-4 flex justify-between text-[14px] font-[450] leading-5', className)}>
      <span style={{ color: light ? 'rgba(255,255,255,0.8)' : '#0a0a0a' }}>{title}</span>
      <span className="flex items-center gap-[3px]" style={{ color: light ? 'rgba(255,255,255,0.55)' : '#0a0a0a' }}>
        {action}
        <ArrowRight size={14} strokeWidth={1.8} />
      </span>
    </div>
  )
}
