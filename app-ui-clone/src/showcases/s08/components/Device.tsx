import type { ReactNode } from 'react'
import { FramedPhone } from '../../shared-canvas/FramedPhone'
import { device, theme } from '../theme'

export function Device({ children }: { children: ReactNode }) {
  return (
    <FramedPhone
      width={device.width}
      height={device.height}
      logicalWidth={device.logicalWidth}
      radius={device.radius}
      background={theme.bg}
      edge="#1a120e"
      shadow="0 12px 26px rgba(0,0,0,0.45)"
    >
      {children}
    </FramedPhone>
  )
}
