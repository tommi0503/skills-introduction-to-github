import { Leaflet, PANEL, Placed, type LeafletDefinition } from '../../ui'
import { regions, theme } from './theme'
import { ProgramPanel } from './panels/ProgramPanel'
import { MessagePanel } from './panels/MessagePanel'
import { CoverPanel } from './panels/CoverPanel'

/** Colour regions that do not follow the folds exactly. */
function Backdrop() {
  return (
    <>
      <Placed x={regions.greenFromX} y={0} width={PANEL.width * 3 - regions.greenFromX} height={PANEL.height} style={{ background: theme.green }} />
      <Placed
        x={regions.yellowBandX}
        y={regions.yellowBandY}
        width={PANEL.width * 3 - regions.yellowBandX}
        height={PANEL.height - regions.yellowBandY}
        style={{ background: theme.yellow }}
      />
    </>
  )
}

function Leaflet01() {
  return (
    <Leaflet panels={3} background={theme.yellow} underlay={<Backdrop />}>
      <ProgramPanel />
      <MessagePanel />
      <CoverPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = { id: '01', title: '미래를 키우는 특별한 나눔', panels: 3, Component: Leaflet01 }
export default definition
