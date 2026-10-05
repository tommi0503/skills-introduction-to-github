import { CircleCheck } from 'lucide-react'
import { cn } from '../../../ui'
import { gh } from '../theme'

/** Filled state capsule (e.g. purple "Closed"). */
export function StateChip({ label, color = gh.purple, className }: { label: string; color?: string; className?: string }) {
  return (
    <span
      className={cn('inline-flex h-[28px] items-center gap-[5px] rounded-full px-[10px] text-[14px] text-white', className)}
      style={{ background: color }}
    >
      <CircleCheck size={16} strokeWidth={1.8} />
      {label}
    </span>
  )
}

/** Grey progress capsule with a purple check (e.g. "1 of 1"). */
export function ProgressChip({ label, height = 24, className }: { label: string; height?: number; className?: string }) {
  return (
    <span className={cn('inline-flex items-center gap-[4px] rounded-full bg-[#f1f1f3] px-[9px] text-[12.5px] text-[#6b7079]', className)} style={{ height }}>
      <CircleCheck size={15} strokeWidth={1.8} style={{ color: gh.purple }} />
      {label}
    </span>
  )
}
