import { ScreenBoard, type AppDefinition } from '../../ui'
import { SignInScreen } from './screens/SignInScreen'
import { HomeScreen } from './screens/HomeScreen'
import { IssueScreen } from './screens/IssueScreen'
import { DiffScreen } from './screens/DiffScreen'
import { CopilotScreen } from './screens/CopilotScreen'

function GitHubApp() {
  return (
    <ScreenBoard>
      <SignInScreen />
      <HomeScreen />
      <IssueScreen />
      <DiffScreen />
      <CopilotScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '08', title: 'GitHub', screens: 5, Component: GitHubApp }
export default app
