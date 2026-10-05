import { ScreenBoard, type AppDefinition } from '../../ui'
import { Onboarding } from './screens/Onboarding'
import { Home } from './screens/Home'
import { SearchResults } from './screens/SearchResults'
import { SpendingPower } from './screens/SpendingPower'

function ZipBoard() {
  return (
    <ScreenBoard>
      <Onboarding />
      <Home />
      <SearchResults />
      <SpendingPower />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '13', title: 'Zip — pay in 4', screens: 4, Component: ZipBoard }
export default app
