import { ArrowDown, ArrowUp } from 'lucide-react'
import { cn } from '../../../ui'

/** Small round arrow showing whether the tide is rising or falling. */
export function LevelBadge({ rising, size = 24, className }: { rising: boolean; size?: number; className?: string }) {
  const Icon = rising ? ArrowUp : ArrowDown
  return (
    <span
      className={cn('flex shrink-0 items-center justify-center rounded-full bg-[#4a7fd0]/35 text-[#5d9df0]', className)}
      style={{ width: size, height: size }}
    >
      <Icon size={size * 0.62} strokeWidth={2.6} />
    </span>
  )
}
