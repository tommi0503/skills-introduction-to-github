import { ScreenBoard, type AppDefinition } from '../../ui'
import { MeetBotScreen } from './screens/MeetBotScreen'
import { ThreadListScreen } from './screens/ThreadListScreen'
import { ConversationScreen } from './screens/ConversationScreen'

function BotApp() {
  return (
    <ScreenBoard>
      <MeetBotScreen />
      <ThreadListScreen />
      <ConversationScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '07', title: 'Bot chat', screens: 3, Component: BotApp }
export default app
