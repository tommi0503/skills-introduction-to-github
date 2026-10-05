import { ScreenBoard, type AppDefinition } from '../../ui'
import { ExploreScreen } from './screens/ExploreScreen'
import { StreakPaywallScreen } from './screens/StreakPaywallScreen'
import { TrialPaywallScreen } from './screens/TrialPaywallScreen'

function A14() {
  return (
    <ScreenBoard>
      <ExploreScreen />
      <StreakPaywallScreen />
      <TrialPaywallScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '14', title: 'Stays explore & premium paywalls', screens: 3, Component: A14 }
export default app
