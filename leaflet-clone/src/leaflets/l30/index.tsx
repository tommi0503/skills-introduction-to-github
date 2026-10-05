import { Leaflet, type LeafletDefinition } from '../../ui'
import { growth } from '../shared-3031/theme'
import { AudiencePanel } from './panels/AudiencePanel'
import { ContactPanel } from './panels/ContactPanel'
import { CoverPanel } from './panels/CoverPanel'

function Leaflet30() {
  return (
    <Leaflet panels={3} background={growth.navy}>
      <AudiencePanel />
      <ContactPanel />
      <CoverPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = { id: '30', title: '지역 성장 지원사업 (외면)', panels: 3, Component: Leaflet30 }
export default definition
