import { Leaflet, PANEL, sheetWidth, type LeafletDefinition } from '../../ui'
import { GroundBand } from '../shared-2425/components/GroundBand'
import { ContactFooter } from '../shared-2425/components/ContactFooter'
import { cover, footer } from './data'
import { ProgramsPanel } from './panels/ProgramsPanel'
import { ApplyPanel } from './panels/ApplyPanel'
import { CoverPanel } from './panels/CoverPanel'
import { art, layout } from './theme'

function Leaflet25() {
  return (
    <Leaflet panels={3} overlay={
        <>
          {/* panels are opaque, so the ground and its footer text paint above them */}
          <GroundBand sheetWidth={sheetWidth(3)} sheetHeight={PANEL.height} shapes={art} />
          <ContactFooter
            items={[...footer, { text: cover.url, x: PANEL.width * 2 + 168 }]}
            y={layout.footerY}
            className="text-[13px] font-semibold text-[#4b5070]"
          />
        </>
      }>
      <ProgramsPanel />
      <ApplyPanel />
      <CoverPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = { id: '25', title: '평생 학습 프로그램 안내', panels: 3, Component: Leaflet25 }
export default definition
