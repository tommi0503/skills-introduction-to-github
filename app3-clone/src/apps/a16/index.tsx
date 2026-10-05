import { ScreenBoard, type AppDefinition } from '../../ui'
import { exercises } from './data'
import { ExerciseScreen } from './screens/ExerciseScreen'

function A16() {
  return (
    <ScreenBoard>
      {exercises.map((e) => (
        <ExerciseScreen key={e.id} exercise={e} />
      ))}
    </ScreenBoard>
  )
}

const app: AppDefinition = { id: '16', title: 'Language lesson — translate', screens: exercises.length, Component: A16 }
export default app
