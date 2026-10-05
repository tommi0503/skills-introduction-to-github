import { ScreenBoard, type AppDefinition } from '../../ui'
import { Home } from './screens/Home'
import { Intro } from './screens/Intro'
import { Locations } from './screens/Locations'
import { Paywall } from './screens/Paywall'

function NordBoard() {
  return (
    <ScreenBoard>
      <Intro />
      <Paywall />
      <Home />
      <Locations />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '14', title: 'NordVPN', screens: 4, Component: NordBoard }
export default app
