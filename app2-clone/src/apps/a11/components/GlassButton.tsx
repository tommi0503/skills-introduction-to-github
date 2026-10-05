import type { ReactNode } from 'react'
import { cn } from '../../../ui'

/** Round translucent map button. */
export function GlassButton({ size = 44, className, children }: { size?: number; className?: string; children: ReactNode }) {
  return (
    <div
      className={cn('absolute flex items-center justify-center rounded-full border border-white/15 bg-[#26304e]/80 text-white', className)}
      style={{ width: size, height: size }}
    >
      {children}
    </div>
  )
}
