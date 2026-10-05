import { Leaflet, PANEL, sheetWidth, type LeafletDefinition } from '../../ui'
import { CoverPanel } from './panels/CoverPanel'
import { JoinPanel } from './panels/JoinPanel'
import { ThanksPanel } from './panels/ThanksPanel'
import { theme } from './theme'

function Band() {
  return (
    <div
      className="absolute left-0"
      style={{ top: theme.bandTop, width: sheetWidth(3), height: PANEL.height - theme.bandTop, background: theme.band }}
    />
  )
}

function L08() {
  return (
    <Leaflet panels={3} background={theme.paper} underlay={<Band />} className="font-gothic-a1">
      <JoinPanel />
      <ThanksPanel />
      <CoverPanel />
    </Leaflet>
  )
}

const def: LeafletDefinition = { id: '08', title: '우리동네 함께재단', panels: 3, Component: L08 }
export default def
