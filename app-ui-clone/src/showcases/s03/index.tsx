import { Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { FlatScreen } from './components/FlatScreen'
import { ChallengesScreen } from './screens/ChallengesScreen'
import { MorningScreen } from './screens/MorningScreen'
import { ProgressScreen } from './screens/ProgressScreen'
import { theme } from './theme'

const W = 1024
const H = 768

const screens = [
  { key: 'progress', x: 111, Screen: ProgressScreen },
  { key: 'morning', x: 393, Screen: MorningScreen },
  { key: 'challenges', x: 675, Screen: ChallengesScreen },
]

function Showcase03() {
  return (
    <Stage width={W} height={H} background={theme.stage}>
      {screens.map(({ key, x, Screen }) => (
        <Placed key={key} x={x} y={126}>
          <FlatScreen>
            <Screen />
          </FlatScreen>
        </Placed>
      ))}
    </Stage>
  )
}

const showcase: ShowcaseDefinition = { id: '03', title: 'Habit streak app', width: W, height: H, Component: Showcase03 }
export default showcase
