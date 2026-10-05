import { ScreenBoard, type AppDefinition } from '../../ui'
import { EditorScreen } from './screens/EditorScreen'
import { LensScreen } from './screens/LensScreen'
import { LibraryScreen } from './screens/LibraryScreen'
import { ViewerScreen } from './screens/ViewerScreen'

const screens = [LibraryScreen, ViewerScreen, EditorScreen, LensScreen]

function GooglePhotos() {
  return (
    <ScreenBoard>
      {screens.map((Screen) => (
        <Screen key={Screen.name} />
      ))}
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '18', title: 'Google Photos & Lens', screens: screens.length, Component: GooglePhotos }
export default app
