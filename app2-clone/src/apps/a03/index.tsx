import { ScreenBoard, type AppDefinition } from '../../ui'
import { BitcoinMenuScreen } from './screens/BitcoinMenuScreen'
import { BitcoinScreen } from './screens/BitcoinScreen'
import { OnboardingScreen } from './screens/OnboardingScreen'
import { OptionsScreen } from './screens/OptionsScreen'
import { PortfolioScreen } from './screens/PortfolioScreen'

function Public() {
  return (
    <ScreenBoard>
      <OnboardingScreen />
      <PortfolioScreen />
      <OptionsScreen />
      <BitcoinScreen />
      <BitcoinMenuScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '03', title: 'Public', screens: 5, Component: Public }
export default app
