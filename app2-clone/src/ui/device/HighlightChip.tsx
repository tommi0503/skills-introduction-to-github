import { cn } from '../core/cn'

export interface HighlightChipProps {
  label?: string
  className?: string
}

/** Grey "Highlight" capsule that overlays the status-bar time in the reference recordings. */
export function HighlightChip({ label = 'Highlight', className }: HighlightChipProps) {
  return (
    <span
      className={cn(
        'absolute z-50 rounded-[8px] bg-[#9a9a9a]/95 px-[9px] py-[5px] text-[16px] leading-none font-semibold text-white',
        className,
      )}
      style={{ left: 22, top: 22 }}
    >
      {label}
    </span>
  )
}
