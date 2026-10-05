import { ScreenBoard, type AppDefinition } from '../../ui'
import { CartScreen } from './screens/CartScreen'

function App12() {
  return (
    <ScreenBoard>
      <CartScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '12', title: 'Shopping cart', screens: 1, Component: App12 }
export default app
