import type { AppDefinition } from '../../ui'
import { ScreenBoard } from '../../ui'
import { FallingTideScreen } from './screens/FallingTideScreen'
import { StationMap } from './screens/StationMap'
import { StationSelected } from './screens/StationSelected'
import { TideList } from './screens/TideList'
import { WindScreen } from './screens/WindScreen'

function TideGuide() {
  return (
    <ScreenBoard>
      <TideList />
      <StationMap />
      <StationSelected />
      <WindScreen />
      <FallingTideScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '11', title: 'Tide Guide', screens: 5, Component: TideGuide }
export default app
