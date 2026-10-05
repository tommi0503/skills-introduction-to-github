import { Leaflet, type LeafletDefinition } from '../../ui'
import { fonts } from '../shared-1718/theme'
import { CoverPanel } from './panels/CoverPanel'
import { InvitationPanel } from './panels/InvitationPanel'
import { TimetablePanel } from './panels/TimetablePanel'

function Leaflet17() {
  return (
    <Leaflet panels={3} className={fonts.body}>
      <InvitationPanel />
      <TimetablePanel />
      <CoverPanel />
    </Leaflet>
  )
}

const definition: LeafletDefinition = {
  id: '17',
  title: '2056 도서관 책축제 (외면)',
  panels: 3,
  Component: Leaflet17,
}

export default definition
