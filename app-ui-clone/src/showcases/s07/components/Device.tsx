import type { ReactNode } from 'react'
import { FramedPhone } from '../../shared-canvas/FramedPhone'
import { device } from '../theme'

/** The borderless phone used three times on the stage (dark hairline edge + soft drop shadow). */
export function Device({ children }: { children: ReactNode }) {
  return (
    <FramedPhone
      width={device.width}
      height={device.height}
      logicalWidth={device.logicalWidth}
      radius={device.radius}
      edge="#05070d"
      shadow="0 10px 24px rgba(0,0,0,0.45)"
    >
      {children}
    </FramedPhone>
  )
}
