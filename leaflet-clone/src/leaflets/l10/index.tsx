import { Leaflet, type LeafletDefinition } from '../../ui'
import { Shapes } from '../shared-0812'
import { WaveBand } from './components/WaveBand'
import { sheetArt, waves } from './data'
import { CoverPanel } from './panels/CoverPanel'
import { GreetingPanel } from './panels/GreetingPanel'
import { GuidePanel } from './panels/GuidePanel'
import { theme } from './theme'

function Artwork() {
  return (
    <>
      <Shapes items={sheetArt} />
      <WaveBand {...waves} />
    </>
  )
}

function L10() {
  return (
    <Leaflet panels={3} background={theme.paper} underlay={<Artwork />} className="font-noto-sans">
      <GreetingPanel />
      <GuidePanel />
      <CoverPanel />
    </Leaflet>
  )
}

const def: LeafletDefinition = { id: '10', title: '나무섬 전망대', panels: 3, Component: L10 }
export default def
