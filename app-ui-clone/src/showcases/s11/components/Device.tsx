import type { ReactNode } from 'react'
import { DynamicIsland, PhoneFrame } from '../../../ui'
import { device, theme } from '../theme'

/** Graphite iPhone with side buttons; the screen content is injected. */
export function Device({ children }: { children: ReactNode }) {
  return (
    <div className="relative">
      {[
        { top: 88, h: 14 },
        { top: 116, h: 28 },
        { top: 152, h: 28 },
      ].map((b) => (
        <span key={b.top} className="absolute left-[-2px] w-[3px] rounded-l-[1px] bg-[#8d8b8b]" style={{ top: b.top, height: b.h }} />
      ))}
      <span className="absolute right-[-2px] w-[3px] rounded-r-[1px] bg-[#8d8b8b]" style={{ top: 130, height: 44 }} />
      <PhoneFrame
        width={device.width}
        height={device.height}
        logicalWidth={device.logicalWidth}
        screenRadius={device.screenRadius}
        bezel={device.bezel}
        screenBackground={theme.screen}
        style={{ boxShadow: `inset 0 0 0 ${device.bezel.edgeWidth}px ${device.bezel.edgeColor}, ${theme.phoneShadow}` }}
      >
        {children}
        <DynamicIsland width={123} height={36} top={13} />
      </PhoneFrame>
    </div>
  )
}
