import type { ReactNode } from 'react'
import { Bell } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'

/** White rounded square used for header actions. */
export function SquareAction({ children }: { children: ReactNode }) {
  return (
    <div className="relative flex h-[42px] w-[42px] items-center justify-center rounded-[14px] bg-white shadow-[0_2px_8px_rgba(0,0,0,0.05)]">
      {children}
    </div>
  )
}

export function NotificationAction() {
  return (
    <SquareAction>
      <Bell size={17} strokeWidth={1.8} className="text-[#9b9a97]" fill="#9b9a97" />
      <span className="absolute right-[12px] top-[11px] h-[6px] w-[6px] rounded-full bg-[#ef4a2f]" />
    </SquareAction>
  )
}

export interface AppHeaderProps {
  left: ReactNode
  top?: number
}

/** Leading action, centred brand logo (placeholder) and notification button. */
export function AppHeader({ left, top = 57 }: AppHeaderProps) {
  return (
    <div className="absolute inset-x-[21px] flex items-center justify-between" style={{ top }}>
      {left}
      <ImagePlaceholder label="Branja logo" className="h-[20px] w-[68px] rounded-[3px]" />
      <NotificationAction />
    </div>
  )
}
