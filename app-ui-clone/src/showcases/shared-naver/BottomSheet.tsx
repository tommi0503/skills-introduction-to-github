import type { ReactNode } from 'react'
import { X } from 'lucide-react'

export interface BottomSheetProps {
  /** Top edge of the sheet (logical px). */
  top: number
  title: string
  /** Baseline offsets inside the sheet. */
  titleTop?: number
  titleSize?: number
  closeSize?: number
  closeTop?: number
  closeRight?: number
  radius?: number
  children?: ReactNode
}

/** Rounded white modal sheet with a centred bold title and a close (×) button. */
export function BottomSheet({
  top,
  title,
  titleTop = 19.5,
  titleSize = 19,
  closeSize = 33,
  closeTop = 6,
  closeRight = 9.2,
  radius = 20,
  children,
}: BottomSheetProps) {
  return (
    <div className="absolute inset-x-0 bottom-0 z-20 bg-white" style={{ top, borderRadius: `${radius}px ${radius}px 0 0` }}>
      <div
        className="absolute inset-x-0 text-center"
        style={{ top: titleTop, fontSize: titleSize, fontWeight: 700, color: '#111', letterSpacing: -0.4 }}
      >
        {title}
      </div>
      <X
        size={closeSize}
        strokeWidth={(1.25 * 33) / closeSize}
        className="absolute"
        style={{ right: closeRight, top: closeTop, color: '#1d1d1d' }}
      />
      {children}
    </div>
  )
}
