import { Leaflet, type LeafletDefinition } from '../../ui'
import { theme } from './theme'
import { ChecklistPanel } from './panels/ChecklistPanel'
import { DirectionsPanel } from './panels/DirectionsPanel'
import { CoverPanel } from './panels/CoverPanel'

function Leaflet03() {
  return (
    <Leaflet panels={3} background={theme.green} className="font-noto-sans">
      <ChecklistPanel />
      <DirectionsPanel />
      <CoverPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = { id: '03', title: '동그라미 플리마켓', panels: 3, Component: Leaflet03 }
export default definition
