/** d21 — blue & sky-blue diagonal corporate report tokens. */
export const t = {
  blue: '#4870b0',
  ink: '#2b2b2b',
  grey: '#8c8c8c',
  pale: '#e6eaeb',
  panel: '#eef2f7',
  label: '#c1ccd4',
  line: '#c5cfdb',
  photo: '#c9c9c9',
  font: 'font-pretendard',
} as const

export type Pt = [number, number]
/** Shared diagonal geometry. */
export const geo = {
  stripe: [[3, 0], [35, 0], [104, 70], [72, 70]] as Pt[],
  stripeWide: [[3, 0], [47, 0], [140, 92], [96, 92]] as Pt[],
  cornerTri: [[1185, 0], [1278, 0], [1278, 96]] as Pt[],
  photoRightSlant: [[1177, 0], [1280, 0], [1280, 720], [934, 720]] as Pt[],
  photoRight: [[843, 0], [1280, 0], [1280, 720], [843, 720]] as Pt[],
  photoLeft: [[0, 0], [402, 0], [402, 720], [0, 720]] as Pt[],
  stripeMid: [[404, 0], [436, 0], [503, 68], [471, 68]] as Pt[],
  bottomRight: [[1280, 518], [1280, 720], [1102, 720]] as Pt[],
}
