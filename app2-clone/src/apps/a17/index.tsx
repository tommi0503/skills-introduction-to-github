import { ScreenBoard, type AppDefinition } from '../../ui'
import { ConversationScreen } from './screens/ConversationScreen'
import { EmptyChatScreen } from './screens/EmptyChatScreen'
import { PlansScreen } from './screens/PlansScreen'
import { ResponseEndScreen } from './screens/ResponseEndScreen'

const screens = [EmptyChatScreen, PlansScreen, ConversationScreen, ResponseEndScreen]

function ClaudeApp() {
  return (
    <ScreenBoard>
      {screens.map((Screen) => (
        <Screen key={Screen.name} />
      ))}
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '17', title: 'Claude', screens: screens.length, Component: ClaudeApp }
export default app
