import { Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { FoodPhone } from './components/FoodPhone'
import { AskAiScreen } from './screens/AskAiScreen'
import { ExploreScreen } from './screens/ExploreScreen'
import { HomeScreen } from './screens/HomeScreen'
import { theme } from './theme'

const phones = [
  { key: 'explore', x: 34.75, y: 81.5, rotate: -1.7, Screen: ExploreScreen, homeIndicator: true },
  { key: 'home', x: 272, y: 33, rotate: 0, Screen: HomeScreen, homeIndicator: false },
  { key: 'ask', x: 509.5, y: 84, rotate: 3, Screen: AskAiScreen, homeIndicator: true },
]

function Showcase18() {
  return (
    <Stage width={752} height={564} background={theme.stage}>
      {phones.map(({ key, x, y, rotate, Screen, homeIndicator }) => (
        <Placed key={key} x={x} y={y} rotate={rotate}>
          <FoodPhone homeIndicator={homeIndicator}>
            <Screen />
          </FoodPhone>
        </Placed>
      ))}
    </Stage>
  )
}

const showcase: ShowcaseDefinition = {
  id: '18',
  title: 'AI food recommendation app',
  width: 752,
  height: 564,
  Component: Showcase18,
}
export default showcase
