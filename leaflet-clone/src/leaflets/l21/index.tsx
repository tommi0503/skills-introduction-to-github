import { Leaflet, type LeafletDefinition } from '../../ui'
import { theme2021 } from '../shared-2021/theme'
import { AudiencePanel } from './panels/AudiencePanel'
import { CurriculumPanel } from './panels/CurriculumPanel'
import { DetailPanel } from './panels/DetailPanel'

function Leaflet21() {
  return (
    <Leaflet panels={3} background={theme2021.sheet}>
      <CurriculumPanel />
      <AudiencePanel />
      <DetailPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = {
  id: '21',
  title: '시니어 디지털&AI 첫걸음교실 (안쪽면)',
  panels: 3,
  Component: Leaflet21,
}

export default definition
