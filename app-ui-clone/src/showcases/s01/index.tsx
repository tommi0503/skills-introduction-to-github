import { ImagePlaceholder, Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { RentiquePhone } from './components/RentiquePhone'
import { HomeScreen } from './screens/HomeScreen'
import { SearchScreen } from './screens/SearchScreen'

const W = 1024
const H = 768

function Showcase01() {
  return (
    <Stage width={W} height={H}>
      <ImagePlaceholder className="absolute inset-0" label="blurred fashion photo background" />
      <Placed x={184} y={43}>
        <RentiquePhone statusColor="#000">
          <HomeScreen />
        </RentiquePhone>
      </Placed>
      <Placed x={526} y={43}>
        <RentiquePhone>
          <SearchScreen />
        </RentiquePhone>
      </Placed>
    </Stage>
  )
}

const showcase: ShowcaseDefinition = { id: '01', title: 'Rentique — fashion rental', width: W, height: H, Component: Showcase01 }
export default showcase
