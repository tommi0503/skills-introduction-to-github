/** Design tokens shared by the outside (15) and inside (16) of the 특별한 음악회 concert brochure. */
export const concertTheme = {
  paper: '#f7f7f6',
  burgundy: '#572829',
  burgundyDeep: '#5a2427',
  mauve: '#673a4b',
  cream: '#ebe1c2',
  creamBox: '#e3dcc0',
  onDark: '#f0e6d6',
  onDarkMuted: '#d6c3b8',
  ink: '#3f3434',
  heading: '#4e2c2f',
  body: '#5d5555',
  rule: '#e6ddcc',
  mapBox: '#e2e2e2',
  mapLine: '#7a5052',
  /** Font utility classes for the brochure's typographic roles. */
  font: {
    latin: 'font-montserrat',
    display: 'font-dohyeon',
    title: 'font-noto-serif font-black',
    serif: 'font-noto-serif font-bold',
  },
} as const
