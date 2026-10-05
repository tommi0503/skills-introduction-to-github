import { ScreenBoard, type AppDefinition } from '../../ui'
import { NationalIdScreen } from './screens/NationalIdScreen'
import { SelfieScreen } from './screens/SelfieScreen'

function App10() {
  return (
    <ScreenBoard>
      <SelfieScreen />
      <NationalIdScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '10', title: 'ID document upload', screens: 2, Component: App10 }
export default app
