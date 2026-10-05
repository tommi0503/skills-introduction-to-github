import { Leaflet, type LeafletDefinition } from '../../ui'
import { CoverPanel } from './panels/CoverPanel'
import { InterviewPanel } from './panels/InterviewPanel'
import { TestimonialsPanel } from './panels/TestimonialsPanel'
import { ProgramPanel } from './panels/ProgramPanel'

function Leaflet02() {
  return (
    <Leaflet panels={4}>
      <CoverPanel />
      <InterviewPanel />
      <TestimonialsPanel />
      <ProgramPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = { id: '02', title: 'Joyful Market', panels: 4, Component: Leaflet02 }
export default definition
