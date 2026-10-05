import type { ReactNode } from 'react'
import { FramedPhone } from '../../shared-canvas/FramedPhone'
import { device, theme } from '../theme'

/** Borderless phone with a very soft shadow, as used across the TheKitchen~ board. */
export function Device({ height = device.height, children }: { height?: number; children?: ReactNode }) {
  return (
    <FramedPhone
      width={device.width}
      height={height}
      logicalWidth={device.logicalWidth}
      radius={device.radius}
      background={theme.canvas}
      shadow="0 6px 18px rgba(0,0,0,0.05)"
    >
      {children}
    </FramedPhone>
  )
}
