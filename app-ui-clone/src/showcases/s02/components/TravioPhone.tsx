import type { ReactNode } from 'react'
import { HomeIndicator, PhoneFrame, StatusBar } from '../../../ui'
import { device, theme } from '../theme'

/** White frameless phone with soft drop shadow used for every Travio screen. */
export function TravioPhone({ children }: { children: ReactNode }) {
  return (
    <PhoneFrame
      width={device.width}
      height={device.height}
      logicalWidth={device.logicalWidth}
      screenRadius={device.radius}
      screenBackground={theme.screen}
      className="rounded-[40px] shadow-[0_8px_24px_rgba(60,60,40,0.10),0_0_0_1px_rgba(0,0,0,0.035)]"
    >
      <div className="absolute inset-0 font-inter text-[#161616]">{children}</div>
      <div className="absolute inset-x-0 top-0">
        <StatusBar paddingX={56} paddingTop={24} fontSize={15.5} height={50} className="pr-[38px]!" timeClassName="font-semibold" />
      </div>
      <HomeIndicator width={129} bottom={12} />
    </PhoneFrame>
  )
}
