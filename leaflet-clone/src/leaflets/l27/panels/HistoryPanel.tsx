import { Panel, Placed } from '../../../ui'
import { seoul } from '../../shared-2627/theme'
import { Photo } from '../../shared-2627/components/Photo'
import { SectionNumber } from '../../shared-2627/components/SectionNumber'
import { Paragraphs } from '../components/Paragraphs'
import { history } from '../data'

/** Panel 1 — 01 과거와 미래가 공존하는 도시 (arch photo). */
export function HistoryPanel() {
  return (
    <Panel background={seoul.paper}>
      <Placed x={55} y={85}>
        <SectionNumber number={history.number} title={history.title} layout="stacked" />
      </Placed>
      <Photo box={history.photo} />
      <Paragraphs items={[history.text]} />
    </Panel>
  )
}
