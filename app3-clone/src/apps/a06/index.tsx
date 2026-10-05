import { ScreenBoard, type AppDefinition } from '../../ui'
import { Artist } from './screens/Artist'
import { HomeOffline } from './screens/HomeOffline'
import { NowPlaying } from './screens/NowPlaying'
import { Premium } from './screens/Premium'

function App06() {
  return (
    <ScreenBoard>
      <Premium />
      <HomeOffline />
      <NowPlaying />
      <Artist />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '06', title: 'Spotify', screens: 4, Component: App06 }
export default app
