import type { ComponentType } from 'react'
import { PhoneFrame, Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { PeekPhone } from './components/PeekPhone'
import { DetailScreen } from './screens/DetailScreen'
import { DiscoverScreen } from './screens/DiscoverScreen'
import { HomeScreen } from './screens/HomeScreen'
import { PlaceScreen } from './screens/PlaceScreen'
import { SplashScreen } from './screens/SplashScreen'
import { bond, device } from './theme'

interface PhoneSlot {
  x: number
  width: number
  Screen: ComponentType
}

const phones: PhoneSlot[] = [
  { x: 13, width: 270, Screen: SplashScreen },
  { x: 307, width: 269, Screen: HomeScreen },
  { x: 600, width: 270, Screen: DiscoverScreen },
  { x: 894, width: 269, Screen: PlaceScreen },
  { x: 1187, width: 270, Screen: DetailScreen },
]

function Showcase25() {
  return (
    <Stage width={1502} height={615} background={bond.stage}>
      {/* sliver of a cropped chip at the top edge of the source capture */}
      <Placed x={438} y={0} width={81} height={1} style={{ background: '#3a3a3a' }} />
      {phones.map(({ x, width, Screen }) => (
        <Placed key={x} x={x} y={23}>
          <PhoneFrame width={width} height={device.height} logicalWidth={device.logicalWidth} screenRadius={device.screenRadius}>
            <Screen />
          </PhoneFrame>
        </Placed>
      ))}
      <Placed x={1481} y={23}>
        <PeekPhone caption="e number" hint="88  88" />
      </Placed>
    </Stage>
  )
}

const showcase: ShowcaseDefinition = {
  id: '25',
  title: 'bond — social memories app',
  width: 1502,
  height: 615,
  Component: Showcase25,
}

export default showcase
