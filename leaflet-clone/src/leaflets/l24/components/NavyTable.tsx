import type { CSSProperties } from 'react'
import { DataTable, type DataColumn } from '../../../ui'
import { library } from '../../shared-2425/theme'

export interface TableColumn {
  key: string
  header: string
  width: number
}

/** A row maps column key -> printed lines of that cell. */
export type TableRow = Record<string, string[]>

export interface TableGeometry {
  x: number
  y: number
  width: number
  headerHeight: number
  rowHeight: number
}

interface NavyTableProps {
  columns: TableColumn[]
  rows: TableRow[]
  geo: Pick<TableGeometry, 'width' | 'headerHeight' | 'rowHeight'>
}

const BORDER = 2.5
/** Light separators between cells (literal class strings so Tailwind picks them up). */
const COL_SEP = 'border-l border-l-[#ddd6c2]'
const ROW_SEP = '[&>td]:border-t [&>td]:border-t-[#ddd6c2]'

/** Navy-framed rounded table: navy header strip, cream body with rounded inner corners. */
export function NavyTable({ columns, rows, geo }: NavyTableProps) {
  const cols: DataColumn<TableRow>[] = columns.map((c, ci) => ({
    key: c.key,
    header: c.header,
    width: c.width,
    render: (row) =>
      row[c.key].map((line) => (
        <span key={line} className="block">
          {line}
        </span>
      )),
    cellClassName: ci > 0 ? COL_SEP : undefined,
  }))
  const vars = {
    width: geo.width,
    background: library.navy,
    padding: `0 ${BORDER}px ${BORDER}px`,
    '--hh': `${geo.headerHeight}px`,
    '--rh': `${geo.rowHeight}px`,
    '--cream': library.cream,
    '--ink': library.ink,
  } as CSSProperties
  return (
    <div
      className="box-border rounded-[16px] [&_tbody_td]:h-[var(--rh)] [&_tbody_td]:bg-[var(--cream)] [&_tbody_tr:first-child_td:first-child]:rounded-tl-[13px] [&_tbody_tr:first-child_td:last-child]:rounded-tr-[13px] [&_tbody_tr:last-child_td:first-child]:rounded-bl-[13px] [&_tbody_tr:last-child_td:last-child]:rounded-br-[13px] [&_thead_th]:h-[var(--hh)]"
      style={vars}
    >
      <DataTable
        columns={cols}
        rows={rows}
        className="table-fixed !border-separate border-spacing-0"
        headCellClassName="p-0 text-[13px] font-semibold text-white"
        rowClassName={(_, i) => (i > 0 ? ROW_SEP : '')}
        cellClassName="p-0 align-middle text-[13px] font-semibold leading-[22px] tracking-[-0.01em] text-[var(--ink)]"
      />
    </div>
  )
}
