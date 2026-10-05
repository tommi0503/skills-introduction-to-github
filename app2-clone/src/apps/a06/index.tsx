import { ScreenBoard, type AppDefinition } from '../../ui'
import { HomeScreen } from './screens/HomeScreen'
import { SearchScreen } from './screens/SearchScreen'

function Baemin() {
  return (
    <ScreenBoard>
      <HomeScreen />
      <SearchScreen />
      <HomeScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '06', title: '배달의민족', screens: 3, Component: Baemin }
export default app
