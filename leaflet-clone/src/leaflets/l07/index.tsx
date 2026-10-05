import { Leaflet, type LeafletDefinition } from '../../ui'
import { CoverPanel } from './panels/CoverPanel'
import { DirectionsPanel } from './panels/DirectionsPanel'
import { InfoPanel } from './panels/InfoPanel'
import { field, theme } from './theme'

/** Sky background with the green field sweeping across the two right panels. */
function FieldUnderlay() {
  return (
    <svg className="absolute inset-0" width="100%" height="100%">
      <path d={field.path} fill={theme.field} />
    </svg>
  )
}

function Leaflet07() {
  return (
    <Leaflet panels={3} background={theme.sky} underlay={<FieldUnderlay />}>
      <InfoPanel />
      <DirectionsPanel />
      <CoverPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = { id: '07', title: '나무섬 전망대', panels: 3, Component: Leaflet07 }
export default definition
