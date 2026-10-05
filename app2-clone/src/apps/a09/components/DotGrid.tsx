import { cn } from '../../../ui'

/** 2×2 ring "apps" glyph. */
export function DotGrid({ className }: { className?: string }) {
  return (
    <span className={cn('grid grid-cols-2 gap-[3px]', className)}>
      {Array.from({ length: 4 }, (_, i) => (
        <span key={i} className="h-[9px] w-[9px] rounded-full border-[1.8px] border-current" />
      ))}
    </span>
  )
}
