import { Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { DeliveryPhone } from './components/DeliveryPhone'
import { DeliveryDetailsScreen } from './screens/DeliveryDetailsScreen'
import { DiscoverScreen } from './screens/DiscoverScreen'
import { LocationScreen } from './screens/LocationScreen'
import { theme } from './theme'

const phones = [
  { key: 'location', x: 37.5, y: 68, Screen: LocationScreen, homeIndicator: true },
  { key: 'details', x: 270.5, y: 37, Screen: DeliveryDetailsScreen, homeIndicator: false },
  { key: 'discover', x: 503, y: 68, Screen: DiscoverScreen, homeIndicator: false },
]

function Showcase16() {
  return (
    <Stage width={752} height={564} background={theme.stage}>
      {phones.map(({ key, x, y, Screen, homeIndicator }) => (
        <Placed key={key} x={x} y={y}>
          <DeliveryPhone homeIndicator={homeIndicator}>
            <Screen />
          </DeliveryPhone>
        </Placed>
      ))}
    </Stage>
  )
}

const showcase: ShowcaseDefinition = {
  id: '16',
  title: 'Delivery & shipment app',
  width: 752,
  height: 564,
  Component: Showcase16,
}
export default showcase
