import { Leaflet, type LeafletDefinition } from '../../ui'
import { seoul } from '../shared-2627/theme'
import { HistoryPanel } from './panels/HistoryPanel'
import { TraditionPanel } from './panels/TraditionPanel'
import { NightPanel } from './panels/NightPanel'

function Leaflet27() {
  return (
    <Leaflet panels={3} background={seoul.paper}>
      <HistoryPanel />
      <TraditionPanel />
      <NightPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = { id: '27', title: 'SEOUL: TRAVEL GUIDE (inside)', panels: 3, Component: Leaflet27 }
export default definition
