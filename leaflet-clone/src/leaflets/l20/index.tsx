import { Leaflet, type LeafletDefinition } from '../../ui'
import { theme2021 } from '../shared-2021/theme'
import { ApplyPanel } from './panels/ApplyPanel'
import { CoverPanel } from './panels/CoverPanel'
import { DirectionsPanel } from './panels/DirectionsPanel'

function Leaflet20() {
  return (
    <Leaflet panels={3} background={theme2021.sheet}>
      <ApplyPanel />
      <DirectionsPanel />
      <CoverPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = {
  id: '20',
  title: '시니어 디지털&AI 첫걸음교실 (바깥면)',
  panels: 3,
  Component: Leaflet20,
}

export default definition
