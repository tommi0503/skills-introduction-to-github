import { cn } from '../../../ui'

/** Small grey capsule shown next to a thread title. */
export function TagChip({ label, className }: { label: string; className?: string }) {
  return (
    <span className={cn('min-w-0 truncate rounded-[5px] bg-[#f1f1f1] px-[6px] py-[1px] text-[13px] leading-[18px] text-[#888]', className)}>
      {label}
    </span>
  )
}
