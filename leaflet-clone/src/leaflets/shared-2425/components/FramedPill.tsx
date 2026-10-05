import type { CSSProperties, ReactNode } from 'react'
import { Pill, cn } from '../../../ui'
import { library } from '../theme'

interface FramedPillProps {
  fill: string
  width?: number
  height?: number
  borderWidth?: number
  className?: string
  style?: CSSProperties
  children: ReactNode
}

/** Capsule label with the navy outline used throughout the library leaflets. */
export function FramedPill({ fill, width, height, borderWidth = 2, className, style, children }: FramedPillProps) {
  return (
    <Pill className={cn('box-border', className)}>
      <span
        className="box-border inline-flex items-center justify-center rounded-[inherit]"
        style={{ width, height, background: fill, border: `${borderWidth}px solid ${library.ink}`, ...style }}
      >
        {children}
      </span>
    </Pill>
  )
}
