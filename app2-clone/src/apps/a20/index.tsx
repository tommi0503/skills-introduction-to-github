import { ScreenBoard, type AppDefinition } from '../../ui'
import { SignInScreen } from './screens/SignInScreen'
import { DocumentsScreen } from './screens/DocumentsScreen'
import { NewFolderScreen } from './screens/NewFolderScreen'
import { AudioClipScreen } from './screens/AudioClipScreen'
import { AiChatScreen } from './screens/AiChatScreen'

function Goodnotes() {
  return (
    <ScreenBoard>
      <SignInScreen />
      <DocumentsScreen />
      <NewFolderScreen />
      <AudioClipScreen />
      <AiChatScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '20', title: 'Goodnotes', screens: 5, Component: Goodnotes }
export default app
