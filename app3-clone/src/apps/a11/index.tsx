import { ScreenBoard, type AppDefinition } from '../../ui'
import { DeliveryRatingScreen } from './screens/DeliveryRatingScreen'
import { PaymentCalculatorScreen } from './screens/PaymentCalculatorScreen'
import { RunFeedbackScreen } from './screens/RunFeedbackScreen'
import { SupportRatingScreen } from './screens/SupportRatingScreen'

function App11() {
  return (
    <ScreenBoard>
      <PaymentCalculatorScreen />
      <SupportRatingScreen />
      <DeliveryRatingScreen />
      <RunFeedbackScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '11', title: 'Feedback bottom sheets', screens: 4, Component: App11 }
export default app
