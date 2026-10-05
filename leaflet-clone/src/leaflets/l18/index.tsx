import { ImagePlaceholder, Leaflet, PANEL, type LeafletDefinition } from '../../ui'
import { fonts, insidePalette as c } from '../shared-1718/theme'
import { ParticipationBox } from './components/ParticipationBox'
import { ProgramsFrame } from './components/ProgramsFrame'
import { participation, programs } from './data'
import { GreetingPanel } from './panels/GreetingPanel'
import { ProgramColumnPanel } from './panels/ProgramColumnPanel'

const SPAN = { x: PANEL.width + 25, width: PANEL.width * 2 - 25 - 27 }
const PROGRAM_TOPS = [131, 310, 505]

function Leaflet18() {
  return (
    <Leaflet
      panels={3}
      background={c.cream}
      className={fonts.body}
      underlay={
        <>
          <ProgramsFrame title={programs.title} palette={c} x={SPAN.x} y={25} width={SPAN.width} height={697} />
          <ParticipationBox
            content={participation}
            palette={c}
            x={SPAN.x}
            y={743}
            width={SPAN.width}
            height={245}
            qr={{ x: 763, y: 77, size: 107 }}
          />
        </>
      }
      overlay={
        <>
          <ImagePlaceholder label="ribbon badge" className="absolute" style={{ left: 735, top: 14, width: 52, height: 62 }} />
          <ImagePlaceholder label="sparkle" className="absolute" style={{ left: 790, top: 75, width: 34, height: 32 }} />
          <ImagePlaceholder label="friends on books illustration" className="absolute" style={{ left: 1225, top: 645, width: 190, height: 168 }} />
        </>
      }
    >
      <GreetingPanel />
      <ProgramColumnPanel programs={programs.columns[0]} palette={c} x={63} width={360} tops={PROGRAM_TOPS} />
      <ProgramColumnPanel programs={programs.columns[1]} palette={c} x={33} width={368} tops={PROGRAM_TOPS} />
    </Leaflet>
  )
}

const definition: LeafletDefinition = {
  id: '18',
  title: '2056 도서관 책축제 (내면)',
  panels: 3,
  Component: Leaflet18,
}

export default definition
