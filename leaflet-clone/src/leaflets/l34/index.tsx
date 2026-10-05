import { Leaflet, type LeafletDefinition } from '../../ui'
import { CoverPanel } from './panels/CoverPanel'
import { DirectionsPanel } from './panels/DirectionsPanel'
import { GreetingPanel } from './panels/GreetingPanel'

function L34() {
  return (
    <Leaflet panels={3}>
      <GreetingPanel />
      <DirectionsPanel />
      <CoverPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = { id: '34', title: '라라나의원 — 외지', panels: 3, Component: L34 }
export default definition
