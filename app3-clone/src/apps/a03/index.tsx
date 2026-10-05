import { ScreenBoard, type AppDefinition } from '../../ui'
import { NotesScreen } from './screens/NotesScreen'
import { TasksScreen } from './screens/TasksScreen'

function App03() {
  return (
    <ScreenBoard>
      <NotesScreen />
      <TasksScreen />
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '03', title: 'Notes & Tasks', screens: 2, Component: App03 }
export default app
