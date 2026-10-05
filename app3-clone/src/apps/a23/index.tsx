import { ScreenBoard, type AppDefinition } from '../../ui'
import { HomeScreen } from './screens/HomeScreen'
import { ProfileScreen } from './screens/ProfileScreen'

const SCREENS = [HomeScreen, ProfileScreen]

function Board() {
  return (
    <ScreenBoard>
      {SCREENS.map((S, i) => (
        <S key={i} />
      ))}
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '23', title: 'Cal AI', screens: SCREENS.length, Component: Board }
export default app
