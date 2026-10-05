import { ScreenBoard, type AppDefinition } from '../../ui'
import { HomeScreen } from './screens/HomeScreen'
import { CategoryScreen } from './screens/CategoryScreen'
import { GigScreen } from './screens/GigScreen'
import { SellerScreen } from './screens/SellerScreen'

function FiverrApp() {
  return (
    <ScreenBoard>
      <HomeScreen />
      <CategoryScreen />
      <GigScreen />
      <SellerScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '09', title: 'Fiverr', screens: 4, Component: FiverrApp }
export default app
