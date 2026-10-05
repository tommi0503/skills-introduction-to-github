import { ScreenBoard, type AppDefinition } from '../../ui'
import { BasketsScreen } from './screens/BasketsScreen'

function A13() {
  return (
    <ScreenBoard>
      <BasketsScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '13', title: 'Uber Eats — Baskets', screens: 1, Component: A13 }
export default app
