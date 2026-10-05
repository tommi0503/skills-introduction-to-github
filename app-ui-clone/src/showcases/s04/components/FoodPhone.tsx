import type { ReactNode } from 'react'
import { DynamicIsland, HomeIndicator, PhoneFrame, StatusBar } from '../../../ui'
import { theme } from '../theme'

export interface FoodPhoneProps {
  width?: number
  height?: number
  screenBackground?: string
  statusColor?: string
  indicatorTone?: 'dark' | 'light'
  showIndicator?: boolean
  children?: ReactNode
}

/** Black-bezel iPhone used by all three Food Zone screens (375pt logical width). */
export function FoodPhone({
  width = 282,
  height = 588,
  screenBackground = '#fff',
  statusColor = '#fff',
  indicatorTone = 'dark',
  showIndicator = true,
  children,
}: FoodPhoneProps) {
  return (
    <PhoneFrame
      width={width}
      height={height}
      logicalWidth={375}
      screenRadius={37}
      bezel={{ thickness: 9, color: theme.bezel, edgeColor: theme.bezelEdge, edgeWidth: 1.6 }}
      screenBackground={screenBackground}
    >
      <div className="absolute inset-x-0 top-0 z-40">
        <StatusBar color={statusColor} paddingX={30} paddingTop={14} fontSize={15} className="font-inter" />
      </div>
      <DynamicIsland width={122} height={35} top={11} />
      {children}
      {showIndicator && <HomeIndicator tone={indicatorTone} width={136} bottom={7} />}
    </PhoneFrame>
  )
}
