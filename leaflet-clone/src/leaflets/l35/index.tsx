import { Leaflet, type LeafletDefinition } from '../../ui'
import { CarePanel } from './panels/CarePanel'
import { CheckupPanel } from './panels/CheckupPanel'
import { GuidePanel } from './panels/GuidePanel'

function L35() {
  return (
    <Leaflet panels={3}>
      <CarePanel />
      <CheckupPanel />
      <GuidePanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = { id: '35', title: '라라나의원 — 내지', panels: 3, Component: L35 }
export default definition
