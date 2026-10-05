import { Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { ArtPhone } from './components/ArtPhone'
import { ArtworkScreen } from './screens/ArtworkScreen'
import { GalleryScreen } from './screens/GalleryScreen'
import { MuseumScreen } from './screens/MuseumScreen'
import { theme } from './theme'

const phones = [
  { key: 'museum', x: 53.5, y: 75, Screen: MuseumScreen },
  { key: 'gallery', x: 278, y: 51, Screen: GalleryScreen },
  { key: 'artwork', x: 506.5, y: 60, Screen: ArtworkScreen },
]

function Showcase17() {
  return (
    <Stage width={752} height={564} background={theme.stage}>
      {phones.map(({ key, x, y, Screen }) => (
        <Placed key={key} x={x} y={y}>
          <ArtPhone>
            <Screen />
          </ArtPhone>
        </Placed>
      ))}
    </Stage>
  )
}

const showcase: ShowcaseDefinition = {
  id: '17',
  title: 'Art gallery app',
  width: 752,
  height: 564,
  Component: Showcase17,
}
export default showcase
