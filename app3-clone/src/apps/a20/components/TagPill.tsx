import { cn } from '../../../ui'
import type { Tag } from '../data'

export function TagPill({ tag, className }: { tag: Tag; className?: string }) {
  return (
    <span
      className={cn(
        'inline-flex h-[20px] items-center rounded-[3px] px-[5px] text-[10px] font-medium',
        tag.tone === 'pink' ? 'bg-[#fbeefb] text-[#c94fcb]' : 'bg-[#f3f4f6] text-[#8a8a90]',
        className,
      )}
    >
      {tag.label}
    </span>
  )
}
