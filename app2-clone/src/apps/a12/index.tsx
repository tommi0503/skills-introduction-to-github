import type { AppDefinition } from '../../ui'
import { ScreenBoard } from '../../ui'
import { JourneyScreen } from './screens/JourneyScreen'
import { MomentumScreen } from './screens/MomentumScreen'
import { SeasonScreen } from './screens/SeasonScreen'
import { TodayScreen } from './screens/TodayScreen'

function LifeReset() {
  return (
    <ScreenBoard>
      <TodayScreen />
      <MomentumScreen />
      <JourneyScreen />
      <SeasonScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '12', title: 'Life Reset', screens: 4, Component: LifeReset }
export default app
