import { Panel, Placed } from '../../../ui'
import { library } from '../../shared-2425/theme'
import { InfoPillList } from '../components/InfoPillList'
import { SectionTab } from '../components/SectionTab'
import { TableBlock } from '../components/TableBlock'
import { common, readingProject } from '../data'
import { layout } from '../theme'

const L = layout.p3

/** Panel 3 — 방학 독서 프로젝트 table + 공통 안내 list. */
export function ProjectPanel() {
  return (
    <Panel>
      <TableBlock section={readingProject} tab={L.tab} table={L.table} />
      <SectionTab title={common.title} geo={L.tab2} />
      <Placed x={32} y={L.commonY}>
        <InfoPillList
          items={common.items}
          fill={library.pale}
          pillWidth={85}
          pillHeight={30}
          pitch={45.7}
          gap={18}
          labelClassName="font-dohyeon text-[13px] text-[#3e4166]"
          valueClassName="text-[15px] font-semibold tracking-[0.01em] text-[#4b4f72]"
        />
      </Placed>
    </Panel>
  )
}
