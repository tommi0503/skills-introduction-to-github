import type { ReactNode } from 'react'
import { DynamicIsland, HomeIndicator, PhoneFrame, StatusBar } from '../../../ui'
import { phone, theme } from '../theme'

export interface DeliveryPhoneProps {
  homeIndicator?: boolean
  children?: ReactNode
}

/** Flat light phone used by every screen of this showcase. */
export function DeliveryPhone({ homeIndicator = true, children }: DeliveryPhoneProps) {
  return (
    <PhoneFrame
      width={phone.width}
      height={phone.height}
      logicalWidth={phone.logicalWidth}
      screenRadius={phone.radius}
      screenBackground={theme.screen}
      className="font-geist"
      style={{ boxShadow: 'inset 0 0 0 1px rgba(255,255,255,0.7)' }}
    >
      <StatusBar color="#111" paddingX={38} paddingTop={21} fontSize={17} timeClassName="pl-[18px]" />
      <DynamicIsland width={100} height={31} top={18} />
      {children}
      {homeIndicator && <HomeIndicator width={138} bottom={7} />}
    </PhoneFrame>
  )
}
