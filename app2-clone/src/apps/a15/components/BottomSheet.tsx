import type { ReactNode } from 'react'
import { cn } from '../../../ui'

/** White bottom sheet with rounded top and optional grabber. */
export function BottomSheet({ top, grabber, className, children }: { top: number; grabber?: boolean; className?: string; children?: ReactNode }) {
  return (
    <div className={cn('absolute inset-x-0 bottom-0 rounded-t-[20px] bg-white', className)} style={{ top }}>
      {grabber && <span className="absolute top-[7px] left-1/2 h-[4px] w-[44px] -translate-x-1/2 rounded-full bg-[#b9b6ba]" />}
      {children}
    </div>
  )
}
