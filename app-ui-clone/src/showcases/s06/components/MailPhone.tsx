import type { ReactNode } from 'react'
import { HomeIndicator, PhoneFrame, StatusBar } from '../../../ui'

/** Flat white phone (no visible bezel or island) with a soft drop shadow. */
export function MailPhone({ children }: { children?: ReactNode }) {
  return (
    <PhoneFrame
      width={210}
      height={451}
      logicalWidth={375}
      screenRadius={30}
      className="rounded-[30px] shadow-[6px_8px_14px_rgba(0,0,0,0.10),0_1px_3px_rgba(0,0,0,0.05)]"
    >
      <div className="absolute inset-x-0 top-0 z-40">
        <StatusBar color="#000" paddingX={36} paddingTop={25} fontSize={15} className="font-inter" />
      </div>
      {children}
      <HomeIndicator width={128} bottom={8} />
    </PhoneFrame>
  )
}
