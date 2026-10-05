import { ScreenBoard, type AppDefinition } from '../../ui'
import { HomeScreen } from './screens/HomeScreen'
import { OrderScreen } from './screens/OrderScreen'
import { LostModeScreen } from './screens/LostModeScreen'
import { RestScreen } from './screens/RestScreen'

function Fi() {
  return (
    <ScreenBoard>
      <HomeScreen />
      <OrderScreen />
      <LostModeScreen />
      <RestScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '19', title: 'Fi', screens: 4, Component: Fi }
export default app
