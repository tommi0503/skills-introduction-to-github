import type { ReactNode } from 'react'
import { cn } from '../../../ui'

/** White rounded card with hairline-separated sections. */
export function Card({ className, children }: { className?: string; children: ReactNode }) {
  return <div className={cn('overflow-hidden rounded-[14px] bg-white divide-y divide-[#efeeeb]', className)}>{children}</div>
}
