import { ScreenBoard, type AppDefinition } from '../../ui'
import { LiveStartTimeScreen } from './screens/LiveStartTimeScreen'
import { SleepScheduleScreen } from './screens/SleepScheduleScreen'
import { WorkoutScheduleScreen } from './screens/WorkoutScheduleScreen'

const SCREENS = [WorkoutScheduleScreen, SleepScheduleScreen, LiveStartTimeScreen]

function Board() {
  return (
    <ScreenBoard>
      {SCREENS.map((S, i) => (
        <S key={i} />
      ))}
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '22', title: 'Date & time pickers', screens: SCREENS.length, Component: Board }
export default app
