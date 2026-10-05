import { Leaflet, type LeafletDefinition } from '../../ui'
import { CoverPanel } from './panels/CoverPanel'
import { ProgramPanel } from './panels/ProgramPanel'
import { VisitPanel } from './panels/VisitPanel'
import { theme } from './theme'

function L09() {
  return (
    <Leaflet panels={3} background={theme.paper} className="font-myeongjo font-bold">
      <ProgramPanel />
      <VisitPanel />
      <CoverPanel />
    </Leaflet>
  )
}

const def: LeafletDefinition = { id: '09', title: '역사를 만나다', panels: 3, Component: L09 }
export default def
