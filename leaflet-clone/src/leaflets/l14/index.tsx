import { Leaflet, type LeafletDefinition } from '../../ui'
import { booths, programs } from './data'
import { IntroPanel } from './panels/IntroPanel'
import { ListPanel } from './panels/ListPanel'

function Leaflet14() {
  return (
    <Leaflet panels={3}>
      <IntroPanel />
      <ListPanel section={booths} ruleX={265} waveOffset={40} itemX={40} />
      <ListPanel section={programs} ruleX={273} waveOffset={40} itemX={46} />
    </Leaflet>
  )
}

const leaflet14: LeafletDefinition = { id: '14', title: '2030 유아용품 박람회 (inside)', panels: 3, Component: Leaflet14 }
export default leaflet14
