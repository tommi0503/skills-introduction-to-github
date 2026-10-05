import { cn } from '../../../ui'
import type { ChipTone } from '../data'

const tones: Record<ChipTone, { bg: string; fg: string }> = {
  blue: { bg: '#f6f6f6', fg: '#3b7bf0' },
  amber: { bg: '#f8f7f5', fg: '#e8a52f' },
  grey: { bg: '#e8e8e8', fg: '#a9a9a9' },
}

/** Small rounded status pill. */
export function StatusChip({ label, tone, className }: { label: string; tone: ChipTone; className?: string }) {
  const t = tones[tone]
  return (
    <span
      className={cn('inline-flex items-center justify-center rounded-full text-[11px] tracking-[-0.1px]', className)}
      style={{ background: t.bg, color: t.fg }}
    >
      {label}
    </span>
  )
}
