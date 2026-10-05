import { ScreenBoard, type AppDefinition } from '../../ui'
import { FeedScreen } from './screens/FeedScreen'
import { ListingScreen } from './screens/ListingScreen'
import { ReviewScreen } from './screens/ReviewScreen'
import { WhereScreen } from './screens/WhereScreen'

function A15() {
  return (
    <ScreenBoard>
      <FeedScreen />
      <WhereScreen />
      <ListingScreen />
      <ReviewScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '15', title: 'Stays booking flow', screens: 4, Component: A15 }
export default app
