import { Pill, cn } from '../../../ui'

interface OutlineBadgeProps {
  label: string
  className?: string
}

/** Small pill label ("Joyful Market", "Artist Interview"). Fill/border injected via className. */
export function OutlineBadge({ label, className }: OutlineBadgeProps) {
  return (
    <Pill className={cn('h-[30px] px-[14px] font-poppins text-[13.5px] font-bold tracking-[0.01em] text-[#1e1e1e]', className)}>
      {label}
    </Pill>
  )
}
