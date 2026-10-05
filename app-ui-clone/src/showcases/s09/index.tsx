import type { ComponentType } from 'react'
import { Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { Device } from './components/Device'
import { quinoa, quinoaCompact } from './data'
import { BlankScreen } from './screens/BlankScreen'
import { CartScreen } from './screens/CartScreen'
import { HomeScreen } from './screens/HomeScreen'
import { MapScreen } from './screens/MapScreen'
import { ProductScreen } from './screens/ProductScreen'
import { QuizScreen } from './screens/QuizScreen'
import { theme } from './theme'

const ProductMain = () => <ProductScreen product={quinoa} />
const ProductCompact = () => <ProductScreen product={quinoaCompact} sheetTop={116} scroll={268.3} footerBottom={37} />

interface PhoneSlot {
  key: string
  x: number
  y: number
  height?: number
  Screen: ComponentType
}

/** Board layout: a staggered wall of phones, several cropped by the canvas edge. */
const slots: PhoneSlot[] = [
  { key: 'cart', x: -108, y: 154, Screen: CartScreen },
  { key: 'home', x: 91.5, y: 102.5, Screen: HomeScreen },
  { key: 'quiz', x: 91.5, y: 502, Screen: QuizScreen },
  { key: 'product', x: 290, y: 48, height: 496, Screen: ProductMain },
  { key: 'map', x: 489, y: 102.5, Screen: MapScreen },
  { key: 'home-2', x: 489, y: 502, Screen: HomeScreen },
  { key: 'product-2', x: 686, y: 154, Screen: ProductCompact },
  { key: 'blank-left', x: -108, y: 553, Screen: BlankScreen },
  { key: 'blank-right', x: 686, y: 552.5, Screen: BlankScreen },
]

function Showcase09() {
  return (
    <Stage width={752} height={564} background={theme.stage}>
      {slots.map(({ key, x, y, height, Screen }) => (
        <Placed key={key} x={x} y={y}>
          <Device height={height}>
            <Screen />
          </Device>
        </Placed>
      ))}
    </Stage>
  )
}

const definition: ShowcaseDefinition = {
  id: '09',
  title: 'TheKitchen~ — food ordering board',
  width: 752,
  height: 564,
  Component: Showcase09,
}
export default definition
