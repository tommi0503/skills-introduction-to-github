import { Leaflet, type LeafletDefinition } from '../../ui'
import { AboutPanel } from './panels/AboutPanel'
import { CoverPanel } from './panels/CoverPanel'
import { QuoteContactPanel } from './panels/QuoteContactPanel'

function Leaflet19() {
  return (
    <Leaflet panels={3}>
      <AboutPanel />
      <QuoteContactPanel />
      <CoverPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = {
  id: '19',
  title: 'Creative Studio',
  panels: 3,
  Component: Leaflet19,
}

export default definition
