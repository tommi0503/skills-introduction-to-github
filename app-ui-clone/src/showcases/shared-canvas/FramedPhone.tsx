import type { CSSProperties, ReactNode } from 'react'
import { PhoneFrame } from '../../ui'

export interface FramedPhoneProps {
  width: number
  height: number
  logicalWidth: number
  radius: number
  /** Hairline edge colour drawn just outside the screen. */
  edge?: string
  shadow?: string
  background?: string
  style?: CSSProperties
  children: ReactNode
}

/** Bezel-less phone mockup: hairline edge + drop shadow around a scaled screen. */
export function FramedPhone({ width, height, logicalWidth, radius, edge, shadow, background, style, children }: FramedPhoneProps) {
  const ring = edge ? `0 0 0 1px ${edge}` : null
  return (
    <PhoneFrame
      width={width}
      height={height}
      logicalWidth={logicalWidth}
      screenRadius={radius}
      screenBackground={background}
      style={{ boxShadow: [ring, shadow].filter(Boolean).join(', ') || undefined, ...style }}
    >
      {children}
    </PhoneFrame>
  )
}
