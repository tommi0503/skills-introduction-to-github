import { ScreenBoard, type AppDefinition } from '../../ui'
import { CalendarScreen } from './screens/CalendarScreen'
import { MatchScreen } from './screens/MatchScreen'
import { PaywallScreen } from './screens/PaywallScreen'
import { ShareScreen } from './screens/ShareScreen'

function Fixtured() {
  return (
    <ScreenBoard>
      <CalendarScreen />
      <PaywallScreen />
      <MatchScreen />
      <ShareScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '19', title: 'Fixtured — sports calendar', screens: 4, Component: Fixtured }
export default app
