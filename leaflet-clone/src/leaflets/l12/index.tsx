import { Leaflet, type LeafletDefinition } from '../../ui'
import { ContactPanel } from './panels/ContactPanel'
import { CoverPanel } from './panels/CoverPanel'
import { CulturePanel } from './panels/CulturePanel'
import { theme } from './theme'

function L12() {
  return (
    <Leaflet panels={3} background={theme.paper} className="font-noto-sans">
      <CulturePanel />
      <ContactPanel />
      <CoverPanel />
    </Leaflet>
  )
}

const def: LeafletDefinition = { id: '12', title: 'JEJU TRAVEL', panels: 3, Component: L12 }
export default def
