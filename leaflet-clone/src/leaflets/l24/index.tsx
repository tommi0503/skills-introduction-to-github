import { Leaflet, PANEL, sheetWidth, type LeafletDefinition } from '../../ui'
import { library } from '../shared-2425/theme'
import { ArtPlaceholder, GroundBand } from '../shared-2425/components/GroundBand'
import { ProgramPanel } from './panels/ProgramPanel'
import { OperationPanel } from './panels/OperationPanel'
import { ProjectPanel } from './panels/ProjectPanel'
import { art } from './theme'

function Leaflet24() {
  return (
    <Leaflet
      panels={3}
      background={library.paper}
      underlay={<GroundBand sheetWidth={sheetWidth(3)} sheetHeight={PANEL.height} shapes={art} />}
      overlay={art.filter((a) => a.front).map((a) => <ArtPlaceholder key={a.key} shape={a} />)}
    >
      <ProgramPanel />
      <OperationPanel />
      <ProjectPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = { id: '24', title: '그림책 마음 여행 아카데미', panels: 3, Component: Leaflet24 }
export default definition
