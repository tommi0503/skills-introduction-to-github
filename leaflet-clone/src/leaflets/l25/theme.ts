import type { ArtShape } from '../shared-2425/components/GroundBand'

/** Panel backgrounds (the sheet changes tone per fold). */
export const panelBg = {
  programs: '#f5f5ef',
  apply: '#f5f0e1',
  cover: 'linear-gradient(180deg,#dde2ef 0%,#e2e6f1 100%)',
} as const

/** Panel-local layout of leaflet 25, measured on public/flat/25.png. */
export const layout = {
  programs: { x: 45, width: 402, headingYs: [72, 308, 553], headingH: 55, firstItemGap: 20, itemPitch: 75, pillW: 115, pillH: 53, descX: 193 },
  apply: { titleY: 86, ruleY: 139, stepYs: [182, 304, 423, 559], stepPitch: 0, circle: 62, ruleYs: [268, 395, 527], notice: { x: 48, y: 700, w: 395, h: 165 } },
  cover: { arcY: 118, titleY: 214, sloganY: 381, centerY: 516, urlY: 977 },
  footerY: 978,
} as const

/** Illustrations standing on / near the ground band, sheet px. */
export const art: ArtShape[] = [
  { key: 'building-1', x: 42, y: 838, w: 63, h: 106 },
  { key: 'building-2', x: 105, y: 876, w: 27, h: 68 },
  { key: 'building-3', x: 132, y: 868, w: 75, h: 76 },
  { key: 'building-3-roof', x: 140, y: 853, w: 45, h: 15 },
  { key: 'building-4', x: 213, y: 912, w: 42, h: 32 },
  { key: 'building-5', x: 255, y: 845, w: 76, h: 99, radius: '0 60px 0 0' },
  { key: 'building-6', x: 336, y: 873, w: 80, h: 71 },
  { key: 'hill-1', x: 0, y: 882, w: 62, h: 62, radius: '0 34px 0 0' },
  { key: 'hill-2', x: 430, y: 893, w: 140, h: 51, radius: '40px 46px 0 0' },
  { key: 'building-mid', x: 902, y: 846, w: 90, h: 98 },
  { key: 'cloud-left', x: 960, y: 600, w: 55, h: 95, radius: '0 40px 40px 0' },
  { key: 'cloud-right', x: 1388, y: 490, w: 52, h: 80, radius: '40px 0 0 40px' },
  { key: 'open-book', x: 1058, y: 548, w: 284, h: 252, radius: '6px' },
  { key: 'monitor', x: 1015, y: 598, w: 370, h: 264, radius: '16px' },
  { key: 'monitor-stand', x: 1135, y: 862, w: 145, h: 82 },
  { key: 'buildings-left-3', x: 960, y: 845, w: 85, h: 99 },
  { key: 'bush-left-3', x: 1018, y: 866, w: 125, h: 78, radius: '50px 50px 0 0' },
  { key: 'bush-right-3', x: 1262, y: 884, w: 125, h: 60, radius: '50px 50px 0 0' },
  { key: 'buildings-right-3', x: 1355, y: 808, w: 85, h: 136 },
]
