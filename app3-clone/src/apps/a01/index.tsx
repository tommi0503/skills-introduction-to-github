import { ScreenBoard, type AppDefinition } from '../../ui'
import { FeedScreen } from './screens/FeedScreen'
import { NewPostScreen } from './screens/NewPostScreen'
import { ReelPostScreen } from './screens/ReelPostScreen'
import { StoryCameraScreen } from './screens/StoryCameraScreen'

function App01() {
  return (
    <ScreenBoard>
      <FeedScreen />
      <ReelPostScreen />
      <StoryCameraScreen />
      <NewPostScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '01', title: 'Instagram', screens: 4, Component: App01 }
export default app
