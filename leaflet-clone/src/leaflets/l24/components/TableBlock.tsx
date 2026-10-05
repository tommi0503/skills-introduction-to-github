import { Placed } from '../../../ui'
import type { TableSection } from '../data'
import { NavyTable, type TableGeometry } from './NavyTable'
import { SectionTab, type TabGeometry } from './SectionTab'

interface TableBlockProps {
  section: TableSection
  tab: TabGeometry
  table: TableGeometry
}

/** Section tab + its navy table. */
export function TableBlock({ section, tab, table }: TableBlockProps) {
  return (
    <>
      <SectionTab title={section.title} geo={tab} />
      <Placed x={table.x} y={table.y}>
        <NavyTable columns={section.columns} rows={section.rows} geo={table} />
      </Placed>
    </>
  )
}
