import { Leaflet, type LeafletDefinition } from '../../ui'
import { AboutPanel } from './panels/AboutPanel'
import { GuidePanel } from './panels/GuidePanel'
import { ProgramPanel } from './panels/ProgramPanel'

function Leaflet16() {
  return (
    <Leaflet panels={3}>
      <AboutPanel />
      <ProgramPanel />
      <GuidePanel />
    </Leaflet>
  )
}

const leaflet16: LeafletDefinition = { id: '16', title: '특별한 음악회 (inside)', panels: 3, Component: Leaflet16 }
export default leaflet16
