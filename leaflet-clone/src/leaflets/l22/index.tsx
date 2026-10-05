import { Leaflet, type LeafletDefinition } from '../../ui'
import { theme2223 } from '../shared-2223/theme'
import { ApplyPanel } from './panels/ApplyPanel'
import { CoverPanel } from './panels/CoverPanel'
import { IntroPanel } from './panels/IntroPanel'

function Leaflet22() {
  return (
    <Leaflet panels={3} background={theme2223.sheet}>
      <IntroPanel />
      <ApplyPanel />
      <CoverPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = {
  id: '22',
  title: '농촌체험 프로그램 (바깥면)',
  panels: 3,
  Component: Leaflet22,
}

export default definition
