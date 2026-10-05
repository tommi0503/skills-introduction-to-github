import { Leaflet, type LeafletDefinition } from '../../ui'
import { services } from './data'
import { PartnersPanel } from './panels/PartnersPanel'
import { ServicePanel } from './panels/ServicePanel'

function L33() {
  return (
    <Leaflet panels={3}>
      {services.map((s) => (
        <ServicePanel key={s.label} service={s} />
      ))}
      <PartnersPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = { id: '33', title: '휴텍 미디어 — 내지', panels: 3, Component: L33 }
export default definition
