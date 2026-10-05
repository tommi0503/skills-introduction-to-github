import { Leaflet, type LeafletDefinition } from '../../ui'
import { CoverPanel } from './panels/CoverPanel'
import { ReviewsPanel } from './panels/ReviewsPanel'
import { TransitPanel } from './panels/TransitPanel'

function Leaflet06() {
  return (
    <Leaflet panels={3}>
      <ReviewsPanel />
      <TransitPanel />
      <CoverPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = { id: '06', title: '행궁동 동네한바퀴', panels: 3, Component: Leaflet06 }
export default definition
