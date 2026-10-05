import type { ReactNode } from 'react'
import { HomeIndicator, PhoneFrame, StatusBar } from '../../../ui'
import { phone, theme } from '../theme'

/** White rounded phone used by all three screens. */
export function FoodPhone({ homeIndicator = true, children }: { homeIndicator?: boolean; children?: ReactNode }) {
  return (
    <PhoneFrame
      width={phone.width}
      height={phone.height}
      logicalWidth={phone.logicalWidth}
      screenRadius={phone.radius}
      screenBackground={theme.screen}
      className="font-inter"
      style={{ boxShadow: '0 1px 2px rgba(0,0,0,0.04)' }}
    >
      <StatusBar color="#111" paddingX={40} paddingTop={18} fontSize={16.5} timeClassName="pl-[18px]" />
      {children}
      {homeIndicator && <HomeIndicator width={136} bottom={5} />}
    </PhoneFrame>
  )
}
