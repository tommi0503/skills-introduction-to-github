import { Leaflet, type LeafletDefinition } from '../../ui'
import { theme2223 } from '../shared-2223/theme'
import { FaqPanel } from './panels/FaqPanel'
import { ProgramPanel } from './panels/ProgramPanel'
import { SchedulePanel } from './panels/SchedulePanel'

function Leaflet23() {
  return (
    <Leaflet panels={3} background={theme2223.sheet}>
      <ProgramPanel />
      <SchedulePanel />
      <FaqPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = {
  id: '23',
  title: '농촌체험 프로그램 (안쪽면)',
  panels: 3,
  Component: Leaflet23,
}

export default definition
