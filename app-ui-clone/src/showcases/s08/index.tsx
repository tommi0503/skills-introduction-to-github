import { Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { Device } from './components/Device'
import { DetailScreen } from './screens/DetailScreen'
import { HomeScreen } from './screens/HomeScreen'
import { SearchScreen } from './screens/SearchScreen'
import { theme } from './theme'

const phones = [
  { key: 'home', x: 46, y: 40, Screen: HomeScreen },
  { key: 'detail', x: 275, y: 62, Screen: DetailScreen },
  { key: 'search', x: 502, y: 84, Screen: SearchScreen },
]

function Showcase08() {
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
  id: '08',
  title: 'MARQET — vintage marketplace',
  width: 752,
  height: 564,
  Component: Showcase08,
}
export default definition
