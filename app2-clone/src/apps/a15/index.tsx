import { ScreenBoard, type AppDefinition } from '../../ui'
import { Destination } from './screens/Destination'
import { Home } from './screens/Home'
import { RideOptions } from './screens/RideOptions'
import { Upsell } from './screens/Upsell'

function LyftBoard() {
  return (
    <ScreenBoard>
      <Home />
      <Destination />
      <RideOptions />
      <Upsell />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '15', title: 'Lyft', screens: 4, Component: LyftBoard }
export default app
