import { Leaflet, type LeafletDefinition } from '../../ui'
import { CoverPanel } from './panels/CoverPanel'
import { DirectionsPanel } from './panels/DirectionsPanel'
import { ParticipationPanel } from './panels/ParticipationPanel'

function Leaflet13() {
  return (
    <Leaflet panels={3}>
      <ParticipationPanel />
      <DirectionsPanel />
      <CoverPanel />
    </Leaflet>
  )
}

const leaflet13: LeafletDefinition = { id: '13', title: '2030 유아용품 박람회 (outside)', panels: 3, Component: Leaflet13 }
export default leaflet13
