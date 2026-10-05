import { Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { FleetPhone } from './components/FleetPhone'
import { AnalyticsScreen } from './screens/AnalyticsScreen'
import { PlannerScreen } from './screens/PlannerScreen'
import { theme } from './theme'

const W = 1024
const H = 768

function Showcase05() {
  return (
    <Stage width={W} height={H} background={theme.stage}>
      <Placed x={261} y={62}>
        <FleetPhone>
          <PlannerScreen />
        </FleetPhone>
      </Placed>
      <Placed x={556} y={184}>
        <FleetPhone>
          <AnalyticsScreen />
        </FleetPhone>
      </Placed>
    </Stage>
  )
}

const showcase: ShowcaseDefinition = { id: '05', title: 'Fleet maintenance planner', width: W, height: H, Component: Showcase05 }
export default showcase
