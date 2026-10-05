import { ScreenBoard, type AppDefinition } from '../../ui'
import { ChatScreen } from './screens/ChatScreen'
import { DetailScreen } from './screens/DetailScreen'
import { HomeScreen } from './screens/HomeScreen'
import { SalesScreen } from './screens/SalesScreen'

function App04() {
  return (
    <ScreenBoard>
      <HomeScreen />
      <DetailScreen />
      <ChatScreen />
      <SalesScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '04', title: 'Karrot market', screens: 4, Component: App04 }
export default app
