import { Leaflet, type LeafletDefinition } from '../../ui'
import { seoul } from '../shared-2627/theme'
import { TipsPanel } from './panels/TipsPanel'
import { InfoPanel } from './panels/InfoPanel'
import { CoverPanel } from './panels/CoverPanel'

function Leaflet26() {
  return (
    <Leaflet panels={3} background={seoul.paper}>
      <TipsPanel />
      <InfoPanel />
      <CoverPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = { id: '26', title: 'SEOUL: TRAVEL GUIDE (outside)', panels: 3, Component: Leaflet26 }
export default definition
