import type { AppDefinition } from '../../ui'
import { ScreenBoard } from '../../ui'
import { TideList } from './screens/TideList'

function TideGuide() {
  return (
    <ScreenBoard>
      <TideList />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '11', title: 'Tide Guide', screens: 5, Component: TideGuide }
export default app
