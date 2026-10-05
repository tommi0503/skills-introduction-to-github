import type { ReactNode } from 'react'
import { cn } from '../../../ui'
import { theme } from '../theme'

/** One handwritten line, optionally with a highlighter stripe behind its lower half. */
export function HandLine({ marked, className, children }: { marked?: boolean; className?: string; children: ReactNode }) {
  return (
    <div className={cn('relative whitespace-nowrap', className)}>
      {marked && (
        <span className="absolute inset-x-[-4px] bottom-[2px] h-[55%]" style={{ background: theme.highlight }} />
      )}
      <span className="relative">{children}</span>
    </div>
  )
}
