import { ScreenBoard, type AppDefinition } from '../../ui'
import { ArticleScreen } from './screens/ArticleScreen'
import { HoroscopeScreen } from './screens/HoroscopeScreen'
import { PaywallScreen } from './screens/PaywallScreen'
import { TransitsScreen } from './screens/TransitsScreen'

function Moonly() {
  return (
    <ScreenBoard>
      <PaywallScreen />
      <TransitsScreen />
      <HoroscopeScreen />
      <ArticleScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '18', title: 'Moonly — astrology & self-discovery', screens: 4, Component: Moonly }
export default app
