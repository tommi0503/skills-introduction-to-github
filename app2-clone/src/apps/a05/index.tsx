import { ScreenBoard, type AppDefinition } from '../../ui'
import './fonts.css'
import { MapScreen } from './screens/MapScreen'
import { PlaceDetailScreen } from './screens/PlaceDetailScreen'
import { SaveSheetScreen } from './screens/SaveSheetScreen'
import { ShareScreen } from './screens/ShareScreen'

function Corner() {
  return (
    <ScreenBoard>
      <MapScreen />
      <PlaceDetailScreen />
      <SaveSheetScreen />
      <ShareScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '05', title: 'Corner', screens: 4, Component: Corner }
export default app
