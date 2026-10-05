import { Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { NaverPhone, naver } from '../shared-naver'
import { QuickPayScreen } from './screens/QuickPayScreen'
import { StoreMethodsScreen } from './screens/StoreMethodsScreen'

const phones = [
  { x: 7, y: 21, Screen: StoreMethodsScreen },
  { x: 427, y: 21, Screen: QuickPayScreen },
]

function Showcase20() {
  return (
    <Stage width={814} height={844} background={naver.stageBg}>
      {phones.map(({ x, y, Screen }) => (
        <Placed key={x} x={x} y={y}>
          <NaverPhone>
            <Screen />
          </NaverPhone>
        </Placed>
      ))}
    </Stage>
  )
}

const showcase: ShowcaseDefinition = {
  id: '20',
  title: 'Naver Pay — 매장별 결제 방법 / 바로결제',
  width: 814,
  height: 844,
  Component: Showcase20,
}
export default showcase
