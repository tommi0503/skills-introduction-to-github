import { cn } from '../../../ui'

interface OutlinedPillProps {
  label: string
  fill: string
  className?: string
}

/** Rounded capsule button with a dark outline (기부 프로그램 options). */
export function OutlinedPill({ label, fill, className }: OutlinedPillProps) {
  return (
    <div
      className={cn(
        'flex items-center justify-center rounded-full border-2 border-[#1f1f1f] font-extrabold tracking-[0.02em] text-[#1a1a1a]',
        className,
      )}
      style={{ background: fill }}
    >
      {label}
    </div>
  )
}
