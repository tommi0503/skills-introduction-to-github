import type { ReactNode } from 'react'
import { X } from 'lucide-react'

export interface BottomSheetProps {
  top: number
  title: string
  children?: ReactNode
}

/** Rounded white sheet with centred title and a close button. */
export function BottomSheet({ top, title, children }: BottomSheetProps) {
  return (
    <div className="absolute inset-x-0 bottom-0 z-20 bg-white" style={{ top, borderRadius: '20px 20px 0 0' }}>
      <div
        className="absolute inset-x-0 text-center"
        style={{ top: 19.5, fontSize: 19, fontWeight: 700, color: '#111', letterSpacing: -0.4 }}
      >
        {title}
      </div>
      <X size={33} strokeWidth={1.25} className="absolute" style={{ right: 9.2, top: 6, color: '#1d1d1d' }} />
      {children}
    </div>
  )
}
