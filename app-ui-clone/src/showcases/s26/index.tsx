import type { ComponentType } from 'react'
import { PhoneFrame, Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { CartScreen } from './screens/CartScreen'
import { HomeScreen } from './screens/HomeScreen'
import { KeepingScreen } from './screens/KeepingScreen'
import { ProductScreen } from './screens/ProductScreen'
import { cu, device } from './theme'

interface PhoneSlot {
  x: number
  width: number
  Screen: ComponentType
}

const phones: PhoneSlot[] = [
  { x: 13, width: 269, Screen: HomeScreen },
  { x: 306, width: 270, Screen: ProductScreen },
  { x: 600, width: 269, Screen: CartScreen },
  { x: 893, width: 270, Screen: KeepingScreen },
]

function Showcase26() {
  return (
    <Stage width={1171} height={603} background={cu.stage}>
      {phones.map(({ x, width, Screen }) => (
        <Placed key={x} x={x} y={21}>
          <PhoneFrame width={width} height={device.height} logicalWidth={device.logicalWidth} screenRadius={device.screenRadius}>
            <Screen />
          </PhoneFrame>
        </Placed>
      ))}
    </Stage>
  )
}

const showcase: ShowcaseDefinition = {
  id: '26',
  title: 'CU convenience store app',
  width: 1171,
  height: 603,
  Component: Showcase26,
}

export default showcase
