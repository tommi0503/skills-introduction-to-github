import { Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { NaverPhone, naver } from '../shared-naver'
import { CompanySearchScreen } from './screens/CompanySearchScreen'
import { ExtraInfoScreen } from './screens/ExtraInfoScreen'
import { IncomeScreen } from './screens/IncomeScreen'
import { JoinDateSheetScreen } from './screens/JoinDateSheetScreen'

const phones = [
  { x: 21, Screen: CompanySearchScreen },
  { x: 441, Screen: JoinDateSheetScreen },
  { x: 861, Screen: IncomeScreen },
  { x: 1281, Screen: ExtraInfoScreen },
]

function Showcase22() {
  return (
    <Stage width={1671} height={870} background={naver.stageBg}>
      {phones.map(({ x, Screen }) => (
        <Placed key={x} x={x} y={35}>
          <NaverPhone>
            <Screen />
          </NaverPhone>
        </Placed>
      ))}
    </Stage>
  )
}

const showcase: ShowcaseDefinition = {
  id: '22',
  title: 'Naver Pay — 직장/소득 정보 입력',
  width: 1671,
  height: 870,
  Component: Showcase22,
}
export default showcase
