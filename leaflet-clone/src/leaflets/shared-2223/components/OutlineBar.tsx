import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export interface OutlineBarProps {
  /** Optional solid green tag at the left end (농사 체험 …). */
  tag?: string
  className?: string
  children: ReactNode
}

/** Pale-green capsule with a green outline, optionally led by a solid tag. */
export function OutlineBar({ tag, className, children }: OutlineBarProps) {
  return (
    <div className={cn('flex h-[35px] items-center overflow-hidden rounded-full border-[3px] border-[#76b282] bg-[#e3f1e5]', className)}>
      {tag && (
        <span className="flex h-full w-[84px] shrink-0 items-center justify-center rounded-full bg-[#76b282] text-[14px] font-semibold tracking-[-0.04em] text-white">
          {tag}
        </span>
      )}
      <span className="min-w-0 flex-1 truncate text-[#5fa76d]">{children}</span>
    </div>
  )
}
