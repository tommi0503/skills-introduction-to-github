import { Leaflet, Panel, type LeafletDefinition } from '../../ui'
import { ArtworkLayer } from '../shared-2829/components/ArtworkLayer'
import { autumn } from '../shared-2829/theme'
import { AreaMap } from './components/AreaMap'
import { artwork } from './data'
import { MapTitlePanel } from './panels/MapTitlePanel'
import { SchedulePanel } from './panels/SchedulePanel'

function Leaflet29() {
  return (
    <Leaflet panels={3} background={autumn.paper} underlay={<ArtworkLayer items={artwork} />} overlay={<AreaMap />}>
      <SchedulePanel />
      <MapTitlePanel />
      {/* Panel 3 holds only the right half of the cross-fold map (overlay). */}
      <Panel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = { id: '29', title: '가을 꽃 축제 (내면)', panels: 3, Component: Leaflet29 }
export default definition
