import { Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { Device } from './components/Device'
import { CameraScreen } from './screens/CameraScreen'
import { LibraryScreen } from './screens/LibraryScreen'
import { ReviewScreen } from './screens/ReviewScreen'
import { theme } from './theme'

const phones = [
  { key: 'camera', x: 47, y: 62, Screen: CameraScreen },
  { key: 'library', x: 274, y: 40, Screen: LibraryScreen },
  { key: 'review', x: 503, y: 62, Screen: ReviewScreen },
]

function Showcase07() {
  return (
    <Stage width={752} height={564} background={theme.stageBg}>
      {phones.map(({ key, x, y, Screen }) => (
        <Placed key={key} x={x} y={y}>
          <Device>
            <Screen />
          </Device>
        </Placed>
      ))}
    </Stage>
  )
}

const definition: ShowcaseDefinition = {
  id: '07',
  title: 'Document scanner — capture, library, review & crop',
  width: 752,
  height: 564,
  Component: Showcase07,
}
export default definition
