import { cn } from '../../../ui'
import type { Tag } from '../data'

/** Rounded chip with a coloured icon + label (categories, dietary tags). */
export function TagChip({ tag, className }: { tag: Tag; className?: string }) {
  const Icon = tag.icon
  return (
    <div className={cn('flex h-[40px] shrink-0 items-center gap-[8px] rounded-[9px] px-[11px]', className)}>
      {tag.badge ? (
        <span className="flex h-[20px] w-[20px] items-center justify-center rounded-full" style={{ background: tag.color }}>
          <Icon size={13} strokeWidth={2.6} color="#fff" />
        </span>
      ) : (
        <Icon size={19} strokeWidth={2} color={tag.color} fill={tag.color} fillOpacity={0.9} />
      )}
      {tag.label && <span className="font-poppins text-[13.5px] leading-none font-medium text-[#111]">{tag.label}</span>}
    </div>
  )
}
