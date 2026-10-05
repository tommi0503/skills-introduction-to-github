import { Leaflet, type LeafletDefinition } from '../../ui'
import { ArtworkLayer } from '../shared-2829/components/ArtworkLayer'
import { autumn } from '../shared-2829/theme'
import { artwork } from './data'
import { CoverPanel } from './panels/CoverPanel'
import { DirectionsPanel } from './panels/DirectionsPanel'
import { OverviewPanel } from './panels/OverviewPanel'

function Leaflet28() {
  return (
    <Leaflet panels={3} background={autumn.paper} underlay={<ArtworkLayer items={artwork} />}>
      <OverviewPanel />
      <DirectionsPanel />
      <CoverPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = { id: '28', title: '가을 꽃 축제 (외면)', panels: 3, Component: Leaflet28 }
export default definition
