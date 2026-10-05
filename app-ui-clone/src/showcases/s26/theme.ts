/** Design tokens for the CU convenience-store app (reference 26). */
export const cu = {
  stage: '#141414',
  green: '#62d049',
  check: '#5fd34b',
  ink: '#1a1a1a',
  text: '#333333',
  sub: '#888888',
  faint: '#b0b0b0',
  line: '#ececec',
  section: '#f5f5f5',
  tile: '#f7f7f9',
  pink: '#e0457b',
  link: '#6a5cf0',
  qr: 'linear-gradient(90deg, #5f79f8 0%, #8666eb 100%)',
  toggle: 'linear-gradient(90deg, #5878f3 0%, #7270fb 100%)',
  searchRing: 'linear-gradient(90deg, #8fb3f4 0%, #c69af0 100%)',
  headerWash: 'linear-gradient(180deg, #f6d4bb 0px, #f6d4bb 118px, #fae6da 165px, #ffffff 205px)',
  banner: 'linear-gradient(180deg, #98cb6a 0%, #78b052 100%)',
} as const

export const device = {
  height: 582,
  logicalWidth: 393,
  screenRadius: 34,
} as const
