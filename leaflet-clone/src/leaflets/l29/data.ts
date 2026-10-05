import { polygonArtwork, type Artwork } from '../shared-2829/components/ArtworkLayer'
import { autumn } from '../shared-2829/theme'

export interface ProgramRow {
  time: string
  program: string
  place: string
}

/** Panel 1 — performance schedule. */
export const schedule = {
  title: '공연 프로그램 안내',
  headers: { time: '시간', program: '프로그램명', place: '장소' },
  rows: Array.from({ length: 11 }, (): ProgramRow => ({ time: '10:00', program: '프로그램', place: '메인존' })),
  footer: ['상세 문의  |   축제 운영 사무국', '02-1234-5678  /  dream@canvakorea.co.kr'],
}

export type PinColor = keyof typeof autumn.pin

export interface PinSpot {
  color: PinColor
  /** Centre of the pin head, sheet coordinates. */
  cx: number
  cy: number
}

export interface LegendEntry {
  number: string
  label: string
  /** Sheet coordinates of the bullet centre. */
  x: number
  y: number
  primary?: boolean
}

const otherColumns = [687, 823, 1028, 1155]
const otherRows = [840, 866, 893, 919]

/** Panels 2–3 — festival area map spanning the fold. */
export const areaMap = {
  title: '축제장 안내도',
  card: { x: 576, y: 137, w: 771, h: 628 },
  legendCard: { x: 576, y: 786, w: 771, h: 167 },
  zones: [
    polygonArtwork('zone A', [[657, 330], [672, 250], [705, 205], [760, 182], [830, 178], [890, 188], [935, 218], [958, 270], [955, 320], [925, 360], [860, 400], [790, 440], [735, 455], [685, 440], [660, 400]]),
    polygonArtwork('zone B', [[976, 205], [995, 190], [1100, 186], [1190, 195], [1255, 228], [1295, 280], [1302, 345], [1285, 400], [1245, 430], [1180, 432], [1120, 400], [1050, 325], [988, 245]]),
    polygonArtwork('zone C', [[892, 420], [930, 378], [962, 366], [988, 375], [1000, 410], [998, 495], [985, 523], [965, 518], [925, 470], [893, 432]]),
    polygonArtwork('zone D', [[1018, 335], [1035, 322], [1052, 330], [1122, 418], [1120, 435], [1080, 462], [1035, 480], [1015, 465], [1013, 400]]),
    polygonArtwork('zone E', [[803, 505], [820, 470], [858, 453], [903, 462], [938, 500], [955, 560], [953, 620], [935, 642], [895, 645], [850, 618], [810, 568]]),
    polygonArtwork('zone F', [[648, 575], [660, 540], [690, 527], [735, 530], [790, 570], [860, 640], [905, 688], [902, 715], [880, 723], [690, 723], [655, 705], [648, 680]]),
    polygonArtwork('zone G', [[1012, 595], [1025, 530], [1065, 485], [1125, 462], [1268, 460], [1282, 472], [1282, 712], [1270, 725], [1025, 725], [1012, 712]]),
  ],
  pins: [
    { color: 'blue', cx: 837, cy: 198 },
    { color: 'green', cx: 719, cy: 258 },
    { color: 'green', cx: 1051, cy: 211 },
    { color: 'red', cx: 1177, cy: 316 },
    { color: 'green', cx: 952, cy: 396 },
    { color: 'blue', cx: 1089, cy: 394 },
    { color: 'red', cx: 873, cy: 504 },
    { color: 'green', cx: 684, cy: 549 },
    { color: 'red', cx: 826, cy: 619 },
    { color: 'blue', cx: 732, cy: 682 },
    { color: 'green', cx: 1090, cy: 556 },
    { color: 'blue', cx: 1225, cy: 523 },
    { color: 'red', cx: 1128, cy: 654 },
    { color: 'green', cx: 1226, cy: 631 },
  ] satisfies PinSpot[],
  legend: <LegendEntry[]>[
    { number: '1', label: '종합안내소', x: 687, y: 813, primary: true },
    ...otherColumns.flatMap((x) => otherRows.map((y) => ({ number: '2', label: '그 외 장소', x, y }))),
  ],
}

/** Artwork in sheet coordinates (hills, leaves, acorns) → placeholders. */
export const artwork: Artwork[] = [
  {
    label: 'autumn hills',
    x: 0,
    y: 690,
    w: 1440,
    h: 328,
    clipPath: 'polygon(0 4px, 45px 4px, 440px 33px, 480px 41px, 600px 76px, 700px 80px, 1340px 148px, 1440px 142px, 1440px 328px, 0 328px)',
  },
  { label: 'acorns', x: 345, y: 0, w: 125, h: 110, radius: '0 40% 45% 45%' },
  { label: 'leaves top right', x: 1318, y: 62, w: 122, h: 258, radius: '45% 0 0 50%' },
  { label: 'yellow leaf', x: 405, y: 838, w: 115, h: 180, radius: '50% 50% 10% 10%' },
  { label: 'green leaf', x: 505, y: 918, w: 130, h: 100, radius: '50% 50% 0 0' },
]
