import type { ReactNode } from 'react'
import { DynamicIsland, HomeIndicator, PhoneFrame, StatusBar } from '../../../ui'
import { device } from '../theme'

interface RentiquePhoneProps {
  /** Colour of status-bar glyphs. */
  statusColor?: string
  screenBackground?: string
  children: ReactNode
}

/** Frameless iPhone used by both Rentique screens (status bar, island, home bar). */
export function RentiquePhone({ statusColor = '#000', screenBackground = '#fff', children }: RentiquePhoneProps) {
  return (
    <PhoneFrame
      width={device.width}
      height={device.height}
      logicalWidth={device.logicalWidth}
      screenRadius={device.radius}
      screenBackground={screenBackground}
    >
      <div className="absolute inset-0 font-jakarta">{children}</div>
      <div className="absolute inset-x-0 top-0">
        <StatusBar color={statusColor} paddingX={45} paddingTop={22} fontSize={14.5} timeClassName="pl-[12px]" />
      </div>
      <DynamicIsland width={105} height={32} top={13} />
      <HomeIndicator width={114} bottom={6} />
    </PhoneFrame>
  )
}
