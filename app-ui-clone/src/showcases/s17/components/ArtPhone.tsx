import type { ReactNode } from 'react'
import { PhoneFrame } from '../../../ui'
import { phone, theme } from '../theme'
import { ArtStatusBar } from './ArtStatusBar'

/** Flat, square-cornered screen mockup with a soft drop shadow. */
export function ArtPhone({ background = theme.screen, children }: { background?: string; children?: ReactNode }) {
  return (
    <PhoneFrame
      width={phone.width}
      height={phone.height}
      logicalWidth={phone.logicalWidth}
      screenRadius={phone.radius}
      screenBackground={background}
      className="font-montalt"
      style={{ boxShadow: phone.shadow, borderRadius: phone.radius }}
    >
      <ArtStatusBar />
      {children}
    </PhoneFrame>
  )
}
