import { ScreenBoard, type AppDefinition } from '../../ui'
import { WelcomeScreen } from './screens/WelcomeScreen'
import { AddAccountScreen } from './screens/AddAccountScreen'
import { EmailEntryScreen } from './screens/EmailEntryScreen'

function NotionMail() {
  return (
    <ScreenBoard>
      <WelcomeScreen />
      <AddAccountScreen />
      <EmailEntryScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '04', title: 'Notion Mail', screens: 3, Component: NotionMail }
export default app
