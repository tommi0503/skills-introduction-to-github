import type { ReactNode } from 'react'
import { DynamicIsland, PhoneFrame, StatusBar } from '../../../ui'
import { theme } from '../theme'

/** Graphite-bezel iPhone (393pt logical) with the app's soft grey screen. */
export function FleetPhone({ children }: { children?: ReactNode }) {
  return (
    <PhoneFrame
      width={254}
      height={522}
      logicalWidth={393}
      screenRadius={32}
      bezel={{ thickness: 12.5, color: theme.bezel, edgeColor: theme.bezelEdge, edgeWidth: 3 }}
      screenBackground={theme.screen}
    >
      <div className="absolute inset-x-0 top-0 z-40">
        <StatusBar color="#111" paddingX={30} paddingTop={21} fontSize={13.5} className="font-inter" timeClassName="!font-medium" battery={{ size: 0.85 }} />
      </div>
      <DynamicIsland width={125} height={37} top={10} />
      {children}
    </PhoneFrame>
  )
}
