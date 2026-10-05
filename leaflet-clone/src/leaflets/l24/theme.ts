import type { ArtShape } from '../shared-2425/components/GroundBand'
import type { TabGeometry } from './components/SectionTab'
import type { TableGeometry } from './components/NavyTable'

/** Panel-local layout of leaflet 24, measured on public/flat/24.png. */
export const layout = {
  p1: {
    tab: { x: 42, y: 55, width: 206, height: 45, lineEnd: 435 } satisfies TabGeometry,
    table: { x: 42, y: 123, width: 400, headerHeight: 44, rowHeight: 86 } satisfies TableGeometry,
    titleY: 469,
    introY: 528,
    factsY: 592,
    box: { x: 40, y: 762, width: 400, height: 123 },
    footerY: 978,
  },
  p2: {
    tab: { x: 32, y: 55, width: 207, height: 45, lineEnd: 432 } satisfies TabGeometry,
    table: { x: 32, y: 123, width: 405, headerHeight: 44, rowHeight: 129 } satisfies TableGeometry,
    opsY: 487,
    opsPitch: 98.7,
  },
  p3: {
    tab: { x: 30, y: 55, width: 210, height: 45, lineEnd: 433 } satisfies TabGeometry,
    table: { x: 28, y: 123, width: 414, headerHeight: 44, rowHeight: 51.4 } satisfies TableGeometry,
    tab2: { x: 30, y: 470, width: 210, height: 45, lineEnd: 433 } satisfies TabGeometry,
    commonY: 538,
  },
} as const

/** Ground artwork in sheet px: hills, bushes, buildings and the two characters. */
export const art: ArtShape[] = [
  { key: 'hill-left', x: 0, y: 885, w: 66, h: 60, radius: '0 40px 0 0' },
  { key: 'bush', x: 775, y: 893, w: 150, h: 52, radius: '60px 60px 0 0' },
  { key: 'buildings', x: 915, y: 843, w: 86, h: 100 },
  { key: 'girl-head', x: 297, y: 577, w: 96, h: 113, radius: '48px 48px 44px 44px', front: true },
  { key: 'girl-body', x: 245, y: 683, w: 196, h: 90, radius: '50px 50px 10px 10px', front: true },
  { key: 'megaphone', x: 1235, y: 785, w: 108, h: 120, radius: '30px 50px 20px 30px', front: true },
  { key: 'boy-head', x: 1350, y: 785, w: 90, h: 125, radius: '45px 0 0 45px', front: true },
  { key: 'boy-body', x: 1268, y: 890, w: 172, h: 128, radius: '30px 30px 0 0', front: true },
]
