import { Leaflet, type LeafletDefinition } from '../../ui'
import { SpanningPhoto } from './components'
import { CoverPanel } from './panels/CoverPanel'
import { DirectionsPanel } from './panels/DirectionsPanel'
import { InfoPanel } from './panels/InfoPanel'
import { theme } from './theme'

function Leaflet05() {
  return (
    <Leaflet panels={3} background={theme.paper} underlay={<SpanningPhoto />}>
      <InfoPanel />
      <DirectionsPanel />
      <CoverPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = { id: '05', title: '강풍호 크루즈 시티투어 (B)', panels: 3, Component: Leaflet05 }
export default definition
