import type { ComponentType } from 'react'
import { PhoneFrame, Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { DrawerScreen } from './screens/DrawerScreen'
import { FeedScreen } from './screens/FeedScreen'
import { MapHomeScreen } from './screens/MapHomeScreen'
import { SplashScreen } from './screens/SplashScreen'
import { device, theme } from './theme'

const phones: { x: number; Screen: ComponentType }[] = [
  { x: 33, Screen: SplashScreen },
  { x: 401, Screen: () => <MapHomeScreen /> },
  { x: 769, Screen: DrawerScreen },
  { x: 1138, Screen: FeedScreen },
]

function Showcase24() {
  return (
    <Stage width={1512} height={759} background={theme.stage}>
      {phones.map(({ x, Screen }) => (
        <Placed key={x} x={x} y={device.top}>
          <PhoneFrame
            width={device.width}
            height={device.height}
            logicalWidth={device.logicalWidth}
            screenRadius={device.radius}
          >
            <Screen />
          </PhoneFrame>
        </Placed>
      ))}
    </Stage>
  )
}

const showcase: ShowcaseDefinition = {
  id: '24',
  title: 'TADA — 타다 이동 서비스',
  width: 1512,
  height: 759,
  Component: Showcase24,
}
export default showcase
