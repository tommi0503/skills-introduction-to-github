import { ScreenBoard, type AppDefinition } from '../../ui'
import { HomeScreen } from './screens/HomeScreen'
import { LensScreen } from './screens/LensScreen'
import { ResultsScreen } from './screens/ResultsScreen'
import { SearchScreen } from './screens/SearchScreen'

function Zigzag() {
  return (
    <ScreenBoard>
      <HomeScreen />
      <SearchScreen />
      <ResultsScreen />
      <LensScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '20', title: 'ZIGZAG — fashion shopping', screens: 4, Component: Zigzag }
export default app
