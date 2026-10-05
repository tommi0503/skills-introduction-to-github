import type { ReactNode } from 'react'
import { cn } from '../../../ui'

/** White rounded surface used by every Zip panel. */
export function Card({ className, children }: { className?: string; children?: ReactNode }) {
  return <div className={cn('rounded-[12px] bg-white', className)}>{children}</div>
}
