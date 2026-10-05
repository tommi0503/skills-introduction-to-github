import { Leaflet, type LeafletDefinition } from '../../ui'
import { AboutPanel } from './panels/AboutPanel'
import { ContactPanel } from './panels/ContactPanel'
import { CoverPanel } from './panels/CoverPanel'

function L32() {
  return (
    <Leaflet panels={3}>
      <CoverPanel />
      <ContactPanel />
      <AboutPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = { id: '32', title: '휴텍 미디어 — 외지', panels: 3, Component: L32 }
export default definition
