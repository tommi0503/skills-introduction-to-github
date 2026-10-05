import { Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { TravioPhone } from './components/TravioPhone'
import { ChatScreen } from './screens/ChatScreen'
import { DatesScreen } from './screens/DatesScreen'
import { WhereToScreen } from './screens/WhereToScreen'

const W = 1024
const H = 768

const phones = [
  { key: 'where', x: 73, y: 161, Screen: WhereToScreen },
  { key: 'chat', x: 384, y: 89, Screen: ChatScreen },
  { key: 'dates', x: 695, y: 73, Screen: DatesScreen },
]

function Showcase02() {
  return (
    <Stage width={W} height={H} background="linear-gradient(90deg, #edeee9 0%, #f0f1ec 50%, #f4f5f0 100%)">
      {phones.map(({ key, x, y, Screen }) => (
        <Placed key={key} x={x} y={y}>
          <TravioPhone>
            <Screen />
          </TravioPhone>
        </Placed>
      ))}
    </Stage>
  )
}

const showcase: ShowcaseDefinition = { id: '02', title: 'Travio AI — travel planner', width: W, height: H, Component: Showcase02 }
export default showcase
