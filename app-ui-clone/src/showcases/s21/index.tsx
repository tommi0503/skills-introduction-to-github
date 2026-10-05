import { Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { NaverPhone, naver } from '../shared-naver'
import { AlertDoneScreen } from './screens/AlertDoneScreen'
import { AlertSetupScreen } from './screens/AlertSetupScreen'
import { CardPaymentsScreen } from './screens/CardPaymentsScreen'

const phones = [
  { x: 16, screen: <AlertSetupScreen /> },
  { x: 436, screen: <AlertSetupScreen selected={1} /> },
  { x: 856, screen: <AlertDoneScreen /> },
  { x: 1276, screen: <CardPaymentsScreen /> },
]

function Showcase21() {
  return (
    <Stage width={1680} height={851} background={naver.stageBg}>
      {/* Edge of a cropped UI element peeking in at the top of the capture. */}
      <Placed x={1443} y={-10} width={135} height={14} className="rounded-[2px] border border-[#dde2ea]" />
      {phones.map(({ x, screen }) => (
        <Placed key={x} x={x} y={25}>
          <NaverPhone>{screen}</NaverPhone>
        </Placed>
      ))}
    </Stage>
  )
}

const showcase: ShowcaseDefinition = {
  id: '21',
  title: 'Naver Pay — 카드 실적 알림',
  width: 1680,
  height: 851,
  Component: Showcase21,
}
export default showcase
