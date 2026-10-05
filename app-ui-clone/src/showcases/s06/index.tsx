import { Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { MailPhone } from './components/MailPhone'
import { CreateScreen } from './screens/CreateScreen'
import { DraftScreen } from './screens/DraftScreen'
import { InboxScreen } from './screens/InboxScreen'
import { theme } from './theme'

const W = 752
const H = 564

const phones = [
  { key: 'inbox', x: 38, y: 69, Screen: InboxScreen },
  { key: 'create', x: 271, y: 43, Screen: CreateScreen },
  { key: 'draft', x: 504, y: 69, Screen: DraftScreen },
]

function Showcase06() {
  return (
    <Stage width={W} height={H} background={theme.stage}>
      {phones.map(({ key, x, y, Screen }) => (
        <Placed key={key} x={x} y={y}>
          <MailPhone>
            <Screen />
          </MailPhone>
        </Placed>
      ))}
    </Stage>
  )
}

const showcase: ShowcaseDefinition = { id: '06', title: 'AI email assistant', width: W, height: H, Component: Showcase06 }
export default showcase
