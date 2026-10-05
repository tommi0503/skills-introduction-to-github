import { cn } from '../../../ui'
import type { Tag } from '../data'

export function TagPill({ tag, compact, className }: { tag: Tag; compact?: boolean; className?: string }) {
  return (
    <span
      className={cn(
        'inline-flex items-center rounded-[3px] font-medium',
        compact ? 'h-[17px] px-[4px] text-[9px]' : 'h-[20px] px-[5px] text-[10px]',
        tag.tone === 'pink' ? 'bg-[#fbeefb] text-[#c94fcb]' : 'bg-[#f3f4f6] text-[#8a8a90]',
        className,
      )}
    >
      {tag.label}
    </span>
  )
}
