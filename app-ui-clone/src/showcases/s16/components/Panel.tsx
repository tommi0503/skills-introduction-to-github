import type { ReactNode } from 'react'
import { cn } from '../../../ui'

/** White rounded content card. */
export function Panel({ className, children }: { className?: string; children?: ReactNode }) {
  return <div className={cn('mx-[16px] rounded-[20px] bg-white', className)}>{children}</div>
}
