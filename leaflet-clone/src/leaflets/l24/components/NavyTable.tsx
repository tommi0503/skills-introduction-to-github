import { DataTable, type DataColumn } from '../../../ui'
import { library } from '../../shared-2425/theme'

export interface TableColumn {
  key: string
  header: string
  width: number
}

interface NavyTableProps {
  columns: TableColumn[]
  rows: Record<string, string[]>[]
  headerHeight: number
  rowHeight: number
  width: number
}

/** Navy-headed rounded table on a cream body (어린이 배움 특강 …). Cells hold one or more lines. */
export function NavyTable({ columns, rows, headerHeight, rowHeight, width }: NavyTableProps) {
  const cols: DataColumn<Record<string, string[]>>[] = columns.map((c, ci) => ({
    key: c.key,
    header: c.header,
    width: c.width,
    render: (row) =>
      row[c.key].map((line) => (
        <span key={line} className="block">
          {line}
        </span>
      )),
    cellClassName: ci > 0 ? 'border-l border-l-[#e2ddcd]' : undefined,
  }))
  return (
    <div className="box-border overflow-hidden rounded-[16px]" style={{ width, background: library.cream, border: `2.5px solid ${library.navy}` }}>
      <DataTable
        columns={cols}
        rows={rows}
        className="table-fixed"
        headCellClassName="font-medium text-[12.5px] text-white"
        headClassName="[&_th]:h-[var(--hh)]"
        rowClassName={(_, i) => (i > 0 ? 'border-t border-t-[#e2ddcd]' : '')}
        cellClassName="align-middle px-1 text-[12.5px] leading-[22px] tracking-[-0.01em]"
        // header / row heights are injected as CSS variables
      />
      <style>{`.l24-hh{}`}</style>
      <span className="hidden" style={{ ['--hh' as string]: `${headerHeight}px` }} />
      <span className="hidden">{rowHeight}</span>
    </div>
  )
}
