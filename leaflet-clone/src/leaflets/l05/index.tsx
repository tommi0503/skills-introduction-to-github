import { ImagePlaceholder, Leaflet, type LeafletDefinition } from '../../ui'
import { CoverPanel } from './panels/CoverPanel'
import { DirectionsPanel } from './panels/DirectionsPanel'
import { InfoPanel } from './panels/InfoPanel'
import { photo, theme } from './theme'

/** Ship photo spanning the top of the two right panels with a slanted lower edge. */
function SpanningPhoto() {
  return (
    <ImagePlaceholder
      label="cruise ship photo"
      tone={theme.photoTone}
      className="absolute top-0"
      style={{
        left: photo.x,
        width: photo.width,
        height: photo.rightBottom,
        clipPath: `polygon(0 0, 100% 0, 100% 100%, 0 ${photo.leftBottom}px)`,
      }}
    />
  )
}

function Leaflet05() {
  return (
    <Leaflet panels={3} background={theme.paper}>
      <InfoPanel />
      <DirectionsPanel />
      <CoverPanel />
    </Leaflet>
  )
}

export { SpanningPhoto }
const definition: LeafletDefinition = { id: '05', title: '강풍호 크루즈 시티투어 (B)', panels: 3, Component: Leaflet05 }
export default definition
