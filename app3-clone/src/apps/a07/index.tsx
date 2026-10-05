import { ScreenBoard, type AppDefinition } from '../../ui'
import { AddMoney } from './screens/AddMoney'
import { CardPicker } from './screens/CardPicker'
import { Home } from './screens/Home'
import { MonthlyLimit } from './screens/MonthlyLimit'

function App07() {
  return (
    <ScreenBoard>
      <CardPicker />
      <Home />
      <AddMoney />
      <MonthlyLimit />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '07', title: 'Revolut', screens: 4, Component: App07 }
export default app
