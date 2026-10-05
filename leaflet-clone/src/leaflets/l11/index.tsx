import { Leaflet, type LeafletDefinition } from '../../ui'
import { footer, spots } from './data'
import { SpotPanel } from './panels/SpotPanel'
import { theme } from './theme'

function L11() {
  return (
    <Leaflet panels={3} background={theme.olive} className="font-noto-sans">
      {spots.map((spot, i) => (
        <SpotPanel key={spot.number} spot={spot} footer={i === footer.panel ? footer.text : undefined} />
      ))}
    </Leaflet>
  )
}

const def: LeafletDefinition = { id: '11', title: '1·2·3 추천 명소', panels: 3, Component: L11 }
export default def
