import type { ReactNode } from 'react'
import { PhoneFrame, StatusBar } from '../../../ui'

export interface BarberPhoneProps {
  background: string
  statusColor?: string
  children?: ReactNode
}

/** Thin-edged device used for all three screens of this showcase (375pt logical). */
export function BarberPhone({ background, statusColor = '#000', children }: BarberPhoneProps) {
  return (
    <PhoneFrame
      width={202}
      height={438}
      logicalWidth={375}
      screenRadius={3}
      screenBackground={background}
      className="shadow-[0_6px_18px_rgba(0,0,0,0.12)]"
    >
      <div className="absolute inset-0 font-urbanist">
        <StatusBar color={statusColor} fontSize={15} paddingTop={14} paddingX={30} height={44} />
        {children}
      </div>
    </PhoneFrame>
  )
}
