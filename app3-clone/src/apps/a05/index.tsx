import { ScreenBoard, type AppDefinition } from '../../ui'
import { Welcome } from './screens/Welcome'
import { Home } from './screens/Home'
import { StoreScreen } from './screens/StoreScreen'
import { GroupOrder } from './screens/GroupOrder'

function App05() {
  return (
    <ScreenBoard>
      <Welcome />
      <Home />
      <StoreScreen />
      <GroupOrder />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '05', title: 'Uber Eats', screens: 4, Component: App05 }
export default app
