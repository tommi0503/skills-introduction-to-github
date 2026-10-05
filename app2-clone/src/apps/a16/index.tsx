import { ScreenBoard, type AppDefinition } from '../../ui'
import { HomeScreen } from './screens/HomeScreen'
import { PaywallScreen } from './screens/PaywallScreen'
import { TravelScreen } from './screens/TravelScreen'
import { WelcomeScreen } from './screens/WelcomeScreen'

const screens = [WelcomeScreen, PaywallScreen, HomeScreen, TravelScreen]

function ElevenReader() {
  return (
    <ScreenBoard>
      {screens.map((Screen) => (
        <Screen key={Screen.name} />
      ))}
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '16', title: 'ElevenReader', screens: screens.length, Component: ElevenReader }
export default app
