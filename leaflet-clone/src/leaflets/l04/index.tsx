import { Leaflet, type LeafletDefinition } from '../../ui'
import { CoverPanel } from './panels/CoverPanel'
import { DirectionsPanel } from './panels/DirectionsPanel'
import { GuidePanel } from './panels/GuidePanel'

function Leaflet04() {
  return (
    <Leaflet panels={3}>
      <GuidePanel />
      <DirectionsPanel />
      <CoverPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = { id: '04', title: '강풍호 크루즈 시티투어', panels: 3, Component: Leaflet04 }
export default definition
