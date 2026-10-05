import type { ReactNode } from 'react'
import { PhoneFrame } from '../../../ui'
import { screen } from '../theme'

/** Square-cornered white screen (no device chrome), scaled from 375pt. */
export function FlatScreen({ children }: { children: ReactNode }) {
  return (
    <PhoneFrame width={screen.width} height={screen.height} logicalWidth={screen.logicalWidth} screenRadius={0}>
      <div className="absolute inset-0 font-jakarta text-[#151518]">{children}</div>
    </PhoneFrame>
  )
}
