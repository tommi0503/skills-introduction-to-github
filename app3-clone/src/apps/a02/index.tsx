import { ScreenBoard, type AppDefinition } from '../../ui'
import { EvidenceScreen } from './screens/EvidenceScreen'
import { ReviewRefundScreen } from './screens/ReviewRefundScreen'

function App02() {
  return (
    <ScreenBoard>
      <ReviewRefundScreen />
      <EvidenceScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '02', title: 'Refund review', screens: 2, Component: App02 }
export default app
