import { ScreenBoard, type AppDefinition } from '../../ui'
import { DigitCodeScreen } from './screens/DigitCodeScreen'
import { SmsCodeScreen } from './screens/SmsCodeScreen'

function App09() {
  return (
    <ScreenBoard>
      <SmsCodeScreen />
      <DigitCodeScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '09', title: 'SMS verification code', screens: 2, Component: App09 }
export default app
