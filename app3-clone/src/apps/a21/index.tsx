import { ScreenBoard, type AppDefinition } from '../../ui'
import { AccountsScreen } from './screens/AccountsScreen'
import { GmailDialogScreen } from './screens/GmailDialogScreen'
import { GmailIntroScreen } from './screens/GmailIntroScreen'
import { ScheduleScreen } from './screens/ScheduleScreen'
import { SplashScreen } from './screens/SplashScreen'

const SCREENS = [AccountsScreen, GmailIntroScreen, GmailDialogScreen, SplashScreen, ScheduleScreen]

function Board() {
  return (
    <ScreenBoard>
      {SCREENS.map((S, i) => (
        <S key={i} />
      ))}
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '21', title: 'Google Calendar onboarding', screens: SCREENS.length, Component: Board }
export default app
