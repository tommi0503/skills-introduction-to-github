import { Leaflet, type LeafletDefinition } from '../../ui'
import { ArtistsPanel } from './panels/ArtistsPanel'
import { CoverPanel } from './panels/CoverPanel'
import { TicketPanel } from './panels/TicketPanel'

function Leaflet15() {
  return (
    <Leaflet panels={3}>
      <ArtistsPanel />
      <TicketPanel />
      <CoverPanel />
    </Leaflet>
  )
}

const leaflet15: LeafletDefinition = { id: '15', title: '특별한 음악회 (outside)', panels: 3, Component: Leaflet15 }
export default leaflet15
