import { ScreenBoard, type AppDefinition } from '../../ui'
import { EventScreen } from './screens/EventScreen'
import { LinkScreen } from './screens/LinkScreen'
import { MeetingScreen } from './screens/MeetingScreen'
import { TaskScreen } from './screens/TaskScreen'
import { TrackScreen } from './screens/TrackScreen'

const SCREENS = [TrackScreen, LinkScreen, TaskScreen, EventScreen, MeetingScreen]

function Board() {
  return (
    <ScreenBoard>
      {SCREENS.map((S, i) => (
        <S key={i} />
      ))}
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '24', title: 'Calendar date pickers', screens: SCREENS.length, Component: Board }
export default app
