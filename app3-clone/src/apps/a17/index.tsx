import { ScreenBoard, type AppDefinition } from '../../ui'
import { AskScreen } from './screens/AskScreen'
import { InboxScreen } from './screens/InboxScreen'
import { PaywallScreen } from './screens/PaywallScreen'
import { WelcomeScreen } from './screens/WelcomeScreen'

function Beside() {
  return (
    <ScreenBoard>
      <WelcomeScreen />
      <PaywallScreen />
      <InboxScreen />
      <AskScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '17', title: 'Beside — AI phone assistant', screens: 4, Component: Beside }
export default app
