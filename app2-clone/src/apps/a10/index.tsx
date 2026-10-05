import type { AppDefinition } from '../../ui'
import { ScreenBoard } from '../../ui'
import { AddFlight } from './screens/AddFlight'
import { AirportDetail } from './screens/AirportDetail'
import { Airports } from './screens/Airports'
import { MyFlights } from './screens/MyFlights'

function Flighty() {
  return (
    <ScreenBoard>
      <AddFlight />
      <MyFlights />
      <Airports />
      <AirportDetail />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '10', title: 'Flighty', screens: 4, Component: Flighty }
export default app
