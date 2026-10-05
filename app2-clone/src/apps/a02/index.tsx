import { ScreenBoard, type AppDefinition } from '../../ui'
import { ChatScreen } from './screens/ChatScreen'
import { HomeScreen } from './screens/HomeScreen'
import { PlannerScreen } from './screens/PlannerScreen'
import { TripsScreen } from './screens/TripsScreen'
import { WelcomeScreen } from './screens/WelcomeScreen'

function Mindtrip() {
  return (
    <ScreenBoard>
      <WelcomeScreen />
      <HomeScreen />
      <ChatScreen />
      <PlannerScreen />
      <TripsScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '02', title: 'Mindtrip', screens: 5, Component: Mindtrip }
export default app
