import type { DeckDefinition } from '../../ui'
import { Contents, Cover, FourKeys, LongText, Process, Summary, Thanks, ThreeKeys, TwoImages, ch } from '../d11/slides'
import { longText } from './data'
import { Org, Timetable, Heatmap, LineCharts, Pies, Bars, Table, WorldMap, Cause, Company, Gallery, Growth, Mockup, Part, Pyramid, Venn, Qna, Stairs, SummaryBoard, Vertical, Zoom } from './slides'

const deck: DeckDefinition = {
  id: '15',
  title: '베이지 기본 보고서 설명서',
  slides: [
    () => <Cover v={{ ts: 129, dy: 4 }} />,
    () => <Contents v={{ dx: 10 }} />,
    () => <LongText data={longText} v={{ ts: 47, dy: -30, by: -32, ky: -12, dx: 510 }} />,
    Company,
    () => <TwoImages chapter={ch(3)} v={{ ts: 47 }} />,
    Vertical,
    () => <FourKeys chapter={ch(5)} v={{ ts: 47, center: true }} />,
    () => <ThreeKeys chapter={ch(6)} v={{ ts: 47, center: true }} />,
    Zoom, Qna, SummaryBoard,
    () => <Process chapter={ch(10)} v={{ ts: 47, bs: 16.5, by: 3 }} />,
    Stairs, Mockup, Gallery, Pyramid, Cause, Venn, Part, Growth, Table, WorldMap, Bars, Pies, LineCharts, Heatmap, Timetable, Org,
    () => <Summary chapter={ch(26)} v={{ ts: 47, dy: 21, bs: 16.2 }} />,
    () => <Thanks v={{ bs: 26.7, bs2: 19.6, ts: 125, dy: 4 }} />,
  ],
}
export default deck
