import { Zap } from 'lucide-react'
import { cn } from '../../../ui'
import { theme } from '../theme'

/** Purple "⚡ N원 즉시할인" strip at the foot of a photo. */
export function DiscountBar({ label, className, size = 'sm' }: { label: string; className?: string; size?: 'sm' | 'md' }) {
  return (
    <div
      className={cn('flex items-center gap-[3px] font-bold text-white', size === 'md' ? 'px-[8px] text-[13px]' : 'justify-center text-[11px]', className)}
      style={{ background: theme.purple }}
    >
      <Zap size={size === 'md' ? 14 : 11} fill="#fff" strokeWidth={0} />
      {label}
    </div>
  )
}
