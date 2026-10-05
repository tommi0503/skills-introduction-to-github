import { Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { NaverPhone, naver } from '../shared-naver'
import { eventsB } from './data'
import { MethodSheetScreen } from './screens/MethodSheetScreen'
import { PayCodeScreen } from './screens/PayCodeScreen'
import { PointHomeScreen } from './screens/PointHomeScreen'
import { t19 } from './theme'

const phones = [
  { x: 7, y: 18, screen: <PayCodeScreen time="1:33" front="point" scrollIndicator /> },
  { x: 427, y: 18, screen: <PointHomeScreen /> },
  { x: 847, y: 18, screen: <PayCodeScreen time="1:31" front="card" events={eventsB} withNav statusColor="#2b3037" eventsLeft={8.3} /> },
  { x: 1267, y: 7, screen: <MethodSheetScreen /> },
]

function Showcase19() {
  return (
    <Stage width={1660} height={841} background={naver.stageBg}>
      {phones.map(({ x, y, screen }) => (
        <Placed key={x} x={x} y={y}>
          <NaverPhone background={t19.screen}>{screen}</NaverPhone>
        </Placed>
      ))}
    </Stage>
  )
}

const showcase: ShowcaseDefinition = {
  id: '19',
  title: 'Naver Pay — 현장결제 (dark)',
  width: 1660,
  height: 841,
  Component: Showcase19,
}
export default showcase
