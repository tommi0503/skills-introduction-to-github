import { ScreenBoard, type AppDefinition } from '../../ui'
import { Checkout } from './screens/Checkout'
import { RequestToBook } from './screens/RequestToBook'

function App08() {
  return (
    <ScreenBoard>
      <RequestToBook />
      <Checkout />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '08', title: 'Booking & checkout', screens: 2, Component: App08 }
export default app
