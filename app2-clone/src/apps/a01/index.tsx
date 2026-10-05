import { ScreenBoard, type AppDefinition } from '../../ui'
import { HomeScreen } from './screens/HomeScreen'
import { SignUpScreen } from './screens/SignUpScreen'

function Rakuten() {
  return (
    <ScreenBoard>
      <HomeScreen />
      <SignUpScreen />
      <SignUpScreen filled />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '01', title: 'Rakuten', screens: 3, Component: Rakuten }
export default app
